#!/usr/bin/env python3
"""Cross-step golden scenarios for intake, routing, manifest audit and report rendering.

Fixtures intentionally pre-populate human QA states so these tests exercise the
machine contracts only. They are not evidence that a real artifact was rendered
or scientifically reviewed.
"""

from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

import test_audit_submission_package as fixture
import validate_conference_portal_package as conference


SCRIPT_DIR = Path(__file__).resolve().parent
RESOLVER = SCRIPT_DIR / "resolve_submission_intake.py"
RENDERER = SCRIPT_DIR / "render_submission_audit_report.py"


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def intake_payload(
    package: Path, journal_id: str, article_type: str, stage: str,
    review_model: str, *, scope: str = "upload-root",
) -> dict[str, object]:
    return {
        "schema_version": "1.1",
        "target_journal_id": journal_id,
        "article_type": article_type,
        "submission_stage": stage,
        "publisher_stage_label": stage,
        "package_root": str(package),
        "review_scope": scope,
        "study_design": ["observational"],
        "review_model": review_model,
        "manuscript_version": "golden-v1",
        "project_id": "GOLDEN-PROJECT-001",
        "study_scope": "imaging-only",
        "project_state_digest": "d" * 64,
        "modality_role_digest": "e" * 64,
        "scientific_handoff_packet_digest": "f" * 64,
        "scientific_prereview_receipt_digest": "not-applicable",
        "source_artifact_id": "ARTIFACT-GOLDEN-MANUSCRIPT",
        "analysis_lock_digest": "a" * 64,
        "claim_registry_digest": "b" * 64,
        "response_package_digest": "c" * 64 if stage == "revision" else "not-applicable",
        "guide_checked_on": "2026-08-22",
        "transfer_context": None,
    }


def bind_upstream(rows: list[dict[str, str]], intake: dict[str, object]) -> None:
    for row in rows:
        row["project_id"] = str(intake["project_id"])
        row["study_scope"] = str(intake["study_scope"])
        row["project_state_digest"] = str(intake["project_state_digest"])
        row["modality_role_digest"] = str(intake["modality_role_digest"])
        row["scientific_handoff_packet_digest"] = str(
            intake["scientific_handoff_packet_digest"]
        )
        row["scientific_prereview_receipt_digest"] = str(
            intake["scientific_prereview_receipt_digest"]
        )
        row["analysis_lock_digest"] = str(intake["analysis_lock_digest"])
        row["claim_registry_digest"] = str(intake["claim_registry_digest"])
        row["response_package_digest"] = str(intake["response_package_digest"])
        row["source_artifact_id"] = (
            str(intake["source_artifact_id"]) if row.get("path") else "not-applicable"
        )


def run_resolver(
    intake_path: Path, output_dir: Path,
) -> tuple[int, dict[str, object]]:
    intake = json.loads(intake_path.read_text(encoding="utf-8"))
    completed = subprocess.run(
        [
            sys.executable, str(RESOLVER), str(intake_path),
            "--package-root", str(intake["package_root"]),
            "--output-dir", str(output_dir),
        ],
        check=False, capture_output=True, text=True, encoding="utf-8",
    )
    return completed.returncode, json.loads(completed.stdout)


def resolver_contract(
    case: unittest.TestCase, intake_path: Path, output_dir: Path, expected_route_id: str,
) -> dict[str, object]:
    code, report = run_resolver(intake_path, output_dir)
    case.assertEqual(0, code, report)
    case.assertEqual("PASS", report["status"])
    case.assertFalse(report["readiness_granted"])
    case.assertEqual(expected_route_id, report["route"]["route_id"])
    case.assertEqual("NOT_PERFORMED", report["package_inventory"]["semantic_mapping"])
    outputs = report["outputs"]
    draft_path = Path(outputs["draft_manifest"])
    case.assertTrue(draft_path.is_file())
    with draft_path.open(encoding="utf-8", newline="") as handle:
        draft_rows = list(csv.DictReader(handle))
    case.assertTrue(draft_rows)
    case.assertTrue(all(row["status"] in {"pending-author", "pending-guide"} for row in draft_rows))
    case.assertTrue(all(row["technical_qa"] == "not-checked" for row in draft_rows))
    case.assertTrue(all(not row["not_applicable_reason"] for row in draft_rows))
    return report


def render_report(temp_root: Path, report: dict[str, object]) -> str:
    source = temp_root / "audit-report.json"
    output = temp_root / "submission-human-review.md"
    write_json(source, report)
    completed = subprocess.run(
        [
            sys.executable, str(RENDERER), str(source),
            "--package-root", str(report["package_dir"]),
            "--expected-audit-sha256", fixture.digest(source),
            "--output", str(output), "--force",
        ],
        check=False, capture_output=True, text=True, encoding="utf-8",
    )
    if completed.returncode != 0:
        raise AssertionError(completed.stderr or completed.stdout)
    return output.read_text(encoding="utf-8")


def make_minimal_tiff(path: Path, marker: bytes) -> None:
    path.write_bytes(b"II*\x00\x08\x00\x00\x00" + marker)


