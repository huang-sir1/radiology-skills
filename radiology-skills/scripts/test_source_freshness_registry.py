#!/usr/bin/env python3
"""Offline, machine-readable source-freshness policy regression."""

from __future__ import annotations

import copy
import json
import re
import unittest
from datetime import date
from pathlib import Path
from unittest import mock
import tempfile


ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "scripts" / "source-freshness-registry.json"
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
FIELDS = {
    "path", "accessed_on", "source_class", "volatility", "max_age_days",
    "normative_artifact_sha256", "normative_artifact_state", "supersession_state",
    "online_verification_state",
}


def reject_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_policy() -> dict[str, object]:
    return json.loads(POLICY.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicates)


def source_access_dates(text: str) -> tuple[list[tuple[int, date]], list[str]]:
    """Read the Accessed column, never publication dates or dates embedded in URLs."""
    rows: list[tuple[int, date]] = []
    errors: list[str] = []
    access_column: int | None = None
    fence: str | None = None
    for line_number, raw_line in enumerate(text.splitlines(), 1):
        line = raw_line.lstrip(" ")
        if len(raw_line) - len(line) > 3:
            access_column = None
            continue
        if line.startswith(("```", "~~~")):
            marker = line[:3]
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
            access_column = None
            continue
        if fence is not None:
            continue
        if not line.startswith("|"):
            access_column = None
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        headers = [cell.lower() for cell in cells]
        if "accessed" in headers:
            access_column = headers.index("accessed")
            continue
        if all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            continue
        if access_column is None:
            if "http" in line:
                errors.append(f"line {line_number}: source row has no Accessed column")
            continue
        if access_column >= len(cells):
            errors.append(f"line {line_number}: source row has no Accessed column")
            continue
        raw_date = cells[access_column]
        try:
            if not DATE_RE.fullmatch(raw_date):
                raise ValueError("not an ISO access date")
            accessed = date.fromisoformat(raw_date)
        except ValueError:
            errors.append(f"line {line_number}: invalid source Accessed date")
            continue
        rows.append((line_number, accessed))
    return rows, errors


def validate(payload: dict[str, object], *, today: date) -> list[str]:
    errors: list[str] = []
    if payload.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    online_states = set(payload.get("online_result_states", []))
    entries = payload.get("registries", [])
    if not isinstance(entries, list):
        return errors + ["registries must be a list"]
    discovered = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "skills").rglob("source-registry.md")
    }
    declared: set[str] = set()
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"registries[{index}] must be an object")
            continue
        if set(entry) != FIELDS:
            errors.append(f"registries[{index}] fields do not match schema")
        relative = entry.get("path")
        if not isinstance(relative, str) or relative in declared:
            errors.append(f"registries[{index}].path is missing or duplicate")
            continue
        declared.add(relative)
        if relative not in discovered:
            errors.append(f"unregistered or unsafe source registry path: {relative}")
            continue
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing source registry: {relative}")
            continue
        try:
            accessed = date.fromisoformat(str(entry.get("accessed_on")))
        except ValueError:
            errors.append(f"{relative}: invalid accessed_on")
            continue
        age = (today - accessed).days
        max_age = entry.get("max_age_days")
        if age < 0:
            errors.append(f"{relative}: accessed_on is in the future")
        if not isinstance(max_age, int) or max_age <= 0:
            errors.append(f"{relative}: max_age_days must be positive")
        elif age > max_age:
            errors.append(f"{relative}: source registry is stale ({age}>{max_age} days)")
        source_rows, row_errors = source_access_dates(path.read_text(encoding="utf-8"))
        errors.extend(f"{relative}: {error}" for error in row_errors)
        if not source_rows:
            errors.append(f"{relative}: no source rows")
        for line_number, source_date in source_rows:
            source_age = (today - source_date).days
            if source_age < 0:
                errors.append(f"{relative}:{line_number}: source Accessed date is in the future")
            if source_date > accessed:
                errors.append(f"{relative}:{line_number}: source Accessed date exceeds registry maintenance date")
            if isinstance(max_age, int) and max_age > 0 and source_age > max_age:
                errors.append(f"{relative}:{line_number}: source row is stale ({source_age}>{max_age} days)")
        sha = entry.get("normative_artifact_sha256")
        artifact_state = entry.get("normative_artifact_state")
        if sha is None and artifact_state != "NOT_CAPTURED_LIVE_SOURCE":
            errors.append(f"{relative}: absent artifact hash needs NOT_CAPTURED_LIVE_SOURCE")
        if sha is not None and (not isinstance(sha, str) or not SHA_RE.fullmatch(sha)):
            errors.append(f"{relative}: invalid normative_artifact_sha256")
        if entry.get("supersession_state") not in {"LIVE_RECHECK_AT_USE", "NO_KNOWN_SUPERSESSION"}:
            errors.append(f"{relative}: invalid supersession_state")
        if entry.get("online_verification_state") not in online_states:
            errors.append(f"{relative}: invalid online_verification_state")
    if declared != discovered:
        errors.append(
            "source registry inventory mismatch: "
            f"missing={sorted(discovered - declared)}, extra={sorted(declared - discovered)}"
        )
    return errors


