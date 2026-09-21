---
name: radiology-polishing
description: "Polish existing research prose while preserving facts and claims; not drafting or scientific repair."
---

# Venue-routed radiology and mechanism prose polishing

Use this skill to take **existing** imaging, omics, pathology, perturbation or imaging–mechanism
prose and make it precise, concise, correctly formatted and evidence-bounded in the selected venue's
voice. The _Radiology_ route is one venue route, not the default for standalone mechanism studies.
For building new content, use `radiology-writing`.

## Core stance

- **Preserve meaning and numbers exactly.** Never change a reported value, CI, p-value, n, or
  citation. Flag suspected errors; don't silently "fix" data.
- **Clarity over flourish.** Short, direct sentences; one idea each. Remove filler ("it is
  worth noting that," "very," "novel").
- **Precise stats reporting** — estimate + 95% CI; exact p (`P = .03`); correct number/unit
  format; named test. (stat-reporting.md)
- **Venue-correct English and number style.** Use American English on the _Radiology_ route; apply
  the verified target venue's rules when they differ.
- **Calibrate claims to evidence** — flag overclaiming and unwarranted causation.
- **Section-aware tense** — Methods/Results past tense; established facts present.

## When to use

- "Tighten / copyedit / polish this paragraph for _Radiology_."
- "Polish this scRNA/spatial Results paragraph for the selected Nature Portfolio journal."
- "Shorten this imaging–mechanism Discussion without upgrading association to causality."
- "Fix the statistical reporting and number formatting."
- "Convert to American English and journal style."
- "Is this overclaiming?"

## When to open extra files

| File | Open when |
|---|---|
| [references/radiology-house-style.md](references/radiology-house-style.md) | Voice, tense, abbreviations, American spelling, terminology, units |
| [references/stat-reporting.md](references/stat-reporting.md) | Formatting p-values, CIs, decimals, percentages, n, ranges, and test names |
| [references/style-guardrails.md](references/style-guardrails.md) | Overclaim/causation detection, hedging calibration, forbidden phrasings |
| [references/venue-voice-and-house-style.md](references/venue-voice-and-house-style.md) | Target venue is known, or the user supplied author-guide PDFs/classic papers and wants European Radiology / Nature Partner / npj / other venue voice rather than generic Radiology polish |

## Workflow

0. **Confirm the target venue.** Use the _Radiology_ route only when it is selected or the manuscript
   is imaging-centred and the user explicitly wants that fallback. For an unresolved venue, retain
   neutral scientific English and mark exact house-style items `VENUE_STYLE_UNVERIFIED`; leading-zero,
   number and reference rules can change across families.
0. **For venue-specific voice**, open `venue-voice-and-house-style.md` and apply the target
   family's wording, abbreviation, p-value, data-availability, and pending-guide checks.
0. **If the project has an author style profile**, read
   `../radiology-writing/references/section-contract-and-style-profile.md`. Apply truth/reporting
   and journal rules first, then compatible author preferences; never polish to imitate a third
   party or evade AI detection.
1. **Identify the section** (sets tense and expectations).
2. **Pass 1 — clarity:** split long sentences, cut filler, fix vague verbs, ensure each
   sentence has one idea and the subject is clear.
3. **Pass 2 — statistics & numbers:** enforce estimate + CI, exact p, decimal/unit format,
   named tests (stat-reporting.md). Do **not** change values.
4. **Pass 3 — house style:** apply the selected venue's spelling, abbreviations, terminology and
   units. American English and the no-abbreviation Key Results rule apply on the verified
   _Radiology_ route; keep neutral conventions when the venue is unresolved.
5. **Pass 4 — guardrails:** flag overclaiming, causal language unsupported by design,
   "first/novel," scope creep; propose calibrated wording (style-guardrails.md).
6. **Return** clean prose + a concise change log; list any flags the author must resolve.

## Output format

1. **`Polished`** — clean, copy-paste-ready prose.
2. **`Change log`** — grouped bullets (clarity / stats / style / claims); brief.
3. **`Venue checks`** — house-style items applied, plus any exact limits marked
   `VERIFY FROM GUIDE`.
4. **`Style-profile note`** — when samples were supplied: profile strength, compatible traits
   applied, and any conflict resolved in favor of scientific/journal convention.
5. **`Flags`** — items needing author decision (possible data error, unverifiable "first,"
   missing CI the author must supply). Never fabricate the missing number.

## Quality bar

Reads like a careful _Radiology_ copyeditor who tightened the prose and corrected the
statistical reporting **without touching the science** — and who flagged, rather than hid,
every overclaim and every missing CI.

## Handoffs
- Restructuring / new content → `radiology-writing`.
- Computing a missing statistic → `radiology-stats`.
- Checklist compliance → `radiology-reporting`.
