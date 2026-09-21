#!/usr/bin/env python3
"""Render structural-audit JSON into a human-review Markdown draft.

The renderer preserves the machine state verbatim and intentionally cannot
issue READY. It is a presentation adapter, not a second auditor.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from audit_submission_package import INVENTORY_BLOCK_CODES, SCHEMA_VERSION
from submission_security import (
    atomic_write_text,
    authorized_package_root,
    bounded_sha256,
    ensure_output_path_safe,
    inventory_snapshot,
    is_linklike,
    load_json_strict,
    reject_duplicate_pairs,
)


MAX_REPORT_BYTES = 20_000_000
MACHINE_STATES = {"BLOCKED_STRUCTURAL", "INCOMPLETE_SCOPE", "HUMAN_GATES_REQUIRED"}
SCOPES = {"upload-root", "attachment-set", "partial"}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
AUDITOR = Path(__file__).with_name("audit_submission_package.py")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render structural audit JSON for human submission review")
    parser.add_argument("audit_json", help="JSON emitted by audit_submission_package.py")
    parser.add_argument(
        "--package-root", required=True,
        help="Explicit user-authorized package root; must exactly match the audited package",
    )
    parser.add_argument(
        "--expected-audit-sha256", required=True,
        help="Nonzero lowercase SHA-256 captured from the exact audit JSON to render",
    )
    parser.add_argument("--output", help="Optional Markdown output path outside the upload package")
    parser.add_argument("--force", action="store_true", help="Replace an existing renderer-owned report")
    return parser.parse_args()


def load_report(path: Path) -> dict[str, Any]:
    report = load_json_strict(path, max_bytes=MAX_REPORT_BYTES)
    if report.get("tool") != "radiology-submission structural auditor":
        raise ValueError("input is not a radiology-submission structural-auditor report")
    return report


def _nonnegative_integer(value: object, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"audit report {name} must be a nonnegative integer")
    return value


def _nonzero_sha(value: object, name: str) -> str:
    text = str(value or "")
    if not SHA256_RE.fullmatch(text) or set(text) == {"0"}:
        raise ValueError(f"audit report {name} must be a nonzero lowercase SHA-256")
    return text


def _outside(path: Path, root: Path, label: str) -> None:
    try:
        path.resolve(strict=False).relative_to(root)
    except ValueError:
        return
    raise ValueError(f"{label} must be outside the authorized package root")


def validate_report(
    report: dict[str, Any], source: Path, package_root: Path, expected_audit_sha256: str,
) -> None:
    expected = _nonzero_sha(expected_audit_sha256, "expected audit JSON digest")
    observed, _ = bounded_sha256(source, max_bytes=MAX_REPORT_BYTES)
    if observed != expected:
        raise ValueError("audit JSON SHA-256 does not match --expected-audit-sha256")
    _outside(source, package_root, "audit JSON")
    if report.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(f"audit report schema_version must equal {SCHEMA_VERSION}")
    recorded_root = authorized_package_root(str(report.get("package_dir") or ""))
    if recorded_root != package_root:
        raise ValueError("audit report package_dir does not match the explicit authorized package root")

    findings = report.get("findings")
    counts = report.get("counts")
    inventory = report.get("inventory")
    route = report.get("route")
    if not isinstance(findings, list) or not isinstance(counts, dict):
        raise ValueError("audit report findings/counts are malformed")
    if not isinstance(inventory, dict) or not isinstance(route, dict):
        raise ValueError("audit report inventory/route are malformed")
    for finding in findings:
        if not isinstance(finding, dict) or finding.get("severity") not in {"ERROR", "WARNING"}:
            raise ValueError("audit report contains a malformed finding")
    actual_errors = sum(item.get("severity") == "ERROR" for item in findings)
    actual_warnings = sum(item.get("severity") == "WARNING" for item in findings)
    errors = _nonnegative_integer(counts.get("errors"), "counts.errors")
    warnings = _nonnegative_integer(counts.get("warnings"), "counts.warnings")
    _nonnegative_integer(counts.get("portal_actions"), "counts.portal_actions")
    manifest_portal_actions = _nonnegative_integer(
        counts.get("manifest_open_portal_actions"), "counts.manifest_open_portal_actions",
    )
    if manifest_portal_actions != counts.get("portal_actions"):
        raise ValueError("audit report portal-action count aliases conflict")
    if (errors, warnings) != (actual_errors, actual_warnings):
        raise ValueError("audit report counts do not match findings")

    scope = inventory.get("declared_scope")
    if scope not in SCOPES:
        raise ValueError("audit report has an invalid declared scope")
    _nonnegative_integer(inventory.get("manifest_rows"), "inventory.manifest_rows")
    _nonnegative_integer(inventory.get("actual_upload_files"), "inventory.actual_upload_files")
    observed_inventory_blockers = sum(
        item.get("code") in INVENTORY_BLOCK_CODES for item in findings
    )
    if inventory.get("blocking_findings") != observed_inventory_blockers:
        raise ValueError("audit inventory blocking_findings conflicts with findings")
    expected_coverage = (
        "INVENTORY_NOT_CLOSED" if observed_inventory_blockers else
        "INVENTORY_CLOSED" if scope == "upload-root" else
        "ATTACHMENT_SET_CLOSED" if scope == "attachment-set" else
        "INVENTORY_PARTIAL"
    )
    if inventory.get("coverage") != expected_coverage:
        raise ValueError("audit inventory coverage conflicts with scope/findings")
    expected_status = "PASS" if errors == 0 else "FAIL"
    if report.get("status") != expected_status:
        raise ValueError("audit report status conflicts with error count")
    if report.get("execution_status") != expected_status:
        raise ValueError("audit report execution_status conflicts with error count")
    expected_machine = (
        "BLOCKED_STRUCTURAL" if errors else
        "INCOMPLETE_SCOPE" if scope != "upload-root" else
        "HUMAN_GATES_REQUIRED"
    )
    if report.get("whole_package_readiness") != expected_machine:
        raise ValueError("audit report whole_package_readiness conflicts with counts/scope")
    if report.get("whole_package_readiness") not in MACHINE_STATES:
        raise ValueError("audit report has an unknown whole_package_readiness state")
    contract_matched = route.get("contract_matched")
    if not isinstance(contract_matched, bool):
        raise ValueError("audit report route.contract_matched must be boolean")
    expected_contract = "PASS" if contract_matched and errors == 0 else "FAIL"
    if route.get("minimum_material_contract") != expected_contract:
        raise ValueError("audit report minimum-material state conflicts with route/errors")

    manifest_value = str(report.get("manifest") or "")
    manifest = Path(manifest_value).resolve(strict=True)
    try:
        manifest_rel = manifest.relative_to(package_root).as_posix()
    except ValueError as exc:
        raise ValueError("audit report manifest escapes the authorized package root") from exc
    if not manifest.is_file() or is_linklike(manifest):
        raise ValueError("audit report manifest is not a regular non-link file")
    manifest_receipt = report.get("manifest_receipt")
    if not isinstance(manifest_receipt, dict):
        raise ValueError("audit report lacks a manifest_receipt")
    if manifest_receipt.get("state") != "VERIFIED_CURRENT_FILE":
        raise ValueError("manifest_receipt is not in VERIFIED_CURRENT_FILE state")
    manifest_digest, manifest_bytes = bounded_sha256(manifest, max_bytes=10_000_000)
    if Path(str(manifest_receipt.get("path") or "")).resolve(strict=False) != manifest:
        raise ValueError("manifest_receipt path conflicts with the report manifest")
    if manifest_receipt.get("bytes") != manifest_bytes:
        raise ValueError("manifest bytes changed after structural audit")
    if _nonzero_sha(manifest_receipt.get("sha256"), "manifest_receipt.sha256") != manifest_digest:
        raise ValueError("manifest SHA-256 changed after structural audit")

    package_receipt = report.get("package_inventory_receipt")
    if not isinstance(package_receipt, dict):
        raise ValueError("audit report lacks a package_inventory_receipt")
    if package_receipt.get("state") != "VERIFIED_CURRENT_FILES":
        raise ValueError("package_inventory_receipt is not in VERIFIED_CURRENT_FILES state")
    snapshot = inventory_snapshot(package_root, excluded_relpaths=[manifest_rel])
    for key in ("file_count", "total_bytes", "sha256", "algorithm"):
        if package_receipt.get(key) != snapshot.get(key):
            raise ValueError(f"package inventory {key} changed after structural audit")
    if inventory.get("actual_upload_files") != snapshot["file_count"]:
        raise ValueError("audit inventory file count conflicts with the current package snapshot")

    for registry_name in ("evidence_registry", "route_contract_registry"):
        registry = report.get(registry_name)
        if not isinstance(registry, dict):
            raise ValueError(f"audit report lacks {registry_name}")
        _nonzero_sha(registry.get("sha256"), f"{registry_name}.sha256")
    provenance = report.get("upstream_provenance")
    if not isinstance(provenance, dict) or provenance.get("authentication") != "NOT_PERFORMED":
        raise ValueError("audit report upstream provenance is malformed")
    for key, values in provenance.items():
        if not (key.endswith("_digest") or key.endswith("_sha256")):
            continue
        if not isinstance(values, list):
            raise ValueError(f"upstream provenance {key} must be an array")
        for value in values:
            if value == "not-applicable" and key in {
                "response_package_digest", "scientific_prereview_receipt_digest",
            }:
                continue
            _nonzero_sha(value, f"upstream_provenance.{key}")


def authoritative_rerun(report: dict[str, Any], package_root: Path) -> dict[str, Any]:
    """Re-run the bundled auditor and require semantic identity with the input JSON."""
    manifest = Path(str(report.get("manifest") or "")).resolve(strict=True)
    manifest_rel = manifest.relative_to(package_root).as_posix()
    scope = str(report.get("inventory", {}).get("declared_scope") or "")
    completed = subprocess.run(
        [
            sys.executable, str(AUDITOR), str(package_root),
            "--manifest", manifest_rel,
            "--submission-mode", "--scope", scope,
        ],
        check=False, capture_output=True, text=True, encoding="utf-8",
    )
    if completed.returncode not in {0, 1}:
        raise ValueError(
            "authoritative structural-auditor rerun failed: "
            + (completed.stderr.strip() or f"exit {completed.returncode}")
        )
    if len(completed.stdout.encode("utf-8")) > MAX_REPORT_BYTES:
        raise ValueError("authoritative structural-auditor rerun exceeded the report-size limit")
    try:
        fresh = json.loads(completed.stdout, object_pairs_hook=reject_duplicate_pairs)
    except (json.JSONDecodeError, ValueError) as exc:
        raise ValueError(f"authoritative structural-auditor rerun emitted invalid JSON: {exc}") from exc
    if not isinstance(fresh, dict):
        raise ValueError("authoritative structural-auditor rerun did not emit an object")
    if fresh != report:
        raise ValueError(
            "audit JSON does not exactly match an authoritative current rerun; preserve the new rerun JSON and review changed findings"
        )
    return fresh


def cell(value: object) -> str:
    text = str(value if value is not None else "")
    text = text.replace("\r", " ").replace("\n", " ").strip()
    escaped: list[str] = []
    markdown_chars = "\\`*_{}[]()#+-.!|~"
    for character in text:
        if ord(character) < 32 or ord(character) == 127 or character in markdown_chars:
            escaped.append(f"&#{ord(character)};")
        else:
            escaped.append(html.escape(character, quote=False))
    return "".join(escaped)


def joined(value: object) -> str:
    if isinstance(value, list):
        return "; ".join(cell(item) for item in value) or "[none]"
    return cell(value) or "[none]"


def review_queue_state(report: dict[str, Any]) -> str:
    machine = report.get("whole_package_readiness")
    if machine == "BLOCKED_STRUCTURAL":
        return "BLOCKED"
    if machine == "INCOMPLETE_SCOPE":
        return "INCOMPLETE"
    return "HUMAN_REVIEW_REQUIRED"


def render(report: dict[str, Any], source_path: Path) -> str:
    route = report.get("route") if isinstance(report.get("route"), dict) else {}
    inventory = report.get("inventory") if isinstance(report.get("inventory"), dict) else {}
    counts = report.get("counts") if isinstance(report.get("counts"), dict) else {}
    provenance = report.get("upstream_provenance") if isinstance(report.get("upstream_provenance"), dict) else {}
    evidence = report.get("evidence_registry") if isinstance(report.get("evidence_registry"), dict) else {}
    contract = report.get("route_contract_registry") if isinstance(report.get("route_contract_registry"), dict) else {}
    findings = report.get("findings") if isinstance(report.get("findings"), list) else []
    limitations = report.get("limitations") if isinstance(report.get("limitations"), list) else []
    queue_state = review_queue_state(report)
    lines = [
        "# Submission package human-review draft",
        "",
        "> This document is generated from a structural audit. It is not a submission certificate and cannot issue READY.",
        "",
        "## Review queue state",
        "",
        f"- Human review queue: `{queue_state}`",
        f"- Machine execution status: `{cell(report.get('execution_status'))}`",
        f"- Machine status: `{cell(report.get('status'))}`",
        f"- Machine whole-package state: `{cell(report.get('whole_package_readiness'))}`",
        f"- Minimum-material contract: `{cell(route.get('minimum_material_contract'))}`",
        f"- Structural audit JSON SHA-256: `{bounded_sha256(source_path, max_bytes=MAX_REPORT_BYTES)[0]}`",
        "- Authoritative bundled-auditor rerun: `MATCHED_EXACTLY`",
        "",
        "The human queue state above is a routing state only. A qualified reviewer must authenticate sources, inspect rendered artifacts and close scientific, ethical, anonymization, cross-file and live-portal gates before assigning a final submission verdict.",
        "",
        "## Route and scope",
        "",
        "| Field | Recorded value |",
        "|---|---|",
        f"| Journal | {joined(route.get('journal_id'))} |",
        f"| Article type | {joined(route.get('article_type'))} |",
        f"| Stage | {joined(route.get('stage'))} |",
        f"| Study design | {joined(route.get('study_design'))} |",
        f"| Review model | {joined(route.get('review_model'))} |",
        f"| Declared scope | {cell(inventory.get('declared_scope'))} |",
        f"| Inventory coverage | {cell(inventory.get('coverage'))} |",
        f"| Manifest rows | {cell(inventory.get('manifest_rows'))} |",
        f"| Upload files | {cell(inventory.get('actual_upload_files'))} |",
        "",
        "## Upstream scientific-version receipts",
        "",
        "| Receipt | Recorded value |",
        "|---|---|",
        f"| Project ID | {joined(provenance.get('project_id'))} |",
        f"| Study scope | {joined(provenance.get('study_scope'))} |",
        f"| Source artifact IDs | {joined(provenance.get('source_artifact_ids'))} |",
        f"| Analysis lock digest | {joined(provenance.get('analysis_lock_digest'))} |",
        f"| Claim registry digest | {joined(provenance.get('claim_registry_digest'))} |",
        f"| Response package digest | {joined(provenance.get('response_package_digest'))} |",
        f"| Project-state digest | {joined(provenance.get('project_state_digest'))} |",
        f"| Modality-role digest | {joined(provenance.get('modality_role_digest'))} |",
        f"| Scientific-handoff packet digest | {joined(provenance.get('scientific_handoff_packet_digest'))} |",
        f"| Scientific-prereview receipt digest | {joined(provenance.get('scientific_prereview_receipt_digest'))} |",
        f"| Upstream authentication | {cell(provenance.get('authentication')) or 'NOT_PERFORMED'} |",
        "",
        cell(provenance.get("boundary")) or "Upstream records were not authenticated by this structural audit.",
        "",
        "## Registry receipts",
        "",
        f"- Evidence registry: `{cell(evidence.get('path'))}` — SHA-256 `{cell(evidence.get('sha256'))}`",
        f"- Route contract registry: `{cell(contract.get('path'))}` — SHA-256 `{cell(contract.get('sha256'))}`",
        "",
        "## Structural findings",
        "",
        f"Recorded errors: `{cell(counts.get('errors'))}`; warnings: `{cell(counts.get('warnings'))}`; open portal actions: `{cell(counts.get('portal_actions'))}`.",
        "",
    ]
    if findings:
        lines.extend([
            "| Severity | Code | Item / path | Finding |",
            "|---|---|---|---|",
        ])
        for finding in findings:
            if not isinstance(finding, dict):
                continue
            locator = cell(finding.get("item_id") or finding.get("path") or "package")
            lines.append(
                f"| {cell(finding.get('severity'))} | {cell(finding.get('code'))} | {locator} | {cell(finding.get('message'))} |"
            )
    else:
        lines.append("No finding was emitted by the structural scan. This does not close any human gate.")
    lines.extend([
        "",
        "## Mandatory human gates",
        "",
        "- [ ] Confirm the exact journal, article type, stage, decision-letter instructions and current logged-in portal requirements.",
        "- [ ] Authenticate the official-source captures and all manifest N/A or portal receipts.",
        "- [ ] Open and render every human-facing file; inspect every page, figure, table, supplement and response item.",
        "- [ ] Verify scientific claims, statistics, reporting standards, ethics, image integrity and mechanism-claim ceilings.",
        "- [ ] Verify anonymization, identities, versions, values, callouts, declarations and revision promises across files.",
        "- [ ] Authenticate the analysis-lock, claim-registry and response-package digests against frozen upstream records.",
        "- [ ] Record a human final verdict and reviewer identity separately; do not overwrite the machine state.",
        "",
        "## Machine limitations carried forward",
        "",
    ])
    if limitations:
        lines.extend(f"- {cell(item)}" for item in limitations)
    else:
        lines.append("- No limitations array was present; treat the review as incomplete.")
    lines.extend([
        "",
        "## Human reviewer decision record",
        "",
        "- Reviewer: `[required]`",
        "- Review date: `[required]`",
        "- Current-guide and portal evidence locators: `[required]`",
        "- Render evidence locators: `[required]`",
        "- Scientific/prereview closure receipt: `[required]`",
        "- Final human verdict: `[not assigned by renderer]`",
        "- Remaining blockers and exact repairs: `[required]`",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    try:
        package_root = authorized_package_root(args.package_root)
        source = Path(args.audit_json).expanduser().resolve(strict=True)
        if not source.is_file() or is_linklike(source):
            raise ValueError("audit JSON must be a regular non-link file")
        report = load_report(source)
        validate_report(report, source, package_root, args.expected_audit_sha256)
        report = authoritative_rerun(report, package_root)
        markdown = render(report, source)
        if args.output:
            output = ensure_output_path_safe(Path(args.output), forbidden_root=package_root)
            if output.exists() and not args.force:
                raise ValueError(f"refusing to replace existing report without --force: {output}")
            if output.exists() and args.force:
                if output.stat().st_size > MAX_REPORT_BYTES:
                    raise ValueError("--force may replace only a bounded renderer-owned Markdown report")
                with output.open(encoding="utf-8") as handle:
                    prefix = handle.read(256)
                if not prefix.startswith(
                    "# Submission package human-review draft\n\n"
                    "> This document is generated from a structural audit."
                ):
                    raise ValueError("--force may replace only a renderer-owned Markdown report")
            atomic_write_text(output, markdown, encoding="utf-8")
        else:
            print(markdown)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
