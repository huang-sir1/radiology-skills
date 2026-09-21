import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class GuidelineVersionContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.versions = (ROOT / "references" / "guideline-versions.md").read_text(encoding="utf-8")
        cls.dta = (ROOT / "references" / "stard-prisma-quadas.md").read_text(encoding="utf-8")
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

    def test_checklist_handoff_names_owner_and_closure_evidence(self):
        self.assertIn("Fix | Owner | Closure evidence", self.skill)
        self.assertIn("assignment alone never closes an item", self.skill)

    def test_tripod_cluster_is_no_longer_pending(self):
        self.assertIn("**TRIPOD-Cluster** | 2023", self.versions)
        self.assertIn("*BMJ* 2023;380:e071018", self.versions)
        self.assertIn("**19 main items**", self.versions)
        self.assertNotIn("verify publication status/venue live before citing", self.versions)

    def test_targeted_source_record_is_auditable(self):
        self.assertIn("## Targeted verification evidence", self.versions)
        self.assertIn("10.1136/bmj-2022-071018", self.versions)
        self.assertIn("10.1038/s41591-025-03953-8", self.versions)
        self.assertIn("A targeted check does not silently re-date", self.versions)

    def test_stard_ai_denominators_are_unambiguous_in_both_references(self):
        for text in (self.versions, self.dta):
            self.assertIn("40", text)
            self.assertIn("4", text)
            self.assertIn("14", text)
            self.assertIn("10 main items", text)
            self.assertNotIn("adds 18\n> new/modified items", text)

    def test_quadas_3_v12_is_current_and_quadas_2_is_legacy(self):
        self.assertIn("**QUADAS-3** | **1.2 (2026)**", self.versions)
        self.assertIn("**QUADAS-2 (legacy)**", self.versions)
        self.assertIn("QUADAS-2 is superseded by QUADAS-3", self.dta)
        self.assertNotIn("PRISMA-DTA + QUADAS-2", self.dta)
        self.assertIn("selected accuracy-estimate level", self.dta)
        for domain in ("Participants", "Index Test", "Target Condition", "Analysis"):
            self.assertIn(domain, self.dta)

    def test_quadas_c_is_paired_with_quadas_3_and_official_urls_are_frozen(self):
        self.assertIn("QUADAS-C cannot be used alone", self.dta)
        self.assertIn("QUADAS-C alongside QUADAS-3", self.dta)
        self.assertIn("does not assess indirect comparisons", self.dta)
        self.assertIn("does not assess applicability", self.dta)
        self.assertIn(
            "https://www.bristol.ac.uk/population-health-sciences/projects/quadas/quadas-3/resources/",
            self.versions,
        )
        self.assertIn(
            "https://www.bristol.ac.uk/population-health-sciences/projects/quadas/quadas-c/",
            self.versions,
        )


if __name__ == "__main__":
    unittest.main()
