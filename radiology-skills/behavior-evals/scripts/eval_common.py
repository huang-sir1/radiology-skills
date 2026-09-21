#!/usr/bin/env python3
"""Shared hashing/JSON helpers for the behavior-eval harness.

Single source for the byte-identical helpers used by both
`validate_behavior_eval_assets.py` and `build_behavior_eval_receipt.py`.
Digest semantics here are release-relevant: change them only with a receipt refresh.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


HARNESS_REQUIRED_FILES = {
    "cases.json",
    "rubric.md",
    "behavior-eval-receipt.schema.json",
    "run-observation.template.json",
    "improvement-candidate.template.json",
    "human-adjudication.template.json",
}
SKILL_ID_RE = re.compile(r"^radiology-[a-z0-9-]+$")


def reject_duplicate_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


def load_unique_json(path: Path) -> object:
    return json.loads(
        path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_pairs,
    )


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def skill_tree_snapshot(skill_path: Path) -> dict[str, object]:
    entries: list[dict[str, object]] = []
    for path in sorted(skill_path.rglob("*"), key=lambda item: item.as_posix().lower()):
        if not path.is_file() or "__pycache__" in path.parts or path.suffix.lower() in {".pyc", ".pyo"}:
            continue
        entries.append({
            "path": path.relative_to(skill_path).as_posix(),
            "size": path.stat().st_size,
            "sha256": sha256_file(path),
        })
    return {
        "file_count": len(entries),
        "tree_sha256": sha256_bytes(json.dumps(
            entries, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
        ).encode("utf-8")),
    }


def evaluation_harness_snapshot(harness_root: Path) -> dict[str, object]:
    """Hash cases, rubric, receipt schema, all templates and the complete scripts tree."""
    missing = sorted(
        relative for relative in HARNESS_REQUIRED_FILES
        if not (harness_root / relative).is_file()
    )
    if missing:
        raise ValueError("evaluation harness missing required files: " + ", ".join(missing))
    selected = {harness_root / relative for relative in HARNESS_REQUIRED_FILES}
    selected.update(harness_root.glob("*.template.json"))
    scripts_root = harness_root / "scripts"
    if not scripts_root.is_dir():
        raise ValueError("evaluation harness scripts directory is missing")
    selected.update(path for path in scripts_root.rglob("*") if path.is_file())
    entries: list[dict[str, object]] = []
    for path in sorted(selected, key=lambda item: item.as_posix().lower()):
        if "__pycache__" in path.parts or path.suffix.lower() in {".pyc", ".pyo"}:
            continue
        entries.append({
            "path": path.relative_to(harness_root).as_posix(),
            "size": path.stat().st_size,
            "sha256": sha256_file(path),
        })
    return {
        "file_count": len(entries),
        "tree_sha256": sha256_bytes(json.dumps(
            entries, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
        ).encode("utf-8")),
    }
