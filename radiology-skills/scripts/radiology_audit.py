#!/usr/bin/env python3
"""Quick Markdown audit for a radiology AI study card."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


TEMPLATE = {
    "study_type": "radiomics | deep-learning | mixed",
    "disease": "",
    "modality": "CT | MRI | PET/CT | ultrasound | multimodal",
    "n_patients": 0,
    "centers": 1,
    "labels": "",
    "endpoint": "",
    "split_level": "patient | lesion | slice | image | unknown",
    "external_validation": False,
    "segmentation_source": "",
    "calibration_reported": False,
    "clinical_utility_reported": False,
    "code_available": False,
    "data_available": False,
}


def as_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "y"}
    return bool(value)


def risk(level: str, item: str, reason: str, fix: str) -> dict[str, str]:
    return {"level": level, "item": item, "reason": reason, "fix": fix}


def audit(card: dict[str, Any]) -> list[dict[str, str]]:
    risks: list[dict[str, str]] = []
    study_type = str(card.get("study_type", "")).lower()
    n_patients = int(card.get("n_patients") or 0)
    centers = int(card.get("centers") or 0)
    split_level = str(card.get("split_level", "unknown")).lower()

    if split_level not in {"patient", "patient-level"}:
        risks.append(risk(
            "blocking",
            "Split unit",
            f"Split level is `{split_level or 'unknown'}`, not patient-level.",
            "Rebuild train/validation/test splits by patient ID before feature selection, augmentation, or tuning.",
        ))

    if not card.get("labels"):
        risks.append(risk(
            "high",
            "Label source",
            "No label or reference standard is documented.",
            "State pathology, follow-up, expert consensus, registry, molecular test, or report-derived label source.",
        ))

    if not card.get("endpoint"):
        risks.append(risk(
            "high",
            "Endpoint",
            "The clinical endpoint is not defined.",
            "Define the prediction target, time horizon, event definition, or segmentation target.",
        ))

    if n_patients <= 0:
        risks.append(risk("high", "Sample size", "Patient count is missing.", "Report patient count and event count."))
    elif "deep" in study_type and n_patients < 200:
        risks.append(risk(
            "high",
            "Sample size",
            f"{n_patients} patients is small for deep learning.",
            "Prefer transfer learning, simpler baselines, nested CV, and cautious claims.",
        ))
    elif n_patients < 100:
        risks.append(risk(
            "medium",
            "Sample size",
            f"{n_patients} patients may be underpowered.",
            "Report event count, confidence intervals, and reduce model complexity.",
        ))

    if centers < 2:
        risks.append(risk(
            "medium",
            "Center diversity",
            "Single-center data limit generalizability.",
            "Use temporal validation if external validation is unavailable and soften external claims.",
        ))

    if not as_bool(card.get("external_validation")):
        risks.append(risk(
            "high",
            "External validation",
            "No independent external validation is documented.",
            "Avoid deployment/generalizability claims; seek external or temporal validation.",
        ))

    if not card.get("segmentation_source"):
        risks.append(risk(
            "medium",
            "Segmentation",
            "Segmentation or ROI source is not documented.",
            "Report manual/automatic source, reader expertise, consensus, and QC.",
        ))

    if not as_bool(card.get("calibration_reported")):
        risks.append(risk(
            "medium",
            "Calibration",
            "Calibration is not reported.",
            "Add calibration curve/intercept/slope or avoid decision-support claims.",
        ))

    if not as_bool(card.get("clinical_utility_reported")):
        risks.append(risk(
            "medium",
            "Clinical utility",
            "Clinical utility is not assessed.",
            "Add DCA/threshold logic or keep claims limited to model performance.",
        ))

    if not as_bool(card.get("code_available")):
        risks.append(risk("low", "Code", "Code availability is not documented.", "Add code availability or restriction reason."))
    if not as_bool(card.get("data_available")):
        risks.append(risk("low", "Data", "Data availability is not documented.", "Add data availability and access route."))

    return risks


def render(card: dict[str, Any], risks: list[dict[str, str]]) -> str:
    lines = [
        "# Radiology Study Audit",
        "",
        "## Study card",
        "",
    ]
    for key in TEMPLATE:
        lines.append(f"- {key}: {card.get(key, '')}")
    lines.extend(["", "## Risks", ""])
    if not risks:
        lines.append("- No major risk detected by the quick audit. Manual review is still required.")
    else:
        lines.append("| Level | Item | Reason | Suggested fix |")
        lines.append("|---|---|---|---|")
        for item in risks:
            lines.append(f"| {item['level']} | {item['item']} | {item['reason']} | {item['fix']} |")
    lines.extend(["", "## Note", "", "This script is a screening helper. It does not replace methodological review."])
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Quick audit for radiology AI study cards.")
    parser.add_argument("--input", help="Path to JSON study card.")
    parser.add_argument("--json", help="Inline JSON study card.")
    parser.add_argument("--template", action="store_true", help="Print a JSON template and exit.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.template:
        print(json.dumps(TEMPLATE, indent=2, ensure_ascii=False))
        return 0
    if args.input:
        card = json.loads(Path(args.input).read_text(encoding="utf-8-sig"))
    elif args.json:
        card = json.loads(args.json)
    else:
        print("Provide --input, --json, or --template.", file=sys.stderr)
        return 2
    print(render(card, audit(card)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
