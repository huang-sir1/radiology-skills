---
name: radiology-prereview
description: "Run author, peer or editorial scientific review with traceable findings; not checklists or upload audits. CN: 模拟审稿、预审、大修风险"
---

# Scientific Prereview and Journal Peer Review

Use this skill to **be the harshest fair reviewer before the real one is**, or to structure an
authorized confidential journal review. It reads the
manuscript the way a methods-literate _Radiology_/Lancet-DH/Nature-Medicine reviewer would,
finds the dealbreakers, and returns a reviewer-style report you can act on — so issues are fixed
on your terms, not surfaced in a rejection.

## Core stance

- **Adversarial but on the author's side.** Hunt for the weakness a reviewer will weaponise, then
  hand back the fix — not just the criticism.
- **Dealbreakers first.** Invalid independent-unit splits, data leakage, missing claim-required validation, undefined
  labels, unclear segmentation, incomplete statistics, overclaiming — these decide the outcome.
  Triage them before cosmetics. Apply each criterion to the study's actual design and claim;
  retrospective or single-center design alone does not establish invalidity.
- **Map to the guideline.** Tie each issue to the specific CLAIM/CLEAR/TRIPOD+AI/STARD/IBSI item
  or methodological risk a reviewer would cite (→ radiology-reporting).
- **Check the claims against the evidence.** Does the abstract/Discussion overstate AUC,
  correlation, or retrospective results? Flag every claim the data don't support.
- **Honest readiness verdict.** Give an editor-style recommendation (ready / minor / major / not
  yet) with the reasons — don't reassure.
- **Integrity.** Never invent compliance, never wave through a real weakness to be encouraging.
- **Mode before content.** `author-prereview`, `journal-peer-review`, `editorial-synthesis` and
  `thesis-prereview` share a scientific engine but have different audiences, confidentiality,
  conflicts, outputs and authority. Never leak editor-only material into author comments.

## When to use

- "Mock-review my paper before I submit." / "投稿前帮我模拟审稿、做预审。"
- "Find the holes a reviewer will find."
- "Is this ready for [target journal], or what must I fix first?"
- After drafting, before `radiology-journal` selection and submission.
- "I was invited to review this confidential manuscript; write comments to authors and editor."
- "Audit my dissertation chapter chain and defense claims before committee review."

For `mechanism-only`, use `radiology-radiogenomics: manuscript-review` as the scientific owner. For
`imaging-mechanism`, require its mechanism/bridge findings before synthesizing this imaging panel.
Do not impose scanner, AUC, reader-study or deployment criteria on a standalone transcriptomic study
unless its actual question and design activate them.

For `evidence-synthesis`, use `radiology-systematic-review` as the scientific owner and select
`evidence-synthesis-review`. Require frozen `protocol`, `search`, `selection-flow`, `extraction`,
`risk-of-bias-applicability`, `synthesis`, and `certainty` artifacts. Set the radiogenomics
`scientific_handoff_digest` to `not-applicable`; review the study-family/report/effect-row hierarchy,
dependence, pooling decision, certainty and synthesized claim ceiling instead of imposing a
primary-data or mechanism handoff.

## When to open extra files

| File | Open when |
|---|---|
| [references/review-dimensions.md](references/review-dimensions.md) | The full set of dimensions to review (design, data, labels, leakage, stats, reporting, figures, claims, sharing) |
| [references/review-modes-and-editorial-governance.md](references/review-modes-and-editorial-governance.md) | Always before a journal-review, editorial-synthesis or thesis-prereview route; also when author-side versus reviewer-side authority is ambiguous |
| [references/dealbreakers.md](references/dealbreakers.md) | The hard issues that trigger desk-reject / major revision, with how to detect and fix each |
| [references/review-report-format.md](references/review-report-format.md) | The reviewer-report + editor-recommendation output structure |
| [references/pre-submission-hard-gates.md](references/pre-submission-hard-gates.md) | Final submission readiness audit, rejected-paper rescue, contribution map, reviewer objection register, or when deciding whether a paper is truly ready |
| [references/ai-radiogenomics-pitfall-audit.md](references/ai-radiogenomics-pitfall-audit.md) | Imaging-AI, foundation-model, VLM, radiomics, deep radiomics, or radiogenomics manuscripts need a targeted audit for leakage, external validation, site/scanner confounding, superficial XAI, weak clinical utility, or mechanism overclaim |
| [references/multi-reviewer-panel.md](references/multi-reviewer-panel.md) | Full manuscripts, top-tier targets, conflicting strengths/risks, or when the user wants independent reviewer reports rather than one blended checklist |
| [references/scientific-prereview-receipt-contract.md](references/scientific-prereview-receipt-contract.md) | Final scientific prereview/re-review needs a canonical digest-bound receipt for response or submission handoff |
| [templates/evidence-synthesis-source-artifacts.template.json](templates/evidence-synthesis-source-artifacts.template.json) | `evidence-synthesis-review` needs the complete seven-role frozen artifact set before the generic prereview receipt is instantiated |
| [templates/prereview-governance-gates.template.json](templates/prereview-governance-gates.template.json) | Any final-readiness review needs separate human-subjects authorization and data/code-sharing gate receipts |

