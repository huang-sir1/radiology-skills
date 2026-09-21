#!/usr/bin/env python3
"""Validate route coverage, evidence authority, templates, and regression tests."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


SKILL_ROOT = Path(__file__).resolve().parents[1]
ROUTER = SKILL_ROOT / "references" / "journal-router.md"
EVIDENCE = SKILL_ROOT / "references" / "journal-requirements-evidence.tsv"
ROUTING_CASES = SKILL_ROOT / "tests" / "submission-routing-cases.json"
MANIFEST_TEMPLATE = SKILL_ROOT / "assets" / "submission-manifest.template.csv"
PROFILE_DIR = SKILL_ROOT / "references" / "journals"
REQUIRED_MATERIALS = SKILL_ROOT / "references" / "journal-required-materials.json"
TEST_SCRIPT = Path(__file__).with_name("test_audit_submission_package.py")
GOLDEN_TEST_SCRIPT = Path(__file__).with_name("test_submission_golden_scenarios.py")
INTAKE_RESOLVER = Path(__file__).with_name("resolve_submission_intake.py")
REPORT_RENDERER = Path(__file__).with_name("render_submission_audit_report.py")
SECURITY_HELPER = Path(__file__).with_name("submission_security.py")
STRUCTURAL_AUDITOR = Path(__file__).with_name("audit_submission_package.py")
VALIDATION_WRAPPER = Path(__file__).with_name("validate_submission_skill.ps1")
VALIDATION_RECEIPT = SKILL_ROOT / "references" / "validation-receipt-2026-08-22.md"
INTAKE_TEMPLATE = SKILL_ROOT / "assets" / "submission-intake.template.json"
EVIDENCE_SYNTHESIS_INTAKE_TEMPLATE = (
    SKILL_ROOT / "assets" / "submission-intake.evidence-synthesis.template.json"
)
TRANSFER_TEMPLATE = SKILL_ROOT / "assets" / "submission-transfer-context.template.json"
AUDIT_REPORT_TEMPLATE = SKILL_ROOT / "assets" / "submission-audit-report.template.md"
CONTRIBUTOR_DISCLOSURE_HANDOFF_TEMPLATE = (
    SKILL_ROOT / "assets" / "contributor-disclosure-handoff.template.csv"
)
CONFERENCE_INTAKE_TEMPLATE = SKILL_ROOT / "assets" / "conference-portal-intake.template.json"
CONFERENCE_MANIFEST_TEMPLATE = SKILL_ROOT / "assets" / "conference-portal-manifest.template.csv"
CONFERENCE_ROUTE_REFERENCE = SKILL_ROOT / "references" / "conference-portal-finalization.md"
CONFERENCE_PACKAGE_VALIDATOR = Path(__file__).with_name("validate_conference_portal_package.py")
AUTHORSHIP_AI_PUBLIC_ACCESS_REFERENCE = (
    SKILL_ROOT / "references" / "authorship-ai-and-public-access-handoff.md"
)
HARD_REQUIREMENTS = {"required", "conditional", "portal-only"}
CONTRACT_CLASSIFIABLE_REQUIREMENTS = HARD_REQUIREMENTS | {"optional"}
NONAUTHORITATIVE = {"PUBLISHED_EXEMPLAR", "SECONDARY_SUMMARY", "PORTAL_PLACEHOLDER"}
EXPECTED_EVIDENCE_HEADERS = [
    "journal_id", "rule_id", "article_type", "stage", "authority_class",
    "requirement_class", "condition", "material", "rule_summary", "allowed_extensions",
    "source_url", "checked_on", "verification_status", "applicable_stages",
]
EXPECTED_MANIFEST_HEADERS = [
    "schema_version", "project_id", "study_scope", "project_state_digest",
    "modality_role_digest", "scientific_handoff_packet_digest",
    "scientific_prereview_receipt_digest", "source_artifact_id", "analysis_lock_digest",
    "claim_registry_digest", "response_package_digest", "item_id", "journal_id",
    "article_type", "submission_stage",
    "study_design", "review_model", "material", "requirement_class", "condition", "rule_id", "authority_class",
    "source_url", "guide_verified_on", "path", "expected_extensions", "version",
    "sha256", "blinded", "tracked_changes_policy", "revision_variant", "status", "technical_qa", "render_qa", "content_gate",
    "anonymization_qa", "crossfile_qa", "owner", "not_applicable_reason", "notes",
]
EXPECTED_INTAKE_FIELDS = [
    "schema_version", "target_journal_id", "article_type", "submission_stage",
    "publisher_stage_label", "package_root", "review_scope", "study_design",
    "review_model", "manuscript_version", "project_id", "study_scope",
    "project_state_digest", "modality_role_digest",
    "scientific_handoff_packet_digest", "scientific_prereview_receipt_digest",
    "source_artifact_id", "analysis_lock_digest", "claim_registry_digest",
    "response_package_digest", "guide_checked_on", "transfer_context",
]
EXPECTED_TRANSFER_FIELDS = {
    "source_journal_id", "target_journal_id", "target_article_type",
    "transfer_offer_receipt_sha256", "transfer_offer_checked_on", "transfer_mode",
    "source_inventory_sha256", "target_portal_inventory_sha256",
    "target_initial_route_id",
}
EXPECTED_CONFERENCE_INTAKE_FIELDS = [
    "schema_version", "route_kind", "venue_name", "venue_series_id",
    "submission_cycle", "submission_type", "current_call_url", "portal_url",
    "call_status", "call_checked_on", "portal_checked_on", "submission_deadline",
    "call_capture_sha256", "call_capture_locator", "portal_capture_sha256",
    "portal_capture_locator", "call_bound_venue_series_id",
    "call_bound_submission_cycle", "call_bound_submission_type",
    "portal_bound_venue_series_id", "portal_bound_submission_cycle",
    "portal_bound_submission_type", "project_id", "abstract_artifact_id",
    "abstract_sha256", "dissemination_handoff_sha256", "claim_registry_digest",
    "analysis_lock_digest", "content_owner", "portal_owner", "embargo_gate",
    "disclosure_gate", "privacy_gate", "rights_gate", "author_approval_gate",
    "package_root", "review_scope", "human_final_action_owner",
    "human_final_action_status",
]
EXPECTED_CONFERENCE_MANIFEST_HEADERS = [
    "schema_version", "venue_series_id", "submission_cycle", "submission_type",
    "item_id", "item_kind", "material", "portal_designation",
    "requirement_class", "condition", "authority_class", "source_url",
    "verified_on", "allowed_extensions", "max_bytes", "version", "source_artifact_id",
    "source_artifact_sha256", "path", "upload_sha256", "value_status", "technical_qa", "render_qa",
    "content_gate", "claim_boundary", "embargo_gate", "disclosure_gate",
    "privacy_gate", "rights_gate", "human_owner", "notes",
]
CONTRACT_STAGES = {"initial", "pre-review", "revision", "transfer", "final-files"}
EVIDENCE_STAGES = CONTRACT_STAGES | {"published"}
ITEM_KINDS = {"file", "portal", "file-or-portal", "field", "embedded"}
REVISION_VARIANTS = {"clean", "marked", "response", "cover", "other-revision"}
OFFICIAL_HOSTS = {
    "radiology": {"pubs.rsna.org", "mc.manuscriptcentral.com"},
    "nature-medicine": {"www.nature.com", "mts-nmed.nature.com"},
    "nature-communications": {"www.nature.com", "mts-ncomms.nature.com"},
    "lancet-digital-health": {"www.thelancet.com", "www.editorialmanager.com", "www.sciencedirect.com"},
    "eclinicalmedicine": {"www.thelancet.com", "www.editorialmanager.com", "www.sciencedirect.com"},
    "cancer-cell": {"www.cell.com", "www.sciencedirect.com"},
    "cell-reports-medicine": {"www.cell.com", "www.sciencedirect.com"},
    "npj-digital-medicine": {"www.nature.com", "submission.springernature.com"},
    "npj-precision-oncology": {"www.nature.com", "submission.springernature.com"},
    "advanced-science": {
        "advanced.onlinelibrary.wiley.com", "onlinelibrary.wiley.com",
        "authorservices.wiley.com", "authors.wiley.com", "www.editorialmanager.com",
    },
    "jama-network-open": {"jamanetwork.com", "manuscripts.jamanetworkopen.com"},
}
PORTAL_ROUTE_ALLOWLIST = {
    "radiology": {("mc.manuscriptcentral.com", "/rad")},
    "nature-medicine": {("mts-nmed.nature.com", "/")},
    "nature-communications": {("mts-ncomms.nature.com", "/")},
    "lancet-digital-health": set(),
    "eclinicalmedicine": set(),
    "cancer-cell": set(),
    "cell-reports-medicine": set(),
    "npj-digital-medicine": {("submission.springernature.com", "/new-submission/41746")},
    "npj-precision-oncology": {("submission.springernature.com", "/new-submission/41698")},
    # The public Advanced Science Editorial Manager page is explicitly a development
    # site at this snapshot, so no route is allowed to resolve a live requirement.
    "advanced-science": set(),
    "jama-network-open": {("manuscripts.jamanetworkopen.com", "/")},
}
EXPECTED_INITIAL_MODE = {
    "radiology": "double-anonymized",
    "nature-medicine": "optional-double-anonymized",
    "nature-communications": "optional-double-anonymized",
    "lancet-digital-health": "single-anonymized",
    "eclinicalmedicine": "single-anonymized",
    "cancer-cell": "single-anonymized",
    "cell-reports-medicine": "single-anonymized",
    "npj-digital-medicine": "single-anonymized",
    "npj-precision-oncology": "single-anonymized",
    "advanced-science": "not-confirmed",
    "jama-network-open": "single-anonymized",
}
EXPECTED_STAGE_ROUTE_COUNTS = {
    "initial": 11,
    "pre-review": 4,
    "revision": 11,
    "transfer": 0,
    "final-files": 6,
}

RECEIPT_ARTIFACTS = {
    "journal_evidence_registry": EVIDENCE,
    "route_contract_registry": REQUIRED_MATERIALS,
    "routing_cases": ROUTING_CASES,
    "manifest_template": MANIFEST_TEMPLATE,
    "intake_template": INTAKE_TEMPLATE,
    "evidence_synthesis_intake_template": EVIDENCE_SYNTHESIS_INTAKE_TEMPLATE,
    "transfer_template": TRANSFER_TEMPLATE,
    "audit_report_template": AUDIT_REPORT_TEMPLATE,
    "contributor_disclosure_handoff_template": CONTRIBUTOR_DISCLOSURE_HANDOFF_TEMPLATE,
    "conference_portal_intake_template": CONFERENCE_INTAKE_TEMPLATE,
    "conference_portal_manifest_template": CONFERENCE_MANIFEST_TEMPLATE,
    "conference_portal_route_reference": CONFERENCE_ROUTE_REFERENCE,
    "conference_portal_package_validator": CONFERENCE_PACKAGE_VALIDATOR,
    "authorship_ai_public_access_reference": AUTHORSHIP_AI_PUBLIC_ACCESS_REFERENCE,
    "structural_auditor": STRUCTURAL_AUDITOR,
    "regression_suite": TEST_SCRIPT,
    "golden_suite": GOLDEN_TEST_SCRIPT,
    "intake_resolver": INTAKE_RESOLVER,
    "report_renderer": REPORT_RENDERER,
    "security_helper": SECURITY_HELPER,
    "skill_entrypoint": SKILL_ROOT / "SKILL.md",
    "validator": Path(__file__).resolve(),
    "validation_wrapper": VALIDATION_WRAPPER,
}
RECEIPT_COUNT_KEYS = {
    "routes",
    "profiles",
    "evidence_rows",
    "route_contracts",
    "negative_contracts",
    "regression_cases",
    "golden_scenarios",
}
RECEIPT_HUMAN_COUNT_LABELS = {
    "routes": "Canonical journal routes",
    "profiles": "Journal profiles",
    "evidence_rows": "Journal evidence rows",
    "route_contracts": "Route contracts",
    "negative_contracts": "Negative-contract fixtures",
    "regression_cases": "Structural regression cases",
    "golden_scenarios": "Cross-step golden scenarios",
}
RECEIPT_BLOCK_RE = re.compile(
    r"<!-- BEGIN MACHINE-VERIFIABLE RECEIPT -->\s*"
    r"```json\s*(\{.*?\})\s*```\s*"
    r"<!-- END MACHINE-VERIFIABLE RECEIPT -->",
    re.DOTALL,
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def _strict_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    seen: set[str] = set()
    for key, value in pairs:
        folded = key.casefold()
        if folded in seen:
            raise ValueError(f"duplicate JSON object key: {key}")
        seen.add(folded)
        result[key] = value
    return result


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def validate_frozen_receipt(errors: list[str], expected_counts: dict[str, int]) -> None:
    """Fail closed when the published validation receipt no longer matches executable inputs."""
    if not VALIDATION_RECEIPT.is_file():
        fail(errors, f"Missing validation receipt: {VALIDATION_RECEIPT}")
        return
    receipt_text = VALIDATION_RECEIPT.read_text(encoding="utf-8")
    matches = RECEIPT_BLOCK_RE.findall(receipt_text)
    if len(matches) != 1:
        fail(errors, "Validation receipt must contain exactly one machine-verifiable JSON block")
        return
    try:
        payload = json.loads(matches[0], object_pairs_hook=_strict_json_object)
    except (json.JSONDecodeError, ValueError) as exc:
        fail(errors, f"Cannot parse machine-verifiable validation receipt: {exc}")
        return
    if not isinstance(payload, dict):
        fail(errors, "Machine-verifiable validation receipt must be a JSON object")
        return
    expected_top_keys = {"schema_version", "validation_date", "counts", "artifacts"}
    if set(payload) != expected_top_keys:
        fail(errors, f"Validation receipt top-level keys mismatch: {sorted(set(payload) ^ expected_top_keys)}")
    if payload.get("schema_version") != "1.0":
        fail(errors, "Validation receipt schema_version must be 1.0")
    validation_date = str(payload.get("validation_date") or "")
    try:
        datetime.strptime(validation_date, "%Y-%m-%d")
    except ValueError:
        fail(errors, "Validation receipt validation_date must use YYYY-MM-DD")
    if f"Validation date: {validation_date}" not in receipt_text:
        fail(errors, "Validation receipt human-readable date does not match the machine block")
    if "Status: **PASS**" not in receipt_text:
        fail(errors, "Validation receipt human-readable status is not PASS")

    counts = payload.get("counts")
    if not isinstance(counts, dict) or set(counts) != RECEIPT_COUNT_KEYS:
        observed_keys = set(counts) if isinstance(counts, dict) else set()
        fail(errors, f"Validation receipt count keys mismatch: {sorted(observed_keys ^ RECEIPT_COUNT_KEYS)}")
    else:
        for key in sorted(RECEIPT_COUNT_KEYS):
            value = counts.get(key)
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                fail(errors, f"Validation receipt count is not a non-negative integer: {key}")
            elif value != expected_counts[key]:
                fail(
                    errors,
                    f"Validation receipt count drift for {key}: frozen={value}, current={expected_counts[key]}",
                )
        for key, label in RECEIPT_HUMAN_COUNT_LABELS.items():
            expected_row = f"| {label} | {expected_counts[key]} |"
            if expected_row not in receipt_text:
                fail(errors, f"Validation receipt human-readable count row is stale or missing: {label}")

    artifacts = payload.get("artifacts")
    expected_artifact_keys = set(RECEIPT_ARTIFACTS)
    if not isinstance(artifacts, dict) or set(artifacts) != expected_artifact_keys:
        observed_keys = set(artifacts) if isinstance(artifacts, dict) else set()
        fail(errors, f"Validation receipt artifact keys mismatch: {sorted(observed_keys ^ expected_artifact_keys)}")
        return
    for name, path in RECEIPT_ARTIFACTS.items():
        entry = artifacts.get(name)
        if not isinstance(entry, dict) or set(entry) != {"path", "bytes", "sha256"}:
            fail(errors, f"Validation receipt artifact entry is malformed: {name}")
            continue
        if not path.is_file():
            fail(errors, f"Frozen validation artifact is missing: {name}")
            continue
        expected_path = path.resolve().relative_to(SKILL_ROOT.resolve()).as_posix()
        if entry.get("path") != expected_path:
            fail(errors, f"Validation receipt path mismatch for {name}")
        byte_count = entry.get("bytes")
        if isinstance(byte_count, bool) or not isinstance(byte_count, int) or byte_count < 0:
            fail(errors, f"Validation receipt byte count is invalid for {name}")
        elif byte_count != path.stat().st_size:
            fail(
                errors,
                f"Validation receipt byte drift for {name}: frozen={byte_count}, current={path.stat().st_size}",
            )
        frozen_hash = str(entry.get("sha256") or "")
        if not re.fullmatch(r"[0-9A-F]{64}", frozen_hash):
            fail(errors, f"Validation receipt SHA-256 is invalid for {name}")
        else:
            current_hash = _sha256(path)
            if frozen_hash != current_hash:
                fail(
                    errors,
                    f"Validation receipt SHA-256 drift for {name}: frozen={frozen_hash}, current={current_hash}",
                )


def portal_route_allowed(journal_id: str, parsed_url) -> bool:
    """Bind shared submission hosts to the exact journal route, not merely the domain."""
    host = parsed_url.netloc.lower()
    raw_path = parsed_url.path
    segments = raw_path.replace("\\", "/").split("/")
    if "\\" in raw_path or "%" in raw_path or any(segment in {".", ".."} for segment in segments):
        return False
    path = "/" + parsed_url.path.strip("/").casefold()
    for allowed_host, allowed_prefix in PORTAL_ROUTE_ALLOWLIST.get(journal_id, set()):
        prefix = "/" + allowed_prefix.strip("/").casefold()
        if host != allowed_host:
            continue
        if prefix == "/" or path == prefix or path.startswith(prefix + "/"):
            return True
    return False


def main() -> int:
    errors: list[str] = []
    route_data = json.loads(ROUTING_CASES.read_text(encoding="utf-8"))
    supported = route_data.get("supported_routes", [])
    conference_route = route_data.get("conference_portal_route")
    negative_contracts = route_data.get("negative_contracts", [])
    expected_conference_route = {
        "route_id": "conference-portal-finalization",
        "request_boundary": (
            "final meeting or congress portal fields, file designations, upload bytes and attestations"
        ),
        "scientific_content_owner": "radiology-dissemination",
        "portal_package_owner": "radiology-submission",
        "required_live_bindings": [
            "venue_series_id", "submission_cycle", "submission_type", "current_call", "live_portal",
        ],
        "progression_state": "HUMAN_PORTAL_ACTION_REQUIRED",
        "blocking_states": [
            "CALL_EVIDENCE_UNVERIFIED", "PORTAL_EVIDENCE_UNVERIFIED", "PORTAL_PACKAGE_BLOCKED",
        ],
        "final_action_owner": "authorized-human",
        "forbidden_machine_claims": [
            "READY", "SUBMITTED", "ACCEPTED", "PUBLISHED", "EMBARGO CLEARED",
        ],
    }
    if conference_route != expected_conference_route:
        fail(errors, "Conference portal route contract is missing or has drifted")
    route_ids = {entry["journal_id"] for entry in supported}
    if len(route_ids) != 11 or len(supported) != 11:
        fail(errors, f"Expected exactly 11 unique journal routes, found {len(route_ids)}")
    if set(OFFICIAL_HOSTS) != route_ids:
        fail(errors, f"Official-host policy route set mismatch: {sorted(set(OFFICIAL_HOSTS) ^ route_ids)}")
    if set(PORTAL_ROUTE_ALLOWLIST) != route_ids:
        fail(errors, f"Portal allowlist route set mismatch: {sorted(set(PORTAL_ROUTE_ALLOWLIST) ^ route_ids)}")
    if set(EXPECTED_INITIAL_MODE) != route_ids:
        fail(errors, f"Review-model policy route set mismatch: {sorted(set(EXPECTED_INITIAL_MODE) ^ route_ids)}")
    router_text = ROUTER.read_text(encoding="utf-8")
    skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
    for entry in supported:
        journal_id = entry["journal_id"]
        if entry.get("initial_model") != EXPECTED_INITIAL_MODE.get(journal_id):
            fail(errors, f"Initial review-model policy mismatch for {journal_id}")
        profile = PROFILE_DIR / entry["profile"]
        if not profile.is_file():
            fail(errors, f"Missing profile for {journal_id}: {profile.name}")
            continue
        if entry["profile"] not in router_text or f"`{journal_id}`" not in router_text:
            fail(errors, f"Router does not link canonical route {journal_id}")
        profile_text = profile.read_text(encoding="utf-8")
        for required_phrase in ("Snapshot checked: 2026-08-22", "Published exemplars", "advisory only"):
            if required_phrase.casefold() not in profile_text.casefold():
                fail(errors, f"Profile {profile.name} lacks phrase: {required_phrase}")
    for required_ref in (
        "journal-router.md", "journal-requirements-evidence.tsv", "all-file-audit-workflow.md",
        "conference-portal-finalization.md", "conference-portal-intake.template.json",
        "conference-portal-manifest.template.csv", "validate_conference_portal_package.py",
    ):
        if required_ref not in skill_text:
            fail(errors, f"SKILL.md does not route to {required_ref}")

    markdown_link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for markdown in SKILL_ROOT.rglob("*.md"):
        for target in markdown_link_re.findall(markdown.read_text(encoding="utf-8")):
            target = target.strip().strip("<>")
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            local_target = target.split("#", 1)[0]
            if local_target and not (markdown.parent / local_target).resolve().exists():
                fail(errors, f"Broken local Markdown link in {markdown.relative_to(SKILL_ROOT)}: {target}")

    with EVIDENCE.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        evidence_rows = list(reader)
        evidence_headers = reader.fieldnames or []
    if len(evidence_headers) != len(set(evidence_headers)):
        duplicate_headers = sorted({name for name in evidence_headers if evidence_headers.count(name) > 1})
        fail(errors, f"Evidence has duplicate headers: {duplicate_headers}")
    if evidence_headers != EXPECTED_EVIDENCE_HEADERS:
        fail(errors, "Evidence headers do not match the required ordered schema")
    evidence_routes = {row["journal_id"] for row in evidence_rows}
    if evidence_routes != route_ids:
        fail(errors, f"Evidence route set mismatch: {sorted(evidence_routes ^ route_ids)}")
    seen_rules: set[str] = set()
    verified_hard_counts = {journal_id: 0 for journal_id in route_ids}
    exemplar_counts = {journal_id: 0 for journal_id in route_ids}
    for line_number, row in enumerate(evidence_rows, start=2):
        journal_id = row["journal_id"]
        rule_id = row["rule_id"]
        if rule_id in seen_rules:
            fail(errors, f"Duplicate rule_id at line {line_number}: {rule_id}")
        seen_rules.add(rule_id)
        url = urlparse(row["source_url"])
        if url.scheme != "https" or not url.netloc:
            fail(errors, f"Non-HTTPS or non-direct URL at line {line_number}: {row['source_url']}")
        elif url.netloc.lower() not in OFFICIAL_HOSTS.get(journal_id, set()):
            fail(errors, f"Non-approved official host at line {line_number}: {url.netloc}")
        if (
            row["authority_class"] == "PORTAL_CURRENT"
            and row["verification_status"] != "UNVERIFIED_CURRENT"
            and not portal_route_allowed(journal_id, url)
        ):
            fail(errors, f"Portal source is not bound to the exact journal route at line {line_number}: {rule_id}")
        try:
            datetime.strptime(row["checked_on"], "%Y-%m-%d")
        except ValueError:
            fail(errors, f"Invalid checked_on at line {line_number}: {row['checked_on']}")
        requirement = row["requirement_class"]
        authority = row["authority_class"]
        verification = row["verification_status"]
        primary_stage = row["stage"].strip()
        applicable_stages = [
            value.strip() for value in (row.get("applicable_stages") or "").split(";") if value.strip()
        ]
        if primary_stage not in EVIDENCE_STAGES:
            fail(errors, f"Invalid evidence stage at line {line_number}: {primary_stage or '[blank]'}")
        if not applicable_stages:
            fail(errors, f"Evidence rule has no applicable_stages at line {line_number}: {rule_id}")
        elif len(applicable_stages) != len(set(applicable_stages)):
            fail(errors, f"Evidence rule repeats applicable_stages at line {line_number}: {rule_id}")
        else:
            invalid_stages = sorted(set(applicable_stages) - EVIDENCE_STAGES)
            if invalid_stages:
                fail(errors, f"Evidence rule has invalid applicable_stages at line {line_number}: {invalid_stages}")
            if primary_stage not in applicable_stages:
                fail(errors, f"Evidence primary stage is absent from applicable_stages at line {line_number}: {rule_id}")
        if verification not in {"VERIFIED_CURRENT", "UNVERIFIED_CURRENT", "OBSERVED_ONLY"}:
            fail(errors, f"Invalid verification_status at line {line_number}: {verification}")
        if requirement in HARD_REQUIREMENTS and authority in NONAUTHORITATIVE:
            fail(errors, f"Non-authoritative hard rule at line {line_number}: {rule_id}")
        if requirement not in {"required", "conditional", "optional", "portal-only", "advisory"}:
            fail(errors, f"Invalid evidence requirement_class at line {line_number}: {requirement}")
        if verification == "VERIFIED_CURRENT" and requirement in HARD_REQUIREMENTS and authority not in NONAUTHORITATIVE:
            verified_hard_counts[journal_id] += 1
        if authority == "PUBLISHED_EXEMPLAR":
            exemplar_counts[journal_id] += 1
            if requirement != "advisory" or verification != "OBSERVED_ONLY":
                fail(errors, f"Exemplar row not advisory-only at line {line_number}: {rule_id}")
        if (
            journal_id == "advanced-science"
            and authority == "PORTAL_CURRENT"
            and row["source_url"].rstrip("/").casefold()
            == "https://www.editorialmanager.com/advancedscience".casefold()
            and verification != "UNVERIFIED_CURRENT"
        ):
            fail(errors, "Advanced Science development portal must remain UNVERIFIED_CURRENT")
    for journal_id in sorted(route_ids):
        if verified_hard_counts[journal_id] == 0:
            fail(errors, f"Route has no verified hard/policy rule: {journal_id}")
        if exemplar_counts[journal_id] == 0:
            fail(errors, f"Route has no advisory exemplar evidence row: {journal_id}")

    route_contract = json.loads(REQUIRED_MATERIALS.read_text(encoding="utf-8"))
    if route_contract.get("schema_version") != "1.0" or not isinstance(route_contract.get("routes"), list):
        fail(errors, "Journal required-material matrix has an invalid schema")
        contract_routes = []
    else:
        contract_routes = route_contract["routes"]
    non_contract_evidence = route_contract.get("non_contract_evidence", [])
    if not isinstance(non_contract_evidence, list):
        fail(errors, "Journal required-material matrix non_contract_evidence must be a list")
        non_contract_evidence = []
    route_keys: set[tuple[str, str, str]] = set()
    contracted_evidence_keys: set[tuple[str, str]] = set()
    initial_contract_ids: set[str] = set()
    initial_contract_article_keys: set[tuple[str, str]] = set()
    evidence_index = {row["rule_id"]: row for row in evidence_rows}
    for route in contract_routes:
        key = (route.get("journal_id", ""), route.get("article_type", ""), route.get("stage", ""))
        if key in route_keys:
            fail(errors, f"Duplicate material route contract: {key}")
        route_keys.add(key)
        if key[2] not in CONTRACT_STAGES:
            fail(errors, f"Invalid canonical stage in route contract: {key}")
        if key[2] == "initial":
            initial_contract_ids.add(key[0])
            initial_contract_article_keys.add((key[0], key[1]))
        route_requirements = route.get("requirements", [])
        route_rule_id_list = [
            str(requirement.get("rule_id") or "")
            for requirement in route_requirements if isinstance(requirement, dict)
        ]
        route_rule_ids = set(route_rule_id_list)
        if len(route_rule_id_list) != len(route_rule_ids):
            fail(errors, f"Material route repeats a rule_id: {key}")
        route_requirements_by_rule = {
            str(requirement.get("rule_id") or ""): requirement
            for requirement in route_requirements if isinstance(requirement, dict)
        }
        revision_variant_owner: dict[str, str] = {}
        for size_field in ("max_package_bytes",):
            size_value = route.get(size_field)
            if size_value is not None and (
                not isinstance(size_value, int) or isinstance(size_value, bool) or size_value <= 0
            ):
                fail(errors, f"Material route has invalid positive integer {size_field}: {key}")
        for requirement in route_requirements:
            rule_id = requirement.get("rule_id", "")
            evidence = evidence_index.get(rule_id)
            if evidence is None:
                fail(errors, f"Material contract references unknown rule_id: {rule_id}")
                continue
            if evidence["journal_id"] != key[0] or evidence["article_type"] != key[1]:
                fail(errors, f"Material contract cross-routes rule {rule_id} into {key}")
            applicable_stages = {
                value.strip()
                for value in (evidence.get("applicable_stages") or "").split(";")
                if value.strip()
            }
            if key[2] not in applicable_stages:
                fail(errors, f"Material contract applies rule {rule_id} outside applicable_stages in {key}")
            contracted_evidence_keys.add((rule_id, key[2]))
            if requirement.get("requirement_class") != evidence["requirement_class"]:
                fail(errors, f"Material contract class differs from evidence for {rule_id}")
            if requirement.get("item_kind") not in ITEM_KINDS:
                fail(errors, f"Material contract has invalid item_kind: {rule_id}")
            if requirement.get("item_kind") == "embedded":
                parent_rule_id = str(requirement.get("parent_rule_id") or "")
                if not parent_rule_id or parent_rule_id not in route_rule_ids:
                    fail(errors, f"Embedded material {rule_id} lacks an in-route parent_rule_id")
                if requirement.get("resolution_required"):
                    fail(errors, f"Embedded material cannot use portal resolution: {rule_id}")
            elif requirement.get("parent_rule_id") is not None:
                fail(errors, f"Non-embedded material declares parent_rule_id: {rule_id}")
            pair_receipt_kind = str(requirement.get("pair_receipt_kind") or "")
            parent_rule_ids = requirement.get("parent_rule_ids", [])
            if requirement.get("item_kind") == "field":
                if pair_receipt_kind != "marked-unmarked-figure":
                    fail(errors, f"Field assertion has unsupported pair_receipt_kind: {rule_id}")
                if (
                    not isinstance(parent_rule_ids, list)
                    or not parent_rule_ids
                    or any(not isinstance(value, str) or not value for value in parent_rule_ids)
                ):
                    fail(errors, f"Field assertion has invalid parent_rule_ids: {rule_id}")
                    parent_rule_ids = []
                if len(parent_rule_ids) != len(set(parent_rule_ids)):
                    fail(errors, f"Field assertion repeats parent_rule_ids: {rule_id}")
                if set(parent_rule_ids) - route_rule_ids:
                    fail(errors, f"Field assertion references out-of-route parents: {rule_id}")
                if any(
                    route_requirements_by_rule.get(parent_id, {}).get("item_kind") != "file"
                    for parent_id in parent_rule_ids
                ):
                    fail(errors, f"Field assertion parent is not a physical file route: {rule_id}")
                if evidence.get("allowed_extensions", "").strip():
                    fail(errors, f"Path-free field assertion carries physical extensions: {rule_id}")
                if evidence.get("requirement_class") != "conditional":
                    fail(errors, f"Cross-file pair assertion must be conditional: {rule_id}")
            elif pair_receipt_kind or parent_rule_ids:
                fail(errors, f"Non-field material declares pair receipt metadata: {rule_id}")
            for size_field in ("max_file_bytes", "max_total_bytes"):
                size_value = requirement.get(size_field)
                if size_value is not None and (
                    not isinstance(size_value, int) or isinstance(size_value, bool) or size_value <= 0
                ):
                    fail(errors, f"Material contract has invalid positive integer {size_field}: {rule_id}")
            allows_marked_revision = requirement.get("allows_marked_revision")
            if allows_marked_revision is not None and not isinstance(allows_marked_revision, bool):
                fail(errors, f"Material contract allows_marked_revision must be boolean: {rule_id}")
            if allows_marked_revision is True and key[2] != "revision":
                fail(errors, f"Material contract allows marked revision outside revision stage: {rule_id}")
            required_revision_variants = requirement.get("required_revision_variants", [])
            if not isinstance(required_revision_variants, list) or any(
                not isinstance(value, str) for value in required_revision_variants
            ):
                fail(errors, f"Material contract required_revision_variants must be a string list: {rule_id}")
                required_revision_variants = []
            if len(required_revision_variants) != len(set(required_revision_variants)):
                fail(errors, f"Material contract repeats required revision variants: {rule_id}")
            invalid_variants = sorted(set(required_revision_variants) - REVISION_VARIANTS)
            if invalid_variants:
                fail(errors, f"Material contract has invalid required revision variants for {rule_id}: {invalid_variants}")
            if required_revision_variants and key[2] != "revision":
                fail(errors, f"Material contract requires revision variants outside revision stage: {rule_id}")
            for variant in required_revision_variants:
                prior_owner = revision_variant_owner.get(variant)
                if prior_owner is not None and prior_owner != rule_id:
                    fail(errors, f"Revision role {variant} is claimed by both {prior_owner} and {rule_id} in {key}")
                revision_variant_owner[variant] = rule_id
            if "marked" in required_revision_variants and allows_marked_revision is not True:
                fail(errors, f"Material contract requires marked revision without explicit permission: {rule_id}")
            if len(required_revision_variants) > int(requirement.get("minimum_rows", 1)):
                fail(errors, f"Material contract minimum_rows cannot cover required revision variants: {rule_id}")
            unblinded_revision_variants = requirement.get("unblinded_revision_variants", [])
            if not isinstance(unblinded_revision_variants, list) or any(
                not isinstance(value, str) for value in unblinded_revision_variants
            ):
                fail(errors, f"Material contract unblinded_revision_variants must be a string list: {rule_id}")
                unblinded_revision_variants = []
            if not set(unblinded_revision_variants).issubset(set(required_revision_variants)):
                fail(errors, f"Unblinded revision variants are not required roles for {rule_id}")
            file_set_alternatives = requirement.get("file_set_alternatives", [])
            if not isinstance(file_set_alternatives, list):
                fail(errors, f"Material contract file_set_alternatives must be a list: {rule_id}")
                file_set_alternatives = []
            alternative_names: set[str] = set()
            registry_extensions = {
                value.strip().lower()
                for value in (evidence.get("allowed_extensions") or "").split(";")
                if value.strip()
            }
            for alternative in file_set_alternatives:
                if not isinstance(alternative, dict):
                    fail(errors, f"Material contract has a non-object file-set alternative: {rule_id}")
                    continue
                alternative_name = str(alternative.get("name") or "")
                if not alternative_name or alternative_name in alternative_names:
                    fail(errors, f"Material contract has an invalid or duplicate file-set alternative name: {rule_id}")
                alternative_names.add(alternative_name)
                declared_extensions: set[str] = set()
                for field in ("any_extensions", "all_extensions", "notes_required_extensions"):
                    values = alternative.get(field, [])
                    if not isinstance(values, list) or any(not isinstance(value, str) for value in values):
                        fail(errors, f"Material contract {field} must be a string list: {rule_id}/{alternative_name}")
                        continue
                    normalized = {value.lower() for value in values}
                    if len(normalized) != len(values) or any(not value.startswith(".") for value in normalized):
                        fail(errors, f"Material contract has duplicate or invalid {field}: {rule_id}/{alternative_name}")
                    declared_extensions |= normalized
                if not alternative.get("any_extensions") and not alternative.get("all_extensions"):
                    fail(errors, f"File-set alternative has no extension criterion: {rule_id}/{alternative_name}")
                if declared_extensions - registry_extensions:
                    fail(errors, f"File-set alternative exceeds evidence extensions for {rule_id}: {sorted(declared_extensions - registry_extensions)}")
                receipt_kind = str(alternative.get("receipt_kind") or "")
                if receipt_kind not in {"", "latex-source-plus-checked-pdf"}:
                    fail(errors, f"File-set alternative has unsupported receipt_kind: {rule_id}/{alternative_name}")
                if receipt_kind == "latex-source-plus-checked-pdf":
                    all_extensions = {str(value).lower() for value in alternative.get("all_extensions", [])}
                    notes_extensions = {
                        str(value).lower() for value in alternative.get("notes_required_extensions", [])
                    }
                    if not {".tex", ".pdf"}.issubset(all_extensions):
                        fail(errors, f"LaTeX receipt alternative lacks .tex + .pdf: {rule_id}/{alternative_name}")
                    if not {".tex", ".pdf"}.issubset(notes_extensions):
                        fail(errors, f"LaTeX receipt alternative lacks notes on both files: {rule_id}/{alternative_name}")
            if evidence["verification_status"] == "UNVERIFIED_CURRENT" and not requirement.get("resolution_required"):
                fail(errors, f"Unverified material rule lacks resolution_required: {rule_id}")
            if (
                requirement.get("item_kind") == "file"
                and requirement.get("requirement_class") == "required"
                and not evidence.get("allowed_extensions", "").strip()
                and not requirement.get("resolution_required")
            ):
                fail(errors, f"Required physical item with no public extension rule lacks portal resolution: {rule_id}")
            if int(requirement.get("minimum_rows", 1)) < 1:
                fail(errors, f"Material contract has invalid minimum_rows: {rule_id}")
    allowed_non_contract_dispositions = {
        "embedded-content", "human-crossfile", "policy-context", "portal-state-only",
        "optional-outside-minimum",
    }
    non_contract_keys: set[tuple[str, str]] = set()
    for entry in non_contract_evidence:
        if not isinstance(entry, dict):
            fail(errors, "non_contract_evidence contains a non-object entry")
            continue
        rule_id = str(entry.get("rule_id") or "")
        stage = str(entry.get("stage") or "")
        disposition = str(entry.get("disposition") or "")
        entry_key = (rule_id, stage)
        if not rule_id or stage not in CONTRACT_STAGES or entry_key in non_contract_keys:
            fail(errors, f"Invalid or duplicate non-contract evidence classification: {entry_key}")
            continue
        non_contract_keys.add(entry_key)
        evidence = evidence_index.get(rule_id)
        if evidence is None:
            fail(errors, f"Non-contract classification references unknown rule_id: {rule_id}")
            continue
        applicable_stages = {
            value.strip() for value in (evidence.get("applicable_stages") or "").split(";") if value.strip()
        }
        if stage not in applicable_stages:
            fail(errors, f"Non-contract classification applies {rule_id} outside evidence stages: {stage}")
        route_key = (evidence["journal_id"], evidence["article_type"], stage)
        if route_key not in route_keys:
            fail(errors, f"Non-contract classification has no executable route: {rule_id}/{stage}")
        if disposition not in allowed_non_contract_dispositions:
            fail(errors, f"Invalid non-contract disposition for {rule_id}/{stage}: {disposition}")
        if disposition == "embedded-content" and evidence.get("allowed_extensions", "").strip():
            fail(errors, f"Embedded-content classification carries physical extensions: {rule_id}/{stage}")
        if disposition == "optional-outside-minimum" and evidence.get("requirement_class") != "optional":
            fail(errors, f"Non-optional evidence is classified outside the minimum contract: {rule_id}/{stage}")
        if disposition == "human-crossfile":
            if evidence.get("requirement_class") not in {"required", "conditional"}:
                fail(errors, f"Human-crossfile evidence is not a required/conditional gate: {rule_id}/{stage}")
            if not evidence.get("allowed_extensions", "").strip():
                fail(errors, f"Human-crossfile evidence lacks a physical extension route: {rule_id}/{stage}")
    overlap = contracted_evidence_keys & non_contract_keys
    if overlap:
        fail(errors, f"Evidence is both contracted and non-contract classified: {sorted(overlap)}")
    classifiable_keys: set[tuple[str, str]] = set()
    for evidence in evidence_rows:
        if evidence.get("authority_class") in NONAUTHORITATIVE:
            continue
        if evidence.get("requirement_class") not in CONTRACT_CLASSIFIABLE_REQUIREMENTS:
            continue
        for stage in (evidence.get("applicable_stages") or "").split(";"):
            stage = stage.strip()
            if (evidence["journal_id"], evidence["article_type"], stage) in route_keys:
                classifiable_keys.add((evidence["rule_id"], stage))
    classified_keys = contracted_evidence_keys | non_contract_keys
    if classifiable_keys != classified_keys:
        fail(
            errors,
            "Evidence-to-contract classification mismatch: "
            f"unclassified={sorted(classifiable_keys - classified_keys)}, "
            f"extraneous={sorted(classified_keys - classifiable_keys)}",
        )
    if initial_contract_ids != route_ids:
        fail(errors, f"Initial material route set mismatch: {sorted(initial_contract_ids ^ route_ids)}")
    supported_article_keys = {
        (str(entry.get("journal_id") or ""), str(entry.get("article_type") or ""))
        for entry in supported
    }
    if initial_contract_article_keys != supported_article_keys:
        fail(
            errors,
            "Initial contract article labels differ from supported route labels: "
            f"{sorted(initial_contract_article_keys ^ supported_article_keys)}",
        )
    observed_stage_counts = {
        stage: sum(1 for key in route_keys if key[2] == stage)
        for stage in CONTRACT_STAGES
    }
    if observed_stage_counts != EXPECTED_STAGE_ROUTE_COUNTS:
        fail(
            errors,
            f"Stage route coverage mismatch: observed={observed_stage_counts}, expected={EXPECTED_STAGE_ROUTE_COUNTS}",
        )
    for stage, count in EXPECTED_STAGE_ROUTE_COUNTS.items():
        documented = (
            f"| {stage} | none;" if count == 0
            else f"| {stage} |"
        )
        if documented not in router_text:
            fail(errors, f"Router does not publish the {stage} contract-coverage row")

    with MANIFEST_TEMPLATE.open(encoding="utf-8-sig", newline="") as handle:
        manifest_headers = next(csv.reader(handle), [])
    if len(manifest_headers) != len(set(manifest_headers)):
        duplicate_headers = sorted({name for name in manifest_headers if manifest_headers.count(name) > 1})
        fail(errors, f"Manifest template has duplicate headers: {duplicate_headers}")
    if manifest_headers != EXPECTED_MANIFEST_HEADERS:
        fail(errors, "Manifest template does not match schema 2.5 ordered headers exactly")
    if not (SKILL_ROOT / "assets" / "submission-audit-report.template.md").is_file():
        fail(errors, "Missing reusable all-files audit report template")
    for required_file in (
        INTAKE_TEMPLATE, EVIDENCE_SYNTHESIS_INTAKE_TEMPLATE, INTAKE_RESOLVER, REPORT_RENDERER,
        SECURITY_HELPER, GOLDEN_TEST_SCRIPT,
        TRANSFER_TEMPLATE,
        CONFERENCE_INTAKE_TEMPLATE, CONFERENCE_MANIFEST_TEMPLATE,
        CONFERENCE_ROUTE_REFERENCE, CONFERENCE_PACKAGE_VALIDATOR,
        SKILL_ROOT / "references" / "intake-transfer-and-human-review.md",
    ):
        if not required_file.is_file():
            fail(errors, f"Missing intake/report workflow artifact: {required_file}")
    if INTAKE_TEMPLATE.is_file():
        try:
            intake_template = json.loads(INTAKE_TEMPLATE.read_text(encoding="utf-8"))
            if (
                not isinstance(intake_template, dict)
                or list(intake_template) != EXPECTED_INTAKE_FIELDS
                or intake_template.get("schema_version") != "1.1"
            ):
                fail(errors, "Submission intake template does not match the exact ordered schema 1.1 fields")
        except (OSError, json.JSONDecodeError) as exc:
            fail(errors, f"Cannot parse submission intake template: {exc}")
    if EVIDENCE_SYNTHESIS_INTAKE_TEMPLATE.is_file():
        try:
            evidence_intake = json.loads(
                EVIDENCE_SYNTHESIS_INTAKE_TEMPLATE.read_text(encoding="utf-8")
            )
            if (
                not isinstance(evidence_intake, dict)
                or list(evidence_intake) != EXPECTED_INTAKE_FIELDS
                or evidence_intake.get("schema_version") != "1.1"
            ):
                fail(
                    errors,
                    "Evidence-synthesis intake template does not match the exact ordered schema 1.1 fields",
                )
            elif (
                evidence_intake.get("study_scope") != "evidence-synthesis"
                or evidence_intake.get("study_design") != ["systematic-review-meta-analysis"]
                or evidence_intake.get("scientific_handoff_packet_digest") != "not-applicable"
                or evidence_intake.get("scientific_prereview_receipt_digest") == "not-applicable"
            ):
                fail(errors, "Evidence-synthesis intake template violates its conditional scope contract")
        except (OSError, json.JSONDecodeError) as exc:
            fail(errors, f"Cannot parse evidence-synthesis intake template: {exc}")
    if TRANSFER_TEMPLATE.is_file():
        try:
            transfer_template = json.loads(TRANSFER_TEMPLATE.read_text(encoding="utf-8"))
            if not isinstance(transfer_template, dict) or set(transfer_template) != EXPECTED_TRANSFER_FIELDS:
                fail(errors, "Transfer-context template does not match the exact dynamic-transfer fields")
        except (OSError, json.JSONDecodeError) as exc:
            fail(errors, f"Cannot parse transfer-context template: {exc}")
    if CONFERENCE_INTAKE_TEMPLATE.is_file():
        try:
            conference_intake = json.loads(CONFERENCE_INTAKE_TEMPLATE.read_text(encoding="utf-8"))
            if (
                not isinstance(conference_intake, dict)
                or list(conference_intake) != EXPECTED_CONFERENCE_INTAKE_FIELDS
                or conference_intake.get("schema_version") != "1.0"
                or conference_intake.get("route_kind") != "conference-portal-finalization"
                or conference_intake.get("content_owner") != "radiology-dissemination"
                or conference_intake.get("portal_owner") != "radiology-submission"
                or conference_intake.get("human_final_action_status") != "PENDING"
            ):
                fail(errors, "Conference portal intake template violates schema/ownership/action boundaries")
            for gate in (
                "embargo_gate", "disclosure_gate", "privacy_gate", "rights_gate",
                "author_approval_gate",
            ):
                if conference_intake.get(gate) != "UNRESOLVED":
                    fail(errors, f"Conference portal template must fail closed at {gate}")
        except (OSError, json.JSONDecodeError) as exc:
            fail(errors, f"Cannot parse conference portal intake template: {exc}")
    if CONFERENCE_MANIFEST_TEMPLATE.is_file():
        try:
            with CONFERENCE_MANIFEST_TEMPLATE.open(encoding="utf-8-sig", newline="") as handle:
                conference_headers = next(csv.reader(handle), [])
            if conference_headers != EXPECTED_CONFERENCE_MANIFEST_HEADERS:
                fail(errors, "Conference portal manifest template headers/order have drifted")
            if len({header.casefold() for header in conference_headers}) != len(conference_headers):
                fail(errors, "Conference portal manifest template has duplicate headers")
        except (OSError, csv.Error) as exc:
            fail(errors, f"Cannot parse conference portal manifest template: {exc}")
    if CONFERENCE_ROUTE_REFERENCE.is_file():
        conference_text = CONFERENCE_ROUTE_REFERENCE.read_text(encoding="utf-8")
        for phrase in (
            "radiology-dissemination", "venue_series_id", "submission_cycle",
            "HUMAN_PORTAL_ACTION_REQUIRED", "readiness_granted=false",
            "portal_action_performed=false", "final action", "Embargo", "Disclosure", "Privacy",
        ):
            if phrase.casefold() not in conference_text.casefold():
                fail(errors, f"Conference portal reference lacks required boundary phrase: {phrase}")
    if CONFERENCE_PACKAGE_VALIDATOR.is_file():
        conference_validator_text = CONFERENCE_PACKAGE_VALIDATOR.read_text(encoding="utf-8")
        for phrase in (
            "HUMAN_PORTAL_ACTION_REQUIRED", '"readiness_granted": False',
            '"portal_action_performed": False', "radiology-dissemination",
            "conference abstract row bound to the frozen dissemination artifact",
        ):
            if phrase not in conference_validator_text:
                fail(errors, f"Conference package validator lacks required fail-closed contract: {phrase}")

    test_source = TEST_SCRIPT.read_text(encoding="utf-8")
    seen_contract_ids: set[str] = set()
    for contract in negative_contracts:
        contract_id = str(contract.get("id") or "")
        if not contract_id or contract_id in seen_contract_ids:
            fail(errors, f"Invalid or duplicate negative contract id: {contract_id or '[blank]'}")
        seen_contract_ids.add(contract_id)
        for field in ("input", "expected", "forbidden", "test_method"):
            if not str(contract.get(field) or "").strip():
                fail(errors, f"Negative contract {contract_id or '[blank]'} lacks {field}")
        method = str(contract.get("test_method") or "")
        if method and not re.search(rf"^\s+def {re.escape(method)}\(self\)", test_source, re.MULTILINE):
            fail(errors, f"Negative contract {contract_id} is not implemented by {method}")

    tests = subprocess.run(
        [sys.executable, str(TEST_SCRIPT)], check=False, capture_output=True, text=True, encoding="utf-8"
    )
    if tests.returncode != 0:
        fail(errors, "Structural auditor regression tests failed:\n" + tests.stdout + tests.stderr)
    golden_tests = subprocess.run(
        [sys.executable, str(GOLDEN_TEST_SCRIPT)],
        check=False, capture_output=True, text=True, encoding="utf-8",
    )
    if golden_tests.returncode != 0:
        fail(errors, "Cross-step submission golden scenarios failed:\n" + golden_tests.stdout + golden_tests.stderr)

    profile_count = len(list(PROFILE_DIR.glob("*.md")))
    regression_case_count = len(re.findall(r"^\s+def test_[A-Za-z0-9_]+\(self\)", test_source, re.MULTILINE))
    golden_scenario_count = len(re.findall(
        r"^\s+def test_[A-Za-z0-9_]+\(self\)",
        GOLDEN_TEST_SCRIPT.read_text(encoding="utf-8") if GOLDEN_TEST_SCRIPT.is_file() else "",
        re.MULTILINE,
    ))
    receipt_counts = {
        "routes": len(route_ids),
        "profiles": profile_count,
        "evidence_rows": len(evidence_rows),
        "route_contracts": len(contract_routes),
        "negative_contracts": len(negative_contracts),
        "regression_cases": regression_case_count,
        "golden_scenarios": golden_scenario_count,
    }
    validate_frozen_receipt(errors, receipt_counts)

    result = {
        "status": "PASS" if not errors else "FAIL",
        "routes": len(route_ids),
        "evidence_rows": len(evidence_rows),
        "profiles": profile_count,
        "route_contracts": len(contract_routes),
        "negative_contracts": len(negative_contracts),
        "regression_tests": "PASS" if tests.returncode == 0 else "FAIL",
        "regression_cases": regression_case_count,
        "golden_tests": "PASS" if golden_tests.returncode == 0 else "FAIL",
        "golden_scenarios": golden_scenario_count,
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
