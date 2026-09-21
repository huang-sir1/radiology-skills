#!/usr/bin/env python3
"""Validate release JSON/YAML, skill identities, and local Markdown links."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml


LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
REFERENCE_LINK_RE = re.compile(r"(?m)^\s{0,3}\[(?!\^)[^\]]+\]:\s*(<[^>]+>|\S+)")
FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---", re.DOTALL)


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects parser-dependent duplicate mappings."""


def construct_unique_mapping(
    loader: UniqueKeyLoader, node: yaml.nodes.MappingNode, deep: bool = False,
) -> dict[object, object]:
    mapping: dict[object, object] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in mapping
        except TypeError as exc:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping", node.start_mark,
                "found an unhashable mapping key", key_node.start_mark,
            ) from exc
        if duplicate:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping", node.start_mark,
                f"found duplicate key: {key!r}", key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_unique_mapping,
)


def load_unique_yaml(text: str) -> object:
    return yaml.load(text, Loader=UniqueKeyLoader)


def reject_duplicate_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def release_files(root: Path) -> list[Path]:
    paths: list[Path] = []
    for relative in (".claude-plugin", ".codex-plugin", "skills", "behavior-evals", "scripts"):
        base = root / relative
        if base.is_dir():
            paths.extend(path for path in base.rglob("*") if path.is_file())
    for relative in ("README.md", "RELEASE.md", "install.md"):
        path = root / relative
        if path.is_file():
            paths.append(path)
    return sorted(set(paths))


def local_link_target(source: Path, raw: str, root: Path) -> Path | None:
    value = raw.strip()
    if value.startswith("<") and value.endswith(">"):
        value = value[1:-1].strip()
    elif " " in value:
        value = value.split(" ", 1)[0]
    lowered = value.lower()
    if not value or value.startswith("#") or lowered.startswith((
        "http://", "https://", "mailto:", "codex:", "data:",
    )):
        return None
    path_text = unquote(value.split("#", 1)[0])
    if not path_text:
        return None
    candidate = (source.parent / path_text).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"link escapes release root: {raw}") from exc
    return candidate


def validate(root: Path) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    counts = {"json": 0, "openai_yaml": 0, "skills": 0, "markdown_links": 0}
    files = release_files(root)

    for path in files:
        relative = path.relative_to(root).as_posix()
        if path.suffix.lower() == ".json":
            counts["json"] += 1
            try:
                json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_pairs)
            except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
                errors.append(f"invalid JSON {relative}: {exc}")

        if path.name == "openai.yaml" and path.parent.name == "agents":
            counts["openai_yaml"] += 1
            try:
                payload = load_unique_yaml(path.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError, yaml.YAMLError) as exc:
                errors.append(f"invalid YAML {relative}: {exc}")
                continue
            interface = payload.get("interface") if isinstance(payload, dict) else None
            if not isinstance(interface, dict):
                errors.append(f"{relative}: interface must be an object")
                continue
            for field in ("display_name", "short_description", "default_prompt"):
                value = interface.get(field)
                if not isinstance(value, str) or not value.strip():
                    errors.append(f"{relative}: interface.{field} must be non-empty")
            skill_name = path.parent.parent.name
            prompt = interface.get("default_prompt", "")
            if isinstance(prompt, str) and f"${skill_name}" not in prompt:
                errors.append(f"{relative}: default_prompt must name ${skill_name}")

        if path.name == "SKILL.md" and path.parent.parent == root / "skills":
            counts["skills"] += 1
            try:
                content = path.read_text(encoding="utf-8")
                match = FRONTMATTER_RE.match(content)
                if not match:
                    errors.append(f"{relative}: invalid YAML frontmatter boundary")
                    continue
                frontmatter = load_unique_yaml(match.group(1))
                if not isinstance(frontmatter, dict) or frontmatter.get("name") != path.parent.name:
                    errors.append(f"{relative}: frontmatter name must match directory")
            except (OSError, UnicodeDecodeError, yaml.YAMLError) as exc:
                errors.append(f"invalid SKILL.md {relative}: {exc}")

        if path.suffix.lower() == ".md":
            try:
                content = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError) as exc:
                errors.append(f"cannot read Markdown {relative}: {exc}")
                continue
            raw_links = LINK_RE.findall(content)
            raw_links.extend(REFERENCE_LINK_RE.findall(content))
            for raw_link in raw_links:
                try:
                    target = local_link_target(path, raw_link, root)
                except ValueError as exc:
                    errors.append(f"{relative}: {exc}")
                    continue
                if target is None:
                    continue
                counts["markdown_links"] += 1
                if not target.exists():
                    errors.append(f"broken local link {relative}: {raw_link}")
    return errors, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=Path(__file__).resolve().parents[1], type=Path)
    args = parser.parse_args()
    root = args.root.expanduser().resolve()
    errors, counts = validate(root)
    report = {"status": "FAIL" if errors else "PASS", "counts": counts, "errors": errors}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
