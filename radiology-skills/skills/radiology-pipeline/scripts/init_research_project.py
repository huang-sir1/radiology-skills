#!/usr/bin/env python3
"""Initialize the lightweight research record used by radiology-pipeline."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


TEMPLATE_FILES = {
    "project_state.template.json": "project_state.json",
    "reported_values.template.csv": "reported_values.csv",
    "claim_register.template.csv": "claim_register.csv",
    "display_register.template.csv": "display_register.csv",
    "artifact_manifest.template.csv": "artifact_manifest.csv",
    "decision_log.template.csv": "decision_log.csv",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_analysis_lock_digest(analysis_lock: object) -> str:
    encoded = json.dumps(
        analysis_lock, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def canonical_modality_role_digest(state: dict[str, object]) -> str:
    research_scope = state.get("research_scope") or {}
    if not isinstance(research_scope, dict):
        research_scope = {}
    semantic = {
        "schema_version": state.get("schema_version"),
        "study_id": state.get("study_id"),
        "study_scope": research_scope.get("study_scope"),
        "modality_roles": {
            "active": sorted(research_scope.get("active_modalities") or []),
            "external_reference": sorted(research_scope.get("external_reference_modalities") or []),
            "generated_or_predicted": sorted(research_scope.get("generated_or_predicted_modalities") or []),
            "proposed_validation": sorted(research_scope.get("proposed_validation_modalities") or []),
        },
    }
    encoded = json.dumps(
        semantic, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def canonical_project_state_digest(state: dict[str, object]) -> str:
    semantic = dict(state)
    semantic.pop("project_state_digest", None)
    encoded = json.dumps(
        semantic, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", help="Project directory to initialize")
    parser.add_argument("--study-id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument(
        "--data-provenance",
        choices=("real", "simulated", "mixed"),
        default="real",
    )
    parser.add_argument("--teaching-only", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.data_provenance != "real" and not args.teaching_only:
        raise SystemExit("Simulated or mixed projects require --teaching-only.")

    project_dir = Path(args.project_dir).expanduser().resolve()
    record_dir = project_dir / "research_record"
    record_dir.mkdir(parents=True, exist_ok=True)
    assets_dir = Path(__file__).resolve().parents[1] / "assets"

    existing = [dst for dst in TEMPLATE_FILES.values() if (record_dir / dst).exists()]
    if existing:
        raise SystemExit(
            "Research record already exists; refusing to overwrite: " + ", ".join(existing)
        )

    for source_name, target_name in TEMPLATE_FILES.items():
        shutil.copyfile(assets_dir / source_name, record_dir / target_name)

    state_path = record_dir / "project_state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    state.update(
        {
            "study_id": args.study_id,
            "project_title": args.title,
            "data_provenance": args.data_provenance,
            "teaching_only": bool(args.teaching_only),
            "last_updated": now,
        }
    )
    state["analysis_lock_digest"] = canonical_analysis_lock_digest(state["analysis_lock"])
    state["modality_role_digest"] = canonical_modality_role_digest(state)
    state["project_state_digest"] = canonical_project_state_digest(state)
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    manifest_path = record_dir / "artifact_manifest.csv"
    record_artifacts = (
        ("ART-001", "project-record", "project_state.json"),
        ("ART-002", "value-registry", "reported_values.csv"),
        ("ART-003", "claim-registry", "claim_register.csv"),
        ("ART-004", "display-registry", "display_register.csv"),
        ("ART-005", "artifact-registry", "artifact_manifest.csv"),
        ("ART-006", "decision-registry", "decision_log.csv"),
    )
    with manifest_path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        for artifact_id, category, file_name in record_artifacts:
            digest = "" if file_name == "artifact_manifest.csv" else sha256_file(record_dir / file_name)
            writer.writerow(
                [
                    artifact_id,
                    category,
                    f"research_record/{file_name}",
                    "radiology-pipeline",
                    "current",
                    "1",
                    digest,
                    "",
                    "",
                    "",
                    "true",
                    now,
                    (
                        "Initialized by init_research_project.py; artifact manifest uses the "
                        "validator's detached record fingerprint instead of a self hash"
                        if file_name == "artifact_manifest.csv"
                        else "Initialized by init_research_project.py"
                    ),
                ]
            )

    print(record_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
