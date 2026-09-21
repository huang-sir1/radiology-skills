#!/usr/bin/env python3
"""Validate or write the canonical scientific-prereview receipt digest."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from pathlib import Path


SCHEMA_VERSION = "1.2"
SCOPES = {"imaging-only", "mechanism-only", "imaging-mechanism", "evidence-synthesis"}
ROUTES = {"imaging-panel", "mechanism-review", "combined", "evidence-synthesis-review"}
SCOPE_ROUTE = {
    "imaging-only": "imaging-panel",
    "mechanism-only": "mechanism-review",
    "imaging-mechanism": "combined",
    "evidence-synthesis": "evidence-synthesis-review",
}
PREREVIEW_STATES = {
    "SCIENTIFIC_PREREVIEW_PASS",
    "SCIENTIFIC_PREREVIEW_CONDITIONAL",
    "SCIENTIFIC_PREREVIEW_FAIL",
}
VERIFICATION_STATES = {"VERIFIED", "PARTIAL", "NOT_VERIFIED", "MADE_WORSE", "NOT_APPLICABLE"}
PRIOR_STATES = VERIFICATION_STATES | {"not-applicable"}
SOURCE_REVIEW_STATES = {
    "VERIFIED", "PARTIAL", "NOT ADDRESSED", "MADE WORSE", "NOT VERIFIABLE", "NOT_VERIFIED",
}
SEVERITIES = {"P0", "P1", "P2"}
REVIEWER_ROLES = {
    "clinical", "methods-statistics", "imaging-reproducibility", "mechanism",
    "evidence-synthesis", "editor-synthesis",
}
EVIDENCE_SYNTHESIS_ARTIFACT_ROLES = {
    "protocol", "search", "selection-flow", "extraction",
    "risk-of-bias-applicability", "synthesis", "certainty",
}
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
PLACEHOLDER_RE = re.compile(r"(?:AUTHOR_INPUT_NEEDED|TODO|TBD|TO CONFIRM)", re.I)


def valid_sha(value: object) -> bool:
    return isinstance(value, str) and bool(SHA_RE.fullmatch(value)) and value != "0" * 64


def canonical_digest(payload: dict[str, object]) -> str:
    semantic = dict(payload)
    semantic.pop("scientific_prereview_receipt_digest", None)
    encoded = json.dumps(
        semantic, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def locator_binds_registered_artifact(value: object, artifact_ids: set[str]) -> bool:
    if not nonempty(value):
        return False
    locator = str(value)
    return any(
        locator.startswith(f"{artifact_id}:")
        and bool(locator[len(artifact_id) + 1:].strip())
        for artifact_id in artifact_ids
    )


def walk(value: object):
    if isinstance(value, dict):
        for item in value.values():
            yield from walk(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk(item)
    else:
        yield value


def validate(payload: object) -> dict[str, object]:
    errors: list[str] = []
    if not isinstance(payload, dict):
        return {"status": "FAIL", "errors": ["receipt root must be an object"]}
    required = {
        "schema_version", "receipt_id", "project_id", "manuscript_id", "study_scope",
        "review_route", "project_state_digest", "modality_role_digest", "analysis_lock_digest",
        "claim_registry_digest",
        "scientific_handoff_digest", "source_artifacts", "findings", "reviewer_roles",
        "reviewed_on", "unresolved_placeholder_count", "scientific_prereview_state",
        "scientific_prereview_receipt_digest",
    }
    missing = sorted(required - payload.keys())
    if missing:
        errors.append("missing top-level fields: " + ", ".join(missing))
    if payload.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION}")
    for field in ("receipt_id", "project_id", "manuscript_id", "reviewed_on"):
        if not nonempty(payload.get(field)):
            errors.append(f"{field} is required")

    scope = payload.get("study_scope")
    route = payload.get("review_route")
    if scope not in SCOPES:
        errors.append("study_scope is invalid")
    if route not in ROUTES:
        errors.append("review_route is invalid")
    elif scope in SCOPE_ROUTE and route != SCOPE_ROUTE[scope]:
        errors.append(f"review_route must be {SCOPE_ROUTE[scope]} for {scope}")
    for field in (
        "project_state_digest", "modality_role_digest", "analysis_lock_digest",
        "claim_registry_digest",
    ):
        if not valid_sha(payload.get(field)):
            errors.append(f"{field} must be a nonzero lowercase SHA-256")
    handoff_digest = payload.get("scientific_handoff_digest")
    if handoff_digest != "not-applicable" and not valid_sha(handoff_digest):
        errors.append("scientific_handoff_digest must be nonzero SHA-256 or not-applicable")
    if scope in {"mechanism-only", "imaging-mechanism"} and not valid_sha(handoff_digest):
        errors.append("mechanism-bearing scope requires a scientific_handoff_digest SHA-256")
    if scope == "evidence-synthesis" and handoff_digest != "not-applicable":
        errors.append("evidence-synthesis scope must not require a radiogenomics scientific_handoff_digest")

    roles = payload.get("reviewer_roles")
    if not isinstance(roles, list) or not roles or any(role not in REVIEWER_ROLES for role in roles):
        errors.append("reviewer_roles must be a non-empty controlled list")
        roles = []
    elif len(roles) != len(set(roles)):
        errors.append("reviewer_roles contains duplicates")
    if route == "imaging-panel" and "imaging-reproducibility" not in roles:
        errors.append("imaging-panel requires the imaging-reproducibility reviewer role")
    if route == "mechanism-review" and "mechanism" not in roles:
        errors.append("mechanism-review requires the mechanism reviewer role")
    if route == "combined" and not {"imaging-reproducibility", "mechanism"}.issubset(set(roles)):
        errors.append("combined review requires imaging-reproducibility and mechanism roles")
    if route == "evidence-synthesis-review" and "evidence-synthesis" not in roles:
        errors.append("evidence-synthesis-review requires the evidence-synthesis reviewer role")

    artifacts = payload.get("source_artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        errors.append("source_artifacts must be a non-empty list")
        artifacts = []
    artifact_registry: dict[str, str] = {}
    artifact_roles: set[str] = set()
    for index, item in enumerate(artifacts):
        if not isinstance(item, dict):
            errors.append(f"source_artifacts[{index}] must be an object")
            continue
        for field in ("artifact_id", "role", "version"):
            if not nonempty(item.get(field)):
                errors.append(f"source_artifacts[{index}].{field} is required")
        if nonempty(item.get("role")):
            artifact_roles.add(str(item.get("role")))
        artifact_id = item.get("artifact_id")
        if nonempty(artifact_id):
            if artifact_id in artifact_registry:
                errors.append(f"duplicate source artifact id: {artifact_id}")
            artifact_registry[str(artifact_id)] = str(item.get("sha256") or "")
        if not valid_sha(item.get("sha256")):
            errors.append(f"source_artifacts[{index}].sha256 must be nonzero lowercase SHA-256")
    if scope == "evidence-synthesis":
        missing_roles = sorted(EVIDENCE_SYNTHESIS_ARTIFACT_ROLES - artifact_roles)
        if missing_roles:
            errors.append(
                "evidence-synthesis source_artifacts missing frozen roles: " + ", ".join(missing_roles)
            )

    findings = payload.get("findings")
    if not isinstance(findings, list):
        errors.append("findings must be a list")
        findings = []
    finding_ids: set[str] = set()
    for index, item in enumerate(findings):
        if not isinstance(item, dict):
            errors.append(f"findings[{index}] must be an object")
            continue
        required_fields = {
            "finding_id", "severity", "criterion", "affected_claim_ids", "source_artifact_id",
            "source_artifact_sha256", "evidence_anchor", "minimum_repair",
            "repair_owner", "closure_evidence_required", "next_gate", "source_review_state", "prior_verification_state",
            "verification_state",
            "verification_evidence_locator", "state_change_evidence", "residual_boundary",
            "required_for_pass", "not_applicable_reason",
        }
        absent = sorted(required_fields - item.keys())
        if absent:
            errors.append(f"findings[{index}] missing fields: " + ", ".join(absent))
        finding_id = item.get("finding_id")
        if not nonempty(finding_id):
            errors.append(f"findings[{index}].finding_id is required")
        elif finding_id in finding_ids:
            errors.append(f"duplicate finding_id: {finding_id}")
        else:
            finding_ids.add(str(finding_id))
        if item.get("severity") not in SEVERITIES:
            errors.append(f"findings[{index}].severity is invalid")
        if item.get("source_review_state") not in SOURCE_REVIEW_STATES:
            errors.append(f"findings[{index}].source_review_state is invalid")
        for field in (
            "criterion", "evidence_anchor", "minimum_repair", "repair_owner",
            "closure_evidence_required", "next_gate", "residual_boundary",
        ):
            if not nonempty(item.get(field)):
                errors.append(f"findings[{index}].{field} is required")
        claim_ids = item.get("affected_claim_ids")
        if not isinstance(claim_ids, list) or not claim_ids or any(not nonempty(value) for value in claim_ids):
            errors.append(f"findings[{index}].affected_claim_ids must be non-empty")
        source_artifact_id = str(item.get("source_artifact_id") or "")
        if source_artifact_id not in artifact_registry:
            errors.append(f"findings[{index}].source_artifact_id is not registered")
        elif item.get("source_artifact_sha256") != artifact_registry[source_artifact_id]:
            errors.append(f"findings[{index}].source_artifact_sha256 differs from artifact registry")
        prior_state = item.get("prior_verification_state")
        current_state = item.get("verification_state")
        if prior_state not in PRIOR_STATES:
            errors.append(f"findings[{index}].prior_verification_state is invalid")
        if current_state not in VERIFICATION_STATES:
            errors.append(f"findings[{index}].verification_state is invalid")
        if not isinstance(item.get("required_for_pass"), bool):
            errors.append(f"findings[{index}].required_for_pass must be boolean")
        elif item.get("severity") in {"P0", "P1"} and item.get("required_for_pass") is not True:
            errors.append(f"findings[{index}] P0/P1 must set required_for_pass=true")
        if current_state in {"VERIFIED", "PARTIAL"}:
            if not nonempty(item.get("verification_evidence_locator")) or not nonempty(item.get("state_change_evidence")):
                errors.append(f"findings[{index}] verified/partial state requires closure and state-change evidence")
            elif not locator_binds_registered_artifact(
                item.get("verification_evidence_locator"), set(artifact_registry)
            ):
                errors.append(
                    f"findings[{index}].verification_evidence_locator must use "
                    "<registered artifact_id>:<locator>"
                )
        if prior_state == "NOT_VERIFIED" and current_state in {"VERIFIED", "PARTIAL"} and (
            not nonempty(item.get("verification_evidence_locator"))
            or not nonempty(item.get("state_change_evidence"))
        ):
            errors.append(f"findings[{index}] cannot upgrade NOT_VERIFIED without new bound evidence")
        if current_state == "NOT_APPLICABLE" and not nonempty(item.get("not_applicable_reason")):
            errors.append(f"findings[{index}] NOT_APPLICABLE requires a criterion-linked rationale")
        if prior_state == "NOT_VERIFIED" and current_state == "NOT_APPLICABLE":
            errors.append(
                f"findings[{index}] cannot convert prior NOT_VERIFIED to NOT_APPLICABLE"
            )

    prereview_state = payload.get("scientific_prereview_state")
    if prereview_state not in PREREVIEW_STATES:
        errors.append("scientific_prereview_state is invalid")
    unresolved = payload.get("unresolved_placeholder_count")
    if isinstance(unresolved, bool) or not isinstance(unresolved, int) or unresolved < 0:
        errors.append("unresolved_placeholder_count must be a non-negative integer")
    if prereview_state in {"SCIENTIFIC_PREREVIEW_CONDITIONAL", "SCIENTIFIC_PREREVIEW_FAIL"} and not findings:
        errors.append("CONDITIONAL/FAIL prereview requires at least one frozen finding")
    if prereview_state == "SCIENTIFIC_PREREVIEW_PASS":
        if unresolved != 0:
            errors.append("SCIENTIFIC_PREREVIEW_PASS requires zero unresolved placeholders")
        for index, item in enumerate(findings):
            if isinstance(item, dict) and item.get("required_for_pass") is True and item.get("verification_state") not in {"VERIFIED", "NOT_APPLICABLE"}:
                errors.append(f"required findings[{index}] is not verified and blocks SCIENTIFIC_PREREVIEW_PASS")
        if any(isinstance(value, str) and PLACEHOLDER_RE.search(value) for value in walk(payload)):
            errors.append("SCIENTIFIC_PREREVIEW_PASS cannot contain placeholder text")

    try:
        computed = canonical_digest(payload)
    except (TypeError, ValueError, OverflowError) as exc:
        errors.append(f"receipt cannot be canonicalized: {exc}")
        computed = ""
    declared = payload.get("scientific_prereview_receipt_digest")
    if not valid_sha(declared):
        errors.append("scientific_prereview_receipt_digest must be a nonzero lowercase SHA-256")
    elif computed and declared != computed:
        errors.append("scientific_prereview_receipt_digest does not match canonical receipt content")
    if any(isinstance(value, float) and not math.isfinite(value) for value in walk(payload)):
        errors.append("receipt contains a non-finite number")
    return {
        "status": "PASS" if not errors else "FAIL",
        "scientific_prereview_state": prereview_state,
        "computed_scientific_prereview_receipt_digest": computed,
        "findings": len(findings),
        "source_artifacts": len(artifacts),
        "errors": errors,
        "boundary": "Receipt identity and closure-contract validation only; no scientific-truth, upload-readiness or acceptance certificate",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", help="Scientific prereview receipt JSON")
    parser.add_argument("--write-digest", action="store_true")
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
        try:
            payload["scientific_prereview_receipt_digest"] = canonical_digest(payload)
            path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        except (OSError, TypeError, ValueError, OverflowError) as exc:
            print(json.dumps({"status": "FAIL", "errors": [str(exc)]}, indent=2))
            return 1
    report = validate(payload)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