def conference_intake(package: Path, abstract_digest: str) -> dict[str, object]:
    return {
        "schema_version": "1.0",
        "route_kind": "conference-portal-finalization",
        "venue_name": "Radiology Research Congress",
        "venue_series_id": "RAD-RESEARCH-CONGRESS",
        "submission_cycle": "2027",
        "submission_type": "Scientific abstract",
        "current_call_url": "https://congress.test/2027/abstract-call",
        "portal_url": "https://submit.congress.test/2027/abstracts",
        "call_status": "OPEN",
        "call_checked_on": "2026-08-23",
        "portal_checked_on": "2026-08-23",
        "submission_deadline": "2027-01-31T17:00:00-05:00",
        "call_capture_sha256": "a" * 64,
        "call_capture_locator": "private current-call capture 2026-08-23",
        "portal_capture_sha256": "b" * 64,
        "portal_capture_locator": "private logged-in portal capture 2026-08-23",
        "call_bound_venue_series_id": "RAD-RESEARCH-CONGRESS",
        "call_bound_submission_cycle": "2027",
        "call_bound_submission_type": "Scientific abstract",
        "portal_bound_venue_series_id": "RAD-RESEARCH-CONGRESS",
        "portal_bound_submission_cycle": "2027",
        "portal_bound_submission_type": "Scientific abstract",
        "project_id": "CONFERENCE-GOLDEN-001",
        "abstract_artifact_id": "ARTIFACT-CONFERENCE-ABSTRACT-V1",
        "abstract_sha256": abstract_digest,
        "dissemination_handoff_sha256": "c" * 64,
        "claim_registry_digest": "d" * 64,
        "analysis_lock_digest": "e" * 64,
        "content_owner": "radiology-dissemination",
        "portal_owner": "radiology-submission",
        "embargo_gate": "PASS",
        "disclosure_gate": "PASS",
        "privacy_gate": "PASS",
        "rights_gate": "PASS",
        "author_approval_gate": "PASS",
        "package_root": str(package),
        "review_scope": "upload-root",
        "human_final_action_owner": "authorized corresponding author",
        "human_final_action_status": "PENDING",
    }


def conference_rows(abstract_digest: str) -> list[dict[str, str]]:
    base = {
        "schema_version": "1.0", "venue_series_id": "RAD-RESEARCH-CONGRESS",
        "submission_cycle": "2027", "submission_type": "Scientific abstract",
        "condition": "", "version": "abstract-v1", "source_artifact_id": "ARTIFACT-CONFERENCE-ABSTRACT-V1",
        "source_artifact_sha256": abstract_digest, "value_status": "READY_FOR_HUMAN_ENTRY",
        "content_gate": "PASS", "claim_boundary": "preserve frozen association-only claims and uncertainty",
        "embargo_gate": "PASS", "disclosure_gate": "PASS", "privacy_gate": "PASS",
        "rights_gate": "PASS", "human_owner": "authorized corresponding author", "notes": "",
    }
    upload = dict(base)
    upload.update({
        "item_id": "CONF-FILE-001", "item_kind": "upload-file",
        "material": "conference abstract upload file", "portal_designation": "Abstract file",
        "requirement_class": "required", "authority_class": "CURRENT_CALL",
        "source_url": "https://congress.test/2027/abstract-call", "verified_on": "2026-08-23",
        "allowed_extensions": ".txt", "max_bytes": "100000",
        "path": "abstract.txt", "upload_sha256": abstract_digest,
        "technical_qa": "PASS", "render_qa": "PASS",
    })
    field = dict(base)
    field.update({
        "item_id": "CONF-FIELD-001", "item_kind": "portal-field",
        "material": "conference abstract title portal field", "portal_designation": "Abstract title",
        "requirement_class": "required", "authority_class": "PORTAL_CURRENT",
        "source_url": "https://submit.congress.test/2027/abstracts", "verified_on": "2026-08-23",
        "allowed_extensions": "", "max_bytes": "",
        "path": "", "upload_sha256": "", "technical_qa": "NOT_APPLICABLE",
        "render_qa": "NOT_APPLICABLE",
    })
    attestation = dict(base)
    attestation.update({
        "item_id": "CONF-ATTEST-001", "item_kind": "portal-attestation",
        "material": "conference disclosure attestation", "portal_designation": "Disclosure certification",
        "requirement_class": "required", "authority_class": "PORTAL_CURRENT",
        "source_url": "https://submit.congress.test/2027/abstracts", "verified_on": "2026-08-23",
        "allowed_extensions": "", "max_bytes": "",
        "path": "", "upload_sha256": "", "technical_qa": "NOT_APPLICABLE",
        "render_qa": "NOT_APPLICABLE",
    })
    return [
        {name: row.get(name, "") for name in conference.MANIFEST_FIELDS}
        for row in (upload, field, attestation)
    ]


