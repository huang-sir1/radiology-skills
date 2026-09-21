#!/usr/bin/env python3
"""Semantic boundary regression for foundation models and synthetic imaging."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[3]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


class FoundationBoundaryContracts(unittest.TestCase):
    def test_conformal_claim_is_assumption_bounded(self) -> None:
        text = read(
            "skills/radiology-deep-learning/references/interpretability-uncertainty.md"
        ).casefold()
        for term in (
            "finite-sample marginal coverage",
            "exchangeability",
            "nonconformity score",
            "marginal/conditional",
            "coverage_assumptions_unresolved",
        ):
            self.assertIn(term, text)
        self.assertNotIn("with a guaranteed coverage rate", text)

    def test_foundation_genealogy_has_closed_world_states_and_privacy_threats(self) -> None:
        text = read(
            "skills/radiology-deep-learning/references/foundation-model-data-genealogy-and-privacy.md"
        ).casefold()
        for term in (
            "verified_no_overlap",
            "partly_assessable",
            "contamination_not_assessable",
            "known_overlap",
            "membership inference",
            "model inversion",
            "provider retention",
            "federated learning is not automatically private",
            "stop_untouched_claim",
        ):
            self.assertIn(term, text)

    def test_foundation_route_does_not_predict_publication_or_reduce_fairness_to_auc(self) -> None:
        text = read(
            "skills/radiology-deep-learning/references/foundation-models-trustworthy-ai.md"
        ).casefold()
        self.assertNotIn("publishable only if", text)
        self.assertRegex(text, r"journal acceptance is not a\s+scientific endpoint")
        self.assertIn("subgroup performance alone is not a fairness determination", text)
        skill = read("skills/radiology-deep-learning/SKILL.md")
        self.assertIn("foundation-model-data-genealogy-and-privacy.md", skill)

    def test_synthetic_task_preserves_real_patient_evidence_boundary(self) -> None:
        text = read(
            "skills/radiology-design/references/tasks/synthetic-imaging-generation.md"
        ).casefold()
        for term in (
            "do not increase the clinical sample size",
            "untouched final evaluation set",
            "real-only baseline",
            "privacy_claim_unresolved",
            "source-patient leakage",
        ):
            self.assertIn(term, text)
        self.assertRegex(text, r"do not by\s+themselves establish")


if __name__ == "__main__":
    unittest.main(verbosity=2)
