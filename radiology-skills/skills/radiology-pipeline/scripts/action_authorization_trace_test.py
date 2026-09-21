#!/usr/bin/env python3
"""Positive and adversarial tests for action authorization traces."""

from __future__ import annotations

import copy
import importlib.util
import unittest
from datetime import datetime, timezone
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("validate_action_authorization_trace.py")
TEMPLATE = MODULE_PATH.parents[1] / "assets" / "action_authorization_trace.template.json"
SPEC = importlib.util.spec_from_file_location("validate_action_authorization_trace", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
VALIDATION_TIME = datetime(2026, 8, 23, 12, 30, tzinfo=timezone.utc)


class ActionAuthorizationTraceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.template = MODULE.load_trace(TEMPLATE)

    def fresh(self) -> dict:
        return copy.deepcopy(self.template)

    def resign(self, payload: dict) -> dict:
        return MODULE.refresh_trace_digests(payload)

    def validate(self, payload: dict) -> list[str]:
        return MODULE.validate_trace(payload, validation_time=VALIDATION_TIME)

    def assert_has(self, errors: list[str], phrase: str) -> None:
        self.assertTrue(any(phrase in error for error in errors), errors)

    def test_positive_workspace_write_template(self) -> None:
        self.assertEqual([], self.validate(self.fresh()))

    def test_positive_read_only_without_approval(self) -> None:
        payload = self.fresh()
        payload["action_class"] = "READ_ONLY"
        target = payload["target_scope"]["targets"][0]
        target["allowed_operations"] = ["READ"]
        authorization = payload["authorization"]
        authorization["state"] = "NOT_REQUIRED"
        authorization["approver"] = {"actor_id": "policy:read-only", "role": "POLICY"}
        authorization["evidence"]["evidence_type"] = "NOT_APPLICABLE"
        authorization["approved_at"] = None
        authorization["expires_at"] = None
        authorization["revoked_at"] = None
        event = payload["execution"]["events"][0]
        event["operation"] = "READ"
        event["after_sha256"] = event["before_sha256"]
        self.resign(payload)
        self.assertEqual([], self.validate(payload))

    def test_positive_requested_external_action_is_blocked_before_call(self) -> None:
        payload = self.fresh()
        payload["action_class"] = "EXTERNAL_STATE_CHANGE"
        payload["target_scope"]["targets"] = [
            {
                "target_id": "service://account/resource-001",
                "target_kind": "EXTERNAL_RESOURCE",
                "allowed_operations": ["UPDATE_EXTERNAL"],
            }
        ]
        authorization = payload["authorization"]
        authorization["state"] = "REQUESTED"
        authorization["approver"] = {"actor_id": "user:resource-owner", "role": "RESOURCE_OWNER"}
        authorization["approved_at"] = None
        authorization["expires_at"] = None
        authorization["revoked_at"] = None
        payload["execution"] = {
            "state": "BLOCKED",
            "started_at": None,
            "completed_at": None,
            "tool_call_ids": [],
            "events": [],
            "aggregate_result_sha256": None,
        }
        self.resign(payload)
        self.assertEqual([], self.validate(payload))

    def test_rejects_self_approval(self) -> None:
        payload = self.fresh()
        payload["authorization"]["approver"]["actor_id"] = payload["requester"]["actor_id"]
        self.resign(payload)
        self.assert_has(self.validate(payload), "self-approval")

    def test_rejects_execution_after_expiry(self) -> None:
        payload = self.fresh()
        payload["authorization"]["expires_at"] = "2026-08-23T12:02:00Z"
        self.resign(payload)
        self.assert_has(self.validate(payload), "after authorization expiry")

    def test_rejects_out_of_scope_target(self) -> None:
        payload = self.fresh()
        payload["execution"]["events"][0]["target_id"] = "workspace://project/other.md"
        self.resign(payload)
        self.assert_has(self.validate(payload), "outside the authorized scope")

    def test_rejects_execution_before_approval(self) -> None:
        payload = self.fresh()
        payload["authorization"]["approved_at"] = "2026-08-23T12:03:00Z"
        self.resign(payload)
        self.assert_has(self.validate(payload), "before approval")

    def test_rejects_missing_result_hash(self) -> None:
        payload = self.fresh()
        payload["execution"]["events"][0]["result_sha256"] = ""
        self.resign(payload)
        self.assert_has(self.validate(payload), "result_sha256 must be 64")

    def test_rejects_missing_after_hash(self) -> None:
        payload = self.fresh()
        payload["execution"]["events"][0]["after_sha256"] = None
        self.resign(payload)
        self.assert_has(self.validate(payload), "after_sha256 must be 64")

    def test_rejects_execution_while_approval_is_only_requested(self) -> None:
        payload = self.fresh()
        payload["authorization"]["state"] = "REQUESTED"
        payload["authorization"]["approved_at"] = None
        payload["authorization"]["expires_at"] = None
        self.resign(payload)
        self.assert_has(self.validate(payload), "requires APPROVED authorization")

    def test_rejects_host_enforced_claim_when_runtime_support_is_false(self) -> None:
        payload = self.fresh()
        payload["host_enforcement"]["declared_level"] = "HOST_ENFORCED"
        self.resign(payload)
        errors = self.validate(payload)
        self.assert_has(errors, "cannot claim HOST_ENFORCED")
        self.assert_has(errors, "requires runtime_authorization_enforcement=true")

    def test_rejects_submission_upload_approved_by_wrong_role(self) -> None:
        payload = self.fresh()
        payload["action_class"] = "SUBMISSION_UPLOAD"
        payload["target_scope"]["targets"] = [
            {
                "target_id": "portal://journal/submission-001",
                "target_kind": "SUBMISSION_PORTAL",
                "allowed_operations": ["UPLOAD"],
            }
        ]
        payload["execution"]["events"][0]["target_id"] = "portal://journal/submission-001"
        payload["execution"]["events"][0]["operation"] = "UPLOAD"
        payload["authorization"]["approver"]["role"] = "USER"
        self.resign(payload)
        self.assert_has(self.validate(payload), "cannot approve SUBMISSION_UPLOAD")

    def test_rejects_clinical_action_without_institutional_evidence(self) -> None:
        payload = self.fresh()
        payload["action_class"] = "CLINICAL_REGULATORY"
        payload["target_scope"]["targets"] = [
            {
                "target_id": "clinical://site/patient-care-state-001",
                "target_kind": "PATIENT_CARE_STATE",
                "allowed_operations": ["CHANGE_CLINICAL_STATE"],
            }
        ]
        payload["execution"]["events"][0]["target_id"] = (
            "clinical://site/patient-care-state-001"
        )
        payload["execution"]["events"][0]["operation"] = "CHANGE_CLINICAL_STATE"
        payload["authorization"]["approver"]["role"] = (
            "CLINICAL_REGULATORY_AUTHORITY"
        )
        self.resign(payload)
        self.assert_has(self.validate(payload), "requires INSTITUTIONAL_RECORD")

    def test_rejects_read_only_event_that_changes_state(self) -> None:
        payload = self.fresh()
        payload["action_class"] = "READ_ONLY"
        payload["target_scope"]["targets"][0]["allowed_operations"] = ["READ"]
        payload["execution"]["events"][0]["operation"] = "READ"
        authorization = payload["authorization"]
        authorization["state"] = "NOT_REQUIRED"
        authorization["approver"] = {"actor_id": "policy:read-only", "role": "POLICY"}
        authorization["evidence"]["evidence_type"] = "NOT_APPLICABLE"
        authorization["approved_at"] = None
        authorization["expires_at"] = None
        self.resign(payload)
        self.assert_has(self.validate(payload), "before and after hashes must be identical")

    def test_rejects_wildcard_target(self) -> None:
        payload = self.fresh()
        payload["target_scope"]["targets"][0]["target_id"] = "workspace://project/*"
        payload["execution"]["events"][0]["target_id"] = "workspace://project/*"
        self.resign(payload)
        self.assert_has(self.validate(payload), "cannot contain wildcard")

    def test_rejects_missing_tool_call_id_binding(self) -> None:
        payload = self.fresh()
        payload["execution"]["tool_call_ids"] = []
        self.resign(payload)
        self.assert_has(self.validate(payload), "must exactly match event order")


if __name__ == "__main__":
    unittest.main(verbosity=2)
