---
name: radiology-journal
description: "Match a finished or near-finished imaging-AI / radiomics / radiogenomics manuscript to the right target journals and build a submission tier list (reach / target / safety) grounded in each venue's publication patterns and the paper's real strengths and weaknesses. Use when the user asks where to submit, \"选刊/投哪个期刊\", journal selection, \"can this go to Nature Medicine / Lancet Digital Health / Radiology\", fit assessment, or a submission ladder. Extracts the paper's type, core selling point, and biggest weakness; grades it on the dimensions top venues weigh (external validation, prospectivity, reader study, calibration, clinical utility, sample size, centers); and returns reach/target/safety tiers with the match reason, risk, and what to strengthen first. Verifies current journal scope via live search; never selects on impact factor alone or inflates an under-validated paper."
---

# Journal Selection & Submission Tiering

Use this skill when the paper is essentially written and the question is **where to send it**.
It reads the manuscript's real strengths and weaknesses, grades it on the dimensions imaging
venues actually weigh, and returns an honest **reach / target / safety** ladder — not a wish
list ranked by impact factor.

## Core stance

- **Fit beats prestige.** The best journal is the one whose published pattern matches this
  paper's design and evidence — not the highest impact factor it might survive.
- **Grade honestly on the right axes.** External validation, prospectivity, reader/clinical-
  utility evidence, calibration, sample size, number of centers, and novelty determine tier far
  more than topic.
- **Name the biggest weakness first.** The limiting factor (single-center, no external
  validation, small n, retrospective) sets the realistic ceiling; say it plainly.
- **Patterns are durable; current scope is not.** Use the publication-pattern heuristics here,
  but **verify each candidate's current aims/scope live** (→ radiology-search) before committing.
- **A ladder, not a bet.** Give reach/target/safety with the trade-off (turnaround, fit, risk),
  and what to strengthen to move up a tier.
- **Integrity.** Don't promise acceptance, don't inflate an under-validated paper into a top-tier
  pitch, and don't pick on impact factor alone.

## When to use

- "Where should I submit this?" / "这篇文章适合投哪个期刊？/ 帮我选刊。"
- "Can my single-center retrospective radiomics paper go to Nature Medicine / Lancet Digital Health?"
- "Build me a reach/target/safety submission list."
- "What's the biggest weakness deciding my journal tier, and how do I move up?"

## When to open extra files

| File | Open when |
|---|---|
| [references/venue-patterns.md](references/venue-patterns.md) | What each imaging/clinical/AI venue tends to publish and the bar it enforces (verify live) |
| [references/fit-grading.md](references/fit-grading.md) | Grading the paper on the tier-deciding dimensions; turning the grade into reach/target/safety |
| [references/submission-logistics.md](references/submission-logistics.md) | Article types, format/word/figure limits, cover letter, suggested reviewers, transfer cascades |

## Workflow

1. **Extract the paper profile** — type (DTA / prediction / radiomics / radiogenomics / reader /
   segmentation), core selling point, and the single biggest weakness.
2. **Grade it** (fit-grading.md) on: external validation, prospectivity, reader/utility evidence,
   calibration, sample size, centers, novelty, reporting compliance.
3. **Map to venues** (venue-patterns.md) — which tiers the grade realistically reaches; reject
   obvious mismatches with the reason.
4. **Verify current scope** — hand each shortlisted venue to `radiology-search` to confirm it
   still publishes this kind of work and recently has.
5. **Build the ladder** — reach / target / safety, each with match reason, risk, turnaround
   consideration, and the one thing to strengthen to climb.
6. **Logistics** (submission-logistics.md) — article type, limits, cover-letter angle, suggested
   reviewers, and any transfer cascade.

## Output contract

1. **`Paper profile`** — type, core selling point, biggest weakness, reporting-guideline fit.
2. **`Fit grade`** — scored on the tier-deciding dimensions, with the limiting factor named.
3. **`Submission ladder`** — **Reach / Target / Safety**, each: venue (pattern-matched + to be
   verified live), match reason, risk, what to strengthen to move up.
4. **`Strengthen-first`** — the highest-leverage improvements to raise the tier (→ relevant skill).
5. **`Verify now`** — the live-scope checks to run before submitting (→ radiology-search).
6. **`Logistics`** — article type, limits, cover-letter angle, suggested reviewers.

## Quality bar

A good selection reads like a mentor who has published across these venues: it names the paper's
ceiling honestly, gives a realistic ladder, verifies scope rather than trusting memory, and tells
the author exactly what to strengthen to aim higher — never selling impact factor as fit.

## Handoffs

- Pre-submission audit to fix weaknesses first → `radiology-prereview`.
- Reporting-guideline compliance and the submission map → `radiology-reporting`.
- Strengthening evidence (external validation, reader study) → `radiology-design` /
  `radiology-translation`.
- Verifying current journal scope / recent comparable papers → `radiology-search`.
- Cover letter / manuscript wording → `radiology-writing`.
- Journal tiering is strategy, not a prediction of acceptance.
