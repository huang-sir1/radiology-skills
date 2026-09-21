#!/usr/bin/env python3
"""Regression tests for the real model-output capture harness."""

from __future__ import annotations

import copy
import importlib.util
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_ROOT = Path(__file__).resolve().parent
EVAL_ROOT = SCRIPT_ROOT.parent
PRODUCT_ROOT = EVAL_ROOT.parent
REGISTRY = EVAL_ROOT / "cases.json"
MANIFEST = EVAL_ROOT.parent / ".codex-plugin" / "plugin.json"
OBSERVATION_TEMPLATE = EVAL_ROOT / "run-observation.template.json"
IMPROVEMENT_TEMPLATE = EVAL_ROOT / "improvement-candidate.template.json"
RECEIPT_SCHEMA = EVAL_ROOT / "behavior-eval-receipt.schema.json"
VALIDATOR_PATH = SCRIPT_ROOT / "validate_behavior_eval_assets.py"
BUILDER_PATH = SCRIPT_ROOT / "build_behavior_eval_receipt.py"
SPEC = importlib.util.spec_from_file_location("validate_behavior_eval_assets", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class BehaviorEvalHarnessTests(unittest.TestCase):
    def build_pilot(
        self, run_root: Path, registry_path: Path = REGISTRY, manifest_path: Path = MANIFEST,
        harness_root: Path | None = None,
    ) -> tuple[dict[str, object], dict[str, object], Path]:
        registry = MODULE.load_registry(registry_path)
        outputs = run_root / "outputs"
        outputs.mkdir()
        for case in registry["cases"]:
            (outputs / f"{case['case_id']}.txt").write_text("original\n", encoding="utf-8")
        receipt = run_root / "receipt.json"
        command = [
            sys.executable, str(BUILDER_PATH), "--registry", str(registry_path),
            "--manifest", str(manifest_path), "--product-root", str(PRODUCT_ROOT),
            "--outputs-dir", str(outputs),
            "--run-id", "harness-test", "--provider", "provider", "--model", "model",
            "--model-version", "version", "--output", str(receipt),
        ]
        if harness_root is not None:
            command.extend(["--harness-root", str(harness_root)])
        subprocess.run(command, check=True, capture_output=True, text=True, encoding="utf-8")
        return registry, json.loads(receipt.read_text(encoding="utf-8")), receipt

    def write_observation(
        self,
        run_root: Path,
        observation_id: str,
        run_id: str,
        prompt_id: str,
        *,
        severity: str = "P2",
        defect_class: str = "HANDOFF_GAP",
        invariant_id: str = "INV-OWNER-HANDOFF",
        defect_signature: str = "SIG-MISSING-OWNER-HANDOFF",
        root_cause_state: str = "SUPPORTED-ROUTER-OMITS-DEPENDENCY",
        affected_contract: str = "behavior-evals/cases.json:dependency_skills",
    ) -> tuple[Path, dict[str, object]]:
        observation = MODULE.load_unique_json(OBSERVATION_TEMPLATE)
        manifest = MODULE.load_unique_json(MANIFEST)
        raw_output = run_root / f"{observation_id}.txt"
        raw_output.write_text("captured output\n", encoding="utf-8")
        observation.update({
            "observation_id": observation_id,
            "run_id": run_id,
            "case_id_or_prompt_sha256": prompt_id,
            "installed_product": {
                "name": manifest["name"],
                "version": manifest["version"],
                "manifest_sha256": hashlib.sha256(MANIFEST.read_bytes()).hexdigest(),
            },
            "execution_identity": {
                "provider": "provider",
                "model": "model",
                "model_version": "version",
                "client": "Codex",
                "system_context_digest": "not-captured",
            },
            "artifact_evidence": [{
                "role": "raw-output",
                "path_or_uri": raw_output.name,
                "sha256": hashlib.sha256(raw_output.read_bytes()).hexdigest(),
                "exact_locator": "line 1",
            }],
            "expected_behavior": "The invariant remains satisfied.",
            "observed_behavior": "The invariant was broken in the captured output.",
            "invariant_id": invariant_id,
            "defect_signature": defect_signature,
            "root_cause_state": root_cause_state,
            "affected_contract": affected_contract,
            "defect_class": defect_class,
            "severity": severity,
            "workaround_or_none": "manual owner handoff",
            "observer_role": "independent evaluator",
            "observed_on": "2026-08-23T00:00:00Z",
        })
        path = run_root / f"{observation_id}.json"
        path.write_text(json.dumps(observation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return path, observation

    def write_candidate(
        self, run_root: Path, observations: list[tuple[Path, dict[str, object]]],
    ) -> tuple[Path, dict[str, object]]:
        candidate = MODULE.load_unique_json(IMPROVEMENT_TEMPLATE)
        candidate.update({
            "candidate_id": "IC-001",
            "status": "READY_FOR_REVIEW",
            "observation_ids": sorted(str(item[1]["observation_id"]) for item in observations),
            "observation_artifacts": [{
                "observation_id": str(observation["observation_id"]),
                "path": path.name,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            } for path, observation in observations],
            "target_file": "behavior-evals/cases.json",
            "smallest_change": "Bind the missing dependency owner.",
            "affected_routes": ["forward-behavior-evaluation"],
            "regression_to_add": "dependency-owner-closure",
            "source_freshness_impact": "none",
            "rollback": "revert the dependency binding",
            "scientific_owner": "evaluation owner",
            "independent_reviewer": "release reviewer",
            "decision_evidence_locator": "cited observation artifacts",
        })
        defect_classes = {str(item[1]["defect_class"]) for item in observations}
        invariant_ids = {str(item[1]["invariant_id"]) for item in observations}
        signatures = {str(item[1]["defect_signature"]) for item in observations}
        root_causes = {str(item[1]["root_cause_state"]) for item in observations}
        candidate["evidence_pattern"].update({
            "distinct_run_ids": sorted({str(item[1]["run_id"]) for item in observations}),
            "distinct_case_or_prompt_ids": sorted({
                str(item[1]["case_id_or_prompt_sha256"]) for item in observations
            }),
            "repeated_defect_class": next(iter(defect_classes)) if len(defect_classes) == 1 else "",
            "repeated_invariant_id": next(iter(invariant_ids)) if len(invariant_ids) == 1 else "",
            "repeated_defect_signature": next(iter(signatures)) if len(signatures) == 1 else "",
            "repeated_root_cause_state": next(iter(root_causes)) if len(root_causes) == 1 else "",
            "affected_contracts": sorted({
                str(item[1]["affected_contract"]) for item in observations
            }),
            "highest_severity": min(
                (str(item[1]["severity"]) for item in observations),
                key=lambda value: MODULE.SEVERITY_RANK[value],
            ),
            "high_severity_invariant_break": any(
                item[1]["severity"] in {"P0", "P1"}
                and item[1]["defect_class"] != "NO_DEFECT"
                for item in observations
            ),
            "basis": "physical observations cited by path and SHA-256",
        })
        path = run_root / "candidate.json"
        path.write_text(json.dumps(candidate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return path, candidate

    def complete_human_record(
        self, run_root: Path, registry: dict[str, object], receipt: dict[str, object],
    ) -> Path:
        output_by_case = {item["case_id"]: item for item in receipt["outputs"]}
        human: dict[str, object] = {
            "schema_version": "1.0",
            "run_id": receipt["run_id"],
            "receipt_digest_reviewed": receipt["capture_receipt_digest"],
            "adjudication_status": "HUMAN_ADJUDICATED",
            "adjudicator_roles": ["qualified-methods-reviewer"],
            "qualification_basis": "Recorded domain-methods experience; identity is not machine-authenticated.",
            "conflict_of_interest_statement": "No declared conflict for this fixture.",
            "adjudicated_on": "2026-08-22",
            "case_reviews": [],
            "disagreements_and_resolution": "No disagreement in this single-reviewer fixture.",
            "overall_decision": "PASS",
            "release_decision_owner": "named-release-review-role",
            "human_adjudication_digest": "",
        }
        for case in registry["cases"]:
            case_id = case["case_id"]
            human["case_reviews"].append({
                "case_id": case_id,
                "output_sha256": output_by_case[case_id]["output_sha256"],
                "required_behavior_scores": [
                    {"behavior": behavior, "score": 2, "evidence_locator": "output:line 1"}
                    for behavior in case["required_behaviors"]
                ],
                "prohibited_behavior_findings": [
                    {"behavior": behavior, "observed": False, "evidence_locator": "full-output review"}
                    for behavior in case["prohibited_behaviors"]
                ],
                "rationale": "Fixture records a complete all-PASS adjudication shape.",
                "decision": "PASS",
            })
        human["human_adjudication_digest"] = MODULE.canonical_digest(
            human, "human_adjudication_digest",
        )
        path = run_root / "human-adjudication.json"
        path.write_text(json.dumps(human, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return path

    def test_registry_hashes_and_prompt_class_coverage(self) -> None:
        registry = MODULE.load_registry(REGISTRY)
        self.assertEqual([], MODULE.validate_registry(registry, PRODUCT_ROOT / "skills"))
        self.assertTrue(all("dependency_skills" in case for case in registry["cases"]))

        invalid = copy.deepcopy(registry)
        invalid["cases"][0]["dependency_skills"] = [
            invalid["cases"][0]["target_skill"],
            "radiology-not-a-real-skill",
            "radiology-not-a-real-skill",
        ]
        errors = MODULE.validate_registry(invalid, PRODUCT_ROOT / "skills")
        self.assertTrue(any("must not repeat target_skill" in error for error in errors))
        self.assertTrue(any("contains duplicates" in error for error in errors))
        self.assertTrue(any("does not exist" in error for error in errors))

        uncovered = copy.deepcopy(registry)
        uncovered["cases"] = [
            case for case in uncovered["cases"]
            if case["target_skill"] != "radiology-design"
        ]
        errors = MODULE.validate_registry(uncovered, PRODUCT_ROOT / "skills")
        self.assertTrue(any("radiology-design" in error for error in errors))

        unmarked = copy.deepcopy(registry)
        del unmarked["cases"][0]["release_blocking"]
        errors = MODULE.validate_registry(unmarked, PRODUCT_ROOT / "skills")
        self.assertTrue(any("release_blocking" in error for error in errors))

    def test_learning_loop_templates_are_fail_closed(self) -> None:
        self.assertEqual([], MODULE.validate_learning_templates(EVAL_ROOT))
        observation = MODULE.load_unique_json(OBSERVATION_TEMPLATE)
        candidate = MODULE.load_unique_json(IMPROVEMENT_TEMPLATE)
        self.assertIs(False, observation["persistent_change_authorized"])
        self.assertIs(False, candidate["persistent_change_authorized"])

    def test_receipt_schema_binds_harness_and_forbids_comparison_claims(self) -> None:
        schema = MODULE.load_unique_json(RECEIPT_SCHEMA)
        self.assertEqual("1.2", schema["properties"]["schema_version"]["const"])
        self.assertIn("evaluation_harness", schema["required"])
        self.assertIn("comparison_claim_eligible", schema["required"])
        self.assertIs(False, schema["properties"]["comparison_claim_eligible"]["const"])

    def test_improvement_candidate_recomputes_repeated_pattern_from_observations(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            run_root = Path(temp)
            first = self.write_observation(run_root, "OBS-001", "RUN-001", "CASE-001")
            second = self.write_observation(run_root, "OBS-002", "RUN-002", "CASE-002")
            candidate_path, candidate = self.write_candidate(run_root, [first, second])
            self.assertEqual([], MODULE.validate_improvement_candidate(
                candidate, candidate_path=candidate_path,
            ))

            candidate["evidence_pattern"]["distinct_run_ids"] = ["RUN-SELF-REPORTED"]
            errors = MODULE.validate_improvement_candidate(candidate, candidate_path=candidate_path)
            self.assertTrue(any("distinct_run_ids does not match" in error for error in errors))

            candidate["persistent_change_authorized"] = True
            errors = MODULE.validate_improvement_candidate(candidate, candidate_path=candidate_path)
            self.assertTrue(any("must remain false" in error for error in errors))

    def test_same_defect_class_alone_does_not_satisfy_repetition_gate(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            run_root = Path(temp)
            first = self.write_observation(run_root, "OBS-001", "RUN-001", "CASE-001")
            second = self.write_observation(
                run_root, "OBS-002", "RUN-002", "CASE-002",
                defect_signature="SIG-DIFFERENT-FAILURE",
            )
            candidate_path, candidate = self.write_candidate(run_root, [first, second])
            candidate["evidence_pattern"]["repeated_defect_signature"] = "SIG-MISSING-OWNER-HANDOFF"
            errors = MODULE.validate_improvement_candidate(candidate, candidate_path=candidate_path)
            self.assertTrue(any("repeated_defect_signature does not match" in error for error in errors))
            self.assertTrue(any("same invariant, defect signature" in error for error in errors))

    def test_repetition_gate_requires_same_invariant_and_root_cause(self) -> None:
        variants = (
            ("invariant_id", "INV-DIFFERENT", "repeated_invariant_id"),
            ("root_cause_state", "SUPPORTED-DIFFERENT-CAUSE", "repeated_root_cause_state"),
        )
        for observation_field, different_value, pattern_field in variants:
            with self.subTest(observation_field=observation_field), tempfile.TemporaryDirectory() as temp:
                run_root = Path(temp)
                first = self.write_observation(run_root, "OBS-001", "RUN-001", "CASE-001")
                second_options = {observation_field: different_value}
                second = self.write_observation(
                    run_root, "OBS-002", "RUN-002", "CASE-002", **second_options,
                )
                candidate_path, candidate = self.write_candidate(run_root, [first, second])
                candidate["evidence_pattern"][pattern_field] = str(first[1][observation_field])
                errors = MODULE.validate_improvement_candidate(candidate, candidate_path=candidate_path)
                self.assertTrue(any(f"{pattern_field} does not match" in error for error in errors))
                self.assertTrue(any("same invariant, defect signature" in error for error in errors))

    def test_observation_sha_tamper_blocks_ready_for_review(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            run_root = Path(temp)
            first = self.write_observation(run_root, "OBS-001", "RUN-001", "CASE-001")
            second = self.write_observation(run_root, "OBS-002", "RUN-002", "CASE-002")
            candidate_path, candidate = self.write_candidate(run_root, [first, second])
            first[0].write_text("{}\n", encoding="utf-8")
            errors = MODULE.validate_improvement_candidate(candidate, candidate_path=candidate_path)
            self.assertTrue(any("observation artifact SHA-256 mismatch" in error for error in errors))
            self.assertTrue(any("every observation artifact" in error for error in errors))

    def test_single_p1_invariant_break_retains_emergency_review_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            run_root = Path(temp)
            observation = self.write_observation(
                run_root, "OBS-P1", "RUN-P1", "CASE-P1",
                severity="P1", root_cause_state="UNRESOLVED",
            )
            candidate_path, candidate = self.write_candidate(run_root, [observation])
            self.assertEqual([], MODULE.validate_improvement_candidate(
                candidate, candidate_path=candidate_path,
            ))

    def test_builder_captures_outputs_but_does_not_claim_human_pass(self) -> None:
        registry = MODULE.load_registry(REGISTRY)
        with tempfile.TemporaryDirectory() as temp:
            run_root = Path(temp)
            outputs = run_root / "outputs"
            outputs.mkdir()
            for case in registry["cases"]:
                (outputs / f"{case['case_id']}.txt").write_text(
                    f"Raw model output for {case['case_id']}\n", encoding="utf-8",
                )
            receipt = run_root / "behavior-eval-receipt.json"
            result = subprocess.run([
                sys.executable, str(BUILDER_PATH),
                "--registry", str(REGISTRY),
                "--manifest", str(MANIFEST),
                "--product-root", str(PRODUCT_ROOT),
                "--outputs-dir", str(outputs),
                "--run-id", "pilot-test",
                "--provider", "test-provider",
                "--model", "test-model",
                "--model-version", "test-version",
                "--output", str(receipt),
            ], check=False, capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            payload = json.loads(receipt.read_text(encoding="utf-8"))
            errors, details = MODULE.validate_receipt(payload, REGISTRY, registry, run_root)
            self.assertEqual([], errors)
            self.assertEqual("NOT_ADJUDICATED", details["behavioral_verdict"])
            self.assertFalse(payload["release_claim_eligible"])
            self.assertFalse(payload["comparison_claim_eligible"])
            self.assertEqual(
                MODULE.required_skill_ids(registry),
                {item["skill_id"] for item in payload["evaluated_skill_bundle"]},
            )
            self.assertGreater(payload["evaluation_harness"]["file_count"], 5)

    def test_harness_tree_tamper_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            run_root = Path(temp)
            harness_copy = run_root / "behavior-evals"
            shutil.copytree(EVAL_ROOT, harness_copy)
            registry_path = harness_copy / "cases.json"
            registry, receipt, _ = self.build_pilot(
                run_root, registry_path=registry_path, harness_root=harness_copy,
            )
            (harness_copy / "rubric.md").write_text("tampered rubric\n", encoding="utf-8")
            errors, _ = MODULE.validate_receipt(
                receipt, registry_path, registry, run_root,
            )
            self.assertTrue(any("evaluation_harness.tree_sha256 mismatch" in error for error in errors))

    def test_not_captured_context_cannot_be_promoted_to_comparison_claim(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            run_root = Path(temp)
            registry, receipt, _ = self.build_pilot(run_root)
            self.assertEqual("not-captured", receipt["execution_identity"]["system_context_digest"])
            receipt["comparison_claim_eligible"] = True
            receipt["behavior_eval_receipt_digest"] = MODULE.canonical_digest(
                receipt, "behavior_eval_receipt_digest",
            )
            errors, _ = MODULE.validate_receipt(receipt, REGISTRY, registry, run_root)
            self.assertTrue(any("forbids cross-version comparison" in error for error in errors))
            self.assertTrue(any("comparison_claim_eligible must remain false" in error for error in errors))

    def test_output_tamper_breaks_receipt(self) -> None:
        registry = MODULE.load_registry(REGISTRY)
        with tempfile.TemporaryDirectory() as temp:
            run_root = Path(temp)
            outputs = run_root / "outputs"
            outputs.mkdir()
            for case in registry["cases"]:
                (outputs / f"{case['case_id']}.txt").write_text("original\n", encoding="utf-8")
            receipt = run_root / "receipt.json"
            subprocess.run([
                sys.executable, str(BUILDER_PATH), "--registry", str(REGISTRY),
                "--manifest", str(MANIFEST), "--product-root", str(PRODUCT_ROOT),
                "--outputs-dir", str(outputs),
                "--run-id", "tamper-test", "--provider", "provider", "--model", "model",
                "--model-version", "version", "--output", str(receipt),
            ], check=True, capture_output=True, text=True, encoding="utf-8")
            first = registry["cases"][0]["case_id"]
            (outputs / f"{first}.txt").write_text("tampered\n", encoding="utf-8")
            payload = json.loads(receipt.read_text(encoding="utf-8"))
            errors, _ = MODULE.validate_receipt(payload, REGISTRY, registry, run_root)
            self.assertTrue(any("output_sha256 mismatch" in error for error in errors))

    def test_manifest_and_registry_physical_tamper_are_detected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            run_root = Path(temp)
            manifest_copy = run_root / "plugin.json"
            manifest_copy.write_bytes(MANIFEST.read_bytes())
            registry_copy = run_root / "cases.json"
            registry_copy.write_bytes(REGISTRY.read_bytes())
            registry, receipt, _ = self.build_pilot(run_root, registry_copy, manifest_copy)
            manifest_copy.write_text("{}\n", encoding="utf-8")
            registry_copy.write_text("{}\n", encoding="utf-8")
            errors, _ = MODULE.validate_receipt(receipt, registry_copy, registry, run_root)
            self.assertTrue(any("manifest SHA-256 mismatch" in error for error in errors))
            self.assertTrue(any("registry SHA-256 mismatch" in error for error in errors))

    def test_target_skill_tree_tamper_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            run_root = Path(temp)
            registry, receipt, _ = self.build_pilot(run_root)
            receipt["evaluated_skill_bundle"][0]["tree_sha256"] = "f" * 64
            receipt["capture_receipt_digest"] = MODULE.capture_digest(receipt)
            receipt["behavior_eval_receipt_digest"] = MODULE.canonical_digest(
                receipt, "behavior_eval_receipt_digest",
            )
            errors, _ = MODULE.validate_receipt(receipt, REGISTRY, registry, run_root)
            self.assertTrue(any("tree_sha256 mismatch" in error for error in errors))

    def test_complete_human_record_is_structural_only_and_cannot_be_release_eligible(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            run_root = Path(temp)
            registry, receipt, _ = self.build_pilot(run_root)
            human_path = self.complete_human_record(run_root, registry, receipt)
            receipt["run_state"] = "HUMAN_ADJUDICATION_RECORDED"
            receipt["human_adjudication"] = {
                "status": "HUMAN_ADJUDICATED",
                "artifact_path": human_path.name,
                "artifact_sha256": hashlib.sha256(human_path.read_bytes()).hexdigest(),
            }
            receipt["release_claim_eligible"] = False
            receipt["behavior_eval_receipt_digest"] = MODULE.canonical_digest(
                receipt, "behavior_eval_receipt_digest",
            )
            errors, details = MODULE.validate_receipt(receipt, REGISTRY, registry, run_root)
            self.assertEqual([], errors)
            self.assertEqual("HUMAN_RECORD_COMPLETE_NOT_AUTHENTICATED", details["behavioral_verdict"])

            receipt["release_claim_eligible"] = True
            receipt["behavior_eval_receipt_digest"] = MODULE.canonical_digest(
                receipt, "behavior_eval_receipt_digest",
            )
            errors, _ = MODULE.validate_receipt(receipt, REGISTRY, registry, run_root)
            self.assertTrue(any("must remain false" in error for error in errors))

    def test_fake_or_tampered_human_record_cannot_make_release_eligible(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            run_root = Path(temp)
            registry, receipt, _ = self.build_pilot(run_root)
            fake = {
                "schema_version": "1.0",
                "run_id": receipt["run_id"],
                "receipt_digest_reviewed": receipt["capture_receipt_digest"],
                "adjudication_status": "HUMAN_ADJUDICATED",
                "adjudicator_roles": [],
                "qualification_basis": "",
                "conflict_of_interest_statement": "",
                "adjudicated_on": "",
                "case_reviews": [],
                "disagreements_and_resolution": "",
                "overall_decision": "PASS",
                "release_decision_owner": "",
                "human_adjudication_digest": "",
            }
            fake["human_adjudication_digest"] = MODULE.canonical_digest(
                fake, "human_adjudication_digest",
            )
            human_path = run_root / "fake-human.json"
            human_path.write_text(json.dumps(fake), encoding="utf-8")
            receipt["run_state"] = "HUMAN_ADJUDICATION_RECORDED"
            receipt["human_adjudication"] = {
                "status": "HUMAN_ADJUDICATED",
                "artifact_path": human_path.name,
                "artifact_sha256": hashlib.sha256(human_path.read_bytes()).hexdigest(),
            }
            receipt["release_claim_eligible"] = True
            receipt["behavior_eval_receipt_digest"] = MODULE.canonical_digest(
                receipt, "behavior_eval_receipt_digest",
            )
            errors, _ = MODULE.validate_receipt(receipt, REGISTRY, registry, run_root)
            self.assertTrue(any("qualification_basis" in error for error in errors))
            self.assertTrue(any("every frozen case" in error for error in errors))
            self.assertTrue(any("must remain false" in error for error in errors))

            human_path.write_text("tampered\n", encoding="utf-8")
            errors, _ = MODULE.validate_receipt(receipt, REGISTRY, registry, run_root)
            self.assertTrue(any("artifact SHA-256 mismatch" in error for error in errors))

    def test_duplicate_json_keys_fail_closed_at_external_artifact_boundaries(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            run_root = Path(temp)

            duplicate_registry = run_root / "duplicate-registry.json"
            duplicate_registry.write_text(
                '{"schema_version":"1.0","schema_version":"1.0","cases":[]}',
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "duplicate JSON key: schema_version"):
                MODULE.load_registry(duplicate_registry)

            duplicate_manifest = run_root / "duplicate-manifest.json"
            duplicate_manifest.write_text(
                '{"name":"first","name":"second","version":"1.2.0"}',
                encoding="utf-8",
            )
            builder_result = subprocess.run([
                sys.executable, str(BUILDER_PATH), "--registry", str(REGISTRY),
                "--manifest", str(duplicate_manifest), "--product-root", str(PRODUCT_ROOT),
                "--outputs-dir", str(run_root),
                "--run-id", "duplicate-test", "--provider", "provider", "--model", "model",
                "--model-version", "version", "--output", str(run_root / "unused.json"),
            ], check=False, capture_output=True, text=True, encoding="utf-8")
            self.assertNotEqual(0, builder_result.returncode)
            self.assertIn("duplicate JSON key: name", builder_result.stdout + builder_result.stderr)

            duplicate_receipt = run_root / "duplicate-receipt.json"
            duplicate_receipt.write_text(
                '{"schema_version":"1.0","schema_version":"1.0"}', encoding="utf-8",
            )
            validator_result = subprocess.run([
                sys.executable, str(VALIDATOR_PATH), "--registry", str(REGISTRY),
                "--receipt", str(duplicate_receipt), "--run-root", str(run_root),
            ], check=False, capture_output=True, text=True, encoding="utf-8")
            self.assertNotEqual(0, validator_result.returncode)
            self.assertIn("duplicate JSON key: schema_version", validator_result.stdout)

            human_run = run_root / "human-run"
            human_run.mkdir()
            registry, receipt, _ = self.build_pilot(human_run)
            human_path = self.complete_human_record(human_run, registry, receipt)
            human_text = human_path.read_text(encoding="utf-8").replace(
                '  "schema_version": "1.0",',
                '  "schema_version": "1.0",\n  "schema_version": "1.0",',
                1,
            )
            human_path.write_text(human_text, encoding="utf-8")
            receipt["run_state"] = "HUMAN_ADJUDICATION_RECORDED"
            receipt["human_adjudication"] = {
                "status": "HUMAN_ADJUDICATED",
                "artifact_path": human_path.name,
                "artifact_sha256": hashlib.sha256(human_path.read_bytes()).hexdigest(),
            }
            receipt["release_claim_eligible"] = True
            receipt["behavior_eval_receipt_digest"] = MODULE.canonical_digest(
                receipt, "behavior_eval_receipt_digest",
            )
            errors, _ = MODULE.validate_receipt(
                receipt, REGISTRY, registry, human_run,
            )
            self.assertTrue(any("duplicate JSON key: schema_version" in error for error in errors))
            self.assertTrue(any("must remain false" in error for error in errors))

    def test_missing_execution_identity_cannot_pass_with_an_empty_capture_digest(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            run_root = Path(temp)
            registry, receipt, _ = self.build_pilot(run_root)
            del receipt["execution_identity"]
            receipt["capture_receipt_digest"] = ""
            receipt["behavior_eval_receipt_digest"] = MODULE.canonical_digest(
                receipt, "behavior_eval_receipt_digest",
            )
            errors, _ = MODULE.validate_receipt(receipt, REGISTRY, registry, run_root)
            self.assertTrue(any("receipt missing required fields: execution_identity" in error for error in errors))
            self.assertTrue(any("capture receipt missing fields: execution_identity" in error for error in errors))
            self.assertTrue(any("execution_identity must be an object" in error for error in errors))


if __name__ == "__main__":
    unittest.main(verbosity=2)
