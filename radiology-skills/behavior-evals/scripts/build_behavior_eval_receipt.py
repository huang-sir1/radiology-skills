#!/usr/bin/env python3
"""Build a hash-bound unadjudicated receipt from already captured model outputs."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eval_common import (  # noqa: E402
    HARNESS_REQUIRED_FILES, SKILL_ID_RE, evaluation_harness_snapshot, load_unique_json,
    reject_duplicate_pairs, sha256_file, skill_tree_snapshot,
)


def required_skill_ids(registry: dict[str, object]) -> list[str]:
    """Return the complete de-duplicated target plus dependency skill closure."""
    skill_ids: set[str] = set()
    cases = registry.get("cases")
    if not isinstance(cases, list):
        raise ValueError("registry cases must be a list")
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            raise ValueError(f"registry cases[{index}] must be an object")
        target = case.get("target_skill")
        dependencies = case.get("dependency_skills")
        if not isinstance(target, str) or not SKILL_ID_RE.fullmatch(target):
            raise ValueError(f"registry cases[{index}].target_skill is required")
        if not isinstance(dependencies, list) or any(
            not isinstance(value, str) or not SKILL_ID_RE.fullmatch(value)
            for value in dependencies
        ):
            raise ValueError(f"registry cases[{index}].dependency_skills must be a string list")
        if len(dependencies) != len(set(dependencies)):
            raise ValueError(f"registry cases[{index}].dependency_skills contains duplicates")
        if target in dependencies:
            raise ValueError(
                f"registry cases[{index}].dependency_skills must not repeat target_skill"
            )
        skill_ids.add(target)
        skill_ids.update(dependencies)
    return sorted(skill_ids)


def canonical_digest(payload: dict[str, object]) -> str:
    semantic = dict(payload)
    semantic.pop("behavior_eval_receipt_digest", None)
    return hashlib.sha256(json.dumps(
        semantic, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")).hexdigest()


def capture_digest(payload: dict[str, object]) -> str:
    fields = (
        "schema_version", "run_id", "captured_on", "installed_product",
        "cases_registry_path", "cases_registry_sha256", "execution_identity",
        "evaluation_harness", "evaluated_skill_bundle", "outputs",
    )
    capture = {field: payload[field] for field in fields}
    return hashlib.sha256(json.dumps(
        capture, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8")).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--product-root", required=True, type=Path)
    parser.add_argument("--harness-root", type=Path)
    parser.add_argument("--outputs-dir", required=True, type=Path)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--provider", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--model-version", required=True)
    parser.add_argument("--client", default="Codex")
    parser.add_argument("--system-context-digest", default="not-captured")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    registry_path = args.registry.expanduser().resolve()
    manifest_path = args.manifest.expanduser().resolve()
    product_root = args.product_root.expanduser().resolve()
    harness_root = (
        args.harness_root.expanduser().resolve()
        if args.harness_root else (product_root / "behavior-evals").resolve()
    )
    outputs_dir = args.outputs_dir.expanduser().resolve()
    output_path = args.output.expanduser().resolve()
    registry = load_unique_json(registry_path)
    manifest = load_unique_json(manifest_path)
    if not isinstance(registry, dict) or not isinstance(manifest, dict):
        raise SystemExit("registry and manifest roots must be JSON objects")
    try:
        target_skills = required_skill_ids(registry)
        harness_snapshot = evaluation_harness_snapshot(harness_root)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    harness_registry = harness_root / "cases.json"
    if sha256_file(harness_registry) != sha256_file(registry_path):
        raise SystemExit("registry does not match evaluation harness cases.json")
    evaluated_skill_bundle: list[dict[str, object]] = []
    for skill_id in target_skills:
        skill_path = product_root / "skills" / skill_id
        if not skill_path.is_dir():
            raise SystemExit(f"Missing evaluated target skill: {skill_path}")
        snapshot = skill_tree_snapshot(skill_path)
        evaluated_skill_bundle.append({
            "skill_id": skill_id,
            "skill_path": skill_path.resolve().as_posix(),
            **snapshot,
        })
    outputs: list[dict[str, str]] = []
    for case in registry.get("cases", []):
        case_id = case["case_id"]
        raw_output = outputs_dir / f"{case_id}.txt"
        if not raw_output.is_file():
            raise SystemExit(f"Missing captured model output: {raw_output}")
        relative_output = raw_output.resolve().relative_to(output_path.parent.resolve()).as_posix()
        outputs.append({
            "case_id": case_id,
            "prompt_sha256": case["prompt_sha256"],
            "output_path": relative_output,
            "output_sha256": sha256_file(raw_output),
            "execution_state": "MODEL_OUTPUT_CAPTURED",
        })
    payload: dict[str, object] = {
        "schema_version": "1.2",
        "run_id": args.run_id,
        "run_state": "PILOT_UNADJUDICATED",
        "captured_on": datetime.now(timezone.utc).isoformat(),
        "installed_product": {
            "name": manifest.get("name"),
            "version": manifest.get("version"),
            "manifest_path": manifest_path.as_posix(),
            "manifest_sha256": sha256_file(manifest_path),
        },
        "cases_registry_path": registry_path.as_posix(),
        "cases_registry_sha256": sha256_file(registry_path),
        "capture_receipt_digest": "",
        "execution_identity": {
            "provider": args.provider,
            "model": args.model,
            "model_version": args.model_version,
            "client": args.client,
            "system_context_digest": args.system_context_digest,
        },
        "evaluation_harness": {
            "harness_path": harness_root.as_posix(),
            **harness_snapshot,
        },
        "evaluated_skill_bundle": evaluated_skill_bundle,
        "outputs": outputs,
        "human_adjudication": {
            "status": "NOT_ADJUDICATED",
            "artifact_path": "",
            "artifact_sha256": "",
        },
        "comparison_claim_eligible": False,
        "release_claim_eligible": False,
        "behavior_eval_receipt_digest": "",
    }
    payload["capture_receipt_digest"] = capture_digest(payload)
    payload["behavior_eval_receipt_digest"] = canonical_digest(payload)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
