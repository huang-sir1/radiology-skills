---
name: radiology-prereview
description: "Run a rigorous pre-submission mock peer review of an imaging-AI / radiomics / radiogenomics manuscript — simulate the methods, statistics, reporting-guideline, figure, citation/claim-verification, and data-sharing reviewer a top journal would assign, and surface the issues that cause desk-reject or major revision before submission. Use when the user wants a mock review, pre-submission audit, \"投稿前预审/模拟审稿\", \"find the holes before a reviewer does\", a two-pass abstract/figure/table claim audit, or a readiness check. Returns a reviewer-style report with Blocker / Major / Minor issues, each tied to the manuscript location and the reporting-guideline or methodological risk, plus an editor-style recommendation and a prioritised fix order. Never fabricates compliance or papers over a real weakness."
---

# Pre-submission Mock Review

Use this skill to **be the harshest fair reviewer before the real one is**. It reads the
manuscript the way a methods-literate _Radiology_/Lancet-DH/Nature-Medicine reviewer would,
finds the dealbreakers, and returns a reviewer-style report you can act on — so issues are fixed
on your terms, not surfaced in a rejection.

## Core stance

- **Adversarial but on the author's side.** Hunt for the weakness a reviewer will weaponise, then
  hand back the fix — not just the criticism.
- **Dealbreakers first.** No patient-level split, data leakage, no external validation, undefined
  labels, unclear segmentation, incomplete statistics, overclaiming — these decide the outcome.
  Triage them before cosmetics.
- **Map to the guideline.** Tie each issue to the specific CLAIM/CLEAR/TRIPOD+AI/STARD/IBSI item
  or methodological risk a reviewer would cite (→ radiology-reporting).
- **Check the claims against the evidence.** Does the abstract/Discussion overstate AUC,
  correlation, or retrospective results? Flag every claim the data don't support.
- **Honest readiness verdict.** Give an editor-style recommendation (ready / minor / major / not
  yet) with the reasons — don't reassure.
- **Integrity.** Never invent compliance, never wave through a real weakness to be encouraging.

## When to use

- "Mock-review my paper before I submit." / "投稿前帮我模拟审稿、做预审。"
- "Find the holes a reviewer will find."
- "Is this ready for [target journal], or what must I fix first?"
- After drafting, before `radiology-journal` selection and submission.

## When to open extra files

| File | Open when |
|---|---|
| [references/review-dimensions.md](references/review-dimensions.md) | The full set of dimensions to review (design, data, labels, leakage, stats, reporting, figures, claims, sharing) |
| [references/dealbreakers.md](references/dealbreakers.md) | The hard issues that trigger desk-reject / major revision, with how to detect and fix each |
| [references/review-report-format.md](references/review-report-format.md) | The reviewer-report + editor-recommendation output structure |
| [references/pre-submission-hard-gates.md](references/pre-submission-hard-gates.md) | Final submission readiness audit, rejected-paper rescue, contribution map, reviewer objection register, or when deciding whether a paper is truly ready |
| [references/ai-radiogenomics-pitfall-audit.md](references/ai-radiogenomics-pitfall-audit.md) | Imaging-AI, foundation-model, VLM, radiomics, deep radiomics, or radiogenomics manuscripts need a targeted audit for leakage, external validation, site/scanner confounding, superficial XAI, weak clinical utility, or mechanism overclaim |
| [references/claim-verification-gate.md](references/claim-verification-gate.md) | Submission-facing abstract, Key Results, figure legend, table, graphical abstract, novelty, comparison, and numerical claims need two-pass extraction and verification |

## Workflow

1. **Intake** — manuscript (or sections), study type, target journal/tier if known.
2. **Classify** the study and load the dimensions (review-dimensions.md); pull the right
   guideline stack via `radiology-reporting`.
3. **For final readiness checks**, open `pre-submission-hard-gates.md` and score each hard
   gate as PASS / CONDITIONAL / FAIL before writing softer reviewer comments.
4. **Hunt dealbreakers** (dealbreakers.md) — partition hygiene, leakage, external validation,
   labels/reference standard, segmentation reproducibility, statistical completeness, overclaim,
   data/code availability.
5. **For AI/radiogenomics manuscripts**, open `ai-radiogenomics-pitfall-audit.md` and audit
   the common failures that make a high-AUC paper look untrustworthy.
6. **Review each dimension** — record `Issue | Severity (Blocker/Major/Minor) | Location |
   Guideline/risk | Fix`.
7. **Run two-pass claim audit for submission-facing text** — abstract, Key Results, figure
   legends, tables, graphical abstract, and Discussion comparison/novelty claims should be
   extracted first, then verified via `references/claim-verification-gate.md`.
8. **Check claims vs evidence** — abstract, Key Results, Discussion: is every claim bounded by the
   data?
9. **Write the report** (review-report-format.md) — reviewer comments by severity + an editor-style
   recommendation + a prioritised fix order (what unlocks the most).

## Output contract

1. **`Summary assessment`** — 3–5 sentences: what the paper does, its real strength, its decisive
   weakness, and the readiness verdict.
2. **`Major/Blocker comments`** — numbered, reviewer-style, each with location, the guideline/risk,
   and the concrete fix.
3. **`Minor comments`** — numbered, smaller issues.
4. **`Claims vs evidence`** — overclaims and the bounded rewording.
5. **`Claim audit status`** — for final readiness: extraction complete? verification complete?
   unsupported/numerical/visual-table claims remaining?
6. **`Hard-gate table`** — if final readiness is requested: contribution, data integrity,
   validation, statistics, reporting, figures, citation, ethics/data availability, and reviewer
   objection status.
7. **`Editor-style recommendation`** — ready / minor revision / major revision / not yet, with
   reasons.
8. **`Fix order`** — prioritised, routed to the relevant skill (stats, reporting, design, etc.).

## Quality bar

A good mock review predicts the real reviews: it catches the dealbreakers, cites the exact item a
reviewer would, separates fatal from cosmetic, and tells the author the order to fix things —
without inventing compliance or softening a genuine blocker.

## Handoffs

- Checklist item-by-item audit → `radiology-reporting`.
- Statistical completeness (CIs, calibration, DCA, multiplicity) → `radiology-stats`.
- Leakage specifics → `radiology-radiomics` / `radiology-deep-learning`.
- Missing external validation / reader study → `radiology-design` / `radiology-translation`.
- Data/code/ethics gaps → `radiology-data` / `radiology-ethics`.
- Rewriting overclaims / sections → `radiology-writing` / `radiology-polishing`.
- Then choose the venue → `radiology-journal`; reviewer replies later → `radiology-response`.
