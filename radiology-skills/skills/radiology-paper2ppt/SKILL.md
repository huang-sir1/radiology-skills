---
name: radiology-paper2ppt
description: "Plan/create/audit evidence-led research decks for defenses, meetings and talks, with render QA. CN: PPT、答辩、组会汇报"
---

# Radiology Research Presentation

Turn frozen research content into an audience-specific scientific presentation. Own both a
content-planning route and, when requested, a real presentation-artifact route; never imply that a
slide outline is a `.pptx` or that a successfully rendered deck validates the science.

## When to use

- "Turn my paper/grant into a defense, conference or lab-meeting deck." /
  "帮我把论文或标书做成答辩、会议或组会 PPT。"
- "Audit my research deck before I present." / "这份科研 PPT 上台前帮我审一遍。"
- "How do I structure a 10-minute research talk?" / audience, decision and timing before slides.

## Scope and boundaries

Use for proposal-defense, lab-meeting, conference, journal-club, project-review,
thesis/defense, and results decks in radiology or imaging research, including creation, editing,
slide planning, speaker notes, and deck audits.

- Review or rewrite a grant/proposal's scientific content with `radiology-grant`. This skill may
  receive a frozen grant handoff and turn it into a defense or pitch deck; it must not silently
  repair aims, methods, feasibility, or budget claims while making slides.
- Use `radiology-reader`, `pdf`, or the relevant research owner to extract or adjudicate source
  content. Do not treat a screenshot or slide as the scientific source of record when the underlying
  paper, data, protocol, or decision record is available.
- Use `radiology-figure` or `radiology-table` for a standalone publication visual/table; this skill
  owns only its audience-specific slide transformation. Manuscript drafting/polishing, prereview, and
  submission packaging remain with `radiology-writing`/`radiology-polishing`, `radiology-prereview`,
  and `radiology-submission`.
- Journal club and own-study decks share this presentation owner but use different routes: journal
  club appraises source authors' evidence; proposal, lab, conference, project, defense, and results
  routes present frozen project evidence. Clinical-pathway and acquisition/reconstruction questions
  remain with `radiology-clinical-domain` and `radiology-acquisition-qc` before slide authoring.
- Use the available presentation skill/tool only for actual PowerPoint or Google Slides work.
  Content planning alone does not require a presentation runtime.
- Do not use a presentation display for individual-patient diagnosis or management.

## Intake contract

Infer what is already clear; ask only for consequential missing information:

1. **Deck job and audience** — what should this audience understand, decide, approve, challenge,
   or do?
2. **Delivery contract** — duration, Q&A, venue/screen or remote format, language, deadline, and
   required slide/template rules.
3. **Evidence state** — planned, exploratory, interim, frozen analysis, published, or mixed; identify
   confidential/unpublished content and any embargo.
4. **Artifact scope** — content plan only, new deck, edit/repair an existing deck, or audit only.
5. **Source authority** — frozen grant/protocol, analysis receipt, manuscript, paper, figures/tables,
   existing deck, branding/template, and permission or license state.
6. **Fidelity contract** — choose an artifact fidelity class and an evidence fidelity class. State
   whether the requested deliverable must remain natively editable and which slides carry decisive
   scientific evidence rather than illustration or exploratory storyboarding.

State the communication job in one sentence: `By the end, [audience] should [outcome] because
[central takeaway or decision basis].` If the talk is exploratory, use the question or decision the
audience should help resolve rather than inventing a persuasive conclusion.

## Route before writing slides

Read [scientific-deck-routing.md](references/scientific-deck-routing.md) and select exactly one
primary deck job. A mixed deck may borrow secondary modules, but one job controls the opening,
evidence order, close, and cut priorities.

Then load only what is needed:

| Need | Read |
|---|---|
| Narrative, assertion-evidence titles, evidence maturity, uncertainty, notes, or timing | [claim-evidence-and-narrative.md](references/claim-evidence-and-narrative.md) |
| Transform figures/tables, show radiology images, de-identify, cite assets, or make visuals accessible | [visual-evidence-and-radiology-images.md](references/visual-evidence-and-radiology-images.md) |
| Create/edit a deck, follow a template, render, inspect, repair, or audit a `.pptx` | [deck-quality-qa.md](references/deck-quality-qa.md) |

Use [deck-brief.md](templates/deck-brief.md) for a new or substantially reworked presentation and
[slide-map-and-source-ledger.md](templates/slide-map-and-source-ledger.md) before artifact authoring.

## Invariants

- **One slide, one narrative job.** Use a message title that the visible evidence can support. A
  planned experiment, question, or unresolved result needs a question/status title, not a result claim.
