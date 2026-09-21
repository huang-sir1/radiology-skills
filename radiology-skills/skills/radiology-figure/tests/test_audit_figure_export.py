#!/usr/bin/env python3
"""CLI regression for the raster figure export auditor."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit_figure_export.py"


def run_audit(path: Path, *args: str) -> tuple[int, dict[str, object]]:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(path), *args],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return result.returncode, json.loads(result.stdout)


class FigureExportAuditTests(unittest.TestCase):
    def make_figure(self, root: Path, *, dpi: int = 300, background: str = "white") -> Path:
        path = root / "figure.png"
        image = Image.new("RGB", (800, 600), background)
        draw = ImageDraw.Draw(image)
        draw.rectangle((120, 90, 680, 510), fill="black")
        image.save(path, dpi=(dpi, dpi))
        return path

    def test_valid_white_300_dpi_figure_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            code, report = run_audit(self.make_figure(Path(temp)), "--require-white")
            self.assertEqual(0, code)
            self.assertEqual("PASS", report["status"])
            self.assertEqual([], [x for x in report["findings"] if x["severity"] == "ERROR"])

    def test_low_dpi_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            code, report = run_audit(self.make_figure(Path(temp), dpi=96))
            self.assertEqual(1, code)
            self.assertIn("DPI_LOW", {x.get("code") for x in report["findings"]})

    def test_blank_image_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "blank.png"
            Image.new("RGB", (300, 200), "white").save(path, dpi=(300, 300))
            code, report = run_audit(path)
            self.assertEqual(1, code)
            self.assertIn("BLANK", {x.get("code") for x in report["findings"]})

    def test_corrupt_or_missing_image_returns_machine_readable_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "not-an-image.png"
            path.write_text("not an image", encoding="utf-8")
            code, report = run_audit(path)
            self.assertEqual(1, code)
            self.assertEqual("FAIL", report["status"])
            self.assertEqual("ERROR", report["findings"][0]["severity"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
