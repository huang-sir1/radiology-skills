# radiology-response

**Point-by-point reviewer response letters for imaging journals** — treats the letter as an
editor-facing verification document. Every comment gets an ID, a classification, a concrete
action, and a traceable location.

## What it does
- Splits the decision letter into atomic, stably-numbered comments.
- Maps each to an action (`ACCEPT_TEXT`, `ACCEPT_ANALYSIS`, `NEW_EXPERIMENT`, `SOFTEN_CLAIM`,
  `DISAGREE_WITH_REASON`, `AUTHOR_INPUT_NEEDED`, …) and a manuscript location.
- Routes the recurring imaging-AI asks (external validation, leakage, calibration, MRMC
  reader study, IBSI reproducibility, fairness) to the right skill.
- Audits completeness, traceability, factuality, tone, and cross-reviewer consistency.

## Reference files
```
references/
├── action-mapping.md               comment classification → action + location
└── imaging-reviewer-playbook.md     recurring imaging-AI/radiomics asks + difficult cases
```

## Example prompts
- "Draft a point-by-point response to this major revision (comments pasted)."
- "Audit my rebuttal for tone and traceability."
- "两位审稿人意见冲突，怎么回复？"

## Integrity
Never invents experiments, analyses, citations, line numbers, or changes. Marks
not-yet-done work as pending. Hands new analyses to `radiology-stats` and new prose to
`radiology-writing`.
