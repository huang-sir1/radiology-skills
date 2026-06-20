---
name: radiology-polishing
description: "Polish finished imaging-research prose to Radiology (RSNA) house style — clear active-or-passive sentences, past tense in Methods/Results, precise statistical reporting (estimates with 95% CIs, exact p-values, correct number/unit formatting), American English, correct abbreviation use, and detection of overclaiming or unwarranted causal language. Use when the user wants to tighten, copyedit, or align existing sentences/paragraphs to Radiology style (not draft new content — use radiology-writing for that). Returns clean copy-paste prose plus a short change log; never alters reported numbers or invents content."
---

# Radiology-Style Prose Polishing

Use this skill to take **existing** imaging-research prose and make it read the way
_Radiology_ publishes — precise, concise, correctly formatted, and free of overclaiming. For
building new content, use `radiology-writing`.

## Core stance

- **Preserve meaning and numbers exactly.** Never change a reported value, CI, p-value, n, or
  citation. Flag suspected errors; don't silently "fix" data.
- **Clarity over flourish.** Short, direct sentences; one idea each. Remove filler ("it is
  worth noting that," "very," "novel").
- **Precise stats reporting** — estimate + 95% CI; exact p (`P = .03`); correct number/unit
  format; named test. (stat-reporting.md)
- **American English** (color, tumor, analyze, catheterization) — _Radiology_ house style.
- **Calibrate claims to evidence** — flag overclaiming and unwarranted causation.
- **Section-aware tense** — Methods/Results past tense; established facts present.

## When to use

- "Tighten / copyedit / polish this paragraph for _Radiology_."
- "Fix the statistical reporting and number formatting."
- "Convert to American English and journal style."
- "Is this overclaiming?"

## When to open extra files

| File | Open when |
|---|---|
| [references/radiology-house-style.md](references/radiology-house-style.md) | Voice, tense, abbreviations, American spelling, terminology, units |
| [references/stat-reporting.md](references/stat-reporting.md) | Formatting p-values, CIs, decimals, percentages, n, ranges, and test names |
| [references/style-guardrails.md](references/style-guardrails.md) | Overclaim/causation detection, hedging calibration, forbidden phrasings |

## Workflow

1. **Identify the section** (sets tense and expectations).
2. **Pass 1 — clarity:** split long sentences, cut filler, fix vague verbs, ensure each
   sentence has one idea and the subject is clear.
3. **Pass 2 — statistics & numbers:** enforce estimate + CI, exact p, decimal/unit format,
   named tests (stat-reporting.md). Do **not** change values.
4. **Pass 3 — house style:** American English, abbreviation rules (define at first use; not
   in Key Results), terminology, units.
5. **Pass 4 — guardrails:** flag overclaiming, causal language unsupported by design,
   "first/novel," scope creep; propose calibrated wording (style-guardrails.md).
6. **Return** clean prose + a concise change log; list any flags the author must resolve.

## Output format

1. **`Polished`** — clean, copy-paste-ready prose.
2. **`Change log`** — grouped bullets (clarity / stats / style / claims); brief.
3. **`Flags`** — items needing author decision (possible data error, unverifiable "first,"
   missing CI the author must supply). Never fabricate the missing number.

## Quality bar

Reads like a careful _Radiology_ copyeditor who tightened the prose and corrected the
statistical reporting **without touching the science** — and who flagged, rather than hid,
every overclaim and every missing CI.

## Handoffs
- Restructuring / new content → `radiology-writing`.
- Computing a missing statistic → `radiology-stats`.
- Checklist compliance → `radiology-reporting`.
