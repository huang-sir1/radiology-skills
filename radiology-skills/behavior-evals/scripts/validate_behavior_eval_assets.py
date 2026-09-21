#!/usr/bin/env python3
"""Validate frozen behavior cases and optional captured-output receipts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eval_common import (  # noqa: E402
    HARNESS_REQUIRED_FILES, SKILL_ID_RE, evaluation_harness_snapshot, load_unique_json,
    reject_duplicate_pairs, sha256_bytes, sha256_file, skill_tree_snapshot,
)


SHA_RE = re.compile(r"^[0-9a-f]{64}$")
PROMPT_CLASSES = {"colloquial", "ambiguous", "compound", "boundary"}
DEFECT_CLASSES = {
    "ROUTING_ERROR", "EXECUTION_LAPSE", "TEMPLATE_FRICTION", "HANDOFF_GAP",
    "SOURCE_DRIFT", "RUNTIME_LIMITATION", "NO_DEFECT",
}
SEVERITIES = {"P0", "P1", "P2"}
CANDIDATE_STATES = {"DRAFT", "READY_FOR_REVIEW", "REJECTED"}
UNRESOLVED_ROOT_CAUSES = {
    "", "UNKNOWN", "UNRESOLVED", "UNDETERMINED", "NOT_ASSESSED", "TBD",
    "AUTHOR_INPUT_NEEDED",
}
SEVERITY_RANK = {"P0": 0, "P1": 1, "P2": 2}


def canonical_digest(payload: dict[str, object], digest_field: str) -> str:
    semantic = dict(payload)
    semantic.pop(digest_field, None)
    return sha256_bytes(json.dumps(
        semantic, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8"))


def capture_digest(payload: dict[str, object]) -> str:
    fields = (
        "schema_version", "run_id", "captured_on", "installed_product",
        "cases_registry_path", "cases_registry_sha256", "execution_identity",
        "evaluation_harness", "evaluated_skill_bundle", "outputs",
    )
    missing = [field for field in fields if field not in payload]
    if missing:
        raise ValueError("capture receipt missing fields: " + ", ".join(missing))
    capture = {field: payload[field] for field in fields}
    return sha256_bytes(json.dumps(
        capture, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8"))


def valid_sha(value: object) -> bool:
    return isinstance(value, str) and bool(SHA_RE.fullmatch(value)) and value != "0" * 64


def load_registry(path: Path) -> dict[str, object]:
    value = load_unique_json(path)
    if not isinstance(value, dict):
        raise ValueError("registry root must be an object")
    return value


def validate_registry(
    registry: dict[str, object], skills_root: Path | None = None,
) -> list[str]:
    errors: list[str] = []
    if registry.get("schema_version") != "1.2":
        errors.append("registry schema_version must be 1.2")
    required_classes = set(registry.get("required_prompt_classes", []))
    if required_classes != PROMPT_CLASSES:
        errors.append("required_prompt_classes must cover colloquial, ambiguous, compound and boundary")
    cases = registry.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + ["cases must be a non-empty list"]
    ids: set[str] = set()
    observed_classes: set[str] = set()
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            errors.append(f"cases[{index}] must be an object")
            continue
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"cases[{index}].case_id is required")
        elif case_id in ids:
            errors.append(f"duplicate case_id: {case_id}")
        else:
            ids.add(case_id)
        target = case.get("target_skill")
        if not isinstance(target, str) or not SKILL_ID_RE.fullmatch(target):
            errors.append(f"{case_id}: target_skill is invalid")
        elif skills_root is not None and not (skills_root / target).is_dir():
            errors.append(f"{case_id}: target_skill does not exist: {target}")
        dependencies = case.get("dependency_skills")
        if not isinstance(dependencies, list) or any(
            not isinstance(value, str) or not SKILL_ID_RE.fullmatch(value)
            for value in dependencies
        ):
            errors.append(f"{case_id}: dependency_skills must be an explicit valid skill-id list")
            dependencies = []
        else:
            if len(dependencies) != len(set(dependencies)):
                errors.append(f"{case_id}: dependency_skills contains duplicates")
            if target in dependencies:
                errors.append(f"{case_id}: dependency_skills must not repeat target_skill")
            if skills_root is not None:
                for dependency in dependencies:
                    if not (skills_root / dependency).is_dir():
                        errors.append(f"{case_id}: dependency skill does not exist: {dependency}")
        prompt = case.get("prompt")
        if not isinstance(prompt, str) or not prompt.strip():
            errors.append(f"cases[{index}].prompt is required")
        else:
            expected = sha256_bytes(prompt.encode("utf-8"))
            if case.get("prompt_sha256") != expected:
                errors.append(f"{case_id}: prompt_sha256 mismatch")
        classes = case.get("prompt_classes")
        if not isinstance(classes, list) or not classes or any(value not in PROMPT_CLASSES for value in classes):
            errors.append(f"{case_id}: prompt_classes is invalid")
        else:
            observed_classes.update(classes)
        for field in ("required_behaviors", "prohibited_behaviors"):
            values = case.get(field)
            if not isinstance(values, list) or len(values) < 3 or any(
                not isinstance(value, str) or not value.strip() for value in values
            ):
                errors.append(f"{case_id}: {field} must contain at least three non-empty items")
        blocking = case.get("release_blocking")
        if not isinstance(blocking, bool):
            errors.append(f"{case_id}: release_blocking must be an explicit boolean")
    missing_classes = sorted(PROMPT_CLASSES - observed_classes)
    if missing_classes:
        errors.append("case coverage missing prompt classes: " + ", ".join(missing_classes))
    if skills_root is not None:
        runtime_skills = {
            path.name for path in skills_root.iterdir()
            if path.is_dir() and (path / "SKILL.md").is_file()
        }
        covered_targets = {
            str(case.get("target_skill")) for case in cases
            if isinstance(case, dict) and isinstance(case.get("target_skill"), str)
        }
        missing_skills = sorted(runtime_skills - covered_targets)
        if missing_skills:
            errors.append(
                "case coverage missing a target case for skills: " + ", ".join(missing_skills)
            )
    return errors


def required_skill_ids(registry: dict[str, object]) -> set[str]:
    """Compute the registry's complete de-duplicated target and dependency closure."""
    skill_ids: set[str] = set()
    for case in registry.get("cases", []):
        if not isinstance(case, dict):
            continue
        target = case.get("target_skill")
        if isinstance(target, str):
            skill_ids.add(target)
        dependencies = case.get("dependency_skills")
        if isinstance(dependencies, list):
            skill_ids.update(value for value in dependencies if isinstance(value, str))
    return skill_ids


