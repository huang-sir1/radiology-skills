#!/usr/bin/env python3
"""Run structural and placeholder checks on a publication-table CSV."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


PLACEHOLDER_RE = re.compile(r"(?:TODO|TBD|TO CONFIRM|AUTHOR_INPUT_NEEDED|VERIFY_FROM_CURRENT_GUIDE)", re.I)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("table_csv")
    parser.add_argument("--mode", choices=("working", "submission"), default="working")
    parser.add_argument("--required-columns", default="", help="Comma-separated required column names")
    parser.add_argument("--id-column", default="", help="Column that must be unique and nonblank")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.table_csv)
    findings: list[dict[str, str]] = []
    try:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.reader(handle)
            rows = list(reader)
    except (OSError, csv.Error) as exc:
        print(json.dumps({"status": "FAIL", "findings": [{"severity": "ERROR", "message": str(exc)}]}, indent=2))
        return 1

    if not rows:
        findings.append({"severity": "ERROR", "code": "EMPTY", "message": "CSV has no rows"})
        headers: list[str] = []
    else:
        headers = [cell.strip() for cell in rows[0]]
        if any(not header for header in headers):
            findings.append({"severity": "ERROR", "code": "BLANK_HEADER", "message": "One or more headers are blank"})
        if len(set(headers)) != len(headers):
            findings.append({"severity": "ERROR", "code": "DUP_HEADER", "message": "Headers are not unique"})
        for index, row in enumerate(rows[1:], start=2):
            if len(row) != len(headers):
                findings.append({"severity": "ERROR", "code": "ROW_WIDTH", "message": f"Row {index} has {len(row)} cells; expected {len(headers)}"})
            if args.mode == "submission" and PLACEHOLDER_RE.search(" ".join(row)):
                findings.append({"severity": "ERROR", "code": "PLACEHOLDER", "message": f"Row {index} contains an unresolved placeholder"})
        if args.mode == "submission" and len(rows) == 1:
            findings.append({"severity": "ERROR", "code": "NO_DATA_ROWS", "message": "Submission table has a header but no data rows"})

    required = [item.strip() for item in args.required_columns.split(",") if item.strip()]
    for column in required:
        if column not in headers:
            findings.append({"severity": "ERROR", "code": "REQUIRED_COLUMN", "message": f"Missing required column: {column}"})

    if args.id_column:
        if args.id_column not in headers:
            findings.append({"severity": "ERROR", "code": "ID_COLUMN", "message": f"Missing ID column: {args.id_column}"})
        else:
            column_index = headers.index(args.id_column)
            seen: set[str] = set()
            for index, row in enumerate(rows[1:], start=2):
                value = row[column_index].strip() if column_index < len(row) else ""
                if not value:
                    findings.append({"severity": "ERROR", "code": "ID_BLANK", "message": f"Row {index} has blank {args.id_column}"})
                elif value in seen:
                    findings.append({"severity": "ERROR", "code": "ID_DUPLICATE", "message": f"Row {index} duplicates {value}"})
                else:
                    seen.add(value)

    errors = sum(item["severity"] == "ERROR" for item in findings)
    report = {
        "file": str(path.resolve()),
        "status": "PASS" if errors == 0 else "FAIL",
        "rows": max(len(rows) - 1, 0),
        "columns": len(headers),
        "findings": findings,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