## Workflow

0. **Select the review mode and governance state** using
   `review-modes-and-editorial-governance.md`. In a real journal review, freeze the journal policy,
   confidentiality, COI/recusal, assistance and AI/tool authorization before processing content.
   Unknown external-processing permission is `STOP_CONFIDENTIALITY_UNRESOLVED`.
1. **Intake** — manuscript (or sections), study scope, source artifact/version/SHA-256, canonical
   project-state digest, modality-role digest, analysis-lock digest, claim-registry digest,
   scientific packet digest when present, study type, target journal/tier if known.
2. **Classify** the study and load the dimensions (review-dimensions.md); pull the right
   guideline stack via `radiology-reporting`.
   For `evidence-synthesis`, first consume the frozen review packet from
   `radiology-systematic-review`, then audit protocol deviations, search/selection completeness,
   extraction traceability, RoB/applicability, synthesis reproducibility and certainty.
3. **For final readiness checks**, open `pre-submission-hard-gates.md` and score each hard
   gate as PASS / CONDITIONAL / FAIL before writing softer reviewer comments. For any applicable
   human-subjects activity, consume a versioned `radiology-ethics: human-subjects` receipt whose
   approval, consent/waiver and data-use authorization fields are `DOCUMENT_VERIFIED`; bind its
   artifact path and SHA-256 in `templates/prereview-governance-gates.template.json`, then run
   `scripts/validate_prereview_governance_gates.py <receipt> --artifact-root <project-root>
   --require-ready`. Missing, author-reported, expired, conflicting or out-of-scope authority is an
   absolute `STOP`, never `CONDITIONAL`. Evaluate Data Availability and Code Availability in the
   separate sharing gate; a sharing statement cannot repair missing authorization and an ethics
   receipt does not prove that promised sharing is feasible. Any applicable authorization `STOP`
   forces `Not ready`; venue choice, lower-scope claims, declared risk or editor preference cannot
   override it.
4. **Hunt dealbreakers** (dealbreakers.md) — partition hygiene, leakage, external validation,
   labels/reference standard, segmentation reproducibility, statistical completeness, overclaim,
   data/code availability.
5. **For AI/radiogenomics manuscripts**, open `ai-radiogenomics-pitfall-audit.md` and audit
   the common failures that make a high-AUC paper look untrustworthy.
6. **Review each dimension** — give every decision-bearing issue a stable Finding ID and record
   `Finding ID | source artifact digest | evidence anchor | Severity (P0/P1/P2) | criterion |
   affected Claim IDs | source_review_state | minimum repair | closure evidence | residual boundary`.
   P0/P1 findings always set `required_for_pass=true`; only advisory P2 findings may be nonblocking.
7. **For full/high-impact review**, open `multi-reviewer-panel.md`. The default is a
   `lens-separated` panel: clinical, methods/statistics and imaging-AI/reproducibility reports are
   distinct, but they are not called independent when one agent/person shares context across them.
   Use the word `independent` only when reviewer contexts are isolated, all reviewers receive the
   same frozen fact base/source digests, no reviewer sees another report, and each report is frozen
   with its own output SHA-256 before editor synthesis. Do not invent reviewer identities.
8. **Run two-pass claim audit for submission-facing text** — abstract, Key Results, figure
   legends, tables, graphical abstract, and Discussion comparison/novelty claims should be
   extracted first, then verified via `radiology-citation/references/claim-verification-gate.md`.
9. **Check claims vs evidence** — abstract, Key Results, Discussion: is every claim bounded by the
   data?
10. **Write the report** (review-report-format.md) — reviewer comments by severity + an editor-style
   recommendation + a prioritised fix order (what unlocks the most). In `journal-peer-review`, keep
   comments to authors and confidential comments to editor separate; the recommendation is advisory
   and must not be presented as an official decision.
11. **Freeze the re-review yardstick** — preserve finding IDs, criteria, source digest, affected
     Claim IDs, immutable source-review state and closure evidence for `radiology-response` and later
     revision verification.
