#!/usr/bin/env python3

from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("validate_scientific_handoff.py")
SPEC = importlib.util.spec_from_file_location("validate_scientific_handoff", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def valid_packet() -> dict[str, object]:
    payload: dict[str, object] = {
        "schema_version": "1.1",
        "packet_id": "WHP-001",
        "study_id": "STUDY-001",
        "study_scope": "mechanism-only",
        "source_manifest_digest": "1" * 64,
        "analysis_lock_digest": "3" * 64,
        "claim_register_sha256": "4" * 64,
        "source_artifacts": [
            {"artifact_id": "ART-101", "version": "v1", "sha256": "2" * 64},
        ],
        "modality_roles": {
            "active": ["single-cell"],
            "external_reference": ["spatial"],
            "generated_or_predicted": [],
            "proposed_validation": ["perturbation"],
        },
        "evidence_topology": {
            "independent_unit": "donor",
            "biological_hierarchy": ["donor", "sample", "cell"],
            "matched_intersections": [
                {
                    "analysis_id": "AN-01", "unit": "donor", "n": 12,
                    "not_applicable_reason": "", "definition": "QC-passing donors",
                    "source_artifact_id": "ART-101",
                }
            ],
        },
        "claims": [
            {
                "claim_id": "CLM-001", "claim_text": "A donor-level cell-state shift was associated with outcome.",
                "evidence_pointers": ["ART-101:table donor_pseudobulk"],
                "primary_evidence_state": "associated", "modality_subtype": "scRNA pseudobulk",
                "claim_link_status": "direct", "independent_unit": "donor", "matched_n": 12,
                "effect_uncertainty": "effect and 95% CI in ART-101",
                "claim_branch": "association", "branch_verdict": "PASS",
                "maximum_wording": "associated with", "protected_placement": ["Results 2", "Figure 2"],
                "residual_boundary": "No causal or spatial-localization claim",
            }
        ],
        "terminology_lock": ["donor", "cell state"],
        "writing_handoff_status": "W-HANDOFF-READY",
        "author_input_needed": [],
        "packet_sha256": "",
    }
    payload["packet_sha256"] = MODULE.canonical_digest(payload)
    return payload


class ScientificHandoffTests(unittest.TestCase):
    def test_valid_mechanism_packet_passes(self) -> None:
        report = MODULE.validate(valid_packet(), require_ready=True)
        self.assertEqual("PASS", report["status"], report)

    def test_scope_role_conflict_fails(self) -> None:
        payload = valid_packet()
        payload["modality_roles"]["active"] = ["radiomics"]  # type: ignore[index]
        payload["packet_sha256"] = MODULE.canonical_digest(payload)
        report = MODULE.validate(payload, require_ready=True)
        self.assertEqual("FAIL", report["status"])
        self.assertTrue(any("mechanism-only" in item for item in report["errors"]))

    def test_tampered_packet_digest_fails(self) -> None:
        payload = valid_packet()
        payload["claims"][0]["maximum_wording"] = "causes"  # type: ignore[index]
        report = MODULE.validate(payload, require_ready=True)
        self.assertEqual("FAIL", report["status"])
        self.assertIn("packet_sha256 does not match canonical packet content", report["errors"])

    def test_ready_packet_cannot_hide_author_input(self) -> None:
        payload = valid_packet()
        payload["author_input_needed"] = ["Confirm donor 12 exclusion"]
        payload["packet_sha256"] = MODULE.canonical_digest(payload)
        report = MODULE.validate(payload, require_ready=True)
        self.assertEqual("FAIL", report["status"])
        self.assertTrue(any("author_input_needed" in item for item in report["errors"]))

    def test_modality_roles_must_be_disjoint(self) -> None:
        payload = valid_packet()
        payload["modality_roles"]["generated_or_predicted"] = ["single-cell"]  # type: ignore[index]
        payload["packet_sha256"] = MODULE.canonical_digest(payload)
        report = MODULE.validate(payload, require_ready=True)
        self.assertEqual("FAIL", report["status"])
        self.assertTrue(any("multiple role groups" in item for item in report["errors"]))

    def test_claim_pointer_must_reference_registered_artifact(self) -> None:
        payload = valid_packet()
        payload["claims"][0]["evidence_pointers"] = ["ART-999:table 1"]  # type: ignore[index]
        payload["packet_sha256"] = MODULE.canonical_digest(payload)
        report = MODULE.validate(payload, require_ready=True)
        self.assertEqual("FAIL", report["status"])
        self.assertTrue(any("registered artifact_id" in item for item in report["errors"]))

    def test_claim_unit_and_n_must_match_linked_topology(self) -> None:
        payload = valid_packet()
        payload["claims"][0]["independent_unit"] = "lesion"  # type: ignore[index]
        payload["claims"][0]["matched_n"] = 999  # type: ignore[index]
        payload["packet_sha256"] = MODULE.canonical_digest(payload)
        report = MODULE.validate(payload, require_ready=True)
        self.assertEqual("FAIL", report["status"])
        self.assertTrue(any("independent_unit" in item for item in report["errors"]))
        self.assertTrue(any("matched_intersection" in item for item in report["errors"]))

    def test_association_cannot_pass_as_mechanistic_or_causal(self) -> None:
        for branch in ("mechanistic", "causal"):
            with self.subTest(branch=branch):
                payload = valid_packet()
                payload["claims"][0]["claim_branch"] = branch  # type: ignore[index]
                payload["claims"][0]["branch_verdict"] = "PASS"  # type: ignore[index]
                payload["claims"][0]["primary_evidence_state"] = "associated"  # type: ignore[index]
                payload["claims"][0]["claim_link_status"] = "inferred"  # type: ignore[index]
                payload["packet_sha256"] = MODULE.canonical_digest(payload)
                report = MODULE.validate(payload, require_ready=True)
                self.assertEqual("FAIL", report["status"])
                self.assertTrue(any(f"cannot PASS a {branch}" in item for item in report["errors"]))

    def test_guided_learner_state_is_preserved_and_validated(self) -> None:
        payload = valid_packet()
        payload["learner_state"] = {
            "interaction_style": "guided-learning",
            "learning_objective": "Distinguish association from mechanism",
            "target_decision": "Choose the claim ceiling for CLM-001",
            "demonstrated_level": "Can identify the donor as the independent unit",
            "baseline_attempt": "Called donor-level association mechanistic",
            "misconception_ids": ["MIS-ASSOCIATION-IS-MECHANISM"],
            "evidence_of_understanding": ["Teach-back correctly named the missing perturbation"],
            "mastery_status": "developing",
            "current_tutor_state": "T5-transfer",
            "next_transfer_task": "Classify an external-atlas concordance claim",
            "support_preference": "One worked example followed by a transfer case",
            "unresolved_learner_questions": [],
        }
        payload["packet_sha256"] = MODULE.canonical_digest(payload)
        report = MODULE.validate(payload, require_ready=True)
        self.assertEqual("PASS", report["status"], report)

    def test_mastery_cannot_be_declared_without_evidence(self) -> None:
        payload = valid_packet()
        payload["learner_state"] = {
            "interaction_style": "guided-learning",
            "learning_objective": "Distinguish association from mechanism",
            "target_decision": "Choose a claim ceiling",
            "demonstrated_level": "unknown",
            "baseline_attempt": "unknown",
            "misconception_ids": [],
            "evidence_of_understanding": [],
            "mastery_status": "demonstrated",
            "current_tutor_state": "T6-mastery",
            "next_transfer_task": "unknown",
            "support_preference": "unknown",
            "unresolved_learner_questions": [],
        }
        payload["packet_sha256"] = MODULE.canonical_digest(payload)
        report = MODULE.validate(payload, require_ready=True)
        self.assertEqual("FAIL", report["status"])
        self.assertTrue(any("requires evidence_of_understanding" in item for item in report["errors"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
