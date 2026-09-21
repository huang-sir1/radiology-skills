#!/usr/bin/env python3
"""Validate a hash-bound radiology search retrieval-run receipt."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


SHA_RE = re.compile(r"^[0-9a-f]{64}$")
RUN_STATES = {"EXECUTED", "PARTIAL", "FAILED"}
SOURCE_STATES = {
    "SUCCESS", "EMPTY_VERIFIED", "RATE_LIMITED", "AUTH_REQUIRED", "NETWORK_FAILED",
    "SOURCE_ERROR", "NOT_RUN",
}
COVERAGE_STATES = {"NOT_CLAIMED", "PARTIAL", "COMPLETE_FOR_DECLARED_SOURCES"}
EVIDENCE_LEVELS = {"FULL_TEXT", "ABSTRACT", "METADATA_ONLY"}


def reject_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicates)
    if not isinstance(value, dict):
        raise ValueError("receipt root must be an object")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest(value: object) -> str:
    return hashlib.sha256(json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")).hexdigest()


def receipt_digest(payload: dict[str, object]) -> str:
    semantic = dict(payload)
    semantic.pop("receipt_sha256", None)
    return digest(semantic)


def valid_sha(value: object, *, allow_not_captured: bool = False) -> bool:
    return bool(
        (allow_not_captured and value == "not-captured")
        or isinstance(value, str) and SHA_RE.fullmatch(value) and value != "0" * 64
    )


def resolved_file(root: Path, value: object) -> Path | None:
    if not isinstance(value, str) or not value:
        return None
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = root / path
    path = path.resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError:
        return None
    return path


def validate(payload: dict[str, object], root: Path) -> list[str]:
    errors: list[str] = []
    required = {
        "schema_version", "run_id", "run_state", "executed_on",
        "question_or_protocol_sha256", "execution_identity", "sources", "retrieval_config",
        "retrieval_config_sha256", "corpus_manifest", "evidence_contexts", "index_identity",
        "failures", "update_triggers", "coverage_claim", "receipt_sha256", "boundary",
    }
    if set(payload) != required:
        errors.append("receipt fields do not match schema")
    if payload.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    for field in ("run_id", "executed_on", "boundary"):
        if not isinstance(payload.get(field), str) or not payload[field].strip():
            errors.append(f"{field} is required")
    if payload.get("run_state") not in RUN_STATES:
        errors.append("run_state is invalid")
    if not valid_sha(payload.get("question_or_protocol_sha256")):
        errors.append("question_or_protocol_sha256 is invalid")

    identity = payload.get("execution_identity")
    if not isinstance(identity, dict) or set(identity) != {
        "provider", "tool", "tool_version", "system_context_digest",
    }:
        errors.append("execution_identity fields do not match schema")
    else:
        for field in ("provider", "tool", "tool_version"):
            if not isinstance(identity.get(field), str) or not identity[field].strip():
                errors.append(f"execution_identity.{field} is required")
        if not valid_sha(identity.get("system_context_digest"), allow_not_captured=True):
            errors.append("execution_identity.system_context_digest is invalid")

    config = payload.get("retrieval_config")
    if not isinstance(config, dict) or set(config) != {
        "parser", "parser_version", "dedup_order", "normalization_rules", "limits",
    }:
        errors.append("retrieval_config fields do not match schema")
    else:
        for field in ("parser", "parser_version"):
            if not isinstance(config.get(field), str) or not config[field].strip():
                errors.append(f"retrieval_config.{field} is required")
        for field in ("dedup_order", "normalization_rules"):
            if not isinstance(config.get(field), list) or not config[field]:
                errors.append(f"retrieval_config.{field} must be a non-empty list")
        if not isinstance(config.get("limits"), dict):
            errors.append("retrieval_config.limits must be an object")
        if payload.get("retrieval_config_sha256") != digest(config):
            errors.append("retrieval_config_sha256 mismatch")

    sources = payload.get("sources")
    complete_sources = True
    seen_sources: set[str] = set()
    if not isinstance(sources, list) or not sources:
        errors.append("sources must be a non-empty list")
        sources = []
    for index, source in enumerate(sources):
        expected = {
            "source_id", "endpoint", "query", "filters", "sort", "pagination_exhausted",
            "request_count", "raw_result_count", "outcome_state", "response_artifacts",
        }
        if not isinstance(source, dict) or set(source) != expected:
            errors.append(f"sources[{index}] fields do not match schema")
            complete_sources = False
            continue
        source_id = source.get("source_id")
        if not isinstance(source_id, str) or not source_id or source_id in seen_sources:
            errors.append(f"sources[{index}].source_id is missing or duplicate")
        else:
            seen_sources.add(source_id)
        for field in ("endpoint", "query"):
            if not isinstance(source.get(field), str) or not source[field].strip():
                errors.append(f"sources[{index}].{field} is required")
        if not isinstance(source.get("filters"), dict):
            errors.append(f"sources[{index}].filters must be an object")
        if not isinstance(source.get("sort"), str):
            errors.append(f"sources[{index}].sort must be a string")
        if not isinstance(source.get("pagination_exhausted"), bool):
            errors.append(f"sources[{index}].pagination_exhausted must be boolean")
        for field in ("request_count", "raw_result_count"):
            if not isinstance(source.get(field), int) or source[field] < 0:
                errors.append(f"sources[{index}].{field} must be non-negative")
        state = source.get("outcome_state")
        if state not in SOURCE_STATES:
            errors.append(f"sources[{index}].outcome_state is invalid")
        if state not in {"SUCCESS", "EMPTY_VERIFIED"} or source.get("pagination_exhausted") is not True:
            complete_sources = False
        if state == "EMPTY_VERIFIED" and source.get("raw_result_count") != 0:
            errors.append(f"sources[{index}] EMPTY_VERIFIED requires zero results")
        artifacts = source.get("response_artifacts")
        if not isinstance(artifacts, list):
            errors.append(f"sources[{index}].response_artifacts must be a list")
            artifacts = []
        if state in {"SUCCESS", "EMPTY_VERIFIED"} and not artifacts:
            errors.append(f"sources[{index}] completed without a response artifact")
        for a_index, artifact in enumerate(artifacts):
            if not isinstance(artifact, dict) or set(artifact) != {"path", "sha256"}:
                errors.append(f"sources[{index}].response_artifacts[{a_index}] is invalid")
                continue
            path = resolved_file(root, artifact.get("path"))
            if path is None or not path.is_file():
                errors.append(f"sources[{index}].response_artifacts[{a_index}] is missing or escapes root")
            elif artifact.get("sha256") != sha256_file(path):
                errors.append(f"sources[{index}].response_artifacts[{a_index}] SHA-256 mismatch")

    manifest = payload.get("corpus_manifest")
    manifest_sha = None
    if not isinstance(manifest, dict) or set(manifest) != {"path", "sha256", "record_count"}:
        errors.append("corpus_manifest fields do not match schema")
    else:
        path = resolved_file(root, manifest.get("path"))
        if path is None or not path.is_file():
            errors.append("corpus_manifest path is missing or escapes root")
        else:
            manifest_sha = sha256_file(path)
            if manifest.get("sha256") != manifest_sha:
                errors.append("corpus_manifest SHA-256 mismatch")
        if not isinstance(manifest.get("record_count"), int) or manifest["record_count"] < 0:
            errors.append("corpus_manifest.record_count must be non-negative")

    contexts = payload.get("evidence_contexts")
    if not isinstance(contexts, list):
        errors.append("evidence_contexts must be a list")
        contexts = []
    for index, context in enumerate(contexts):
        expected = {"record_id", "evidence_level", "source_locator", "content_sha256", "claim_ids"}
        if not isinstance(context, dict) or set(context) != expected:
            errors.append(f"evidence_contexts[{index}] fields do not match schema")
            continue
        for field in ("record_id", "source_locator"):
            if not isinstance(context.get(field), str) or not context[field].strip():
                errors.append(f"evidence_contexts[{index}].{field} is required")
        if context.get("evidence_level") not in EVIDENCE_LEVELS:
            errors.append(f"evidence_contexts[{index}].evidence_level is invalid")
        if not valid_sha(context.get("content_sha256")):
            errors.append(f"evidence_contexts[{index}].content_sha256 is invalid")
        if not isinstance(context.get("claim_ids"), list):
            errors.append(f"evidence_contexts[{index}].claim_ids must be a list")

    index = payload.get("index_identity")
    if not isinstance(index, dict) or set(index) != {
        "state", "corpus_manifest_sha256", "retrieval_config_sha256", "index_sha256",
    }:
        errors.append("index_identity fields do not match schema")
    else:
        state = index.get("state")
        if state not in {"CURRENT", "STALE", "NOT_BUILT"}:
            errors.append("index_identity.state is invalid")
        if state == "CURRENT":
            if index.get("corpus_manifest_sha256") != manifest_sha:
                errors.append("CURRENT index corpus digest mismatch")
            if index.get("retrieval_config_sha256") != payload.get("retrieval_config_sha256"):
                errors.append("CURRENT index configuration digest mismatch")
            if not valid_sha(index.get("index_sha256")):
                errors.append("CURRENT index_sha256 is invalid")
        elif state == "NOT_BUILT" and any(index.get(field) for field in (
            "corpus_manifest_sha256", "retrieval_config_sha256", "index_sha256",
        )):
            errors.append("NOT_BUILT index must not carry identity digests")

    for field in ("failures", "update_triggers"):
        values = payload.get(field)
        if not isinstance(values, list) or any(not isinstance(value, str) or not value.strip() for value in values):
            errors.append(f"{field} must be a string list")
    coverage = payload.get("coverage_claim")
    if coverage not in COVERAGE_STATES:
        errors.append("coverage_claim is invalid")
    if coverage == "COMPLETE_FOR_DECLARED_SOURCES" and not complete_sources:
        errors.append("complete coverage requires every declared source and pagination to complete")
    if payload.get("run_state") in {"PARTIAL", "FAILED"} and coverage == "COMPLETE_FOR_DECLARED_SOURCES":
        errors.append("PARTIAL/FAILED run cannot claim complete coverage")
    if payload.get("run_state") == "FAILED" and not payload.get("failures"):
        errors.append("FAILED run requires failures")
    if payload.get("receipt_sha256") != receipt_digest(payload):
        errors.append("receipt_sha256 mismatch")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", type=Path)
    args = parser.parse_args()
    path = args.receipt.expanduser().resolve()
    try:
        payload = load(path)
        errors = validate(payload, path.parent)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors = [str(exc)]
    print(json.dumps({
        "status": "FAIL" if errors else "PASS",
        "errors": errors,
        "boundary": "Structural retrieval identity only; no query execution, authority, completeness or support verdict is inferred.",
    }, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
