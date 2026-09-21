#!/usr/bin/env python3
"""Repository-wide progressive-disclosure and resource-reachability lint."""

from __future__ import annotations

import math
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".py", ".ps1", ".csv", ".tsv", ".txt"}
RESOURCE_DIRS = {"references", "templates", "assets", "scripts"}
TRIGGER_SECTION_MARKERS = (
    "## When to use",
    "## When to open extra files",
    "## Route by mode",
    "## Route by task",
    "## Choose the mode",
    "## Choose an operating mode",
    "## Choose the entry mode",
    "## Choose the product and mode",
    "## Operating modes",
    "## Ownership gate",
)


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def runtime_files(skill: Path) -> list[Path]:
    result: list[Path] = []
    for path in skill.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        relative = path.relative_to(skill)
        if "tests" in relative.parts or "__pycache__" in relative.parts:
            continue
        if (
            path.name == "README.md"
            or path.name.startswith(("test_", "validate_"))
            or path.name.endswith("_test.py")
        ):
            continue
        result.append(path)
    return sorted(result)


def reachable_resources(skill: Path) -> tuple[set[Path], set[Path]]:
    files = runtime_files(skill)
    entry = skill / "SKILL.md"
    resources = {
        path for path in files
        if set(path.relative_to(skill).parts) & RESOURCE_DIRS and path != entry
    }
    content = {path: text(path) for path in files}
    gate_text = "\n".join(
        text(path) for path in skill.rglob("*")
        if path.is_file() and path.suffix.lower() in {".py", ".ps1"}
        and (path.name.startswith(("test_", "validate_")) or path.name.endswith("_test.py"))
        and "__pycache__" not in path.parts
    )
    gate_only_scripts = {
        path for path in resources
        if "scripts" in path.relative_to(skill).parts
        and path.name in gate_text
        and not any(path.name in body for body in content.values())
    }
    resources -= gate_only_scripts
    edges: dict[Path, set[Path]] = {path: set() for path in files}
    for source, body in content.items():
        for target in files:
            if source == target:
                continue
            relative = target.relative_to(skill).as_posix()
            if target.name in body or relative in body:
                edges[source].add(target)
    reached: set[Path] = {entry}
    frontier = [entry]
    while frontier:
        source = frontier.pop()
        for target in edges.get(source, set()):
            if target not in reached:
                reached.add(target)
                frontier.append(target)
    return resources, reached


class ProgressiveDisclosureContracts(unittest.TestCase):
    def test_discovery_metadata_retains_space_for_future_routes(self) -> None:
        total = 0
        for skill in SKILLS.iterdir():
            path = skill / "SKILL.md"
            if not path.is_file():
                continue
            match = re.search(r'^description:\s*["\'](.+)["\']\s*$', text(path), re.MULTILINE)
            self.assertIsNotNone(match, f"{skill.name} lacks one quoted description")
            total += len(match.group(1)) + 2
        self.assertLessEqual(total, 4500, f"discovery metadata uses {total}/5000 characters")

    def test_entrypoints_stay_within_conservative_context_surrogate(self) -> None:
        for skill in SKILLS.iterdir():
            path = skill / "SKILL.md"
            if not path.is_file():
                continue
            body = text(path)
            words = len(re.findall(r"\S+", body))
            estimated_units = max(math.ceil(len(body.encode("utf-8")) / 4), math.ceil(words * 1.35))
            self.assertLessEqual(
                estimated_units, 5400,
                f"{skill.name} entrypoint uses {estimated_units} conservative context units; move detail to references",
            )

    def test_every_runtime_resource_is_reachable_from_skill_entrypoint(self) -> None:
        orphans: list[str] = []
        for skill in SKILLS.iterdir():
            if not (skill / "SKILL.md").is_file():
                continue
            resources, reached = reachable_resources(skill)
            orphans.extend(
                path.relative_to(ROOT).as_posix() for path in sorted(resources - reached)
            )
        self.assertEqual([], orphans, "unreachable runtime resources: " + ", ".join(orphans))

    def test_entrypoints_do_not_route_to_legacy_readmes(self) -> None:
        offenders: list[str] = []
        for path in SKILLS.glob("radiology-*/SKILL.md"):
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text(path)):
                if target.split("#", 1)[0].lower().endswith("readme.md"):
                    offenders.append(f"{path.relative_to(ROOT).as_posix()} -> {target}")
        self.assertEqual([], offenders)

    def test_every_entrypoint_exposes_a_trigger_surface(self) -> None:
        missing: list[str] = []
        for skill in SKILLS.iterdir():
            path = skill / "SKILL.md"
            if not path.is_file():
                continue
            body = text(path)
            if not any(marker in body for marker in TRIGGER_SECTION_MARKERS):
                missing.append(skill.name)
        self.assertEqual(
            [], missing, "entrypoints without a when-to-use surface: " + ", ".join(missing),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