def exact_key_errors(payload: dict[str, object], required: set[str], label: str) -> list[str]:
    errors: list[str] = []
    missing = sorted(required - set(payload))
    extra = sorted(set(payload) - required)
    if missing:
        errors.append(f"{label} missing fields: " + ", ".join(missing))
    if extra:
        errors.append(f"{label} has unsupported fields: " + ", ".join(extra))
    return errors


def validate_run_observation(payload: object, *, template: bool = False) -> list[str]:
    """Validate one evidence-bound run observation; never authorize a persistent change."""
    if not isinstance(payload, dict):
        return ["run observation root must be an object"]
    required = {
        "schema_version", "observation_id", "run_id", "case_id_or_prompt_sha256",
        "installed_product", "execution_identity", "artifact_evidence",
        "expected_behavior", "observed_behavior", "invariant_id", "defect_signature",
        "root_cause_state", "affected_contract", "defect_class", "severity",
        "workaround_or_none", "observer_role", "observed_on",
        "persistent_change_authorized",
    }
    errors = exact_key_errors(payload, required, "run observation")
    if payload.get("schema_version") != "1.1":
        errors.append("run observation schema_version must be 1.1")
    for field in (
        "observation_id", "run_id", "case_id_or_prompt_sha256", "expected_behavior",
        "observed_behavior", "invariant_id", "defect_signature", "root_cause_state",
        "affected_contract", "workaround_or_none", "observer_role", "observed_on",
    ):
        value = payload.get(field)
        if not template and (not isinstance(value, str) or not value.strip()):
            errors.append(f"run observation {field} is required")
    for field in ("invariant_id", "defect_signature", "root_cause_state", "affected_contract"):
        value = payload.get(field)
        if not template and isinstance(value, str) and (
            value != value.strip() or "\n" in value or "\r" in value
        ):
            errors.append(f"run observation {field} must be one canonical single-line value")
    installed = payload.get("installed_product")
    installed_fields = {"name", "version", "manifest_sha256"}
    if not isinstance(installed, dict):
        errors.append("run observation installed_product must be an object")
    else:
        errors.extend(exact_key_errors(installed, installed_fields, "run observation installed_product"))
        if not template:
            for field in ("name", "version"):
                if not isinstance(installed.get(field), str) or not installed[field].strip():
                    errors.append(f"run observation installed_product.{field} is required")
            if not valid_sha(installed.get("manifest_sha256")):
                errors.append("run observation installed_product.manifest_sha256 is invalid")
    execution = payload.get("execution_identity")
    execution_fields = {"provider", "model", "model_version", "client", "system_context_digest"}
    if not isinstance(execution, dict):
        errors.append("run observation execution_identity must be an object")
    else:
        errors.extend(exact_key_errors(execution, execution_fields, "run observation execution_identity"))
        if not template:
            for field in ("provider", "model", "model_version", "client"):
                if not isinstance(execution.get(field), str) or not execution[field].strip():
                    errors.append(f"run observation execution_identity.{field} is required")
        context = execution.get("system_context_digest")
        if context != "not-captured" and not (template and context == "") and not valid_sha(context):
            errors.append("run observation execution_identity.system_context_digest is invalid")
    artifacts = payload.get("artifact_evidence")
    artifact_fields = {"role", "path_or_uri", "sha256", "exact_locator"}
    if not isinstance(artifacts, list) or not artifacts:
        errors.append("run observation artifact_evidence must be a non-empty list")
    else:
        for index, item in enumerate(artifacts):
            if not isinstance(item, dict):
                errors.append(f"run observation artifact_evidence[{index}] must be an object")
                continue
            errors.extend(exact_key_errors(item, artifact_fields, f"run observation artifact_evidence[{index}]"))
            if not template:
                for field in ("role", "path_or_uri", "exact_locator"):
                    if not isinstance(item.get(field), str) or not item[field].strip():
                        errors.append(f"run observation artifact_evidence[{index}].{field} is required")
                if not valid_sha(item.get("sha256")):
                    errors.append(f"run observation artifact_evidence[{index}].sha256 is invalid")
    if payload.get("defect_class") not in DEFECT_CLASSES:
        errors.append("run observation defect_class is invalid")
    if payload.get("severity") not in SEVERITIES:
        errors.append("run observation severity is invalid")
    if payload.get("persistent_change_authorized") is not False:
        errors.append("run observation persistent_change_authorized must remain false")
    return errors


