#!/usr/bin/env python3
"""Compute or verify the canonical digest of project_state.analysis_lock."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from compute_project_state_digests import (
    canonical_analysis_lock_digest,
    computed_digests,
    write_state_and_refresh_manifest,
)


def canonical_digest(analysis_lock: object) -> str:
    return canonical_analysis_lock_digest(analysis_lock)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_state", help="Path to project_state.json")
    parser.add_argument(
        "--write", action="store_true",
        help="Write the computed digest to top-level analysis_lock_digest",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.project_state).expanduser().resolve()
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "errors": [str(exc)]}, indent=2))
        return 1
    if not isinstance(payload, dict) or not isinstance(payload.get("analysis_lock"), dict):
        print(json.dumps({"status": "FAIL", "errors": ["analysis_lock must be an object"]}, indent=2))
        return 1
    if payload.get("schema_version") != "1.3":
        print(json.dumps({
            "status": "FAIL",
            "errors": [
                "legacy schema requires compute_project_state_digests.py --write "
                "--migrate-to-current; pre-1.2 schemas require manual handoff migration"
            ],
        }, indent=2))
        return 1
    try:
        computed = computed_digests(payload)
    except (TypeError, ValueError, OverflowError) as exc:
        print(json.dumps({"status": "FAIL", "errors": [str(exc)]}, indent=2))
        return 1
    declared = {field: payload.get(field) for field in computed}
    if args.write:
        payload.update(computed)
        try:
            manifest_updated = write_state_and_refresh_manifest(path, payload)
        except (OSError, ValueError) as exc:
            print(json.dumps({"status": "FAIL", "errors": [str(exc)]}, indent=2))
            return 1
        declared = dict(computed)
    else:
        manifest_updated = False
    status = "PASS" if declared == computed else "FAIL"
    print(json.dumps({
        "status": status,
        "project_state": str(path),
        "declared": declared,
        "computed": computed,
        "artifact_manifest_updated": manifest_updated,
        "boundary": "Canonical analysis-lock, modality-role and project-state identity receipts only; no scientific-validity certification",
    }, indent=2))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
