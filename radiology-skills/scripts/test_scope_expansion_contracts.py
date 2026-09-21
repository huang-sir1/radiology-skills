#!/usr/bin/env python3
"""Cross-skill regression tests for the radiology research scope expansion."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    path = ROOT / relative
    if not path.is_file():
        raise AssertionError(f"required scope artifact is missing: {relative}")
    return path.read_text(encoding="utf-8")


def assert_contract(
    case: unittest.TestCase,
    relative: str,
    required_terms: tuple[str, ...],
    *,
    require_source: bool = True,
) -> str:
    text = read(relative)
    folded = text.casefold()
    for term in required_terms:
        case.assertIn(term.casefold(), folded, f"{relative} is missing contract term {term!r}")
    if require_source:
        case.assertRegex(text, r"https?://", f"{relative} has no auditable source locator")
    return text


class ScopeExpansionContractTests(unittest.TestCase):
    NEW_INDEPENDENT_SKILLS = (
        "radiology-research-integrity",
        "radiology-research-ops",
        "radiology-consensus-guideline",
        "radiology-qualitative-mixed-methods",
        "radiology-health-economics",
        "radiology-reproducibility",
        "radiology-dissemination",
        "radiology-bibliometrics",
        "radiology-innovation-transfer",
    )

    def test_eight_primary_task_contracts_are_complete(self) -> None:
        tasks = (
            "detection-localization",
            "segmentation-quantification",
            "diagnosis-triage",
            "prognosis-risk",
            "response-longitudinal",
            "reconstruction-enhancement",
            "synthetic-imaging-generation",
            "report-generation-vlm",
        )
        for task in tasks:
            text = assert_contract(
                self,
                f"skills/radiology-design/references/tasks/{task}.md",
                ("claim", "stop"),
            )
            folded = text.casefold()
            self.assertRegex(
                folded,
                r"\bindependent unit\b|\|\s*[^|\n]*unit[^|\n]*\|",
                f"{task} has no explicit analysis-unit field",
            )
            self.assertRegex(
                folded,
                r"\breference\b|\boutcome\b|\btarget\b",
                f"{task} has no explicit target/reference/outcome construct",
            )

        router = read("skills/radiology-design/references/task-contract-router.md")
        for task in tasks:
            self.assertIn(f"tasks/{task}.md", router)
        self.assertIn("one primary task", router.casefold())

    def test_protocol_sap_and_amendment_controls_are_preserved(self) -> None:
        protocol_reference = assert_contract(
            self,
            "skills/radiology-design/references/primary-imaging-study-protocol-and-preregistration.md",
            ("protocol", "sap", "protected-test", "amendment", "preregistration"),
        )
        protocol_template = read("skills/radiology-design/templates/imaging-study-protocol.md")
        sap_template = read("skills/radiology-design/templates/imaging-statistical-analysis-plan.md")
        for text in (protocol_reference, protocol_template, sap_template):
            folded = text.casefold()
            self.assertIn("independent unit", folded)
            self.assertIn("claim", folded)
            self.assertTrue("protected-test" in folded or "protected test" in folded)
            self.assertTrue("amendment" in folded or "deviation" in folded)

    def test_reference_standard_and_longitudinal_label_contracts_exist(self) -> None:
        references = (
            "label-ontology-and-reference-standard",
            "noisy-weak-and-report-derived-labels",
            "longitudinal-lesion-and-exam-linkage",
        )
        for name in references:
            assert_contract(
                self,
                f"skills/radiology-annotation/references/{name}.md",
                ("reference", "stop", "claim"),
            )

    def test_imaging_specific_inference_routes_are_bounded(self) -> None:
        references = (
            "quantitative-imaging-measurement-science",
            "causal-and-clinical-impact-inference",
            "longitudinal-and-multistate-imaging",
        )
        for name in references:
            text = assert_contract(
                self,
                f"skills/radiology-stats/references/{name}.md",
                ("estimand", "stop", "claim"),
            )
            self.assertRegex(
                text.casefold(),
                r"\buncertainty\b|\bci\b|\bcis\b|confidence interval",
                f"{name} has no uncertainty-reporting contract",
            )

    def test_clinical_impact_and_human_factors_are_not_accuracy_proxies(self) -> None:
        impact = assert_contract(
            self,
            "skills/radiology-translation/references/clinical-impact-study-design.md",
            ("clinical impact", "causal estimand", "reader", "stop", "claim ceiling"),
        )
        human_factors = assert_contract(
            self,
            "skills/radiology-translation/references/human-factors-and-implementation.md",
            ("human", "workflow", "use error", "stop", "claim ceiling"),
        )
        boundary = r"(?:do|does) not establish|cannot establish"
        self.assertRegex(impact.casefold(), boundary)
        self.assertRegex(human_factors.casefold(), boundary)

    def test_acquisition_owner_has_modality_cards_and_measurement_passport(self) -> None:
        cards = (
            "ct-acquisition-reconstruction",
            "mr-acquisition-reconstruction",
            "pet-spect-acquisition-quantification",
            "ultrasound-ceus-elastography",
            "projection-radiography-mammo-dbt",
            "phantom-test-retest-protocol-shift",
        )
        for card in cards:
            assert_contract(
                self,
                f"skills/radiology-acquisition-qc/references/{card}.md",
                ("pass", "conditional", "stop"),
            )
        assert_contract(
            self,
            "skills/radiology-acquisition-qc/templates/imaging-measurement-passport.md",
            ("acquisition", "reconstruction", "qc", "claim"),
            require_source=False,
        )
        routes = read("skills/radiology-pipeline/references/research-intent-routing.md")
        self.assertIn("radiology-acquisition-qc", routes)

    def test_four_focused_clinical_domain_packs_exist(self) -> None:
        packs = (
            "acute-emergency-imaging-research",
            "musculoskeletal-imaging-research",
            "pediatric-imaging-research",
            "nuclear-medicine-theranostics-research",
        )
        for pack in packs:
            text = assert_contract(
                self,
                f"skills/radiology-clinical-domain/references/{pack}.md",
                ("stop", "claim"),
            )
            self.assertGreaterEqual(len(re.findall(r"https?://", text)), 2)

    def test_open_science_gate_binds_lock_execution_and_closeout(self) -> None:
        gate = assert_contract(
            self,
            "skills/radiology-pipeline/references/open-science-and-reproducibility-gate.md",
            ("D4", "D5", "D9", "FAIR", "Transparency and Openness Promotion", "STOP"),
        )
        self.assertIn("10.1038/sdata.2016.18", gate)
        self.assertIn("10.1126/science.aab2374", gate)

    def test_v15_to_v17_independent_skill_packages_are_complete(self) -> None:
        for skill in self.NEW_INDEPENDENT_SKILLS:
            root = ROOT / "skills" / skill
            for relative in (
                "SKILL.md",
                "agents/openai.yaml",
                "references/source-registry.md",
                "tests/routing-cases.json",
            ):
                self.assertTrue((root / relative).is_file(), f"{skill} lacks {relative}")
            validators = tuple((root / "scripts").glob("validate_*_skill.ps1"))
            self.assertEqual(len(validators), 1, f"{skill} needs one dedicated validator")
            cases = json.loads((root / "tests/routing-cases.json").read_text(encoding="utf-8"))
            self.assertGreaterEqual(len(cases["positive_cases"]), 5)
            self.assertGreaterEqual(len(cases["boundary_cases"]), 6)
            source = (root / "references/source-registry.md").read_text(encoding="utf-8")
            self.assertRegex(source, r"\b20\d{2}-\d{2}-\d{2}\b")
            self.assertRegex(source, r"https?://")

    def test_global_router_covers_all_skills_with_budget_and_boundaries(self) -> None:
        routes = read("skills/radiology-pipeline/references/research-intent-routing.md")
        cases = json.loads(
            read("skills/radiology-pipeline/tests/global-research-routing-cases.json")
        )
        skill_dirs = sorted(
            p.name for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").is_file()
        )
        owners = {case["expected_owner"] for case in cases["positive_cases"]}
        self.assertEqual(set(skill_dirs), owners)
        for skill in self.NEW_INDEPENDENT_SKILLS:
            self.assertIn(f"`{skill}`", routes)
        descriptions = []
        for skill in skill_dirs:
            text = read(f"skills/{skill}/SKILL.md")
            match = re.search(r'^description:\s*["\'](.+)["\']\s*$', text, re.MULTILINE)
            self.assertIsNotNone(match, f"{skill} lacks a quoted one-line description")
            descriptions.append(len(match.group(1)) + 2)
        self.assertLessEqual(sum(descriptions), 5000)
        boundary_owners = {
            owner
            for case in cases["boundary_cases"]
            for owner in (case["owner_a"], case["owner_b"])
        }
        self.assertEqual(set(skill_dirs), boundary_owners)

    def test_translation_is_an_independent_two_axis_and_lifecycle_package(self) -> None:
        translation = read("skills/radiology-translation/SKILL.md")
        for relative in (
            "references/source-registry.md",
            "tests/routing-cases.json",
            "scripts/validate_translation_skill.ps1",
        ):
            self.assertTrue((ROOT / "skills/radiology-translation" / relative).is_file())
        self.assertIn("seven-axis", translation.casefold())
        self.assertIn("evidence-to-claim matrix", translation.casefold())
        self.assertNotIn("prospective beats retrospective", translation.casefold())
        threshold = read("skills/radiology-translation/references/threshold-to-action.md")
        self.assertIn("does not directly observe", threshold.casefold())
        self.assertIn("final evaluation set", threshold.casefold())
        prospective = read("skills/radiology-translation/references/prospective-deployment.md")
        self.assertIn("no universal strength ranking", prospective.casefold())

    def test_reproducibility_separates_computational_and_external_axes(self) -> None:
        skill = read("skills/radiology-reproducibility/SKILL.md")
        self.assertIn(
            "TRACEABLE -> RERUNNABLE -> REPLAYED -> INDEPENDENTLY_REPRODUCED", skill
        )
        self.assertIn("separate scientific-validation axis", skill)
        passport = read(
            "skills/radiology-reproducibility/templates/reproducibility-passport.md"
        )
        self.assertIn("requested computational level", passport)
        self.assertIn("separate scientific-validation state", passport)

    def test_data_design_review_thesis_reporting_and_postpublication_extensions_exist(self) -> None:
        contracts = {
            "skills/radiology-data/references/data-lifecycle-management-plan.md": (
                "living",
                "retention",
                "request",
            ),
            "skills/radiology-design/references/registered-reports-ppi-and-equity.md": (
                "registered report",
                "ppi",
                "equity",
            ),
            "skills/radiology-prereview/references/review-modes-and-editorial-governance.md": (
                "journal-peer-review",
                "confidential",
                "conflict",
            ),
            "skills/radiology-writing/references/thesis-and-dissertation-architecture.md": (
                "monograph",
                "article-based",
                "thesis-to-paper",
            ),
            "skills/radiology-pipeline/references/post-publication-and-staleness-lifecycle.md": (
                "correction",
                "retraction",
                "stale",
            ),
            "skills/radiology-reporting/references/guideline-consensus-qualitative-economic-implementation.md": (
                "right",
                "coreq",
                "cheers",
            ),
        }
        for path, terms in contracts.items():
            text = read(path).casefold()
            for term in terms:
                self.assertIn(term, text, f"{path} lacks {term}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
