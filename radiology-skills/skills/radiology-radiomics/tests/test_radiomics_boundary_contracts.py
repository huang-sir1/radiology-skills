import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (SKILL_ROOT / relative).read_text(encoding="utf-8")


class RadiomicsBoundaryContractTests(unittest.TestCase):
    def test_ibsi_is_not_empirical_reproducibility_certification(self):
        skill = " ".join(read("SKILL.md").split())
        preprocessing = " ".join(read("references/preprocessing-ibsi.md").split())
        self.assertIn("IBSI defines; evidence verifies", skill)
        self.assertIn("does not by itself establish empirical repeatability", skill)
        self.assertIn("not proof of implementation equivalence", preprocessing)
        self.assertNotIn("IBSI or it isn't reproducible", skill)

    def test_resampling_is_not_scanner_harmonisation(self):
        text = " ".join(read("references/preprocessing-ibsi.md").split())
        self.assertIn("does **not** make scanners", text)
        self.assertIn("native-spacing distribution", text)
        self.assertIn("illustrative only, **not recommended defaults**", text)

    def test_no_universal_epv_or_model_menu(self):
        text = " ".join(read("references/selection-modelling.md").split())
        self.assertIn("No selector/model combination is a universal default", text)
        self.assertIn("no universal permitted number", text)
        self.assertIn("Do not derive an allowed feature count", text)
        self.assertNotIn("EPV ≈ 10", text)
        self.assertNotIn("At most **2–3", text)

    def test_decision_curve_requires_a_defined_decision(self):
        text = " ".join(read("references/selection-modelling.md").split())
        self.assertIn("decision-curve analysis only when", text)
        self.assertIn("otherwise omit it", text)
        self.assertIn("does not establish observed clinical utility", text)

    def test_reporting_template_does_not_prescribe_an_unperformed_pipeline(self):
        text = read("references/selection-modelling.md")
        template = text.split("## Reporting sentence", 1)[1]
        normalized = " ".join(template.split())
        self.assertIn("selection method or no selection was [AUTHOR_INPUT_NEEDED]", normalized)
        self.assertIn("the model was [AUTHOR_INPUT_NEEDED]", normalized)
        self.assertIn("only if that resampling procedure was actually used", normalized)
        self.assertIn("only from the performed pipeline and outputs", template)
        self.assertNotIn("ICC > 0.80", template)
        self.assertNotIn("selected by LASSO", template)


if __name__ == "__main__":
    unittest.main()
