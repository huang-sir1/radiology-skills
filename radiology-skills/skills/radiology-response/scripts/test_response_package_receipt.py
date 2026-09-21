#!/usr/bin/env python3
"""Regression tests for the canonical response-package receipt."""

from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("validate_response_package_receipt.py")
SPEC = importlib.util.spec_from_file_location("validate_response_package_receipt", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

PREREVIEW_MODULE_PATH = (
    MODULE_PATH.parents[2]
    / "radiology-prereview" / "scripts" / "validate_scientific_prereview_receipt.py"
)
PREREVIEW_SPEC = importlib.util.spec_from_file_location(
    "validate_scientific_prereview_receipt_for_response_test", PREREVIEW_MODULE_PATH,
)
assert PREREVIEW_SPEC and PREREVIEW_SPEC.loader
PREREVIEW = importlib.util.module_from_spec(PREREVIEW_SPEC)
PREREVIEW_SPEC.loader.exec_module(PREREVIEW)


def valid_prereview_receipts() -> tuple[dict[str, object], dict[str, object]]:
    source_artifact_digest = "6" * 64
    revised_artifact_digest = "9" * 64
    source: dict[str, object] = {
        "schema_version": "1.2",
        "receipt_id": "SPR-SOURCE-001",
        "project_id": "PROJECT-001",
        "manuscript_id": "MANUSCRIPT-001",
        "study_scope": "imaging-mechanism",
        "review_route": "combined",
        "project_state_digest": "7" * 64,
        "modality_role_digest": "8" * 64,
        "analysis_lock_digest": "1" * 64,
        "claim_registry_digest": "2" * 64,
        "scientific_handoff_digest": "3" * 64,
        "source_artifacts": [{
            "artifact_id": "manuscript-source",
            "role": "source-manuscript",
            "version": "v1",
            "sha256": source_artifact_digest,
        }],
        "findings": [{
            "finding_id": "F-001",
            "severity": "P1",
            "criterion": "The matched unit and effect estimate remain explicit.",
            "affected_claim_ids": ["CLAIM-001"],
            "source_artifact_id": "manuscript-source",
            "source_artifact_sha256": source_artifact_digest,
            "evidence_anchor": "Results paragraph 3",
            "minimum_repair": "Add matched donor n and effect uncertainty.",
            "repair_owner": "radiology-stats",
            "closure_evidence_required": "Version-bound revised Results text.",
            "next_gate": "radiology-prereview re-review",
            "source_review_state": "PARTIAL",
            "prior_verification_state": "not-applicable",
            "verification_state": "PARTIAL",
            "verification_evidence_locator": "manuscript-source:Results paragraph 3",
            "state_change_evidence": "Initial review found the unit but not the uncertainty.",
            "residual_boundary": "No causal claim.",
            "required_for_pass": True,
            "not_applicable_reason": "",
        }],
        "reviewer_roles": ["imaging-reproducibility", "mechanism", "editor-synthesis"],
        "reviewed_on": "2026-08-20",
        "unresolved_placeholder_count": 0,
        "scientific_prereview_state": "SCIENTIFIC_PREREVIEW_CONDITIONAL",
        "scientific_prereview_receipt_digest": "",
    }
    source["scientific_prereview_receipt_digest"] = PREREVIEW.canonical_digest(source)
    post = copy.deepcopy(source)
    post["receipt_id"] = "SPR-POST-001"
    post["source_artifacts"] = [{
        "artifact_id": "manuscript-revised",
        "role": "revised-manuscript",
        "version": "v2",
        "sha256": revised_artifact_digest,
    }]
    post_finding = post["findings"][0]
    post_finding["source_artifact_id"] = "manuscript-revised"
    post_finding["source_artifact_sha256"] = revised_artifact_digest
    post_finding["evidence_anchor"] = "Results paragraph 4"
    post_finding["prior_verification_state"] = "PARTIAL"
    post_finding["verification_state"] = "VERIFIED"
    post_finding["verification_evidence_locator"] = "manuscript-revised:Results paragraph 4"
    post_finding["state_change_evidence"] = "Matched donor n and estimate were added and rechecked."
    post["reviewed_on"] = "2026-08-22"
    post["scientific_prereview_state"] = "SCIENTIFIC_PREREVIEW_PASS"
    post["scientific_prereview_receipt_digest"] = PREREVIEW.canonical_digest(post)
    return source, post


def valid_evidence_synthesis_prereview_receipts() -> tuple[dict[str, object], dict[str, object]]:
    role_names = (
        "protocol", "search", "selection-flow", "extraction",
        "risk-of-bias-applicability", "synthesis", "certainty",
    )
    source_artifacts = [
        {
            "artifact_id": f"review-{role}",
            "role": role,
            "version": "v1",
            "sha256": format(index, "x") * 64,
        }
        for index, role in enumerate(role_names, start=4)
    ]
    synthesis_artifact = next(
        artifact for artifact in source_artifacts if artifact["role"] == "synthesis"
    )
    source: dict[str, object] = {
        "schema_version": "1.2",
        "receipt_id": "SPR-REVIEW-SOURCE-001",
        "project_id": "PROJECT-001",
        "manuscript_id": "MANUSCRIPT-001",
        "study_scope": "evidence-synthesis",
        "review_route": "evidence-synthesis-review",
        "project_state_digest": "7" * 64,
        "modality_role_digest": "8" * 64,
        "analysis_lock_digest": "1" * 64,
        "claim_registry_digest": "2" * 64,
        "scientific_handoff_digest": "not-applicable",
        "source_artifacts": source_artifacts,
        "findings": [{
            "finding_id": "F-ES-001",
            "severity": "P1",
            "criterion": "Study-family dependence and the synthesized claim ceiling remain explicit.",
            "affected_claim_ids": ["CLAIM-ES-001"],
            "source_artifact_id": synthesis_artifact["artifact_id"],
            "source_artifact_sha256": synthesis_artifact["sha256"],
            "evidence_anchor": "Synthesis group 1",
            "minimum_repair": "Reconcile overlapping reports and rerun the bounded synthesis.",
            "repair_owner": "radiology-systematic-review",
            "closure_evidence_required": "Version-bound revised synthesis and certainty statement.",
            "next_gate": "radiology-prereview re-review",
            "source_review_state": "PARTIAL",
            "prior_verification_state": "not-applicable",
            "verification_state": "PARTIAL",
            "verification_evidence_locator": "review-synthesis:Synthesis group 1",
            "state_change_evidence": "Initial review found unresolved report-level dependence.",
            "residual_boundary": "No claim beyond the represented study families.",
            "required_for_pass": True,
            "not_applicable_reason": "",
        }],
        "reviewer_roles": ["evidence-synthesis", "methods-statistics", "editor-synthesis"],
        "reviewed_on": "2026-08-20",
        "unresolved_placeholder_count": 0,
        "scientific_prereview_state": "SCIENTIFIC_PREREVIEW_CONDITIONAL",
        "scientific_prereview_receipt_digest": "",
    }
    source["scientific_prereview_receipt_digest"] = PREREVIEW.canonical_digest(source)
    post = copy.deepcopy(source)
    post["receipt_id"] = "SPR-REVIEW-POST-001"
    post["source_artifacts"].append({
        "artifact_id": "manuscript-revised",
        "role": "revised-manuscript",
        "version": "v2",
        "sha256": "9" * 64,
    })
    post_finding = post["findings"][0]
    post_finding["source_artifact_id"] = "manuscript-revised"
    post_finding["source_artifact_sha256"] = "9" * 64
    post_finding["evidence_anchor"] = "Results paragraph 4"
    post_finding["prior_verification_state"] = "PARTIAL"
    post_finding["verification_state"] = "VERIFIED"
    post_finding["verification_evidence_locator"] = "manuscript-revised:Results paragraph 4"
    post_finding["state_change_evidence"] = (
        "Study families were reconciled and the claim was narrowed to the verified synthesis."
    )
    post["reviewed_on"] = "2026-08-22"
    post["scientific_prereview_state"] = "SCIENTIFIC_PREREVIEW_PASS"
    post["scientific_prereview_receipt_digest"] = PREREVIEW.canonical_digest(post)
    return source, post


def valid_receipt() -> dict[str, object]:
    source, post = valid_prereview_receipts()
    source_artifact_digest = "6" * 64
    revised_artifact_digest = "9" * 64
    payload: dict[str, object] = {
        "schema_version": "1.1",
        "response_package_id": "RESP-001",
        "project_id": "PROJECT-001",
        "manuscript_id": "MANUSCRIPT-001",
        "revision_round": "RR1",
        "study_scope": "imaging-mechanism",
        "project_state_digest": "7" * 64,
        "modality_role_digest": "8" * 64,
        "analysis_lock_digest": "1" * 64,
        "claim_registry_digest": "2" * 64,
        "scientific_handoff_digest": "3" * 64,
        "source_scientific_prereview_state": "SCIENTIFIC_PREREVIEW_CONDITIONAL",
        "post_revision_scientific_prereview_state": "SCIENTIFIC_PREREVIEW_PASS",
        "source_scientific_prereview_receipt_digest": source["scientific_prereview_receipt_digest"],
        "post_revision_scientific_prereview_receipt_digest": post["scientific_prereview_receipt_digest"],
        "source_review_items": [
            {
                "finding_id": "F-001",
                "affected_claim_ids": ["CLAIM-001"],
                "criterion": "The matched unit and effect estimate remain explicit.",
                "source_review_state": "PARTIAL",
                "source_artifact_id": "manuscript-source",
                "source_artifact_sha256": source_artifact_digest,
                "evidence_locator": "Results paragraph 3",
                "response_item_id": "RR1-R1-1",
                "response_closure_state": "VERIFIED",
                "closure_evidence_locator": "manuscript-revised:Results paragraph 4",
                "state_change_evidence": "Matched donor n and estimate were added and rechecked.",
                "required_for_release": True,
                "not_applicable_reason": "",
            }
        ],
        "artifacts": [
            {
                "artifact_id": "manuscript-source",
                "role": "source-manuscript",
                "version": "v1",
                "sha256": source_artifact_digest,
            },
            {
                "artifact_id": "manuscript-revised",
                "role": "revised-manuscript",
                "version": "v2",
                "sha256": revised_artifact_digest,
            }
        ],
        "unresolved_placeholder_count": 0,
        "package_status": "READY_FOR_SUBMISSION_ASSEMBLY",
        "response_package_digest": "",
    }
    payload["response_package_digest"] = MODULE.canonical_digest(payload)
    return payload


def valid_evidence_synthesis_receipt() -> tuple[
    dict[str, object], tuple[dict[str, object], dict[str, object]]
]:
    source, post = valid_evidence_synthesis_prereview_receipts()
    synthesis_artifact = next(
        artifact for artifact in source["source_artifacts"] if artifact["role"] == "synthesis"
    )
    payload: dict[str, object] = {
        "schema_version": "1.1",
        "response_package_id": "RESP-ES-001",
        "project_id": "PROJECT-001",
        "manuscript_id": "MANUSCRIPT-001",
        "revision_round": "RR1",
        "study_scope": "evidence-synthesis",
        "project_state_digest": "7" * 64,
        "modality_role_digest": "8" * 64,
        "analysis_lock_digest": "1" * 64,
        "claim_registry_digest": "2" * 64,
        "scientific_handoff_digest": "not-applicable",
        "source_scientific_prereview_state": "SCIENTIFIC_PREREVIEW_CONDITIONAL",
        "post_revision_scientific_prereview_state": "SCIENTIFIC_PREREVIEW_PASS",
        "source_scientific_prereview_receipt_digest": source[
            "scientific_prereview_receipt_digest"
        ],
        "post_revision_scientific_prereview_receipt_digest": post[
            "scientific_prereview_receipt_digest"
        ],
        "source_review_items": [{
            "finding_id": "F-ES-001",
            "affected_claim_ids": ["CLAIM-ES-001"],
            "criterion": "Study-family dependence and the synthesized claim ceiling remain explicit.",
            "source_review_state": "PARTIAL",
            "source_artifact_id": synthesis_artifact["artifact_id"],
            "source_artifact_sha256": synthesis_artifact["sha256"],
            "evidence_locator": "Synthesis group 1",
            "response_item_id": "RR1-R1-1",
            "response_closure_state": "VERIFIED",
            "closure_evidence_locator": "manuscript-revised:Results paragraph 4",
            "state_change_evidence": (
                "Study families were reconciled and the claim was narrowed to the verified synthesis."
            ),
            "required_for_release": True,
            "not_applicable_reason": "",
        }],
        "artifacts": [
            *copy.deepcopy(source["source_artifacts"]),
            {
                "artifact_id": "manuscript-revised",
                "role": "revised-manuscript",
                "version": "v2",
                "sha256": "9" * 64,
            },
        ],
        "unresolved_placeholder_count": 0,
        "package_status": "READY_FOR_SUBMISSION_ASSEMBLY",
        "response_package_digest": "",
    }
    payload["response_package_digest"] = MODULE.canonical_digest(payload)
    return payload, (source, post)


class ResponsePackageReceiptTests(unittest.TestCase):
    def assert_fails_with(
        self,
        payload: dict[str, object],
        fragment: str,
        prereviews: tuple[dict[str, object], dict[str, object]] | None = None,
    ) -> None:
        payload["response_package_digest"] = MODULE.canonical_digest(payload)
        source, post = prereviews or valid_prereview_receipts()
        result = MODULE.validate(payload, source, post)
        self.assertEqual("FAIL", result["status"])
        self.assertTrue(
            any(fragment in error for error in result["errors"]),
            msg=f"expected {fragment!r} in {result['errors']!r}",
        )

    def test_valid_ready_receipt_passes(self) -> None:
        source, post = valid_prereview_receipts()
        self.assertEqual("PASS", MODULE.validate(valid_receipt(), source, post)["status"])

    def test_valid_evidence_synthesis_receipt_passes_without_radiogenomics_handoff(self) -> None:
        payload, prereviews = valid_evidence_synthesis_receipt()
        self.assertEqual("PASS", MODULE.validate(payload, *prereviews)["status"])

    def test_evidence_synthesis_rejects_radiogenomics_handoff(self) -> None:
        payload, prereviews = valid_evidence_synthesis_receipt()
        payload["scientific_handoff_digest"] = "3" * 64
        self.assert_fails_with(
            payload,
            "must not require a radiogenomics scientific_handoff_digest",
            prereviews,
        )

    def test_evidence_synthesis_response_requires_all_frozen_artifact_roles(self) -> None:
        payload, prereviews = valid_evidence_synthesis_receipt()
        payload["artifacts"] = [
            artifact for artifact in payload["artifacts"] if artifact["role"] != "certainty"
        ]
        self.assert_fails_with(
            payload,
            "response artifacts missing frozen roles: certainty",
            prereviews,
        )

    def test_actual_prereview_receipt_objects_are_required(self) -> None:
        result = MODULE.validate(valid_receipt())
        self.assertEqual("FAIL", result["status"])
        self.assertTrue(any("receipt object is required" in error for error in result["errors"]))

    def test_semantic_tamper_invalidates_digest(self) -> None:
        payload = valid_receipt()
        payload["revision_round"] = "RR2"
        source, post = valid_prereview_receipts()
        result = MODULE.validate(payload, source, post)
        self.assertEqual("FAIL", result["status"])
        self.assertTrue(any("does not match canonical" in error for error in result["errors"]))

    def test_cli_writes_and_validates_canonical_digest(self) -> None:
        payload = valid_receipt()
        payload["response_package_digest"] = ""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "response-receipt.json"
            source_path = Path(temp_dir) / "source-prereview.json"
            post_path = Path(temp_dir) / "post-prereview.json"
            path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
            source, post = valid_prereview_receipts()
            source_path.write_text(json.dumps(source, ensure_ascii=False, indent=2), encoding="utf-8")
            post_path.write_text(json.dumps(post, ensure_ascii=False, indent=2), encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable, str(MODULE_PATH), str(path),
                    "--source-prereview-receipt", str(source_path),
                    "--post-prereview-receipt", str(post_path),
                    "--write-digest",
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(0, result.returncode, msg=result.stdout + result.stderr)
            written = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(MODULE.canonical_digest(written), written["response_package_digest"])
            self.assertEqual("PASS", MODULE.validate(written, source, post)["status"])

    def test_project_and_modality_receipts_are_required(self) -> None:
        payload = valid_receipt()
        payload.pop("project_state_digest")
        payload.pop("modality_role_digest")
        self.assert_fails_with(payload, "missing top-level fields")

    def test_affected_claim_ids_are_required(self) -> None:
        payload = valid_receipt()
        payload["source_review_items"][0]["affected_claim_ids"] = []
        self.assert_fails_with(payload, "affected_claim_ids must be non-empty")

    def test_post_revision_prereview_must_pass_before_ready(self) -> None:
        payload = valid_receipt()
        payload["post_revision_scientific_prereview_state"] = "SCIENTIFIC_PREREVIEW_CONDITIONAL"
        self.assert_fails_with(payload, "requires post-revision scientific prereview PASS")

    def test_required_open_item_blocks_ready(self) -> None:
        payload = valid_receipt()
        payload["source_review_items"][0]["response_closure_state"] = "NOT_VERIFIED"
        self.assert_fails_with(payload, "required source_review_items[0] is not closed")

    def test_source_artifact_is_a_digest_bound_foreign_key(self) -> None:
        payload = valid_receipt()
        payload["source_review_items"][0]["source_artifact_sha256"] = "7" * 64
        self.assert_fails_with(payload, "does not match artifacts registry")

    def test_closure_locator_must_bind_registered_artifact(self) -> None:
        payload = valid_receipt()
        payload["source_review_items"][0]["closure_evidence_locator"] = (
            "unregistered:Results paragraph 4"
        )
        self.assert_fails_with(payload, "registered artifact_id")

    def test_unverifiable_cannot_be_relabelled_not_applicable(self) -> None:
        payload = valid_receipt()
        item = payload["source_review_items"][0]
        item["source_review_state"] = "NOT VERIFIABLE"
        item["response_closure_state"] = "NOT_APPLICABLE"
        item["not_applicable_reason"] = "Author says no change is needed."
        self.assert_fails_with(payload, "cannot be converted to NOT_APPLICABLE")

    def test_prereview_not_verified_cannot_be_relabelled_not_applicable(self) -> None:
        payload = valid_receipt()
        item = payload["source_review_items"][0]
        item["source_review_state"] = "NOT_VERIFIED"
        item["response_closure_state"] = "NOT_APPLICABLE"
        item["not_applicable_reason"] = "Response prose says the issue is resolved."
        self.assert_fails_with(payload, "cannot be converted to NOT_APPLICABLE")

    def test_source_review_state_cannot_be_not_applicable(self) -> None:
        payload = valid_receipt()
        payload["source_review_items"][0]["source_review_state"] = "NOT_APPLICABLE"
        self.assert_fails_with(payload, "source_review_state is invalid")

    def test_fake_finding_id_is_rejected_against_bound_receipts(self) -> None:
        payload = valid_receipt()
        payload["source_review_items"][0]["finding_id"] = "F-FAKE"
        self.assert_fails_with(payload, "absent from both bound prereview receipts")

    def test_fake_claim_id_is_rejected_against_bound_finding(self) -> None:
        payload = valid_receipt()
        payload["source_review_items"][0]["affected_claim_ids"] = ["CLAIM-FAKE"]
        self.assert_fails_with(payload, "affected_claim_ids differs from frozen finding")

    def test_state_and_digest_must_match_actual_bound_receipt(self) -> None:
        payload = valid_receipt()
        source, post = valid_prereview_receipts()
        payload["post_revision_scientific_prereview_receipt_digest"] = source[
            "scientific_prereview_receipt_digest"
        ]
        self.assert_fails_with(
            payload,
            "post-revision scientific-prereview receipt digest differs from response",
            (source, post),
        )

    def test_bound_required_finding_cannot_be_omitted(self) -> None:
        payload = valid_receipt()
        source, post = valid_prereview_receipts()
        for receipt, verification_state, locator, state_change in (
            (
                source, "PARTIAL", "manuscript-source:Discussion paragraph 2",
                "Initial review found an unbounded mechanism statement.",
            ),
            (
                post, "VERIFIED", "manuscript-revised:Discussion paragraph 2",
                "The statement was narrowed to association and rechecked.",
            ),
        ):
            artifact = receipt["source_artifacts"][0]
            receipt["findings"].append({
                "finding_id": "F-002",
                "severity": "P1",
                "criterion": "Mechanism wording stays within the measured evidence.",
                "affected_claim_ids": ["CLAIM-002"],
                "source_artifact_id": artifact["artifact_id"],
                "source_artifact_sha256": artifact["sha256"],
                "evidence_anchor": "Discussion paragraph 2",
                "minimum_repair": "Narrow the mechanism statement.",
                "repair_owner": "radiology-writing",
                "closure_evidence_required": "Version-bound revised Discussion text.",
                "next_gate": "radiology-prereview re-review",
                "source_review_state": "PARTIAL",
                "prior_verification_state": "PARTIAL",
                "verification_state": verification_state,
                "verification_evidence_locator": locator,
                "state_change_evidence": state_change,
                "residual_boundary": "No causal claim.",
                "required_for_pass": True,
                "not_applicable_reason": "",
            })
            receipt["scientific_prereview_receipt_digest"] = PREREVIEW.canonical_digest(receipt)
        payload["source_scientific_prereview_receipt_digest"] = source[
            "scientific_prereview_receipt_digest"
        ]
        payload["post_revision_scientific_prereview_receipt_digest"] = post[
            "scientific_prereview_receipt_digest"
        ]
        self.assert_fails_with(
            payload,
            "bound scientific-prereview findings are missing from response",
            (source, post),
        )

    def test_required_prereview_finding_cannot_be_downgraded(self) -> None:
        payload = valid_receipt()
        payload["source_review_items"][0]["required_for_release"] = False
        self.assert_fails_with(payload, "cannot downgrade a required prereview finding")


if __name__ == "__main__":
    unittest.main()