def jno_revision_rows(root: Path) -> list[dict[str, str]]:
    guide = "https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors"
    portal = "https://manuscripts.jamanetworkopen.com/"
    route_receipt = fixture.base_row("", "")
    route_receipt.update({
        "item_id": "REVISION-ROUTE", "journal_id": "jama-network-open",
        "article_type": "Original Investigation", "submission_stage": "revision",
        "review_model": "single-anonymized", "material": "revision package routing",
        "requirement_class": "portal-only", "condition": "revision invited",
        "rule_id": "JNO-REVISION-PAIR", "authority_class": "PORTAL_CURRENT",
        "source_url": portal, "path": "", "expected_extensions": "", "version": "",
        "sha256": "", "blinded": "not-applicable", "tracked_changes_policy": "not-applicable",
        "revision_variant": "not-applicable", "status": "ready",
        "technical_qa": "not-applicable", "render_qa": "not-applicable",
        "content_gate": "not-applicable", "anonymization_qa": "not-applicable",
        "crossfile_qa": "not-applicable", "source_artifact_id": "not-applicable",
        "notes": fixture.portal_receipt(
            "jama-network-open", "Original Investigation", "revision",
            "Revision Files", "private JNO revision route capture",
        ),
    })
    rows = [route_receipt]
    for rule_id, material in (
        ("JNO-REV-FIG-GRAPH", "separate revision graph or plot"),
        ("JNO-REV-FIG-FLOW", "separate revision flow diagram"),
        ("JNO-REV-FIG-ILLUS", "separate revision illustration"),
        ("JNO-REV-FIG-LINE", "separate revision line drawing"),
    ):
        row = fixture.conditional_na(rule_id, material, guide, blinded="false")
        row.update({
            "journal_id": "jama-network-open", "article_type": "Original Investigation",
            "submission_stage": "revision", "review_model": "single-anonymized",
        })
        rows.append(row)
    marked = root / "figure1-marked.tif"
    unmarked = root / "figure1-unmarked.tif"
    make_minimal_tiff(marked, b"marked")
    make_minimal_tiff(unmarked, b"unmarked")
    photo_rows: list[dict[str, str]] = []
    for item_id, path in (("PHOTO-MARKED", marked), ("PHOTO-UNMARKED", unmarked)):
        row = fixture.base_row(path.name, fixture.digest(path))
        row.update({
            "item_id": item_id, "journal_id": "jama-network-open",
            "article_type": "Original Investigation", "submission_stage": "revision",
            "review_model": "single-anonymized", "material": "separate revision photographic or clinical image",
            "requirement_class": "conditional",
            "condition": "photograph clinical image radiograph microscopy CT MRI or ultrasound figure exists",
            "rule_id": "JNO-REV-FIG-PHOTO", "source_url": guide,
            "expected_extensions": ".tif", "blinded": "false",
            "revision_variant": "other-revision",
        })
        photo_rows.append(row)
    assertion = fixture.base_row("", "")
    assertion.update({
        "item_id": "PHOTO-PAIR", "journal_id": "jama-network-open",
        "article_type": "Original Investigation", "submission_stage": "revision",
        "review_model": "single-anonymized", "material": "revision marked and unmarked figure-pair assertion",
        "requirement_class": "conditional",
        "condition": "photograph clinical image photomicrograph gel or similar image contains labels arrows or other markers",
        "rule_id": "JNO-REV-FIG-MARKER-PAIR", "source_url": guide,
        "path": "", "expected_extensions": "", "version": "", "sha256": "",
        "blinded": "not-applicable", "tracked_changes_policy": "not-applicable",
        "revision_variant": "not-applicable", "status": "ready",
        "technical_qa": "not-applicable", "render_qa": "not-applicable",
        "content_gate": "pass", "anonymization_qa": "not-applicable",
        "crossfile_qa": "pass", "source_artifact_id": "not-applicable",
        "notes": "; ".join([
            "figure_pair_id=Figure 1", "marked_item_id=PHOTO-MARKED",
            "unmarked_item_id=PHOTO-UNMARKED",
            f"marked_sha256={photo_rows[0]['sha256']}",
            f"unmarked_sha256={photo_rows[1]['sha256']}",
            "pair_review_locator=private rendered JNO revision pair Figure 1",
        ]),
    })
    return [*rows, *photo_rows, assertion]


