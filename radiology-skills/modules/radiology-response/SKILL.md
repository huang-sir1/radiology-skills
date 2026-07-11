---
name: radiology-response
description: "Draft, audit, and revise point-by-point reviewer response letters for Radiology (RSNA) and imaging-journal revisions. Use when the user has reviewer comments / a major or minor revision / 审稿意见 to answer for an imaging-AI/radiomics/radiogenomics manuscript. Assigns each comment a stable ID, classifies it, maps it to a concrete manuscript action, and ties every claimed change to a specific location — without fabricating experiments, analyses, citations, line numbers, or results. Bilingual-aware (中文作者备注 → English response + Chinese confirmation items)."
---

# Reviewer Response Letters (imaging journals)

Treat the response letter as an **editor-facing verification document**: every reviewer
concern gets an ID, a classification, a concrete action, and a traceable manuscript location.

## Core stance
- **Completeness** — every comment gets an ID and a response, cross-reference, or an explicit
  unresolved flag. Nothing ignored.
- **Action mapping** — each reply maps to a concrete action: `ACCEPT_TEXT`, `ACCEPT_ANALYSIS`,
  `NEW_EXPERIMENT`, `ADD_RESULT`, `SOFTEN_CLAIM`, `CLARIFY`, `DISAGREE_WITH_REASON`,
  `AUTHOR_INPUT_NEEDED`.
- **Traceability** — every claimed change cites a section/page/line/figure/table/supplement,
  or a visible placeholder. No vague "we have revised accordingly."
- **Factuality** — never invent experiments, analyses, statistics, citations, line numbers,
  figure panels, editor instructions, or changes not actually made.
- **Tone** — cooperative, evidence-forward; disagree only with scientific/scope reasoning,
  never dismissively.
- **Imaging-aware** — common imaging-AI reviewer asks (external validation, leakage, calibration,
  reader study/MRMC, IBSI reproducibility, subgroup/fairness) routed to the right skill.

## When to use
- "Help me respond to these reviewer comments." / "Draft the rebuttal for this major revision."
- "Audit my draft response for completeness/tone/traceability."
- "审稿意见回复" for an imaging manuscript.

## When to open extra files
| File | Open when |
|---|---|
| [references/action-mapping.md](references/action-mapping.md) | Classifying comments and mapping each to a concrete action + manuscript location |
| [references/imaging-reviewer-playbook.md](references/imaging-reviewer-playbook.md) | Handling the recurring imaging-AI/radiomics asks (validation, leakage, calibration, MRMC, IBSI) and difficult cases |
| [references/response-audit-gate.md](references/response-audit-gate.md) | Final audit of a response letter, complex/conflicting reviewer comments, many analysis requests, or when traceability/factuality must be locked before resubmission |

## Workflow
1. **Intake** — split the decision letter into atomic comments; assign stable IDs
   (R1-1, R1-2, R2-1 …). Note the editor's overall ask.
2. **Classify** each (action-mapping.md): major/minor; analysis / clarification / claim /
   reference / presentation; feasible vs needs author input.
3. **Map to action + location** — what changes, where; if it needs a new analysis/experiment,
   route it (stats / reporting / figure) and mark `AUTHOR_INPUT_NEEDED` until done.
4. **Draft each response** — restate the comment, state the action, quote/point to the
   revised text + location; calibrate tone; disagree only with reasons.
5. **For final response packages**, open `response-audit-gate.md` and maintain the response
   ledger before calling the letter complete.
6. **Audit** — completeness (every comment answered), traceability (every claim located),
   factuality (no fabricated change), tone, and consistency across reviewers (conflicting
   asks reconciled).
7. **Output** the letter + an unresolved/author-input list.

## Output contract
1. **`Response letter`** — per comment: `ID | Reviewer comment (quoted) | Response | Action |
   Location`.
2. **`Summary of changes`** — short editor-facing overview.
3. **`Response audit`** — for final packages: every comment has an action, location, evidence
   artifact/status, and no unsupported claimed change.
4. **`Unresolved / author input needed`** — comments requiring data/decisions only the author
   can provide (e.g. "run external validation," "confirm patient-level split").
5. **`待确认（中文）`** — for Chinese authors, the items needing confirmation.

Never claim a change that was not made. If a requested analysis is not yet done, say so and
mark it pending rather than fabricating a result.

## Handoffs
New statistics (external validation, DeLong, calibration, MRMC) → `radiology-stats`;
checklist gaps a reviewer cited → `radiology-reporting`; new/edited prose → `radiology-writing`/
`radiology-polishing`; new figures → `radiology-figure`.