- **Claim follows evidence maturity.** Keep `SOURCE_OBSERVED`, `ANALYSIS_DERIVED`,
  `INTERPRETATION`, `RECOMMENDATION`, and `PROPOSED` distinct. Preliminary or adapted evidence
  cannot be promoted to confirmed, generalizable, causal, clinically useful, or deployment-ready.
- **Visible evidence and spoken claim agree.** Axes, units, denominator, uncertainty, cohort, time
  point, reference standard, and comparison must survive figure/table transformation.
- **Images remain evidence.** Preserve modality/sequence or view, orientation/laterality, frame or
  slice context, window/level intent, scale, panel labels, annotations, and relevant acquisition or
  reconstruction context. Record every crop, redraw, enhancement, or composite.
- **Evidence-critical content remains inspectable.** Decisive numbers, tables, equations, citations,
  and data-dependent graphics use native editable text/tables/vectors or an accurate, source-linked
  crop. A generated image or text-to-image rendering is never an evidence carrier.
- **Unknowns remain visible.** Use visible `MISSING — ...` or `UNVERIFIED — ...` placeholders until
  resolved. Do not silently fill, visually hide, or move an unresolved evidence dependency only to
  speaker notes.
- **Privacy and rights are gates.** Inspect both metadata and pixels for identifiers; verify permission
  or license state. A citation is not permission.
- **Notes carry delivery support, not hidden certainty.** Put talk track, transition, timing, caveats,
  anticipated questions, and `[Sources]` blocks in speaker notes; never add an unsupported stronger
  conclusion only in notes.
- **A deck is not its validation.** Artifact QA, scientific QA, accessibility QA, and timed rehearsal
  are separate receipts.

## Workflow

1. Freeze the source set, evidence state, audience decision, exclusions, and artifact/evidence
   fidelity classes in the deck brief.
2. Select the primary deck route and allocate section time, including Q&A and a cut path.
3. Build the slide map first: message title, claim state, evidence, visual, source, caveat, notes,
   timing, and keep/cut/backup status. Resolve unsupported titles before layout work.
4. Transform only decision-relevant figures/tables/images; populate the source and transformation
   ledger. Label author-recreated or adapted visuals explicitly.
5. If the user requested content planning only, deliver the brief, slide map, visual plan, and QA plan.
   Do not invoke artifact creation or report a `.pptx`.
6. If the user requested an artifact, follow the creation/edit/template route in
   `deck-quality-qa.md` and the active presentation skill. Preserve supplied templates and existing
   deck hierarchy where applicable.
7. Render every final slide, inspect the contact sheet and each slide at full size, fix all unintended
   overlap/clipping/wrapping, then run scientific, accessibility, package, and rehearsal checks.
8. For an editable PPTX delivery, reopen the final package and run the parity/round-trip checks in
   `deck-quality-qa.md`; compare the reopened artifact and its fresh render/export with the approved
   slide map and inspected render.
9. Report what was actually verified and any unresolved source, permission, runtime, display,
   parity, or rehearsal limitation.

## Output contract

Return only the artifacts requested, while preserving these receipts:

1. **Deck brief** — communication job, audience, route, evidence state, artifact/evidence fidelity
   classes, duration, constraints, and claim ceiling.
2. **Slide map** — slide/scene, upstream Claim ID, message, evidence, visual, claim state, caveat,
   timing, and cut status.
3. **Source and transformation ledger** — claim/asset to authoritative source, locator, license or
   permission state, and every material transformation.
4. **Speaker notes plan** — talk track, transition, caveat, timing, anticipated questions, and sources.
5. **Presentation artifact**, only when requested and actually created or edited.
6. **QA receipt** — scientific consistency, privacy/rights, accessibility, render/layout, editable
   PPTX parity/round-trip, package, and rehearsal status reported separately as `PASS`,
   `CONDITIONAL`, `STOP`, or `NOT_RUN`.

Use `STOP` rather than polishing around missing decisive evidence, unresolved patient identifiers,
unknown reuse rights for a required public asset, a title contradicted by its visual, or a corrupt
artifact. Use `CONDITIONAL` for visible, bounded limitations that do not invalidate the deck's job.

## Handoffs

- Frozen proposal/grant content: `radiology-grant` -> this skill.
- Source extraction or paper appraisal: `radiology-reader`, `pdf`, `radiology-reporting`, or the
  relevant scientific owner -> this skill.
- Actual presentation artifact: this skill's deck brief + slide/source ledger -> active presentation
  skill/tool; return the render/package receipt here.
- Statistical or clinical inference conflict: return to `radiology-stats`, `radiology-method-evaluation`,
  `radiology-clinical-domain`, or `radiology-translation`; do not resolve it through slide wording.
