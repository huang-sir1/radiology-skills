#!/usr/bin/env python3
"""Regression tests for the canonical scientific-prereview receipt."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("validate_scientific_prereview_receipt.py")
SPEC = importlib.util.spec_from_file_location("validate_scientific_prereview_receipt", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def valid_receipt() -> dict[str, object]:
    artifact_digest = "4" * 64
    payload: dict[str, object] = {
        "schema_version": "1.2",
        "receipt_id": "SPR-001",
        "project_id": "PROJECT-001",
        "manuscript_id": "MANUSCRIPT-001",
        "study_scope": "mechanism-only",
        "review_route": "mechanism-review",
        "project_state_digest": "6" * 64,
        "modality_role_digest": "7" * 64,
        "analysis_lock_digest": "1" * 64,
        "claim_registry_digest": "2" * 64,
        "scientific_handoff_digest": "3" * 64,
        "source_artifacts": [{
            "artifact_id": "manuscript-v2",
            "role": "revised-manuscript",
            "version": "v2",
            "sha256": artifact_digest,
        }],
        "findings": [{
            "finding_id": "F-001",
            "severity": "P1",
            "criterion": "Donor is the independent unit and causal wording is absent.",
            "affected_claim_ids": ["CLM-001"],
            "source_artifact_id": "manuscript-v2",
            "source_artifact_sha256": artifact_digest,
            "evidence_anchor": "Results paragraph 3",
            "minimum_repair": "Report donor n and retain association wording.",
            "repair_owner": "radiology-radiogenomics",
            "closure_evidence_required": "Donor-level estimate plus bounded claim in final manuscript.",
            "next_gate": "radiology-prereview re-review",
            "source_review_state": "PARTIAL",
            "prior_verification_state": "NOT_VERIFIED",
            "verification_state": "VERIFIED",
            "verification_evidence_locator": "manuscript-v2:Results paragraph 3",
            "state_change_evidence": "Donor n and association wording were added and rechecked.",
            "residual_boundary": "No causal or intervention claim.",
            "required_for_pass": True,
            "not_applicable_reason": "",
        }],
        "reviewer_roles": ["mechanism", "methods-statistics", "editor-synthesis"],
        "reviewed_on": "2026-08-22",
        "unresolved_placeholder_count": 0,
        "scientific_prereview_state": "SCIENTIFIC_PREREVIEW_PASS",
        "scientific_prereview_receipt_digest": "",
    }
    payload["scientific_prereview_receipt_digest"] = MODULE.canonical_digest(payload)
    return payload


def valid_evidence_synthesis_receipt() -> dict[str, object]:
    payload = valid_receipt()
    payload["receipt_id"] = "SPR-ES-001"
    payload["study_scope"] = "evidence-synthesis"
    payload["review_route"] = "evidence-synthesis-review"
    payload["scientific_handoff_digest"] = "not-applicable"
    payload["reviewer_roles"] = ["evidence-synthesis", "methods-statistics", "editor-synthesis"]
    payload["source_artifacts"] = [
        {
            "artifact_id": "manuscript-v2",
            "role": "revised-manuscript",
            "version": "v2",
            "sha256": "4" * 64,
        },
        *[
            {
                "artifact_id": f"review-{role}",
                "role": role,
                "version": "v1",
                "sha256": f"{index:x}" * 64,
            }
            for index, role in enumerate(sorted(MODULE.EVIDENCE_SYNTHESIS_ARTIFACT_ROLES), start=5)
        ],
    ]
    payload["scientific_prereview_receipt_digest"] = MODULE.canonical_digest(payload)
    return payload


class ScientificPrereviewReceiptTests(unittest.TestCase):
    def refresh_and_validate(self, payload: dict[str, object]) -> dict[str, object]:
        payload["scientific_prereview_receipt_digest"] = MODULE.canonical_digest(payload)
        return MODULE.validate(payload)

    def test_valid_pass_receipt(self) -> None:
        self.assertEqual("PASS", MODULE.validate(valid_receipt())["status"])

    def test_valid_evidence_synthesis_receipt_consumes_frozen_review_artifacts(self) -> None:
        self.assertEqual(
            "PASS", MODULE.validate(valid_evidence_synthesis_receipt())["status"]
        )

    def test_evidence_synthesis_receipt_rejects_missing_review_artifact_role(self) -> None:
        payload = valid_evidence_synthesis_receipt()
        payload["source_artifacts"] = [
            item for item in payload["source_artifacts"] if item["role"] != "certainty"
        ]
        result = self.refresh_and_validate(payload)
        self.assertEqual("FAIL", result["status"])
        self.assertTrue(any("missing frozen roles: certainty" in error for error in result["errors"]))

    def test_evidence_synthesis_receipt_rejects_radiogenomics_handoff(self) -> None:
        payload = valid_evidence_synthesis_receipt()
        payload["scientific_handoff_digest"] = "3" * 64
        result = self.refresh_and_validate(payload)
        self.assertEqual("FAIL", result["status"])
        self.assertTrue(any("must not require" in error for error in result["errors"]))

    def test_cli_writes_and_validates_canonical_digest(self) -> None:
        payload = valid_receipt()
        payload["scientific_prereview_receipt_digest"] = ""
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "receipt.json"
            path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(MODULE_PATH), str(path), "--write-digest"],
                check=False, capture_output=True, text=True, encoding="utf-8",
            )
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            written = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(MODULE.canonical_digest(written), written["scientific_prereview_receipt_digest"])

    def test_semantic_tamper_invalidates_digest(self) -> None:
        payload = valid_receipt()
        payload["scientific_prereview_state"] = "SCIENTIFIC_PREREVIEW_CONDITIONAL"
        result = MODULE.validate(payload)
        self.assertEqual("FAIL", result["status"])
        self.assertTrue(any("does not match canonical" in error for error in result["errors"]))

    def test_missing_finding_field_fails(self) -> None:
        payload = valid_receipt()
        del payload["findings"][0]["affected_claim_ids"]
        result = self.refresh_and_validate(payload)
        self.assertEqual("FAIL", result["status"])
        self.assertTrue(any("affected_claim_ids" in error for error in result["errors"]))

    def test_finding_requires_accountable_owner_and_next_gate(self) -> None:
        for field in ("repair_owner", "next_gate"):
            with self.subTest(field=field):
                payload = valid_receipt()
                payload["findings"][0][field] = ""
                result = self.refresh_and_validate(payload)
                self.assertEqual("FAIL", result["status"])
                self.assertTrue(any(field in error for error in result["errors"]))

    def test_not_verified_finding_cannot_hide_under_global_pass(self) -> None:
        payload = valid_receipt()
        payload["findings"][0]["verification_state"] = "NOT_VERIFIED"
        result = self.refresh_and_validate(payload)
        self.assertEqual("FAIL", result["status"])
        self.assertTrue(any("blocks SCIENTIFIC_PREREVIEW_PASS" in error for error in result["errors"]))

    def test_not_verified_upgrade_requires_new_bound_evidence(self) -> None:
        payload = valid_receipt()
        payload["findings"][0]["verification_evidence_locator"] = ""
        payload["findings"][0]["state_change_evidence"] = ""
        result = self.refresh_and_validate(payload)
        self.assertEqual("FAIL", result["status"])
        self.assertTrue(any("cannot upgrade NOT_VERIFIED" in error for error in result["errors"]))

    def test_closure_locator_must_bind_registered_artifact(self) -> None:
        payload = valid_receipt()
        payload["findings"][0]["verification_evidence_locator"] = "unregistered:Results paragraph 3"
        result = self.refresh_and_validate(payload)
        self.assertEqual("FAIL", result["status"])
        self.assertTrue(any("registered artifact_id" in error for error in result["errors"]))

    def test_not_verified_cannot_be_converted_to_not_applicable(self) -> None:
        payload = valid_receipt()
        payload["findings"][0]["verification_state"] = "NOT_APPLICABLE"
        payload["findings"][0]["verification_evidence_locator"] = ""
        payload["findings"][0]["state_change_evidence"] = ""
        payload["findings"][0]["not_applicable_reason"] = "The response labels it irrelevant."
        result = self.refresh_and_validate(payload)
        self.assertEqual("FAIL", result["status"])
        self.assertTrue(any("prior NOT_VERIFIED" in error for error in result["errors"]))

    def test_p0_or_p1_cannot_be_marked_nonblocking(self) -> None:
        for severity in ("P0", "P1"):
            with self.subTest(severity=severity):
                payload = valid_receipt()
                payload["findings"][0]["severity"] = severity
                payload["findings"][0]["required_for_pass"] = False
                payload["findings"][0]["verification_state"] = "NOT_VERIFIED"
                result = self.refresh_and_validate(payload)
                self.assertEqual("FAIL", result["status"])
                self.assertTrue(any("P0/P1" in error for error in result["errors"]))

    def test_finding_source_digest_is_registry_bound(self) -> None:
        payload = valid_receipt()
        payload["findings"][0]["source_artifact_sha256"] = "5" * 64
        result = self.refresh_and_validate(payload)
        self.assertEqual("FAIL", result["status"])
        self.assertTrue(any("differs from artifact registry" in error for error in result["errors"]))

    def test_mechanism_scope_cannot_use_imaging_only_route(self) -> None:
        payload = valid_receipt()
        payload["review_route"] = "imaging-panel"
        result = self.refresh_and_validate(payload)
        self.assertEqual("FAIL", result["status"])
        self.assertTrue(any("review_route must be mechanism-review" in error for error in result["errors"]))

    def test_global_pass_rejects_placeholders(self) -> None:
        payload = valid_receipt()
        payload["findings"][0]["residual_boundary"] = "AUTHOR_INPUT_NEEDED"
        result = self.refresh_and_validate(payload)
        self.assertEqual("FAIL", result["status"])
        self.assertTrue(any("cannot contain placeholder" in error for error in result["errors"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
