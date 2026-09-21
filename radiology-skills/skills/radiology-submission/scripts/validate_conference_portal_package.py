#!/usr/bin/env python3
"""Fail-closed conference portal field/file contract.

This checker never opens a portal, enters values, attests, uploads, submits, or
grants readiness.  It validates the prepared handoff for a final human action.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urlparse

from submission_security import (
    authorized_package_root,
    bounded_sha256,
    inventory_snapshot,
    is_linklike,
    load_json_strict,
)


INTAKE_FIELDS = [
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
MANIFEST_FIELDS = [
    "schema_version", "venue_series_id", "submission_cycle", "submission_type",
    "item_id", "item_kind", "material", "portal_designation",
    "requirement_class", "condition", "authority_class", "source_url",
    "verified_on", "allowed_extensions", "max_bytes", "version", "source_artifact_id",
    "source_artifact_sha256", "path", "upload_sha256", "value_status", "technical_qa", "render_qa",
    "content_gate", "claim_boundary", "embargo_gate", "disclosure_gate",
    "privacy_gate", "rights_gate", "human_owner", "notes",
]
ITEM_KINDS = {"upload-file", "portal-field", "portal-attestation"}
REQUIREMENT_CLASSES = {"required", "conditional", "optional"}
AUTHORITY_CLASSES = {"CURRENT_CALL", "PORTAL_CURRENT", "OFFICIAL_FORM"}
VALUE_STATES = {"READY_FOR_HUMAN_ENTRY", "NOT_APPLICABLE_WITH_HUMAN_RECEIPT"}
QA_STATES = {"PASS", "NOT_APPLICABLE"}
HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
PLACEHOLDER_RE = re.compile(r"replace|example|todo|tbd|unknown|placeholder", re.IGNORECASE)
MAX_CONTROL_BYTES = 2_000_000


def _text(value: Any) -> str:
    return str(value or "").strip()


def _is_nonzero_digest(value: Any) -> bool:
    digest = _text(value)
    return bool(HEX64_RE.fullmatch(digest)) and digest != "0" * 64


def _is_concrete(value: Any) -> bool:
    text = _text(value)
    return bool(text) and not PLACEHOLDER_RE.search(text)


def _https_url(value: Any) -> bool:
    parsed = urlparse(_text(value))
    return parsed.scheme == "https" and bool(parsed.netloc) and not PLACEHOLDER_RE.search(parsed.netloc)


def _parse_day(value: Any, label: str, errors: list[str]) -> date | None:
    try:
        return datetime.strptime(_text(value), "%Y-%m-%d").date()
    except ValueError:
        errors.append(f"{label} must use YYYY-MM-DD")
        return None


def _safe_relative_path(value: str) -> bool:
    if not value or "\\" in value:
        return False
    pure = PurePosixPath(value)
    return not pure.is_absolute() and all(part not in {"", ".", ".."} for part in pure.parts)


def validate_intake(
    payload: dict[str, Any], *, now: datetime | None = None, max_live_age_days: int = 7,
) -> list[str]:
    errors: list[str] = []
    if list(payload) != INTAKE_FIELDS:
        errors.append("intake keys/order do not match conference schema 1.0")
        return errors
    if payload.get("schema_version") != "1.0":
        errors.append("intake schema_version must be 1.0")
    if payload.get("route_kind") != "conference-portal-finalization":
        errors.append("route_kind must be conference-portal-finalization")
    for field in (
        "venue_name", "venue_series_id", "submission_cycle", "submission_type",
        "project_id", "abstract_artifact_id", "call_capture_locator",
        "portal_capture_locator", "human_final_action_owner",
    ):
        if not _is_concrete(payload.get(field)):
            errors.append(f"{field} must be concrete and non-placeholder")
    for field in ("current_call_url", "portal_url"):
        if not _https_url(payload.get(field)):
            errors.append(f"{field} must be a concrete direct HTTPS URL")
    if payload.get("call_status") != "OPEN":
        errors.append("current call must be visibly OPEN for this cycle/type")
    current = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    for field in ("call_checked_on", "portal_checked_on"):
        checked = _parse_day(payload.get(field), field, errors)
        if checked is not None:
            age = (current.date() - checked).days
            if age < 0:
                errors.append(f"{field} cannot be in the future")
            elif age > max_live_age_days:
                errors.append(f"{field} is older than {max_live_age_days} days; reverify live")
    deadline_text = _text(payload.get("submission_deadline"))
    try:
        deadline = datetime.fromisoformat(deadline_text)
        if deadline.tzinfo is None or deadline.utcoffset() is None:
            raise ValueError
        if deadline.astimezone(timezone.utc) <= current:
            errors.append("submission_deadline has passed")
    except ValueError:
        errors.append("submission_deadline must be ISO 8601 with an explicit UTC offset")
    for field in (
        "call_capture_sha256", "portal_capture_sha256", "abstract_sha256",
        "dissemination_handoff_sha256", "claim_registry_digest", "analysis_lock_digest",
    ):
        if not _is_nonzero_digest(payload.get(field)):
            errors.append(f"{field} must be a nonzero lowercase SHA-256")
    for prefix in ("call", "portal"):
        for suffix, canonical in (
            ("venue_series_id", "venue_series_id"),
            ("submission_cycle", "submission_cycle"),
            ("submission_type", "submission_type"),
        ):
            if payload.get(f"{prefix}_bound_{suffix}") != payload.get(canonical):
                errors.append(f"{prefix} evidence is not bound to exact {canonical}")
    if payload.get("content_owner") != "radiology-dissemination":
        errors.append("conference abstract content owner must remain radiology-dissemination")
    if payload.get("portal_owner") != "radiology-submission":
        errors.append("conference field/file finalization owner must be radiology-submission")
    for field in (
        "embargo_gate", "disclosure_gate", "privacy_gate", "rights_gate",
        "author_approval_gate",
    ):
        if payload.get(field) != "PASS":
            errors.append(f"{field} must be human-adjudicated PASS before portal handoff")
    if payload.get("review_scope") != "upload-root":
        errors.append("conference portal finalization requires an author-confirmed upload-root")
    if payload.get("human_final_action_status") != "PENDING":
        errors.append("human_final_action_status must remain PENDING; the machine cannot submit")
    return errors


def load_manifest(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    errors: list[str] = []
    if path.stat().st_size > MAX_CONTROL_BYTES:
        return [], [f"manifest exceeds {MAX_CONTROL_BYTES} bytes"]
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        if len({header.casefold() for header in headers}) != len(headers):
            errors.append("manifest has duplicate headers")
        if headers != MANIFEST_FIELDS:
            errors.append("manifest headers/order do not match conference schema 1.0")
        rows = list(reader)
    if not rows:
        errors.append("conference manifest has no field/file rows")
    return rows, errors


def validate_manifest_rows(
    intake: dict[str, Any], rows: list[dict[str, str]], root: Path,
    *, now: datetime | None = None, max_live_age_days: int = 7,
) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    current = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    item_ids: set[str] = set()
    manifest_files: dict[str, str] = {}
    abstract_bound = False
    for index, row in enumerate(rows, start=2):
        label = f"manifest line {index}"
        if list(row) != MANIFEST_FIELDS:
            errors.append(f"{label} has an invalid schema")
            continue
        item_id = _text(row.get("item_id"))
        folded_id = item_id.casefold()
        if not _is_concrete(item_id) or folded_id in item_ids:
            errors.append(f"{label} has a blank/placeholder/duplicate item_id")
        item_ids.add(folded_id)
        for field in ("venue_series_id", "submission_cycle", "submission_type"):
            if row.get(field) != _text(intake.get(field)):
                errors.append(f"{label} does not match intake {field}")
        if row.get("schema_version") != "1.0":
            errors.append(f"{label} schema_version must be 1.0")
        item_kind = row.get("item_kind", "")
        if item_kind not in ITEM_KINDS:
            errors.append(f"{label} has invalid item_kind")
        requirement = row.get("requirement_class", "")
        if requirement not in REQUIREMENT_CLASSES:
            errors.append(f"{label} has invalid requirement_class")
        if requirement == "conditional" and not _is_concrete(row.get("condition")):
            errors.append(f"{label} conditional row lacks a concrete condition")
        authority = row.get("authority_class", "")
        if authority not in AUTHORITY_CLASSES:
            errors.append(f"{label} has invalid authority_class")
        source_url = row.get("source_url", "")
        if not _https_url(source_url):
            errors.append(f"{label} lacks a concrete direct HTTPS source")
        if authority == "CURRENT_CALL" and source_url != _text(intake.get("current_call_url")):
            errors.append(f"{label} CURRENT_CALL source differs from frozen intake")
        if authority == "PORTAL_CURRENT" and source_url != _text(intake.get("portal_url")):
            errors.append(f"{label} PORTAL_CURRENT source differs from frozen intake")
        expected_day = (
            _text(intake.get("call_checked_on")) if authority == "CURRENT_CALL"
            else _text(intake.get("portal_checked_on"))
        )
        if authority in {"CURRENT_CALL", "PORTAL_CURRENT"} and row.get("verified_on") != expected_day:
            errors.append(f"{label} checked date differs from frozen live evidence")
        verified_day = _parse_day(row.get("verified_on"), f"{label} verified_on", errors)
        if verified_day is not None:
            age = (current.date() - verified_day).days
            if age < 0 or age > max_live_age_days:
                errors.append(f"{label} source verification is not current; reverify live")
        if not _is_concrete(row.get("material")) or not _is_concrete(row.get("portal_designation")):
            errors.append(f"{label} lacks material or exact portal designation")
        if not _is_concrete(row.get("version")):
            errors.append(f"{label} lacks a concrete frozen version")
        if not _is_concrete(row.get("source_artifact_id")):
            errors.append(f"{label} lacks source_artifact_id")
        if not _is_nonzero_digest(row.get("source_artifact_sha256")):
            errors.append(f"{label} lacks source_artifact_sha256")
        value_state = row.get("value_status", "")
        if value_state not in VALUE_STATES:
            errors.append(f"{label} has invalid value_status")
        if value_state == "NOT_APPLICABLE_WITH_HUMAN_RECEIPT":
            if requirement != "optional" or not all(
                token in row.get("notes", "")
                for token in ("na_attested_by=", "na_attested_on=", "na_basis=")
            ):
                errors.append(f"{label} N/A is limited to optional rows with a human receipt")
        for field in (
            "content_gate", "embargo_gate", "disclosure_gate", "privacy_gate", "rights_gate",
        ):
            if row.get(field) != "PASS":
                errors.append(f"{label} {field} must be PASS")
        if not _is_concrete(row.get("claim_boundary")):
            errors.append(f"{label} lacks an explicit claim boundary")
        if not _is_concrete(row.get("human_owner")):
            errors.append(f"{label} lacks an authorized human owner")

        relative = row.get("path", "")
        upload_digest = row.get("upload_sha256", "")
        observed_size: int | None = None
        if item_kind == "upload-file":
            if not _safe_relative_path(relative):
                errors.append(f"{label} upload path must be a safe POSIX-style relative path")
            else:
                folded_path = relative.casefold()
                if folded_path in manifest_files:
                    errors.append(f"{label} duplicates upload path {relative}")
                manifest_files[folded_path] = relative
                candidate = (root / Path(*PurePosixPath(relative).parts)).resolve(strict=False)
                try:
                    candidate.relative_to(root)
                except ValueError:
                    errors.append(f"{label} upload path escapes package root")
                else:
                    if not candidate.is_file() or is_linklike(candidate):
                        errors.append(f"{label} upload file is missing or link-mediated")
                    elif not _is_nonzero_digest(upload_digest):
                        errors.append(f"{label} upload_sha256 must be a nonzero lowercase SHA-256")
                    else:
                        observed, observed_size = bounded_sha256(candidate)
                        if observed != upload_digest:
                            errors.append(f"{label} upload_sha256 does not match current bytes")
            extension_tokens = [
                token.strip().casefold() for token in row.get("allowed_extensions", "").split(";")
                if token.strip()
            ]
            if (
                not extension_tokens
                or any(not re.fullmatch(r"\.[a-z0-9]{1,10}", token) for token in extension_tokens)
                or len(extension_tokens) != len(set(extension_tokens))
            ):
                errors.append(f"{label} upload file needs a unique source-backed extension allowlist")
            elif PurePosixPath(relative).suffix.casefold() not in extension_tokens:
                errors.append(f"{label} upload suffix is outside the source-backed allowlist")
            max_bytes_text = row.get("max_bytes", "").strip()
            if max_bytes_text:
                try:
                    max_bytes = int(max_bytes_text)
                    if max_bytes <= 0:
                        raise ValueError
                    if observed_size is not None and observed_size > max_bytes:
                        errors.append(f"{label} upload file exceeds max_bytes")
                except ValueError:
                    errors.append(f"{label} max_bytes must be a positive integer when supplied")
            if row.get("technical_qa") != "PASS" or row.get("render_qa") != "PASS":
                errors.append(f"{label} upload file requires technical_qa and render_qa PASS")
        else:
            if relative or upload_digest or row.get("allowed_extensions") or row.get("max_bytes"):
                errors.append(
                    f"{label} non-file row must not carry path, upload_sha256, allowed_extensions, or max_bytes"
                )
            if row.get("technical_qa") != "NOT_APPLICABLE" or row.get("render_qa") != "NOT_APPLICABLE":
                errors.append(f"{label} non-file row requires NOT_APPLICABLE technical/render QA")

        if (
            "conference abstract" in row.get("material", "").casefold()
            and row.get("source_artifact_id") == _text(intake.get("abstract_artifact_id"))
            and row.get("source_artifact_sha256") == _text(intake.get("abstract_sha256"))
        ):
            abstract_bound = True
    if not abstract_bound:
        errors.append("manifest lacks a conference abstract row bound to the frozen dissemination artifact")

    snapshot = inventory_snapshot(root)
    inventory_files = {record["path"].casefold(): record for record in snapshot["records"]}
    missing = sorted(set(manifest_files) - set(inventory_files))
    unmanifested = sorted(set(inventory_files) - set(manifest_files))
    if missing:
        errors.append(f"manifested upload files absent from inventory: {missing}")
    if unmanifested:
        errors.append(f"unmanifested files in upload root: {unmanifested}")
    return errors, snapshot


def audit_conference_portal(
    intake: dict[str, Any], rows: list[dict[str, str]], root: Path,
    *, now: datetime | None = None,
) -> dict[str, Any]:
    intake_errors = validate_intake(intake, now=now)
    manifest_errors: list[str] = []
    snapshot: dict[str, Any] = {"file_count": 0, "total_bytes": 0, "sha256": None, "records": []}
    if not intake_errors:
        manifest_errors, snapshot = validate_manifest_rows(intake, rows, root, now=now)
    errors = intake_errors + manifest_errors
    call_evidence_tokens = (
        "current call", "current_call", "call_checked_on", "call evidence", "submission_deadline",
    )
    if any(any(token in error for token in call_evidence_tokens) for error in errors):
        route_state = "CALL_EVIDENCE_UNVERIFIED"
    elif any("portal" in error.casefold() and "owner" not in error.casefold() for error in errors):
        route_state = "PORTAL_EVIDENCE_UNVERIFIED"
    elif errors:
        route_state = "PORTAL_PACKAGE_BLOCKED"
    else:
        route_state = "HUMAN_PORTAL_ACTION_REQUIRED"
    return {
        "schema_version": "1.0",
        "status": "PASS" if not errors else "FAIL",
        "route_state": route_state,
        "route_kind": "conference-portal-finalization",
        "content_owner": "radiology-dissemination",
        "portal_owner": "radiology-submission",
        "readiness_granted": False,
        "portal_action_performed": False,
        "human_final_action_required": True,
        "inventory": snapshot,
        "limitations": [
            "live captures and human attestations were not authenticated by this checker",
            "portal values were not entered or compared against a live logged-in session",
            "no upload, attestation, payment, submission, withdrawal, or acceptance action occurred",
            "PASS does not certify scientific validity, acceptance, publication, or embargo clearance",
        ],
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("intake", type=Path)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--package-root", required=True)
    args = parser.parse_args()
    try:
        root = authorized_package_root(args.package_root)
        intake_path = args.intake.resolve(strict=True)
        manifest_path = args.manifest.resolve(strict=True)
        for control in (intake_path, manifest_path):
            try:
                control.relative_to(root)
            except ValueError:
                pass
            else:
                raise ValueError("intake and manifest control files must remain outside the upload root")
        intake = load_json_strict(intake_path, max_bytes=MAX_CONTROL_BYTES)
        intake_root = authorized_package_root(_text(intake.get("package_root")))
        if os.path.normcase(str(intake_root)) != os.path.normcase(str(root)):
            raise ValueError("--package-root does not match the frozen intake package_root")
        rows, manifest_errors = load_manifest(manifest_path)
        report = audit_conference_portal(intake, rows, root)
        if manifest_errors:
            report["errors"] = manifest_errors + report["errors"]
            report["status"] = "FAIL"
            report["route_state"] = "PORTAL_PACKAGE_BLOCKED"
    except (OSError, ValueError, csv.Error, json.JSONDecodeError) as exc:
        report = {
            "schema_version": "1.0", "status": "FAIL",
            "route_state": "PORTAL_PACKAGE_BLOCKED",
            "route_kind": "conference-portal-finalization",
            "readiness_granted": False, "portal_action_performed": False,
            "human_final_action_required": True, "errors": [str(exc)],
        }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