def validate_improvement_candidate(
    payload: object, *, template: bool = False, candidate_path: Path | None = None,
) -> list[str]:
    """Validate review-entry evidence by re-reading every cited observation artifact."""
    if not isinstance(payload, dict):
        return ["improvement candidate root must be an object"]
    required = {
        "schema_version", "candidate_id", "status", "observation_ids",
        "observation_artifacts", "evidence_pattern", "target_file", "smallest_change",
        "affected_routes", "regression_to_add", "source_freshness_impact", "rollback",
        "scientific_owner", "independent_reviewer", "decision_evidence_locator",
        "persistent_change_authorized",
    }
    errors = exact_key_errors(payload, required, "improvement candidate")
    if payload.get("schema_version") != "1.1":
        errors.append("improvement candidate schema_version must be 1.1")
    status = payload.get("status")
    if status not in CANDIDATE_STATES:
        errors.append("improvement candidate status is invalid")

    observation_ids = payload.get("observation_ids")
    if not isinstance(observation_ids, list) or any(
        not isinstance(value, str) or (not template and not value.strip()) for value in observation_ids
    ):
        errors.append("improvement candidate observation_ids must be a string list")
        observation_ids = []
    elif len(observation_ids) != len(set(observation_ids)):
        errors.append("improvement candidate observation_ids contains duplicates")

    artifact_fields = {"observation_id", "path", "sha256"}
    observation_artifacts = payload.get("observation_artifacts")
    if not isinstance(observation_artifacts, list):
        errors.append("improvement candidate observation_artifacts must be a list")
        observation_artifacts = []
    declared_artifact_ids: list[str] = []
    declared_paths: set[str] = set()
    for index, artifact in enumerate(observation_artifacts):
        label = f"improvement candidate observation_artifacts[{index}]"
        if not isinstance(artifact, dict):
            errors.append(f"{label} must be an object")
            continue
        errors.extend(exact_key_errors(artifact, artifact_fields, label))
        artifact_id = artifact.get("observation_id")
        artifact_path = artifact.get("path")
        artifact_sha = artifact.get("sha256")
        if not template and (not isinstance(artifact_id, str) or not artifact_id.strip()):
            errors.append(f"{label}.observation_id is required")
        elif isinstance(artifact_id, str) and artifact_id:
            declared_artifact_ids.append(artifact_id)
        if not template and (not isinstance(artifact_path, str) or not artifact_path.strip()):
            errors.append(f"{label}.path is required")
        elif isinstance(artifact_path, str) and artifact_path:
            if artifact_path in declared_paths:
                errors.append("improvement candidate observation_artifacts contains duplicate paths")
            declared_paths.add(artifact_path)
        if not template and not valid_sha(artifact_sha):
            errors.append(f"{label}.sha256 is invalid")
    if len(declared_artifact_ids) != len(set(declared_artifact_ids)):
        errors.append("improvement candidate observation_artifacts contains duplicate observation_id values")

    pattern = payload.get("evidence_pattern")
    pattern_fields = {
        "distinct_run_ids", "distinct_case_or_prompt_ids", "repeated_defect_class",
        "repeated_invariant_id", "repeated_defect_signature", "repeated_root_cause_state",
        "affected_contracts", "highest_severity", "high_severity_invariant_break", "basis",
    }
    if not isinstance(pattern, dict):
        errors.append("improvement candidate evidence_pattern must be an object")
        pattern = {}
    else:
        errors.extend(exact_key_errors(pattern, pattern_fields, "improvement candidate evidence_pattern"))
    list_fields = (
        "distinct_run_ids", "distinct_case_or_prompt_ids", "affected_contracts",
    )
    for field in list_fields:
        values = pattern.get(field)
        if not isinstance(values, list) or any(
            not isinstance(value, str) or (not template and not value.strip()) for value in values
        ):
            errors.append(f"improvement candidate evidence_pattern.{field} must be a string list")
        elif len(values) != len(set(values)):
            errors.append(f"improvement candidate evidence_pattern.{field} contains duplicates")
    repeated_class = pattern.get("repeated_defect_class")
    if repeated_class not in (DEFECT_CLASSES - {"NO_DEFECT"}) and not (template and repeated_class == ""):
        errors.append("improvement candidate repeated_defect_class is invalid")
    for field in (
        "repeated_invariant_id", "repeated_defect_signature", "repeated_root_cause_state",
    ):
        value = pattern.get(field)
        if not isinstance(value, str) or (not template and not value.strip()):
            errors.append(f"improvement candidate evidence_pattern.{field} is required")
    severity = pattern.get("highest_severity")
    if severity not in SEVERITIES:
        errors.append("improvement candidate highest_severity is invalid")
    high_break = pattern.get("high_severity_invariant_break")
    if not isinstance(high_break, bool):
        errors.append("improvement candidate high_severity_invariant_break must be boolean")
    if payload.get("persistent_change_authorized") is not False:
        errors.append("improvement candidate persistent_change_authorized must remain false")

    if status == "READY_FOR_REVIEW":
        if not observation_ids:
            errors.append("READY_FOR_REVIEW requires observation_ids")
        if not observation_artifacts:
            errors.append("READY_FOR_REVIEW requires observation_artifacts")
        for field in (
            "candidate_id", "target_file", "smallest_change", "regression_to_add",
            "source_freshness_impact", "rollback", "scientific_owner",
            "independent_reviewer", "decision_evidence_locator",
        ):
            value = payload.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"READY_FOR_REVIEW requires {field}")
        routes = payload.get("affected_routes")
        if not isinstance(routes, list) or not routes or any(
            not isinstance(value, str) or not value.strip() for value in routes
        ):
            errors.append("READY_FOR_REVIEW requires affected_routes")
        if not isinstance(pattern.get("basis"), str) or not pattern["basis"].strip():
            errors.append("READY_FOR_REVIEW requires evidence_pattern.basis")
        if candidate_path is None:
            errors.append("READY_FOR_REVIEW requires candidate_path to resolve observation artifacts")
            return errors

        loaded_observations: list[dict[str, object]] = []
        candidate_parent = candidate_path.expanduser().resolve().parent
        for index, artifact in enumerate(observation_artifacts):
            if not isinstance(artifact, dict):
                continue
            artifact_id = artifact.get("observation_id")
            path_value = artifact.get("path")
            declared_sha = artifact.get("sha256")
            if not isinstance(path_value, str) or not path_value or not valid_sha(declared_sha):
                continue
            observation_path = Path(path_value).expanduser()
            if not observation_path.is_absolute():
                observation_path = candidate_parent / observation_path
            observation_path = observation_path.resolve()
            if not observation_path.is_file():
                errors.append(f"observation artifact is missing: {path_value}")
                continue
            if sha256_file(observation_path) != declared_sha:
                errors.append(f"observation artifact SHA-256 mismatch: {path_value}")
                continue
            try:
                observation = load_unique_json(observation_path)
            except (OSError, json.JSONDecodeError, UnicodeDecodeError, ValueError) as exc:
                errors.append(f"observation artifact cannot be parsed: {path_value}: {exc}")
                continue
            observation_errors = validate_run_observation(observation)
            errors.extend(
                f"observation artifact {path_value}: {error}" for error in observation_errors
            )
            if observation_errors or not isinstance(observation, dict):
                continue
            if observation.get("observation_id") != artifact_id:
                errors.append(f"observation artifact ID mismatch: {path_value}")
                continue
            loaded_observations.append(observation)

        physical_ids = sorted(str(item["observation_id"]) for item in loaded_observations)
        if sorted(observation_ids) != physical_ids:
            errors.append("observation_ids do not exactly match validated observation artifacts")
        if sorted(declared_artifact_ids) != physical_ids:
            errors.append("declared observation artifact IDs do not match physical observations")
        if len(loaded_observations) != len(observation_artifacts):
            errors.append("READY_FOR_REVIEW requires every observation artifact to validate")

        if loaded_observations:
            computed_runs = sorted({str(item["run_id"]) for item in loaded_observations})
            computed_prompts = sorted({
                str(item["case_id_or_prompt_sha256"]) for item in loaded_observations
            })
            computed_contracts = sorted({
                str(item["affected_contract"]) for item in loaded_observations
            })
            defect_classes = {str(item["defect_class"]) for item in loaded_observations}
            invariant_ids = {str(item["invariant_id"]) for item in loaded_observations}
            signatures = {str(item["defect_signature"]) for item in loaded_observations}
            root_causes = {str(item["root_cause_state"]) for item in loaded_observations}
            computed_severity = min(
                (str(item["severity"]) for item in loaded_observations),
                key=lambda value: SEVERITY_RANK[value],
            )
            computed_high_break = any(
                item["severity"] in {"P0", "P1"}
                and item["defect_class"] != "NO_DEFECT"
                and bool(str(item["invariant_id"]).strip())
                for item in loaded_observations
            )
            computed_scalar = {
                "repeated_defect_class": next(iter(defect_classes)) if len(defect_classes) == 1 else "",
                "repeated_invariant_id": next(iter(invariant_ids)) if len(invariant_ids) == 1 else "",
                "repeated_defect_signature": next(iter(signatures)) if len(signatures) == 1 else "",
                "repeated_root_cause_state": next(iter(root_causes)) if len(root_causes) == 1 else "",
                "highest_severity": computed_severity,
                "high_severity_invariant_break": computed_high_break,
            }
            for field, computed in (
                ("distinct_run_ids", computed_runs),
                ("distinct_case_or_prompt_ids", computed_prompts),
                ("affected_contracts", computed_contracts),
            ):
                reported = pattern.get(field)
                if not isinstance(reported, list) or sorted(reported) != computed:
                    errors.append(f"evidence_pattern.{field} does not match observation evidence")
            for field, computed in computed_scalar.items():
                if pattern.get(field) != computed:
                    errors.append(f"evidence_pattern.{field} does not match observation evidence")

            repeated = (
                len(computed_runs) >= 2
                and len(computed_prompts) >= 2
                and len(defect_classes) == 1
                and next(iter(defect_classes)) in (DEFECT_CLASSES - {"NO_DEFECT"})
                and len(invariant_ids) == 1
                and len(signatures) == 1
                and len(root_causes) == 1
                and next(iter(root_causes)).strip().upper() not in UNRESOLVED_ROOT_CAUSES
            )
            emergency = len(loaded_observations) == 1 and computed_high_break
            if not (repeated or emergency):
                errors.append(
                    "READY_FOR_REVIEW requires the same invariant, defect signature and resolved "
                    "root cause across at least two runs and two cases/prompts, or one documented "
                    "P0/P1 invariant break"
                )
    return errors


