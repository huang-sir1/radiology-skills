#!/usr/bin/env python3
"""Fail-closed structural audit for a journal submission package.

This utility proves inventory and byte-level conditions only. It never certifies
scientific validity, visual quality, or live-portal completion.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import stat
import sys
import tarfile
import zipfile
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path
from typing import Iterable

from submission_security import (
    MAX_INVENTORY_FILE_BYTES,
    MAX_INVENTORY_FILES,
    MAX_INVENTORY_TOTAL_BYTES,
    authorized_package_root,
    bounded_sha256,
    inventory_snapshot,
)


SCHEMA_VERSION = "2.5"
REQUIRED_HEADER_ORDER = [
    "schema_version", "project_id", "study_scope", "project_state_digest",
    "modality_role_digest", "scientific_handoff_packet_digest",
    "scientific_prereview_receipt_digest", "source_artifact_id", "analysis_lock_digest",
    "claim_registry_digest", "response_package_digest", "item_id", "journal_id",
    "article_type", "submission_stage",
    "study_design", "review_model", "material", "requirement_class", "condition", "rule_id", "authority_class",
    "source_url", "guide_verified_on", "path", "expected_extensions", "version",
    "sha256", "blinded", "tracked_changes_policy", "revision_variant", "status",
    "technical_qa", "render_qa", "content_gate", "anonymization_qa", "crossfile_qa",
    "owner", "not_applicable_reason", "notes",
]
REQUIRED_HEADERS = set(REQUIRED_HEADER_ORDER)
EVIDENCE_HEADER_ORDER = [
    "journal_id", "rule_id", "article_type", "stage", "authority_class",
    "requirement_class", "condition", "material", "rule_summary",
    "allowed_extensions", "source_url", "checked_on", "verification_status",
    "applicable_stages",
]
REQUIREMENT_CLASSES = {"required", "conditional", "optional", "portal-only"}
AUTHORITY_CLASSES = {
    "JOURNAL_GUIDE", "PORTAL_CURRENT", "OFFICIAL_FORM", "PUBLISHER_POLICY",
    "REPORTING_STANDARD", "PUBLISHED_EXEMPLAR", "SECONDARY_SUMMARY",
    "PORTAL_PLACEHOLDER",
}
HARD_RULE_AUTHORITIES = {
    "JOURNAL_GUIDE", "PORTAL_CURRENT", "OFFICIAL_FORM", "PUBLISHER_POLICY",
}
STATUSES = {
    "ready", "pending-author", "pending-guide", "blocked-upstream",
    "not-applicable", "portal-entry",
}
QA_STATES = {"pass", "fail", "not-checked", "not-applicable", "unverified", "unavailable"}
STAGES = {"initial", "pre-review", "revision", "transfer", "final-files"}
TRACKED_CHANGE_POLICIES = {"prohibited", "allowed-marked-revision", "not-applicable"}
REVISION_VARIANTS = {"not-applicable", "clean", "marked", "response", "cover", "other-revision"}
STUDY_DESIGNS = {
    "randomized-trial", "nonrandomized-intervention", "observational", "diagnostic-accuracy",
    "prognostic-prediction", "medical-ai", "systematic-review-meta-analysis",
    "qualitative-mixed-methods", "oncology-biomarker", "animal-preclinical",
    "software-methods", "other",
}
STUDY_SCOPES = {"imaging-only", "mechanism-only", "imaging-mechanism", "evidence-synthesis"}
REVIEW_MODELS = {"single-anonymized", "double-anonymized", "not-confirmed"}
PROJECT_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{2,127}$")
ARTIFACT_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{1,127}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def is_nonzero_sha256(value: str) -> bool:
    return bool(SHA256_RE.fullmatch(value)) and set(value) != {"0"}
JOURNAL_REVIEW_MODELS = {
    "radiology": {"double-anonymized"},
    "nature-medicine": {"single-anonymized", "double-anonymized"},
    "nature-communications": {"single-anonymized", "double-anonymized"},
    "lancet-digital-health": {"single-anonymized"},
    "eclinicalmedicine": {"single-anonymized"},
    "cancer-cell": {"single-anonymized"},
    "cell-reports-medicine": {"single-anonymized"},
    "npj-digital-medicine": {"single-anonymized"},
    "npj-precision-oncology": {"single-anonymized"},
    "advanced-science": {"not-confirmed"},
    "jama-network-open": {"single-anonymized"},
}
HUMAN_STUDY_DESIGNS = STUDY_DESIGNS - {"animal-preclinical", "software-methods", "other"}
CONDITION_DESIGN_TRIGGERS = {
    "clinical trial": {"randomized-trial", "nonrandomized-intervention"},
    "randomized or nonrandomized clinical trial": {"randomized-trial", "nonrandomized-intervention"},
    "trial or systematic review": {
        "randomized-trial", "nonrandomized-intervention", "systematic-review-meta-analysis",
    },
    "medical ai study": {"medical-ai"},
    "machine-learning research": {"medical-ai", "software-methods"},
    "biological or biomedical research": {
        "randomized-trial", "nonrandomized-intervention", "observational", "diagnostic-accuracy",
        "prognostic-prediction", "medical-ai", "oncology-biomarker", "animal-preclinical",
    },
    "declared study type matches a reporting standard": STUDY_DESIGNS - {"other"},
    "human study design matches a named guideline": HUMAN_STUDY_DESIGNS,
    "relevant life-science or clinical research": STUDY_DESIGNS - {"other"},
    "relevant life-science or oncology research": STUDY_DESIGNS - {"other"},
    "relevant life-science research": STUDY_DESIGNS - {"other"},
    "relevant research": STUDY_DESIGNS - {"other"},
}
INVENTORY_BLOCK_CODES = {
    "MANIFEST_ESCAPE", "MANIFEST_SYMLINK", "MANIFEST_READ", "MANIFEST_SIZE", "HEADERS",
    "DUPLICATE_HEADERS", "ROW_WIDTH", "EMPTY_MANIFEST",
    "PACKAGE_LIMIT", "PACKAGE_SNAPSHOT",
    "SYMLINK", "ITEM_ID", "ITEM_DUP", "PATH_ESCAPE", "PATH_SYMLINK", "FILE_PATH",
    "FILE_MISSING", "NOT_FILE", "PATH_DUP", "UNMANIFESTED_FILE", "ACTUAL_PATH_ESCAPE",
    "ABSOLUTE_PATH", "NONCANONICAL_PATH", "MANIFEST_AS_UPLOAD",
}
TRUE_VALUES = {"1", "true", "yes", "y"}
FALSE_VALUES = {"0", "false", "no", "n"}
BLINDED_VALUES = TRUE_VALUES | FALSE_VALUES | {"not-applicable"}
MAX_TEXT_SCAN_BYTES = 25_000_000
PLACEHOLDER_RE = re.compile(
    r"(?:TODO|TBD|AUTHOR_INPUT_NEEDED|VERIFY_FROM_CURRENT_GUIDE|"
    r"UNVERIFIED_CURRENT_GUIDE|\[INSERT[^\]]*\]|\bTO CONFIRM\b)", re.I,
)
TEMP_NAME_RE = re.compile(
    r"(?:^~\$|(?:\.tmp|\.temp|\.bak|\.autosave|\.swp|\.part|\.old)$)", re.I,
)
TEXT_SUFFIXES = {
    ".txt", ".md", ".tex", ".csv", ".tsv", ".json", ".yaml", ".yml",
    ".xml", ".rtf", ".svg", ".html", ".htm", ".owl", ".sbml",
}
EXPECTED_TYPES = {
    ".pdf": {"pdf"}, ".docx": {"docx"}, ".xlsx": {"xlsx"}, ".pptx": {"pptx"},
    ".zip": {"zip"}, ".png": {"png"}, ".jpg": {"jpeg"}, ".jpeg": {"jpeg"},
    ".tif": {"tiff"}, ".tiff": {"tiff"}, ".eps": {"eps", "postscript"},
    ".ai": {"pdf", "eps", "postscript"}, ".psd": {"psd"}, ".bmp": {"bmp"},
    # Legacy OLE Office files require a format-aware compound-document parser.
    # A stream-name byte search is not sufficient to certify that a .doc/.xls/.ppt
    # is structurally valid, so these expected types are deliberately unreachable
    # unless a future verified adapter is added.
    ".gif": {"gif"}, ".doc": {"ole-word-verified"}, ".xls": {"ole-excel-verified"},
    ".ppt": {"ole-powerpoint-verified"},
    ".mp4": {"mp4"}, ".m4v": {"mp4"}, ".mov": {"quicktime"}, ".mp3": {"mp3"},
    ".wav": {"wav"}, ".avi": {"avi"}, ".wmv": {"wmv"}, ".mpg": {"mpeg"},
    ".mpeg": {"mpeg"}, ".swf": {"swf"}, ".emf": {"emf"}, ".wmf": {"wmf"},
    ".gz": {"gzip"}, ".tgz": {"gzip"}, ".tar": {"tar"}, ".wpd": {"wordperfect"},
    ".ps": {"postscript"},
}

BUNDLED_EVIDENCE_PATH = (
    Path(__file__).resolve().parents[1] / "references" / "journal-requirements-evidence.tsv"
)
BUNDLED_ROUTE_MATRIX_PATH = (
    Path(__file__).resolve().parents[1] / "references" / "journal-required-materials.json"
)
EVIDENCE_REFRESH_MUTABLE_FIELDS = {"checked_on", "verification_status"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package_dir", help="Explicit submission-package root")
    parser.add_argument("--manifest", default="submission-manifest.csv")
    parser.add_argument(
        "--evidence",
        default=str(BUNDLED_EVIDENCE_PATH),
        help=(
            "Machine-readable current rule registry. In submission mode a task-local refresh may "
            "change only checked_on/verification_status; rule substance remains bound to the "
            "validated bundled registry."
        ),
    )
    parser.add_argument(
        "--route-matrix",
        default=str(BUNDLED_ROUTE_MATRIX_PATH),
        help="Minimum journal/article/stage material contract matrix",
    )
    parser.add_argument("--submission-mode", action="store_true")
    parser.add_argument(
        "--scope", choices=("upload-root", "attachment-set", "partial"), default="partial",
        help=(
            "Declared inventory scope. Only upload-root can support a whole-package readiness hint; "
            "attachment-set and partial remain package-incomplete (safe default: partial)"
        ),
    )
    parser.add_argument("--as-of", help="Audit date YYYY-MM-DD; defaults to today")
    parser.add_argument(
        "--max-guide-age-days", type=int, default=30,
        help="Maximum age of decisive rule verification in submission mode (default: 30)",
    )
    return parser.parse_args()


def load_evidence_registry(path: Path) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if (reader.fieldnames or []) != EVIDENCE_HEADER_ORDER:
            raise ValueError("Evidence registry must use the exact ordered schema including applicable_stages")
        rows = list(reader)
    registry: dict[str, dict[str, str]] = {}
    for row in rows:
        rule_id = (row.get("rule_id") or "").strip()
        if not rule_id or rule_id in registry:
            raise ValueError(f"Invalid or duplicate rule_id in evidence registry: {rule_id or '[blank]'}")
        registry[rule_id] = row
    return registry


def load_validated_evidence_registry(
    path: Path, bundled_path: Path,
) -> tuple[dict[str, dict[str, str]], dict[str, object]]:
    """Load evidence and constrain task-local refreshes to provenance-only changes.

    The route contract is maintained and regression-tested with the bundled rule
    substance.  A caller may refresh the verification date/status after checking
    the same source, but may not use --evidence to rewrite journal, stage,
    requirement, file type, authority, source, or rule meaning.
    """
    registry = load_evidence_registry(path)
    baseline = load_evidence_registry(bundled_path)
    custom = path != bundled_path
    if custom:
        if set(registry) != set(baseline):
            missing = sorted(set(baseline) - set(registry))
            extra = sorted(set(registry) - set(baseline))
            raise ValueError(
                "Evidence refresh must preserve the complete bundled rule set "
                f"(missing={missing}, extra={extra})"
            )
        immutable_fields = [
            field for field in EVIDENCE_HEADER_ORDER
            if field not in EVIDENCE_REFRESH_MUTABLE_FIELDS
        ]
        for rule_id, row in registry.items():
            baseline_row = baseline[rule_id]
            changed = [
                field for field in immutable_fields
                if (row.get(field) or "") != (baseline_row.get(field) or "")
            ]
            if changed:
                raise ValueError(
                    f"Evidence refresh rewrites validated rule substance for {rule_id}: {changed}; "
                    "update the bundled registry and run maintainer validation instead"
                )
    for rule_id, row in registry.items():
        if parse_iso_date((row.get("checked_on") or "").strip()) is None:
            raise ValueError(f"Evidence rule {rule_id} has invalid checked_on")
        if row.get("verification_status") not in {
            "VERIFIED_CURRENT", "UNVERIFIED_CURRENT", "OBSERVED_ONLY",
        }:
            raise ValueError(f"Evidence rule {rule_id} has invalid verification_status")
    return registry, {
        "path": str(path),
        "sha256": sha256_file(path),
        "bundled_path": str(bundled_path),
        "bundled_sha256": sha256_file(bundled_path),
        "custom_refresh": custom,
        "substance_bound_to_bundled_registry": True,
        "mutable_refresh_fields": sorted(EVIDENCE_REFRESH_MUTABLE_FIELDS),
    }


def load_route_matrix(path: Path) -> list[dict[str, object]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != "1.0" or not isinstance(payload.get("routes"), list):
        raise ValueError("Route matrix schema must be 1.0 with a routes list")
    return payload["routes"]


def source_route_allowed(journal_id: str, source_url: str) -> bool:
    """Accept only a live portal route bound to the exact target journal.

    Publisher-level host checks are insufficient because several journals share
    Editorial Manager or Springer Nature infrastructure.  An unrelated journal's
    portal must never resolve a target journal's otherwise-unverified rule.
    """
    from urllib.parse import urlparse

    parsed = urlparse(source_url)
    if parsed.scheme.lower() != "https" or parsed.username or parsed.password:
        return False
    host = (parsed.hostname or "").lower()
    try:
        if parsed.port not in {None, 443}:
            return False
    except ValueError:
        return False
    raw_path = parsed.path
    path_segments = raw_path.replace("\\", "/").split("/")
    if "\\" in raw_path or "%" in raw_path or any(segment in {".", ".."} for segment in path_segments):
        return False
    path = "/" + parsed.path.lstrip("/").casefold()
    exact_routes = {
        "radiology": lambda: host == "mc.manuscriptcentral.com" and (path == "/rad" or path.startswith("/rad/")),
        "nature-medicine": lambda: host == "mts-nmed.nature.com",
        "nature-communications": lambda: host == "mts-ncomms.nature.com",
        "npj-digital-medicine": lambda: (
            host == "submission.springernature.com"
            and path.startswith("/new-submission/41746/")
        ),
        "npj-precision-oncology": lambda: (
            host == "submission.springernature.com"
            and path.startswith("/new-submission/41698/")
        ),
        # The public TLDH and eClinicalMedicine Editorial Manager pages explicitly
        # say "Site under development" at the 2026-08-22 snapshot. No live route
        # is accepted until an official working instance is captured. Decision letters
        # require separate human adjudication and cannot masquerade as PORTAL_CURRENT.
        "jama-network-open": lambda: host == "manuscripts.jamanetworkopen.com",
    }
    predicate = exact_routes.get(journal_id)
    return bool(predicate and predicate())


def add_finding(
    findings: list[dict[str, object]], severity: str, code: str, message: str,
    *, item_id: str = "", path: str = "",
) -> None:
    finding: dict[str, object] = {"severity": severity, "code": code, "message": message}
    if item_id:
        finding["item_id"] = item_id
    if path:
        finding["path"] = path
    findings.append(finding)


def parse_iso_date(value: str) -> date | None:
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return None


def structured_note_fields(notes: str) -> dict[str, str]:
    """Parse semicolon-delimited key=value provenance fields from manifest notes."""
    fields: dict[str, str] = {}
    duplicate_keys: list[str] = []
    for segment in notes.split(";"):
        if "=" not in segment:
            continue
        key, value = segment.split("=", 1)
        normalized_key = key.strip().lower()
        if not normalized_key:
            continue
        if normalized_key in fields:
            duplicate_keys.append(normalized_key)
            continue
        fields[normalized_key] = value.strip()
    if duplicate_keys:
        fields["__duplicate_receipt_keys__"] = ",".join(sorted(set(duplicate_keys)))
    return fields


def portal_receipt_issues(row: dict[str, str]) -> list[str]:
    """Validate a provenance receipt for an exact-journal live-portal observation.

    The receipt binds the observation to a capture artifact hash and the exact
    journal/article/stage screen. Authenticity and private-locator access remain
    human gates, but a free-form note can no longer self-authorize a portal rule.
    """
    fields = structured_note_fields((row.get("notes") or "").strip())
    required = {
        "portal_capture_sha256", "portal_capture_date", "portal_journal_id",
        "portal_article_type", "portal_stage", "portal_screen", "portal_locator",
    }
    missing = sorted(required - fields.keys())
    issues: list[str] = []
    if fields.get("__duplicate_receipt_keys__"):
        issues.append("duplicate receipt keys: " + fields["__duplicate_receipt_keys__"])
    if missing:
        issues.append("missing " + ", ".join(missing))
    capture_sha = fields.get("portal_capture_sha256", "")
    if capture_sha and (
        not re.fullmatch(r"[0-9a-fA-F]{64}", capture_sha)
        or capture_sha == "0" * 64
    ):
        issues.append("portal_capture_sha256 is not a nonzero SHA-256")
    capture_date = fields.get("portal_capture_date", "")
    if capture_date and parse_iso_date(capture_date) is None:
        issues.append("portal_capture_date is not YYYY-MM-DD")
    if capture_date and capture_date != (row.get("guide_verified_on") or "").strip():
        issues.append("portal_capture_date does not match guide_verified_on")
    bindings = {
        "portal_journal_id": (row.get("journal_id") or "").strip(),
        "portal_article_type": (row.get("article_type") or "").strip(),
        "portal_stage": (row.get("submission_stage") or "").strip().lower(),
    }
    for key, expected in bindings.items():
        observed = fields.get(key, "")
        if observed and observed != expected:
            issues.append(f"{key}={observed!r} does not bind to {expected!r}")
    for key in ("portal_screen", "portal_locator"):
        value = fields.get(key, "")
        if value and (len(value) < 5 or PLACEHOLDER_RE.search(value)):
            issues.append(f"{key} is empty, too vague, or a placeholder")
    return issues


def conditional_na_attestation_issues(
    row: dict[str, str], audit_date: date, max_age_days: int,
) -> list[str]:
    """Bind a conditional N/A decision to a dated human attestation.

    The receipt does not prove that the scientific condition is absent. It makes
    the responsible human decision explicit and prevents an arbitrary free-text
    reason from silently closing a route requirement.
    """
    fields = structured_note_fields((row.get("notes") or "").strip())
    required = {
        "na_attested_by", "na_attested_on", "na_rule_id", "na_basis",
        "na_decision_locator",
    }
    missing = sorted(required - fields.keys())
    issues: list[str] = []
    if fields.get("__duplicate_receipt_keys__"):
        issues.append("duplicate receipt keys: " + fields["__duplicate_receipt_keys__"])
    if missing:
        issues.append("missing " + ", ".join(missing))
    attested_on = parse_iso_date(fields.get("na_attested_on", ""))
    if fields.get("na_attested_on") and attested_on is None:
        issues.append("na_attested_on is not YYYY-MM-DD")
    elif attested_on is not None:
        age = (audit_date - attested_on).days
        if age < 0 or age > max_age_days:
            issues.append(f"na_attested_on is outside the 0-{max_age_days} day audit window")
    if fields.get("na_rule_id", "") != (row.get("rule_id") or "").strip():
        issues.append("na_rule_id does not bind to rule_id")
    reason = (row.get("not_applicable_reason") or "").strip()
    if fields.get("na_basis", "") != reason:
        issues.append("na_basis does not exactly match not_applicable_reason")
    for key in ("na_attested_by", "na_decision_locator"):
        value = fields.get(key, "")
        if value and (len(value) < 5 or PLACEHOLDER_RE.search(value)):
            issues.append(f"{key} is empty, too vague, or a placeholder")
    return issues


def marked_unmarked_pair_receipt_issues(
    assertion_row: dict[str, str], all_rows: list[dict[str, str]],
    allowed_parent_rule_ids: set[str],
) -> list[str]:
    """Validate a path-free human assertion that cross-links two upload files.

    File identity and hashes are machine checked. Whether the two images depict the
    same underlying image and differ only by authorized markers remains a rendered
    human cross-file judgment represented by crossfile_qa=pass.
    """
    fields = structured_note_fields((assertion_row.get("notes") or "").strip())
    required = {
        "figure_pair_id", "marked_item_id", "unmarked_item_id",
        "marked_sha256", "unmarked_sha256", "pair_review_locator",
    }
    missing = sorted(required - fields.keys())
    issues: list[str] = []
    if fields.get("__duplicate_receipt_keys__"):
        issues.append("duplicate receipt keys: " + fields["__duplicate_receipt_keys__"])
    if missing:
        issues.append("missing " + ", ".join(missing))
    pair_id = fields.get("figure_pair_id", "")
    locator = fields.get("pair_review_locator", "")
    if pair_id and (len(pair_id) < 2 or PLACEHOLDER_RE.search(pair_id)):
        issues.append("figure_pair_id is empty, too vague, or a placeholder")
    if locator and (len(locator) < 5 or PLACEHOLDER_RE.search(locator)):
        issues.append("pair_review_locator is empty, too vague, or a placeholder")
    marked_id = fields.get("marked_item_id", "")
    unmarked_id = fields.get("unmarked_item_id", "")
    if marked_id and unmarked_id and marked_id == unmarked_id:
        issues.append("marked_item_id and unmarked_item_id must differ")
    rows_by_item = {
        (row.get("item_id") or "").strip(): row for row in all_rows
        if (row.get("item_id") or "").strip()
    }
    pair_rows: list[tuple[str, dict[str, str] | None, str]] = [
        ("marked", rows_by_item.get(marked_id), fields.get("marked_sha256", "")),
        ("unmarked", rows_by_item.get(unmarked_id), fields.get("unmarked_sha256", "")),
    ]
    observed_hashes: list[str] = []
    for role, row, receipt_sha in pair_rows:
        if row is None:
            if (marked_id if role == "marked" else unmarked_id):
                issues.append(f"{role}_item_id does not resolve to a manifest row")
            continue
        observed_sha = (row.get("sha256") or "").strip().lower()
        observed_hashes.append(observed_sha)
        if (
            not re.fullmatch(r"[0-9a-fA-F]{64}", receipt_sha or "")
            or receipt_sha == "0" * 64
            or receipt_sha.lower() != observed_sha
        ):
            issues.append(f"{role}_sha256 does not bind to the referenced manifest row")
        if not (row.get("path") or "").strip() or (row.get("status") or "").strip().lower() != "ready":
            issues.append(f"{role} item is not a ready physical upload file")
        if (row.get("rule_id") or "").strip() not in allowed_parent_rule_ids:
            issues.append(f"{role} item is outside the allowed figure route")
        if (row.get("crossfile_qa") or "").strip().lower() != "pass":
            issues.append(f"{role} item crossfile_qa is not pass")
    if len(observed_hashes) == 2 and observed_hashes[0] == observed_hashes[1]:
        issues.append("marked and unmarked files have identical SHA-256")
    if (assertion_row.get("content_gate") or "").strip().lower() != "pass":
        issues.append("pair assertion content_gate is not pass")
    if (assertion_row.get("crossfile_qa") or "").strip().lower() != "pass":
        issues.append("pair assertion crossfile_qa is not pass")
    return issues


def latex_source_receipt_issues(rows: list[dict[str, str]]) -> list[str]:
    """Require one mutually hash-bound TeX/PDF pair plus external receipt hashes.

    This proves provenance fields are internally coherent. It does not authenticate
    the external dependency manifest/compile receipt or replace isolated compilation
    and rendered source-to-PDF review.
    """
    tex_rows = [row for row in rows if Path((row.get("path") or "").strip()).suffix.lower() == ".tex"]
    pdf_rows = [row for row in rows if Path((row.get("path") or "").strip()).suffix.lower() == ".pdf"]
    if not tex_rows or not pdf_rows:
        return ["LaTeX route requires at least one .tex source and one checked .pdf"]
    receipt_hash_keys = {
        "latex_source_set_sha256", "latex_dependency_manifest_sha256",
        "latex_compile_receipt_sha256",
    }
    locator_keys = {"latex_dependency_manifest_locator", "latex_compile_receipt_locator"}
    for tex_row in tex_rows:
        tex_fields = structured_note_fields((tex_row.get("notes") or "").strip())
        tex_sha = (tex_row.get("sha256") or "").strip().lower()
        for pdf_row in pdf_rows:
            pdf_fields = structured_note_fields((pdf_row.get("notes") or "").strip())
            if tex_fields.get("__duplicate_receipt_keys__") or pdf_fields.get("__duplicate_receipt_keys__"):
                continue
            pdf_sha = (pdf_row.get("sha256") or "").strip().lower()
            if tex_fields.get("latex_checked_pdf_sha256", "").lower() != pdf_sha:
                continue
            if pdf_fields.get("latex_source_tex_sha256", "").lower() != tex_sha:
                continue
            if any(tex_fields.get(key, "").lower() != pdf_fields.get(key, "").lower() for key in receipt_hash_keys):
                continue
            if any(tex_fields.get(key, "") != pdf_fields.get(key, "") for key in locator_keys):
                continue
            all_fields = {**tex_fields, **pdf_fields}
            hash_values = [all_fields.get(key, "") for key in receipt_hash_keys]
            if any(
                not re.fullmatch(r"[0-9a-fA-F]{64}", value or "") or value == "0" * 64
                for value in hash_values
            ):
                continue
            if any(
                len(all_fields.get(key, "")) < 5 or PLACEHOLDER_RE.search(all_fields.get(key, ""))
                for key in locator_keys
            ):
                continue
            return []
    return [
        "no .tex/.pdf pair has mutually bound file hashes plus matching nonzero source-set, "
        "dependency-manifest and compile-receipt SHA-256/locator fields"
    ]


def sha256_file(path: Path) -> str:
    return bounded_sha256(path)[0]


def normalized_rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def is_linklike(path: Path) -> bool:
    if path.is_symlink():
        return True
    is_junction = getattr(path, "is_junction", None)
    if is_junction and is_junction():
        return True
    try:
        attributes = getattr(path.lstat(), "st_file_attributes", 0)
    except OSError:
        return False
    return bool(attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400))


def enumerate_package(root: Path) -> tuple[list[Path], list[Path]]:
    files: list[Path] = []
    symlinks: list[Path] = []
    total_bytes = 0
    for current, dirs, names in os.walk(root, topdown=True, followlinks=False):
        current_path = Path(current)
        kept_dirs: list[str] = []
        for name in dirs:
            candidate = current_path / name
            if is_linklike(candidate):
                symlinks.append(candidate)
            else:
                kept_dirs.append(name)
        dirs[:] = kept_dirs
        for name in names:
            candidate = current_path / name
            if is_linklike(candidate):
                symlinks.append(candidate)
            elif candidate.is_file():
                size = candidate.stat().st_size
                if size > MAX_INVENTORY_FILE_BYTES:
                    raise ValueError(
                        f"{normalized_rel(candidate, root)} exceeds the "
                        f"{MAX_INVENTORY_FILE_BYTES}-byte audit limit"
                    )
                files.append(candidate)
                total_bytes += size
                if len(files) > MAX_INVENTORY_FILES:
                    raise ValueError(f"package exceeds {MAX_INVENTORY_FILES} files")
                if total_bytes > MAX_INVENTORY_TOTAL_BYTES:
                    raise ValueError(f"package exceeds the {MAX_INVENTORY_TOTAL_BYTES}-byte audit limit")
    return sorted(files, key=lambda p: normalized_rel(p, root).casefold()), symlinks


def has_symlink_component(root: Path, candidate: Path) -> bool:
    try:
        relative = candidate.relative_to(root)
    except ValueError:
        return True
    cursor = root
    for part in relative.parts:
        cursor = cursor / part
        if is_linklike(cursor):
            return True
    return False


def detect_file_type(path: Path) -> tuple[str, str]:
    """Return the observed container/signature type and a short explanation."""
    try:
        with path.open("rb") as handle:
            head = handle.read(512)
    except OSError as exc:
        return "unreadable", str(exc)
    if head.startswith(b"%PDF-"):
        return "pdf", "PDF signature"
    if head.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png", "PNG signature"
    if head.startswith(b"\xff\xd8\xff"):
        return "jpeg", "JPEG signature"
    if head.startswith((b"II*\x00", b"MM\x00*")):
        return "tiff", "TIFF signature"
    if head.startswith(b"8BPS"):
        return "psd", "Photoshop signature"
    if head.startswith(b"BM"):
        return "bmp", "BMP signature"
    if head.startswith((b"GIF87a", b"GIF89a")):
        return "gif", "GIF signature"
    if head.startswith(b"ID3") or head.startswith((b"\xff\xfb", b"\xff\xf3", b"\xff\xf2")):
        return "mp3", "MP3 signature"
    if head.startswith(b"RIFF") and head[8:12] == b"WAVE":
        return "wav", "RIFF/WAVE signature"
    if head.startswith(b"RIFF") and head[8:12] == b"AVI ":
        return "avi", "RIFF/AVI signature"
    if head.startswith(b"\x30\x26\xb2\x75\x8e\x66\xcf\x11\xa6\xd9\x00\xaa\x00\x62\xce\x6c"):
        return "wmv", "ASF/WMV signature"
    if head.startswith((b"\x00\x00\x01\xba", b"\x00\x00\x01\xb3")):
        return "mpeg", "MPEG signature"
    if head.startswith((b"FWS", b"CWS", b"ZWS")):
        return "swf", "SWF signature"
    if len(head) >= 44 and head[40:44] == b" EMF":
        return "emf", "Enhanced Metafile signature"
    if head.startswith(b"\xd7\xcd\xc6\x9a"):
        return "wmf", "Placeable Windows Metafile signature"
    if head.startswith(b"\x1f\x8b"):
        return "gzip", "GZIP signature"
    if len(head) >= 262 and head[257:262] == b"ustar":
        return "tar", "TAR signature"
    if head.startswith(b"\xffWPC"):
        return "wordperfect", "WordPerfect signature"
    if head.startswith(b"%!PS-Adobe"):
        return "eps" if b"EPSF" in head else "postscript", "PostScript signature"
    if head.startswith(b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"):
        return "ole-unverified", "Legacy OLE container; no format-aware compound-document parser"
    if len(head) >= 12 and head[4:8] == b"ftyp":
        return ("quicktime", "ISO BMFF QuickTime brand") if head[8:12] == b"qt  " else ("mp4", "ISO BMFF/MP4 signature")
    if head.startswith((b"PK\x03\x04", b"PK\x05\x06")):
        try:
            with zipfile.ZipFile(path) as archive:
                names = set(archive.namelist())
                if "word/document.xml" in names:
                    return "docx", "OOXML Word container"
                if "xl/workbook.xml" in names:
                    return "xlsx", "OOXML Excel container"
                if "ppt/presentation.xml" in names:
                    return "pptx", "OOXML PowerPoint container"
                return "zip", "ZIP container"
        except (OSError, zipfile.BadZipFile):
            return "invalid-zip", "ZIP signature but invalid container"
    if path.suffix.lower() in TEXT_SUFFIXES:
        try:
            strict_text_payload(path)
            return "text", "Complete bounded UTF-8 text payload"
        except (OSError, UnicodeError, ValueError) as exc:
            return "binary-text-extension", f"Text extension but unsafe/non-UTF payload ({type(exc).__name__})"
    return "unknown", "No recognized signature"


def archive_features(path: Path) -> dict[str, object]:
    result: dict[str, object] = {
        "encrypted": False, "unsafe_names": [], "symlink_entries": [], "bad_member": "",
        "bomb_risk": False, "integrity_skipped": False, "unsupported": False,
        "duplicate_names": [], "case_collisions": [], "canonical_collisions": [],
    }
    try:
        with zipfile.ZipFile(path) as archive:
            infos = archive.infolist()
            member_names = [getattr(info, "orig_filename", info.filename) for info in infos]
            name_counts: defaultdict[str, int] = defaultdict(int)
            case_groups: defaultdict[str, set[str]] = defaultdict(set)
            canonical_groups: defaultdict[str, set[str]] = defaultdict(set)
            for member_name in member_names:
                name_counts[member_name] += 1
                case_groups[member_name.casefold()].add(member_name)
                canonical = "/".join(
                    part for part in member_name.replace("\\", "/").split("/")
                    if part not in {"", "."}
                )
                canonical_groups[canonical.casefold()].add(member_name)
            result["duplicate_names"] = sorted(name for name, count in name_counts.items() if count > 1)
            result["case_collisions"] = sorted(
                sorted(group) for group in case_groups.values() if len(group) > 1
            )
            result["canonical_collisions"] = sorted(
                sorted(group) for group in canonical_groups.values() if len(group) > 1
            )
            total_uncompressed = sum(info.file_size for info in infos)
            if len(infos) > 10_000 or total_uncompressed > 2_000_000_000:
                result["bomb_risk"] = True
            for info in infos:
                if info.flag_bits & 0x1:
                    result["encrypted"] = True
                if info.file_size > 1_000_000_000 or (
                    info.compress_size > 0 and info.file_size > 100_000_000
                    and info.file_size / info.compress_size > 200
                ):
                    result["bomb_risk"] = True
                raw_name = getattr(info, "orig_filename", info.filename)
                normalized = raw_name.replace("\\", "/")
                raw_parts = normalized.split("/")
                parts = [part for part in raw_parts if part not in {"", "."}]
                has_internal_empty = "" in raw_parts[1:-1]
                if (
                    "\\" in raw_name or normalized.startswith(("/", "\\"))
                    or (parts and ":" in parts[0]) or any(part in {".", ".."} for part in raw_parts)
                    or has_internal_empty
                ):
                    result["unsafe_names"].append(info.filename)  # type: ignore[union-attr]
                unix_mode = (info.external_attr >> 16) & 0o170000
                if unix_mode == 0o120000:
                    result["symlink_entries"].append(info.filename)  # type: ignore[union-attr]
            if result["bomb_risk"] or total_uncompressed > 100_000_000:
                result["integrity_skipped"] = True
            else:
                result["bad_member"] = archive.testzip() or ""
    except (NotImplementedError, RuntimeError, ValueError) as exc:
        result["unsupported"] = True
        result["unsupported_detail"] = type(exc).__name__
    except (OSError, zipfile.BadZipFile):
        result["invalid"] = True
    return result


def tar_archive_features(path: Path) -> dict[str, object]:
    """Inspect an uncompressed TAR without extracting or opening member payloads."""
    result: dict[str, object] = {
        "unsafe_names": [], "link_entries": [], "special_entries": [],
        "duplicate_names": [], "case_collisions": [], "canonical_collisions": [],
        "bomb_risk": False, "unsupported": False, "invalid": False,
    }
    try:
        name_counts: defaultdict[str, int] = defaultdict(int)
        case_groups: defaultdict[str, set[str]] = defaultdict(set)
        canonical_groups: defaultdict[str, set[str]] = defaultdict(set)
        total_size = 0
        member_count = 0
        # Stream mode never retains an unbounded TarInfo list and never extracts.
        with tarfile.open(path, mode="r|") as archive:
            for member in archive:
                member_count += 1
                if member_count > 10_000:
                    result["bomb_risk"] = True
                    break
                raw_name = member.name
                normalized = raw_name.replace("\\", "/")
                raw_parts = normalized.split("/")
                parts = [part for part in raw_parts if part not in {"", "."}]
                canonical = "/".join(parts)
                name_counts[raw_name] += 1
                case_groups[raw_name.casefold()].add(raw_name)
                canonical_groups[canonical.casefold()].add(raw_name)
                has_internal_empty = "" in raw_parts[1:-1]
                if (
                    "\\" in raw_name or normalized.startswith(("/", "\\"))
                    or (parts and ":" in parts[0]) or any(part in {".", ".."} for part in raw_parts)
                    or has_internal_empty
                ):
                    result["unsafe_names"].append(raw_name)  # type: ignore[union-attr]
                if member.issym() or member.islnk():
                    result["link_entries"].append(raw_name)  # type: ignore[union-attr]
                if member.ischr() or member.isblk() or member.isfifo() or member.isdev():
                    result["special_entries"].append(raw_name)  # type: ignore[union-attr]
                total_size += max(0, int(member.size))
                if member.size > 1_000_000_000 or total_size > 2_000_000_000:
                    result["bomb_risk"] = True
                    break
        result["duplicate_names"] = sorted(name for name, count in name_counts.items() if count > 1)
        result["case_collisions"] = sorted(
            sorted(group) for group in case_groups.values() if len(group) > 1
        )
        result["canonical_collisions"] = sorted(
            sorted(group) for group in canonical_groups.values() if len(group) > 1
        )
        if member_count > 10_000 or total_size > 2_000_000_000:
            result["bomb_risk"] = True
    except (OSError, tarfile.TarError, ValueError, OverflowError) as exc:
        result["invalid"] = True
        result["invalid_detail"] = type(exc).__name__
    return result


def safe_zip_member_bytes(archive: zipfile.ZipFile, names: list[str]) -> dict[str, bytes]:
    infos = {info.filename: info for info in archive.infolist()}
    selected = [infos[name] for name in names if name in infos]
    total = sum(info.file_size for info in selected)
    if len(selected) > 5_000 or total > 50_000_000:
        raise ValueError("OOXML XML payload exceeds safe inspection limits")
    for info in selected:
        if info.file_size > 10_000_000 or (
            info.compress_size > 0 and info.file_size > 5_000_000
            and info.file_size / info.compress_size > 200
        ):
            raise ValueError("OOXML member exceeds safe inspection limits")
    return {info.filename: archive.read(info) for info in selected}


def safe_zip_xml_text(archive: zipfile.ZipFile, names: list[str]) -> str:
    return " ".join(
        payload.decode("utf-8", errors="ignore")
        for payload in safe_zip_member_bytes(archive, names).values()
    )


WORDPROCESSING_NAMESPACES = {
    "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "http://purl.oclc.org/ooxml/wordprocessingml/main",
}
DC_NAMESPACE = "http://purl.org/dc/elements/1.1/"
CORE_NAMESPACE = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"


def expanded_name(tag: str) -> tuple[str, str]:
    if tag.startswith("{") and "}" in tag:
        namespace, local = tag[1:].split("}", 1)
        return namespace, local
    return "", tag


def parse_bounded_xml(payload: bytes) -> ET.Element:
    if re.search(br"<!\s*(?:DOCTYPE|ENTITY)\b", payload, flags=re.I):
        raise ValueError("DTD/entity declarations are prohibited during OOXML inspection")
    return ET.fromstring(payload)


def ooxml_structure_valid(path: Path, observed_type: str) -> bool:
    main_parts = {
        "docx": "word/document.xml",
        "xlsx": "xl/workbook.xml",
        "pptx": "ppt/presentation.xml",
    }
    expected_content_types = {
        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml",
        "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml",
        "pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml",
    }
    expected_roots = {
        "docx": {
            ("http://schemas.openxmlformats.org/wordprocessingml/2006/main", "document"),
            ("http://purl.oclc.org/ooxml/wordprocessingml/main", "document"),
        },
        "xlsx": {
            ("http://schemas.openxmlformats.org/spreadsheetml/2006/main", "workbook"),
            ("http://purl.oclc.org/ooxml/spreadsheetml/main", "workbook"),
        },
        "pptx": {
            ("http://schemas.openxmlformats.org/presentationml/2006/main", "presentation"),
            ("http://purl.oclc.org/ooxml/presentationml/main", "presentation"),
        },
    }
    relationship_types = {
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument",
        "http://purl.oclc.org/ooxml/officeDocument/relationships/officeDocument",
    }
    main_part = main_parts.get(observed_type)
    if main_part is None:
        return True
    try:
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
            required = {"[Content_Types].xml", "_rels/.rels", main_part}
            if not required.issubset(names):
                return False
            payloads = safe_zip_member_bytes(archive, ["[Content_Types].xml", "_rels/.rels", main_part])
            types_root = parse_bounded_xml(payloads["[Content_Types].xml"])
            rels_root = parse_bounded_xml(payloads["_rels/.rels"])
            main_root = parse_bounded_xml(payloads[main_part])
            types_ns, types_local = expanded_name(types_root.tag)
            rels_ns, rels_local = expanded_name(rels_root.tag)
            if (types_ns, types_local) != (
                "http://schemas.openxmlformats.org/package/2006/content-types", "Types",
            ):
                return False
            if (rels_ns, rels_local) != (
                "http://schemas.openxmlformats.org/package/2006/relationships", "Relationships",
            ):
                return False
            part_name = "/" + main_part
            has_content_type = any(
                expanded_name(element.tag)[1] == "Override"
                and element.attrib.get("PartName", "") == part_name
                and element.attrib.get("ContentType", "") == expected_content_types[observed_type]
                for element in types_root
            )
            has_root_relationship = any(
                expanded_name(element.tag)[1] == "Relationship"
                and element.attrib.get("Type", "") in relationship_types
                and element.attrib.get("Target", "").lstrip("/") == main_part
                for element in rels_root
            )
            return (
                has_content_type and has_root_relationship
                and expanded_name(main_root.tag) in expected_roots[observed_type]
            )
    except (OSError, zipfile.BadZipFile, KeyError, ValueError, ET.ParseError, NotImplementedError, RuntimeError):
        return False


def ooxml_risky_features(path: Path) -> dict[str, object]:
    """Detect external relationships and executable/embedded OOXML parts."""
    result: dict[str, object] = {
        "external_relationships": [], "active_or_embedded_parts": [], "invalid": False,
    }
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            relationship_names = [name for name in names if name.lower().endswith(".rels")]
            payloads = safe_zip_member_bytes(archive, relationship_names)
            for name, payload in payloads.items():
                root = parse_bounded_xml(payload)
                for element in root.iter():
                    if expanded_name(element.tag)[1] != "Relationship":
                        continue
                    target_mode = element.attrib.get("TargetMode", "")
                    target = element.attrib.get("Target", "")
                    relation_type = element.attrib.get("Type", "")
                    if target_mode.casefold() == "external" or re.match(
                        r"^(?:https?|ftp|file|javascript|data):", target, flags=re.I,
                    ):
                        result["external_relationships"].append(  # type: ignore[union-attr]
                            {"part": name, "type": relation_type, "target": target[:500]}
                        )
            risky_tokens = (
                "vbaproject.bin", "activex/", "/embeddings/", "oleobject",
                "attachedtemplate", "externalLinks/",
            )
            result["active_or_embedded_parts"] = sorted(
                name for name in names
                if any(token.casefold() in name.casefold() for token in risky_tokens)
            )
    except (OSError, zipfile.BadZipFile, KeyError, ValueError, ET.ParseError, NotImplementedError, RuntimeError):
        result["invalid"] = True
    return result


def stream_contains(path: Path, patterns: tuple[bytes, ...]) -> bool:
    """Scan a file with bounded memory while preserving cross-chunk matches."""
    overlap = max((len(pattern) for pattern in patterns), default=1) - 1
    previous = b""
    try:
        with path.open("rb") as handle:
            while True:
                block = handle.read(1024 * 1024)
                if not block:
                    return False
                payload = previous + block
                if any(pattern in payload for pattern in patterns):
                    return True
                previous = payload[-overlap:] if overlap else b""
    except OSError:
        return False


def pdf_object_has_active_content(root: object, *, max_objects: int = 50_000) -> bool:
    """Walk parsed PDF objects with a hard budget so escaped names cannot evade checks."""
    pending: list[object] = [root]
    seen_indirect: set[tuple[int, int]] = set()
    visited = 0
    while pending:
        current = pending.pop()
        visited += 1
        if visited > max_objects:
            raise ValueError("PDF object graph exceeds safe active-content inspection budget")
        if hasattr(current, "idnum") and hasattr(current, "generation") and hasattr(current, "get_object"):
            identity = (int(current.idnum), int(current.generation))  # type: ignore[attr-defined]
            if identity in seen_indirect:
                continue
            seen_indirect.add(identity)
            current = current.get_object()  # type: ignore[attr-defined]
        if isinstance(current, dict):
            normalized = {str(key): value for key, value in current.items()}
            active_keys = {
                "/JavaScript", "/JS", "/OpenAction", "/AA", "/Launch",
                "/SubmitForm", "/GoToR", "/RichMedia", "/EmbeddedFiles",
            }
            if active_keys & normalized.keys():
                return True
            if str(normalized.get("/S", "")) in {
                "/JavaScript", "/Launch", "/SubmitForm", "/GoToR", "/RichMedia",
            }:
                return True
            pending.extend(normalized.values())
        elif isinstance(current, (list, tuple)):
            pending.extend(current)
    return False


def pdf_features(path: Path) -> dict[str, object]:
    """Parse the complete PDF structure; marker-only checks never prove integrity."""
    result: dict[str, object] = {
        "encrypted": False, "active_javascript": False, "author_metadata": False,
    }
    try:
        from pypdf import PdfReader
    except ImportError:
        result["parser_unavailable"] = True
        return result
    try:
        reader = PdfReader(str(path), strict=True)
        result["encrypted"] = bool(reader.is_encrypted)
        if result["encrypted"]:
            return result
        page_count = len(reader.pages)
        if page_count < 1:
            raise ValueError("PDF contains no pages")
        result["page_count"] = page_count
        metadata = reader.metadata or {}
        author = metadata.get("/Author") if hasattr(metadata, "get") else None
        result["author_metadata"] = bool(str(author).strip()) if author is not None else False
        try:
            xmp = reader.xmp_metadata
            xmp_creators = getattr(xmp, "dc_creator", None) if xmp is not None else None
            if xmp_creators:
                result["author_metadata"] = True
        except Exception:
            # Malformed XMP is a parser-integrity failure for a submission audit.
            raise ValueError("PDF XMP metadata could not be parsed")
        # pypdf proves the object/xref/page tree.  A streaming scan then rejects
        # active-script tokens without the former first-2-MB blind spot. Parsed
        # object traversal also catches PDF name escaping such as #53 for "S".
        result["active_javascript"] = pdf_object_has_active_content(reader.trailer) or stream_contains(
            path, (
                b"/JavaScript", b"/JS ", b"/JS\t", b"/JS\r", b"/JS\n",
                b"/OpenAction", b"/AA ", b"/Launch", b"/SubmitForm", b"/GoToR",
                b"/RichMedia", b"/EmbeddedFiles",
            ),
        )
    except Exception as exc:  # pypdf raises several format-specific exception types
        result["parse_error"] = True
        result["parse_error_type"] = type(exc).__name__
    return result


def split_extensions(value: str) -> set[str]:
    result: set[str] = set()
    for piece in re.split(r"[;,|\s]+", value.strip()):
        if piece:
            result.add(piece.lower() if piece.startswith(".") else "." + piece.lower())
    return result


def split_controlled_tokens(value: str) -> set[str]:
    return {
        piece.strip().lower() for piece in re.split(r"[;,|]+", value)
        if piece.strip()
    }


def strict_text_payload(path: Path) -> str:
    """Read the complete bounded text file with strict decoding and control checks."""
    size = path.stat().st_size
    if size > MAX_TEXT_SCAN_BYTES:
        raise ValueError("Text payload exceeds safe inspection limit")
    payload = path.read_bytes()
    text = payload.decode("utf-8-sig", errors="strict")
    disallowed = [
        character for character in text
        if (ord(character) < 32 and character not in {"\t", "\n", "\r"})
        or ord(character) == 127
    ]
    if disallowed:
        raise ValueError("Text payload contains NUL or disallowed control characters")
    return text


def text_payload(path: Path) -> str:
    if path.suffix.lower() == ".docx":
        with zipfile.ZipFile(path) as archive:
            names = [
                name for name in archive.namelist()
                if (name.startswith("word/") or name.startswith("docProps/")) and name.endswith(".xml")
            ]
            fragments: list[str] = []
            for payload in safe_zip_member_bytes(archive, names).values():
                root = parse_bounded_xml(payload)
                fragments.extend(text for text in root.itertext() if text)
            return " ".join(fragments)
    if path.suffix.lower() in TEXT_SUFFIXES:
        return strict_text_payload(path)
    return ""


def docx_features(path: Path) -> dict[str, object]:
    features: dict[str, object] = {"comments": False, "tracked_changes": False, "authors": []}
    try:
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
            word_names = [name for name in names if name.startswith("word/") and name.endswith(".xml")]
            for payload in safe_zip_member_bytes(archive, word_names).values():
                root = parse_bounded_xml(payload)
                for element in root.iter():
                    namespace, local = expanded_name(element.tag)
                    if namespace not in WORDPROCESSING_NAMESPACES:
                        continue
                    if local in {"comment", "commentRangeStart", "commentRangeEnd", "commentReference"}:
                        features["comments"] = True
                    if local in {"ins", "del", "moveFrom", "moveTo"}:
                        features["tracked_changes"] = True
            authors: list[str] = []
            if "docProps/core.xml" in names:
                core_payload = safe_zip_member_bytes(archive, ["docProps/core.xml"])["docProps/core.xml"]
                core_root = parse_bounded_xml(core_payload)
                for element in core_root.iter():
                    namespace, local = expanded_name(element.tag)
                    if (namespace, local) not in {
                        (DC_NAMESPACE, "creator"), (CORE_NAMESPACE, "lastModifiedBy"),
                    }:
                        continue
                    value = re.sub(r"\s+", " ", "".join(element.itertext())).strip()
                    if value:
                        authors.append(value)
            features["authors"] = authors
    except (OSError, zipfile.BadZipFile, KeyError, ValueError, ET.ParseError, NotImplementedError, RuntimeError):
        features["invalid"] = True
    return features


def validate_rule_fields(
    row: dict[str, str], row_number: int, item_id: str, requirement: str,
    audit_date: date, max_age: int, findings: list[dict[str, object]],
) -> None:
    authority = (row.get("authority_class") or "").strip().upper()
    rule_id = (row.get("rule_id") or "").strip()
    source_url = (row.get("source_url") or "").strip()
    verified = (row.get("guide_verified_on") or "").strip()
    decisive = requirement in {"required", "conditional", "portal-only"}
    if decisive and not rule_id:
        add_finding(findings, "ERROR", "RULE_ID", f"Row {row_number} has no rule_id", item_id=item_id)
    if authority not in AUTHORITY_CLASSES:
        add_finding(findings, "ERROR", "AUTHORITY_CLASS", f"Row {row_number} has invalid authority_class: {authority or '[blank]'}", item_id=item_id)
    if decisive and authority not in HARD_RULE_AUTHORITIES:
        add_finding(findings, "ERROR", "NONAUTHORITATIVE_HARD_RULE", f"{item_id} uses {authority or '[blank]'} for a {requirement} requirement", item_id=item_id)
    if decisive and not source_url.startswith("https://"):
        add_finding(findings, "ERROR", "SOURCE_URL", f"{item_id} lacks a direct HTTPS official source URL", item_id=item_id)
    verified_date = parse_iso_date(verified)
    if decisive and verified_date is None:
        add_finding(findings, "ERROR", "GUIDE_DATE", f"{item_id} guide_verified_on must be YYYY-MM-DD", item_id=item_id)
    elif verified_date is not None:
        age = (audit_date - verified_date).days
        if age < 0:
            add_finding(findings, "ERROR", "GUIDE_DATE_FUTURE", f"{item_id} guide verification date is in the future", item_id=item_id)
        elif decisive and age > max_age:
            add_finding(findings, "ERROR", "GUIDE_STALE", f"{item_id} decisive rule was checked {age} days ago (maximum {max_age})", item_id=item_id)


def main() -> int:
    args = parse_args()
    findings: list[dict[str, object]] = []
    evidence_provenance: dict[str, object] | None = None
    try:
        audit_date = parse_iso_date(args.as_of) if args.as_of else date.today()
        if audit_date is None:
            raise ValueError("--as-of must use YYYY-MM-DD")
        if args.max_guide_age_days < 0:
            raise ValueError("--max-guide-age-days must be nonnegative")
        root = authorized_package_root(args.package_dir)
    except (OSError, ValueError) as exc:
        print(json.dumps({"execution_status": "FAIL", "status": "FAIL", "findings": [{"severity": "ERROR", "code": "INPUT", "message": str(exc)}]}, ensure_ascii=False, indent=2))
        return 2

    manifest_raw = str(args.manifest or "").strip()
    manifest_input = Path(manifest_raw).expanduser()
    manifest_candidate = manifest_input if manifest_input.is_absolute() else root / manifest_input
    manifest_path = Path(os.path.abspath(str(manifest_candidate)))
    unsafe_manifest_parts = [
        part for part in manifest_input.parts
        if part not in {manifest_input.anchor, ".", ""} and (part == ".." or ":" in part)
    ]
    if (
        not manifest_raw
        or manifest_raw.startswith(("\\\\", "//", "\\\\?\\", "\\\\.\\"))
        or unsafe_manifest_parts
    ):
        add_finding(
            findings, "ERROR", "MANIFEST_ESCAPE",
            "Manifest path must be canonical, must not use UNC/device/parent traversal, and must not contain an alternate data stream",
        )
        return emit_report(
            root, manifest_path, [], [], findings, scope=args.scope,
            active_route=None, evidence_provenance=evidence_provenance,
            manifest_trusted=False,
        )
    try:
        manifest_path.relative_to(root)
    except ValueError:
        add_finding(findings, "ERROR", "MANIFEST_ESCAPE", "Manifest path escapes package root")
        return emit_report(
            root, manifest_path, [], [], findings, scope=args.scope,
            active_route=None, evidence_provenance=evidence_provenance,
            manifest_trusted=False,
        )
    if has_symlink_component(root, manifest_candidate):
        add_finding(findings, "ERROR", "MANIFEST_SYMLINK", "Manifest path contains a symlink")
        return emit_report(
            root, manifest_path, [], [], findings, scope=args.scope,
            active_route=None, evidence_provenance=evidence_provenance,
            manifest_trusted=False,
        )
    try:
        manifest_path = manifest_path.resolve(strict=True)
        if not manifest_path.is_file():
            raise ValueError("manifest is not a regular file")
        manifest_path.relative_to(root)
    except (OSError, ValueError) as exc:
        add_finding(findings, "ERROR", "MANIFEST_READ", str(exc))
        return emit_report(
            root, manifest_path, [], [], findings, scope=args.scope,
            active_route=None, evidence_provenance=evidence_provenance,
            manifest_trusted=False,
        )
    try:
        if manifest_path.stat().st_size > 10_000_000:
            add_finding(findings, "ERROR", "MANIFEST_SIZE", "Manifest exceeds the 10 MB safe parsing limit")
            return emit_report(
                root, manifest_path, [], [], findings, scope=args.scope,
                active_route=None, evidence_provenance=evidence_provenance,
            )
        with manifest_path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            rows = []
            too_many_rows = False
            for index, row in enumerate(reader):
                if index >= 10_000:
                    too_many_rows = True
                    break
                rows.append(row)
            header_list = reader.fieldnames or []
            headers = set(header_list)
    except (OSError, csv.Error) as exc:
        add_finding(findings, "ERROR", "MANIFEST_READ", str(exc))
        return emit_report(
            root, manifest_path, [], [], findings, scope=args.scope,
            active_route=None, evidence_provenance=evidence_provenance,
        )

    evidence_by_rule: dict[str, dict[str, str]] = {}
    active_route: dict[str, object] | None = None
    if args.submission_mode:
        try:
            evidence_path = Path(args.evidence).expanduser().resolve(strict=True)
            route_matrix_path = Path(args.route_matrix).expanduser().resolve(strict=True)
            bundled_route_matrix = BUNDLED_ROUTE_MATRIX_PATH.resolve(strict=True)
            bundled_evidence = BUNDLED_EVIDENCE_PATH.resolve(strict=True)
            if route_matrix_path != bundled_route_matrix:
                raise ValueError("Custom route matrices are prohibited in submission mode; update and validate the bundled contract instead")
            evidence_by_rule, evidence_provenance = load_validated_evidence_registry(
                evidence_path, bundled_evidence,
            )
            route_matrix = load_route_matrix(route_matrix_path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            add_finding(findings, "ERROR", "RULE_REGISTRY", f"Cannot load route/evidence registry: {exc}")
            route_matrix = []
        pre_journals = {(row.get("journal_id") or "").strip() for row in rows if (row.get("journal_id") or "").strip()}
        pre_articles = {(row.get("article_type") or "").strip() for row in rows if (row.get("article_type") or "").strip()}
        pre_stages = {(row.get("submission_stage") or "").strip().lower() for row in rows if (row.get("submission_stage") or "").strip()}
        if len(pre_journals) == len(pre_articles) == len(pre_stages) == 1:
            route_key = (next(iter(pre_journals)), next(iter(pre_articles)), next(iter(pre_stages)))
            matches = [
                route for route in route_matrix
                if (route.get("journal_id"), route.get("article_type"), route.get("stage")) == route_key
            ]
            if len(matches) == 1:
                active_route = matches[0]
            else:
                add_finding(findings, "ERROR", "ROUTE_UNSUPPORTED", f"No unique current route contract for {route_key}")

    contract_items_by_rule: defaultdict[str, list[dict[str, object]]] = defaultdict(list)
    for requirement_item in (active_route or {}).get("requirements", []):
        if isinstance(requirement_item, dict):
            contract_items_by_rule[str(requirement_item.get("rule_id") or "")].append(requirement_item)

    duplicate_headers = sorted({name for name in header_list if header_list.count(name) > 1})
    if duplicate_headers:
        add_finding(findings, "ERROR", "DUPLICATE_HEADERS", "Duplicate headers: " + ", ".join(duplicate_headers))
    if too_many_rows:
        add_finding(findings, "ERROR", "MANIFEST_SIZE", "Manifest exceeds the 10,000-row safe parsing limit")
    for row_number, row in enumerate(rows, start=2):
        if None in row or any(value is None for key, value in row.items() if key is not None):
            add_finding(findings, "ERROR", "ROW_WIDTH", f"Row {row_number} does not have exactly one value per schema column")
    if header_list != REQUIRED_HEADER_ORDER:
        missing_headers = sorted(REQUIRED_HEADERS - headers)
        extra_headers = sorted(headers - REQUIRED_HEADERS)
        details: list[str] = []
        if missing_headers:
            details.append("missing=" + ",".join(missing_headers))
        if extra_headers:
            details.append("extra=" + ",".join(extra_headers))
        if not missing_headers and not extra_headers:
            details.append("columns are out of canonical order")
        add_finding(findings, "ERROR", "HEADERS", "Manifest must use the exact ordered schema: " + "; ".join(details))
    if args.submission_mode and not rows:
        add_finding(findings, "ERROR", "EMPTY_MANIFEST", "Submission manifest has no items")

    try:
        actual_files, symlinks = enumerate_package(root)
    except (OSError, ValueError) as exc:
        add_finding(findings, "ERROR", "PACKAGE_LIMIT", f"Package inventory is outside bounded audit limits: {exc}")
        return emit_report(
            root, manifest_path, rows, [], findings, scope=args.scope,
            active_route=active_route, evidence_provenance=evidence_provenance,
        )
    for symlink in symlinks:
        add_finding(findings, "ERROR", "SYMLINK", "Submission root contains a symlink; contents were not followed", path=normalized_rel(symlink, root))
    manifest_rel = normalized_rel(manifest_path, root) if manifest_path.exists() else args.manifest.replace("\\", "/")
    actual_upload_files = [path for path in actual_files if normalized_rel(path, root).casefold() != manifest_rel.casefold()]
    actual_by_rel = {normalized_rel(path, root).casefold(): path for path in actual_upload_files}
    path_rows: defaultdict[str, list[str]] = defaultdict(list)
    seen_ids: set[str] = set()
    claimed_paths: set[str] = set()
    observed_hashes: defaultdict[str, list[str]] = defaultdict(list)
    journal_values: set[str] = set()
    article_values: set[str] = set()
    stage_values: set[str] = set()
    study_design_values: set[str] = set()
    review_model_values: set[str] = set()
    project_id_values: set[str] = set()
    study_scope_values: set[str] = set()
    project_state_digest_values: set[str] = set()
    modality_role_digest_values: set[str] = set()
    scientific_handoff_packet_digest_values: set[str] = set()
    scientific_prereview_receipt_digest_values: set[str] = set()
    analysis_lock_digest_values: set[str] = set()
    claim_registry_digest_values: set[str] = set()
    response_package_digest_values: set[str] = set()

    for path in actual_upload_files:
        relative = normalized_rel(path, root)
        try:
            path.resolve(strict=True).relative_to(root)
        except (OSError, ValueError):
            add_finding(findings, "ERROR", "ACTUAL_PATH_ESCAPE", "Resolved actual file escapes the package root", path=relative)
        if TEMP_NAME_RE.search(path.name):
            add_finding(findings, "ERROR", "TEMP_FILE", "Temporary or backup file is inside upload root", path=relative)
        try:
            if path.stat().st_size == 0:
                add_finding(findings, "ERROR", "ZERO_BYTE", "Zero-byte file", path=relative)
        except OSError as exc:
            add_finding(findings, "ERROR", "FILE_STAT", f"Cannot inspect file metadata: {exc}", path=relative)

    for row_number, row in enumerate(rows, start=2):
        item_id = (row.get("item_id") or "").strip()
        requirement = (row.get("requirement_class") or "").strip().lower()
        status = (row.get("status") or "").strip().lower()
        material = (row.get("material") or "").strip()
        tracked_policy = (row.get("tracked_changes_policy") or "").strip().lower()
        revision_variant = (row.get("revision_variant") or "").strip().lower()
        relative = (row.get("path") or "").strip().replace("\\", "/")
        blinded_value = (row.get("blinded") or "").strip().lower()
        blinded = blinded_value in TRUE_VALUES
        journal = (row.get("journal_id") or "").strip()
        article_type = (row.get("article_type") or "").strip()
        stage = (row.get("submission_stage") or "").strip().lower()
        study_design_raw = (row.get("study_design") or "").strip().lower()
        study_designs = split_controlled_tokens(study_design_raw)
        review_model = (row.get("review_model") or "").strip().lower()
        project_id = (row.get("project_id") or "").strip()
        study_scope = (row.get("study_scope") or "").strip().lower()
        project_state_digest = (row.get("project_state_digest") or "").strip()
        modality_role_digest = (row.get("modality_role_digest") or "").strip()
        scientific_handoff_packet_digest = (
            row.get("scientific_handoff_packet_digest") or ""
        ).strip()
        scientific_prereview_receipt_digest = (
            row.get("scientific_prereview_receipt_digest") or ""
        ).strip()
        source_artifact_id = (row.get("source_artifact_id") or "").strip()
        analysis_lock_digest = (row.get("analysis_lock_digest") or "").strip()
        claim_registry_digest = (row.get("claim_registry_digest") or "").strip()
        response_package_digest = (row.get("response_package_digest") or "").strip()
        if journal:
            journal_values.add(journal)
        if article_type:
            article_values.add(article_type)
        if stage:
            stage_values.add(stage)
        if study_design_raw:
            study_design_values.add(";".join(sorted(study_designs)))
        if review_model:
            review_model_values.add(review_model)
        if project_id:
            project_id_values.add(project_id)
        if study_scope:
            study_scope_values.add(study_scope)
        if project_state_digest:
            project_state_digest_values.add(project_state_digest)
        if modality_role_digest:
            modality_role_digest_values.add(modality_role_digest)
        if scientific_handoff_packet_digest:
            scientific_handoff_packet_digest_values.add(scientific_handoff_packet_digest)
        if scientific_prereview_receipt_digest:
            scientific_prereview_receipt_digest_values.add(scientific_prereview_receipt_digest)
        if analysis_lock_digest:
            analysis_lock_digest_values.add(analysis_lock_digest)
        if claim_registry_digest:
            claim_registry_digest_values.add(claim_registry_digest)
        if response_package_digest:
            response_package_digest_values.add(response_package_digest)

        if (row.get("schema_version") or "").strip() != SCHEMA_VERSION:
            add_finding(findings, "ERROR", "SCHEMA_VERSION", f"Row {row_number} must use schema_version {SCHEMA_VERSION}", item_id=item_id)
        if not PROJECT_ID_RE.fullmatch(project_id):
            add_finding(
                findings, "ERROR", "PROJECT_ID",
                f"Row {row_number} project_id must be a stable 3-128 character identifier",
                item_id=item_id,
            )
        if study_scope not in STUDY_SCOPES:
            add_finding(
                findings, "ERROR", "STUDY_SCOPE",
                f"{item_id} study_scope must be one of {sorted(STUDY_SCOPES)}",
                item_id=item_id,
            )
        for digest_field, digest_value in (
            ("project_state_digest", project_state_digest),
            ("modality_role_digest", modality_role_digest),
        ):
            if not is_nonzero_sha256(digest_value):
                add_finding(
                    findings, "ERROR", "SCIENTIFIC_HANDOFF_DIGEST",
                    f"{item_id} {digest_field} must be a nonzero lowercase SHA-256",
                    item_id=item_id,
                )
        if study_scope == "evidence-synthesis":
            if scientific_handoff_packet_digest != "not-applicable":
                add_finding(
                    findings, "ERROR", "EVIDENCE_SYNTHESIS_HANDOFF",
                    f"{item_id} evidence-synthesis scope requires scientific_handoff_packet_digest=not-applicable",
                    item_id=item_id,
                )
            if not is_nonzero_sha256(scientific_prereview_receipt_digest):
                add_finding(
                    findings, "ERROR", "EVIDENCE_SYNTHESIS_PREREVIEW",
                    f"{item_id} evidence-synthesis scope requires a nonzero scientific_prereview_receipt_digest",
                    item_id=item_id,
                )
            if "systematic-review-meta-analysis" not in study_designs:
                add_finding(
                    findings, "ERROR", "EVIDENCE_SYNTHESIS_DESIGN",
                    f"{item_id} evidence-synthesis scope requires study_design=systematic-review-meta-analysis",
                    item_id=item_id,
                )
        elif not is_nonzero_sha256(scientific_handoff_packet_digest):
            add_finding(
                findings, "ERROR", "SCIENTIFIC_HANDOFF_DIGEST",
                f"{item_id} scientific_handoff_packet_digest must be a nonzero lowercase SHA-256",
                item_id=item_id,
            )
        if (
            scientific_prereview_receipt_digest != "not-applicable"
            and not is_nonzero_sha256(scientific_prereview_receipt_digest)
        ):
            add_finding(
                findings, "ERROR", "SCIENTIFIC_PREREVIEW_RECEIPT_DIGEST",
                f"{item_id} scientific_prereview_receipt_digest must be a nonzero lowercase SHA-256 or not-applicable",
                item_id=item_id,
            )
        if not source_artifact_id:
            add_finding(
                findings, "ERROR", "SOURCE_ARTIFACT_ID",
                f"Row {row_number} has no source_artifact_id foreign key",
                item_id=item_id,
            )
        elif source_artifact_id != "not-applicable" and not ARTIFACT_ID_RE.fullmatch(source_artifact_id):
            add_finding(
                findings, "ERROR", "SOURCE_ARTIFACT_ID",
                f"{item_id} source_artifact_id must be a stable 2-128 character identifier or not-applicable",
                item_id=item_id,
            )
        elif relative and source_artifact_id == "not-applicable":
            add_finding(
                findings, "ERROR", "SOURCE_ARTIFACT_ID",
                f"{item_id} is a physical file and cannot use source_artifact_id=not-applicable",
                item_id=item_id,
            )
        for digest_field, digest_value in (
            ("analysis_lock_digest", analysis_lock_digest),
            ("claim_registry_digest", claim_registry_digest),
        ):
            if not is_nonzero_sha256(digest_value):
                add_finding(
                    findings, "ERROR", "UPSTREAM_DIGEST",
                    f"{item_id} {digest_field} must be a nonzero lowercase SHA-256",
                    item_id=item_id,
                )
        if stage == "revision":
            if not is_nonzero_sha256(response_package_digest):
                add_finding(
                    findings, "ERROR", "RESPONSE_PACKAGE_DIGEST",
                    f"{item_id} revision row requires a nonzero lowercase response_package_digest SHA-256",
                    item_id=item_id,
                )
        elif response_package_digest != "not-applicable" and not is_nonzero_sha256(response_package_digest):
            add_finding(
                findings, "ERROR", "RESPONSE_PACKAGE_DIGEST",
                f"{item_id} response_package_digest must be a nonzero lowercase SHA-256 or not-applicable",
                item_id=item_id,
            )
        if not item_id:
            add_finding(findings, "ERROR", "ITEM_ID", f"Row {row_number} has no item_id")
        elif item_id in seen_ids:
            add_finding(findings, "ERROR", "ITEM_DUP", f"Row {row_number} duplicates item_id {item_id}", item_id=item_id)
        seen_ids.add(item_id)
        if requirement not in REQUIREMENT_CLASSES:
            add_finding(findings, "ERROR", "REQUIREMENT_CLASS", f"Row {row_number} has invalid requirement_class: {requirement or '[blank]'}", item_id=item_id)
        if status not in STATUSES:
            add_finding(findings, "ERROR", "STATUS", f"Row {row_number} has invalid status: {status or '[blank]'}", item_id=item_id)
        if stage and stage not in STAGES:
            add_finding(findings, "ERROR", "STAGE", f"Row {row_number} has invalid submission_stage: {stage}", item_id=item_id)
        if not study_designs:
            add_finding(findings, "ERROR", "STUDY_DESIGN", f"{item_id} has no controlled study_design", item_id=item_id)
        else:
            invalid_designs = sorted(study_designs - STUDY_DESIGNS)
            if invalid_designs:
                add_finding(findings, "ERROR", "STUDY_DESIGN", f"{item_id} has invalid study_design token(s): {invalid_designs}", item_id=item_id)
            if args.submission_mode and study_designs == {"other"}:
                add_finding(
                    findings, "ERROR", "STUDY_DESIGN_OTHER_UNRESOLVED",
                    f"{item_id} uses only study_design=other; extend or manually adjudicate the design route before closing conditional-material gates",
                    item_id=item_id,
                )
        if review_model not in REVIEW_MODELS:
            add_finding(findings, "ERROR", "REVIEW_MODEL", f"{item_id} has invalid review_model: {review_model or '[blank]'}", item_id=item_id)
        elif review_model == "not-confirmed":
            add_finding(findings, "ERROR", "REVIEW_MODEL_UNRESOLVED", f"{item_id} review model is not confirmed", item_id=item_id)
        elif journal and review_model not in JOURNAL_REVIEW_MODELS.get(journal, set()):
            add_finding(findings, "ERROR", "REVIEW_MODEL_ROUTE", f"{item_id} review model conflicts with the target-journal profile", item_id=item_id)
        if blinded_value not in BLINDED_VALUES:
            add_finding(findings, "ERROR", "BLINDED_STATE", f"{item_id} has invalid blinded value: {blinded_value or '[blank]'}", item_id=item_id)
        if tracked_policy not in TRACKED_CHANGE_POLICIES:
            add_finding(findings, "ERROR", "TRACKED_POLICY", f"{item_id} has invalid tracked_changes_policy: {tracked_policy or '[blank]'}", item_id=item_id)
        if revision_variant not in REVISION_VARIANTS:
            add_finding(findings, "ERROR", "REVISION_VARIANT", f"{item_id} has invalid revision_variant: {revision_variant or '[blank]'}", item_id=item_id)
        if stage != "revision" and revision_variant != "not-applicable":
            add_finding(findings, "ERROR", "REVISION_VARIANT_STAGE", f"{item_id} may use a revision variant only at revision stage", item_id=item_id)
        if stage != "revision" and tracked_policy == "allowed-marked-revision":
            add_finding(findings, "ERROR", "TRACKED_POLICY_STAGE", f"{item_id} cannot allow a marked revision outside revision stage", item_id=item_id)
        if revision_variant == "marked" and tracked_policy != "allowed-marked-revision":
            add_finding(findings, "ERROR", "MARKED_POLICY", f"{item_id} marked revision must explicitly use allowed-marked-revision", item_id=item_id)
        if tracked_policy == "allowed-marked-revision" and revision_variant != "marked":
            add_finding(findings, "ERROR", "MARKED_VARIANT", f"{item_id} allowed-marked-revision requires revision_variant=marked", item_id=item_id)
        if stage == "revision" and relative and revision_variant == "not-applicable":
            add_finding(findings, "ERROR", "REVISION_VARIANT_REQUIRED", f"{item_id} is a physical revision-stage file and must declare its revision role", item_id=item_id)
        if args.submission_mode and tracked_policy == "allowed-marked-revision":
            rule_id = (row.get("rule_id") or "").strip()
            contract_allows_marked = any(
                bool(item.get("allows_marked_revision"))
                for item in contract_items_by_rule.get(rule_id, [])
            )
            portal_allows_marked = (
                (row.get("authority_class") or "").strip().upper() == "PORTAL_CURRENT"
                and source_route_allowed(journal, (row.get("source_url") or "").strip())
                and not portal_receipt_issues(row)
            )
            if not (contract_allows_marked or portal_allows_marked):
                add_finding(
                    findings, "ERROR", "MARKED_REVISION_UNAUTHORIZED",
                    f"{item_id} cannot self-authorize tracked changes; the target revision route must explicitly allow a marked manuscript",
                    item_id=item_id,
                )
        for qa_field in ("technical_qa", "render_qa", "content_gate", "anonymization_qa", "crossfile_qa"):
            qa_value = (row.get(qa_field) or "").strip().lower()
            if qa_value not in QA_STATES:
                add_finding(findings, "ERROR", "QA_STATE", f"{item_id} has invalid {qa_field}: {qa_value or '[blank]'}", item_id=item_id)

        if args.submission_mode:
            validate_rule_fields(row, row_number, item_id, requirement, audit_date, args.max_guide_age_days, findings)
            if not journal or not article_type or not stage:
                add_finding(findings, "ERROR", "ROUTE_FIELDS", f"{item_id} lacks journal_id, article_type, or submission_stage", item_id=item_id)
            evidence = evidence_by_rule.get((row.get("rule_id") or "").strip())
            authority = (row.get("authority_class") or "").strip().upper()
            source_url = (row.get("source_url") or "").strip()
            portal_evidence_note = (row.get("notes") or "").strip()
            if authority in {"PUBLISHED_EXEMPLAR", "SECONDARY_SUMMARY"}:
                add_finding(findings, "ERROR", "NONRULE_MANIFEST_BASIS", f"{item_id} uses {authority} as a manifest rule basis", item_id=item_id)
            if authority == "PORTAL_CURRENT" and (
                not portal_evidence_note or PLACEHOLDER_RE.search(portal_evidence_note)
            ):
                add_finding(
                    findings, "ERROR", "PORTAL_EVIDENCE_LOCATOR",
                    f"{item_id} needs a concrete, non-placeholder note identifying the captured exact-journal portal screen",
                    item_id=item_id,
                )
            if authority == "PORTAL_CURRENT":
                receipt_issues = portal_receipt_issues(row)
                if receipt_issues:
                    add_finding(
                        findings, "ERROR", "PORTAL_EVIDENCE_RECEIPT",
                        f"{item_id} live-portal evidence receipt is incomplete: {'; '.join(receipt_issues)}",
                        item_id=item_id,
                    )
            if evidence is None:
                if authority != "PORTAL_CURRENT":
                    add_finding(findings, "ERROR", "RULE_UNKNOWN", f"{item_id} rule_id is absent from the refreshed evidence registry", item_id=item_id)
                elif not source_route_allowed(journal, source_url):
                    add_finding(findings, "ERROR", "PORTAL_SOURCE_ROUTE", f"{item_id} portal override is not bound to the exact target-journal route", item_id=item_id)
            else:
                if evidence.get("journal_id") != journal:
                    add_finding(findings, "ERROR", "RULE_JOURNAL_MISMATCH", f"{item_id} uses a rule belonging to {evidence.get('journal_id')}", item_id=item_id)
                if evidence.get("article_type") != article_type:
                    add_finding(findings, "ERROR", "RULE_ARTICLE_MISMATCH", f"{item_id} rule article type is {evidence.get('article_type')}", item_id=item_id)
                contract_item_for_rule = next(
                    iter(contract_items_by_rule.get((row.get("rule_id") or "").strip(), [])), None,
                )
                applicable_stages = {
                    value.strip() for value in re.split(
                        r"[;,|\s]+", (evidence.get("applicable_stages") or evidence.get("stage") or "").strip()
                    ) if value.strip()
                }
                if stage not in applicable_stages:
                    add_finding(
                        findings, "ERROR", "RULE_STAGE_MISMATCH",
                        f"{item_id} uses a rule applicable to {sorted(applicable_stages)} in a {stage} manifest",
                        item_id=item_id,
                    )
                if authority != "PORTAL_CURRENT":
                    if evidence.get("authority_class") != authority:
                        add_finding(findings, "ERROR", "RULE_AUTHORITY_MISMATCH", f"{item_id} authority does not match evidence registry", item_id=item_id)
                    if evidence.get("source_url") != source_url:
                        add_finding(findings, "ERROR", "RULE_SOURCE_MISMATCH", f"{item_id} source URL does not match evidence registry", item_id=item_id)
                    if evidence.get("checked_on") != (row.get("guide_verified_on") or "").strip():
                        add_finding(
                            findings, "ERROR", "RULE_DATE_MISMATCH",
                            f"{item_id} verification date does not match the governing evidence receipt",
                            item_id=item_id,
                        )
                    evidence_class = evidence.get("requirement_class")
                    allowed_classes = set(
                        contract_item_for_rule.get("allowed_requirement_classes", [])
                        if isinstance(contract_item_for_rule, dict) else []
                    )
                    if evidence_class in REQUIREMENT_CLASSES and evidence_class != requirement and requirement not in allowed_classes:
                        add_finding(findings, "ERROR", "RULE_CLASS_MISMATCH", f"{item_id} requirement_class does not match evidence registry", item_id=item_id)
                elif not source_route_allowed(journal, source_url):
                    add_finding(findings, "ERROR", "PORTAL_SOURCE_ROUTE", f"{item_id} portal override is not bound to the exact target-journal route", item_id=item_id)
                if evidence.get("verification_status") == "UNVERIFIED_CURRENT" and authority != "PORTAL_CURRENT":
                    add_finding(
                        findings, "ERROR", "RULE_CURRENT_UNRESOLVED",
                        f"{item_id} relies on an unresolved current rule without an exact-journal live-portal override",
                        item_id=item_id,
                    )
                if requirement == "conditional" and status == "not-applicable":
                    evidence_condition = (evidence.get("condition") or "").strip().casefold()
                    design_triggers = CONDITION_DESIGN_TRIGGERS.get(evidence_condition, set())
                    if study_designs & design_triggers:
                        add_finding(
                            findings, "ERROR", "CONDITIONAL_TRIGGERED_NA",
                            f"{item_id} is not-applicable even though study_design activates {evidence.get('condition')}",
                            item_id=item_id,
                        )
                if relative and authority != "PORTAL_CURRENT":
                    registry_extensions = split_extensions(evidence.get("allowed_extensions") or "")
                    declared_extensions = split_extensions(row.get("expected_extensions") or "")
                    if not registry_extensions:
                        add_finding(
                            findings, "ERROR", "RULE_FILETYPE_UNRESOLVED",
                            f"{item_id} has a physical upload but its official registry rule does not establish accepted extensions; capture the exact-journal live portal or maintain the validated rule registry/contract after human adjudication",
                            item_id=item_id, path=relative,
                        )
                    elif declared_extensions - registry_extensions:
                        add_finding(
                            findings, "ERROR", "RULE_EXTENSIONS_MISMATCH",
                            f"{item_id} declares extensions absent from the governing rule: {sorted(declared_extensions - registry_extensions)}",
                            item_id=item_id, path=relative,
                        )
        if requirement == "required" and status == "not-applicable":
            add_finding(findings, "ERROR", "REQUIRED_NA", f"Required item {item_id} cannot be not-applicable", item_id=item_id)
        if requirement == "conditional" and status == "not-applicable":
            if not (row.get("condition") or "").strip() or not (row.get("not_applicable_reason") or "").strip():
                add_finding(findings, "ERROR", "CONDITIONAL_NA", f"Conditional item {item_id} needs condition and not_applicable_reason", item_id=item_id)
            attestation_issues = conditional_na_attestation_issues(
                row, audit_date, args.max_guide_age_days,
            )
            if attestation_issues:
                add_finding(
                    findings, "ERROR", "CONDITIONAL_NA_ATTESTATION",
                    f"Conditional item {item_id} lacks a current human N/A receipt: "
                    + "; ".join(attestation_issues),
                    item_id=item_id,
                )
        if requirement == "portal-only" and relative:
            add_finding(findings, "ERROR", "PORTAL_PATH", f"Portal-only item {item_id} must not claim a local file", item_id=item_id, path=relative)
        if args.submission_mode and requirement == "portal-only" and status in {"pending-guide", "blocked-upstream", "not-applicable"}:
            add_finding(findings, "ERROR", "PORTAL_GATE_OPEN", f"Portal-only item {item_id} has unresolved status {status}", item_id=item_id)
        if args.submission_mode and requirement == "portal-only" and status == "ready":
            portal_ready_proven = (
                (row.get("authority_class") or "").strip().upper() == "PORTAL_CURRENT"
                and source_route_allowed(journal, (row.get("source_url") or "").strip())
                and not portal_receipt_issues(row)
            )
            if not portal_ready_proven:
                add_finding(
                    findings, "ERROR", "PORTAL_READY_UNPROVEN",
                    f"{item_id} cannot self-declare a path-free portal action complete without an exact-route capture locator",
                    item_id=item_id,
                )

        file_expected = requirement in {"required", "conditional"} and status != "not-applicable"
        contract_kinds_for_rule = {
            str(item.get("item_kind") or "")
            for item in contract_items_by_rule.get((row.get("rule_id") or "").strip(), [])
        }
        embedded_item = contract_kinds_for_rule == {"embedded"}
        field_item = contract_kinds_for_rule == {"field"}
        if embedded_item:
            file_expected = False
            if relative:
                add_finding(
                    findings, "ERROR", "EMBEDDED_ITEM_PATH",
                    f"{item_id} is an embedded-content assertion and must point to its parent file through the route contract, not duplicate the file path",
                    item_id=item_id, path=relative,
                )
            if args.submission_mode and status != "not-applicable":
                if status != "ready":
                    add_finding(findings, "ERROR", "EMBEDDED_ITEM_OPEN", f"{item_id} embedded-content check is not closed", item_id=item_id)
                if not (row.get("notes") or "").strip():
                    add_finding(findings, "ERROR", "EMBEDDED_LOCATOR", f"{item_id} needs a page/section/table locator in notes", item_id=item_id)
                for qa_field in ("content_gate", "crossfile_qa"):
                    if (row.get(qa_field) or "").strip().lower() != "pass":
                        add_finding(findings, "ERROR", "EMBEDDED_QA", f"{item_id} {qa_field} must be pass", item_id=item_id)
        if field_item:
            file_expected = False
            if relative:
                add_finding(
                    findings, "ERROR", "FIELD_ITEM_PATH",
                    f"{item_id} is a path-free cross-file assertion and must reference physical items in notes",
                    item_id=item_id, path=relative,
                )
            if args.submission_mode and status != "not-applicable" and status != "ready":
                add_finding(
                    findings, "ERROR", "FIELD_ITEM_OPEN",
                    f"{item_id} cross-file assertion is not closed", item_id=item_id,
                )
        optional_present = requirement == "optional" and bool(relative)
        file_path: Path | None = None
        if relative:
            relative_path = Path(relative)
            if relative_path.is_absolute() or relative_path.drive:
                add_finding(findings, "ERROR", "ABSOLUTE_PATH", "Manifest file paths must be relative to package root", item_id=item_id, path=relative)
                continue
            if ".." in relative_path.parts or any(":" in part for part in relative_path.parts):
                add_finding(findings, "ERROR", "NONCANONICAL_PATH", "Manifest path contains parent traversal or an alternate-stream/drive marker", item_id=item_id, path=relative)
                continue
            if relative.casefold() == manifest_rel.casefold():
                add_finding(findings, "ERROR", "MANIFEST_AS_UPLOAD", "The audit manifest is not a journal upload item", item_id=item_id, path=relative)
                continue
            raw_candidate = root / relative_path
            resolved = raw_candidate.resolve(strict=False)
            try:
                resolved.relative_to(root)
            except ValueError:
                add_finding(findings, "ERROR", "PATH_ESCAPE", f"Manifest path escapes package root: {relative}", item_id=item_id, path=relative)
                continue
            if has_symlink_component(root, raw_candidate):
                add_finding(findings, "ERROR", "PATH_SYMLINK", "Manifest path contains a symlink", item_id=item_id, path=relative)
                continue
            file_path = resolved
            folded = relative.casefold()
            path_rows[folded].append(item_id)
            claimed_paths.add(folded)
        if file_expected and not relative:
            add_finding(findings, "ERROR", "FILE_PATH", f"{item_id} requires a file path", item_id=item_id)
        if (file_expected or optional_present) and (file_path is None or not file_path.exists()):
            add_finding(findings, "ERROR", "FILE_MISSING", f"File missing: {relative or '[blank]'}", item_id=item_id, path=relative)
            continue
        if file_path is None or not file_path.exists():
            continue
        if not file_path.is_file():
            add_finding(findings, "ERROR", "NOT_FILE", "Manifest path is not a regular file", item_id=item_id, path=relative)
            continue
        if (
            args.submission_mode and review_model == "double-anonymized"
            and stage in {"initial", "pre-review", "revision"} and not blinded
        ):
            editor_only = any(
                requirement_item.get("blinded") is False
                or revision_variant in set(requirement_item.get("unblinded_revision_variants", []))
                for requirement_item in contract_items_by_rule.get((row.get("rule_id") or "").strip(), [])
            )
            if not editor_only:
                add_finding(
                    findings, "ERROR", "DOUBLE_BLIND_FILE",
                    f"{item_id} is a physical file in a double-anonymized package but is not marked blinded",
                    item_id=item_id, path=relative,
                )

        observed_type, type_detail = detect_file_type(file_path)
        suffix = file_path.suffix.lower()
        allowed = split_extensions(row.get("expected_extensions") or "")
        if not allowed:
            add_finding(findings, "ERROR", "EXPECTED_EXTENSIONS", f"{item_id} has no source-backed expected_extensions", item_id=item_id, path=relative)
        if allowed and suffix not in allowed:
            add_finding(findings, "ERROR", "EXTENSION_NOT_ALLOWED", f"{suffix or '[none]'} not in allowed set {sorted(allowed)}", item_id=item_id, path=relative)
        expected_observed = {"text"} if suffix in TEXT_SUFFIXES else EXPECTED_TYPES.get(suffix)
        if expected_observed and observed_type not in expected_observed:
            add_finding(findings, "ERROR", "SIGNATURE_MISMATCH", f"Extension {suffix} expects one of {sorted(expected_observed)}, observed {observed_type} ({type_detail})", item_id=item_id, path=relative)
        elif observed_type in {"unknown", "unreadable", "invalid-zip", "binary-text-extension"}:
            add_finding(findings, "ERROR", "TYPE_UNVERIFIED", f"Could not verify file type: {observed_type} ({type_detail})", item_id=item_id, path=relative)
        if observed_type == "ole-unverified":
            add_finding(
                findings, "ERROR", "OLE_PARSE_UNAVAILABLE",
                "Legacy .doc/.xls/.ppt cannot be certified from magic bytes alone; convert to a source-allowed modern format or use a format-aware OLE validator",
                item_id=item_id, path=relative,
            )

        zip_features: dict[str, object] | None = None
        archive_preflight_ok = True
        if observed_type == "tar":
            tar_features = tar_archive_features(file_path)
            tar_checks = (
                ("invalid", "TAR_INTEGRITY", "TAR container could not be parsed safely"),
                ("unsafe_names", "TAR_UNSAFE_PATH", "TAR contains absolute, parent-traversal, backslash, ADS-like or noncanonical member names"),
                ("link_entries", "TAR_LINK", "TAR contains symbolic or hard-link entries"),
                ("special_entries", "TAR_SPECIAL_ENTRY", "TAR contains device or FIFO entries"),
                ("duplicate_names", "TAR_DUPLICATE_MEMBER", "TAR contains duplicate member names"),
                ("case_collisions", "TAR_CASE_COLLISION", "TAR contains case-colliding member names"),
                ("canonical_collisions", "TAR_CANONICAL_COLLISION", "TAR member names collide after safe normalization"),
                ("bomb_risk", "TAR_BOMB_RISK", "TAR exceeds bounded member-count or expanded-size limits"),
            )
            for key, code, message in tar_checks:
                if tar_features.get(key):
                    add_finding(findings, "ERROR", code, message, item_id=item_id, path=relative)
                    archive_preflight_ok = False
        elif observed_type == "gzip":
            add_finding(
                findings, "ERROR", "GZIP_PREFLIGHT_UNAVAILABLE",
                "GZIP/TGZ cannot pass structural audit until a bounded stream/member inspector is available; do not auto-extract it",
                item_id=item_id, path=relative,
            )
            archive_preflight_ok = False
        if observed_type in {"docx", "xlsx", "pptx", "zip"}:
            # Preflight must finish before any OOXML member is decompressed/read.
            zip_features = archive_features(file_path)
            if zip_features.get("invalid") or zip_features.get("bad_member"):
                add_finding(findings, "ERROR", "ZIP_INTEGRITY", f"ZIP/OOXML integrity failure: {zip_features.get('bad_member') or 'invalid archive'}", item_id=item_id, path=relative)
            if zip_features.get("unsupported"):
                add_finding(
                    findings, "ERROR", "ZIP_UNSUPPORTED",
                    f"ZIP/OOXML uses an unsupported or unsafe compression feature ({zip_features.get('unsupported_detail') or 'unknown'})",
                    item_id=item_id, path=relative,
                )
            if zip_features.get("encrypted"):
                add_finding(findings, "ERROR", "ZIP_ENCRYPTED", "Encrypted/password-protected ZIP member detected", item_id=item_id, path=relative)
            if zip_features.get("unsafe_names"):
                add_finding(findings, "ERROR", "ZIP_UNSAFE_PATH", "Archive contains absolute or parent-traversal member names", item_id=item_id, path=relative)
            if zip_features.get("symlink_entries"):
                add_finding(findings, "ERROR", "ZIP_SYMLINK", "Archive contains symlink entries", item_id=item_id, path=relative)
            if zip_features.get("duplicate_names"):
                add_finding(findings, "ERROR", "ZIP_DUPLICATE_MEMBER", "Archive contains duplicate member names", item_id=item_id, path=relative)
            if zip_features.get("case_collisions"):
                add_finding(findings, "ERROR", "ZIP_CASE_COLLISION", "Archive contains case-colliding member names", item_id=item_id, path=relative)
            if zip_features.get("canonical_collisions"):
                add_finding(findings, "ERROR", "ZIP_CANONICAL_COLLISION", "Archive member names collide after safe path normalization", item_id=item_id, path=relative)
            if zip_features.get("bomb_risk"):
                add_finding(findings, "ERROR", "ZIP_BOMB_RISK", "Archive exceeds safe entry, expansion, or compression-ratio limits", item_id=item_id, path=relative)
            elif zip_features.get("integrity_skipped"):
                add_finding(findings, "ERROR", "ZIP_PREFLIGHT_INCOMPLETE", "Archive is too large for bounded integrity preflight; use a safe format-aware inspector", item_id=item_id, path=relative)
            archive_preflight_ok = not any(
                zip_features.get(key) for key in (
                    "invalid", "bad_member", "unsupported", "encrypted", "unsafe_names",
                    "symlink_entries", "duplicate_names", "case_collisions", "canonical_collisions",
                    "bomb_risk", "integrity_skipped",
                )
            )
            if archive_preflight_ok and observed_type in {"docx", "xlsx", "pptx"}:
                if not ooxml_structure_valid(file_path, observed_type):
                    add_finding(
                        findings, "ERROR", "OOXML_STRUCTURE",
                        "OOXML package lacks a valid content-type declaration, root relationship, or main part",
                        item_id=item_id, path=relative,
                    )
                    archive_preflight_ok = False
                else:
                    risky_ooxml = ooxml_risky_features(file_path)
                    if risky_ooxml.get("invalid"):
                        add_finding(
                            findings, "ERROR", "OOXML_RELATIONSHIP_INSPECTION",
                            "OOXML relationship/embedded-part inspection could not be completed safely",
                            item_id=item_id, path=relative,
                        )
                        archive_preflight_ok = False
                    if risky_ooxml.get("external_relationships"):
                        add_finding(
                            findings, "ERROR", "OOXML_EXTERNAL_RELATIONSHIP",
                            "OOXML contains external relationships; remove them and perform any viewing in an offline isolated renderer",
                            item_id=item_id, path=relative,
                        )
                        archive_preflight_ok = False
                    if risky_ooxml.get("active_or_embedded_parts"):
                        add_finding(
                            findings, "ERROR", "OOXML_ACTIVE_OR_EMBEDDED_PART",
                            "OOXML contains ActiveX, OLE, embedded-object, remote-template or external-link parts",
                            item_id=item_id, path=relative,
                        )
                        if any(
                            str(name).lower().endswith("vbaproject.bin")
                            for name in risky_ooxml.get("active_or_embedded_parts", [])
                        ):
                            add_finding(
                                findings, "ERROR", "OFFICE_MACRO",
                                "OOXML/archive contains a VBA project",
                                item_id=item_id, path=relative,
                            )
                        archive_preflight_ok = False
            if archive_preflight_ok:
                try:
                    with zipfile.ZipFile(file_path) as archive:
                        if any(name.lower().endswith("vbaproject.bin") for name in archive.namelist()):
                            add_finding(findings, "ERROR", "OFFICE_MACRO", "OOXML/archive contains a VBA project", item_id=item_id, path=relative)
                except (OSError, zipfile.BadZipFile, NotImplementedError, RuntimeError, ValueError):
                    add_finding(findings, "ERROR", "ZIP_INSPECTION", "ZIP/OOXML macro inspection could not be completed safely", item_id=item_id, path=relative)

        try:
            actual_hash = sha256_file(file_path)
        except (OSError, ValueError) as exc:
            add_finding(findings, "ERROR", "FILE_READ", f"Cannot hash/read file: {exc}", item_id=item_id, path=relative)
            continue
        observed_hashes[actual_hash].append(relative)
        expected_hash = (row.get("sha256") or "").strip().lower()
        if args.submission_mode and not expected_hash:
            add_finding(findings, "ERROR", "HASH_MISSING", f"{item_id} has no sha256", item_id=item_id, path=relative)
        elif expected_hash and not re.fullmatch(r"[0-9a-f]{64}", expected_hash):
            add_finding(findings, "ERROR", "HASH_FORMAT", f"{item_id} sha256 is not 64 lowercase hex characters", item_id=item_id, path=relative)
        elif expected_hash and expected_hash != actual_hash:
            add_finding(findings, "ERROR", "HASH_MISMATCH", f"{item_id} sha256 does not match the file", item_id=item_id, path=relative)
        try:
            if file_path.stat().st_size == 0:
                add_finding(findings, "ERROR", "ZERO_BYTE", "Manifest references a zero-byte file", item_id=item_id, path=relative)
        except OSError as exc:
            add_finding(findings, "ERROR", "FILE_STAT", f"Cannot inspect file metadata: {exc}", item_id=item_id, path=relative)
        payload = ""
        if observed_type not in {"docx", "xlsx", "pptx", "zip", "tar", "gzip"} or archive_preflight_ok:
            try:
                payload = text_payload(file_path)
            except (OSError, zipfile.BadZipFile, KeyError, ValueError, NotImplementedError, RuntimeError) as exc:
                if args.submission_mode and suffix in TEXT_SUFFIXES | {".docx"}:
                    add_finding(findings, "ERROR", "TEXT_SCAN_UNAVAILABLE", f"Could not safely inspect text payload: {exc}", item_id=item_id, path=relative)
        if args.submission_mode and payload and PLACEHOLDER_RE.search(payload):
            add_finding(findings, "ERROR", "PLACEHOLDER", "Unresolved placeholder in file", item_id=item_id, path=relative)

        if suffix == ".docx" and observed_type == "docx" and archive_preflight_ok:
            features = docx_features(file_path)
            if features.get("invalid"):
                add_finding(findings, "ERROR", "DOCX_INSPECTION", "DOCX XML could not be safely and completely inspected", item_id=item_id, path=relative)
            if features.get("comments"):
                add_finding(findings, "ERROR" if args.submission_mode else "WARNING", "DOCX_COMMENTS", "DOCX contains comments", item_id=item_id, path=relative)
            if features.get("tracked_changes") and tracked_policy != "allowed-marked-revision":
                add_finding(findings, "ERROR" if args.submission_mode else "WARNING", "DOCX_TRACKED_CHANGES", "DOCX contains tracked changes but policy does not explicitly allow a marked revision", item_id=item_id, path=relative)
            if blinded and features.get("authors"):
                add_finding(findings, "ERROR", "BLIND_METADATA", "Blinded DOCX contains creator/last-modified-by metadata", item_id=item_id, path=relative)
        if observed_type == "pdf":
            features = pdf_features(file_path)
            if features.get("parser_unavailable"):
                add_finding(findings, "ERROR", "PDF_PARSE_UNAVAILABLE", "A constrained PDF parser is unavailable; PDF openability cannot be proven", item_id=item_id, path=relative)
            if features.get("parse_error"):
                add_finding(
                    findings, "ERROR", "PDF_INTEGRITY",
                    f"PDF object/xref/page-tree parsing failed ({features.get('parse_error_type') or 'unknown'})",
                    item_id=item_id, path=relative,
                )
            if features.get("encrypted"):
                add_finding(findings, "ERROR", "PDF_ENCRYPTED", "PDF is encrypted/password protected", item_id=item_id, path=relative)
            if features.get("active_javascript"):
                add_finding(findings, "ERROR", "PDF_ACTIVE_CONTENT", "PDF contains JavaScript/action content", item_id=item_id, path=relative)
            if blinded and features.get("author_metadata"):
                add_finding(findings, "ERROR", "BLIND_PDF_METADATA", "Blinded PDF contains Author metadata", item_id=item_id, path=relative)

        if args.submission_mode and relative and file_path is not None and file_path.exists():
            if status != "ready":
                add_finding(findings, "ERROR", "NOT_READY", f"{item_id} status is {status}; every present upload file must be ready", item_id=item_id)
            if not (row.get("version") or "").strip():
                add_finding(findings, "ERROR", "VERSION", f"{item_id} has no version", item_id=item_id)
            render_states = {"pass", "not-applicable"} if observed_type in {"zip", "tar", "gzip"} else {"pass"}
            required_qa = {
                "technical_qa": {"pass"}, "render_qa": render_states,
                "content_gate": {"pass"},
                "anonymization_qa": {"pass"} if blinded else {"pass", "not-applicable"},
                "crossfile_qa": {"pass"},
            }
            for qa_field, pass_states in required_qa.items():
                qa_value = (row.get(qa_field) or "").strip().lower()
                if qa_value not in pass_states:
                    add_finding(findings, "ERROR", "QA_NOT_CLOSED", f"{item_id} {qa_field} is {qa_value or '[blank]'}", item_id=item_id)

    for folded, item_ids in path_rows.items():
        if len(item_ids) > 1:
            add_finding(findings, "ERROR", "PATH_DUP", f"Manifest path is claimed by multiple items: {', '.join(item_ids)}", path=folded)
    for folded, path in actual_by_rel.items():
        if folded not in claimed_paths:
            add_finding(findings, "ERROR", "UNMANIFESTED_FILE", "Actual upload-root file is not in the manifest", path=normalized_rel(path, root))
    for digest, paths in observed_hashes.items():
        if len(set(path.casefold() for path in paths)) > 1:
            add_finding(findings, "WARNING", "DUPLICATE_CONTENT", f"Files have identical SHA-256 {digest}: {', '.join(sorted(paths))}")
    name_groups: defaultdict[str, list[str]] = defaultdict(list)
    for path in actual_upload_files:
        name_groups[path.name.casefold()].append(normalized_rel(path, root))
    for paths in name_groups.values():
        if len(paths) > 1:
            add_finding(findings, "ERROR", "FILENAME_DUP", "Duplicate upload filename ignoring case: " + ", ".join(paths))
    if args.submission_mode:
        if active_route is not None:
            manifest_by_rule: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
            for row in rows:
                manifest_by_rule[(row.get("rule_id") or "").strip()].append(row)
            for contract_item in active_route.get("requirements", []):
                if not isinstance(contract_item, dict):
                    add_finding(findings, "ERROR", "ROUTE_CONTRACT", "Route requirement is not an object")
                    continue
                rule_id = str(contract_item.get("rule_id") or "")
                expected_class = str(contract_item.get("requirement_class") or "")
                item_kind = str(contract_item.get("item_kind") or "")
                minimum_rows = int(contract_item.get("minimum_rows") or 1)
                matching_rows = manifest_by_rule.get(rule_id, [])
                if len(matching_rows) < minimum_rows:
                    add_finding(
                        findings, "ERROR", "ROUTE_MATERIAL_MISSING",
                        f"Route requires at least {minimum_rows} manifest row(s) for {rule_id}; found {len(matching_rows)}",
                    )
                    continue
                matching_statuses = {
                    (matched.get("status") or "").strip().lower() for matched in matching_rows
                }
                if expected_class == "conditional" and "not-applicable" in matching_statuses and len(matching_statuses) > 1:
                    add_finding(
                        findings, "ERROR", "ROUTE_CONDITIONAL_STATUS_MIX",
                        f"{rule_id} cannot mix not-applicable and active manifest rows",
                    )
                for matched in matching_rows:
                    matched_item = (matched.get("item_id") or "").strip()
                    matched_class = (matched.get("requirement_class") or "").strip().lower()
                    matched_status = (matched.get("status") or "").strip().lower()
                    matched_path = (matched.get("path") or "").strip()
                    matched_authority = (matched.get("authority_class") or "").strip().upper()
                    allowed_classes = set(contract_item.get("allowed_requirement_classes", [expected_class]))
                    if matched_class not in allowed_classes:
                        add_finding(findings, "ERROR", "ROUTE_CLASS_MISMATCH", f"{matched_item} must use requirement_class {expected_class} for {rule_id}", item_id=matched_item)
                    if item_kind == "portal" and (matched_class != "portal-only" or matched_path):
                        add_finding(findings, "ERROR", "ROUTE_PORTAL_MISMATCH", f"{matched_item} must be a path-free portal-only row", item_id=matched_item)
                    if item_kind == "embedded":
                        if matched_path:
                            add_finding(findings, "ERROR", "ROUTE_EMBEDDED_MISMATCH", f"{matched_item} must be a path-free embedded-content assertion", item_id=matched_item)
                        parent_rule_id = str(contract_item.get("parent_rule_id") or "")
                        parent_rows = manifest_by_rule.get(parent_rule_id, [])
                        if not parent_rule_id or not any(
                            (parent.get("path") or "").strip()
                            and (parent.get("status") or "").strip().lower() != "not-applicable"
                            for parent in parent_rows
                        ):
                            add_finding(
                                findings, "ERROR", "ROUTE_EMBEDDED_PARENT",
                                f"{matched_item} has no active physical parent for embedded rule {rule_id}",
                                item_id=matched_item,
                            )
                    if item_kind == "field":
                        if matched_path:
                            add_finding(
                                findings, "ERROR", "ROUTE_FIELD_MISMATCH",
                                f"{matched_item} must be a path-free cross-file assertion",
                                item_id=matched_item,
                            )
                        if matched_status != "not-applicable":
                            if matched_status != "ready":
                                add_finding(
                                    findings, "ERROR", "ROUTE_FIELD_OPEN",
                                    f"{matched_item} cross-file assertion is not ready",
                                    item_id=matched_item,
                                )
                            pair_receipt_kind = str(contract_item.get("pair_receipt_kind") or "")
                            if pair_receipt_kind == "marked-unmarked-figure":
                                pair_issues = marked_unmarked_pair_receipt_issues(
                                    matched, rows,
                                    {
                                        str(value) for value in contract_item.get("parent_rule_ids", [])
                                        if str(value)
                                    },
                                )
                                if pair_issues:
                                    add_finding(
                                        findings, "ERROR", "ROUTE_FIGURE_PAIR_RECEIPT",
                                        f"{matched_item} marked/unmarked pair receipt is incomplete: "
                                        + "; ".join(pair_issues),
                                        item_id=matched_item,
                                    )
                    if (
                        item_kind == "file"
                        and matched_class in {"required", "conditional"}
                        and matched_status != "not-applicable"
                        and not matched_path
                    ):
                        add_finding(findings, "ERROR", "ROUTE_FILE_MISSING", f"{matched_item} is an active physical route item", item_id=matched_item)
                    if item_kind == "file-or-portal":
                        if (
                            matched_class in {"required", "conditional"}
                            and matched_status != "not-applicable"
                            and not matched_path
                        ):
                            add_finding(findings, "ERROR", "ROUTE_FILE_MISSING", f"{matched_item} selected the attachment route but has no file", item_id=matched_item)
                        if matched_class == "portal-only" and matched_path:
                            add_finding(findings, "ERROR", "ROUTE_PORTAL_MISMATCH", f"{matched_item} selected the portal-text route but claims a file", item_id=matched_item)
                    expected_blinded = contract_item.get("blinded")
                    if expected_blinded is not None and matched_status != "not-applicable":
                        observed_blinded = (matched.get("blinded") or "").strip().lower() in TRUE_VALUES
                        if observed_blinded != bool(expected_blinded):
                            add_finding(findings, "ERROR", "ROUTE_BLINDING_MISMATCH", f"{matched_item} blinded state conflicts with the journal route", item_id=matched_item)
                required_variants = {
                    str(value) for value in contract_item.get("required_revision_variants", [])
                    if str(value)
                }
                if required_variants:
                    observed_variants = {
                        (matched.get("revision_variant") or "").strip().lower()
                        for matched in matching_rows
                        if (matched.get("path") or "").strip()
                        and (matched.get("status") or "").strip().lower() != "not-applicable"
                    }
                    missing_variants = sorted(required_variants - observed_variants)
                    if missing_variants:
                        add_finding(
                            findings, "ERROR", "ROUTE_REVISION_VARIANT_MISSING",
                            f"{rule_id} lacks required revision role(s): {', '.join(missing_variants)}",
                        )
                    hash_roles: defaultdict[str, set[str]] = defaultdict(set)
                    for matched in matching_rows:
                        digest_value = (matched.get("sha256") or "").strip().lower()
                        variant_value = (matched.get("revision_variant") or "").strip().lower()
                        if digest_value and variant_value in required_variants:
                            hash_roles[digest_value].add(variant_value)
                    for digest_value, variants in hash_roles.items():
                        if len(variants) > 1:
                            add_finding(
                                findings, "ERROR", "ROUTE_REVISION_ROLE_DUPLICATE",
                                f"Required revision roles {sorted(variants)} have identical file bytes ({digest_value})",
                            )
                file_set_alternatives = contract_item.get("file_set_alternatives", [])
                if file_set_alternatives:
                    active_file_rows = [
                        matched for matched in matching_rows
                        if (matched.get("path") or "").strip()
                        and (matched.get("status") or "").strip().lower() != "not-applicable"
                    ]
                    observed_extensions = {
                        Path((matched.get("path") or "").strip()).suffix.lower()
                        for matched in active_file_rows
                    }
                    satisfied_alternatives: list[str] = []
                    alternative_receipt_issues: list[str] = []
                    for alternative in file_set_alternatives:
                        if not isinstance(alternative, dict):
                            continue
                        any_extensions = {
                            str(value).lower() for value in alternative.get("any_extensions", [])
                            if str(value)
                        }
                        all_extensions = {
                            str(value).lower() for value in alternative.get("all_extensions", [])
                            if str(value)
                        }
                        notes_required_extensions = {
                            str(value).lower() for value in alternative.get("notes_required_extensions", [])
                            if str(value)
                        }
                        any_ok = not any_extensions or bool(observed_extensions & any_extensions)
                        all_ok = all_extensions.issubset(observed_extensions)
                        notes_ok = all(
                            any(
                                Path((matched.get("path") or "").strip()).suffix.lower() == extension
                                and bool((matched.get("notes") or "").strip())
                                and not PLACEHOLDER_RE.search((matched.get("notes") or "").strip())
                                for matched in active_file_rows
                            )
                            for extension in notes_required_extensions
                        )
                        receipt_ok = True
                        receipt_kind = str(alternative.get("receipt_kind") or "")
                        if receipt_kind == "latex-source-plus-checked-pdf" and any_ok and all_ok:
                            latex_issues = latex_source_receipt_issues(active_file_rows)
                            receipt_ok = not latex_issues
                            alternative_receipt_issues.extend(latex_issues)
                        if any_ok and all_ok and notes_ok and receipt_ok:
                            satisfied_alternatives.append(str(alternative.get("name") or "unnamed"))
                    if not satisfied_alternatives:
                        alternative_names = [
                            str(alternative.get("name") or "unnamed")
                            for alternative in file_set_alternatives if isinstance(alternative, dict)
                        ]
                        add_finding(
                            findings, "ERROR", "ROUTE_FILE_SET_ALTERNATIVE",
                            f"{rule_id} does not satisfy any complete source-file alternative: {', '.join(alternative_names)}",
                        )
                        if alternative_receipt_issues:
                            add_finding(
                                findings, "ERROR", "ROUTE_LATEX_RECEIPT",
                                f"{rule_id} LaTeX provenance receipt is incomplete: "
                                + "; ".join(sorted(set(alternative_receipt_issues))),
                            )
                max_file_bytes = contract_item.get("max_file_bytes")
                max_total_bytes = contract_item.get("max_total_bytes")
                matched_sizes: list[tuple[str, int]] = []
                for matched in matching_rows:
                    matched_relative = (matched.get("path") or "").strip().replace("\\", "/")
                    if not matched_relative:
                        continue
                    try:
                        matched_path = (root / Path(matched_relative)).resolve(strict=True)
                        matched_path.relative_to(root)
                        matched_sizes.append(((matched.get("item_id") or "").strip(), matched_path.stat().st_size))
                    except (OSError, ValueError):
                        continue
                if isinstance(max_file_bytes, int):
                    for matched_item_id, matched_size in matched_sizes:
                        if matched_size > max_file_bytes:
                            add_finding(
                                findings, "ERROR", "ROUTE_FILE_SIZE",
                                f"{matched_item_id} is {matched_size} bytes; route limit is {max_file_bytes}",
                                item_id=matched_item_id,
                            )
                if isinstance(max_total_bytes, int):
                    total_size = sum(size for _, size in matched_sizes)
                    if total_size > max_total_bytes:
                        add_finding(
                            findings, "ERROR", "ROUTE_RULE_TOTAL_SIZE",
                            f"{rule_id} files total {total_size} bytes; route limit is {max_total_bytes}",
                        )
                if contract_item.get("resolution_required"):
                    active_resolution_rows = [
                        row for row in matching_rows
                        if (row.get("status") or "").strip().lower() != "not-applicable"
                    ]
                    resolved_rows = [
                        row for row in active_resolution_rows
                        if (row.get("authority_class") or "").strip().upper() == "PORTAL_CURRENT"
                        and (row.get("status") or "").strip().lower() in {"ready", "portal-entry"}
                        and source_route_allowed(
                            (row.get("journal_id") or "").strip(),
                            (row.get("source_url") or "").strip(),
                        )
                        and not portal_receipt_issues(row)
                    ]
                    if active_resolution_rows and not resolved_rows:
                        add_finding(
                            findings, "ERROR", "ROUTE_CURRENT_UNRESOLVED",
                            f"{rule_id} requires a captured exact-journal current portal resolution; a decision letter must first be human-adjudicated into the validated registry/contract",
                        )
            route_max_package = active_route.get("max_package_bytes")
            if isinstance(route_max_package, int):
                package_bytes = sum(path.stat().st_size for path in actual_upload_files if path.is_file())
                if package_bytes > route_max_package:
                    add_finding(
                        findings, "ERROR", "ROUTE_PACKAGE_SIZE",
                        f"Upload package totals {package_bytes} bytes; route limit is {route_max_package}",
                    )
        if not any(
            (row.get("requirement_class") or "").strip().lower() in {"required", "conditional", "optional"}
            and (row.get("path") or "").strip()
            for row in rows
        ):
            add_finding(findings, "ERROR", "NO_UPLOAD_FILE_ROW", "Submission manifest contains no physical upload-file row")
        if not actual_upload_files:
            add_finding(findings, "ERROR", "NO_UPLOAD_FILE", "Submission root contains no physical upload file")
        if len(journal_values) != 1:
            add_finding(findings, "ERROR", "JOURNAL_MIX", f"Manifest must resolve to exactly one journal_id; found {sorted(journal_values)}")
        if len(article_values) != 1:
            add_finding(findings, "ERROR", "ARTICLE_TYPE_MIX", f"Manifest must resolve to exactly one article_type; found {sorted(article_values)}")
        if len(stage_values) != 1:
            add_finding(findings, "ERROR", "STAGE_MIX", f"Manifest must resolve to exactly one submission_stage; found {sorted(stage_values)}")
        if len(study_design_values) != 1:
            add_finding(findings, "ERROR", "STUDY_DESIGN_MIX", f"Manifest must resolve to one package-level study_design set; found {sorted(study_design_values)}")
        if len(review_model_values) != 1:
            add_finding(findings, "ERROR", "REVIEW_MODEL_MIX", f"Manifest must resolve to exactly one review_model; found {sorted(review_model_values)}")
        if len(project_id_values) != 1:
            add_finding(findings, "ERROR", "PROJECT_ID_MIX", f"Manifest must resolve to exactly one project_id; found {sorted(project_id_values)}")
        if len(study_scope_values) != 1:
            add_finding(
                findings, "ERROR", "STUDY_SCOPE_MIX",
                f"Manifest must resolve to exactly one study_scope; found {sorted(study_scope_values)}",
            )
        for digest_name, values, finding_code in (
            ("project_state_digest", project_state_digest_values, "PROJECT_STATE_DIGEST_MIX"),
            ("modality_role_digest", modality_role_digest_values, "MODALITY_ROLE_DIGEST_MIX"),
            (
                "scientific_handoff_packet_digest",
                scientific_handoff_packet_digest_values,
                "SCIENTIFIC_HANDOFF_PACKET_DIGEST_MIX",
            ),
            (
                "scientific_prereview_receipt_digest",
                scientific_prereview_receipt_digest_values,
                "SCIENTIFIC_PREREVIEW_RECEIPT_DIGEST_MIX",
            ),
        ):
            if len(values) != 1:
                add_finding(
                    findings, "ERROR", finding_code,
                    f"Manifest must resolve to exactly one {digest_name}; found {sorted(values)}",
                )
        if len(analysis_lock_digest_values) != 1:
            add_finding(
                findings, "ERROR", "ANALYSIS_LOCK_DIGEST_MIX",
                f"Manifest must resolve to exactly one analysis_lock_digest; found {sorted(analysis_lock_digest_values)}",
            )
        if len(claim_registry_digest_values) != 1:
            add_finding(
                findings, "ERROR", "CLAIM_REGISTRY_DIGEST_MIX",
                f"Manifest must resolve to exactly one claim_registry_digest; found {sorted(claim_registry_digest_values)}",
            )
        if len(response_package_digest_values) != 1:
            add_finding(
                findings, "ERROR", "RESPONSE_PACKAGE_DIGEST_MIX",
                f"Manifest must resolve to exactly one response_package_digest; found {sorted(response_package_digest_values)}",
            )
    return emit_report(
        root, manifest_path, rows, actual_upload_files, findings,
        scope=args.scope, active_route=active_route,
        evidence_provenance=evidence_provenance,
    )


def emit_report(
    root: Path, manifest_path: Path, rows: Iterable[dict[str, str]],
    actual_files: Iterable[Path], findings: list[dict[str, object]],
    *, scope: str, active_route: dict[str, object] | None,
    evidence_provenance: dict[str, object] | None = None,
    manifest_trusted: bool = True,
) -> int:
    rows_list = list(rows)
    files_list = list(actual_files)
    manifest_receipt: dict[str, object]
    package_inventory_receipt: dict[str, object]
    try:
        if not manifest_trusted:
            raise ValueError("manifest path was rejected before read authorization")
        manifest_sha256, manifest_bytes = bounded_sha256(manifest_path, max_bytes=10_000_000)
        manifest_receipt = {
            "path": str(manifest_path), "bytes": manifest_bytes,
            "sha256": manifest_sha256, "state": "VERIFIED_CURRENT_FILE",
        }
        manifest_rel = normalized_rel(manifest_path, root)
        snapshot = inventory_snapshot(root, excluded_relpaths=[manifest_rel])
        package_inventory_receipt = {
            key: snapshot[key] for key in ("algorithm", "file_count", "total_bytes", "sha256", "limits")
        }
        package_inventory_receipt["state"] = "VERIFIED_CURRENT_FILES"
    except (OSError, ValueError) as exc:
        add_finding(
            findings, "ERROR", "PACKAGE_SNAPSHOT",
            f"Could not bind the report to a bounded current package snapshot: {exc}",
        )
        manifest_receipt = {"path": str(manifest_path), "state": "NOT_VERIFIED"}
        package_inventory_receipt = {
            "state": "NOT_VERIFIED",
            "limits": {
                "max_files": MAX_INVENTORY_FILES,
                "max_file_bytes": MAX_INVENTORY_FILE_BYTES,
                "max_total_bytes": MAX_INVENTORY_TOTAL_BYTES,
            },
        }
    errors = sum(item["severity"] == "ERROR" for item in findings)
    warnings = sum(item["severity"] == "WARNING" for item in findings)
    portal_actions = sum(
        (row.get("requirement_class") or "").strip().lower() == "portal-only"
        and (row.get("status") or "").strip().lower() != "ready"
        for row in rows_list
    )
    inventory_blockers = [item for item in findings if item.get("code") in INVENTORY_BLOCK_CODES]
    if inventory_blockers:
        inventory_coverage = "INVENTORY_NOT_CLOSED"
    elif scope == "upload-root":
        inventory_coverage = "INVENTORY_CLOSED"
    elif scope == "attachment-set":
        inventory_coverage = "ATTACHMENT_SET_CLOSED"
    else:
        inventory_coverage = "INVENTORY_PARTIAL"
    if errors:
        readiness_hint = "BLOCKED"
    elif scope != "upload-root":
        readiness_hint = "SCOPED_FILES_PASS_PACKAGE_INCOMPLETE"
    elif portal_actions:
        readiness_hint = "STRUCTURAL_UPLOAD_FILES_PASS_PORTAL_ACTIONS_REMAIN"
    else:
        readiness_hint = "STRUCTURAL_PACKAGE_GATES_PASS_HUMAN_GATES_REMAIN"
    route_values = {
        "journal_id": sorted({(row.get("journal_id") or "").strip() for row in rows_list if (row.get("journal_id") or "").strip()}),
        "article_type": sorted({(row.get("article_type") or "").strip() for row in rows_list if (row.get("article_type") or "").strip()}),
        "stage": sorted({(row.get("submission_stage") or "").strip() for row in rows_list if (row.get("submission_stage") or "").strip()}),
        "study_design": sorted({(row.get("study_design") or "").strip() for row in rows_list if (row.get("study_design") or "").strip()}),
        "review_model": sorted({(row.get("review_model") or "").strip() for row in rows_list if (row.get("review_model") or "").strip()}),
    }
    upstream_provenance = {
        "project_id": sorted({
            (row.get("project_id") or "").strip()
            for row in rows_list if (row.get("project_id") or "").strip()
        }),
        "study_scope": sorted({
            (row.get("study_scope") or "").strip()
            for row in rows_list if (row.get("study_scope") or "").strip()
        }),
        "project_state_digest": sorted({
            (row.get("project_state_digest") or "").strip()
            for row in rows_list if (row.get("project_state_digest") or "").strip()
        }),
        "modality_role_digest": sorted({
            (row.get("modality_role_digest") or "").strip()
            for row in rows_list if (row.get("modality_role_digest") or "").strip()
        }),
        "scientific_handoff_packet_digest": sorted({
            (row.get("scientific_handoff_packet_digest") or "").strip()
            for row in rows_list
            if (row.get("scientific_handoff_packet_digest") or "").strip()
        }),
        "scientific_prereview_receipt_digest": sorted({
            (row.get("scientific_prereview_receipt_digest") or "").strip()
            for row in rows_list
            if (row.get("scientific_prereview_receipt_digest") or "").strip()
        }),
        "source_artifact_ids": sorted({
            (row.get("source_artifact_id") or "").strip()
            for row in rows_list if (row.get("source_artifact_id") or "").strip()
        }),
        "analysis_lock_digest": sorted({
            (row.get("analysis_lock_digest") or "").strip()
            for row in rows_list if (row.get("analysis_lock_digest") or "").strip()
        }),
        "claim_registry_digest": sorted({
            (row.get("claim_registry_digest") or "").strip()
            for row in rows_list if (row.get("claim_registry_digest") or "").strip()
        }),
        "response_package_digest": sorted({
            (row.get("response_package_digest") or "").strip()
            for row in rows_list if (row.get("response_package_digest") or "").strip()
        }),
        "authentication": "NOT_PERFORMED",
        "boundary": (
            "These values are manifest foreign-key receipts only; study scope and scientific-handoff "
            "digests preserve package-level identity, but this auditor checks syntax and within-package "
            "consistency only and does not authenticate or reconstruct the upstream records"
        ),
    }
    try:
        bundled_route_path = BUNDLED_ROUTE_MATRIX_PATH.resolve(strict=True)
        route_contract_registry: dict[str, object] = {
            "path": str(bundled_route_path),
            "sha256": sha256_file(bundled_route_path),
            "custom_route_matrix_allowed": False,
        }
    except OSError as exc:
        route_contract_registry = {
            "path": str(BUNDLED_ROUTE_MATRIX_PATH.resolve()),
            "sha256": None,
            "custom_route_matrix_allowed": False,
            "provenance_error": str(exc),
        }
    if errors:
        whole_package_readiness = "BLOCKED_STRUCTURAL"
    elif scope != "upload-root":
        whole_package_readiness = "INCOMPLETE_SCOPE"
    else:
        whole_package_readiness = "HUMAN_GATES_REQUIRED"
    report = {
        "tool": "radiology-submission structural auditor",
        "schema_version": SCHEMA_VERSION,
        "package_dir": str(root),
        "manifest": str(manifest_path),
        "manifest_receipt": manifest_receipt,
        "package_inventory_receipt": package_inventory_receipt,
        "evidence_registry": evidence_provenance,
        "route_contract_registry": route_contract_registry,
        "upstream_provenance": upstream_provenance,
        "execution_status": "PASS" if errors == 0 else "FAIL",
        "status": "PASS" if errors == 0 else "FAIL",
        "whole_package_readiness": whole_package_readiness,
        "readiness_hint": readiness_hint,
        "route": {
            **route_values,
            "contract_matched": active_route is not None,
            "minimum_material_contract": "PASS" if active_route is not None and errors == 0 else "FAIL",
        },
        "inventory": {
            "manifest_rows": len(rows_list), "actual_upload_files": len(files_list),
            "declared_scope": scope,
            "coverage": inventory_coverage,
            "blocking_findings": len(inventory_blockers),
        },
        "counts": {
            "errors": errors, "warnings": warnings,
            "portal_actions": portal_actions,
            "manifest_open_portal_actions": portal_actions,
        },
        "limitations": [
            "Minimum-material-contract PASS covers only the bundled validated matrix and deterministic structural gates; profile content checks, exact-journal live-portal requirements and human-adjudicated decision letters remain additive",
            "No scientific-validity certification", "No visual/render certification",
            "No live-portal completion certification",
            "Upstream project-state, modality-role, handoff, prereview, analysis, claim and response digests are consistency receipts, not proof that the cited records are authentic or scientifically valid",
        ],
        "findings": findings,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