def npjdm_revision_rows(root: Path, *, resolve_figures: bool) -> list[dict[str, str]]:
    public_guide = "https://www.nature.com/npjdigitalmed/for-authors-and-referees/editorial-process"
    portal = "https://submission.springernature.com/new-submission/41746/"
    rows: list[dict[str, str]] = []
    for item_id, filename, variant, text, capture_digest in (
        ("CLEAN", "revised-clean.docx", "clean", "clean revised manuscript", "a" * 64),
        ("RESPONSE", "response.docx", "response", "point by point response", "b" * 64),
        ("COVER", "change-cover.docx", "cover", "change cover letter", "c" * 64),
    ):
        path = root / filename
        fixture.make_docx(path, text=text)
        row = fixture.base_row(filename, fixture.digest(path))
        row.update({
            "item_id": item_id, "journal_id": "npj-digital-medicine",
            "article_type": "Article", "submission_stage": "revision",
            "review_model": "single-anonymized", "material": "revision package",
            "condition": "revision invited", "rule_id": "NPJDM-REV-PACKAGE",
            "authority_class": "PORTAL_CURRENT", "source_url": portal,
            "expected_extensions": ".docx", "blinded": "false",
            "revision_variant": variant,
            "notes": fixture.portal_receipt(
                "npj-digital-medicine", "Article", "revision",
                f"Revision {variant} upload", f"private npjdm {variant} upload capture",
                capture_sha256=capture_digest,
            ),
        })
        rows.append(row)
    convention = fixture.base_row("", "")
    convention.update({
        "item_id": "CLEAN-MARKED-ROUTE", "journal_id": "npj-digital-medicine",
        "article_type": "Article", "submission_stage": "revision",
        "review_model": "single-anonymized", "material": "clean and marked manuscript convention",
        "requirement_class": "portal-only", "condition": "revision invited",
        "rule_id": "NPJDM-REV-CLEAN-MARKED", "authority_class": "PORTAL_CURRENT",
        "source_url": portal, "path": "", "expected_extensions": "", "version": "",
        "sha256": "", "blinded": "not-applicable", "tracked_changes_policy": "not-applicable",
        "revision_variant": "not-applicable", "status": "ready",
        "technical_qa": "not-applicable", "render_qa": "not-applicable",
        "content_gate": "not-applicable", "anonymization_qa": "not-applicable",
        "crossfile_qa": "not-applicable", "source_artifact_id": "not-applicable",
        "notes": fixture.portal_receipt(
            "npj-digital-medicine", "Article", "revision", "Revision manuscript convention",
            "private npjdm clean-marked route capture", capture_sha256="d" * 64,
        ),
    })
    figures = fixture.base_row("", "")
    figures.update({
        "item_id": "FIGURE-ROUTE", "journal_id": "npj-digital-medicine",
        "article_type": "Article", "submission_stage": "revision",
        "review_model": "single-anonymized", "material": "revision figure files or portal-designated figure items",
        "requirement_class": "portal-only",
        "condition": "main-article figures are supplied during revision",
        "rule_id": "NPJDM-REV-FIGURES", "path": "", "expected_extensions": "",
        "version": "", "sha256": "", "blinded": "not-applicable",
        "tracked_changes_policy": "not-applicable", "revision_variant": "not-applicable",
        "status": "ready" if resolve_figures else "pending-guide",
        "technical_qa": "not-applicable", "render_qa": "not-applicable",
        "content_gate": "not-applicable", "anonymization_qa": "not-applicable",
        "crossfile_qa": "not-applicable", "source_artifact_id": "not-applicable",
    })
    if resolve_figures:
        figures.update({
            "authority_class": "PORTAL_CURRENT", "source_url": portal,
            "notes": fixture.portal_receipt(
                "npj-digital-medicine", "Article", "revision", "Revision figure designation",
                "private npjdm figure route capture", capture_sha256="e" * 64,
            ),
        })
    else:
        figures.update({
            "authority_class": "JOURNAL_GUIDE", "source_url": public_guide,
            "notes": "awaiting authenticated exact-journal revision portal capture",
        })
    return [*rows, convention, figures]


