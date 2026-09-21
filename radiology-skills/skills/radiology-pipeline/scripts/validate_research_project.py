#!/usr/bin/env python3
"""Validate radiology-pipeline project records and cross-register references."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


REQUIRED_FILES = (
    "project_state.json",
    "reported_values.csv",
    "claim_register.csv",
    "display_register.csv",
    "artifact_manifest.csv",
    "decision_log.csv",
)
REQUIRED_STATE_KEYS = (
    "schema_version",
    "study_id",
    "project_title",
    "data_provenance",
    "teaching_only",
    "target_venue",
    "core_design",
    "analysis_lock",
    "reporting_stack",
    "current_stage",
    "stage_status",
    "hard_gates",
    "unresolved_items",
    "last_updated",
)
EXTENDED_STATE_KEYS = ("research_scope", "evidence_topology", "scientific_handoff")
CURRENT_STATE_SCHEMA = "1.3"
SPLIT_HANDOFF_DIGEST_SCHEMAS = {"1.2", CURRENT_STATE_SCHEMA}
ALLOWED_PROVENANCE = {"real", "simulated", "mixed"}
ALLOWED_GATE_STATUS = {"PASS", "CONDITIONAL", "FAIL", "NOT_APPLICABLE"}
ALLOWED_CLAIM_STATUS = {"supported", "partial", "unsupported", "pending", "simulated"}
ALLOWED_VALUE_STATUS = {"verified", "pending", "superseded", "simulated"}
ALLOWED_ARTIFACT_STATUS = {"current", "stale", "pending", "superseded", "missing"}
ALLOWED_STUDY_SCOPES = {
    "imaging-only", "mechanism-only", "imaging-mechanism", "evidence-synthesis",
}
ALLOWED_MODALITIES = {
    "radiomics", "deep-learning", "bulk-rna", "single-cell", "spatial", "pathology", "deep-fusion",
    "multi-omics", "other-omics", "perturbation",
}
ALLOWED_HANDOFF_STATUS = {"not-created", "draft", "validated", "superseded"}
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
ARTIFACT_MANIFEST_HEADERS = {
    "artifact_id", "category", "path", "producer", "status", "version", "sha256",
    "source_inputs", "source_input_sha256s", "source_manifest_digest",
    "required_for_submission", "last_verified", "notes",
}
CLAIM_HANDOFF_HEADERS = {
    "primary_evidence_state", "modality_subtype", "claim_link_status", "independent_unit",
    "matched_n", "effect_uncertainty", "claim_branch", "branch_verdict", "maximum_wording",
    "residual_boundary", "protected_placement",
}
ALLOWED_EVIDENCE_STATES = {
    "measured", "derived", "estimated", "associated", "predicted", "perturbed", "synthesized",
}
ALLOWED_CLAIM_LINK_STATUS = {"direct", "inferred", "proposed"}
ALLOWED_CLAIM_BRANCHES = {
    "technical-validity", "descriptive", "association", "localization-or-concordance",
    "prognostic-prediction", "treatment-effect", "mechanistic", "causal",
}
ALLOWED_BRANCH_VERDICTS = {"PASS", "CONDITIONAL", "STOP"}
PLACEHOLDER_RE = re.compile(r"(?:TODO|TBD|TO CONFIRM|AUTHOR_INPUT_NEEDED|VERIFY_FROM_CURRENT_GUIDE)", re.I)
HANDOFF_VALIDATOR_PATH = (
    Path(__file__).resolve().parents[2]
    / "radiology-radiogenomics" / "scripts" / "validate_scientific_handoff.py"
)


@dataclass
class Finding:
    severity: str
    code: str
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", help="Project root or research_record directory")
    parser.add_argument("--mode", choices=("working", "submission"), default="working")
    parser.add_argument("--json-output", help="Optional JSON report path")
    return parser.parse_args()


def split_ids(value: str) -> list[str]:
    return [item.strip() for item in re.split(r"[;,|]", value or "") if item.strip()]


def read_csv(path: Path, findings: list[Finding]) -> list[dict[str, str]]:
    try:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames or any(not (name or "").strip() for name in reader.fieldnames):
                findings.append(Finding("ERROR", "CSV_HEADER", f"Invalid header in {path.name}"))
                return []
            if len(set(reader.fieldnames)) != len(reader.fieldnames):
                findings.append(Finding("ERROR", "CSV_DUP_HEADER", f"Duplicate header in {path.name}"))
                return []
            return [dict(row) for row in reader]
    except (OSError, csv.Error) as exc:
        findings.append(Finding("ERROR", "CSV_READ", f"Cannot read {path.name}: {exc}"))
        return []


def read_csv_headers(path: Path) -> set[str]:
    try:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            return set(next(csv.reader(handle), []))
    except (OSError, csv.Error, StopIteration):
        return set()


def require_unique(rows: Iterable[dict[str, str]], field: str, file_name: str, findings: list[Finding]) -> set[str]:
    seen: set[str] = set()
    for index, row in enumerate(rows, start=2):
        value = (row.get(field) or "").strip()
        if not value:
            findings.append(Finding("ERROR", "ID_MISSING", f"{file_name}:{index} missing {field}"))
        elif value in seen:
            findings.append(Finding("ERROR", "ID_DUPLICATE", f"{file_name}:{index} duplicate {value}"))
        else:
            seen.add(value)
    return seen


def bool_value(value: str) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "y"}


def canonical_analysis_lock_digest(analysis_lock: object) -> str:
    encoded = json.dumps(
        analysis_lock, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def canonical_modality_role_digest(state: dict[str, object]) -> str:
    research_scope = state.get("research_scope") or {}
    if not isinstance(research_scope, dict):
        raise ValueError("research_scope must be an object")
    role_fields = {
        "active": "active_modalities",
        "external_reference": "external_reference_modalities",
        "generated_or_predicted": "generated_or_predicted_modalities",
        "proposed_validation": "proposed_validation_modalities",
    }
    roles: dict[str, list[str]] = {}
    for canonical_name, state_name in role_fields.items():
        values = research_scope.get(state_name)
        if not isinstance(values, list) or any(not isinstance(value, str) for value in values):
            raise ValueError(f"research_scope.{state_name} must be a string list")
        roles[canonical_name] = sorted(values)
    semantic = {
        "schema_version": state.get("schema_version"),
        "study_id": state.get("study_id"),
        "study_scope": research_scope.get("study_scope"),
        "modality_roles": roles,
    }
    encoded = json.dumps(
        semantic, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def canonical_project_state_digest(state: dict[str, object]) -> str:
    semantic = dict(state)
    semantic.pop("project_state_digest", None)
    encoded = json.dumps(
        semantic, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def run_scientific_handoff_validator(packet_path: Path) -> tuple[dict[str, object], dict[str, object]]:
    if not HANDOFF_VALIDATOR_PATH.is_file():
        raise OSError(f"scientific handoff validator is missing: {HANDOFF_VALIDATOR_PATH}")
    spec = importlib.util.spec_from_file_location(
        "radiology_scientific_handoff_validator", HANDOFF_VALIDATOR_PATH,
    )
    if spec is None or spec.loader is None:
        raise OSError("scientific handoff validator could not be loaded")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    payload = json.loads(packet_path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("scientific handoff packet root must be an object")
    return module.validate(payload, require_ready=True), payload


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def find_record_dir(project_dir: Path) -> Path:
    direct = project_dir / "project_state.json"
    if direct.exists():
        return project_dir
    return project_dir / "research_record"


def validate(project_dir: Path, mode: str) -> dict[str, object]:
    findings: list[Finding] = []
    record_dir = find_record_dir(project_dir)
    for name in REQUIRED_FILES:
        if not (record_dir / name).exists():
            findings.append(Finding("ERROR", "FILE_MISSING", f"Missing research_record/{name}"))
    if any(item.code == "FILE_MISSING" for item in findings):
        return summarize(record_dir, mode, findings)

    try:
        state = json.loads((record_dir / "project_state.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        findings.append(Finding("ERROR", "STATE_READ", f"Cannot parse project_state.json: {exc}"))
        return summarize(record_dir, mode, findings)

    for key in REQUIRED_STATE_KEYS:
        if key not in state:
            findings.append(Finding("ERROR", "STATE_KEY", f"project_state.json missing {key}"))

    state_schema = str(state.get("schema_version") or "")
    if state_schema not in {"1.0", "1.1", "1.2", CURRENT_STATE_SCHEMA}:
        findings.append(Finding("ERROR", "STATE_SCHEMA", f"Unsupported state schema: {state_schema!r}"))
    legacy_schema = state_schema == "1.0"
    if legacy_schema:
        findings.append(Finding(
            "ERROR" if mode == "submission" else "WARNING",
            "STATE_SCHEMA_LEGACY",
            "Schema 1.0 lacks scope-aware scientific handoff and canonical identity fields; migrate to 1.3",
        ))
    else:
        for key in EXTENDED_STATE_KEYS:
            if key not in state:
                findings.append(Finding("ERROR", "STATE_KEY", f"project_state.json missing {key}"))
    if state_schema == "1.1":
        findings.append(Finding(
            "ERROR" if mode == "submission" else "WARNING",
            "STATE_SCHEMA_LEGACY",
            "Schema 1.1 conflates packet semantic/file digests and lacks current canonical receipts; migrate to 1.3",
        ))
    if state_schema == "1.2":
        findings.append(Finding(
            "ERROR" if mode == "submission" else "WARNING",
            "STATE_SCHEMA_LEGACY",
            "Schema 1.2 lacks canonical modality_role_digest and project_state_digest; migrate to 1.3",
        ))
    if state_schema == CURRENT_STATE_SCHEMA:
        for key in ("analysis_lock_digest", "modality_role_digest", "project_state_digest"):
            if key not in state:
                findings.append(Finding("ERROR", "STATE_KEY", f"project_state.json missing {key}"))

    provenance = state.get("data_provenance")
    if provenance not in ALLOWED_PROVENANCE:
        findings.append(Finding("ERROR", "PROVENANCE", f"Invalid data_provenance: {provenance!r}"))
    if provenance in {"simulated", "mixed"} and state.get("teaching_only") is not True:
        findings.append(Finding("ERROR", "SIMULATION_LABEL", "Simulated/mixed projects must set teaching_only=true"))
    if mode == "submission" and provenance != "real":
        findings.append(Finding("ERROR", "SIMULATION_SUBMISSION", "Submission mode requires data_provenance=real"))

    analysis_lock_object = state.get("analysis_lock") or {}
    if not isinstance(analysis_lock_object, dict):
        findings.append(Finding("ERROR", "ANALYSIS_SHAPE", "analysis_lock must be an object"))
        analysis_lock_object = {}
    if state_schema in SPLIT_HANDOFF_DIGEST_SCHEMAS:
        declared_analysis_digest = str(state.get("analysis_lock_digest") or "").strip()
        try:
            computed_analysis_digest = canonical_analysis_lock_digest(analysis_lock_object)
        except (TypeError, ValueError, OverflowError) as exc:
            findings.append(Finding("ERROR", "ANALYSIS_LOCK_DIGEST", f"analysis_lock cannot be canonicalized: {exc}"))
            computed_analysis_digest = ""
        if not SHA_RE.fullmatch(declared_analysis_digest):
            findings.append(Finding(
                "ERROR" if mode == "submission" else "WARNING",
                "ANALYSIS_LOCK_DIGEST",
                "analysis_lock_digest must be a 64-character canonical SHA-256",
            ))
        elif computed_analysis_digest and declared_analysis_digest != computed_analysis_digest:
            findings.append(Finding(
                "ERROR", "ANALYSIS_LOCK_DIGEST_MISMATCH",
                "analysis_lock_digest does not match the canonical analysis_lock object",
            ))
    if state_schema == CURRENT_STATE_SCHEMA:
        declared_modality_digest = str(state.get("modality_role_digest") or "").strip()
        try:
            computed_modality_digest = canonical_modality_role_digest(state)
        except (TypeError, ValueError, OverflowError) as exc:
            findings.append(Finding("ERROR", "MODALITY_ROLE_DIGEST", f"modality roles cannot be canonicalized: {exc}"))
            computed_modality_digest = ""
        if not SHA_RE.fullmatch(declared_modality_digest) or declared_modality_digest == "0" * 64:
            findings.append(Finding("ERROR", "MODALITY_ROLE_DIGEST", "modality_role_digest must be a nonzero canonical SHA-256"))
        elif computed_modality_digest and declared_modality_digest != computed_modality_digest:
            findings.append(Finding("ERROR", "MODALITY_ROLE_DIGEST_MISMATCH", "modality_role_digest does not match study/scope/role content"))
        declared_project_digest = str(state.get("project_state_digest") or "").strip()
        try:
            computed_project_digest = canonical_project_state_digest(state)
        except (TypeError, ValueError, OverflowError) as exc:
            findings.append(Finding("ERROR", "PROJECT_STATE_DIGEST", f"project state cannot be canonicalized: {exc}"))
            computed_project_digest = ""
        if not SHA_RE.fullmatch(declared_project_digest) or declared_project_digest == "0" * 64:
            findings.append(Finding("ERROR", "PROJECT_STATE_DIGEST", "project_state_digest must be a nonzero canonical SHA-256"))
        elif computed_project_digest and declared_project_digest != computed_project_digest:
            findings.append(Finding("ERROR", "PROJECT_STATE_DIGEST_MISMATCH", "project_state_digest does not match canonical project state"))

    if not str(state.get("study_id") or "").strip():
        findings.append(Finding("ERROR", "STUDY_ID", "study_id is empty"))
    if not str(state.get("project_title") or "").strip():
        findings.append(Finding("ERROR", "PROJECT_TITLE", "project_title is empty"))

    research_scope = state.get("research_scope") or {}
    if not isinstance(research_scope, dict):
        findings.append(Finding("ERROR", "SCOPE_SHAPE", "research_scope must be an object"))
        research_scope = {}
    study_scope = str(research_scope.get("study_scope") or "")
    if not legacy_schema or study_scope:
        if not study_scope:
            findings.append(Finding(
                "ERROR" if mode == "submission" else "WARNING", "STUDY_SCOPE",
                "study_scope has not been locked",
            ))
        elif study_scope not in ALLOWED_STUDY_SCOPES:
            findings.append(Finding("ERROR", "STUDY_SCOPE", f"Invalid study_scope: {study_scope!r}"))
        role_fields = (
            "active_modalities", "external_reference_modalities",
            "generated_or_predicted_modalities", "proposed_validation_modalities",
        )
        role_values: dict[str, set[str]] = {}
        for field in role_fields:
            values = research_scope.get(field)
            if not isinstance(values, list):
                findings.append(Finding("ERROR", "MODALITY_ROLE", f"research_scope.{field} must be a list"))
                values = []
            elif any(not isinstance(value, str) for value in values):
                findings.append(Finding(
                    "ERROR", "MODALITY_ROLE",
                    f"research_scope.{field} must contain only string modality names",
                ))
                values = [value for value in values if isinstance(value, str)]
            if len(values) != len(set(values)):
                findings.append(Finding("ERROR", "MODALITY_ROLE", f"research_scope.{field} contains duplicates"))
            invalid = sorted(set(values) - ALLOWED_MODALITIES)
            if invalid:
                findings.append(Finding("ERROR", "MODALITY_ROLE", f"research_scope.{field} invalid: {invalid}"))
            role_values[field] = set(values)
        role_memberships: dict[str, list[str]] = {}
        for field, values in role_values.items():
            for modality in values:
                role_memberships.setdefault(modality, []).append(field)
        for modality, memberships in sorted(role_memberships.items()):
            if len(memberships) > 1:
                findings.append(Finding(
                    "ERROR", "MODALITY_ROLE_OVERLAP",
                    f"Modality {modality!r} appears in multiple research_scope role groups: "
                    + ", ".join(memberships),
                ))
        active_modalities = role_values.get("active_modalities", set())
        if not active_modalities and study_scope != "evidence-synthesis":
            findings.append(Finding("ERROR" if mode == "submission" else "WARNING", "ACTIVE_MODALITY", "No active modality recorded"))
        imaging_modalities = {"radiomics", "deep-learning", "deep-fusion"}
        mechanism_modalities = ALLOWED_MODALITIES - imaging_modalities
        if study_scope == "imaging-only" and active_modalities - imaging_modalities:
            findings.append(Finding("ERROR", "SCOPE_MODALITY_CONFLICT", "imaging-only has active mechanism modalities"))
        if study_scope == "mechanism-only" and active_modalities & imaging_modalities:
            findings.append(Finding("ERROR", "SCOPE_MODALITY_CONFLICT", "mechanism-only has active imaging/fusion modalities"))
        if study_scope == "imaging-mechanism" and (
            not active_modalities & imaging_modalities or not active_modalities & mechanism_modalities
        ):
            findings.append(Finding("ERROR", "SCOPE_MODALITY_CONFLICT", "imaging-mechanism requires both active imaging and mechanism modalities"))
        if study_scope == "evidence-synthesis" and (
            role_values.get("generated_or_predicted_modalities", set())
            or role_values.get("proposed_validation_modalities", set())
        ):
            findings.append(Finding(
                "ERROR", "SCOPE_MODALITY_CONFLICT",
                "evidence-synthesis records included evidence domains as active/external-reference roles; "
                "it cannot relabel generated or proposed-validation modalities as synthesized evidence",
            ))

    evidence_topology = state.get("evidence_topology") or {}
    if not isinstance(evidence_topology, dict):
        findings.append(Finding("ERROR", "TOPOLOGY_SHAPE", "evidence_topology must be an object"))
        evidence_topology = {}
    if not legacy_schema:
        if not str(evidence_topology.get("independent_unit") or "").strip():
            findings.append(Finding("ERROR" if mode == "submission" else "WARNING", "INDEPENDENT_UNIT", "evidence_topology.independent_unit is empty"))
        hierarchy = evidence_topology.get("biological_hierarchy")
        if not isinstance(hierarchy, list) or not hierarchy:
            findings.append(Finding("ERROR" if mode == "submission" else "WARNING", "BIOLOGICAL_HIERARCHY", "No biological hierarchy recorded"))
        intersections = evidence_topology.get("matched_intersections")
        if study_scope != "evidence-synthesis" and (not isinstance(intersections, list) or not intersections):
            findings.append(Finding("ERROR" if mode == "submission" else "WARNING", "MATCHED_INTERSECTION", "No usable matched intersection recorded"))

    hard_gates = state.get("hard_gates") or {}
    if not isinstance(hard_gates, dict):
        findings.append(Finding("ERROR", "GATES_SHAPE", "hard_gates must be an object"))
    else:
        for gate, payload in hard_gates.items():
            status = payload.get("status") if isinstance(payload, dict) else payload
            if status not in ALLOWED_GATE_STATUS:
                findings.append(Finding("ERROR", "GATE_STATUS", f"Gate {gate} has invalid status {status!r}"))
            if mode == "submission" and status == "FAIL":
                findings.append(Finding("ERROR", "GATE_FAIL", f"Gate {gate} is FAIL"))
            if mode == "submission" and status == "CONDITIONAL":
                findings.append(Finding("WARNING", "GATE_CONDITIONAL", f"Gate {gate} remains CONDITIONAL"))
        if mode == "submission" and not hard_gates:
            findings.append(Finding("ERROR", "GATES_EMPTY", "No hard gates recorded"))

    unresolved = state.get("unresolved_items") or []
    if mode == "submission" and unresolved:
        findings.append(Finding("ERROR", "UNRESOLVED", f"{len(unresolved)} unresolved project item(s) remain"))

    venue = state.get("target_venue") or {}
    if not isinstance(venue, dict):
        findings.append(Finding("ERROR", "VENUE_SHAPE", "target_venue must be an object"))
        venue = {}
    if mode == "submission":
        for key, value in venue.items():
            if PLACEHOLDER_RE.search(str(value or "")):
                findings.append(Finding("ERROR", "VENUE_PLACEHOLDER", f"target_venue.{key} contains unresolved placeholder"))
        for key in ("journal", "article_type", "guide_source", "verified_on"):
            if not str(venue.get(key) or "").strip():
                findings.append(Finding("ERROR", "VENUE_GUIDE", f"target_venue.{key} is empty"))
        core_design = state.get("core_design") or {}
        if not isinstance(core_design, dict):
            findings.append(Finding("ERROR", "DESIGN_SHAPE", "core_design must be an object"))
            core_design = {}
        for key in (
            "disease_population",
            "modality",
            "primary_endpoint_estimand",
            "unit_of_analysis",
            "primary_model",
            "validation_design",
        ):
            if not str(core_design.get(key) or "").strip():
                findings.append(Finding("ERROR", "DESIGN_LOCK", f"core_design.{key} is empty"))
        if not core_design.get("cohorts"):
            findings.append(Finding("ERROR", "DESIGN_LOCK", "core_design.cohorts is empty"))
        analysis_lock = analysis_lock_object
        if analysis_lock.get("status") not in {"locked", "frozen"}:
            findings.append(Finding("ERROR", "ANALYSIS_LOCK", "analysis_lock.status must be locked or frozen"))
        for key in ("source_manifest", "software_environment"):
            if not str(analysis_lock.get(key) or "").strip():
                findings.append(Finding("ERROR", "ANALYSIS_LOCK", f"analysis_lock.{key} is empty"))
        for key in ("source_manifest_sha256", "software_environment_sha256"):
            value = str(analysis_lock.get(key) or "").strip()
            if not SHA_RE.fullmatch(value):
                findings.append(Finding("ERROR", "ANALYSIS_LOCK_DIGEST", f"analysis_lock.{key} is not a SHA-256"))
        if study_scope in {"imaging-only", "imaging-mechanism"}:
            if not str(analysis_lock.get("split_manifest") or "").strip():
                findings.append(Finding("ERROR", "ANALYSIS_LOCK", "analysis_lock.split_manifest is empty for an imaging/predictive scope"))
            if not SHA_RE.fullmatch(str(analysis_lock.get("split_manifest_sha256") or "").strip()):
                findings.append(Finding("ERROR", "ANALYSIS_LOCK_DIGEST", "analysis_lock.split_manifest_sha256 is not a SHA-256"))
        if not state.get("reporting_stack"):
            findings.append(Finding("ERROR", "REPORTING_STACK", "reporting_stack is empty"))

    values = read_csv(record_dir / "reported_values.csv", findings)
    claims = read_csv(record_dir / "claim_register.csv", findings)
    displays = read_csv(record_dir / "display_register.csv", findings)
    artifacts = read_csv(record_dir / "artifact_manifest.csv", findings)
    decisions = read_csv(record_dir / "decision_log.csv", findings)

    claim_headers = read_csv_headers(record_dir / "claim_register.csv")
    artifact_headers = read_csv_headers(record_dir / "artifact_manifest.csv")
    missing_claim_headers = sorted(CLAIM_HANDOFF_HEADERS - claim_headers)
    missing_artifact_headers = sorted(ARTIFACT_MANIFEST_HEADERS - artifact_headers)
    if missing_claim_headers:
        findings.append(Finding(
            "ERROR" if mode == "submission" else "WARNING", "CLAIM_SCHEMA_LEGACY",
            "claim_register.csv lacks scientific handoff fields: " + ", ".join(missing_claim_headers),
        ))
    if missing_artifact_headers:
        findings.append(Finding(
            "ERROR" if mode == "submission" else "WARNING", "ARTIFACT_SCHEMA_LEGACY",
            "artifact_manifest.csv lacks identity fields: " + ", ".join(missing_artifact_headers),
        ))

    if mode == "submission":
        if not values:
            findings.append(Finding("ERROR", "VALUES_EMPTY", "No canonical reported values recorded"))
        if not claims:
            findings.append(Finding("ERROR", "CLAIMS_EMPTY", "No claims recorded"))
        if not displays:
            findings.append(Finding("ERROR", "DISPLAYS_EMPTY", "No figure/table/display records recorded"))

    value_ids = require_unique(values, "value_id", "reported_values.csv", findings)
    claim_ids = require_unique(claims, "claim_id", "claim_register.csv", findings)
    require_unique(displays, "item_id", "display_register.csv", findings)
    require_unique(artifacts, "artifact_id", "artifact_manifest.csv", findings)
    require_unique(decisions, "decision_id", "decision_log.csv", findings)
    claim_registry = {
        (row.get("claim_id") or "").strip(): row
        for row in claims if (row.get("claim_id") or "").strip()
    }
    artifact_registry = {
        (row.get("artifact_id") or "").strip(): row
        for row in artifacts if (row.get("artifact_id") or "").strip()
    }

    for index, row in enumerate(values, start=2):
        status = (row.get("verified_status") or "").strip()
        if status not in ALLOWED_VALUE_STATUS:
            findings.append(Finding("ERROR", "VALUE_STATUS", f"reported_values.csv:{index} invalid status {status!r}"))
        if mode == "submission" and status != "verified":
            findings.append(Finding("ERROR", "VALUE_UNVERIFIED", f"reported_values.csv:{index} is {status or 'blank'}"))
        if not (row.get("source_artifact") or "").strip():
            findings.append(Finding("WARNING", "VALUE_SOURCE", f"reported_values.csv:{index} has no source_artifact"))

    for index, row in enumerate(claims, start=2):
        status = (row.get("status") or "").strip()
        if status not in ALLOWED_CLAIM_STATUS:
            findings.append(Finding("ERROR", "CLAIM_STATUS", f"claim_register.csv:{index} invalid status {status!r}"))
        referenced_values = split_ids(row.get("value_keys") or "")
        missing = sorted(set(referenced_values) - value_ids)
        if missing:
            findings.append(Finding("ERROR", "CLAIM_VALUE_REF", f"claim_register.csv:{index} unknown value IDs: {', '.join(missing)}"))
        if mode == "submission" and bool_value(row.get("submission_eligible") or ""):
            if status != "supported":
                findings.append(Finding("ERROR", "CLAIM_UNSUPPORTED", f"claim_register.csv:{index} submission claim is {status}"))
            if not (row.get("evidence_artifacts") or "").strip() and not (row.get("citation_ids") or "").strip():
                findings.append(Finding("ERROR", "CLAIM_EVIDENCE", f"claim_register.csv:{index} has no evidence or citation"))
            if not missing_claim_headers:
                evidence_state = (row.get("primary_evidence_state") or "").strip()
                claim_link = (row.get("claim_link_status") or "").strip()
                claim_branch = (row.get("claim_branch") or "").strip()
                branch_verdict = (row.get("branch_verdict") or "").strip()
                if evidence_state not in ALLOWED_EVIDENCE_STATES:
                    findings.append(Finding("ERROR", "CLAIM_EVIDENCE_STATE", f"claim_register.csv:{index} invalid primary_evidence_state {evidence_state!r}"))
                if claim_link not in ALLOWED_CLAIM_LINK_STATUS:
                    findings.append(Finding("ERROR", "CLAIM_LINK_STATUS", f"claim_register.csv:{index} invalid claim_link_status {claim_link!r}"))
                if claim_branch not in ALLOWED_CLAIM_BRANCHES:
                    findings.append(Finding("ERROR", "CLAIM_BRANCH", f"claim_register.csv:{index} invalid claim_branch {claim_branch!r}"))
                if branch_verdict not in ALLOWED_BRANCH_VERDICTS:
                    findings.append(Finding("ERROR", "CLAIM_BRANCH_VERDICT", f"claim_register.csv:{index} invalid branch_verdict {branch_verdict!r}"))
                elif branch_verdict == "STOP":
                    findings.append(Finding("ERROR", "CLAIM_STOP", f"claim_register.csv:{index} is submission eligible but its branch verdict is STOP"))
                elif branch_verdict == "CONDITIONAL":
                    findings.append(Finding("WARNING", "CLAIM_CONDITIONAL", f"claim_register.csv:{index} retains a CONDITIONAL claim ceiling"))
                for field in (
                    "modality_subtype", "independent_unit", "effect_uncertainty",
                    "maximum_wording", "residual_boundary", "protected_placement",
                ):
                    if not (row.get(field) or "").strip():
                        findings.append(Finding("ERROR", "CLAIM_HANDOFF_FIELD", f"claim_register.csv:{index} missing {field}"))
                matched_n = (row.get("matched_n") or "").strip()
                if matched_n != "not-applicable" and (not matched_n.isdigit() or int(matched_n) < 1):
                    findings.append(Finding("ERROR", "CLAIM_MATCHED_N", f"claim_register.csv:{index} matched_n must be a positive integer or not-applicable"))
        if mode == "submission" and PLACEHOLDER_RE.search(" ".join(str(value or "") for value in row.values())):
            findings.append(Finding("ERROR", "CLAIM_PLACEHOLDER", f"claim_register.csv:{index} contains unresolved placeholder"))
    if mode == "submission" and claims and not any(bool_value(row.get("submission_eligible") or "") for row in claims):
        findings.append(Finding("ERROR", "CLAIM_ELIGIBILITY", "No claim is marked submission_eligible=true"))

    for index, row in enumerate(displays, start=2):
        missing_claims = sorted(set(split_ids(row.get("claim_ids") or "")) - claim_ids)
        missing_values = sorted(set(split_ids(row.get("value_keys") or "")) - value_ids)
        if missing_claims:
            findings.append(Finding("ERROR", "DISPLAY_CLAIM_REF", f"display_register.csv:{index} unknown claim IDs: {', '.join(missing_claims)}"))
        if missing_values:
            findings.append(Finding("ERROR", "DISPLAY_VALUE_REF", f"display_register.csv:{index} unknown value IDs: {', '.join(missing_values)}"))
        if not (row.get("source_data") or "").strip():
            findings.append(Finding("ERROR" if mode == "submission" else "WARNING", "DISPLAY_SOURCE", f"display_register.csv:{index} has no source_data"))
        if mode == "submission" and (row.get("qa_status") or "").strip().lower() != "pass":
            findings.append(Finding("ERROR", "DISPLAY_QA", f"display_register.csv:{index} QA is not pass"))

    project_root = record_dir.parent
    for index, row in enumerate(artifacts, start=2):
        status = (row.get("status") or "").strip()
        if status not in ALLOWED_ARTIFACT_STATUS:
            findings.append(Finding("ERROR", "ARTIFACT_STATUS", f"artifact_manifest.csv:{index} invalid status {status!r}"))
        required_for_submission = bool_value(row.get("required_for_submission") or "")
        relative = (row.get("path") or "").strip()
        artifact_path: Path | None = None
        if relative:
            relative_path = Path(relative)
            if relative_path.is_absolute() or ".." in relative_path.parts:
                findings.append(Finding("ERROR", "ARTIFACT_PATH_ESCAPE", f"artifact_manifest.csv:{index} has non-contained path: {relative}"))
            else:
                candidate = (project_root / relative_path).resolve(strict=False)
                try:
                    candidate.relative_to(project_root.resolve())
                    artifact_path = candidate
                except ValueError:
                    findings.append(Finding("ERROR", "ARTIFACT_PATH_ESCAPE", f"artifact_manifest.csv:{index} escapes project root: {relative}"))
        if mode == "submission" and required_for_submission:
            if artifact_path is None or not artifact_path.exists():
                findings.append(Finding("ERROR", "ARTIFACT_PATH", f"artifact_manifest.csv:{index} required path missing: {relative or '[blank]'}"))
            if status != "current":
                findings.append(Finding("ERROR", "ARTIFACT_STALE", f"artifact_manifest.csv:{index} required artifact is {status}"))
        if artifact_path is not None and artifact_path.is_file() and not missing_artifact_headers:
            self_manifest = artifact_path.resolve() == (record_dir / "artifact_manifest.csv").resolve()
            declared_hash = (row.get("sha256") or "").strip()
            if self_manifest:
                if declared_hash:
                    findings.append(Finding("WARNING", "ARTIFACT_SELF_HASH", "artifact_manifest.csv self hash is ignored; use record_fingerprint"))
            elif not declared_hash:
                findings.append(Finding(
                    "ERROR" if mode == "submission" and required_for_submission else "WARNING",
                    "ARTIFACT_HASH_MISSING", f"artifact_manifest.csv:{index} has no SHA-256",
                ))
            elif not SHA_RE.fullmatch(declared_hash):
                findings.append(Finding("ERROR", "ARTIFACT_HASH_FORMAT", f"artifact_manifest.csv:{index} has invalid SHA-256"))
            else:
                try:
                    observed_hash = sha256_file(artifact_path)
                except OSError as exc:
                    findings.append(Finding("ERROR", "ARTIFACT_HASH_READ", f"artifact_manifest.csv:{index} cannot be hashed: {exc}"))
                else:
                    if observed_hash != declared_hash:
                        findings.append(Finding("ERROR", "ARTIFACT_HASH_MISMATCH", f"artifact_manifest.csv:{index} SHA-256 does not match {relative}"))
            if (row.get("source_inputs") or "").strip() and not (
                (row.get("source_input_sha256s") or "").strip()
                or (row.get("source_manifest_digest") or "").strip()
            ):
                findings.append(Finding(
                    "ERROR" if mode == "submission" else "WARNING", "ARTIFACT_LINEAGE_DIGEST",
                    f"artifact_manifest.csv:{index} has source inputs without source hashes/manifest digest",
                ))

    if not legacy_schema:
        handoff = state.get("scientific_handoff") or {}
        if not isinstance(handoff, dict):
            findings.append(Finding("ERROR", "HANDOFF_SHAPE", "scientific_handoff must be an object"))
            handoff = {}
        handoff_status = str(handoff.get("status") or "")
        if handoff_status not in ALLOWED_HANDOFF_STATUS:
            findings.append(Finding("ERROR", "HANDOFF_STATUS", f"Invalid scientific_handoff.status: {handoff_status!r}"))
        handoff_required = mode == "submission" and study_scope in {"mechanism-only", "imaging-mechanism"}
        if handoff_required and handoff_status != "validated":
            findings.append(Finding("ERROR", "HANDOFF_NOT_VALIDATED", "scientific_handoff.status must be validated"))
        if handoff_status == "validated" or handoff_required:
            packet_relative = str(handoff.get("packet_path") or "").strip()
            packet_path: Path | None = None
            if packet_relative:
                candidate = (project_root / packet_relative).resolve(strict=False)
                try:
                    candidate.relative_to(project_root.resolve())
                    packet_path = candidate
                except ValueError:
                    findings.append(Finding("ERROR", "HANDOFF_PATH_ESCAPE", "scientific_handoff.packet_path escapes project root"))
            packet_payload: dict[str, object] = {}
            semantic_report: dict[str, object] = {}
            if packet_path is None or not packet_path.is_file():
                findings.append(Finding("ERROR", "HANDOFF_PATH", "Validated scientific handoff packet is missing"))
            else:
                file_digest_field = "packet_file_sha256" if state_schema in SPLIT_HANDOFF_DIGEST_SCHEMAS else "packet_sha256"
                declared_file_hash = str(handoff.get(file_digest_field) or "").strip()
                if not SHA_RE.fullmatch(declared_file_hash):
                    findings.append(Finding("ERROR", "HANDOFF_FILE_DIGEST", f"scientific_handoff.{file_digest_field} is invalid"))
                elif sha256_file(packet_path) != declared_file_hash:
                    findings.append(Finding("ERROR", "HANDOFF_FILE_DIGEST", "scientific handoff packet file SHA-256 does not match"))
                try:
                    semantic_report, packet_payload = run_scientific_handoff_validator(packet_path)
                except (OSError, ValueError, json.JSONDecodeError) as exc:
                    findings.append(Finding("ERROR", "HANDOFF_SEMANTIC_VALIDATOR", str(exc)))
                else:
                    if semantic_report.get("status") != "PASS":
                        for error in semantic_report.get("errors", []):
                            findings.append(Finding("ERROR", "HANDOFF_SEMANTIC", str(error)))
                    computed_canonical = str(semantic_report.get("computed_packet_sha256") or "")
                    if state_schema in SPLIT_HANDOFF_DIGEST_SCHEMAS:
                        declared_canonical = str(handoff.get("canonical_packet_sha256") or "").strip()
                        if not SHA_RE.fullmatch(declared_canonical):
                            findings.append(Finding("ERROR", "HANDOFF_CANONICAL_DIGEST", "scientific_handoff.canonical_packet_sha256 is invalid"))
                        elif computed_canonical and declared_canonical != computed_canonical:
                            findings.append(Finding("ERROR", "HANDOFF_CANONICAL_DIGEST", "project record canonical packet digest does not match packet semantics"))
                        if packet_payload.get("packet_sha256") != declared_canonical:
                            findings.append(Finding("ERROR", "HANDOFF_CANONICAL_DIGEST", "packet-declared canonical digest differs from project record"))
            for key in ("source_manifest_digest", "claim_register_sha256"):
                if not SHA_RE.fullmatch(str(handoff.get(key) or "").strip()):
                    findings.append(Finding("ERROR", "HANDOFF_DIGEST", f"scientific_handoff.{key} is invalid"))
            claim_register_path = record_dir / "claim_register.csv"
            if claim_register_path.is_file() and SHA_RE.fullmatch(str(handoff.get("claim_register_sha256") or "").strip()):
                if sha256_file(claim_register_path) != str(handoff.get("claim_register_sha256")):
                    findings.append(Finding("ERROR", "HANDOFF_CLAIM_DRIFT", "claim_register.csv changed after scientific handoff validation"))
            if packet_payload:
                if str(packet_payload.get("study_id") or "") != str(state.get("study_id") or ""):
                    findings.append(Finding("ERROR", "HANDOFF_STUDY_DRIFT", "packet study_id differs from project state"))
                if str(packet_payload.get("study_scope") or "") != study_scope:
                    findings.append(Finding("ERROR", "HANDOFF_SCOPE_DRIFT", "packet study_scope differs from project state"))
                packet_roles = packet_payload.get("modality_roles") or {}
                role_field_map = {
                    "active": "active_modalities",
                    "external_reference": "external_reference_modalities",
                    "generated_or_predicted": "generated_or_predicted_modalities",
                    "proposed_validation": "proposed_validation_modalities",
                }
                if isinstance(packet_roles, dict):
                    for packet_role, project_field in role_field_map.items():
                        if set(packet_roles.get(packet_role) or []) != set((research_scope or {}).get(project_field) or []):
                            findings.append(Finding("ERROR", "HANDOFF_ROLE_DRIFT", f"packet modality role {packet_role} differs from project state"))
                if packet_payload.get("evidence_topology") != evidence_topology:
                    findings.append(Finding("ERROR", "HANDOFF_TOPOLOGY_DRIFT", "packet evidence_topology differs from project state"))
                packet_manifest = str(packet_payload.get("source_manifest_digest") or "")
                project_manifest = str(handoff.get("source_manifest_digest") or "")
                analysis_manifest = str(analysis_lock_object.get("source_manifest_sha256") or "")
                if packet_manifest != project_manifest or packet_manifest != analysis_manifest:
                    findings.append(Finding("ERROR", "HANDOFF_SOURCE_DRIFT", "packet, project handoff and analysis lock source-manifest digests differ"))
                packet_claim_digest = str(packet_payload.get("claim_register_sha256") or "")
                if packet_claim_digest != str(handoff.get("claim_register_sha256") or ""):
                    findings.append(Finding("ERROR", "HANDOFF_CLAIM_DRIFT", "packet and project handoff claim-register digests differ"))
                packet_analysis_digest = str(packet_payload.get("analysis_lock_digest") or "")
                if packet_analysis_digest != str(state.get("analysis_lock_digest") or ""):
                    findings.append(Finding("ERROR", "HANDOFF_ANALYSIS_DRIFT", "packet analysis-lock digest differs from project state"))
                packet_artifacts = packet_payload.get("source_artifacts") or []
                if isinstance(packet_artifacts, list):
                    for packet_artifact in packet_artifacts:
                        if not isinstance(packet_artifact, dict):
                            continue
                        artifact_id = str(packet_artifact.get("artifact_id") or "")
                        registry_row = artifact_registry.get(artifact_id)
                        if registry_row is None:
                            findings.append(Finding(
                                "ERROR", "HANDOFF_ARTIFACT_REF",
                                f"packet source artifact {artifact_id!r} is absent from artifact_manifest.csv",
                            ))
                        elif str(packet_artifact.get("sha256") or "") != str(registry_row.get("sha256") or ""):
                            findings.append(Finding(
                                "ERROR", "HANDOFF_ARTIFACT_DRIFT",
                                f"packet source artifact {artifact_id!r} digest differs from artifact_manifest.csv",
                            ))
                packet_claims = packet_payload.get("claims") or []
                if isinstance(packet_claims, list):
                    for packet_claim in packet_claims:
                        if not isinstance(packet_claim, dict):
                            continue
                        packet_claim_id = str(packet_claim.get("claim_id") or "")
                        registry_claim = claim_registry.get(packet_claim_id)
                        if registry_claim is None:
                            findings.append(Finding(
                                "ERROR", "HANDOFF_CLAIM_REF",
                                f"packet claim {packet_claim_id!r} is absent from claim_register.csv",
                            ))
                            continue
                        for field in (
                            "claim_text", "primary_evidence_state", "modality_subtype",
                            "claim_link_status", "independent_unit", "effect_uncertainty",
                            "claim_branch", "branch_verdict", "maximum_wording", "residual_boundary",
                        ):
                            if str(packet_claim.get(field) or "") != str(registry_claim.get(field) or ""):
                                findings.append(Finding(
                                    "ERROR", "HANDOFF_CLAIM_FIELD_DRIFT",
                                    f"packet claim {packet_claim_id!r} field {field} differs from claim_register.csv",
                                ))
                        packet_matched_n = (
                            "not-applicable" if packet_claim.get("matched_n") is None
                            else str(packet_claim.get("matched_n"))
                        )
                        if packet_matched_n != str(registry_claim.get("matched_n") or ""):
                            findings.append(Finding(
                                "ERROR", "HANDOFF_CLAIM_FIELD_DRIFT",
                                f"packet claim {packet_claim_id!r} field matched_n differs from claim_register.csv",
                            ))
                        packet_placements = set(packet_claim.get("protected_placement") or [])
                        registry_placements = set(split_ids(registry_claim.get("protected_placement") or ""))
                        if packet_placements != registry_placements:
                            findings.append(Finding(
                                "ERROR", "HANDOFF_CLAIM_FIELD_DRIFT",
                                f"packet claim {packet_claim_id!r} protected placement differs from claim_register.csv",
                            ))
                        pointer_artifact_ids = {
                            str(pointer).split(":", 1)[0]
                            for pointer in packet_claim.get("evidence_pointers") or []
                            if isinstance(pointer, str) and ":" in pointer
                        }
                        registry_evidence_ids = set(split_ids(registry_claim.get("evidence_artifacts") or ""))
                        if not pointer_artifact_ids.issubset(registry_evidence_ids):
                            findings.append(Finding(
                                "ERROR", "HANDOFF_CLAIM_ARTIFACT_DRIFT",
                                f"packet claim {packet_claim_id!r} points outside its claim-register evidence artifacts",
                            ))

    return summarize(record_dir, mode, findings)


def summarize(record_dir: Path, mode: str, findings: list[Finding]) -> dict[str, object]:
    error_count = sum(item.severity == "ERROR" for item in findings)
    warning_count = sum(item.severity == "WARNING" for item in findings)
    fingerprint: dict[str, str | None] = {}
    for name in REQUIRED_FILES:
        path = record_dir / name
        try:
            fingerprint[name] = sha256_file(path) if path.is_file() else None
        except OSError:
            fingerprint[name] = None
    return {
        "record_dir": str(record_dir),
        "mode": mode,
        "status": "PASS" if error_count == 0 else "FAIL",
        "errors": error_count,
        "warnings": warning_count,
        "record_fingerprint": fingerprint,
        "findings": [asdict(item) for item in findings],
    }


def main() -> int:
    args = parse_args()
    report = validate(Path(args.project_dir).expanduser().resolve(), args.mode)
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    print(rendered)
    if args.json_output:
        Path(args.json_output).write_text(rendered + "\n", encoding="utf-8")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
