#!/usr/bin/env python3
"""Validate or write a canonical response-package receipt digest."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import re
from pathlib import Path


SCHEMA_VERSION = "1.1"
SCOPES = {"imaging-only", "mechanism-only", "imaging-mechanism", "evidence-synthesis"}
EVIDENCE_SYNTHESIS_ARTIFACT_ROLES = {
    "protocol", "search", "selection-flow", "extraction",
    "risk-of-bias-applicability", "synthesis", "certainty",
}
PREREVIEW_STATES = {
    "SCIENTIFIC_PREREVIEW_PASS",
    "SCIENTIFIC_PREREVIEW_CONDITIONAL",
    "SCIENTIFIC_PREREVIEW_FAIL",
}
SOURCE_STATES = {
    "VERIFIED", "PARTIAL", "NOT ADDRESSED", "MADE WORSE", "NOT VERIFIABLE",
    "NOT_VERIFIED",
}
CLOSURE_STATES = {"VERIFIED", "PARTIAL", "NOT_VERIFIED", "MADE_WORSE", "NOT_APPLICABLE"}
PACKAGE_STATES = {"READY_FOR_SUBMISSION_ASSEMBLY", "NOT_READY_FOR_SUBMISSION_ASSEMBLY"}
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
PLACEHOLDER_RE = re.compile(r"(?:AUTHOR_INPUT_NEEDED|TODO|TBD|TO CONFIRM)", re.I)
PREREVIEW_VALIDATOR_PATH = (
    Path(__file__).resolve().parents[2]
    / "radiology-prereview" / "scripts" / "validate_scientific_prereview_receipt.py"
)


def valid_sha(value: object) -> bool:
    return isinstance(value, str) and bool(SHA_RE.fullmatch(value)) and value != "0" * 64


def canonical_digest(payload: dict[str, object]) -> str:
    semantic = dict(payload)
    semantic.pop("response_package_digest", None)
    encoded = json.dumps(
        semantic, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
        allow_nan=False,
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


def validate_bound_prereview(payload: object) -> dict[str, object]:
    if not PREREVIEW_VALIDATOR_PATH.is_file():
        return {"status": "FAIL", "errors": ["scientific-prereview validator is missing"]}
    spec = importlib.util.spec_from_file_location(
        "radiology_scientific_prereview_receipt_validator", PREREVIEW_VALIDATOR_PATH,
    )
    if spec is None or spec.loader is None:
        return {"status": "FAIL", "errors": ["scientific-prereview validator cannot be loaded"]}
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate(payload)


def walk(value: object):
    if isinstance(value, dict):
        for item in value.values():
            yield from walk(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk(item)
    else:
        yield value


def validate(
    payload: object,
    source_prereview_receipt: object | None = None,
    post_prereview_receipt: object | None = None,
) -> dict[str, object]:
    errors: list[str] = []
    if not isinstance(payload, dict):
        return {"status": "FAIL", "errors": ["receipt root must be an object"]}
    required = {
        "schema_version", "response_package_id", "project_id", "manuscript_id",
        "revision_round", "study_scope", "project_state_digest", "modality_role_digest",
        "analysis_lock_digest", "claim_registry_digest",
        "scientific_handoff_digest", "source_scientific_prereview_state",
        "post_revision_scientific_prereview_state",
        "source_scientific_prereview_receipt_digest",
        "post_revision_scientific_prereview_receipt_digest", "source_review_items", "artifacts",
        "unresolved_placeholder_count", "package_status", "response_package_digest",
    }
    missing = sorted(required - payload.keys())
    if missing:
        errors.append("missing top-level fields: " + ", ".join(missing))
    if payload.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION}")
    for field in ("response_package_id", "project_id", "manuscript_id", "revision_round"):
        if not nonempty(payload.get(field)):
            errors.append(f"{field} is required")
    if payload.get("study_scope") not in SCOPES:
        errors.append("study_scope is invalid")
    for field in (
        "project_state_digest", "modality_role_digest", "analysis_lock_digest",
        "claim_registry_digest",
    ):
        if not valid_sha(payload.get(field)):
            errors.append(f"{field} must be a nonzero lowercase SHA-256")
    for field in (
        "source_scientific_prereview_receipt_digest",
        "post_revision_scientific_prereview_receipt_digest",
    ):
        if not valid_sha(payload.get(field)):
            errors.append(f"{field} must be a nonzero lowercase SHA-256")
    handoff_digest = payload.get("scientific_handoff_digest")
    if handoff_digest != "not-applicable" and (
        not valid_sha(handoff_digest)
    ):
        errors.append("scientific_handoff_digest must be SHA-256 or not-applicable")
    if payload.get("study_scope") in {"mechanism-only", "imaging-mechanism"} and not (
        valid_sha(handoff_digest)
    ):
        errors.append("mechanism-bearing scope requires a scientific_handoff_digest SHA-256")
    if payload.get("study_scope") == "evidence-synthesis" and handoff_digest != "not-applicable":
        errors.append("evidence-synthesis scope must not require a radiogenomics scientific_handoff_digest")
    source_state = payload.get("source_scientific_prereview_state")
    post_state = payload.get("post_revision_scientific_prereview_state")
    if source_state not in PREREVIEW_STATES:
        errors.append("source_scientific_prereview_state is invalid")
    if post_state not in PREREVIEW_STATES:
        errors.append("post_revision_scientific_prereview_state is invalid")

    source_receipt = (
        source_prereview_receipt if isinstance(source_prereview_receipt, dict) else None
    )
    post_receipt = post_prereview_receipt if isinstance(post_prereview_receipt, dict) else None
    source_finding_registry: dict[str, dict[str, object]] = {}
    post_finding_registry: dict[str, dict[str, object]] = {}
    if source_receipt is None:
        errors.append("source scientific-prereview receipt object is required")
    if post_receipt is None:
        errors.append("post-revision scientific-prereview receipt object is required")
    for label, receipt in (("source", source_receipt), ("post-revision", post_receipt)):
        if receipt is None:
            continue
        prereview_report = validate_bound_prereview(receipt)
        if prereview_report.get("status") != "PASS":
            for error in prereview_report.get("errors", []):
                errors.append(f"{label} scientific-prereview receipt invalid: {error}")
        for field in ("project_id", "manuscript_id", "study_scope"):
            if receipt.get(field) != payload.get(field):
                errors.append(f"{label} scientific-prereview receipt {field} differs from response")
    if source_receipt is not None:
        if source_receipt.get("scientific_prereview_receipt_digest") != payload.get(
            "source_scientific_prereview_receipt_digest"
        ):
            errors.append("source scientific-prereview receipt digest differs from response")
        if source_receipt.get("scientific_prereview_state") != source_state:
            errors.append("source scientific-prereview state differs from bound receipt")
        source_finding_registry = {
            str(item.get("finding_id")): item
            for item in source_receipt.get("findings", [])
            if isinstance(item, dict) and nonempty(item.get("finding_id"))
        }
    if post_receipt is not None:
        if post_receipt.get("scientific_prereview_receipt_digest") != payload.get(
            "post_revision_scientific_prereview_receipt_digest"
        ):
            errors.append("post-revision scientific-prereview receipt digest differs from response")
        if post_receipt.get("scientific_prereview_state") != post_state:
            errors.append("post-revision scientific-prereview state differs from bound receipt")
        for field in (
            "project_state_digest", "modality_role_digest", "analysis_lock_digest",
            "claim_registry_digest", "scientific_handoff_digest",
        ):
            if post_receipt.get(field) != payload.get(field):
                errors.append(
                    f"post-revision scientific-prereview receipt {field} differs from response"
                )
        post_finding_registry = {
            str(item.get("finding_id")): item
            for item in post_receipt.get("findings", [])
            if isinstance(item, dict) and nonempty(item.get("finding_id"))
        }
    for finding_id, source_finding in source_finding_registry.items():
        post_finding = post_finding_registry.get(finding_id)
        if post_finding is None:
            errors.append(f"source finding {finding_id!r} is missing from post-revision receipt")
            continue
        for field in ("criterion", "affected_claim_ids", "source_review_state"):
            if post_finding.get(field) != source_finding.get(field):
                errors.append(
                    f"post-revision finding {finding_id!r} immutable field {field} drifted"
                )

    items = payload.get("source_review_items")
    if not isinstance(items, list) or not items:
        errors.append("source_review_items must be a non-empty list")
        items = []
    finding_ids: set[str] = set()
    response_ids: set[str] = set()
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"source_review_items[{index}] must be an object")
            continue
        for field in (
            "finding_id", "criterion", "source_artifact_id", "source_artifact_sha256",
            "evidence_locator", "response_item_id", "closure_evidence_locator",
            "state_change_evidence", "not_applicable_reason",
        ):
            if field not in item:
                errors.append(f"source_review_items[{index}] missing {field}")
        finding_id = item.get("finding_id")
        response_id = item.get("response_item_id")
        if not nonempty(finding_id):
            errors.append(f"source_review_items[{index}].finding_id is required")
        elif finding_id in finding_ids:
            errors.append(f"duplicate finding_id: {finding_id}")
        else:
            finding_ids.add(str(finding_id))
        if not nonempty(response_id):
            errors.append(f"source_review_items[{index}].response_item_id is required")
        elif response_id in response_ids:
            errors.append(f"duplicate response_item_id: {response_id}")
        else:
            response_ids.add(str(response_id))
        claims = item.get("affected_claim_ids")
        if not isinstance(claims, list) or not claims or any(not nonempty(value) for value in claims):
            errors.append(f"source_review_items[{index}].affected_claim_ids must be non-empty")
        elif len(claims) != len(set(claims)):
            errors.append(f"source_review_items[{index}].affected_claim_ids contains duplicates")
        for field in ("criterion", "source_artifact_id", "evidence_locator"):
            if not nonempty(item.get(field)):
                errors.append(f"source_review_items[{index}].{field} is required")
        if not valid_sha(item.get("source_artifact_sha256")):
            errors.append(f"source_review_items[{index}].source_artifact_sha256 is invalid")
        item_source_state = item.get("source_review_state")
        closure_state = item.get("response_closure_state")
        if item_source_state not in SOURCE_STATES:
            errors.append(f"source_review_items[{index}].source_review_state is invalid")
        if closure_state not in CLOSURE_STATES:
            errors.append(f"source_review_items[{index}].response_closure_state is invalid")
        if not isinstance(item.get("required_for_release"), bool):
            errors.append(f"source_review_items[{index}].required_for_release must be boolean")
        if closure_state in {"VERIFIED", "PARTIAL"}:
            if not nonempty(item.get("closure_evidence_locator")) or not nonempty(item.get("state_change_evidence")):
                errors.append(f"source_review_items[{index}] verified/partial closure needs evidence and state-change basis")
        if closure_state == "NOT_APPLICABLE" and not nonempty(item.get("not_applicable_reason")):
            errors.append(f"source_review_items[{index}] NOT_APPLICABLE needs a rationale")
        if item_source_state in {"NOT ADDRESSED", "NOT VERIFIABLE", "NOT_VERIFIED"} and closure_state == "NOT_APPLICABLE":
            errors.append(
                f"source_review_items[{index}] {item_source_state} cannot be converted to NOT_APPLICABLE"
            )
        source_finding = source_finding_registry.get(str(finding_id))
        post_finding = post_finding_registry.get(str(finding_id))
        frozen_finding = source_finding or post_finding
        if frozen_finding is None:
            errors.append(
                f"source_review_items[{index}].finding_id is absent from both bound prereview receipts"
            )
        else:
            field_pairs = (
                ("criterion", "criterion"),
                ("affected_claim_ids", "affected_claim_ids"),
                ("source_review_state", "source_review_state"),
                ("source_artifact_id", "source_artifact_id"),
                ("source_artifact_sha256", "source_artifact_sha256"),
                ("evidence_locator", "evidence_anchor"),
            )
            for response_field, prereview_field in field_pairs:
                if item.get(response_field) != frozen_finding.get(prereview_field):
                    errors.append(
                        f"source_review_items[{index}].{response_field} differs from frozen finding"
                    )
            if frozen_finding.get("required_for_pass") is True and item.get(
                "required_for_release"
            ) is not True:
                errors.append(
                    f"source_review_items[{index}] cannot downgrade a required prereview finding"
                )
        if post_finding is None:
            errors.append(
                f"source_review_items[{index}].finding_id is absent from post-revision receipt"
            )
        else:
            closure_pairs = (
                ("response_closure_state", "verification_state"),
                ("closure_evidence_locator", "verification_evidence_locator"),
                ("state_change_evidence", "state_change_evidence"),
            )
            for response_field, prereview_field in closure_pairs:
                if item.get(response_field) != post_finding.get(prereview_field):
                    errors.append(
                        f"source_review_items[{index}].{response_field} differs from post-revision finding"
                    )

    expected_finding_ids = set(source_finding_registry) | set(post_finding_registry)
    omitted_finding_ids = sorted(expected_finding_ids - finding_ids)
    if omitted_finding_ids:
        errors.append(
            "bound scientific-prereview findings are missing from response: "
            + ", ".join(omitted_finding_ids)
        )

    artifacts = payload.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        errors.append("artifacts must be a non-empty list")
        artifacts = []
    artifact_ids: set[str] = set()
    for index, item in enumerate(artifacts):
        if not isinstance(item, dict):
            errors.append(f"artifacts[{index}] must be an object")
            continue
        for field in ("artifact_id", "role", "version"):
            if not nonempty(item.get(field)):
                errors.append(f"artifacts[{index}].{field} is required")
        artifact_id = item.get("artifact_id")
        if nonempty(artifact_id):
            if artifact_id in artifact_ids:
                errors.append(f"duplicate artifact_id: {artifact_id}")
            artifact_ids.add(str(artifact_id))
        if not valid_sha(item.get("sha256")):
            errors.append(f"artifacts[{index}].sha256 is invalid")

    artifact_registry = {
        str(item.get("artifact_id")): str(item.get("sha256"))
        for item in artifacts
        if isinstance(item, dict) and nonempty(item.get("artifact_id"))
    }
    if payload.get("study_scope") == "evidence-synthesis":
        artifact_roles = {
            str(item.get("role"))
            for item in artifacts
            if isinstance(item, dict) and nonempty(item.get("role"))
        }
        missing_roles = sorted(EVIDENCE_SYNTHESIS_ARTIFACT_ROLES - artifact_roles)
        if missing_roles:
            errors.append(
                "evidence-synthesis response artifacts missing frozen roles: "
                + ", ".join(missing_roles)
            )
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            continue
        source_artifact_id = str(item.get("source_artifact_id") or "")
        if source_artifact_id not in artifact_registry:
            errors.append(
                f"source_review_items[{index}].source_artifact_id is not registered in artifacts"
            )
        elif item.get("source_artifact_sha256") != artifact_registry[source_artifact_id]:
            errors.append(
                f"source_review_items[{index}].source_artifact_sha256 does not match artifacts registry"
            )
        closure_state = item.get("response_closure_state")
        if closure_state in {"VERIFIED", "PARTIAL"} and not locator_binds_registered_artifact(
            item.get("closure_evidence_locator"), set(artifact_registry)
        ):
            errors.append(
                f"source_review_items[{index}].closure_evidence_locator must use "
                "<registered artifact_id>:<locator>"
            )

    unresolved = payload.get("unresolved_placeholder_count")
    if isinstance(unresolved, bool) or not isinstance(unresolved, int) or unresolved < 0:
        errors.append("unresolved_placeholder_count must be a non-negative integer")
    package_state = payload.get("package_status")
    if package_state not in PACKAGE_STATES:
        errors.append("package_status is invalid")
    if package_state == "READY_FOR_SUBMISSION_ASSEMBLY":
        if post_state != "SCIENTIFIC_PREREVIEW_PASS":
            errors.append("READY_FOR_SUBMISSION_ASSEMBLY requires post-revision scientific prereview PASS")
        if unresolved != 0:
            errors.append("READY_FOR_SUBMISSION_ASSEMBLY requires zero unresolved placeholders")
        for index, item in enumerate(items):
            if isinstance(item, dict) and item.get("required_for_release") is True and item.get("response_closure_state") not in {"VERIFIED", "NOT_APPLICABLE"}:
                errors.append(f"required source_review_items[{index}] is not closed")
        for value in walk(payload):
            if isinstance(value, str) and PLACEHOLDER_RE.search(value):
                errors.append("READY_FOR_SUBMISSION_ASSEMBLY cannot contain placeholder text")
                break

    try:
        computed = canonical_digest(payload)
    except (TypeError, ValueError, OverflowError) as exc:
        errors.append(f"receipt cannot be canonicalized: {exc}")
        computed = ""
    declared = payload.get("response_package_digest")
    if not valid_sha(declared):
        errors.append("response_package_digest must be a nonzero lowercase SHA-256")
    elif computed and declared != computed:
        errors.append("response_package_digest does not match canonical receipt content")
    for value in walk(payload):
        if isinstance(value, float) and not math.isfinite(value):
            errors.append("receipt contains a non-finite number")
            break
    return {
        "status": "PASS" if not errors else "FAIL",
        "computed_response_package_digest": computed,
        "items": len(items),
        "artifacts": len(artifacts),
        "errors": errors,
        "boundary": "Identity and closure-contract validation only; no scientific-validity or acceptance certificate",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", help="Response package receipt JSON")
    parser.add_argument(
        "--source-prereview-receipt", required=True,
        help="Canonical source-round scientific-prereview receipt JSON",
    )
    parser.add_argument(
        "--post-prereview-receipt", required=True,
        help="Canonical post-revision scientific-prereview receipt JSON",
    )
    parser.add_argument("--write-digest", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = Path(args.receipt).expanduser().resolve()
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        source_prereview_receipt = json.loads(
            Path(args.source_prereview_receipt).expanduser().resolve().read_text(encoding="utf-8")
        )
        post_prereview_receipt = json.loads(
            Path(args.post_prereview_receipt).expanduser().resolve().read_text(encoding="utf-8")
        )
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "errors": [str(exc)]}, indent=2))
        return 1
    if args.write_digest and isinstance(payload, dict):
        try:
            payload["response_package_digest"] = canonical_digest(payload)
            path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        except (OSError, TypeError, ValueError, OverflowError) as exc:
            print(json.dumps({"status": "FAIL", "errors": [str(exc)]}, indent=2))
            return 1
    report = validate(payload, source_prereview_receipt, post_prereview_receipt)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
