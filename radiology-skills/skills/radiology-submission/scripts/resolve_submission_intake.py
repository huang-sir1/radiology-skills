#!/usr/bin/env python3
"""Resolve an untrusted submission intake into a fail-closed route plan.

The resolver selects only exact bundled routes, inventories bytes without
inferring their semantic role, and may emit an unresolved draft manifest. It
never creates file/QA PASS, READY, not-applicable decisions, portal receipts,
or human QA evidence. Its execution_status may be PASS only for route resolution.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any

from audit_submission_package import (
    JOURNAL_REVIEW_MODELS,
    REQUIRED_HEADER_ORDER,
    REVIEW_MODELS,
    SCHEMA_VERSION as MANIFEST_SCHEMA_VERSION,
    STAGES,
    STUDY_DESIGNS,
    STUDY_SCOPES,
    is_nonzero_sha256,
    is_linklike,
)
from submission_security import (
    atomic_write_text,
    authorized_package_root as validate_package_root,
    bounded_sha256,
    ensure_output_path_safe,
    load_json_strict,
)


INTAKE_SCHEMA_VERSION = "1.1"
SKILL_ROOT = Path(__file__).resolve().parents[1]
ROUTE_REGISTRY = SKILL_ROOT / "references" / "journal-required-materials.json"
EVIDENCE_REGISTRY = SKILL_ROOT / "references" / "journal-requirements-evidence.tsv"
ROUTING_CASES = SKILL_ROOT / "tests" / "submission-routing-cases.json"
PROFILE_DIR = SKILL_ROOT / "references" / "journals"
SCOPES = {"upload-root", "attachment-set", "partial"}
TRANSFER_MODES = {"as-is", "modify"}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
PROJECT_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{2,127}$")
ARTIFACT_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{1,127}$")
MAX_INTAKE_BYTES = 1_000_000
MAX_INVENTORY_FILES = 10_000
MAX_INVENTORY_FILE_BYTES = 2_000_000_000
MAX_INVENTORY_TOTAL_BYTES = 5_000_000_000
TOP_LEVEL_FIELD_ORDER = [
    "schema_version", "target_journal_id", "article_type", "submission_stage",
    "publisher_stage_label", "package_root", "review_scope", "study_design",
    "review_model", "manuscript_version", "project_id", "study_scope",
    "project_state_digest", "modality_role_digest",
    "scientific_handoff_packet_digest", "scientific_prereview_receipt_digest",
    "source_artifact_id", "analysis_lock_digest", "claim_registry_digest",
    "response_package_digest", "guide_checked_on", "transfer_context",
]
TOP_LEVEL_FIELDS = set(TOP_LEVEL_FIELD_ORDER)
TRANSFER_FIELDS = {
    "source_journal_id", "target_journal_id", "target_article_type",
    "transfer_offer_receipt_sha256", "transfer_offer_checked_on", "transfer_mode",
    "source_inventory_sha256", "target_portal_inventory_sha256",
    "target_initial_route_id",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Resolve exact journal/article/stage intake without granting readiness",
    )
    parser.add_argument("intake", help="Path to submission-intake JSON")
    parser.add_argument(
        "--package-root", required=True,
        help="Explicit user-authorized absolute package root; must exactly match intake package_root",
    )
    parser.add_argument(
        "--output-dir",
        help="Optional directory outside package_root for route-plan JSON and draft manifest CSV",
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Replace resolver-owned output files; never modifies author package files",
    )
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    return bounded_sha256(path)[0]


def load_json(path: Path) -> dict[str, Any]:
    return load_json_strict(path, max_bytes=MAX_INTAKE_BYTES)


def iso_date(value: object) -> date | None:
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return None


def canonical_route_id(journal_id: str, article_type: str, stage: str) -> str:
    return f"{journal_id}::{article_type}::{stage}"


def add_error(errors: list[dict[str, str]], code: str, message: str) -> None:
    errors.append({"code": code, "message": message})


def authorized_package_root(raw_value: str) -> Path:
    return validate_package_root(raw_value)


def inventory_package(root: Path, errors: list[dict[str, str]]) -> list[dict[str, object]]:
    candidates: list[tuple[Path, str, int]] = []
    total_bytes = 0
    limit_exceeded = False
    for current_root, dirnames, filenames in os.walk(root, followlinks=False):
        current = Path(current_root)
        for dirname in list(dirnames):
            candidate = current / dirname
            if is_linklike(candidate):
                add_error(errors, "PACKAGE_SYMLINK", f"directory symlink was not followed: {candidate.relative_to(root).as_posix()}")
                dirnames.remove(dirname)
        for filename in filenames:
            candidate = current / filename
            relative = candidate.relative_to(root).as_posix()
            if is_linklike(candidate):
                add_error(errors, "PACKAGE_SYMLINK", f"file symlink was not followed: {relative}")
                continue
            if not candidate.is_file():
                continue
            try:
                size = candidate.stat().st_size
            except OSError as exc:
                add_error(errors, "PACKAGE_STAT", f"cannot inspect {relative}: {exc}")
                continue
            candidates.append((candidate, relative, size))
            total_bytes += size
            if len(candidates) > MAX_INVENTORY_FILES:
                add_error(errors, "PACKAGE_LIMIT", f"package exceeds {MAX_INVENTORY_FILES} files")
                limit_exceeded = True
                break
            if size > MAX_INVENTORY_FILE_BYTES:
                add_error(errors, "PACKAGE_LIMIT", f"{relative} exceeds the {MAX_INVENTORY_FILE_BYTES}-byte intake hashing limit")
                limit_exceeded = True
            if total_bytes > MAX_INVENTORY_TOTAL_BYTES:
                add_error(errors, "PACKAGE_LIMIT", f"package exceeds the {MAX_INVENTORY_TOTAL_BYTES}-byte intake hashing limit")
                limit_exceeded = True
                break
        if limit_exceeded:
            break
    if limit_exceeded:
        return [{
            "path": relative, "bytes": size, "sha256": None,
            "suffix": candidate.suffix.lower(), "semantic_mapping": "NOT_HASHED_LIMIT",
        } for candidate, relative, size in candidates]
    inventory: list[dict[str, object]] = []
    for candidate, relative, size in candidates:
        inventory.append({
                "path": relative,
                "bytes": size,
                "sha256": sha256_file(candidate),
                "suffix": candidate.suffix.lower(),
                "semantic_mapping": "UNASSIGNED_HUMAN_GATE",
            })
    return sorted(inventory, key=lambda item: str(item["path"]).casefold())


def supported_profiles() -> tuple[dict[tuple[str, str], dict[str, str]], dict[str, str]]:
    with ROUTING_CASES.open(encoding="utf-8") as handle:
        data = json.load(handle)
    profiles: dict[tuple[str, str], dict[str, str]] = {}
    journal_profiles: dict[str, str] = {}
    for row in data.get("supported_routes", []):
        key = (str(row["journal_id"]), str(row["article_type"]))
        profiles[key] = {str(k): str(v) for k, v in row.items()}
        journal_profiles[key[0]] = str(row["profile"])
    return profiles, journal_profiles


def route_registry() -> tuple[list[dict[str, Any]], str]:
    with ROUTE_REGISTRY.open(encoding="utf-8") as handle:
        data = json.load(handle)
    routes = data.get("routes")
    if not isinstance(routes, list):
        raise ValueError("bundled route registry has no routes array")
    return routes, sha256_file(ROUTE_REGISTRY)


def evidence_by_rule() -> tuple[dict[str, dict[str, str]], str]:
    with EVIDENCE_REGISTRY.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    return {str(row.get("rule_id") or ""): row for row in rows}, sha256_file(EVIDENCE_REGISTRY)


def validate_transfer(
    intake: dict[str, Any], target_journal: str, target_article: str,
    routes: list[dict[str, Any]], errors: list[dict[str, str]],
) -> dict[str, Any] | None:
    context = intake.get("transfer_context")
    if not isinstance(context, dict):
        add_error(errors, "TRANSFER_CONTEXT", "transfer stage requires a structured transfer_context")
        return None
    unknown = sorted(set(context) - TRANSFER_FIELDS)
    missing = sorted(TRANSFER_FIELDS - set(context))
    if unknown:
        add_error(errors, "TRANSFER_CONTEXT_FIELDS", f"unknown transfer_context fields: {unknown}")
    if missing:
        add_error(errors, "TRANSFER_CONTEXT_FIELDS", f"missing transfer_context fields: {missing}")
    source_journal = str(context.get("source_journal_id") or "").strip()
    if not source_journal or source_journal == target_journal:
        add_error(errors, "TRANSFER_SOURCE", "source_journal_id must identify a different source journal")
    if str(context.get("target_journal_id") or "") != target_journal:
        add_error(errors, "TRANSFER_TARGET", "transfer target_journal_id must exactly match intake target_journal_id")
    if str(context.get("target_article_type") or "") != target_article:
        add_error(errors, "TRANSFER_ARTICLE", "transfer target_article_type must exactly match intake article_type")
    if str(context.get("transfer_mode") or "") not in TRANSFER_MODES:
        add_error(errors, "TRANSFER_MODE", "transfer_mode must be as-is or modify")
    for field in (
        "transfer_offer_receipt_sha256", "source_inventory_sha256",
        "target_portal_inventory_sha256",
    ):
        value = str(context.get(field) or "")
        if not SHA256_RE.fullmatch(value) or set(value) == {"0"}:
            add_error(errors, "TRANSFER_DIGEST", f"{field} must be a nonzero lowercase SHA-256")
    checked = iso_date(context.get("transfer_offer_checked_on"))
    if checked is None or checked > date.today():
        add_error(errors, "TRANSFER_DATE", "transfer_offer_checked_on must be a nonfuture YYYY-MM-DD")
    expected_route_id = canonical_route_id(target_journal, target_article, "initial")
    if str(context.get("target_initial_route_id") or "") != expected_route_id:
        add_error(errors, "TRANSFER_ROUTE_ID", f"target_initial_route_id must equal {expected_route_id}")
    initial_matches = [
        route for route in routes
        if (route.get("journal_id"), route.get("article_type"), route.get("stage"))
        == (target_journal, target_article, "initial")
    ]
    if len(initial_matches) != 1:
        add_error(errors, "TRANSFER_TARGET_ROUTE", "target has no unique bundled initial route")
        return None
    return initial_matches[0]


def draft_manifest_rows(
    intake: dict[str, Any], route: dict[str, Any] | None,
    evidence: dict[str, dict[str, str]], effective_stage: str,
) -> list[dict[str, str]]:
    if route is None:
        return []
    rows: list[dict[str, str]] = []
    designs = ";".join(sorted(str(value) for value in intake.get("study_design", [])))
    for index, requirement in enumerate(route.get("requirements", []), start=1):
        rule_id = str(requirement.get("rule_id") or "")
        rule = evidence.get(rule_id, {})
        pending_guide = bool(requirement.get("resolution_required")) or (
            str(rule.get("verification_status") or "").upper()
            not in {"CURRENT", "VERIFIED_CURRENT"}
        )
        row = {header: "" for header in REQUIRED_HEADER_ORDER}
        row.update({
            "schema_version": MANIFEST_SCHEMA_VERSION,
            "project_id": str(intake.get("project_id") or ""),
            "study_scope": str(intake.get("study_scope") or ""),
            "project_state_digest": str(intake.get("project_state_digest") or ""),
            "modality_role_digest": str(intake.get("modality_role_digest") or ""),
            "scientific_handoff_packet_digest": str(
                intake.get("scientific_handoff_packet_digest") or ""
            ),
            "scientific_prereview_receipt_digest": str(
                intake.get("scientific_prereview_receipt_digest") or ""
            ),
            "source_artifact_id": "not-applicable",
            "analysis_lock_digest": str(intake.get("analysis_lock_digest") or ""),
            "claim_registry_digest": str(intake.get("claim_registry_digest") or ""),
            "response_package_digest": str(intake.get("response_package_digest") or ""),
            "item_id": f"UNASSIGNED-{index:02d}-{rule_id}",
            "journal_id": str(intake.get("target_journal_id") or ""),
            "article_type": str(intake.get("article_type") or ""),
            "submission_stage": effective_stage,
            "study_design": designs,
            "review_model": str(intake.get("review_model") or ""),
            "material": str(rule.get("material") or rule.get("rule_summary") or rule_id),
            "requirement_class": str(requirement.get("requirement_class") or ""),
            "condition": str(rule.get("condition") or "human adjudication required"),
            "rule_id": rule_id,
            "authority_class": str(rule.get("authority_class") or ""),
            "source_url": str(rule.get("source_url") or ""),
            "guide_verified_on": str(rule.get("checked_on") or ""),
            "expected_extensions": str(rule.get("allowed_extensions") or ""),
            "blinded": (
                str(requirement.get("blinded")).lower()
                if isinstance(requirement.get("blinded"), bool) else "not-applicable"
            ),
            "tracked_changes_policy": "not-applicable",
            "revision_variant": "not-applicable",
            "status": "pending-guide" if pending_guide else "pending-author",
            "technical_qa": "not-checked",
            "render_qa": "not-checked",
            "content_gate": "not-checked",
            "anonymization_qa": "not-checked",
            "crossfile_qa": "not-checked",
            "owner": "author-and-reviewer",
            "notes": "resolver_seed_only=true; no file mapping, N/A decision, portal receipt, QA PASS or readiness granted",
        })
        rows.append(row)
    return rows


def write_outputs(
    output_dir: Path, package_root: Path, report: dict[str, Any],
    draft_rows: list[dict[str, str]], force: bool,
) -> dict[str, str]:
    resolved_output = ensure_output_path_safe(
        output_dir / "submission-route-plan.json", forbidden_root=package_root,
    ).parent
    plan_path = ensure_output_path_safe(
        resolved_output / "submission-route-plan.json", forbidden_root=package_root,
    )
    manifest_path = ensure_output_path_safe(
        resolved_output / "submission-manifest.draft.csv", forbidden_root=package_root,
    )
    for path in (plan_path, manifest_path):
        if path.exists() and not force:
            raise ValueError(f"refusing to replace existing resolver output without --force: {path}")
    if force and plan_path.exists():
        existing = load_json_strict(plan_path, max_bytes=MAX_INTAKE_BYTES)
        if existing.get("tool") != "radiology-submission intake resolver":
            raise ValueError("--force may replace only a resolver-owned route-plan JSON")
    if force and manifest_path.exists():
        with manifest_path.open(encoding="utf-8-sig", newline="") as handle:
            if next(csv.reader(handle), []) != REQUIRED_HEADER_ORDER:
                raise ValueError("--force may replace only a resolver-owned draft-manifest schema")
    manifest_buffer = io.StringIO(newline="")
    writer = csv.DictWriter(manifest_buffer, fieldnames=REQUIRED_HEADER_ORDER)
    writer.writeheader()
    writer.writerows(draft_rows)
    # Publish the plan last. A failed draft write can therefore never leave a
    # newly published PASS plan pointing at an absent/stale draft.
    atomic_write_text(manifest_path, manifest_buffer.getvalue(), encoding="utf-8")
    atomic_write_text(
        plan_path, json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8",
    )
    return {"route_plan": str(plan_path), "draft_manifest": str(manifest_path)}


def main() -> int:
    args = parse_args()
    errors: list[dict[str, str]] = []
    try:
        intake_path = Path(args.intake).expanduser().resolve(strict=True)
        intake = load_json(intake_path)
        routes, route_hash = route_registry()
        evidence, evidence_hash = evidence_by_rule()
        profiles, journal_profiles = supported_profiles()
    except (OSError, ValueError, json.JSONDecodeError, csv.Error) as exc:
        print(json.dumps({"execution_status": "FAIL", "status": "FAIL", "intake_state": "TARGET_OR_ROUTE_UNRESOLVED", "errors": [{"code": "INPUT", "message": str(exc)}]}, ensure_ascii=False, indent=2))
        return 2

    unknown_fields = sorted(set(intake) - TOP_LEVEL_FIELDS)
    missing_fields = sorted(TOP_LEVEL_FIELDS - set(intake))
    if unknown_fields:
        add_error(errors, "INTAKE_FIELDS", f"unknown intake fields: {unknown_fields}")
    if missing_fields:
        add_error(errors, "INTAKE_FIELDS", f"missing intake fields: {missing_fields}")
    if not unknown_fields and not missing_fields and list(intake) != TOP_LEVEL_FIELD_ORDER:
        add_error(
            errors, "INTAKE_FIELD_ORDER",
            "intake JSON must use the exact canonical field order for schema 1.1",
        )
    if str(intake.get("schema_version") or "") != INTAKE_SCHEMA_VERSION:
        add_error(errors, "INTAKE_SCHEMA", f"schema_version must equal {INTAKE_SCHEMA_VERSION}")

    journal_id = str(intake.get("target_journal_id") or "").strip()
    article_type = str(intake.get("article_type") or "").strip()
    stage = str(intake.get("submission_stage") or "").strip()
    scope = str(intake.get("review_scope") or "").strip()
    review_model = str(intake.get("review_model") or "").strip()
    project_id = str(intake.get("project_id") or "").strip()
    study_scope = str(intake.get("study_scope") or "").strip().lower()
    source_artifact_id = str(intake.get("source_artifact_id") or "").strip()
    profile_key = (journal_id, article_type)
    if profile_key not in profiles:
        add_error(errors, "TARGET_EXACT_MATCH", "journal_id and article_type must exactly match one supported route; aliases and family proxies are forbidden")
    if stage not in STAGES:
        add_error(errors, "STAGE", f"submission_stage must be one of {sorted(STAGES)}")
    if scope not in SCOPES:
        add_error(errors, "SCOPE", f"review_scope must be one of {sorted(SCOPES)}")
    designs = intake.get("study_design")
    if not isinstance(designs, list) or not designs or any(not isinstance(value, str) for value in designs):
        add_error(errors, "STUDY_DESIGN", "study_design must be a nonempty array of controlled strings")
        design_set: set[str] = set()
    else:
        design_set = set(designs)
        if len(design_set) != len(designs):
            add_error(errors, "STUDY_DESIGN", "study_design must not contain duplicate tokens")
        invalid = sorted(design_set - STUDY_DESIGNS)
        if invalid:
            add_error(errors, "STUDY_DESIGN", f"invalid study_design tokens: {invalid}")
        if design_set == {"other"}:
            add_error(errors, "STUDY_DESIGN", "study_design=other cannot be the sole submission route")
    if review_model not in REVIEW_MODELS:
        add_error(errors, "REVIEW_MODEL", f"review_model must be one of {sorted(REVIEW_MODELS)}")
    elif review_model == "not-confirmed":
        add_error(errors, "REVIEW_MODEL", "review_model=not-confirmed is an unresolved intake state")
    elif journal_id and review_model not in JOURNAL_REVIEW_MODELS.get(journal_id, set()):
        add_error(errors, "REVIEW_MODEL_ROUTE", "selected review_model conflicts with the journal profile")
    if not PROJECT_ID_RE.fullmatch(project_id):
        add_error(errors, "PROJECT_ID", "project_id must be a stable 3-128 character identifier")
    if study_scope not in STUDY_SCOPES:
        add_error(errors, "STUDY_SCOPE", f"study_scope must be one of {sorted(STUDY_SCOPES)}")
    for field in ("project_state_digest", "modality_role_digest"):
        if not is_nonzero_sha256(str(intake.get(field) or "")):
            add_error(errors, "SCIENTIFIC_HANDOFF_DIGEST", f"{field} must be a nonzero lowercase SHA-256")
    handoff_digest = str(intake.get("scientific_handoff_packet_digest") or "")
    prereview_digest = str(intake.get("scientific_prereview_receipt_digest") or "")
    if prereview_digest != "not-applicable" and not is_nonzero_sha256(prereview_digest):
        add_error(
            errors, "SCIENTIFIC_PREREVIEW_RECEIPT_DIGEST",
            "scientific_prereview_receipt_digest must be a nonzero lowercase SHA-256 or not-applicable",
        )
    if study_scope == "evidence-synthesis":
        if handoff_digest != "not-applicable":
            add_error(
                errors, "EVIDENCE_SYNTHESIS_HANDOFF",
                "evidence-synthesis scope requires scientific_handoff_packet_digest=not-applicable",
            )
        if not is_nonzero_sha256(prereview_digest):
            add_error(
                errors, "EVIDENCE_SYNTHESIS_PREREVIEW",
                "evidence-synthesis scope requires a nonzero scientific_prereview_receipt_digest",
            )
        if "systematic-review-meta-analysis" not in design_set:
            add_error(
                errors, "EVIDENCE_SYNTHESIS_DESIGN",
                "evidence-synthesis scope requires study_design=systematic-review-meta-analysis",
            )
    elif not is_nonzero_sha256(handoff_digest):
        add_error(
            errors, "SCIENTIFIC_HANDOFF_DIGEST",
            "scientific_handoff_packet_digest must be a nonzero lowercase SHA-256",
        )
    if not ARTIFACT_ID_RE.fullmatch(source_artifact_id) or source_artifact_id == "not-applicable":
        add_error(errors, "SOURCE_ARTIFACT_ID", "source_artifact_id must be a stable 2-128 character frozen-source identifier")
    for field in ("analysis_lock_digest", "claim_registry_digest"):
        if not is_nonzero_sha256(str(intake.get(field) or "")):
            add_error(errors, "UPSTREAM_DIGEST", f"{field} must be a nonzero lowercase SHA-256")
    response_digest = str(intake.get("response_package_digest") or "")
    if stage == "revision":
        if not is_nonzero_sha256(response_digest):
            add_error(errors, "RESPONSE_PACKAGE_DIGEST", "revision intake requires a nonzero lowercase response_package_digest SHA-256")
    elif response_digest != "not-applicable" and not is_nonzero_sha256(response_digest):
        add_error(errors, "RESPONSE_PACKAGE_DIGEST", "response_package_digest must be a nonzero lowercase SHA-256 or not-applicable")
    checked = iso_date(intake.get("guide_checked_on"))
    if checked is None or checked > date.today():
        add_error(errors, "GUIDE_DATE", "guide_checked_on must be a nonfuture YYYY-MM-DD")
    if not str(intake.get("manuscript_version") or "").strip():
        add_error(errors, "MANUSCRIPT_VERSION", "manuscript_version is required")
    if not str(intake.get("publisher_stage_label") or "").strip():
        add_error(errors, "PUBLISHER_STAGE_LABEL", "publisher_stage_label is required and preserves publisher wording")

    package_root: Path | None = None
    inventory: list[dict[str, object]] = []
    try:
        package_root = authorized_package_root(args.package_root)
        intake_root_raw = str(intake.get("package_root") or "").strip()
        if intake_root_raw.startswith(("\\\\", "//", "\\\\?\\", "\\\\.\\")):
            raise ValueError("intake package_root cannot be UNC or a Windows device path")
        intake_root = Path(intake_root_raw).expanduser()
        if not intake_root.is_absolute():
            raise ValueError("intake package_root must be absolute")
        intake_lexical = Path(os.path.abspath(str(intake_root)))
        authorized_lexical = Path(os.path.abspath(args.package_root))
        if os.path.normcase(str(intake_lexical)) != os.path.normcase(str(authorized_lexical)):
            raise ValueError("intake package_root does not exactly match the explicit --package-root authorization")
        inventory = inventory_package(package_root, errors)
    except (OSError, ValueError) as exc:
        add_error(errors, "PACKAGE_ROOT", str(exc))

    selected_route: dict[str, Any] | None = None
    effective_stage = stage
    transfer_context: dict[str, Any] | None = None
    if stage == "transfer":
        selected_route = validate_transfer(intake, journal_id, article_type, routes, errors)
        effective_stage = "initial"
        transfer_context = intake.get("transfer_context") if isinstance(intake.get("transfer_context"), dict) else None
    elif stage in STAGES:
        matches = [
            route for route in routes
            if (route.get("journal_id"), route.get("article_type"), route.get("stage"))
            == (journal_id, article_type, stage)
        ]
        if len(matches) != 1:
            add_error(errors, "ROUTE_UNSUPPORTED", f"no unique bundled route for {canonical_route_id(journal_id, article_type, stage)}")
        else:
            selected_route = matches[0]

    profile_path: Path | None = None
    profile_hash: str | None = None
    if journal_id in journal_profiles:
        candidate = PROFILE_DIR / journal_profiles[journal_id]
        if candidate.is_file():
            profile_path = candidate.resolve()
            profile_hash = sha256_file(candidate)
        else:
            add_error(errors, "PROFILE", f"journal profile is missing: {candidate}")

    draft_rows = draft_manifest_rows(intake, selected_route, evidence, effective_stage)
    unresolved_rules = [
        str(requirement.get("rule_id") or "")
        for requirement in (selected_route or {}).get("requirements", [])
        if requirement.get("resolution_required")
    ]
    if errors:
        intake_state = "TARGET_OR_ROUTE_UNRESOLVED"
    elif stage == "transfer":
        intake_state = "TRANSFER_REPROFILE_REQUIRED"
    else:
        intake_state = "INTAKE_ONLY"
    report: dict[str, Any] = {
        "tool": "radiology-submission intake resolver",
        "execution_status": "FAIL" if errors else "PASS",
        "status": "FAIL" if errors else "PASS",
        "intake_state": intake_state,
        "readiness_granted": False,
        "boundary": "Route selection and byte inventory only; no semantic file mapping, N/A decision, portal completion, QA PASS or submission READY is inferred",
        "intake": {
            "path": str(intake_path),
            "journal_id": journal_id,
            "article_type": article_type,
            "requested_stage": stage,
            "publisher_stage_label": str(intake.get("publisher_stage_label") or ""),
            "effective_contract_stage": effective_stage,
            "review_scope": scope,
            "study_design": sorted(design_set),
            "review_model": review_model,
            "project_id": project_id,
            "study_scope": study_scope,
            "manuscript_version": str(intake.get("manuscript_version") or ""),
        },
        "upstream_provenance": {
            "project_id": [project_id] if project_id else [],
            "study_scope": [study_scope] if study_scope else [],
            "project_state_digest": [str(intake.get("project_state_digest") or "")],
            "modality_role_digest": [str(intake.get("modality_role_digest") or "")],
            "scientific_handoff_packet_digest": [
                str(intake.get("scientific_handoff_packet_digest") or "")
            ],
            "scientific_prereview_receipt_digest": [prereview_digest],
            "source_artifact_ids": [source_artifact_id] if source_artifact_id else [],
            "analysis_lock_digest": [str(intake.get("analysis_lock_digest") or "")],
            "claim_registry_digest": [str(intake.get("claim_registry_digest") or "")],
            "response_package_digest": [str(intake.get("response_package_digest") or "")],
            "authentication": "NOT_PERFORMED",
            "boundary": (
                "These are intake foreign-key receipts only; the resolver validates syntax and "
                "route binding but does not authenticate upstream project, modality, handoff, "
                "prereview, analysis, claim or response records"
            ),
        },
        "route": {
            "route_id": canonical_route_id(journal_id, article_type, effective_stage) if selected_route else None,
            "contract_matched": selected_route is not None,
            "requirements": (selected_route or {}).get("requirements", []),
            "unresolved_current_rule_ids": unresolved_rules,
        },
        "registries": {
            "route_contract": {"path": str(ROUTE_REGISTRY.resolve()), "sha256": route_hash},
            "evidence": {"path": str(EVIDENCE_REGISTRY.resolve()), "sha256": evidence_hash},
            "journal_profile": {"path": str(profile_path) if profile_path else None, "sha256": profile_hash},
        },
        "package_inventory": {
            "root": str(package_root) if package_root else None,
            "declared_scope": scope,
            "files": inventory,
            "semantic_mapping": "NOT_PERFORMED",
        },
        "transfer_context": transfer_context,
        "draft_manifest": {
            "schema_version": MANIFEST_SCHEMA_VERSION,
            "rows": len(draft_rows),
            "state": "UNRESOLVED_SEED_ONLY",
        },
        "human_gates": [
            "Authenticate and read the exact current journal guide and applicable logged-in portal screen",
            "Map each inventoried file to a route requirement and adjudicate every conditional branch",
            "Render and inspect every human-facing artifact; verify anonymization and cross-file consistency",
            "Authenticate upstream project-state, modality-role, scientific-handoff, prereview, analysis, claim and response digests against their frozen registries",
            "A human submission reviewer alone may issue READY or another final readiness verdict",
        ],
        "errors": errors,
    }
    if args.output_dir and package_root is not None and not errors:
        try:
            report["outputs"] = write_outputs(Path(args.output_dir), package_root, report, draft_rows, args.force)
        except (OSError, ValueError) as exc:
            add_error(errors, "OUTPUT", str(exc))
            report["status"] = "FAIL"
            report["execution_status"] = "FAIL"
            report["intake_state"] = "TARGET_OR_ROUTE_UNRESOLVED"
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
