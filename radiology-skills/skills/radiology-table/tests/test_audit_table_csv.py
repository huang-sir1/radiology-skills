#!/usr/bin/env python3
"""CLI regression for the publication-table CSV auditor."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit_table_csv.py"


def run_audit(path: Path, *args: str) -> tuple[int, dict[str, object]]:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(path), *args],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return result.returncode, json.loads(result.stdout)


class TableCsvAuditTests(unittest.TestCase):
    def test_valid_submission_table_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "table.csv"
            path.write_text("id,estimate,ci\nA,0.72,0.68-0.76\nB,0.69,0.64-0.74\n", encoding="utf-8")
            code, report = run_audit(
                path, "--mode", "submission", "--required-columns", "id,estimate,ci",
                "--id-column", "id",
            )
            self.assertEqual(0, code)
            self.assertEqual("PASS", report["status"])

    def test_submission_placeholder_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "table.csv"
            path.write_text("id,value\nA,TBD\n", encoding="utf-8")
            code, report = run_audit(path, "--mode", "submission")
            self.assertEqual(1, code)
            self.assertIn("PLACEHOLDER", {x.get("code") for x in report["findings"]})

    def test_duplicate_id_and_row_width_fail(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "table.csv"
            path.write_text("id,value\nA,1\nA,2,extra\n", encoding="utf-8")
            code, report = run_audit(path, "--id-column", "id")
            self.assertEqual(1, code)
            codes = {x.get("code") for x in report["findings"]}
            self.assertTrue({"ID_DUPLICATE", "ROW_WIDTH"}.issubset(codes))

    def test_missing_file_returns_machine_readable_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            code, report = run_audit(Path(temp) / "missing.csv")
            self.assertEqual(1, code)
            self.assertEqual("FAIL", report["status"])
            self.assertEqual("ERROR", report["findings"][0]["severity"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
