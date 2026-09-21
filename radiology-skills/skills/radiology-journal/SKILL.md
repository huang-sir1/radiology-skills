---
name: radiology-journal
description: "Match a near-finished imaging paper to live journal scope and tier; not scientific review or file audit."
---

# Journal Selection & Submission Tiering

Use this skill when the paper is essentially written and the question is **where to send it**.
It reads the manuscript's real strengths and weaknesses, grades it on the dimensions imaging
venues actually weigh, and returns an honest **reach / target / safety** ladder — not a wish
list ranked by impact factor.

## Core stance

- **Fit beats prestige.** The best journal is the one whose published pattern matches this
  paper's design and evidence — not the highest impact factor it might survive.
- **Grade the actual study type.** Evaluate whether validation, design, precision, clinical or
  biological evidence and novelty support this manuscript's claims; mark irrelevant dimensions
  not-applicable. No single design feature supplies a universal venue cutoff.
- **Name the decisive weakness.** Explain its effect on inference or venue fit using source
  evidence; single-center or retrospective design alone is not a fatal verdict.
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
| [references/venue-style-profiles.md](references/venue-style-profiles.md) | The user supplies author-guide PDFs/classic articles, asks for journal "taste," or the target is European Radiology / Nature Partner / npj and style/logistics must match the parsed guide profile |

## Workflow

1. **Extract the paper profile** — type (DTA / prediction / radiomics / radiogenomics / reader /
   segmentation), core selling point, and the single biggest weakness.
2. **Grade it** (fit-grading.md) on: external validation, prospectivity, reader/utility evidence,
   calibration, sample size, centers, novelty and reporting compliance where applicable to the study.
3. **Map to venues** (venue-patterns.md) — which tiers the grade realistically reaches; reject
   obvious mismatches with the reason.
4. **Apply venue style profile when available** (venue-style-profiles.md) — article shape,
   house taste, required compliance artifacts, and visual/writing constraints from supplied
   guides or classic papers.
5. **Verify current scope and guide** — hand each shortlisted venue to `radiology-search` to
   confirm it still publishes this kind of work and recently has; record official guide source,
   article type, update/access date, and portal-specific requirements.
6. **Build the ladder** — reach / target / safety, each with match reason, risk, turnaround
   consideration, and the one thing to strengthen to climb.
7. **Logistics** (submission-logistics.md) — article type, limits, cover-letter angle, suggested
   reviewers, and any transfer cascade.

## Output contract

1. **`Paper profile`** — type, core selling point, biggest weakness, reporting-guideline fit.
2. **`Fit grade`** — scored on the tier-deciding dimensions, with the limiting factor named.
3. **`Submission ladder`** — **Reach / Target / Safety**, each: venue (pattern-matched + to be
   verified live), match reason, risk, what to strengthen to move up.
4. **`Strengthen-first`** — the highest-leverage improvements to raise the tier (→ relevant skill).
5. **`Verify now`** — the live-scope checks to run before submitting (→ radiology-search).
6. **`Venue style`** — if a guide/profile is available: article shape, voice, figure/table
   taste, and compliance artifacts to satisfy before submission.
7. **`Guide provenance`** — official source, article type, guide version/update/access date,
   verified limits, and unresolved portal fields.
8. **`Logistics`** — article type, limits, cover-letter angle, suggested reviewers.

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
- Cover letter and journal package → `radiology-submission`; manuscript wording → `radiology-writing`.
- Upload-ready package and manifest → `radiology-submission`; project gate state →
  `radiology-pipeline`.
- Journal tiering is strategy, not a prediction of acceptance.
