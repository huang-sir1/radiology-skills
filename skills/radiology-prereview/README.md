# radiology-prereview

**Stage 5 — Submission & Translation.** A rigorous pre-submission mock peer review: be the
harshest fair reviewer before the real one is.

## What it does

- **Simulates the reviewer** a top imaging journal would assign — methods, statistics,
  reporting-guideline, figure, and data-sharing literate.
- **Hunts dealbreakers first** — leakage, no patient-level split, missing external validation,
  undefined labels, unclear segmentation, incomplete statistics, overclaiming, weak baseline,
  unavailable data/code, ethics inconsistency.
- **Reviewer-style report** — Blocker / Major / Minor comments, each with manuscript location,
  the guideline item or methodological risk, and the concrete fix.
- **Claims vs evidence** — flags every overstatement and gives the bounded rewording.
- **Editor-style recommendation** + a prioritised fix order routed to the producing skill.

## Trigger examples

- "投稿前帮我模拟审稿、做严格预审。"
- "Find the holes a reviewer will find before I submit."
- "Is this ready for [journal], or what must I fix first?"

## Reference files

| File | Use |
|---|---|
| `references/review-dimensions.md` | Every dimension to review + severity rubric |
| `references/dealbreakers.md` | The fatal issues, how to detect and fix each |
| `references/review-report-format.md` | Reviewer-report + editor-recommendation structure |

## Handoffs

`radiology-reporting` (checklist audit) · `radiology-stats` (statistical completeness) ·
`radiology-radiomics` / `radiology-deep-learning` (leakage) · `radiology-design` /
`radiology-translation` (missing validation/reader study) · `radiology-data` / `radiology-ethics`
(sharing) · `radiology-writing` / `radiology-polishing` (overclaims) · then `radiology-journal`
(venue) and later `radiology-response` (real reviews).

A rehearsal, not a guarantee of acceptance.
