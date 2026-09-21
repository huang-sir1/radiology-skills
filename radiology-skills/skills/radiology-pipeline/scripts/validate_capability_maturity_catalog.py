#!/usr/bin/env python3
"""Validate the machine-readable capability maturity catalog.

This is a governance validator. It does not execute or substitute for a Skill's
dedicated capability tests, source refresh, human behavior adjudication, or
release-artifact verification.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
DEFAULT_REGISTRY = (
    ROOT
    / "skills"
    / "radiology-pipeline"
    / "references"
    / "capability-maturity-registry.json"
)
DEFAULT_README = ROOT / "README.md"

MATURITY_LABELS = {"CONTRACTED", "EXPERIMENTAL", "VALIDATED"}
FRAMEWORK_STATES = {"PLANNED", "CONTRACTED"}
BOUNDARY_STATES = {"NOT_DEFINED", "CONTRACT_DEFINED", "BOUNDARY_VERIFIED"}
CONTENT_STATES = {"SKELETON", "PARTIAL", "IMPLEMENTED"}
EXECUTABLE_STATES = {
    "NOT_PRESENT",
    "STATIC_CONTRACT_ONLY",
    "EXECUTABLE_PASS_CURRENT_TREE",
}
BEHAVIOR_STATES = {"NOT_RUN", "NOT_ADJUDICATED", "QUALIFIED_HUMAN_PASS"}
SOURCE_STATES = {
    "NOT_ASSESSED",
    "STATIC_SNAPSHOT",
    "LIVE_REFRESH_REQUIRED",
    "CURRENT_VERIFIED",
    "NOT_APPLICABLE",
}
RELEASE_ARTIFACT_STATES = {"NOT_RECORDED", "HASH_MANIFEST_VERIFIED"}
EVIDENCE_KEYS = {
    "contract",
    "static_checks",
    "executable_tests",
    "executable_receipts",
    "behavior",
    "source",
    "release_artifact",
}
VALIDATED_PATH_FIELDS = {
    "dedicated_gate_receipt",
    "source_verification_receipt",
    "behavior_adjudication_receipt",
    "adjudicator_qualification_evidence",
    "release_artifact_manifest",
}
VALIDATED_IDENTITY_FIELDS = {
    "behavior_run_identity",
    "release_artifact_id",
    "release_artifact_sha256",
    "toolchain_identity",
}
SKILL_ID = re.compile(r"^radiology-[a-z0-9]+(?:-[a-z0-9]+)*$")


class DuplicateKeyError(ValueError):
    """Raised when JSON contains a duplicate object key."""


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_registry(path: Path) -> dict[str, Any]:
    payload = json.loads(
        path.read_text(encoding="utf-8"), object_pairs_hook=_reject_duplicate_keys
    )
    if not isinstance(payload, dict):
        raise ValueError("registry root must be a JSON object")
    return payload


def _is_safe_relative_path(value: str) -> bool:
    path = Path(value)
    return bool(value) and not path.is_absolute() and ".." not in path.parts


def _path_within_root(root: Path, value: str) -> Path | None:
    if not _is_safe_relative_path(value):
        return None
    candidate = (root / value).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        return None
    return candidate


def _runtime_skill_ids(root: Path, runtime_root: str) -> set[str]:
    skills_root = root / runtime_root
    if not skills_root.is_dir():
        return set()
    return {
        child.name
        for child in skills_root.iterdir()
        if child.is_dir() and (child / "SKILL.md").is_file()
    }


def _readme_index(readme_text: str) -> str:
    marker = "## 技能索引"
    start = readme_text.find(marker)
    if start < 0:
        return ""
    match = re.search(r"^## (?!技能索引).+$", readme_text[start + len(marker) :], re.MULTILINE)
    if match is None:
        return readme_text[start:]
    end = start + len(marker) + match.start()
    return readme_text[start:end]


def _validate_evidence(
    skill_id: str, entry: dict[str, Any], root: Path, errors: list[str]
) -> dict[str, list[str]] | None:
    evidence = entry.get("evidence")
    if not isinstance(evidence, dict):
        errors.append(f"{skill_id}: evidence must be an object")
        return None
    missing_keys = EVIDENCE_KEYS - set(evidence)
    extra_keys = set(evidence) - EVIDENCE_KEYS
    if missing_keys:
        errors.append(f"{skill_id}: missing evidence keys {sorted(missing_keys)}")
    if extra_keys:
        errors.append(f"{skill_id}: unknown evidence keys {sorted(extra_keys)}")

    normalized: dict[str, list[str]] = {}
    for key in EVIDENCE_KEYS:
        paths = evidence.get(key)
        if not isinstance(paths, list) or any(not isinstance(path, str) for path in paths):
            errors.append(f"{skill_id}: evidence.{key} must be a list of paths")
            normalized[key] = []
            continue
        if len(paths) != len(set(paths)):
            errors.append(f"{skill_id}: evidence.{key} contains duplicate paths")
        normalized[key] = paths
        for path in paths:
            candidate = _path_within_root(root, path)
            if candidate is None:
                errors.append(f"{skill_id}: unsafe evidence path {path!r}")
            elif not candidate.is_file():
                errors.append(f"{skill_id}: evidence path does not exist as a file: {path}")

    canonical_contract = f"skills/{skill_id}/SKILL.md"
    if canonical_contract not in normalized["contract"]:
        errors.append(f"{skill_id}: contract evidence must include {canonical_contract}")
    return normalized


def _validate_maturity(
    skill_id: str,
    entry: dict[str, Any],
    evidence: dict[str, list[str]],
    root: Path,
    errors: list[str],
) -> None:
    label = entry.get("maturity_label")
    framework = entry.get("framework_state")
    boundary = entry.get("boundary_state")
    content = entry.get("content_state")
    executable = entry.get("executable_test_state")
    behavior = entry.get("behavior_state")
    source = entry.get("source_state")
    release_artifact = entry.get("release_artifact_state")
    release_eligible = entry.get("release_eligible")

    enum_checks = (
        ("maturity_label", label, MATURITY_LABELS),
        ("framework_state", framework, FRAMEWORK_STATES),
        ("boundary_state", boundary, BOUNDARY_STATES),
        ("content_state", content, CONTENT_STATES),
        ("executable_test_state", executable, EXECUTABLE_STATES),
        ("behavior_state", behavior, BEHAVIOR_STATES),
        ("source_state", source, SOURCE_STATES),
        ("release_artifact_state", release_artifact, RELEASE_ARTIFACT_STATES),
    )
    for field, value, allowed in enum_checks:
        if value not in allowed:
            errors.append(f"{skill_id}: invalid {field} {value!r}")
    if not isinstance(release_eligible, bool):
        errors.append(f"{skill_id}: release_eligible must be Boolean")

    if framework == "PLANNED":
        errors.append(f"{skill_id}: runtime skills cannot have framework_state=PLANNED")
    if framework != "CONTRACTED":
        errors.append(f"{skill_id}: runtime framework_state must be CONTRACTED")

    if executable == "NOT_PRESENT" and (
        evidence["executable_tests"] or evidence["executable_receipts"]
    ):
        errors.append(
            f"{skill_id}: NOT_PRESENT cannot list executable test or receipt evidence"
        )
    if executable == "STATIC_CONTRACT_ONLY":
        if not evidence["static_checks"]:
            errors.append(f"{skill_id}: STATIC_CONTRACT_ONLY needs static_checks evidence")
        if evidence["executable_tests"]:
            errors.append(
                f"{skill_id}: static string/contract checks cannot be listed as executable tests"
            )
        if evidence["executable_receipts"]:
            errors.append(
                f"{skill_id}: STATIC_CONTRACT_ONLY cannot list executable pass receipts"
            )
        if label != "CONTRACTED":
            errors.append(
                f"{skill_id}: STATIC_CONTRACT_ONLY cannot upgrade beyond CONTRACTED"
            )
    if executable == "EXECUTABLE_PASS_CURRENT_TREE" and not evidence["executable_tests"]:
        errors.append(
            f"{skill_id}: EXECUTABLE_PASS_CURRENT_TREE needs dedicated executable test evidence"
        )

    if behavior in {"NOT_ADJUDICATED", "QUALIFIED_HUMAN_PASS"} and not evidence["behavior"]:
        errors.append(f"{skill_id}: {behavior} needs behavior evidence")
    if source == "NOT_ASSESSED" and evidence["source"]:
        errors.append(f"{skill_id}: NOT_ASSESSED cannot list source-verification evidence")
    if source in {
        "STATIC_SNAPSHOT",
        "LIVE_REFRESH_REQUIRED",
        "CURRENT_VERIFIED",
        "NOT_APPLICABLE",
    } and not evidence["source"]:
        errors.append(f"{skill_id}: {source} needs source evidence")
    if release_artifact == "NOT_RECORDED" and evidence["release_artifact"]:
        errors.append(f"{skill_id}: NOT_RECORDED cannot list release-artifact evidence")
    if release_artifact == "HASH_MANIFEST_VERIFIED" and not evidence["release_artifact"]:
        errors.append(f"{skill_id}: HASH_MANIFEST_VERIFIED needs release-artifact evidence")

    if label == "CONTRACTED":
        if executable == "EXECUTABLE_PASS_CURRENT_TREE":
            errors.append(f"{skill_id}: executable capability gate requires EXPERIMENTAL or VALIDATED")
        if release_eligible is True:
            errors.append(f"{skill_id}: CONTRACTED cannot be release eligible")
    elif label == "EXPERIMENTAL":
        if not (
            framework == "CONTRACTED"
            and boundary in {"CONTRACT_DEFINED", "BOUNDARY_VERIFIED"}
            and content == "IMPLEMENTED"
            and executable == "EXECUTABLE_PASS_CURRENT_TREE"
        ):
            errors.append(
                f"{skill_id}: EXPERIMENTAL requires implemented content and a dedicated executable gate"
            )
        if release_eligible is True:
            errors.append(f"{skill_id}: EXPERIMENTAL cannot be release eligible")
    elif label == "VALIDATED":
        receipt = entry.get("validation_receipt")
        receipt_valid = True
        if not isinstance(receipt, dict):
            errors.append(f"{skill_id}: VALIDATED requires a structured validation_receipt")
            receipt_valid = False
        else:
            missing_receipt = (VALIDATED_PATH_FIELDS | VALIDATED_IDENTITY_FIELDS) - set(receipt)
            if missing_receipt:
                errors.append(
                    f"{skill_id}: validation_receipt missing fields {sorted(missing_receipt)}"
                )
                receipt_valid = False
            receipt_paths: dict[str, str] = {}
            for field in VALIDATED_PATH_FIELDS:
                value = receipt.get(field)
                if not isinstance(value, str):
                    errors.append(f"{skill_id}: validation_receipt.{field} must be a path")
                    receipt_valid = False
                    continue
                candidate = _path_within_root(root, value)
                if candidate is None or not candidate.is_file():
                    errors.append(
                        f"{skill_id}: validation_receipt.{field} is missing or unsafe: {value!r}"
                    )
                    receipt_valid = False
                receipt_paths[field] = value
            if len(set(receipt_paths.values())) != len(receipt_paths):
                errors.append(
                    f"{skill_id}: validated path fields must be distinct dedicated receipts"
                )
                receipt_valid = False
            evidence_membership = {
                "dedicated_gate_receipt": "executable_receipts",
                "source_verification_receipt": "source",
                "behavior_adjudication_receipt": "behavior",
                "adjudicator_qualification_evidence": "behavior",
                "release_artifact_manifest": "release_artifact",
            }
            for field, evidence_axis in evidence_membership.items():
                value = receipt_paths.get(field)
                if value and value not in evidence[evidence_axis]:
                    errors.append(
                        f"{skill_id}: validation_receipt.{field} must be registered in "
                        f"evidence.{evidence_axis}"
                    )
                    receipt_valid = False
            gate_receipt = receipt_paths.get("dedicated_gate_receipt")
            if gate_receipt and gate_receipt in (
                evidence["static_checks"] + evidence["executable_tests"]
            ):
                errors.append(
                    f"{skill_id}: dedicated_gate_receipt must be a run receipt, not test source"
                )
                receipt_valid = False
            for field in VALIDATED_IDENTITY_FIELDS:
                value = receipt.get(field)
                if not isinstance(value, str) or not value.strip():
                    errors.append(
                        f"{skill_id}: validation_receipt.{field} must be a non-empty identity"
                    )
                    receipt_valid = False
            artifact_sha = receipt.get("release_artifact_sha256")
            if not isinstance(artifact_sha, str) or not re.fullmatch(
                r"[0-9a-fA-F]{64}", artifact_sha
            ):
                errors.append(
                    f"{skill_id}: validation_receipt.release_artifact_sha256 must be 64 hex"
                )
                receipt_valid = False
        validated = (
            framework == "CONTRACTED"
            and boundary == "BOUNDARY_VERIFIED"
            and content == "IMPLEMENTED"
            and executable == "EXECUTABLE_PASS_CURRENT_TREE"
            and bool(evidence["executable_tests"])
            and behavior == "QUALIFIED_HUMAN_PASS"
            and bool(evidence["behavior"])
            and source in {"CURRENT_VERIFIED", "NOT_APPLICABLE"}
            and bool(evidence["source"])
            and release_artifact == "HASH_MANIFEST_VERIFIED"
            and bool(evidence["release_artifact"])
            and release_eligible is True
            and receipt_valid
        )
        if not validated:
            errors.append(
                f"{skill_id}: VALIDATED requires executable, source, qualified-human behavior, "
                "and hash-manifest release evidence"
            )

    if behavior == "NOT_ADJUDICATED" and (label == "VALIDATED" or release_eligible is True):
        errors.append(
            f"{skill_id}: NOT_ADJUDICATED behavior cannot be VALIDATED or release eligible"
        )
    if label != "VALIDATED" and entry.get("validation_receipt") not in (None, {}):
        errors.append(f"{skill_id}: non-VALIDATED entry cannot retain a validation_receipt")


def _validate_planned(
    payload: dict[str, Any], root: Path, runtime_ids: set[str], errors: list[str]
) -> None:
    planned_root = payload.get("planned_root")
    planned = payload.get("planned_capabilities")
    if planned_root != "roadmap/skills":
        errors.append("planned_root must be roadmap/skills")
    if not isinstance(planned, list):
        errors.append("planned_capabilities must be a list")
        return

    registered_paths: set[str] = set()
    registered_ids: set[str] = set()
    for index, item in enumerate(planned):
        prefix = f"planned_capabilities[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        required = {
            "capability_id",
            "path",
            "framework_state",
            "release_eligible",
            "evidence_paths",
        }
        missing = required - set(item)
        if missing:
            errors.append(f"{prefix} missing fields {sorted(missing)}")
            continue
        capability_id = item.get("capability_id")
        path = item.get("path")
        if not isinstance(capability_id, str) or not SKILL_ID.fullmatch(capability_id):
            errors.append(f"{prefix}: invalid capability_id {capability_id!r}")
        elif capability_id in registered_ids:
            errors.append(f"{prefix}: duplicate capability_id {capability_id}")
        else:
            registered_ids.add(capability_id)
        if capability_id in runtime_ids:
            errors.append(f"{prefix}: planned capability collides with runtime skill {capability_id}")
        if not isinstance(path, str) or not path.startswith("roadmap/skills/"):
            errors.append(f"{prefix}: planned path must stay under roadmap/skills")
        elif not _is_safe_relative_path(path):
            errors.append(f"{prefix}: unsafe planned path {path!r}")
        else:
            registered_paths.add(path.rstrip("/"))
        if item.get("framework_state") != "PLANNED":
            errors.append(f"{prefix}: framework_state must be PLANNED")
        if item.get("release_eligible") is not False:
            errors.append(f"{prefix}: planned capability cannot be release eligible")
        evidence_paths = item.get("evidence_paths")
        if not isinstance(evidence_paths, list) or any(
            not isinstance(value, str) for value in evidence_paths
        ):
            errors.append(f"{prefix}: evidence_paths must be a list of paths")
        else:
            for value in evidence_paths:
                candidate = _path_within_root(root, value)
                if candidate is None:
                    errors.append(f"{prefix}: unsafe evidence path {value!r}")
                elif not candidate.is_file():
                    errors.append(f"{prefix}: evidence path does not exist as a file: {value}")

    planned_dir = root / "roadmap" / "skills"
    if not planned_dir.exists():
        if planned:
            errors.append("planned_capabilities must be empty when roadmap/skills is absent")
        return
    actual_paths = {
        child.relative_to(root).as_posix()
        for child in planned_dir.iterdir()
        if child.is_dir()
    }
    if registered_paths != actual_paths:
        errors.append(
            "planned directory coverage mismatch: "
            f"registry_only={sorted(registered_paths - actual_paths)}, "
            f"directory_only={sorted(actual_paths - registered_paths)}"
        )


def _validate_readme(
    entries: list[dict[str, Any]], readme_text: str, errors: list[str]
) -> None:
    index = _readme_index(readme_text)
    if not index:
        errors.append("README is missing the 技能索引 section")
        return
    linked_ids = re.findall(
        r"\[`(radiology-[a-z0-9-]+)`\]\(skills/\1/SKILL\.md\)", index
    )
    expected_ids = {entry.get("skill_id") for entry in entries if isinstance(entry, dict)}
    if set(linked_ids) != expected_ids or len(linked_ids) != len(expected_ids):
        errors.append(
            "README canonical skill-link coverage does not match registry: "
            f"missing={sorted(expected_ids - set(linked_ids))}, "
            f"extra={sorted(set(linked_ids) - expected_ids)}"
        )
    if re.search(r"skills/radiology-[a-z0-9-]+/README\.md\)", index):
        errors.append("README skill index must link canonical SKILL.md, not per-skill README.md")
    for legacy in ("| 稳定版 |", "| 测试版 |", "| 草案 |"):
        if legacy in index:
            errors.append(f"README skill index contains legacy non-evidence status {legacy.strip()}")

    for entry in entries:
        skill_id = entry.get("skill_id")
        expected = entry.get("maturity_label")
        if not isinstance(skill_id, str):
            continue
        pattern = re.compile(
            rf"^\|\s*\[`{re.escape(skill_id)}`\]"
            rf"\(skills/{re.escape(skill_id)}/SKILL\.md\).*?\|\s*([A-Z_]+)\s*\|",
            re.MULTILINE,
        )
        match = pattern.search(index)
        if match is None:
            errors.append(f"README is missing a canonical status row for {skill_id}")
        elif match.group(1) != expected:
            errors.append(
                f"README status mismatch for {skill_id}: "
                f"README={match.group(1)}, registry={expected}"
            )

    required_links = (
        "skills/radiology-pipeline/references/capability-maturity-and-release-governance.md",
        "skills/radiology-pipeline/references/capability-maturity-registry.json",
    )
    for target in required_links:
        if f"]({target})" not in readme_text:
            errors.append(f"README is missing governance link: {target}")


def validate_catalog(
    payload: dict[str, Any], root: Path = ROOT, readme_text: str | None = None
) -> list[str]:
    """Return all catalog errors without mutating the payload or filesystem."""
    errors: list[str] = []
    required_top = {
        "schema_version",
        "registry_id",
        "snapshot_date",
        "expected_runtime_skill_count",
        "runtime_root",
        "planned_root",
        "governance_contract",
        "current_behavior_baseline",
        "validated_receipt_contract",
        "planned_capabilities",
        "skills",
    }
    missing_top = required_top - set(payload)
    if missing_top:
        errors.append(f"registry missing top-level fields {sorted(missing_top)}")
    if payload.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    if payload.get("registry_id") != "radiology-skills-capability-maturity":
        errors.append("unexpected registry_id")
    if payload.get("runtime_root") != "skills":
        errors.append("runtime_root must be skills")
    if payload.get("current_behavior_baseline") not in BEHAVIOR_STATES:
        errors.append("invalid current_behavior_baseline")
    expected_count = payload.get("expected_runtime_skill_count")
    if not isinstance(expected_count, int) or isinstance(expected_count, bool) or expected_count < 1:
        errors.append("expected_runtime_skill_count must be a positive integer")
    receipt_contract = payload.get("validated_receipt_contract")
    if not isinstance(receipt_contract, dict):
        errors.append("validated_receipt_contract must be an object")
    else:
        path_fields = receipt_contract.get("required_path_fields")
        identity_fields = receipt_contract.get("required_identity_fields")
        if not isinstance(path_fields, list) or set(path_fields) != VALIDATED_PATH_FIELDS:
            errors.append("validated_receipt_contract required_path_fields do not match policy")
        if not isinstance(identity_fields, list) or set(identity_fields) != VALIDATED_IDENTITY_FIELDS:
            errors.append("validated_receipt_contract required_identity_fields do not match policy")

    governance = payload.get("governance_contract")
    if not isinstance(governance, str):
        errors.append("governance_contract must be a path")
    else:
        governance_path = _path_within_root(root, governance)
        if governance_path is None or not governance_path.is_file():
            errors.append("governance_contract path is missing or unsafe")

    runtime_ids = _runtime_skill_ids(root, "skills")
    entries = payload.get("skills")
    if not isinstance(entries, list):
        errors.append("skills must be a list")
        entries = []
    registry_ids: list[str] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"skills[{index}] must be an object")
            continue
        skill_id = entry.get("skill_id")
        if not isinstance(skill_id, str) or not SKILL_ID.fullmatch(skill_id):
            errors.append(f"skills[{index}]: invalid skill_id {skill_id!r}")
            continue
        registry_ids.append(skill_id)
        evidence = _validate_evidence(skill_id, entry, root, errors)
        if evidence is not None:
            _validate_maturity(skill_id, entry, evidence, root, errors)

    duplicates = sorted(skill_id for skill_id, count in Counter(registry_ids).items() if count > 1)
    if duplicates:
        errors.append(f"duplicate registry skill ids: {duplicates}")
    registered = set(registry_ids)
    if registered != runtime_ids or len(registry_ids) != len(runtime_ids):
        errors.append(
            "runtime directory coverage mismatch: "
            f"registry_only={sorted(registered - runtime_ids)}, "
            f"directory_only={sorted(runtime_ids - registered)}"
        )
    if isinstance(expected_count, int) and not isinstance(expected_count, bool):
        if len(runtime_ids) != expected_count or len(registry_ids) != expected_count:
            errors.append(
                f"catalog expects {expected_count} runtime skills, "
                f"found directories={len(runtime_ids)}, registry={len(registry_ids)}"
            )

    if payload.get("current_behavior_baseline") == "NOT_ADJUDICATED":
        if any(
            isinstance(entry, dict)
            and (entry.get("maturity_label") == "VALIDATED" or entry.get("release_eligible") is True)
            for entry in entries
        ):
            errors.append(
                "NOT_ADJUDICATED behavior baseline forbids VALIDATED or release-eligible entries"
            )

    _validate_planned(payload, root, runtime_ids, errors)
    if readme_text is None:
        readme_text = DEFAULT_README.read_text(encoding="utf-8")
    _validate_readme(entries, readme_text, errors)
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--readme", type=Path, default=DEFAULT_README)
    args = parser.parse_args(argv)
    try:
        payload = load_registry(args.registry)
        readme_text = args.readme.read_text(encoding="utf-8")
        errors = validate_catalog(payload, root=ROOT, readme_text=readme_text)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors = [f"catalog could not be loaded: {exc}"]
        payload = {}

    entries = payload.get("skills", []) if isinstance(payload, dict) else []
    labels = Counter(
        entry.get("maturity_label", "INVALID")
        for entry in entries
        if isinstance(entry, dict)
    )
    report = {
        "status": "PASS" if not errors else "FAIL",
        "registry": str(args.registry),
        "skill_count": len(entries),
        "maturity_counts": dict(sorted(labels.items())),
        "errors": errors,
        "note": "Governance validation is not capability behavior or release validation.",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