class SubmissionGoldenScenarios(unittest.TestCase):
    def test_conference_portal_finalization_stops_at_named_human_action(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package = root / "conference-upload"
            package.mkdir()
            abstract = package / "abstract.txt"
            abstract.write_text("Frozen association-only conference abstract.", encoding="utf-8")
            abstract_digest = fixture.digest(abstract)
            intake = conference_intake(package, abstract_digest)
            rows = conference_rows(abstract_digest)
            report = conference.audit_conference_portal(
                intake, rows, package,
                now=datetime(2026, 8, 23, 12, tzinfo=timezone.utc),
            )
            self.assertEqual("PASS", report["status"], report)
            self.assertEqual("HUMAN_PORTAL_ACTION_REQUIRED", report["route_state"])
            self.assertEqual("radiology-dissemination", report["content_owner"])
            self.assertEqual("radiology-submission", report["portal_owner"])
            self.assertFalse(report["readiness_granted"])
            self.assertFalse(report["portal_action_performed"])
            self.assertTrue(report["human_final_action_required"])

            # The real CLI uses the wall clock. Only its synthetic fixture is
            # relative to today; fixed-clock boundary scenarios below stay fixed.
            cli_now = datetime.now(timezone.utc)
            cli_checked_on = cli_now.date().isoformat()
            cli_cycle = str(cli_now.year + 1)
            intake.update({
                "submission_cycle": cli_cycle,
                "current_call_url": f"https://congress.test/{cli_cycle}/abstract-call",
                "portal_url": f"https://submit.congress.test/{cli_cycle}/abstracts",
                "call_checked_on": cli_checked_on,
                "portal_checked_on": cli_checked_on,
                "submission_deadline": f"{cli_cycle}-01-31T17:00:00-05:00",
                "call_capture_locator": f"synthetic CLI current-call capture {cli_checked_on}",
                "portal_capture_locator": f"synthetic CLI portal capture {cli_checked_on}",
                "call_bound_submission_cycle": cli_cycle,
                "portal_bound_submission_cycle": cli_cycle,
            })
            for row in rows:
                row["submission_cycle"] = cli_cycle
                row["verified_on"] = cli_checked_on
                row["source_url"] = str(intake[
                    "current_call_url" if row["authority_class"] == "CURRENT_CALL" else "portal_url"
                ])

            intake_path = root / "conference-intake.json"
            manifest_path = root / "conference-manifest.csv"
            write_json(intake_path, intake)
            with manifest_path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=conference.MANIFEST_FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            completed = subprocess.run(
                [
                    sys.executable, str(SCRIPT_DIR / "validate_conference_portal_package.py"),
                    str(intake_path), str(manifest_path), "--package-root", str(package),
                ],
                check=False, capture_output=True, text=True, encoding="utf-8",
            )
            self.assertEqual(0, completed.returncode, completed.stderr or completed.stdout)
            cli_report = json.loads(completed.stdout)
            self.assertEqual("HUMAN_PORTAL_ACTION_REQUIRED", cli_report["route_state"])
            self.assertFalse(cli_report["portal_action_performed"])

    def test_conference_portal_wrong_cycle_stale_call_and_machine_submit_claim_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package = root / "conference-upload"
            package.mkdir()
            abstract = package / "abstract.txt"
            abstract.write_text("Frozen conference abstract.", encoding="utf-8")
            abstract_digest = fixture.digest(abstract)
            intake = conference_intake(package, abstract_digest)
            rows = conference_rows(abstract_digest)

            wrong_cycle = [dict(row) for row in rows]
            wrong_cycle[0]["submission_cycle"] = "2026"
            wrong_report = conference.audit_conference_portal(
                intake, wrong_cycle, package,
                now=datetime(2026, 8, 23, 12, tzinfo=timezone.utc),
            )
            self.assertEqual("FAIL", wrong_report["status"])
            self.assertEqual("PORTAL_PACKAGE_BLOCKED", wrong_report["route_state"])

            wrong_format = [dict(row) for row in rows]
            wrong_format[0]["allowed_extensions"] = ".pdf"
            format_report = conference.audit_conference_portal(
                intake, wrong_format, package,
                now=datetime(2026, 8, 23, 12, tzinfo=timezone.utc),
            )
            self.assertEqual("FAIL", format_report["status"])
            self.assertTrue(any("source-backed allowlist" in value for value in format_report["errors"]))

            stale_report = conference.audit_conference_portal(
                intake, rows, package,
                now=datetime(2026, 9, 1, 12, tzinfo=timezone.utc),
            )
            self.assertEqual("FAIL", stale_report["status"])
            self.assertEqual("CALL_EVIDENCE_UNVERIFIED", stale_report["route_state"])
            self.assertTrue(any("older than 7 days" in value for value in stale_report["errors"]))

            future_report = conference.audit_conference_portal(
                intake, rows, package,
                now=datetime(2026, 8, 22, 12, tzinfo=timezone.utc),
            )
            self.assertEqual("FAIL", future_report["status"])
            self.assertEqual("CALL_EVIDENCE_UNVERIFIED", future_report["route_state"])
            self.assertTrue(any("cannot be in the future" in value for value in future_report["errors"]))

            claimed_submit = dict(intake)
            claimed_submit["human_final_action_status"] = "SUBMITTED"
            submit_report = conference.audit_conference_portal(
                claimed_submit, rows, package,
                now=datetime(2026, 8, 23, 12, tzinfo=timezone.utc),
            )
            self.assertEqual("FAIL", submit_report["status"])
            self.assertFalse(submit_report["portal_action_performed"])
            self.assertTrue(any("machine cannot submit" in value for value in submit_report["errors"]))

    def test_markdown_renderer_escapes_untrusted_manifest_derived_text(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package = root / "package"
            package.mkdir()
            rows = fixture.complete_radiology_rows(package)
            main = next(row for row in rows if row["item_id"] == "MAIN")
            main["item_id"] = (
                "<script>alert(1)</script> **fake PASS** "
                "![pixel](https://tracker.invalid/p) [click](javascript:alert(1))"
            )
            main["render_qa"] = "fail"
            fixture.write_manifest(package, rows)
            code, report = fixture.run_audit(package)
            self.assertNotEqual(0, code, report)
            markdown = render_report(root, report)
            self.assertNotIn("<script>", markdown)
            self.assertNotIn("![pixel]", markdown)
            self.assertNotIn("[click](javascript:", markdown)
            self.assertNotIn("**fake PASS**", markdown)
            self.assertIn("&lt;script&gt;", markdown)
            self.assertIn("&#42;&#42;fake PASS&#42;&#42;", markdown)

    def test_renderer_rejects_forged_state_and_post_audit_package_drift(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package = root / "package"
            package.mkdir()
            rows = fixture.complete_radiology_rows(package)
            fixture.write_manifest(package, rows)
            code, report = fixture.run_audit(package)
            self.assertEqual(0, code, report)

            forged = dict(report)
            forged["counts"] = dict(report["counts"])
            forged["counts"]["errors"] = 99
            with self.assertRaises(AssertionError):
                render_report(root, forged)

            main = next(row for row in rows if row["item_id"] == "MAIN")
            (package / main["path"]).write_bytes(b"post-audit drift")
            with self.assertRaises(AssertionError):
                render_report(root, report)

    def test_renderer_rejects_self_consistent_forged_pass_via_authoritative_rerun(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package = root / "package"
            package.mkdir()
            rows = fixture.complete_radiology_rows(package)
            main = next(row for row in rows if row["item_id"] == "MAIN")
            main["sha256"] = "9" * 64
            fixture.write_manifest(package, rows)
            code, report = fixture.run_audit(package)
            self.assertNotEqual(0, code, report)
            self.assertIn("HASH_MISMATCH", fixture.codes(report))

            forged = dict(report)
            forged["findings"] = []
            forged["counts"] = dict(report["counts"])
            forged["counts"]["errors"] = 0
            forged["counts"]["warnings"] = 0
            forged["execution_status"] = "PASS"
            forged["status"] = "PASS"
            forged["whole_package_readiness"] = "HUMAN_GATES_REQUIRED"
            forged["route"] = dict(report["route"])
            forged["route"]["minimum_material_contract"] = "PASS"
            forged["inventory"] = dict(report["inventory"])
            forged["inventory"]["blocking_findings"] = 0
            forged["inventory"]["coverage"] = "INVENTORY_CLOSED"
            with self.assertRaises(AssertionError) as captured:
                render_report(root, forged)
            self.assertIn("authoritative current rerun", str(captured.exception))

    def test_renderer_and_resolver_reject_duplicate_json_keys(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package = root / "package"
            package.mkdir()
            rows = fixture.complete_radiology_rows(package)
            fixture.write_manifest(package, rows)
            code, report = fixture.run_audit(package)
            self.assertEqual(0, code, report)
            source = root / "duplicate-audit.json"
            valid_body = json.dumps(report, ensure_ascii=False)[1:-1]
            source.write_text(
                '{"schema_version":"0.0","schema_version":"2.5",' + valid_body + "}",
                encoding="utf-8",
            )
            completed = subprocess.run(
                [
                    sys.executable, str(RENDERER), str(source),
                    "--package-root", str(package),
                    "--expected-audit-sha256", fixture.digest(source),
                ],
                check=False, capture_output=True, text=True, encoding="utf-8",
            )
            self.assertNotEqual(0, completed.returncode)
            self.assertIn("duplicate JSON object key", completed.stderr)

            intake = intake_payload(
                package, "radiology", "Original Research", "initial", "double-anonymized",
            )
            intake_text = json.dumps(intake, ensure_ascii=False)[1:-1]
            intake_path = root / "duplicate-intake.json"
            intake_path.write_text(
                '{"schema_version":"0.0","schema_version":"1.1",' + intake_text + "}",
                encoding="utf-8",
            )
            resolver = subprocess.run(
                [
                    sys.executable, str(RESOLVER), str(intake_path),
                    "--package-root", str(package),
                ],
                check=False, capture_output=True, text=True, encoding="utf-8",
            )
            self.assertNotEqual(0, resolver.returncode)
            self.assertIn("duplicate JSON object key", resolver.stdout)

    def test_transfer_is_dynamic_reprofiling_not_a_static_ready_route(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package = root / "package"
            package.mkdir()
            fixture.make_docx(package / "source-manuscript.docx")
            intake = intake_payload(
                package, "nature-communications", "Article", "transfer", "single-anonymized",
            )
            intake["transfer_context"] = {
                "source_journal_id": "radiology",
                "target_journal_id": "nature-communications",
                "target_article_type": "Article",
                "transfer_offer_receipt_sha256": "1" * 64,
                "transfer_offer_checked_on": "2026-08-22",
                "transfer_mode": "modify",
                "source_inventory_sha256": "2" * 64,
                "target_portal_inventory_sha256": "3" * 64,
                "target_initial_route_id": "nature-communications::Article::initial",
            }
            intake_path = root / "intake.json"
            write_json(intake_path, intake)
            plan = resolver_contract(
                self, intake_path, root / "resolved",
                "nature-communications::Article::initial",
            )
            self.assertEqual("TRANSFER_REPROFILE_REQUIRED", plan["intake_state"])
            self.assertEqual("transfer", plan["intake"]["requested_stage"])
            self.assertEqual("initial", plan["intake"]["effective_contract_stage"])
            self.assertFalse(plan["readiness_granted"])

            intake["transfer_context"]["target_portal_inventory_sha256"] = ""
            bad_path = root / "bad-intake.json"
            write_json(bad_path, intake)
            bad_code, bad_report = run_resolver(bad_path, root / "bad-resolved")
            self.assertNotEqual(0, bad_code)
            self.assertEqual("TARGET_OR_ROUTE_UNRESOLVED", bad_report["intake_state"])
            self.assertTrue(any(item["code"] == "TRANSFER_DIGEST" for item in bad_report["errors"]))

    def test_intake_schema_1_1_scientific_receipts_are_exact_and_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package = root / "package"
            package.mkdir()
            fixture.make_docx(package / "manuscript.docx")
            valid = intake_payload(
                package, "radiology", "Original Research", "initial", "double-anonymized",
            )
            variants: list[tuple[str, dict[str, object], str]] = []
            zero_digest = dict(valid)
            zero_digest["project_state_digest"] = "0" * 64
            variants.append(("zero-project-state", zero_digest, "SCIENTIFIC_HANDOFF_DIGEST"))
            unknown_scope = dict(valid)
            unknown_scope["study_scope"] = "radiogenomics"
            variants.append(("unknown-scope", unknown_scope, "STUDY_SCOPE"))
            ordered_items = list(valid.items())
            reordered = dict([ordered_items[1], ordered_items[0], *ordered_items[2:]])
            variants.append(("field-order", reordered, "INTAKE_FIELD_ORDER"))
            for name, payload, expected_code in variants:
                intake_path = root / f"{name}.json"
                write_json(intake_path, payload)
                code, report = run_resolver(intake_path, root / f"resolved-{name}")
                self.assertNotEqual(0, code, report)
                self.assertTrue(
                    any(item["code"] == expected_code for item in report["errors"]),
                    report,
                )

    def test_evidence_synthesis_intake_requires_review_receipt_not_radiogenomics_handoff(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package = root / "package"
            package.mkdir()
            fixture.make_docx(package / "manuscript.docx")
            evidence = intake_payload(
                package, "radiology", "Original Research", "initial", "double-anonymized",
            )
            evidence["study_scope"] = "evidence-synthesis"
            evidence["study_design"] = ["systematic-review-meta-analysis"]
            evidence["scientific_handoff_packet_digest"] = "not-applicable"
            evidence["scientific_prereview_receipt_digest"] = "4" * 64
            intake_path = root / "evidence-intake.json"
            write_json(intake_path, evidence)
            resolver_contract(
                self, intake_path, root / "resolved-evidence",
                "radiology::Original Research::initial",
            )

            variants: list[tuple[str, dict[str, object], str]] = []
            wrong_handoff = dict(evidence)
            wrong_handoff["scientific_handoff_packet_digest"] = "3" * 64
            variants.append(("radiogenomics-handoff", wrong_handoff, "EVIDENCE_SYNTHESIS_HANDOFF"))
            missing_prereview = dict(evidence)
            missing_prereview["scientific_prereview_receipt_digest"] = "not-applicable"
            variants.append(("missing-prereview", missing_prereview, "EVIDENCE_SYNTHESIS_PREREVIEW"))
            wrong_design = dict(evidence)
            wrong_design["study_design"] = ["observational"]
            variants.append(("wrong-design", wrong_design, "EVIDENCE_SYNTHESIS_DESIGN"))
            for name, payload, expected_code in variants:
                bad_path = root / f"{name}.json"
                write_json(bad_path, payload)
                code, report = run_resolver(bad_path, root / f"resolved-{name}")
                self.assertNotEqual(0, code, report)
                self.assertTrue(
                    any(item["code"] == expected_code for item in report["errors"]),
                    report,
                )

    def test_radiology_initial_intake_to_human_review(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package = root / "package"
            package.mkdir()
            rows = fixture.complete_radiology_rows(package)
            intake = intake_payload(package, "radiology", "Original Research", "initial", "double-anonymized")
            bind_upstream(rows, intake)
            intake_path = root / "intake.json"
            write_json(intake_path, intake)
            resolver_contract(self, intake_path, root / "resolved", "radiology::Original Research::initial")
            fixture.write_manifest(package, rows)
            code, report = fixture.run_audit(package)
            self.assertEqual(0, code, report)
            self.assertEqual("HUMAN_GATES_REQUIRED", report["whole_package_readiness"])
            self.assertEqual(["GOLDEN-PROJECT-001"], report["upstream_provenance"]["project_id"])
            self.assertEqual(["imaging-only"], report["upstream_provenance"]["study_scope"])
            self.assertEqual(["d" * 64], report["upstream_provenance"]["project_state_digest"])
            self.assertEqual(
                ["f" * 64], report["upstream_provenance"]["scientific_handoff_packet_digest"],
            )
            self.assertEqual("NOT_PERFORMED", report["upstream_provenance"]["authentication"])
            markdown = render_report(root, report)
            self.assertIn("Human review queue: `HUMAN_REVIEW_REQUIRED`", markdown)
            self.assertIn("Final human verdict: `[not assigned by renderer]`", markdown)

            main = next(row for row in rows if row["item_id"] == "MAIN")
            main_path = package / main["path"]
            fixture.make_docx(main_path, creator="Named Author")
            main["sha256"] = fixture.digest(main_path)
            fixture.write_manifest(package, rows)
            bad_code, bad_report = fixture.run_audit(package)
            self.assertNotEqual(0, bad_code)
            self.assertIn("BLIND_METADATA", fixture.codes(bad_report))

    def test_jno_revision_pair_and_receipt_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package = root / "package"
            package.mkdir()
            rows = jno_revision_rows(package)
            intake = intake_payload(
                package, "jama-network-open", "Original Investigation", "revision", "single-anonymized",
            )
            bind_upstream(rows, intake)
            intake_path = root / "intake.json"
            write_json(intake_path, intake)
            resolver_contract(
                self, intake_path, root / "resolved",
                "jama-network-open::Original Investigation::revision",
            )
            fixture.write_manifest(package, rows)
            code, report = fixture.run_audit(package)
            self.assertEqual(0, code, report)
            self.assertEqual("PASS", report["route"]["minimum_material_contract"])
            pair = next(row for row in rows if row["rule_id"] == "JNO-REV-FIG-MARKER-PAIR")
            pair["notes"] = pair["notes"].replace(
                next(row["sha256"] for row in rows if row["item_id"] == "PHOTO-MARKED"),
                "f" * 64,
            )
            fixture.write_manifest(package, rows)
            bad_code, bad_report = fixture.run_audit(package)
            self.assertNotEqual(0, bad_code)
            self.assertIn("ROUTE_FIGURE_PAIR_RECEIPT", fixture.codes(bad_report))

    def test_cancer_cell_final_latex_and_crosslink_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package = root / "package"
            package.mkdir()
            rows = fixture.complete_cancer_cell_final_rows(package, source_mode="latex-plus-pdf")
            intake = intake_payload(
                package, "cancer-cell", "Research Article", "final-files", "single-anonymized",
            )
            bind_upstream(rows, intake)
            intake_path = root / "intake.json"
            write_json(intake_path, intake)
            resolver_contract(
                self, intake_path, root / "resolved",
                "cancer-cell::Research Article::final-files",
            )
            fixture.write_manifest(package, rows)
            code, report = fixture.run_audit(package)
            self.assertEqual(0, code, report)
            self.assertEqual("HUMAN_GATES_REQUIRED", report["whole_package_readiness"])
            source = next(row for row in rows if row["path"].endswith(".tex"))
            source["notes"] = source["notes"].replace(
                source["notes"].split("latex_checked_pdf_sha256=", 1)[1].split(";", 1)[0],
                "f" * 64,
            )
            fixture.write_manifest(package, rows)
            bad_code, bad_report = fixture.run_audit(package)
            self.assertNotEqual(0, bad_code)
            self.assertIn("ROUTE_LATEX_RECEIPT", fixture.codes(bad_report))

    def test_npjdm_revision_isolates_portal_rule_and_then_closes_structurally(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package = root / "package"
            package.mkdir()
            rows = npjdm_revision_rows(package, resolve_figures=False)
            intake = intake_payload(
                package, "npj-digital-medicine", "Article", "revision", "single-anonymized",
            )
            bind_upstream(rows, intake)
            intake_path = root / "intake.json"
            write_json(intake_path, intake)
            resolver_contract(
                self, intake_path, root / "resolved",
                "npj-digital-medicine::Article::revision",
            )
            fixture.write_manifest(package, rows)
            code, report = fixture.run_audit(package)
            self.assertNotEqual(0, code)
            observed = fixture.codes(report)
            expected_portal_block = {"RULE_CURRENT_UNRESOLVED", "PORTAL_GATE_OPEN", "ROUTE_CURRENT_UNRESOLVED"}
            self.assertTrue(expected_portal_block.issubset(observed), report)
            self.assertEqual("BLOCKED_STRUCTURAL", report["whole_package_readiness"])
            self.assertEqual("FAIL", report["route"]["minimum_material_contract"])

            resolved_rows = npjdm_revision_rows(package, resolve_figures=True)
            bind_upstream(resolved_rows, intake)
            fixture.write_manifest(package, resolved_rows)
            closed_code, closed_report = fixture.run_audit(package)
            self.assertEqual(0, closed_code, closed_report)
            self.assertTrue(expected_portal_block.isdisjoint(fixture.codes(closed_report)))
            self.assertEqual("HUMAN_GATES_REQUIRED", closed_report["whole_package_readiness"])

    def test_partial_and_attachment_scopes_never_gain_package_readiness(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            package = root / "package"
            package.mkdir()
            rows = fixture.complete_radiology_rows(package)
            intake = intake_payload(
                package, "radiology", "Original Research", "initial", "double-anonymized",
                scope="partial",
            )
            bind_upstream(rows, intake)
            intake_path = root / "intake.json"
            write_json(intake_path, intake)
            plan = resolver_contract(
                self, intake_path, root / "resolved", "radiology::Original Research::initial",
            )
            self.assertEqual("partial", plan["intake"]["review_scope"])
            fixture.write_manifest(package, rows)
            for scope, coverage in (
                ("partial", "INVENTORY_PARTIAL"),
                ("attachment-set", "ATTACHMENT_SET_CLOSED"),
            ):
                code, report = fixture.run_audit(package, scope=scope)
                self.assertEqual(0, code, report)
                self.assertEqual(coverage, report["inventory"]["coverage"])
                self.assertEqual("INCOMPLETE_SCOPE", report["whole_package_readiness"])
                markdown = render_report(root, report)
                self.assertIn("Human review queue: `INCOMPLETE`", markdown)
            full_code, full_report = fixture.run_audit(package, scope="upload-root")
            self.assertEqual(0, full_code, full_report)
            self.assertEqual("HUMAN_GATES_REQUIRED", full_report["whole_package_readiness"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
