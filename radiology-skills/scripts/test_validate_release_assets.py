#!/usr/bin/env python3
"""Regression tests for fail-closed release metadata parsing."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().with_name("validate_release_assets.py")
SPEC = importlib.util.spec_from_file_location("validate_release_assets", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ReleaseAssetValidationTests(unittest.TestCase):
    def test_duplicate_openai_yaml_and_frontmatter_keys_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            skill = root / "skills" / "radiology-test"
            agents = skill / "agents"
            agents.mkdir(parents=True)
            (agents / "openai.yaml").write_text(
                "interface:\n"
                "  display_name: Test\n"
                "  short_description: first\n"
                "  short_description: second\n"
                "  default_prompt: Use $radiology-test.\n",
                encoding="utf-8",
            )
            (skill / "SKILL.md").write_text(
                "---\n"
                "name: radiology-test\n"
                "name: radiology-test\n"
                "description: Test.\n"
                "---\n",
                encoding="utf-8",
            )
            (root / "README.md").write_text(
                "See [missing artifact][missing].\n\n[missing]: ./does-not-exist.md\n",
                encoding="utf-8",
            )

            errors, counts = MODULE.validate(root)
            self.assertEqual(1, counts["openai_yaml"])
            self.assertEqual(1, counts["skills"])
            self.assertTrue(any("duplicate key: 'short_description'" in error for error in errors))
            self.assertTrue(any("duplicate key: 'name'" in error for error in errors))
            self.assertTrue(any("broken local link README.md" in error for error in errors))


if __name__ == "__main__":
    unittest.main(verbosity=2)