def validate_learning_templates(eval_root: Path) -> list[str]:
    errors: list[str] = []
    for filename, validator in (
        ("run-observation.template.json", validate_run_observation),
        ("improvement-candidate.template.json", validate_improvement_candidate),
    ):
        path = eval_root / filename
        if not path.is_file():
            errors.append(f"missing learning-loop template: {filename}")
            continue
        try:
            payload = load_unique_json(path)
        except (OSError, json.JSONDecodeError, UnicodeDecodeError, ValueError) as exc:
            errors.append(f"{filename} cannot be parsed: {exc}")
            continue
        errors.extend(f"{filename}: {error}" for error in validator(payload, template=True))
    return errors


def validate_human_adjudication(
    payload: object,
    receipt: dict[str, object],
    expected_cases: dict[str, dict[str, object]],
) -> tuple[list[str], str]:
    errors: list[str] = []
    if not isinstance(payload, dict):
        return ["human adjudication root must be an object"], "NOT_ADJUDICATED"
    required = {
        "schema_version", "run_id", "receipt_digest_reviewed", "adjudication_status",
        "adjudicator_roles", "qualification_basis", "conflict_of_interest_statement",
        "adjudicated_on", "case_reviews", "disagreements_and_resolution", "overall_decision",
        "release_decision_owner", "human_adjudication_digest",
    }
    missing = sorted(required - payload.keys())
    if missing:
        errors.append("human adjudication missing fields: " + ", ".join(missing))
    if payload.get("schema_version") != "1.0":
        errors.append("human adjudication schema_version must be 1.0")
    if payload.get("run_id") != receipt.get("run_id"):
        errors.append("human adjudication run_id does not match receipt")
    if payload.get("receipt_digest_reviewed") != receipt.get("capture_receipt_digest"):
        errors.append("human adjudication receipt_digest_reviewed must match capture_receipt_digest")
    if payload.get("adjudication_status") != "HUMAN_ADJUDICATED":
        errors.append("human adjudication status must be HUMAN_ADJUDICATED")
    roles = payload.get("adjudicator_roles")
    if not isinstance(roles, list) or not roles or any(
        not isinstance(value, str) or not value.strip() for value in roles
    ):
        errors.append("human adjudicator_roles must be a non-empty string list")
    for field in (
        "qualification_basis", "conflict_of_interest_statement", "adjudicated_on",
        "disagreements_and_resolution", "release_decision_owner",
    ):
        value = payload.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"human adjudication {field} is required")

    output_by_case = {
        item.get("case_id"): item
        for item in receipt.get("outputs", [])
        if isinstance(item, dict)
    }
    reviews = payload.get("case_reviews")
    if not isinstance(reviews, list):
        errors.append("human adjudication case_reviews must be a list")
        reviews = []
    seen: set[str] = set()
    decisions: list[str] = []
    for index, review in enumerate(reviews):
        if not isinstance(review, dict):
            errors.append(f"case_reviews[{index}] must be an object")
            continue
        case_id = review.get("case_id")
        if case_id not in expected_cases:
            errors.append(f"case_reviews[{index}] has unknown case_id")
            continue
        if case_id in seen:
            errors.append(f"duplicate human case review: {case_id}")
        seen.add(str(case_id))
        expected_output = output_by_case.get(case_id, {})
        if review.get("output_sha256") != expected_output.get("output_sha256"):
            errors.append(f"{case_id}: human review output_sha256 mismatch")

        scores = review.get("required_behavior_scores")
        score_map: dict[str, object] = {}
        if not isinstance(scores, list):
            errors.append(f"{case_id}: required_behavior_scores must be a list")
            scores = []
        for item in scores:
            if not isinstance(item, dict) or not isinstance(item.get("behavior"), str):
                errors.append(f"{case_id}: malformed required behavior score")
                continue
            behavior = item["behavior"]
            if behavior in score_map:
                errors.append(f"{case_id}: duplicate required behavior score")
            score_map[behavior] = item.get("score")
            score = item.get("score")
            if isinstance(score, bool) or not isinstance(score, int) or score not in {0, 1, 2}:
                errors.append(f"{case_id}: required behavior score must be 0, 1 or 2")
            if not isinstance(item.get("evidence_locator"), str) or not item["evidence_locator"].strip():
                errors.append(f"{case_id}: required behavior score needs an evidence locator")
        required_behaviors = set(expected_cases[case_id].get("required_behaviors", []))
        if set(score_map) != required_behaviors:
            errors.append(f"{case_id}: required behavior scores do not exactly match frozen rubric")

        findings = review.get("prohibited_behavior_findings")
        finding_map: dict[str, object] = {}
        if not isinstance(findings, list):
            errors.append(f"{case_id}: prohibited_behavior_findings must be a list")
            findings = []
        for item in findings:
            if not isinstance(item, dict) or not isinstance(item.get("behavior"), str):
                errors.append(f"{case_id}: malformed prohibited behavior finding")
                continue
            behavior = item["behavior"]
            if behavior in finding_map:
                errors.append(f"{case_id}: duplicate prohibited behavior finding")
            observed = item.get("observed")
            finding_map[behavior] = observed
            if not isinstance(observed, bool):
                errors.append(f"{case_id}: prohibited behavior observed must be boolean")
            if not isinstance(item.get("evidence_locator"), str) or not item["evidence_locator"].strip():
                errors.append(f"{case_id}: prohibited behavior finding needs an evidence locator")
        prohibited_behaviors = set(expected_cases[case_id].get("prohibited_behaviors", []))
        if set(finding_map) != prohibited_behaviors:
            errors.append(f"{case_id}: prohibited findings do not exactly match frozen rubric")

        decision = review.get("decision")
        if decision not in {"PASS", "CONDITIONAL", "FAIL"}:
            errors.append(f"{case_id}: human decision is invalid")
        else:
            decisions.append(str(decision))
        if not isinstance(review.get("rationale"), str) or not review["rationale"].strip():
            errors.append(f"{case_id}: human rationale is required")
        if decision == "PASS" and (
            any(score != 2 for score in score_map.values())
            or any(value is not False for value in finding_map.values())
        ):
            errors.append(f"{case_id}: PASS requires every required score=2 and no prohibited behavior")

    if seen != set(expected_cases):
        errors.append("human adjudication must review every frozen case exactly once")
    overall = payload.get("overall_decision")
    if overall not in {"PASS", "CONDITIONAL", "FAIL"}:
        errors.append("human adjudication overall_decision is invalid")
        overall = "NOT_ADJUDICATED"
    if overall == "PASS" and (len(decisions) != len(expected_cases) or any(
        decision != "PASS" for decision in decisions
    )):
        errors.append("human overall PASS requires every frozen case PASS")
    computed = canonical_digest(payload, "human_adjudication_digest")
    declared = payload.get("human_adjudication_digest")
    if not valid_sha(declared) or declared != computed:
        errors.append("human_adjudication_digest mismatch")
    return errors, str(overall)


