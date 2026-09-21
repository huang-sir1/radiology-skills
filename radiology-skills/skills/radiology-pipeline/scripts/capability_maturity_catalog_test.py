#!/usr/bin/env python3
"""Release-inventory regression tests for capability maturity catalog governance."""

from __future__ import annotations

import copy
import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("validate_capability_maturity_catalog.py")
SPEC = importlib.util.spec_from_file_location("validate_capability_maturity_catalog", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CapabilityMaturityCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = MODULE.load_registry(MODULE.DEFAULT_REGISTRY)
        cls.readme = MODULE.DEFAULT_README.read_text(encoding="utf-8")

    def validate(self, payload: dict | None = None, readme: str | None = None) -> list[str]:
        return MODULE.validate_catalog(
            copy.deepcopy(payload if payload is not None else self.payload),
            root=MODULE.ROOT,
            readme_text=self.readme if readme is None else readme,
        )

    def entry(self, payload: dict, skill_id: str) -> dict:
        return next(item for item in payload["skills"] if item["skill_id"] == skill_id)

    def test_current_tree_passes(self) -> None:
        self.assertEqual([], self.validate())

    def test_runtime_directory_coverage_is_exact(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["skills"].pop()
        errors = self.validate(payload)
        self.assertTrue(any("runtime directory coverage mismatch" in error for error in errors), errors)

    def test_runtime_skill_cannot_be_planned(self) -> None:
        payload = copy.deepcopy(self.payload)
        self.entry(payload, "radiology-writing")["framework_state"] = "PLANNED"
        errors = self.validate(payload)
        self.assertTrue(any("runtime skills cannot" in error for error in errors), errors)

    def test_invalid_enum_is_rejected(self) -> None:
        payload = copy.deepcopy(self.payload)
        self.entry(payload, "radiology-writing")["boundary_state"] = "LOOKS_GOOD"
        errors = self.validate(payload)
        self.assertTrue(any("invalid boundary_state" in error for error in errors), errors)

    def test_static_string_pass_cannot_upgrade(self) -> None:
        payload = copy.deepcopy(self.payload)
        self.entry(payload, "radiology-acquisition-qc")["maturity_label"] = "EXPERIMENTAL"
        errors = self.validate(payload)
        self.assertTrue(any("STATIC_CONTRACT_ONLY cannot upgrade" in error for error in errors), errors)

    def test_validated_requires_all_release_evidence(self) -> None:
        payload = copy.deepcopy(self.payload)
        entry = self.entry(payload, "radiology-pipeline")
        entry["maturity_label"] = "VALIDATED"
        entry["release_eligible"] = True
        errors = self.validate(payload)
        self.assertTrue(any("VALIDATED requires executable" in error for error in errors), errors)
        self.assertTrue(any("structured validation_receipt" in error for error in errors), errors)
        self.assertTrue(any("NOT_ADJUDICATED behavior" in error for error in errors), errors)

    def test_missing_evidence_path_is_rejected(self) -> None:
        payload = copy.deepcopy(self.payload)
        entry = self.entry(payload, "radiology-acquisition-qc")
        entry["evidence"]["static_checks"] = ["missing/catalog-evidence.ps1"]
        errors = self.validate(payload)
        self.assertTrue(any("evidence path does not exist" in error for error in errors), errors)

    def test_readme_requires_canonical_link_and_registry_status(self) -> None:
        readme = self.readme.replace(
            "skills/radiology-writing/SKILL.md",
            "skills/radiology-writing/README.md",
            1,
        )
        errors = self.validate(readme=readme)
        self.assertTrue(any("canonical skill-link coverage" in error for error in errors), errors)
        self.assertTrue(any("not per-skill README.md" in error for error in errors), errors)

    def test_planned_capability_cannot_live_under_runtime_skills(self) -> None:
        payload = copy.deepcopy(self.payload)
        payload["planned_capabilities"] = [
            {
                "capability_id": "radiology-future-capability",
                "path": "skills/radiology-future-capability",
                "framework_state": "PLANNED",
                "release_eligible": False,
                "evidence_paths": [
                    "skills/radiology-pipeline/references/"
                    "capability-maturity-and-release-governance.md"
                ],
            }
        ]
        errors = self.validate(payload)
        self.assertTrue(any("planned path must stay under roadmap/skills" in error for error in errors), errors)

    def test_duplicate_json_key_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "duplicate.json"
            path.write_text('{"schema_version":"1.0","schema_version":"2.0"}', encoding="utf-8")
            with self.assertRaises(MODULE.DuplicateKeyError):
                MODULE.load_registry(path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
