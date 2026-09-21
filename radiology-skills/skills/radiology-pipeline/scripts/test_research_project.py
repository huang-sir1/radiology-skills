#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import csv
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
INIT = SCRIPT_DIR / "init_research_project.py"
VALIDATE = SCRIPT_DIR / "validate_research_project.py"
COMPUTE_ANALYSIS_LOCK = SCRIPT_DIR / "compute_analysis_lock_digest.py"
COMPUTE_PROJECT_DIGESTS = SCRIPT_DIR / "compute_project_state_digests.py"
SPEC = importlib.util.spec_from_file_location("validate_research_project", VALIDATE)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def initialize(root: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(INIT), str(root), "--study-id", "TEST-001", "--title", "Test project"],
        check=False, capture_output=True, text=True, encoding="utf-8",
    )
    if result.returncode:
        raise AssertionError(result.stdout + result.stderr)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_packet_digest(payload: dict[str, object]) -> str:
    semantic = dict(payload)
    semantic.pop("packet_sha256", None)
    encoded = json.dumps(
        semantic, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def refresh_project_state_manifest_hash(root: Path) -> None:
    manifest = root / "research_record" / "artifact_manifest.csv"
    with manifest.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
        headers = list(rows[0])
    for row in rows:
        relative = row.get("path") or ""
        artifact = root / relative
        if relative != "research_record/artifact_manifest.csv" and artifact.is_file():
            row["sha256"] = digest(artifact)
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def append_csv_row(path: Path, values: dict[str, str]) -> None:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = list(reader.fieldnames or [])
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writerow({field: values.get(field, "") for field in headers})


def refresh_state_semantic_digests(state: dict[str, object]) -> None:
    state["analysis_lock_digest"] = MODULE.canonical_analysis_lock_digest(state["analysis_lock"])
    state["modality_role_digest"] = MODULE.canonical_modality_role_digest(state)
    state["project_state_digest"] = MODULE.canonical_project_state_digest(state)


class ResearchProjectTests(unittest.TestCase):
    def test_new_record_is_valid_working_state(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            report = MODULE.validate(root, "working")
            self.assertEqual("PASS", report["status"], json.dumps(report, indent=2))
            self.assertEqual(6, len(report["record_fingerprint"]))
            codes = {item["code"] for item in report["findings"]}
            self.assertIn("STUDY_SCOPE", codes)
            self.assertNotIn("ARTIFACT_HASH_MISMATCH", codes)

    def test_registry_tamper_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            values = root / "research_record" / "reported_values.csv"
            values.write_text(values.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            report = MODULE.validate(root, "working")
            self.assertEqual("FAIL", report["status"])
            codes = {item["code"] for item in report["findings"]}
            self.assertIn("ARTIFACT_HASH_MISMATCH", codes)

    def test_submission_cannot_skip_scope(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            report = MODULE.validate(root, "submission")
            self.assertEqual("FAIL", report["status"])
            codes = {item["code"] for item in report["findings"]}
            self.assertIn("STUDY_SCOPE", codes)

    def test_evidence_synthesis_scope_uses_review_topology_without_mechanism_handoff(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["research_scope"] = {
                "study_scope": "evidence-synthesis",
                "active_modalities": [],
                "external_reference_modalities": [],
                "generated_or_predicted_modalities": [],
                "proposed_validation_modalities": [],
            }
            state["evidence_topology"] = {
                "independent_unit": "study family",
                "biological_hierarchy": ["review", "study family", "report", "effect row"],
                "matched_intersections": [],
            }
            refresh_state_semantic_digests(state)
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            refresh_project_state_manifest_hash(root)
            working = MODULE.validate(root, "working")
            self.assertEqual("PASS", working["status"], json.dumps(working, indent=2))
            working_codes = {item["code"] for item in working["findings"]}
            self.assertNotIn("ACTIVE_MODALITY", working_codes)
            self.assertNotIn("MATCHED_INTERSECTION", working_codes)
            submission = MODULE.validate(root, "submission")
            submission_codes = {item["code"] for item in submission["findings"]}
            self.assertNotIn("HANDOFF_NOT_VALIDATED", submission_codes)
            self.assertNotIn("HANDOFF_PATH", submission_codes)

    def test_evidence_synthesis_rejects_generated_modality_role(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["research_scope"] = {
                "study_scope": "evidence-synthesis",
                "active_modalities": [],
                "external_reference_modalities": [],
                "generated_or_predicted_modalities": ["single-cell"],
                "proposed_validation_modalities": [],
            }
            state["evidence_topology"] = {
                "independent_unit": "study family",
                "biological_hierarchy": ["review", "study family", "report", "effect row"],
                "matched_intersections": [],
            }
            refresh_state_semantic_digests(state)
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            refresh_project_state_manifest_hash(root)
            report = MODULE.validate(root, "working")
            self.assertEqual("FAIL", report["status"])
            self.assertIn("SCOPE_MODALITY_CONFLICT", {item["code"] for item in report["findings"]})

    def test_evidence_synthesis_claim_accepts_synthesized_state(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["research_scope"] = {
                "study_scope": "evidence-synthesis",
                "active_modalities": [],
                "external_reference_modalities": [],
                "generated_or_predicted_modalities": [],
                "proposed_validation_modalities": [],
            }
            state["evidence_topology"] = {
                "independent_unit": "study family",
                "biological_hierarchy": ["review", "study family", "report", "effect row"],
                "matched_intersections": [],
            }
            refresh_state_semantic_digests(state)
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            append_csv_row(root / "research_record" / "claim_register.csv", {
                "claim_id": "CLM-SYN-001",
                "claim_text": "The frozen eligible evidence supports the bounded review conclusion.",
                "claim_type": "primary result",
                "cohort": "eligible study families",
                "evidence_artifacts": "ART-001",
                "primary_evidence_state": "synthesized",
                "modality_subtype": "systematic-narrative",
                "claim_link_status": "direct",
                "independent_unit": "study family",
                "matched_n": "not-applicable",
                "effect_uncertainty": "bounded synthesis with uncertainty and heterogeneity retained",
                "claim_branch": "association",
                "branch_verdict": "PASS",
                "maximum_wording": "supports the bounded synthesized conclusion",
                "residual_boundary": "limited to the eligible study families and declared route",
                "status": "supported",
                "manuscript_locations": "Results;Discussion",
                "protected_placement": "Abstract;Results;Discussion",
                "submission_eligible": "true",
                "owner": "radiology-systematic-review",
            })
            refresh_project_state_manifest_hash(root)
            report = MODULE.validate(root, "submission")
            codes = {item["code"] for item in report["findings"]}
            self.assertNotIn("CLAIM_EVIDENCE_STATE", codes, json.dumps(report, indent=2))
            self.assertIn("synthesized", MODULE.ALLOWED_EVIDENCE_STATES)

    def test_analysis_lock_digest_detects_semantic_tamper(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["analysis_lock"]["random_seed"] = 7
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            refresh_project_state_manifest_hash(root)
            report = MODULE.validate(root, "working")
            self.assertEqual("FAIL", report["status"])
            self.assertIn("ANALYSIS_LOCK_DIGEST_MISMATCH", {item["code"] for item in report["findings"]})

    def test_analysis_lock_cli_regenerates_canonical_digest(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["analysis_lock"]["random_seed"] = 19
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            stale = subprocess.run(
                [sys.executable, str(COMPUTE_ANALYSIS_LOCK), str(state_path)],
                check=False, capture_output=True, text=True, encoding="utf-8",
            )
            self.assertNotEqual(0, stale.returncode)
            refreshed = subprocess.run(
                [sys.executable, str(COMPUTE_ANALYSIS_LOCK), str(state_path), "--write"],
                check=False, capture_output=True, text=True, encoding="utf-8",
            )
            self.assertEqual(0, refreshed.returncode, refreshed.stdout + refreshed.stderr)
            written = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual(
                MODULE.canonical_analysis_lock_digest(written["analysis_lock"]),
                written["analysis_lock_digest"],
            )
            self.assertEqual(MODULE.canonical_modality_role_digest(written), written["modality_role_digest"])
            self.assertEqual(MODULE.canonical_project_state_digest(written), written["project_state_digest"])
            report = MODULE.validate(root, "working")
            self.assertNotIn("ARTIFACT_HASH_MISMATCH", {item["code"] for item in report["findings"]})

    def test_unified_project_digest_cli_regenerates_all_receipts(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["research_scope"]["study_scope"] = "imaging-only"
            state["research_scope"]["active_modalities"] = ["radiomics"]
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(COMPUTE_PROJECT_DIGESTS), str(state_path), "--write"],
                check=False, capture_output=True, text=True, encoding="utf-8",
            )
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            written = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual(MODULE.canonical_analysis_lock_digest(written["analysis_lock"]), written["analysis_lock_digest"])
            self.assertEqual(MODULE.canonical_modality_role_digest(written), written["modality_role_digest"])
            self.assertEqual(MODULE.canonical_project_state_digest(written), written["project_state_digest"])
            report = MODULE.validate(root, "working")
            self.assertNotIn("ARTIFACT_HASH_MISMATCH", {item["code"] for item in report["findings"]})

    def test_digest_write_refuses_missing_manifest_binding_before_state_change(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            manifest_path = root / "research_record" / "artifact_manifest.csv"
            with manifest_path.open(encoding="utf-8-sig", newline="") as handle:
                rows = list(csv.DictReader(handle))
                headers = list(rows[0])
            for row in rows:
                if row.get("path") == "research_record/project_state.json":
                    row["path"] = "research_record/not-project-state.json"
            with manifest_path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=headers)
                writer.writeheader()
                writer.writerows(rows)
            before = state_path.read_bytes()
            result = subprocess.run(
                [sys.executable, str(COMPUTE_PROJECT_DIGESTS), str(state_path), "--write"],
                check=False, capture_output=True, text=True, encoding="utf-8",
            )
            self.assertNotEqual(0, result.returncode)
            self.assertIn("exactly one path binding", result.stdout)
            self.assertEqual(before, state_path.read_bytes())

    def test_role_and_project_digests_detect_scope_tamper(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["research_scope"] = {
                "study_scope": "imaging-only",
                "active_modalities": ["radiomics"],
                "external_reference_modalities": ["single-cell"],
                "generated_or_predicted_modalities": [],
                "proposed_validation_modalities": [],
            }
            refresh_state_semantic_digests(state)
            state["research_scope"]["external_reference_modalities"].append("spatial")
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            refresh_project_state_manifest_hash(root)
            report = MODULE.validate(root, "working")
            codes = {item["code"] for item in report["findings"]}
            self.assertIn("MODALITY_ROLE_DIGEST_MISMATCH", codes)
            self.assertIn("PROJECT_STATE_DIGEST_MISMATCH", codes)

    def test_project_state_digest_detects_non_role_tamper(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["project_title"] = "Changed after receipt"
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            refresh_project_state_manifest_hash(root)
            report = MODULE.validate(root, "working")
            codes = {item["code"] for item in report["findings"]}
            self.assertIn("PROJECT_STATE_DIGEST_MISMATCH", codes)
            self.assertNotIn("MODALITY_ROLE_DIGEST_MISMATCH", codes)

    def test_schema_12_is_working_legacy_but_submission_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["schema_version"] = "1.2"
            state.pop("modality_role_digest", None)
            state.pop("project_state_digest", None)
            state["analysis_lock_digest"] = MODULE.canonical_analysis_lock_digest(state["analysis_lock"])
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            refresh_project_state_manifest_hash(root)
            working = MODULE.validate(root, "working")
            submission = MODULE.validate(root, "submission")
            self.assertIn("STATE_SCHEMA_LEGACY", {item["code"] for item in working["findings"]})
            self.assertEqual("PASS", working["status"])
            self.assertEqual("FAIL", submission["status"])

    def test_schema_12_requires_explicit_cli_migration_to_13(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["schema_version"] = "1.2"
            state.pop("modality_role_digest", None)
            state.pop("project_state_digest", None)
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            implicit = subprocess.run(
                [sys.executable, str(COMPUTE_PROJECT_DIGESTS), str(state_path), "--write"],
                check=False, capture_output=True, text=True, encoding="utf-8",
            )
            self.assertNotEqual(0, implicit.returncode)
            migrated = subprocess.run(
                [
                    sys.executable, str(COMPUTE_PROJECT_DIGESTS), str(state_path),
                    "--write", "--migrate-to-current",
                ],
                check=False, capture_output=True, text=True, encoding="utf-8",
            )
            self.assertEqual(0, migrated.returncode, migrated.stdout + migrated.stderr)
            written = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual("1.3", written["schema_version"])
            self.assertEqual(MODULE.canonical_modality_role_digest(written), written["modality_role_digest"])
            self.assertEqual(MODULE.canonical_project_state_digest(written), written["project_state_digest"])
            report = MODULE.validate(root, "working")
            self.assertEqual("PASS", report["status"], json.dumps(report, indent=2))
            self.assertNotIn("STATE_SCHEMA_LEGACY", {item["code"] for item in report["findings"]})
            self.assertNotIn("ARTIFACT_HASH_MISMATCH", {item["code"] for item in report["findings"]})

    def test_pre_12_schema_refuses_automatic_semantic_migration(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["schema_version"] = "1.1"
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable, str(COMPUTE_PROJECT_DIGESTS), str(state_path),
                    "--write", "--migrate-to-current",
                ],
                check=False, capture_output=True, text=True, encoding="utf-8",
            )
            self.assertNotEqual(0, result.returncode)
            self.assertIn("manual migration", result.stdout)

    def test_modality_roles_cannot_overlap_in_project_state(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["research_scope"] = {
                "study_scope": "imaging-only",
                "active_modalities": ["radiomics"],
                "external_reference_modalities": [],
                "generated_or_predicted_modalities": ["radiomics"],
                "proposed_validation_modalities": [],
            }
            refresh_state_semantic_digests(state)
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            refresh_project_state_manifest_hash(root)
            report = MODULE.validate(root, "working")
            self.assertEqual("FAIL", report["status"])
            self.assertIn("MODALITY_ROLE_OVERLAP", {item["code"] for item in report["findings"]})

    def test_malformed_modality_role_returns_structured_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["research_scope"]["active_modalities"] = [{"not": "a modality"}]
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            report = MODULE.validate(root, "working")
            self.assertEqual("FAIL", report["status"])
            self.assertIn("MODALITY_ROLE", {item["code"] for item in report["findings"]})

    def test_explicit_imaging_only_scope_does_not_require_mechanism_handoff(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["research_scope"] = {
                "study_scope": "imaging-only",
                "active_modalities": ["radiomics"],
                "external_reference_modalities": [],
                "generated_or_predicted_modalities": [],
                "proposed_validation_modalities": [],
            }
            state["evidence_topology"] = {
                "independent_unit": "patient",
                "biological_hierarchy": ["patient", "scan", "ROI"],
                "matched_intersections": [{
                    "analysis_id": "AN-IMG", "unit": "patient", "n": 20,
                    "not_applicable_reason": "", "definition": "analysis cohort",
                    "source_artifact_id": "ART-002",
                }],
            }
            refresh_state_semantic_digests(state)
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            refresh_project_state_manifest_hash(root)
            report = MODULE.validate(root, "submission")
            codes = {item["code"] for item in report["findings"]}
            self.assertNotIn("HANDOFF_NOT_VALIDATED", codes)
            self.assertNotIn("HANDOFF_PATH", codes)

    def test_standalone_deep_learning_is_valid_imaging_modality(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["research_scope"] = {
                "study_scope": "imaging-only",
                "active_modalities": ["deep-learning"],
                "external_reference_modalities": [],
                "generated_or_predicted_modalities": [],
                "proposed_validation_modalities": [],
            }
            state["evidence_topology"] = {
                "independent_unit": "patient",
                "biological_hierarchy": ["patient", "scan", "image"],
                "matched_intersections": [{
                    "analysis_id": "AN-DL", "unit": "patient", "n": 20,
                    "not_applicable_reason": "", "definition": "deep-learning analysis cohort",
                    "source_artifact_id": "ART-002",
                }],
            }
            refresh_state_semantic_digests(state)
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            refresh_project_state_manifest_hash(root)
            report = MODULE.validate(root, "working")
            codes = {item["code"] for item in report["findings"]}
            self.assertNotIn("MODALITY_ROLE", codes)
            self.assertNotIn("SCOPE_MODALITY_CONFLICT", codes)

    def test_validated_status_cannot_hide_invalid_handoff_packet(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            packet = root / "bad-packet.json"
            packet.write_text('{"garbage": true}\n', encoding="utf-8")
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            state["scientific_handoff"] = {
                "status": "validated",
                "packet_path": "bad-packet.json",
                "canonical_packet_sha256": "0" * 64,
                "packet_file_sha256": digest(packet),
                "source_manifest_digest": "1" * 64,
                "claim_register_sha256": digest(root / "research_record" / "claim_register.csv"),
            }
            refresh_state_semantic_digests(state)
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            refresh_project_state_manifest_hash(root)
            report = MODULE.validate(root, "working")
            self.assertEqual("FAIL", report["status"])
            self.assertIn("HANDOFF_SEMANTIC", {item["code"] for item in report["findings"]})

    def test_valid_semantic_handoff_binds_both_digest_types(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initialize(root)
            state_path = root / "research_record" / "project_state.json"
            state = json.loads(state_path.read_text(encoding="utf-8"))
            topology = {
                "independent_unit": "donor",
                "biological_hierarchy": ["donor", "sample", "cell"],
                "matched_intersections": [{
                    "analysis_id": "AN-01", "unit": "donor", "n": 12,
                    "not_applicable_reason": "", "definition": "QC-passing donors",
                    "source_artifact_id": "ART-101",
                }],
            }
            state["research_scope"] = {
                "study_scope": "mechanism-only",
                "active_modalities": ["single-cell"],
                "external_reference_modalities": [],
                "generated_or_predicted_modalities": [],
                "proposed_validation_modalities": [],
            }
            state["evidence_topology"] = topology
            state["analysis_lock"]["source_manifest_sha256"] = "1" * 64
            refresh_state_semantic_digests(state)
            result_artifact = root / "analysis-result.json"
            result_artifact.write_text('{"result": "donor association"}\n', encoding="utf-8")
            result_digest = digest(result_artifact)
            append_csv_row(root / "research_record" / "artifact_manifest.csv", {
                "artifact_id": "ART-101", "category": "analysis-result",
                "path": "analysis-result.json", "producer": "radiology-radiogenomics",
                "status": "current", "version": "v1", "sha256": result_digest,
                "required_for_submission": "false",
            })
            claim_text = "A donor-level state shift was associated with outcome."
            append_csv_row(root / "research_record" / "claim_register.csv", {
                "claim_id": "CLM-001", "claim_text": claim_text,
                "claim_type": "primary result", "cohort": "analysis cohort",
                "evidence_artifacts": "ART-101", "primary_evidence_state": "associated",
                "modality_subtype": "scRNA pseudobulk", "claim_link_status": "direct",
                "independent_unit": "donor", "matched_n": "12",
                "effect_uncertainty": "effect and 95% CI in ART-101",
                "claim_branch": "association", "branch_verdict": "PASS",
                "maximum_wording": "associated with", "residual_boundary": "No causal claim",
                "status": "supported", "protected_placement": "Results 2",
                "submission_eligible": "true",
            })
            claim_digest = digest(root / "research_record" / "claim_register.csv")
            packet_payload: dict[str, object] = {
                "schema_version": "1.1", "packet_id": "WHP-001", "study_id": "TEST-001",
                "study_scope": "mechanism-only", "source_manifest_digest": "1" * 64,
                "analysis_lock_digest": state["analysis_lock_digest"],
                "claim_register_sha256": claim_digest,
                "source_artifacts": [{"artifact_id": "ART-101", "version": "v1", "sha256": result_digest}],
                "modality_roles": {
                    "active": ["single-cell"], "external_reference": [],
                    "generated_or_predicted": [], "proposed_validation": [],
                },
                "evidence_topology": topology,
                "claims": [{
                    "claim_id": "CLM-001", "claim_text": claim_text,
                    "evidence_pointers": ["ART-101:table donor_pseudobulk"],
                    "primary_evidence_state": "associated", "modality_subtype": "scRNA pseudobulk",
                    "claim_link_status": "direct", "independent_unit": "donor", "matched_n": 12,
                    "effect_uncertainty": "effect and 95% CI in ART-101", "claim_branch": "association",
                    "branch_verdict": "PASS", "maximum_wording": "associated with",
                    "protected_placement": ["Results 2"], "residual_boundary": "No causal claim",
                }],
                "terminology_lock": ["donor"], "writing_handoff_status": "W-HANDOFF-READY",
                "author_input_needed": [], "packet_sha256": "",
            }
            packet_payload["packet_sha256"] = canonical_packet_digest(packet_payload)
            packet = root / "scientific-handoff.json"
            packet.write_text(json.dumps(packet_payload, indent=2) + "\n", encoding="utf-8")
            state["scientific_handoff"] = {
                "status": "validated", "packet_path": "scientific-handoff.json",
                "canonical_packet_sha256": packet_payload["packet_sha256"],
                "packet_file_sha256": digest(packet), "source_manifest_digest": "1" * 64,
                "claim_register_sha256": claim_digest,
            }
            refresh_state_semantic_digests(state)
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            refresh_project_state_manifest_hash(root)
            report = MODULE.validate(root, "working")
            self.assertEqual("PASS", report["status"], json.dumps(report, indent=2))
            self.assertFalse(any(item["code"].startswith("HANDOFF_") for item in report["findings"]))

            packet_payload["source_artifacts"][0]["sha256"] = "3" * 64
            packet_payload["packet_sha256"] = canonical_packet_digest(packet_payload)
            packet.write_text(json.dumps(packet_payload, indent=2) + "\n", encoding="utf-8")
            state["scientific_handoff"]["canonical_packet_sha256"] = packet_payload["packet_sha256"]
            state["scientific_handoff"]["packet_file_sha256"] = digest(packet)
            refresh_state_semantic_digests(state)
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            refresh_project_state_manifest_hash(root)
            drift_report = MODULE.validate(root, "working")
            self.assertIn(
                "HANDOFF_ARTIFACT_DRIFT",
                {item["code"] for item in drift_report["findings"]},
            )

            packet_payload["source_artifacts"][0]["sha256"] = result_digest
            packet_payload["claims"][0]["maximum_wording"] = "causes"
            packet_payload["packet_sha256"] = canonical_packet_digest(packet_payload)
            packet.write_text(json.dumps(packet_payload, indent=2) + "\n", encoding="utf-8")
            state["scientific_handoff"]["canonical_packet_sha256"] = packet_payload["packet_sha256"]
            state["scientific_handoff"]["packet_file_sha256"] = digest(packet)
            refresh_state_semantic_digests(state)
            state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
            refresh_project_state_manifest_hash(root)
            claim_drift_report = MODULE.validate(root, "working")
            self.assertIn(
                "HANDOFF_CLAIM_FIELD_DRIFT",
                {item["code"] for item in claim_drift_report["findings"]},
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