def validate_receipt(
    receipt: dict[str, object], registry_path: Path, registry: dict[str, object], run_root: Path,
) -> tuple[list[str], dict[str, object]]:
    errors: list[str] = []
    required_fields = {
        "schema_version", "run_id", "run_state", "captured_on", "installed_product",
        "cases_registry_path", "cases_registry_sha256", "capture_receipt_digest",
        "execution_identity", "evaluation_harness", "evaluated_skill_bundle", "outputs",
        "human_adjudication", "comparison_claim_eligible", "release_claim_eligible",
        "behavior_eval_receipt_digest",
    }
    extra_fields = sorted(set(receipt) - required_fields)
    missing_fields = sorted(required_fields - set(receipt))
    if missing_fields:
        errors.append("receipt missing required fields: " + ", ".join(missing_fields))
    if extra_fields:
        errors.append("receipt has unsupported fields: " + ", ".join(extra_fields))
    if receipt.get("schema_version") != "1.2":
        errors.append("receipt schema_version must be 1.2")
    if not isinstance(receipt.get("run_id"), str) or not receipt.get("run_id", "").strip():
        errors.append("receipt run_id must be a non-empty string")
    if receipt.get("run_state") not in {"PILOT_UNADJUDICATED", "HUMAN_ADJUDICATION_RECORDED"}:
        errors.append("receipt run_state is invalid")
    receipt_registry_path = receipt.get("cases_registry_path")
    if not isinstance(receipt_registry_path, str) or not receipt_registry_path:
        errors.append("cases_registry_path is required")
    else:
        physical_registry = Path(receipt_registry_path).expanduser()
        if not physical_registry.is_absolute():
            physical_registry = run_root / physical_registry
        physical_registry = physical_registry.resolve()
        if not physical_registry.is_file():
            errors.append("cases_registry_path does not resolve to a file")
        elif receipt.get("cases_registry_sha256") != sha256_file(physical_registry):
            errors.append("physical cases registry SHA-256 mismatch")
    if receipt.get("cases_registry_sha256") != sha256_file(registry_path):
        errors.append("cases_registry_sha256 mismatch")
    try:
        expected_capture_digest = capture_digest(receipt)
    except ValueError as exc:
        errors.append(str(exc))
    else:
        if not valid_sha(receipt.get("capture_receipt_digest")) or (
            receipt.get("capture_receipt_digest") != expected_capture_digest
        ):
            errors.append("capture_receipt_digest mismatch")

    installed = receipt.get("installed_product")
    manifest_payload: dict[str, object] = {}
    if not isinstance(installed, dict):
        errors.append("installed_product must be an object")
        installed = {}
    manifest_path_value = installed.get("manifest_path")
    if not isinstance(manifest_path_value, str) or not manifest_path_value:
        errors.append("installed_product.manifest_path is required")
    else:
        manifest_path = Path(manifest_path_value).expanduser()
        if not manifest_path.is_absolute():
            manifest_path = run_root / manifest_path
        manifest_path = manifest_path.resolve()
        if not manifest_path.is_file():
            errors.append("installed product manifest file is missing")
        else:
            if installed.get("manifest_sha256") != sha256_file(manifest_path):
                errors.append("installed product manifest SHA-256 mismatch")
            try:
                manifest_value = load_unique_json(manifest_path)
                if isinstance(manifest_value, dict):
                    manifest_payload = manifest_value
                else:
                    errors.append("installed product manifest root must be an object")
            except (OSError, json.JSONDecodeError, UnicodeDecodeError, ValueError) as exc:
                errors.append(f"installed product manifest cannot be parsed: {exc}")
    for field in ("name", "version"):
        if installed.get(field) != manifest_payload.get(field):
            errors.append(f"installed_product.{field} does not match physical manifest")
    execution = receipt.get("execution_identity")
    context_digest: object = None
    execution_fields = {"provider", "model", "model_version", "client", "system_context_digest"}
    if not isinstance(execution, dict):
        errors.append("execution_identity must be an object")
    else:
        missing_execution = sorted(execution_fields - set(execution))
        extra_execution = sorted(set(execution) - execution_fields)
        if missing_execution:
            errors.append("execution_identity missing fields: " + ", ".join(missing_execution))
        if extra_execution:
            errors.append("execution_identity has unsupported fields: " + ", ".join(extra_execution))
        for field in ("provider", "model", "model_version", "client"):
            if not isinstance(execution.get(field), str) or not execution.get(field, "").strip():
                errors.append(f"execution_identity.{field} must be a non-empty string")
        context_digest = execution.get("system_context_digest")
        if context_digest != "not-captured" and not valid_sha(context_digest):
            errors.append("execution_identity.system_context_digest is invalid")

    harness = receipt.get("evaluation_harness")
    harness_fields = {"harness_path", "file_count", "tree_sha256"}
    if not isinstance(harness, dict):
        errors.append("evaluation_harness must be an object")
    else:
        errors.extend(exact_key_errors(harness, harness_fields, "evaluation_harness"))
        harness_path_value = harness.get("harness_path")
        if not isinstance(harness_path_value, str) or not harness_path_value:
            errors.append("evaluation_harness.harness_path is required")
        else:
            harness_path = Path(harness_path_value).expanduser()
            if not harness_path.is_absolute():
                harness_path = run_root / harness_path
            harness_path = harness_path.resolve()
            if not harness_path.is_dir():
                errors.append("evaluation_harness.harness_path is missing")
            else:
                try:
                    snapshot = evaluation_harness_snapshot(harness_path)
                except ValueError as exc:
                    errors.append(str(exc))
                else:
                    if harness.get("file_count") != snapshot["file_count"]:
                        errors.append("evaluation_harness.file_count mismatch")
                    if harness.get("tree_sha256") != snapshot["tree_sha256"]:
                        errors.append("evaluation_harness.tree_sha256 mismatch")
                    harness_registry = harness_path / "cases.json"
                    if sha256_file(harness_registry) != receipt.get("cases_registry_sha256"):
                        errors.append("evaluation harness cases.json does not match captured registry")
    expected_cases = {case["case_id"]: case for case in registry.get("cases", []) if isinstance(case, dict)}
    expected_skills = required_skill_ids(registry)
    bundle = receipt.get("evaluated_skill_bundle")
    bundle_by_skill: dict[str, dict[str, object]] = {}
    bundle_fields = {"skill_id", "skill_path", "file_count", "tree_sha256"}
    if not isinstance(bundle, list) or not bundle:
        errors.append("evaluated_skill_bundle must be a non-empty list")
        bundle = []
    for index, item in enumerate(bundle):
        if not isinstance(item, dict):
            errors.append(f"evaluated_skill_bundle[{index}] must be an object")
            continue
        missing_bundle = sorted(bundle_fields - set(item))
        extra_bundle = sorted(set(item) - bundle_fields)
        if missing_bundle:
            errors.append(f"evaluated_skill_bundle[{index}] missing fields: " + ", ".join(missing_bundle))
        if extra_bundle:
            errors.append(f"evaluated_skill_bundle[{index}] has unsupported fields: " + ", ".join(extra_bundle))
        skill_id = item.get("skill_id")
        if not isinstance(skill_id, str) or not SKILL_ID_RE.fullmatch(skill_id):
            errors.append(f"evaluated_skill_bundle[{index}].skill_id is required")
            continue
        if skill_id in bundle_by_skill:
            errors.append(f"duplicate evaluated skill bundle: {skill_id}")
        bundle_by_skill[skill_id] = item
        skill_path_value = item.get("skill_path")
        if not isinstance(skill_path_value, str) or not skill_path_value:
            errors.append(f"{skill_id}: skill_path is required")
            continue
        skill_path = Path(skill_path_value).expanduser().resolve()
        if skill_path.name != skill_id:
            errors.append(f"{skill_id}: skill_path basename must match skill_id")
        if not skill_path.is_dir():
            errors.append(f"{skill_id}: evaluated skill_path is missing")
            continue
        snapshot = skill_tree_snapshot(skill_path)
        if item.get("file_count") != snapshot["file_count"]:
            errors.append(f"{skill_id}: evaluated skill file_count mismatch")
        if item.get("tree_sha256") != snapshot["tree_sha256"]:
            errors.append(f"{skill_id}: evaluated skill tree_sha256 mismatch")
    if set(bundle_by_skill) != expected_skills:
        errors.append(
            "evaluated_skill_bundle must cover the complete de-duplicated target_skill plus "
            "dependency_skills closure exactly once"
        )
    outputs = receipt.get("outputs")
    if not isinstance(outputs, list):
        errors.append("outputs must be a list")
        outputs = []
    seen: set[str] = set()
    for index, output in enumerate(outputs):
        if not isinstance(output, dict):
            errors.append(f"outputs[{index}] must be an object")
            continue
        case_id = output.get("case_id")
        if case_id not in expected_cases:
            errors.append(f"outputs[{index}] has unknown case_id")
            continue
        if case_id in seen:
            errors.append(f"duplicate output case_id: {case_id}")
        seen.add(str(case_id))
        if output.get("prompt_sha256") != expected_cases[case_id].get("prompt_sha256"):
            errors.append(f"{case_id}: receipt prompt_sha256 mismatch")
        raw_path = output.get("output_path")
        if not isinstance(raw_path, str) or not raw_path:
            errors.append(f"{case_id}: output_path is required")
            continue
        path = (run_root / raw_path).resolve()
        try:
            path.relative_to(run_root.resolve())
        except ValueError:
            errors.append(f"{case_id}: output_path escapes run root")
            continue
        if not path.is_file():
            errors.append(f"{case_id}: output file is missing")
        elif output.get("output_sha256") != sha256_file(path):
            errors.append(f"{case_id}: output_sha256 mismatch")
        if output.get("execution_state") != "MODEL_OUTPUT_CAPTURED":
            errors.append(f"{case_id}: execution_state must be MODEL_OUTPUT_CAPTURED")
    if seen != set(expected_cases):
        errors.append("receipt must bind exactly one output for every frozen case")

    declared = receipt.get("behavior_eval_receipt_digest")
    computed = canonical_digest(receipt, "behavior_eval_receipt_digest")
    if not valid_sha(declared) or declared != computed:
        errors.append("behavior_eval_receipt_digest mismatch")
    human = receipt.get("human_adjudication")
    human_status = human.get("status") if isinstance(human, dict) else None
    if human_status not in {"NOT_ADJUDICATED", "HUMAN_ADJUDICATED"}:
        errors.append("human_adjudication.status is invalid")
    if human_status == "HUMAN_ADJUDICATED" and receipt.get("run_state") != "HUMAN_ADJUDICATION_RECORDED":
        errors.append("HUMAN_ADJUDICATED requires run_state HUMAN_ADJUDICATION_RECORDED")
    if receipt.get("run_state") == "HUMAN_ADJUDICATION_RECORDED" and human_status != "HUMAN_ADJUDICATED":
        errors.append("HUMAN_ADJUDICATION_RECORDED requires a human adjudication artifact")
    human_record_complete = False
    recorded_overall_decision = "NOT_ADJUDICATED"
    if human_status == "HUMAN_ADJUDICATED" and isinstance(human, dict):
        artifact_value = human.get("artifact_path")
        artifact_sha = human.get("artifact_sha256")
        if not isinstance(artifact_value, str) or not artifact_value:
            errors.append("human adjudication artifact_path is required")
        elif not valid_sha(artifact_sha):
            errors.append("human adjudication artifact_sha256 is invalid")
        else:
            human_path: Path | None = (run_root / artifact_value).resolve()
            try:
                human_path.relative_to(run_root.resolve())
            except ValueError:
                errors.append("human adjudication artifact_path escapes run root")
                human_path = None
            if human_path is not None and not human_path.is_file():
                errors.append("human adjudication artifact is missing")
            elif human_path is not None:
                if sha256_file(human_path) != artifact_sha:
                    errors.append("human adjudication artifact SHA-256 mismatch")
                else:
                    try:
                        human_payload = load_unique_json(human_path)
                        human_errors, recorded_overall_decision = validate_human_adjudication(
                            human_payload, receipt, expected_cases,
                        )
                        errors.extend(human_errors)
                        human_record_complete = not human_errors
                    except (OSError, json.JSONDecodeError, UnicodeDecodeError, ValueError) as exc:
                        errors.append(f"human adjudication artifact cannot be parsed: {exc}")

    if receipt.get("run_state") == "PILOT_UNADJUDICATED":
        if human_status != "NOT_ADJUDICATED" or receipt.get("release_claim_eligible") is not False:
            errors.append("unadjudicated pilot must remain release_claim_eligible=false")
    if human_status == "NOT_ADJUDICATED" and receipt.get("release_claim_eligible") is not False:
        errors.append("machine-captured outputs cannot be release-eligible without human adjudication")
    if receipt.get("comparison_claim_eligible") is not False:
        if context_digest == "not-captured":
            errors.append(
                "system_context_digest=not-captured forbids cross-version comparison and "
                "maturity upgrade claims"
            )
        errors.append("comparison_claim_eligible must remain false in this capture harness")
    if receipt.get("release_claim_eligible") is not False:
        errors.append(
            "release_claim_eligible must remain false: this validator checks record completeness "
            "but does not authenticate adjudicator identity, qualification or signature"
        )
    return errors, {
        "outputs": len(outputs),
        "evaluated_skills": len(bundle),
        "human_adjudication": human_status,
        "comparison_claim_eligible": False,
        "recorded_overall_decision": recorded_overall_decision,
        "behavioral_verdict": "NOT_ADJUDICATED" if human_status == "NOT_ADJUDICATED" else "HUMAN_RECORD_COMPLETE_NOT_AUTHENTICATED" if human_record_complete else "HUMAN_RECORD_INCOMPLETE",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", required=True, type=Path)
    parser.add_argument("--product-root", type=Path)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--run-root", type=Path)
    parser.add_argument("--run-observation", type=Path)
    parser.add_argument("--improvement-candidate", type=Path)
    args = parser.parse_args()
    registry_path = args.registry.expanduser().resolve()
    try:
        registry = load_registry(registry_path)
        product_root = (
            args.product_root.expanduser().resolve()
            if args.product_root else Path(__file__).resolve().parents[2]
        )
        errors = validate_registry(registry, product_root / "skills")
        errors.extend(validate_learning_templates(registry_path.parent))
        details: dict[str, object] = {
            "cases": len(registry.get("cases", [])), "learning_loop_templates": 2,
        }
        if args.receipt:
            receipt_path = args.receipt.expanduser().resolve()
            receipt = load_unique_json(receipt_path)
            run_root = args.run_root.expanduser().resolve() if args.run_root else receipt_path.parent
            receipt_errors, receipt_details = validate_receipt(receipt, registry_path, registry, run_root)
            errors.extend(receipt_errors)
            details.update(receipt_details)
        if args.run_observation:
            observation = load_unique_json(args.run_observation.expanduser().resolve())
            errors.extend(validate_run_observation(observation))
            details["run_observation_checked"] = True
        if args.improvement_candidate:
            candidate_path = args.improvement_candidate.expanduser().resolve()
            candidate = load_unique_json(candidate_path)
            errors.extend(validate_improvement_candidate(candidate, candidate_path=candidate_path))
            details["improvement_candidate_checked"] = True
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors = [str(exc)]
        details = {}
    report = {
        "status": "FAIL" if errors else "PASS",
        "details": details,
        "errors": errors,
        "boundary": "Structural identity validation only; no model was run and no human behavior verdict is inferred",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
