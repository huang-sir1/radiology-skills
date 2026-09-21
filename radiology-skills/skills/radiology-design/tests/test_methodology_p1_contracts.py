import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]


def read_reference(name):
    return (SKILL_ROOT / "references" / name).read_text(encoding="utf-8")


class ReferenceStandardContractTests(unittest.TestCase):
    def test_no_universal_pathology_hierarchy(self):
        text = read_reference("feasibility-triage.md")
        self.assertNotIn("Pathology > consensus read > single read > report-mined", text)
        self.assertIn("There is no universal", text)
        for dimension in (
            "Construct match",
            "Patient/lesion/region match",
            "Time alignment",
            "Sampling coverage",
            "Independence and blinding",
            "Verification process",
            "Reproducibility",
        ):
            self.assertIn(dimension, text)


class TreatmentEstimandContractTests(unittest.TestCase):
    def test_blueprint_separates_three_treatment_questions(self):
        text = read_reference("study-blueprints.md")
        flat = " ".join(text.split())
        for phrase in (
            "Treatment-contextual prognosis",
            "Average treatment effect (ATE)",
            "Effect modification / predictive biomarker",
            "treatment-by-marker contrast",
            "two within-arm P values do not establish a difference",
        ):
            self.assertIn(phrase, flat)

    def test_endpoint_reference_rejects_single_arm_benefit_claim(self):
        text = read_reference("endpoints-and-estimands.md")
        flat = " ".join(text.split())
        self.assertIn("not individual treatment benefit", flat)
        self.assertIn("Calling a marker “predictive of treatment benefit” from one treatment arm", flat)
        self.assertIn("test the between-treatment contrast", flat)


class ValidationBoundaryContractTests(unittest.TestCase):
    def test_validation_dimensions_have_no_universal_center_ladder(self):
        text = read_reference("validation-strategy.md")
        flat = " ".join(text.split())
        self.assertIn("No universal weak-to-strong ladder", flat)
        self.assertIn("There is no universal number of centers", flat)
        self.assertIn("pattern as a hypothesis, not a diagnosis", flat)
        self.assertIn("not a universal small-center repair", flat)
        self.assertNotIn("Need ≥3 centers to be convincing", text)
        self.assertNotIn("| 3–5 |", text)


if __name__ == "__main__":
    unittest.main()
