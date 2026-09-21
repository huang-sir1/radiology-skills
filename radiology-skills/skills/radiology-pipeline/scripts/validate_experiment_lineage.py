#!/usr/bin/env python3
"""Validate an optional experiment-lineage DAG and protected-test discipline."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path


SHA_RE = re.compile(r"^[0-9a-f]{64}$")
ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{1,127}$")
BOUNDARY = "ITERATION_LINEAGE_ONLY_NOT_CAUSAL_EVIDENCE"
DECISIONS = {"PROCEED", "REFINE", "REPLICATE", "PIVOT", "STOP", "SUPERSEDE", "ABANDON"}
INTENTS = {"PRE_SPECIFIED_CONFIRMATORY", "EXPLORATORY"}
SPLIT_ROLES = {"DEVELOPMENT", "INTERNAL_VALIDATION", "CONFIRMATORY_TEST", "EXTERNAL_CONFIRMATORY_TEST"}
RESULT_STATES = {"NOT_RUN", "COMPLETED", "FAILED_EXECUTION", "VALID_NEGATIVE", "NULL_RESULT"}
LIFECYCLE_STATES = {"ACTIVE", "COMPLETED", "SUPERSEDED", "ABANDONED"}
CLAIM_STATES = {
    "NON_CLAIM_BEARING", "EXPLORATORY", "INTERNAL_VALIDATION",
    "CONFIRMATORY", "EXTERNAL_CONFIRMATORY",
}
SELECTION_BASES = {"PRE_SPECIFIED_RULE", "EXPLORATORY_PERFORMANCE_COMPARISON"}


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


def valid_sha(value: object) -> bool:
    return isinstance(value, str) and bool(SHA_RE.fullmatch(value)) and value != "0" * 64


def parse_time(value: object, label: str, errors: list[str], *, required: bool = True) -> datetime | None:
    if not isinstance(value, str) or not value:
        if required:
            errors.append(f"{label} must be an ISO-8601 timestamp")
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        errors.append(f"{label} must be an ISO-8601 timestamp")
        return None
    if parsed.tzinfo is None:
        errors.append(f"{label} must include a timezone")
        return None
    return parsed


def exact_keys(value: object, required: set[str], label: str, errors: list[str]) -> dict[str, object]:
    if not isinstance(value, dict):
        errors.append(f"{label} must be an object")
        return {}
    missing = sorted(required - set(value))
    extra = sorted(set(value) - required)
    if missing:
        errors.append(f"{label} missing fields: " + ", ".join(missing))
    if extra:
        errors.append(f"{label} has unsupported fields: " + ", ".join(extra))
    return value


def nonempty(value: object, label: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label} is required")
        return ""
    if value != value.strip() or "\n" in value or "\r" in value:
        errors.append(f"{label} must be one canonical single-line value")
    return value


def validate(payload: object) -> list[str]:
    errors: list[str] = []
    root_fields = {
        "schema_version", "lineage_id", "study_id", "created_on", "claim_boundary",
        "checkpoint_selection_policy", "experiments", "checkpoint_selections",
    }
    root = exact_keys(payload, root_fields, "lineage", errors)
    if not root:
        return errors
    if root.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    for field in ("lineage_id", "study_id"):
        value = nonempty(root.get(field), field, errors)
        if value and not ID_RE.fullmatch(value):
            errors.append(f"{field} has an invalid identifier")
    parse_time(root.get("created_on"), "created_on", errors)
    if root.get("claim_boundary") != BOUNDARY:
        errors.append("claim_boundary must preserve the non-causal lineage boundary")

    policy_fields = {"applicability", "rule", "locked_on", "artifact_sha256", "not_applicable_reason"}
    policy = exact_keys(
        root.get("checkpoint_selection_policy"), policy_fields,
        "checkpoint_selection_policy", errors,
    )
    applicability = policy.get("applicability")
    policy_locked: datetime | None = None
    if applicability == "APPLICABLE":
        nonempty(policy.get("rule"), "checkpoint_selection_policy.rule", errors)
        policy_locked = parse_time(
            policy.get("locked_on"), "checkpoint_selection_policy.locked_on", errors,
        )
        if not valid_sha(policy.get("artifact_sha256")):
            errors.append("checkpoint_selection_policy.artifact_sha256 is invalid")
        if policy.get("not_applicable_reason") not in {"", None}:
            errors.append("applicable checkpoint policy must not have not_applicable_reason")
    elif applicability == "NOT_APPLICABLE":
        nonempty(
            policy.get("not_applicable_reason"),
            "checkpoint_selection_policy.not_applicable_reason", errors,
        )
        if any(policy.get(field) not in {"", None} for field in ("rule", "locked_on", "artifact_sha256")):
            errors.append("NOT_APPLICABLE checkpoint policy must leave rule, lock and hash empty")
    else:
        errors.append("checkpoint_selection_policy.applicability is invalid")

    experiments = root.get("experiments")
    if not isinstance(experiments, list) or not experiments:
        return errors + ["experiments must be a non-empty list"]
    node_fields = {
        "experiment_id", "parent_ids", "created_on", "hypothesis", "decision",
        "analysis_intent", "intent_locked_on", "intent_lock_artifact_sha256",
        "data_identity", "split_identity", "test_access", "configuration", "artifacts",
        "result", "feedback", "branch_reason", "selection_family_id", "lifecycle_status",
        "terminal_reason", "claim_status",
    }
    nodes: dict[str, dict[str, object]] = {}
    created_times: dict[str, datetime | None] = {}
    intent_times: dict[str, datetime | None] = {}
    access_times: dict[str, datetime | None] = {}
    result_times: dict[str, datetime | None] = {}
    artifact_hashes: dict[str, set[str]] = {}

    for index, raw_node in enumerate(experiments):
        label = f"experiments[{index}]"
        node = exact_keys(raw_node, node_fields, label, errors)
        if not node:
            continue
        experiment_id = nonempty(node.get("experiment_id"), f"{label}.experiment_id", errors)
        if experiment_id and not ID_RE.fullmatch(experiment_id):
            errors.append(f"{label}.experiment_id has an invalid identifier")
        if experiment_id in nodes:
            errors.append(f"duplicate experiment_id: {experiment_id}")
        elif experiment_id:
            nodes[experiment_id] = node

        parents = node.get("parent_ids")
        if not isinstance(parents, list) or any(
            not isinstance(value, str) or not ID_RE.fullmatch(value) for value in parents
        ):
            errors.append(f"{label}.parent_ids must be a valid identifier list")
            parents = []
        elif len(parents) != len(set(parents)):
            errors.append(f"{label}.parent_ids contains duplicates")
        if experiment_id and experiment_id in parents:
            errors.append(f"{experiment_id}: parent_ids contains itself")

        created_times[experiment_id] = parse_time(node.get("created_on"), f"{label}.created_on", errors)
        nonempty(node.get("hypothesis"), f"{label}.hypothesis", errors)
        if node.get("decision") not in DECISIONS:
            errors.append(f"{label}.decision is invalid")
        intent = node.get("analysis_intent")
        if intent not in INTENTS:
            errors.append(f"{label}.analysis_intent is invalid")
        if intent == "PRE_SPECIFIED_CONFIRMATORY":
            intent_times[experiment_id] = parse_time(
                node.get("intent_locked_on"), f"{label}.intent_locked_on", errors,
            )
            if not valid_sha(node.get("intent_lock_artifact_sha256")):
                errors.append(f"{label}.intent_lock_artifact_sha256 is invalid")
        else:
            intent_times[experiment_id] = None
            if node.get("intent_locked_on") not in {"", None} or node.get("intent_lock_artifact_sha256") not in {"", None}:
                errors.append(f"{label}: exploratory intent must not carry a confirmatory intent lock")

        data = exact_keys(
            node.get("data_identity"), {"dataset_id", "manifest_sha256"},
            f"{label}.data_identity", errors,
        )
        nonempty(data.get("dataset_id"), f"{label}.data_identity.dataset_id", errors)
        if not valid_sha(data.get("manifest_sha256")):
            errors.append(f"{label}.data_identity.manifest_sha256 is invalid")

        split = exact_keys(
            node.get("split_identity"), {"split_id", "manifest_sha256", "role"},
            f"{label}.split_identity", errors,
        )
        nonempty(split.get("split_id"), f"{label}.split_identity.split_id", errors)
        if not valid_sha(split.get("manifest_sha256")):
            errors.append(f"{label}.split_identity.manifest_sha256 is invalid")
        split_role = split.get("role")
        if split_role not in SPLIT_ROLES:
            errors.append(f"{label}.split_identity.role is invalid")

        access = exact_keys(
            node.get("test_access"), {"test_id", "accessed", "access_counter", "accessed_on"},
            f"{label}.test_access", errors,
        )
        accessed = access.get("accessed")
        counter = access.get("access_counter")
        if not isinstance(accessed, bool):
            errors.append(f"{label}.test_access.accessed must be boolean")
        if isinstance(counter, bool) or not isinstance(counter, int) or counter < 0:
            errors.append(f"{label}.test_access.access_counter must be a non-negative integer")
        test_role = split_role in {"CONFIRMATORY_TEST", "EXTERNAL_CONFIRMATORY_TEST"}
        if test_role:
            nonempty(access.get("test_id"), f"{label}.test_access.test_id", errors)
            if accessed is True:
                access_times[experiment_id] = parse_time(
                    access.get("accessed_on"), f"{label}.test_access.accessed_on", errors,
                )
                if not isinstance(counter, int) or isinstance(counter, bool) or counter < 1:
                    errors.append(f"{label}: accessed confirmatory test requires counter >= 1")
            else:
                access_times[experiment_id] = None
                if counter != 0 or access.get("accessed_on") not in {"", None}:
                    errors.append(f"{label}: unaccessed confirmatory test requires counter 0 and no time")
        else:
            access_times[experiment_id] = None
            if access.get("test_id") not in {"", None} or accessed is not False or counter != 0 or access.get("accessed_on") not in {"", None}:
                errors.append(f"{label}: non-confirmatory split must not record confirmatory test access")

        config = exact_keys(
            node.get("configuration"),
            {"configuration_id", "configuration_sha256", "code_sha256", "environment_sha256"},
            f"{label}.configuration", errors,
        )
        nonempty(config.get("configuration_id"), f"{label}.configuration.configuration_id", errors)
        for field in ("configuration_sha256", "code_sha256", "environment_sha256"):
            if not valid_sha(config.get(field)):
                errors.append(f"{label}.configuration.{field} is invalid")

        artifacts = node.get("artifacts")
        hashes: set[str] = set()
        artifact_ids: set[str] = set()
        if not isinstance(artifacts, list):
            errors.append(f"{label}.artifacts must be a list")
            artifacts = []
        for artifact_index, artifact_raw in enumerate(artifacts):
            artifact_label = f"{label}.artifacts[{artifact_index}]"
            artifact = exact_keys(artifact_raw, {"artifact_id", "role", "sha256"}, artifact_label, errors)
            artifact_id = nonempty(artifact.get("artifact_id"), f"{artifact_label}.artifact_id", errors)
            nonempty(artifact.get("role"), f"{artifact_label}.role", errors)
            if artifact_id in artifact_ids:
                errors.append(f"{label}.artifacts contains duplicate artifact_id: {artifact_id}")
            artifact_ids.add(artifact_id)
            if not valid_sha(artifact.get("sha256")):
                errors.append(f"{artifact_label}.sha256 is invalid")
            else:
                hashes.add(str(artifact["sha256"]))
        artifact_hashes[experiment_id] = hashes

        result = exact_keys(
            node.get("result"),
            {"status", "recorded_on", "summary", "primary_metric_name", "primary_metric_value", "artifact_sha256"},
            f"{label}.result", errors,
        )
        result_status = result.get("status")
        if result_status not in RESULT_STATES:
            errors.append(f"{label}.result.status is invalid")
        metric_value = result.get("primary_metric_value")
        if isinstance(metric_value, bool) or (metric_value is not None and not isinstance(metric_value, (int, float))):
            errors.append(f"{label}.result.primary_metric_value must be numeric or null")
        if result_status == "NOT_RUN":
            result_times[experiment_id] = None
            if any(result.get(field) not in {"", None} for field in ("recorded_on", "summary", "primary_metric_name", "artifact_sha256")) or metric_value is not None:
                errors.append(f"{label}: NOT_RUN result must not contain result evidence")
        else:
            result_times[experiment_id] = parse_time(
                result.get("recorded_on"), f"{label}.result.recorded_on", errors,
            )
            nonempty(result.get("summary"), f"{label}.result.summary", errors)
            if not valid_sha(result.get("artifact_sha256")) or result.get("artifact_sha256") not in hashes:
                errors.append(f"{label}.result.artifact_sha256 must resolve to node artifacts")

        feedback = exact_keys(
            node.get("feedback"), {"summary", "child_experiment_ids", "artifact_sha256"},
            f"{label}.feedback", errors,
        )
        child_ids = feedback.get("child_experiment_ids")
        if not isinstance(child_ids, list) or any(not isinstance(value, str) for value in child_ids):
            errors.append(f"{label}.feedback.child_experiment_ids must be a string list")
        elif len(child_ids) != len(set(child_ids)):
            errors.append(f"{label}.feedback.child_experiment_ids contains duplicates")
        if result_status != "NOT_RUN":
            nonempty(feedback.get("summary"), f"{label}.feedback.summary", errors)
            if not valid_sha(feedback.get("artifact_sha256")) or feedback.get("artifact_sha256") not in hashes:
                errors.append(f"{label}.feedback.artifact_sha256 must resolve to node artifacts")

        branch_reason = nonempty(node.get("branch_reason"), f"{label}.branch_reason", errors)
        if parents and branch_reason == "ROOT":
            errors.append(f"{label}: child branch_reason cannot be ROOT")
        if not parents and branch_reason != "ROOT":
            errors.append(f"{label}: a root experiment requires branch_reason ROOT")
        family = node.get("selection_family_id")
        if not isinstance(family, str):
            errors.append(f"{label}.selection_family_id must be a string")
        elif family and not ID_RE.fullmatch(family):
            errors.append(f"{label}.selection_family_id is invalid")
        lifecycle = node.get("lifecycle_status")
        if lifecycle not in LIFECYCLE_STATES:
            errors.append(f"{label}.lifecycle_status is invalid")
        terminal_reason = node.get("terminal_reason")
        if lifecycle in {"SUPERSEDED", "ABANDONED"}:
            nonempty(terminal_reason, f"{label}.terminal_reason", errors)
        elif terminal_reason not in {"", None}:
            errors.append(f"{label}: terminal_reason is only for superseded or abandoned nodes")
        claim_status = node.get("claim_status")
        if claim_status not in CLAIM_STATES:
            errors.append(f"{label}.claim_status is invalid")
        if intent == "EXPLORATORY" and claim_status in {"CONFIRMATORY", "EXTERNAL_CONFIRMATORY"}:
            errors.append(f"{label}: exploratory intent cannot be relabelled confirmatory")
        expected_role = {
            "CONFIRMATORY": "CONFIRMATORY_TEST",
            "EXTERNAL_CONFIRMATORY": "EXTERNAL_CONFIRMATORY_TEST",
        }.get(str(claim_status))
        if expected_role is not None:
            if intent != "PRE_SPECIFIED_CONFIRMATORY" or split_role != expected_role:
                errors.append(f"{label}: {claim_status} requires prespecified intent and {expected_role}")
            if accessed is not True or result_status == "NOT_RUN":
                errors.append(f"{label}: {claim_status} requires one completed protected-test access")

    if not nodes:
        return errors + ["no valid experiment IDs were found"]

    children: dict[str, set[str]] = {experiment_id: set() for experiment_id in nodes}
    for experiment_id, node in nodes.items():
        for parent_id in node.get("parent_ids", []):
            if parent_id not in nodes:
                errors.append(f"{experiment_id}: orphan parent_id {parent_id}")
            else:
                children[parent_id].add(experiment_id)
    if not any(not node.get("parent_ids") for node in nodes.values()):
        errors.append("DAG requires at least one root experiment")

    state: dict[str, int] = {}

    def visit(experiment_id: str) -> None:
        if state.get(experiment_id) == 1:
            errors.append(f"DAG cycle detected at {experiment_id}")
            return
        if state.get(experiment_id) == 2:
            return
        state[experiment_id] = 1
        for parent_id in nodes[experiment_id].get("parent_ids", []):
            if parent_id in nodes:
                visit(parent_id)
        state[experiment_id] = 2

    for experiment_id in nodes:
        visit(experiment_id)

    for experiment_id, node in nodes.items():
        reported_children = node.get("feedback", {}).get("child_experiment_ids", [])
        if isinstance(reported_children, list) and set(reported_children) != children[experiment_id]:
            errors.append(f"{experiment_id}: feedback child list does not match DAG edges")

    accesses_by_test: dict[str, list[tuple[str, int, datetime | None]]] = {}
    for experiment_id, node in nodes.items():
        split_role = node.get("split_identity", {}).get("role")
        access = node.get("test_access", {})
        if split_role in {"CONFIRMATORY_TEST", "EXTERNAL_CONFIRMATORY_TEST"} and access.get("accessed") is True:
            test_id = str(access.get("test_id") or "")
            counter = access.get("access_counter")
            if test_id and isinstance(counter, int) and not isinstance(counter, bool):
                accesses_by_test.setdefault(test_id, []).append(
                    (experiment_id, counter, access_times.get(experiment_id)),
                )
    for test_id, accesses in accesses_by_test.items():
        counters = sorted(item[1] for item in accesses)
        if counters != list(range(1, len(accesses) + 1)):
            errors.append(f"test {test_id}: access counters must be unique and contiguous from 1")
        if len(accesses) > 1:
            errors.append(f"test {test_id}: confirmatory test reused across experiments")
        for experiment_id, counter, accessed_on in accesses:
            node = nodes[experiment_id]
            if counter != 1:
                errors.append(f"{experiment_id}: a confirmatory test access must be the first and only access")
            if node.get("analysis_intent") == "PRE_SPECIFIED_CONFIRMATORY":
                created_on = created_times.get(experiment_id)
                locked_on = intent_times.get(experiment_id)
                if created_on and locked_on and locked_on < created_on:
                    errors.append(f"{experiment_id}: intent lock predates node creation")
                if locked_on and accessed_on and locked_on >= accessed_on:
                    errors.append(f"{experiment_id}: confirmatory intent was not locked before test access")

    selections = root.get("checkpoint_selections")
    if not isinstance(selections, list):
        errors.append("checkpoint_selections must be a list")
        selections = []
    if applicability == "NOT_APPLICABLE" and selections:
        errors.append("checkpoint selections require an APPLICABLE checkpoint policy")
    selection_fields = {
        "selection_id", "selection_family_id", "selected_experiment_id",
        "all_attempt_experiment_ids", "selection_basis", "selected_on",
        "multiple_attempts_artifact_sha256",
    }
    seen_selection_ids: set[str] = set()
    seen_families: set[str] = set()
    for index, raw_selection in enumerate(selections):
        label = f"checkpoint_selections[{index}]"
        selection = exact_keys(raw_selection, selection_fields, label, errors)
        selection_id = nonempty(selection.get("selection_id"), f"{label}.selection_id", errors)
        family_id = nonempty(selection.get("selection_family_id"), f"{label}.selection_family_id", errors)
        if selection_id in seen_selection_ids:
            errors.append(f"duplicate checkpoint selection_id: {selection_id}")
        seen_selection_ids.add(selection_id)
        if family_id in seen_families:
            errors.append(f"multiple checkpoint selections for family {family_id}")
        seen_families.add(family_id)
        selected_id = selection.get("selected_experiment_id")
        attempts = selection.get("all_attempt_experiment_ids")
        if not isinstance(attempts, list) or not attempts or any(not isinstance(value, str) for value in attempts):
            errors.append(f"{label}.all_attempt_experiment_ids must be a non-empty string list")
            attempts = []
        elif len(attempts) != len(set(attempts)):
            errors.append(f"{label}.all_attempt_experiment_ids contains duplicates")
        expected_attempts = {
            experiment_id for experiment_id, node in nodes.items()
            if node.get("selection_family_id") == family_id
        }
        if set(attempts) != expected_attempts:
            errors.append(f"{label}: all attempts do not match the recorded selection family")
        if selected_id not in attempts or selected_id not in nodes:
            errors.append(f"{label}: selected_experiment_id must be one recorded attempt")
        basis = selection.get("selection_basis")
        if basis not in SELECTION_BASES:
            errors.append(f"{label}.selection_basis is invalid")
        selected_on = parse_time(selection.get("selected_on"), f"{label}.selected_on", errors)
        attempt_result_times = [result_times.get(value) for value in attempts if value in nodes]
        if any(value is None for value in attempt_result_times):
            errors.append(f"{label}: every checkpoint attempt requires a recorded result")
        elif selected_on and any(value and value > selected_on for value in attempt_result_times):
            errors.append(f"{label}: selection predates an attempt result")
        if policy_locked and any(value and policy_locked >= value for value in attempt_result_times):
            errors.append(f"{label}: checkpoint selection rule was not locked before attempt results")
        if len(attempts) > 1 or basis == "EXPLORATORY_PERFORMANCE_COMPARISON":
            if not valid_sha(selection.get("multiple_attempts_artifact_sha256")):
                errors.append(f"{label}: multiple/performance selection requires an attempts artifact SHA-256")
        elif selection.get("multiple_attempts_artifact_sha256") not in {"", None}:
            errors.append(f"{label}: single-attempt selection must not invent a multiple-attempt artifact")
        if any(
            nodes[value].get("split_identity", {}).get("role") in {"CONFIRMATORY_TEST", "EXTERNAL_CONFIRMATORY_TEST"}
            and nodes[value].get("test_access", {}).get("accessed") is True
            for value in attempts if value in nodes
        ):
            errors.append(f"{label}: checkpoint selection cannot optimize over confirmatory-test results")
        if selected_id in nodes and nodes[selected_id].get("claim_status") in {"CONFIRMATORY", "EXTERNAL_CONFIRMATORY"}:
            errors.append(f"{label}: a performance-selected node cannot itself be confirmation")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lineage", type=Path)
    args = parser.parse_args()
    try:
        payload = load_unique_json(args.lineage.expanduser().resolve())
        errors = validate(payload)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        errors = [str(exc)]
    report = {
        "status": "FAIL" if errors else "PASS",
        "errors": errors,
        "boundary": "Iteration lineage only; no causal or external-confirmation claim is inferred",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
