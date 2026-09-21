#!/usr/bin/env python3
"""Regression tests for deterministic release identity helpers."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().with_name("build_release.py")
SPEC = importlib.util.spec_from_file_location("build_release", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class BuildReleaseTests(unittest.TestCase):
    def test_tree_digest_changes_with_content_not_mtime(self) -> None:
        entries = [
            {"path": "a.txt", "size": 1, "sha256": "a" * 64},
            {"path": "nested/b.txt", "size": 2, "sha256": "b" * 64},
        ]
        first = MODULE.tree_digest(entries)
        self.assertEqual(first, MODULE.tree_digest(list(reversed(entries))))
        changed = [dict(entry) for entry in entries]
        changed[0]["sha256"] = "c" * 64
        self.assertNotEqual(first, MODULE.tree_digest(changed))

    def test_deterministic_archives_have_equal_sha256(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "tree"
            root.mkdir()
            (root / "a.txt").write_text("alpha\n", encoding="utf-8")
            nested = root / "nested"
            nested.mkdir()
            (nested / "b.txt").write_text("beta\n", encoding="utf-8")
            entries = [
                {"path": "a.txt", "size": 6, "sha256": MODULE.sha256_file(root / "a.txt")},
                {"path": "nested/b.txt", "size": 5, "sha256": MODULE.sha256_file(nested / "b.txt")},
            ]
            first = Path(temp) / "first.zip"
            second = Path(temp) / "second.zip"
            MODULE.deterministic_zip(root, first, entries)
            MODULE.deterministic_zip(root, second, list(reversed(entries)))
            self.assertEqual(MODULE.sha256_file(first), MODULE.sha256_file(second))

    def test_copy_refuses_existing_or_nested_staging(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "source"
            source.mkdir()
            existing = Path(temp) / "existing"
            existing.mkdir()
            with self.assertRaises(FileExistsError):
                MODULE.copy_allowlisted(source, existing)
            with self.assertRaises(ValueError):
                MODULE.copy_allowlisted(source, source / "release-build")

    def test_toolchain_identity_comes_from_requested_interpreter(self) -> None:
        try:
            identity = MODULE.python_toolchain(Path(sys.executable).resolve())
            pwsh_version = MODULE.powershell_toolchain()["version"]
        except (OSError, subprocess.SubprocessError) as exc:
            self.skipTest(
                "release toolchain probe needs a real Python 3.10+ with PyYAML/pypdf/Pillow "
                f"plus pwsh on PATH: {exc}"
            )
        self.assertEqual(Path(identity["executable"]).resolve(), Path(sys.executable).resolve())
        self.assertTrue({"PyYAML", "pypdf", "Pillow"}.issubset(identity["packages"]))
        self.assertTrue(pwsh_version)


if __name__ == "__main__":
    unittest.main(verbosity=2)
