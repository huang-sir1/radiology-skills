#!/usr/bin/env python3
"""Positive and adversarial tests for experiment-lineage DAG validation."""

from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT_ROOT = Path(__file__).resolve().parent
VALIDATOR_PATH = SCRIPT_ROOT / "validate_experiment_lineage.py"
TEMPLATE_PATH = SCRIPT_ROOT.parent / "assets" / "experiment-lineage.template.json"
SPEC = importlib.util.spec_from_file_location("validate_experiment_lineage", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def digest(character: str) -> str:
    return character * 64


def experiment(
    experiment_id: str,
    parents: list[str],
    created_on: str,
    *,
    split_role: str = "DEVELOPMENT",
    intent: str = "EXPLORATORY",
    claim_status: str = "EXPLORATORY",
    test_id: str = "",
    accessed: bool = False,
    counter: int = 0,
    accessed_on: str = "",
    intent_locked_on: str = "",
    selection_family_id: str = "",
    children: list[str] | None = None,
) -> dict[str, object]:
    suffix = experiment_id[-1].lower()
    result_sha = digest("a" if suffix not in "0123456789abcdef" else suffix)
    feedback_sha = digest("b" if suffix == "a" else "e")
    return {
        "experiment_id": experiment_id,
        "parent_ids": parents,
        "created_on": created_on,
        "hypothesis": f"Frozen hypothesis for {experiment_id}",
        "decision": "PROCEED",
        "analysis_intent": intent,
        "intent_locked_on": intent_locked_on,
        "intent_lock_artifact_sha256": digest("c") if intent_locked_on else "",
        "data_identity": {
            "dataset_id": "DATA-DEV" if split_role == "DEVELOPMENT" else "DATA-TEST",
            "manifest_sha256": digest("d"),
        },
        "split_identity": {
            "split_id": f"SPLIT-{experiment_id}",
            "manifest_sha256": digest("f"),
            "role": split_role,
        },
        "test_access": {
            "test_id": test_id,
            "accessed": accessed,
            "access_counter": counter,
            "accessed_on": accessed_on,
        },
        "configuration": {
            "configuration_id": f"CFG-{experiment_id}",
            "configuration_sha256": digest("1"),
            "code_sha256": digest("2"),
            "environment_sha256": digest("3"),
        },
        "artifacts": [
            {"artifact_id": f"RES-{experiment_id}", "role": "result", "sha256": result_sha},
            {"artifact_id": f"FDB-{experiment_id}", "role": "feedback", "sha256": feedback_sha},
        ],
        "result": {
            "status": "COMPLETED",
            "recorded_on": accessed_on or "2026-08-02T12:00:00Z",
            "summary": "Frozen result summary.",
            "primary_metric_name": "AUROC",
            "primary_metric_value": 0.75,
            "artifact_sha256": result_sha,
        },
        "feedback": {
            "summary": "Decision-bearing feedback.",
            "child_experiment_ids": children or [],
            "artifact_sha256": feedback_sha,
        },
        "branch_reason": "ROOT" if not parents else "Prespecified refinement after parent feedback.",
        "selection_family_id": selection_family_id,
        "lifecycle_status": "COMPLETED",
        "terminal_reason": "",
        "claim_status": claim_status,
    }


def valid_lineage() -> dict[str, object]:
    first = experiment(
        "EXP-001", [], "2026-08-01T01:00:00Z",
        selection_family_id="FAM-001", children=["EXP-002"],
    )
    first["result"]["recorded_on"] = "2026-08-01T12:00:00Z"
    second = experiment(
        "EXP-002", ["EXP-001"], "2026-08-01T02:00:00Z",
        split_role="INTERNAL_VALIDATION", claim_status="INTERNAL_VALIDATION",
        selection_family_id="FAM-001", children=["EXP-003"],
    )
    second["result"]["recorded_on"] = "2026-08-02T12:00:00Z"
    third = experiment(
        "EXP-003", ["EXP-002"], "2026-08-03T00:00:00Z",
        split_role="EXTERNAL_CONFIRMATORY_TEST",
        intent="PRE_SPECIFIED_CONFIRMATORY",
        claim_status="EXTERNAL_CONFIRMATORY",
        test_id="TEST-EXT-001", accessed=True, counter=1,
        intent_locked_on="2026-08-03T01:00:00Z",
        accessed_on="2026-08-04T12:00:00Z",
    )
    return {
        "schema_version": "1.0",
        "lineage_id": "LINEAGE-001",
        "study_id": "STUDY-001",
        "created_on": "2026-08-01T00:00:00Z",
        "claim_boundary": MODULE.BOUNDARY,
        "checkpoint_selection_policy": {
            "applicability": "APPLICABLE",
            "rule": "Select the highest internal-validation AUROC; break ties by lower complexity.",
            "locked_on": "2026-08-01T00:30:00Z",
            "artifact_sha256": digest("4"),
            "not_applicable_reason": "",
        },
        "experiments": [first, second, third],
        "checkpoint_selections": [{
            "selection_id": "SEL-001",
            "selection_family_id": "FAM-001",
            "selected_experiment_id": "EXP-002",
            "all_attempt_experiment_ids": ["EXP-001", "EXP-002"],
            "selection_basis": "PRE_SPECIFIED_RULE",
            "selected_on": "2026-08-02T13:00:00Z",
            "multiple_attempts_artifact_sha256": digest("5"),
        }],
    }


class ExperimentLineageTests(unittest.TestCase):
    def test_valid_branch_selection_and_single_external_confirmation(self) -> None:
        self.assertEqual([], MODULE.validate(valid_lineage()))

    def test_template_exposes_required_contract_without_claiming_evidence(self) -> None:
        template = MODULE.load_unique_json(TEMPLATE_PATH)
        self.assertEqual(MODULE.BOUNDARY, template["claim_boundary"])
        self.assertIn("checkpoint_selection_policy", template)
        self.assertIn("test_access", template["experiments"][0])
        self.assertTrue(MODULE.validate(template))

    def test_cycle_and_orphan_are_rejected(self) -> None:
        cycle = valid_lineage()
        cycle["experiments"][0]["parent_ids"] = ["EXP-002"]
        cycle["experiments"][0]["branch_reason"] = "Cycle fixture."
        cycle["experiments"][1]["feedback"]["child_experiment_ids"] = ["EXP-001", "EXP-003"]
        self.assertTrue(any("cycle" in error.lower() for error in MODULE.validate(cycle)))

        orphan = valid_lineage()
        orphan["experiments"][1]["parent_ids"] = ["EXP-MISSING"]
        self.assertTrue(any("orphan" in error.lower() for error in MODULE.validate(orphan)))

    def test_confirmatory_test_reuse_and_counter_gaps_are_rejected(self) -> None:
        payload = valid_lineage()
        duplicate = copy.deepcopy(payload["experiments"][2])
        duplicate["experiment_id"] = "EXP-004"
        duplicate["created_on"] = "2026-08-03T02:00:00Z"
        duplicate["intent_locked_on"] = "2026-08-03T03:00:00Z"
        duplicate["test_access"]["access_counter"] = 2
        duplicate["test_access"]["accessed_on"] = "2026-08-05T12:00:00Z"
        duplicate["result"]["recorded_on"] = "2026-08-05T12:00:00Z"
        duplicate["artifacts"][0]["artifact_id"] = "RES-EXP-004"
        duplicate["artifacts"][1]["artifact_id"] = "FDB-EXP-004"
        payload["experiments"].append(duplicate)
        payload["experiments"][1]["feedback"]["child_experiment_ids"].append("EXP-004")
        errors = MODULE.validate(payload)
        self.assertTrue(any("confirmatory test reused" in error for error in errors))
        self.assertTrue(any("first and only access" in error for error in errors))

        single_gap = valid_lineage()
        single_gap["experiments"][2]["test_access"]["access_counter"] = 2
        self.assertTrue(any("contiguous from 1" in error for error in MODULE.validate(single_gap)))

    def test_post_test_or_exploratory_relabelling_is_rejected(self) -> None:
        post_test = valid_lineage()
        post_test["experiments"][2]["intent_locked_on"] = "2026-08-05T00:00:00Z"
        self.assertTrue(any("not locked before test access" in error for error in MODULE.validate(post_test)))

        relabelled = valid_lineage()
        node = relabelled["experiments"][2]
        node["analysis_intent"] = "EXPLORATORY"
        node["intent_locked_on"] = ""
        node["intent_lock_artifact_sha256"] = ""
        self.assertTrue(any("cannot be relabelled confirmatory" in error for error in MODULE.validate(relabelled)))

    def test_performance_selection_requires_complete_attempt_record(self) -> None:
        missing_attempts = valid_lineage()
        extra = experiment(
            "EXP-004", ["EXP-001"], "2026-08-01T03:00:00Z",
            split_role="INTERNAL_VALIDATION", claim_status="INTERNAL_VALIDATION",
            selection_family_id="FAM-001",
        )
        missing_attempts["experiments"].append(extra)
        missing_attempts["experiments"][0]["feedback"]["child_experiment_ids"].append("EXP-004")
        self.assertTrue(any(
            "all attempts do not match" in error for error in MODULE.validate(missing_attempts)
        ))

        no_attempt_artifact = valid_lineage()
        selection = no_attempt_artifact["checkpoint_selections"][0]
        selection["selection_basis"] = "EXPLORATORY_PERFORMANCE_COMPARISON"
        selection["multiple_attempts_artifact_sha256"] = ""
        self.assertTrue(any(
            "attempts artifact SHA-256" in error for error in MODULE.validate(no_attempt_artifact)
        ))

    def test_best_confirmatory_test_node_cannot_be_called_external_confirmation(self) -> None:
        payload = valid_lineage()
        payload["experiments"][2]["selection_family_id"] = "FAM-TEST"
        payload["checkpoint_selections"].append({
            "selection_id": "SEL-TEST",
            "selection_family_id": "FAM-TEST",
            "selected_experiment_id": "EXP-003",
            "all_attempt_experiment_ids": ["EXP-003"],
            "selection_basis": "EXPLORATORY_PERFORMANCE_COMPARISON",
            "selected_on": "2026-08-05T00:00:00Z",
            "multiple_attempts_artifact_sha256": digest("6"),
        })
        errors = MODULE.validate(payload)
        self.assertTrue(any("cannot optimize over confirmatory-test results" in error for error in errors))
        self.assertTrue(any("cannot itself be confirmation" in error for error in errors))

    def test_result_feedback_and_terminal_reasons_are_fail_closed(self) -> None:
        missing_result = valid_lineage()
        missing_result["experiments"][0]["result"]["artifact_sha256"] = digest("9")
        self.assertTrue(any("must resolve to node artifacts" in error for error in MODULE.validate(missing_result)))

        missing_feedback_edge = valid_lineage()
        missing_feedback_edge["experiments"][0]["feedback"]["child_experiment_ids"] = []
        self.assertTrue(any("child list does not match" in error for error in MODULE.validate(missing_feedback_edge)))

        superseded = valid_lineage()
        superseded["experiments"][0]["lifecycle_status"] = "SUPERSEDED"
        self.assertTrue(any("terminal_reason" in error for error in MODULE.validate(superseded)))

    def test_duplicate_json_keys_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "duplicate.json"
            path.write_text('{"schema_version":"1.0","schema_version":"1.0"}', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
                MODULE.load_unique_json(path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
