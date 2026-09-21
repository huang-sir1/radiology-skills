import math
import re
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]


def read_reference(name):
    return (SKILL_ROOT / "references" / name).read_text(encoding="utf-8")


class DiagnosticAccuracyContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = read_reference("diagnostic-accuracy.md")
        match = re.search(r"```python\n(.*?)\n```", cls.text, flags=re.DOTALL)
        if not match:
            raise AssertionError("diagnostic-accuracy.md needs an executable Python block")
        cls.namespace = {}
        exec(match.group(1), cls.namespace)

    def test_observed_and_target_prevalence_are_distinct(self):
        result = self.namespace["diag_metrics"](130, 42, 19, 158, target_prevalence=0.27)
        self.assertTrue(math.isclose(result["sample"]["prevalence"], 149 / 349))
        self.assertTrue(math.isclose(result["target_scenario"]["prevalence"], 0.27))
        self.assertTrue(math.isclose(result["target_scenario"]["ppv"], 0.605781328473276))
        self.assertTrue(math.isclose(result["target_scenario"]["npv"], 0.943662466793252))

    def test_invalid_target_prevalence_is_rejected(self):
        function = self.namespace["predictive_values_at_prevalence"]
        for invalid in (0, 1, -0.1, 1.1):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    function(0.8, 0.9, invalid)

    def test_undefined_predictive_value_is_reported_explicitly(self):
        function = self.namespace["predictive_values_at_prevalence"]
        for sensitivity, specificity in ((0, 1), (1, 0)):
            with self.subTest(sensitivity=sensitivity, specificity=specificity):
                with self.assertRaisesRegex(ValueError, "undefined"):
                    function(sensitivity, specificity, 0.27)

    def test_transport_uncertainty_is_not_sample_wilson_interval(self):
        self.assertIn("Do **not** attach the sample PPV/NPV", self.text)
        self.assertIn("Propagate uncertainty in sensitivity, specificity", self.text)
        self.assertIn("transported estimates, not new validation data", self.text)

    def test_entrypoint_example_matches_computed_wilson_interval(self):
        skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        interval = self.namespace["wilson_interval"](158, 200)
        self.assertEqual((0.73, 0.84), tuple(round(value, 2) for value in interval))
        self.assertIn("CI: 0.73, 0.84; 158/200", skill_text)
        self.assertNotIn("CI: 0.72, 0.85; 158/200", skill_text)


class HighDimensionalAndSurvivalContractTests(unittest.TestCase):
    def test_prespecification_does_not_erase_multiplicity(self):
        text = read_reference("high-dimensional-omics.md")
        flat = " ".join(text.split())
        self.assertIn("does not by itself erase multiplicity", flat)
        self.assertIn("Multiple primary endpoints, contrasts, time points", flat)
        self.assertNotIn("primary hypothesis (escapes correction)", text)

    def test_combat_distinguishes_seen_and_unseen_batches(self):
        text = read_reference("high-dimensional-omics.md")
        flat = " ".join(text.split())
        self.assertIn("represented in training", flat)
        self.assertIn("wholly unseen external site/batch", flat)
        self.assertIn("adapted/transductive rather than an untouched external validation", flat)

    def test_non_significant_ph_test_is_not_proof(self):
        text = read_reference("survival-prognostic.md")
        flat = " ".join(text.split())
        self.assertIn("no evidence of a proportional-hazards violation", flat)
        self.assertIn("does not prove the assumption", flat)
        self.assertNotIn("Proportional hazards held", text)

    def test_dca_is_not_claimed_as_observed_clinical_utility(self):
        text = read_reference("model-evaluation.md")
        flat = " ".join(text.split())
        self.assertIn("decision-analytic net benefit", flat)
        self.assertIn("does **not** observe patient benefit", flat)
        self.assertIn("Do not label a positive net-benefit curve", flat)
        self.assertNotIn("## Clinical utility — decision-curve analysis", text)

    def test_incremental_inference_separates_binary_survival_and_fitting_state(self):
        text = read_reference("incremental-value.md")
        flat = " ".join(text.split())
        self.assertIn("ordinary ROC DeLong is not a test for censored C-index differences", flat)
        self.assertIn("do not use ordinary DeLong on apparent fitted scores", flat)
        self.assertIn("Do not repeat a development LRT on frozen external predictions", flat)
        self.assertIn("Selected, penalized or non-likelihood models", flat)
        self.assertIn("does not automatically include development uncertainty", flat)
        self.assertNotIn("DeLong** (or bootstrap) on ΔAUC / ΔC-index", text)

    def test_incremental_metrics_do_not_force_nri_or_undefined_decision_curves(self):
        text = read_reference("incremental-value.md")
        flat = " ".join(text.split())
        self.assertIn("Do not default to **category-free (continuous) NRI**", flat)
        self.assertIn("Omitting NRI/IDI is acceptable", flat)
        self.assertIn("Otherwise omit it and bound the claim", flat)
        self.assertIn("observed clinical utility", flat)
        self.assertNotIn("Prefer **category-free (continuous) NRI**", text)
        self.assertNotIn("| Clinical utility | **DCA**", text)

    def test_reader_inference_follows_fixed_random_target_and_design(self):
        text = read_reference("agreement-mrmc.md")
        flat = " ".join(text.split())
        self.assertIn("fixed-reader inference is conditional on those named readers", flat)
        self.assertIn("Fully crossed is not universally most powerful", flat)
        self.assertIn("fixed/random factor, design and missingness support", flat)
        self.assertIn("not FDA endorsement or approval", flat)
        self.assertNotIn("both readers and cases are random effects", text)
        self.assertNotIn("# R, FDA-endorsed", text)

    def test_icc_model_and_agreement_definition_are_distinct(self):
        text = " ".join(read_reference("agreement-mrmc.md").split())
        self.assertIn("Specify model, agreement definition and single/average unit separately", text)
        self.assertIn("not automatically an absolute-agreement or consistency coefficient", text)


if __name__ == "__main__":
    unittest.main()
