#!/usr/bin/env python3
"""Validate prereview authorization and sharing gates without conflating them."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


SCHEMA_VERSION = "1.0"
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
APPLICABILITY = {"APPLICABLE", "NOT_APPLICABLE_LOCAL_OWNER_CONFIRMED"}
ETHICS_STATES = {"DOCUMENT_VERIFIED", "UNKNOWN_AUTHOR_INPUT_NEEDED", "AUTHOR_REPORTED", "CONFLICTING"}
SHARING_STATES = {"PASS", "CONDITIONAL", "STOP", "NOT_APPLICABLE"}


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def valid_sha(value: object) -> bool:
    return isinstance(value, str) and bool(SHA_RE.fullmatch(value)) and value != "0" * 64


def canonical_digest(payload: dict[str, object]) -> str:
    semantic = dict(payload)
    semantic.pop("governance_gate_receipt_digest", None)
    encoded = json.dumps(
        semantic, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def resolve_artifact(root: Path | None, raw_path: object) -> Path | None:
    if root is None or not nonempty(raw_path):
        return None
    candidate = (root / str(raw_path)).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        return None
    return candidate


def validate(
    payload: object,
    *,
    artifact_root: Path | None = None,
    require_artifact: bool = False,
) -> dict[str, object]:
    errors: list[str] = []
    if not isinstance(payload, dict):
        return {"status": "FAIL", "errors": ["receipt root must be an object"]}

    required = {
        "schema_version", "project_id", "manuscript_id", "human_subjects_applicability",
        "ethics_receipt", "data_code_sharing_gate", "reviewed_on",
        "governance_gate_receipt_digest",
    }
    missing = sorted(required - payload.keys())
    if missing:
        errors.append("missing top-level fields: " + ", ".join(missing))
    if payload.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION}")
    for field in ("project_id", "manuscript_id", "reviewed_on"):
        if not nonempty(payload.get(field)):
            errors.append(f"{field} is required")

    applicability = payload.get("human_subjects_applicability")
    if applicability not in APPLICABILITY:
        errors.append("human_subjects_applicability is invalid")

    ethics = payload.get("ethics_receipt")
    ethics_ready = True
    artifact_verified = False
    if not isinstance(ethics, dict):
        errors.append("ethics_receipt must be an object")
        ethics = {}
        ethics_ready = False
    for field in (
        "producer", "branch", "artifact_id", "artifact_path", "artifact_version",
        "artifact_sha256", "evidence_state", "verdict", "verified_on", "local_owner",
        "activity_scope_locator", "approval_locator", "consent_or_waiver_locator",
        "data_use_authorization_locator", "non_applicability_locator", "stop_reasons",
    ):
        if field not in ethics:
            errors.append(f"ethics_receipt.{field} is required")
    if ethics.get("producer") != "radiology-ethics":
        errors.append("ethics_receipt.producer must be radiology-ethics")
        ethics_ready = False
    if ethics.get("branch") != "human-subjects":
        errors.append("ethics_receipt.branch must be human-subjects")
        ethics_ready = False
    for field in ("artifact_id", "artifact_path", "artifact_version", "verified_on", "local_owner"):
        if not nonempty(ethics.get(field)):
            errors.append(f"ethics_receipt.{field} is required")
            ethics_ready = False
    if not valid_sha(ethics.get("artifact_sha256")):
        errors.append("ethics_receipt.artifact_sha256 must be a nonzero lowercase SHA-256")
        ethics_ready = False
    if ethics.get("evidence_state") not in ETHICS_STATES:
        errors.append("ethics_receipt.evidence_state is invalid")
        ethics_ready = False
    if ethics.get("verdict") not in {"PASS", "STOP"}:
        errors.append("ethics_receipt.verdict must be PASS or STOP")
        ethics_ready = False
    if not isinstance(ethics.get("stop_reasons"), list) or any(
        not nonempty(value) for value in ethics.get("stop_reasons", [])
    ):
        errors.append("ethics_receipt.stop_reasons must be an array of non-empty strings")

    if applicability == "APPLICABLE":
        for field in (
            "activity_scope_locator", "approval_locator", "consent_or_waiver_locator",
            "data_use_authorization_locator",
        ):
            if not nonempty(ethics.get(field)):
                ethics_ready = False
        if ethics.get("evidence_state") != "DOCUMENT_VERIFIED" or ethics.get("verdict") != "PASS":
            ethics_ready = False
    elif applicability == "NOT_APPLICABLE_LOCAL_OWNER_CONFIRMED":
        if not nonempty(ethics.get("non_applicability_locator")):
            ethics_ready = False
        if ethics.get("evidence_state") != "DOCUMENT_VERIFIED" or ethics.get("verdict") != "PASS":
            ethics_ready = False

    artifact = resolve_artifact(artifact_root, ethics.get("artifact_path"))
    if artifact is not None and artifact.is_file() and valid_sha(ethics.get("artifact_sha256")):
        artifact_verified = file_sha256(artifact) == ethics.get("artifact_sha256")
        if not artifact_verified:
            errors.append("ethics receipt physical SHA-256 does not match artifact_sha256")
    elif require_artifact:
        errors.append("document-verified ethics receipt artifact is missing or outside artifact_root")
    if require_artifact and not artifact_verified:
        ethics_ready = False

    sharing = payload.get("data_code_sharing_gate")
    if not isinstance(sharing, dict):
        errors.append("data_code_sharing_gate must be an object")
        sharing = {}
    sharing_required = {
        "status", "data_availability_evidence_locator", "code_availability_evidence_locator",
        "consent_dua_consistency_locator", "residual_restrictions", "owner",
        "not_applicable_reason",
    }
    absent = sorted(sharing_required - sharing.keys())
    if absent:
        errors.append("data_code_sharing_gate missing fields: " + ", ".join(absent))
    sharing_status = sharing.get("status")
    if sharing_status not in SHARING_STATES:
        errors.append("data_code_sharing_gate.status is invalid")
    if not nonempty(sharing.get("owner")):
        errors.append("data_code_sharing_gate.owner is required")
    if sharing_status == "PASS":
        for field in (
            "data_availability_evidence_locator", "code_availability_evidence_locator",
            "consent_dua_consistency_locator",
        ):
            if not nonempty(sharing.get(field)):
                errors.append(f"data_code_sharing_gate.{field} is required for PASS")
    if sharing_status == "NOT_APPLICABLE" and not nonempty(sharing.get("not_applicable_reason")):
        errors.append("data_code_sharing_gate.not_applicable_reason is required for NOT_APPLICABLE")

    try:
        computed = canonical_digest(payload)
    except (TypeError, ValueError, OverflowError) as exc:
        errors.append(f"receipt cannot be canonicalized: {exc}")
        computed = ""
    declared = payload.get("governance_gate_receipt_digest")
    if not valid_sha(declared):
        errors.append("governance_gate_receipt_digest must be a nonzero lowercase SHA-256")
    elif computed and declared != computed:
        errors.append("governance_gate_receipt_digest does not match canonical receipt content")

    ethics_gate = "PASS" if ethics_ready else "STOP"
    if ethics_gate == "STOP" or sharing_status == "STOP":
        submission_gate = "STOP"
    elif sharing_status == "CONDITIONAL":
        submission_gate = "CONDITIONAL"
    else:
        submission_gate = "PASS"
    return {
        "status": "PASS" if not errors else "FAIL",
        "ethics_authorization_gate": ethics_gate,
        "data_code_sharing_gate": sharing_status,
        "submission_gate": submission_gate,
        "ethics_artifact_verified": artifact_verified,
        "computed_governance_gate_receipt_digest": computed,
        "errors": errors,
        "boundary": "Schema/digest and gate evaluation only; radiology-ethics and the current local owner determine authorization",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", help="Prereview governance-gates JSON")
    parser.add_argument("--artifact-root", type=Path)
    parser.add_argument("--write-digest", action="store_true")
    parser.add_argument("--require-ready", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.receipt).expanduser().resolve()
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "errors": [str(exc)]}, indent=2))
        return 1
    if args.write_digest and isinstance(payload, dict):
        payload["governance_gate_receipt_digest"] = canonical_digest(payload)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = validate(
        payload,
        artifact_root=args.artifact_root.expanduser().resolve() if args.artifact_root else None,
        require_artifact=args.require_ready,
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report["status"] != "PASS":
        return 1
    if args.require_ready and report["submission_gate"] != "PASS":
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