class SourceFreshnessRegistryTests(unittest.TestCase):
    def test_current_registry_is_complete_and_fresh(self) -> None:
        self.assertEqual([], validate(load_policy(), today=date.today()))

    def test_future_clock_exposes_stale_sources(self) -> None:
        payload = copy.deepcopy(load_policy())
        errors = validate(payload, today=date(2030, 1, 1))
        self.assertTrue(any("is stale" in error for error in errors))

    def test_source_validators_do_not_freeze_policy_access_date(self) -> None:
        payload = load_policy()
        for entry in payload["registries"]:
            skill_root = (ROOT / entry["path"]).parents[1]
            for validator in (skill_root / "scripts").glob("validate_*.ps1"):
                self.assertNotIn(
                    entry["accessed_on"], validator.read_text(encoding="utf-8"),
                    f"{validator} freezes a snapshot date instead of checking policy age",
                )

    def test_online_state_distinguishes_failure_modes(self) -> None:
        states = set(load_policy()["online_result_states"])
        self.assertTrue({
            "HTTP_404_OR_410", "NETWORK_UNAVAILABLE", "RATE_LIMITED_403_OR_429",
            "PORTAL_OR_AUTH_REQUIRED", "REACHABLE_EXACT_ARTIFACT",
        }.issubset(states))

    def test_access_dates_are_read_from_the_named_column(self) -> None:
        rows, errors = source_access_dates(
            "| Source | Version | Accessed |\n|---|---|---|\n"
            "| https://example.org/2026-09-04 | published 2026-09-03 | 2026-08-23 |\n"
        )
        self.assertEqual([], errors)
        self.assertEqual([(3, date(2026, 8, 23))], rows)
        _, errors = source_access_dates(
            "| Source | Accessed |\n|---|---|\n| https://example.org/2026-09-04 | not checked |\n"
        )
        self.assertTrue(any("invalid source Accessed" in error for error in errors))

    def test_partial_refresh_preserves_old_rows_and_does_not_hide_staleness(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            relative = "skills/example/references/source-registry.md"
            path = root / relative
            path.parent.mkdir(parents=True)
            path.write_text(
                "| Source | Accessed |\n|---|---|\n"
                "| https://example.org/a | 2026-08-23 |\n"
                "| https://example.org/b | 2026-09-04 |\n", encoding="utf-8",
            )
            payload = copy.deepcopy(load_policy())
            payload["registries"] = [payload["registries"][0]]
            entry = payload["registries"][0]
            entry.update(path=relative, accessed_on="2026-09-04", max_age_days=30)
            with mock.patch(f"{__name__}.ROOT", root):
                self.assertEqual([], validate(payload, today=date(2026, 9, 4)))
                entry["accessed_on"] = "2026-09-24"
                errors = validate(payload, today=date(2026, 9, 24))
                self.assertTrue(any("source row is stale" in error for error in errors))
                path.write_text(
                    "| Source | Accessed |\n|---|---|\n"
                    "| https://example.org/a | 2026-09-25 |\n", encoding="utf-8",
                )
                errors = validate(payload, today=date(2026, 9, 24))
                self.assertTrue(any("in the future" in error for error in errors))

    def test_indented_tables_and_non_url_rows_cannot_hide_old_sources(self) -> None:
        for indent in (" ", "  ", "   "):
            source = "| Source | Accessed |\n|---|---|\n| https://example.org/a | 2026-09-04 |\n\n"
            source += "\n".join(indent + line for line in (
                "| Source | Accessed |", "|---|---|", "| archived source | 2020-01-01 |",
            ))
            rows, errors = source_access_dates(source)
            self.assertEqual([], errors)
            self.assertEqual([date(2026, 9, 4), date(2020, 1, 1)], [row[1] for row in rows])
        _, errors = source_access_dates(
            "| Source | Accessed |\n|---|---|\n| unresolved source | never |\n"
        )
        self.assertTrue(errors)

    def test_documentation_code_blocks_do_not_claim_live_source_access(self) -> None:
        for fence in ("```", "~~~"):
            rows, errors = source_access_dates(
                f"{fence}\n| Source | Accessed |\n|---|---|\n"
                f"| https://example.org/a | [ACCESS_DATE] |\n{fence}\n"
            )
            self.assertEqual([], rows)
            self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main(verbosity=2)