12. **Generate the canonical prereview receipt** — open
    `scientific-prereview-receipt-contract.md`, instantiate
    `templates/scientific-prereview-receipt.template.json`, bind every source artifact and upstream
    digest, then run `scripts/validate_scientific_prereview_receipt.py <receipt> --write-digest`.
    For `evidence-synthesis`, copy the seven rows from
    `templates/evidence-synthesis-source-artifacts.template.json` into `source_artifacts`; do not
    replace them with a manuscript-only row or a radiogenomics handoff.
    A global PASS cannot conceal a required `NOT_VERIFIED`/`PARTIAL`/`MADE_WORSE` finding or any
    unresolved placeholder.

## Output contract

1. **`Summary assessment`** — 3–5 sentences: what the paper does, its real strength, its decisive
   weakness, and the readiness verdict.
2. **`Review-mode governance receipt`** — mode, audience, frozen source/version, review policy,
   confidentiality, COI/recusal, assistance, AI/tool authorization and authority boundary.
3. **`Major/Blocker comments`** — numbered, reviewer-style, each with location, the guideline/risk,
   and the concrete fix.
4. **`Minor comments`** — numbered, smaller issues.
5. **`Claims vs evidence`** — overclaims and the bounded rewording.
6. **`Claim audit status`** — for final readiness: extraction complete? verification complete?
   unsupported/numerical/visual-table claims remaining?
7. **`Hard-gate table`** — if final readiness is requested: contribution, data integrity,
   validation, statistics, reporting, figures, citation, human-subjects authorization, data/code
   sharing, and reviewer-objection status. Keep authorization and sharing in separate rows.
8. **`Scientific prereview state`** — `SCIENTIFIC_PREREVIEW_PASS`,
   `SCIENTIFIC_PREREVIEW_CONDITIONAL`, or `SCIENTIFIC_PREREVIEW_FAIL`, with reasons. This is not the
   submission Skill's `READY*` namespace.
9. **`Canonical prereview receipt`** — validated receipt path, scope route, finding/artifact counts,
   project-state/modality-role/analysis/claim/handoff digests and
   `scientific_prereview_receipt_digest`; never present it as a scientific-truth or upload-readiness
   certificate.
10. **`Mode-specific output`** — author fix plan; or separate journal comments to authors and
    confidential comments to editor; or editorial agreement/disagreement synthesis; or thesis
    chapter/contribution/defense audit. Never mix audiences.
11. **`Cross-review synthesis`** — for panel mode: declare `lens-separated` or `independent`, report
   the isolation/freeze evidence when independent, then give consensus strengths, consensus
   blockers, weighting differences, broad-readership/clinical-importance read, and unresolved
   disagreement.
12. **`Fix order`** — prioritised, routed to the relevant skill (stats, reporting, design, etc.).
13. **`Frozen closure yardstick`** — source digest, stable finding IDs, criteria, affected Claim IDs
     and observable closure evidence for response/re-review.

## Quality bar

A good mock review predicts the real reviews: it catches the dealbreakers, cites the exact item a
reviewer would, separates fatal from cosmetic, and tells the author the order to fix things —
without inventing compliance or softening a genuine blocker.

## Handoffs

- Checklist item-by-item audit → `radiology-reporting`.
- Statistical completeness (CIs, calibration, DCA, multiplicity) → `radiology-stats`.
- Leakage specifics → `radiology-radiomics` / `radiology-deep-learning`.
- Missing external validation / reader study → `radiology-design` / `radiology-translation`.
- Human-subjects authorization gaps → `radiology-ethics: human-subjects`; they remain absolute STOP
  items until its document-verified receipt closes them.
- Data/code availability and repository/access implementation → `radiology-data`; keep this sharing
  gate separate from the authorization receipt.
- Integrity signal/evidence preservation, authorship/COI/AI disclosure or correction/retraction route
  → `radiology-research-integrity`; this skill never adjudicates misconduct or infers intent.
- Thesis architecture → `radiology-writing`; thesis-defense deck → `radiology-paper2ppt`; local degree
  and committee rules remain `LIVE_VERIFICATION_REQUIRED`.
- Rewriting overclaims / sections → `radiology-writing` / `radiology-polishing`.
- Tables and cross-display value defects → `radiology-table` / `radiology-pipeline`.
- Then choose the venue → `radiology-journal`; pass the validated prereview receipt digest to
  `radiology-submission`; reviewer replies later → `radiology-response`, which preserves the source
  digest and produces a fresh post-revision prereview receipt before assembly.
