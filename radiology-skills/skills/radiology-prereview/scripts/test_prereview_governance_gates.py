#!/usr/bin/env python3
"""Regression tests for prereview authorization and sharing gates."""

from __future__ import annotations

import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("validate_prereview_governance_gates.py")
SPEC = importlib.util.spec_from_file_location("validate_prereview_governance_gates", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def payload_for(artifact_sha: str) -> dict[str, object]:
    payload: dict[str, object] = {
        "schema_version": "1.0",
        "project_id": "PROJECT-001",
        "manuscript_id": "MANUSCRIPT-001",
        "human_subjects_applicability": "APPLICABLE",
        "ethics_receipt": {
            "producer": "radiology-ethics",
            "branch": "human-subjects",
            "artifact_id": "ETHICS-001",
            "artifact_path": "ethics-receipt.md",
            "artifact_version": "v1",
            "artifact_sha256": artifact_sha,
            "evidence_state": "DOCUMENT_VERIFIED",
            "verdict": "PASS",
            "verified_on": "2026-08-22",
            "local_owner": "institutional ethics office",
            "activity_scope_locator": "Section 4, row ACT-001",
            "approval_locator": "Section 4, approval row",
            "consent_or_waiver_locator": "Section 5, consent row",
            "data_use_authorization_locator": "Section 5, secondary-use row",
            "non_applicability_locator": "",
            "stop_reasons": [],
        },
        "data_code_sharing_gate": {
            "status": "PASS",
            "data_availability_evidence_locator": "manuscript:Data Availability",
            "code_availability_evidence_locator": "repository-release:v1",
            "consent_dua_consistency_locator": "ETHICS-001:Section 8",
            "residual_restrictions": "controlled access",
            "owner": "radiology-data",
            "not_applicable_reason": "",
        },
        "reviewed_on": "2026-08-22",
        "governance_gate_receipt_digest": "",
    }
    payload["governance_gate_receipt_digest"] = MODULE.canonical_digest(payload)
    return payload


class GovernanceGateTests(unittest.TestCase):
    def test_document_verified_receipt_and_separate_sharing_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            artifact = root / "ethics-receipt.md"
            artifact.write_text("document-verified ethics receipt\n", encoding="utf-8")
            payload = payload_for(hashlib.sha256(artifact.read_bytes()).hexdigest())
            report = MODULE.validate(payload, artifact_root=root, require_artifact=True)
            self.assertEqual("PASS", report["status"])
            self.assertEqual("PASS", report["ethics_authorization_gate"])
            self.assertEqual("PASS", report["submission_gate"])

    def test_author_reported_ethics_is_absolute_stop(self) -> None:
        payload = payload_for("a" * 64)
        payload["ethics_receipt"]["evidence_state"] = "AUTHOR_REPORTED"
        payload["governance_gate_receipt_digest"] = MODULE.canonical_digest(payload)
        report = MODULE.validate(payload)
        self.assertEqual("PASS", report["status"])
        self.assertEqual("STOP", report["ethics_authorization_gate"])
        self.assertEqual("STOP", report["submission_gate"])

    def test_missing_consent_cannot_be_conditional(self) -> None:
        payload = payload_for("a" * 64)
        payload["ethics_receipt"]["consent_or_waiver_locator"] = ""
        payload["governance_gate_receipt_digest"] = MODULE.canonical_digest(payload)
        report = MODULE.validate(payload)
        self.assertEqual("STOP", report["ethics_authorization_gate"])

    def test_sharing_conditional_does_not_change_ethics_pass(self) -> None:
        payload = payload_for("a" * 64)
        payload["data_code_sharing_gate"]["status"] = "CONDITIONAL"
        payload["governance_gate_receipt_digest"] = MODULE.canonical_digest(payload)
        report = MODULE.validate(payload)
        self.assertEqual("PASS", report["ethics_authorization_gate"])
        self.assertEqual("CONDITIONAL", report["submission_gate"])

    def test_physical_digest_mismatch_fails_ready_validation(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "ethics-receipt.md").write_text("different\n", encoding="utf-8")
            payload = payload_for("a" * 64)
            report = MODULE.validate(payload, artifact_root=root, require_artifact=True)
            self.assertEqual("FAIL", report["status"])
            self.assertEqual("STOP", report["ethics_authorization_gate"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
