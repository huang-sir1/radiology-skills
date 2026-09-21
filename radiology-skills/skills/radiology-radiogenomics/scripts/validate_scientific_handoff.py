#!/usr/bin/env python3
"""Validate the shared scientific-state interoperability packet.

This validator checks shape, controlled vocabulary and byte binding. It does not
certify that an analysis occurred or that a scientific claim is correct.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from pathlib import Path


SCHEMA_VERSION = "1.1"
SCOPES = {"imaging-only", "mechanism-only", "imaging-mechanism"}
MODALITIES = {
    "radiomics", "bulk-rna", "single-cell", "spatial", "pathology",
    "deep-fusion", "multi-omics", "other-omics", "perturbation",
}
IMAGING_MODALITIES = {"radiomics", "deep-fusion"}
MECHANISM_MODALITIES = MODALITIES - IMAGING_MODALITIES
EVIDENCE_STATES = {
    "measured", "derived", "estimated", "associated", "predicted", "perturbed",
}
CLAIM_LINK_STATES = {"direct", "inferred", "proposed"}
CLAIM_BRANCHES = {
    "technical-validity", "descriptive", "association", "localization-or-concordance",
    "prognostic-prediction", "treatment-effect", "average-treatment-effect",
    "effect-modification", "mechanistic", "causal",
}
VERDICTS = {"PASS", "CONDITIONAL", "STOP"}
HANDOFF_STATES = {
    "W-RETURN-TO-LEDGER", "W-REVISE", "W-LEDGER-READY", "W-HANDOFF-READY",
    "W-POLISH-READY",
}
TUTOR_STYLES = {"not-applicable", "provisional", "direct-expert", "guided-learning"}
MASTERY_STATES = {"unknown", "provisional", "developing", "demonstrated", "blocked"}
TUTOR_STATES = {
    "not-applicable", "T0-contract", "T1-baseline", "T2-diagnose", "T3-feedback",
    "T4-teach-back", "T5-transfer", "T6-mastery",
}
SHA_RE = re.compile(r"^[0-9a-f]{64}$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", help="Scientific handoff packet JSON")
    parser.add_argument("--require-ready", action="store_true")
    return parser.parse_args()


def canonical_digest(payload: dict[str, object]) -> str:
    semantic = dict(payload)
    semantic.pop("packet_sha256", None)
    encoded = json.dumps(
        semantic, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(payload: object, *, require_ready: bool = False) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(payload, dict):
        return {"status": "FAIL", "errors": ["packet root must be an object"], "warnings": []}

    required = {
        "schema_version", "packet_id", "study_id", "study_scope",
        "source_manifest_digest", "analysis_lock_digest", "claim_register_sha256",
        "source_artifacts", "modality_roles",
        "evidence_topology", "claims", "terminology_lock",
        "writing_handoff_status", "author_input_needed", "packet_sha256",
    }
    missing = sorted(required - payload.keys())
    if missing:
        errors.append("missing top-level fields: " + ", ".join(missing))
    if payload.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION}")
    for field in ("packet_id", "study_id"):
        if not nonempty(payload.get(field)):
            errors.append(f"{field} is required")

    scope = payload.get("study_scope")
    if scope not in SCOPES:
        errors.append(f"invalid study_scope: {scope!r}")

    manifest_digest = payload.get("source_manifest_digest")
    if not isinstance(manifest_digest, str) or not SHA_RE.fullmatch(manifest_digest):
        errors.append("source_manifest_digest must be 64 lowercase hex characters")
    for field in ("analysis_lock_digest", "claim_register_sha256"):
        digest = payload.get(field)
        if not isinstance(digest, str) or not SHA_RE.fullmatch(digest):
            errors.append(f"{field} must be 64 lowercase hex characters")

    artifacts = payload.get("source_artifacts")
    artifact_ids: set[str] = set()
    if not isinstance(artifacts, list) or not artifacts:
        errors.append("source_artifacts must be a non-empty list")
        artifacts = []
    for index, item in enumerate(artifacts):
        if not isinstance(item, dict):
            errors.append(f"source_artifacts[{index}] must be an object")
            continue
        artifact_id = item.get("artifact_id")
        if not nonempty(artifact_id):
            errors.append(f"source_artifacts[{index}].artifact_id is required")
        elif artifact_id in artifact_ids:
            errors.append(f"duplicate source artifact id: {artifact_id}")
        else:
            artifact_ids.add(str(artifact_id))
        if not nonempty(item.get("version")):
            errors.append(f"source_artifacts[{index}].version is required")
        digest = item.get("sha256")
        if not isinstance(digest, str) or not SHA_RE.fullmatch(digest):
            errors.append(f"source_artifacts[{index}].sha256 is invalid")

    roles = payload.get("modality_roles")
    active: set[str] = set()
    role_memberships: dict[str, list[str]] = {}
    if not isinstance(roles, dict):
        errors.append("modality_roles must be an object")
    else:
        expected_roles = {
            "active", "external_reference", "generated_or_predicted", "proposed_validation",
        }
        if set(roles) != expected_roles:
            errors.append("modality_roles must contain exactly: " + ", ".join(sorted(expected_roles)))
        for role in sorted(expected_roles):
            values = roles.get(role)
            if not isinstance(values, list) or any(value not in MODALITIES for value in values):
                errors.append(f"modality_roles.{role} contains invalid values")
                continue
            if len(values) != len(set(values)):
                errors.append(f"modality_roles.{role} contains duplicates")
            for value in values:
                role_memberships.setdefault(value, []).append(role)
            if role == "active":
                active = set(values)
        for modality, memberships in sorted(role_memberships.items()):
            if len(memberships) > 1:
                errors.append(
                    f"modality {modality!r} appears in multiple role groups: "
                    + ", ".join(memberships)
                )
        if not active:
            errors.append("modality_roles.active cannot be empty")
        if scope == "imaging-only" and active - IMAGING_MODALITIES:
            errors.append("imaging-only cannot have active mechanism modalities")
        if scope == "mechanism-only" and active & IMAGING_MODALITIES:
            errors.append("mechanism-only cannot have active imaging/fusion modalities")
        if scope == "imaging-mechanism":
            if not active & IMAGING_MODALITIES or not active & MECHANISM_MODALITIES:
                errors.append("imaging-mechanism requires active imaging and mechanism modalities")

    topology = payload.get("evidence_topology")
    if not isinstance(topology, dict):
        errors.append("evidence_topology must be an object")
        topology = {}
    if not nonempty(topology.get("independent_unit")):
        errors.append("evidence_topology.independent_unit is required")
    hierarchy = topology.get("biological_hierarchy")
    if not isinstance(hierarchy, list) or not hierarchy or any(not nonempty(item) for item in hierarchy):
        errors.append("evidence_topology.biological_hierarchy must be a non-empty string list")
    intersections = topology.get("matched_intersections")
    if not isinstance(intersections, list) or not intersections:
        errors.append("evidence_topology.matched_intersections must be non-empty")
        intersections = []
    normalized_intersections: list[dict[str, object]] = []
    for index, item in enumerate(intersections):
        if not isinstance(item, dict):
            errors.append(f"matched_intersections[{index}] must be an object")
            continue
        for field in ("analysis_id", "unit", "definition", "source_artifact_id"):
            if not nonempty(item.get(field)):
                errors.append(f"matched_intersections[{index}].{field} is required")
        if item.get("source_artifact_id") not in artifact_ids:
            errors.append(f"matched_intersections[{index}] references an unknown source artifact")
        n_value = item.get("n")
        na_reason = item.get("not_applicable_reason")
        if isinstance(n_value, bool) or (
            n_value is not None and (not isinstance(n_value, int) or n_value < 1)
        ):
            errors.append(f"matched_intersections[{index}].n must be a positive integer or null")
        if n_value is None and not nonempty(na_reason):
            errors.append(f"matched_intersections[{index}] needs n or not_applicable_reason")
        if n_value is not None and nonempty(na_reason):
            errors.append(f"matched_intersections[{index}] cannot have both n and not_applicable_reason")
        normalized_intersections.append(item)

    claims = payload.get("claims")
    claim_ids: set[str] = set()
    if not isinstance(claims, list) or not claims:
        errors.append("claims must be a non-empty list")
        claims = []
    for index, claim in enumerate(claims):
        if not isinstance(claim, dict):
            errors.append(f"claims[{index}] must be an object")
            continue
        claim_id = claim.get("claim_id")
        if not nonempty(claim_id):
            errors.append(f"claims[{index}].claim_id is required")
        elif claim_id in claim_ids:
            errors.append(f"duplicate claim_id: {claim_id}")
        else:
            claim_ids.add(str(claim_id))
        for field in (
            "claim_text", "modality_subtype", "independent_unit", "effect_uncertainty",
            "maximum_wording", "residual_boundary",
        ):
            if not nonempty(claim.get(field)):
                errors.append(f"claims[{index}].{field} is required")
        pointers = claim.get("evidence_pointers")
        pointer_artifact_ids: set[str] = set()
        if not isinstance(pointers, list) or not pointers or any(not nonempty(item) for item in pointers):
            errors.append(f"claims[{index}].evidence_pointers must be non-empty")
        else:
            for pointer_index, pointer in enumerate(pointers):
                matches = [
                    artifact_id for artifact_id in artifact_ids
                    if str(pointer).startswith(f"{artifact_id}:")
                    and nonempty(str(pointer)[len(artifact_id) + 1:])
                ]
                if not matches:
                    errors.append(
                        f"claims[{index}].evidence_pointers[{pointer_index}] must use "
                        "<registered artifact_id>:<locator>"
                    )
                    continue
                longest = max(len(item) for item in matches)
                best = [item for item in matches if len(item) == longest]
                if len(best) != 1:
                    errors.append(
                        f"claims[{index}].evidence_pointers[{pointer_index}] is ambiguous"
                    )
                    continue
                pointer_artifact_ids.add(best[0])
        placements = claim.get("protected_placement")
        if not isinstance(placements, list) or not placements or any(not nonempty(item) for item in placements):
            errors.append(f"claims[{index}].protected_placement must be non-empty")
        evidence_state = claim.get("primary_evidence_state")
        claim_link_status = claim.get("claim_link_status")
        claim_branch = claim.get("claim_branch")
        branch_verdict = claim.get("branch_verdict")
        if evidence_state not in EVIDENCE_STATES:
            errors.append(f"claims[{index}].primary_evidence_state is invalid")
        if claim_link_status not in CLAIM_LINK_STATES:
            errors.append(f"claims[{index}].claim_link_status is invalid")
        if claim_branch not in CLAIM_BRANCHES:
            errors.append(f"claims[{index}].claim_branch is invalid")
        if branch_verdict not in VERDICTS:
            errors.append(f"claims[{index}].branch_verdict is invalid")
        if claim_branch in {"mechanistic", "causal"} and branch_verdict == "PASS" and (
            evidence_state not in {"measured", "perturbed"} or claim_link_status != "direct"
        ):
            errors.append(
                f"claims[{index}] cannot PASS a {claim_branch} branch with "
                f"{evidence_state}/{claim_link_status} evidence"
            )
        matched_n = claim.get("matched_n")
        if isinstance(matched_n, bool) or matched_n is not None and (
            not isinstance(matched_n, int) or matched_n < 1
        ):
            errors.append(f"claims[{index}].matched_n must be a positive integer or null")
        claim_unit = claim.get("independent_unit")
        topology_unit = topology.get("independent_unit")
        if nonempty(claim_unit) and nonempty(topology_unit) and claim_unit != topology_unit:
            errors.append(
                f"claims[{index}].independent_unit must equal evidence_topology.independent_unit"
            )
        if pointer_artifact_ids:
            linked_intersections = [
                item for item in normalized_intersections
                if item.get("source_artifact_id") in pointer_artifact_ids
            ]
            if not linked_intersections:
                errors.append(
                    f"claims[{index}] has no matched_intersection linked to its evidence artifact(s)"
                )
            else:
                matching = [
                    item for item in linked_intersections
                    if item.get("unit") == claim_unit and item.get("n") == matched_n
                ]
                if not matching:
                    errors.append(
                        f"claims[{index}] independent_unit/matched_n does not match a "
                        "matched_intersection for its evidence artifact(s)"
                    )

    terminology = payload.get("terminology_lock")
    if not isinstance(terminology, list):
        errors.append("terminology_lock must be a list")
    learner_state = payload.get("learner_state")
    if learner_state is not None:
        expected_learner_fields = {
            "interaction_style", "learning_objective", "target_decision",
            "demonstrated_level", "baseline_attempt", "misconception_ids",
            "evidence_of_understanding", "mastery_status", "current_tutor_state",
            "next_transfer_task", "support_preference", "unresolved_learner_questions",
        }
        if not isinstance(learner_state, dict):
            errors.append("learner_state must be an object when present")
        else:
            if set(learner_state) != expected_learner_fields:
                errors.append(
                    "learner_state must contain exactly: "
                    + ", ".join(sorted(expected_learner_fields))
                )
            for field in (
                "learning_objective", "target_decision", "demonstrated_level",
                "baseline_attempt", "next_transfer_task", "support_preference",
            ):
                if not nonempty(learner_state.get(field)):
                    errors.append(f"learner_state.{field} must be a non-empty string")
            for field in (
                "misconception_ids", "evidence_of_understanding",
                "unresolved_learner_questions",
            ):
                values = learner_state.get(field)
                if not isinstance(values, list) or any(not nonempty(item) for item in values):
                    errors.append(f"learner_state.{field} must be a string list")
            if learner_state.get("interaction_style") not in TUTOR_STYLES:
                errors.append("learner_state.interaction_style is invalid")
            if learner_state.get("mastery_status") not in MASTERY_STATES:
                errors.append("learner_state.mastery_status is invalid")
            if learner_state.get("current_tutor_state") not in TUTOR_STATES:
                errors.append("learner_state.current_tutor_state is invalid")
            if (
                learner_state.get("mastery_status") == "demonstrated"
                and not learner_state.get("evidence_of_understanding")
            ):
                errors.append(
                    "learner_state.mastery_status=demonstrated requires evidence_of_understanding"
                )
    status = payload.get("writing_handoff_status")
    if status not in HANDOFF_STATES:
        errors.append(f"invalid writing_handoff_status: {status!r}")
    author_input = payload.get("author_input_needed")
    if not isinstance(author_input, list):
        errors.append("author_input_needed must be a list")
        author_input = []
    if (require_ready or status == "W-HANDOFF-READY") and status != "W-HANDOFF-READY":
        errors.append("--require-ready requires writing_handoff_status=W-HANDOFF-READY")
    if status == "W-HANDOFF-READY" and author_input:
        errors.append("a ready packet cannot contain author_input_needed items")

    try:
        digest = canonical_digest(payload)
    except (TypeError, ValueError, OverflowError) as exc:
        errors.append(f"packet cannot be canonicalized: {exc}")
        digest = ""
    declared_digest = payload.get("packet_sha256")
    if not isinstance(declared_digest, str) or not SHA_RE.fullmatch(declared_digest):
        errors.append("packet_sha256 must be 64 lowercase hex characters")
    elif digest and declared_digest != digest:
        errors.append("packet_sha256 does not match canonical packet content")

    for value in _walk_numbers(payload):
        if isinstance(value, float) and not math.isfinite(value):
            errors.append("packet contains a non-finite number")
            break

    if status != "W-HANDOFF-READY":
        warnings.append("packet is not ready for shared-state scientific writing")
    return {
        "status": "PASS" if not errors else "FAIL",
        "writing_handoff_status": status,
        "computed_packet_sha256": digest,
        "claims": len(claims),
        "source_artifacts": len(artifacts),
        "errors": errors,
        "warnings": warnings,
        "boundary": "Shape and byte binding only; no scientific-validity certification",
    }


def _walk_numbers(value: object):
    if isinstance(value, dict):
        for item in value.values():
            yield from _walk_numbers(item)
    elif isinstance(value, list):
        for item in value:
            yield from _walk_numbers(item)
    elif isinstance(value, (int, float)) and not isinstance(value, bool):
        yield value


def main() -> int:
    args = parse_args()
    try:
        payload = json.loads(Path(args.packet).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 1
    report = validate(payload, require_ready=args.require_ready)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
