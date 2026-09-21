#!/usr/bin/env python3
"""Adversarial regression for release-allowlist path containment."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


RELEASE_GATE = Path(__file__).resolve().with_name("validate_release_boundary.ps1")


@unittest.skipUnless(shutil.which("pwsh"), "release gate tests require pwsh on PATH")
class ReleaseAllowlistBoundaryTests(unittest.TestCase):
    REQUIRED_ALLOWLIST = [
        ".claude-plugin/", ".codex-plugin/", "skills/", "behavior-evals/", "README.md",
        "install.md", "LICENSE", ".gitignore", "RELEASE.md", "release-allowlist.txt", "scripts/",
    ]

    def make_product(self, root: Path, developer_name: str = "test") -> None:
        (root / ".claude-plugin").mkdir(parents=True)
        (root / ".codex-plugin").mkdir()
        (root / "skills").mkdir()
        (root / "behavior-evals").mkdir()
        (root / "scripts").mkdir()
        identity = {
            "name": "test", "version": "1.0.0", "description": "test",
            "author": {"name": "test"}, "license": "test-license",
        }
        (root / ".claude-plugin" / "plugin.json").write_text(
            json.dumps(identity), encoding="utf-8",
        )
        marketplace = {
            "name": "test", "owner": {"name": "test"},
            "plugins": [{
                "name": "test", "version": "1.0.0", "description": "test", "source": "./",
            }],
        }
        (root / ".claude-plugin" / "marketplace.json").write_text(
            json.dumps(marketplace), encoding="utf-8",
        )
        codex = {
            **identity, "skills": "./skills/",
            "interface": {
                "displayName": "Test", "shortDescription": "Test plugin",
                "longDescription": "Test plugin fixture", "developerName": developer_name,
                "category": "Research", "capabilities": ["Analysis"],
                "defaultPrompt": ["Test prompt"],
            },
        }
        (root / ".codex-plugin" / "plugin.json").write_text(
            json.dumps(codex), encoding="utf-8",
        )
        (root / ".gitignore").write_text(
            "/research/\n/tmp/\n**/__pycache__/\n*.py[cod]\n", encoding="utf-8",
        )
        for name in ("README.md", "install.md", "LICENSE", "RELEASE.md"):
            (root / name).write_text("test\n", encoding="utf-8")
        (root / "scripts" / "release-test-inventory.json").write_text(
            json.dumps({"schema_version": "1.0", "python_tests": [], "powershell_validators": []}),
            encoding="utf-8",
        )

    def run_gate(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run([
            "pwsh", "-NoProfile", "-File", str(RELEASE_GATE),
            "-ProductRoot", str(root), "-PythonExecutable", sys.executable,
        ], check=False, capture_output=True, text=True, encoding="utf-8")

    def test_dot_parent_and_absolute_entries_fail_before_enumeration(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "product"
            self.make_product(root)
            absolute = root.parent / "outside"
            (root / "release-allowlist.txt").write_text(
                f"README.md\n./research/\n../outside/\n{absolute}\n", encoding="utf-8",
            )

            result = self.run_gate(root)
            output = result.stdout + result.stderr
            self.assertNotEqual(0, result.returncode)
            self.assertIn(
                "Allowlist entry contains an empty, dot or parent segment: ./research/", output,
            )
            self.assertIn(
                "Allowlist entry contains an empty, dot or parent segment: ../outside/", output,
            )
            self.assertIn(
                "Allowlist entry must be a non-rooted path below the product root", output,
            )

    @unittest.skipUnless(os.name == "nt", "attrib hidden-attribute fixture requires Windows")
    def test_extra_surface_developer_drift_and_hidden_payload_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "product"
            self.make_product(root, developer_name="Attacker")
            private_dir = root / "private-data"
            private_dir.mkdir()
            (private_dir / "patient-export.pdf").write_bytes(b"synthetic fixture")
            hidden_executable = root / "skills" / "payload.exe"
            hidden_executable.write_bytes(b"MZ synthetic fixture")
            subprocess.run(
                ["attrib", "+H", str(hidden_executable)], check=True,
                capture_output=True, text=True, encoding="utf-8",
            )
            dot_dir = root / "skills" / ".secret"
            dot_dir.mkdir()
            (dot_dir / "payload.bin").write_bytes(b"synthetic fixture")
            entries = [*self.REQUIRED_ALLOWLIST, "private-data/"]
            (root / "release-allowlist.txt").write_text("\n".join(entries) + "\n", encoding="utf-8")
            try:
                result = self.run_gate(root)
            finally:
                subprocess.run(
                    ["attrib", "-H", str(hidden_executable)], check=False,
                    capture_output=True, text=True, encoding="utf-8",
                )
            output = result.stdout + result.stderr
            self.assertNotEqual(0, result.returncode)
            self.assertIn("Unapproved extra top-level release surface is allowlisted: private-data", output)
            self.assertIn("Claude, marketplace and Codex author/owner identities must match", output)
            self.assertIn("Hidden, system or dot-prefixed payload exists", output)
            self.assertIn("Forbidden generated or compiled artifact exists", output)

    def test_missing_frozen_tests_and_validators_cannot_zero_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "product"
            self.make_product(root)
            (root / "release-allowlist.txt").write_text(
                "\n".join(self.REQUIRED_ALLOWLIST) + "\n", encoding="utf-8",
            )
            (root / "scripts" / "release-test-inventory.json").write_text(
                json.dumps({
                    "schema_version": "1.0",
                    "python_tests": ["scripts/test_required.py"],
                    "powershell_validators": [
                        "skills/radiology-test/scripts/validate_required.ps1",
                    ],
                }),
                encoding="utf-8",
            )
            result = self.run_gate(root)
            output = result.stdout + result.stderr
            self.assertNotEqual(0, result.returncode)
            self.assertIn(
                "Frozen Python test inventory member is missing: scripts/test_required.py", output,
            )
            self.assertIn(
                "Frozen PowerShell validator inventory member is missing: "
                "skills/radiology-test/scripts/validate_required.ps1",
                output,
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
