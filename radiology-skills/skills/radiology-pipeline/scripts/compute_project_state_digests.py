#!/usr/bin/env python3
"""Generate or verify canonical analysis-lock, modality-role and project-state digests."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path


SHA_RE = re.compile(r"^[0-9a-f]{64}$")
CURRENT_SCHEMA_VERSION = "1.3"
AUTO_MIGRATABLE_SCHEMA_VERSIONS = {"1.2"}


def canonical_analysis_lock_digest(analysis_lock: object) -> str:
    encoded = json.dumps(
        analysis_lock, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def canonical_modality_role_object(state: dict[str, object]) -> dict[str, object]:
    research_scope = state.get("research_scope") or {}
    if not isinstance(research_scope, dict):
        raise ValueError("research_scope must be an object")
    role_fields = {
        "active": "active_modalities",
        "external_reference": "external_reference_modalities",
        "generated_or_predicted": "generated_or_predicted_modalities",
        "proposed_validation": "proposed_validation_modalities",
    }
    roles: dict[str, list[str]] = {}
    for canonical_name, state_name in role_fields.items():
        values = research_scope.get(state_name)
        if not isinstance(values, list) or any(not isinstance(value, str) for value in values):
            raise ValueError(f"research_scope.{state_name} must be a string list")
        roles[canonical_name] = sorted(values)
    return {
        "schema_version": state.get("schema_version"),
        "study_id": state.get("study_id"),
        "study_scope": research_scope.get("study_scope"),
        "modality_roles": roles,
    }


def canonical_modality_role_digest(state: dict[str, object]) -> str:
    encoded = json.dumps(
        canonical_modality_role_object(state), ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def canonical_project_state_digest(state: dict[str, object]) -> str:
    semantic = dict(state)
    semantic.pop("project_state_digest", None)
    encoded = json.dumps(
        semantic, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def computed_digests(state: dict[str, object]) -> dict[str, str]:
    working = dict(state)
    analysis_digest = canonical_analysis_lock_digest(working.get("analysis_lock"))
    working["analysis_lock_digest"] = analysis_digest
    modality_digest = canonical_modality_role_digest(working)
    working["modality_role_digest"] = modality_digest
    project_digest = canonical_project_state_digest(working)
    return {
        "analysis_lock_digest": analysis_digest,
        "modality_role_digest": modality_digest,
        "project_state_digest": project_digest,
    }


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_state_and_refresh_manifest(path: Path, payload: dict[str, object]) -> bool:
    """Write state and refresh its unique artifact-manifest binding when present."""
    manifest_path = path.parent / "artifact_manifest.csv"
    manifest_headers: list[str] = []
    manifest_rows: list[dict[str, str]] = []
    bound_index: int | None = None
    if manifest_path.is_file():
        with manifest_path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            manifest_headers = list(reader.fieldnames or [])
            manifest_rows = [dict(row) for row in reader]
        if "path" not in manifest_headers or "sha256" not in manifest_headers:
            raise ValueError("artifact_manifest.csv must contain path and sha256 columns")
        project_root = path.parent.parent.resolve()
        matching: list[int] = []
        for index, row in enumerate(manifest_rows):
            relative = Path((row.get("path") or "").strip())
            if not str(relative) or relative.is_absolute() or ".." in relative.parts:
                continue
            candidate = (project_root / relative).resolve(strict=False)
            if candidate == path.resolve():
                matching.append(index)
        if len(matching) != 1:
            raise ValueError(
                "artifact_manifest.csv must contain exactly one path binding for project_state.json"
            )
        bound_index = matching[0]

    rendered = json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", newline="", dir=path.parent,
        prefix=f".{path.name}.", suffix=".tmp", delete=False,
    ) as handle:
        state_temp = Path(handle.name)
        handle.write(rendered)
    try:
        os.replace(state_temp, path)
    finally:
        if state_temp.exists():
            state_temp.unlink()

    if bound_index is None:
        return False
    manifest_rows[bound_index]["sha256"] = sha256_file(path)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", newline="", dir=manifest_path.parent,
        prefix=f".{manifest_path.name}.", suffix=".tmp", delete=False,
    ) as handle:
        manifest_temp = Path(handle.name)
        writer = csv.DictWriter(handle, fieldnames=manifest_headers)
        writer.writeheader()
        writer.writerows(manifest_rows)
    try:
        os.replace(manifest_temp, manifest_path)
    finally:
        if manifest_temp.exists():
            manifest_temp.unlink()
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_state", help="Path to project_state.json")
    parser.add_argument("--write", action="store_true", help="Write all three canonical digests")
    parser.add_argument(
        "--migrate-to-current", action="store_true",
        help="Explicitly migrate schema 1.2 to 1.3 before writing canonical digests",
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
        print(json.dumps({"status": "FAIL", "errors": ["project state and analysis_lock must be objects"]}, indent=2))
        return 1
    schema_version = str(payload.get("schema_version") or "")
    if args.migrate_to_current and not args.write:
        print(json.dumps({
            "status": "FAIL",
            "errors": ["--migrate-to-current requires --write"],
        }, indent=2))
        return 1
    if schema_version != CURRENT_SCHEMA_VERSION:
        if args.migrate_to_current and schema_version in AUTO_MIGRATABLE_SCHEMA_VERSIONS:
            payload["schema_version"] = CURRENT_SCHEMA_VERSION
        else:
            migration = (
                "rerun with --write --migrate-to-current"
                if schema_version in AUTO_MIGRATABLE_SCHEMA_VERSIONS
                else "manual migration is required because pre-1.2 handoff semantics differ"
            )
            print(json.dumps({
                "status": "FAIL",
                "errors": [
                    f"schema_version {schema_version!r} cannot produce current receipts; {migration}"
                ],
            }, indent=2))
            return 1
    try:
        computed = computed_digests(payload)
    except (TypeError, ValueError, OverflowError) as exc:
        print(json.dumps({"status": "FAIL", "errors": [str(exc)]}, indent=2))
        return 1
    artifact_manifest_updated = False
    if args.write:
        payload.update(computed)
        try:
            artifact_manifest_updated = write_state_and_refresh_manifest(path, payload)
        except (OSError, ValueError) as exc:
            print(json.dumps({"status": "FAIL", "errors": [str(exc)]}, indent=2))
            return 1
    declared = {field: payload.get(field) for field in computed}
    errors = [
        f"{field} does not match canonical content"
        for field, value in computed.items()
        if declared.get(field) != value or not isinstance(declared.get(field), str)
        or not SHA_RE.fullmatch(str(declared.get(field)))
    ]
    report = {
        "status": "PASS" if not errors else "FAIL",
        "project_state": str(path),
        "declared": declared,
        "computed": computed,
        "schema_version": payload.get("schema_version"),
        "migrated_from": schema_version if schema_version != payload.get("schema_version") else None,
        "artifact_manifest_updated": artifact_manifest_updated,
        "errors": errors,
        "boundary": "Canonical identity receipts only; no scientific-validity or submission-readiness certificate",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
