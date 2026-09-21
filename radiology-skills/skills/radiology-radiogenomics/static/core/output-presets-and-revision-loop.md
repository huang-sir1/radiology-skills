# Output presets and targeted revision loop

Return the smallest auditable package that completes the request. Do not emit every possible artifact by default.
Every package must state the route, inspected-material boundary, claim-changing stop condition, and one viable
next move. Use `AUTHOR_INPUT_NEEDED` only for short factual gaps that materially change the decision or wording.

## Universal header

1. `Route and goal` — mode, task, stage, linkage, claim type, audience, and requested deliverable.
2. `Evidence boundary` — inspected artifacts, user-provided assertions, assumptions, missing inputs, and matched n.
3. `Decision summary` — highest defensible claim, global verdict when appropriate, and the decisive limitation.

## Preset A — audit

- Reconstructed contribution and genuine evidence-anchored strengths before defects; do not
  manufacture balance or give strengths a weakness severity.
- Severity-ranked findings using the constructive contract:
  `problem -> typed location -> scientific impact -> minimum repair -> optional stronger route ->
  cost/trade-off -> closure evidence`, with obligation and reviewer scope recorded separately.
- Gate/claim decisions with `PASS`, `CONDITIONAL`, `STOP`, evidence locations, and claim ceilings.
- Preserved valid work, exact repairs, completion criteria, and `AUTHOR_INPUT_NEEDED`.
- Reviewer-risk note and ready-to-use wording when writing was supplied.

## Preset B — mentoring or study design

- One-sentence question and mechanism/question tree.
- Resource and matched-cohort passport with feasibility blockers.
- Conservative, standard, and ambitious routes; recommend one using explicit trade-offs.
- Competing explanations, discriminating observations, negative controls, failure criteria, and immediate action.
- Learning note: why the recommendation wins and what evidence would change it.

Use the reusable [mentor decision memo](../../templates/mentor-decision-memo.md) when options,
trade-offs and the next executable action must be handed back to a learner or project team.

## Preset C — mechanism interpretation or bridge

- Start at the first observed object. For imaging-mechanism use `image/physical signal -> tissue structure ->
  cell source/state -> molecular program -> functional evidence -> clinical context`; for mechanism-only use
  `tissue/cell/molecular observation -> candidate process -> functional or perturbational evidence -> context`
  and omit nonexistent imaging links. Label every retained layer by evidence state, subtype, link status and scale.
- At least H1 and H2 biological explanations plus H3 technical/sampling/confounding explanation.
- Cross-scale claim-evidence ledger, discordance map, falsifiers, and minimum/standard/mechanism-advancing validation.
- Current claim ceiling and the shortest feasible upgrade test.

## Preset D — scientific writing

Mode overlay:

- `reviewer + writing-revision`: combine Preset D's scientific map with Preset A's typed locations,
  consequence, exact repair and closure criterion; do not expand the manuscript by default.
- `mentor + writing-revision`: combine Preset D with Preset B's principle, options/trade-offs,
  recommendation, next action and success/failure criterion.
- `combined + writing-revision`: use Preset E order, freeze valid claims/text, then apply Preset D only
  to affected nodes and return a change log.

- Writing entry point and `W-LEDGER-READY / W-REVISE / W-HANDOFF-READY / W-POLISH-READY /
  W-RETURN-TO-LEDGER` status, kept separate from
  claim verdict and finding severity.
- One-sentence bounded argument, claim-to-section map and evidence-placement decisions needed for
  the requested artifact.
- Ready-to-paste text for only the requested section when the source-bound scientific state permits it.
- Claim-evidence map, units and canonical terminology decisions used in the text.
- Material assumptions or missing evidence; never hide them under fluent prose.
- Methods reconstruct provenance and analysis; Results report effect, uncertainty and validation; legends define
  denominator and evidence state; Discussion gives alternatives, generalizability, boundaries, and next evidence.
- Cross-artifact check of counts, effects, evidence-state labels, claim verbs and decisive negative or
  discordant results; do not bury conclusion-changing evidence in supplementary material.
- Use outcome-prediction wording unless a valid treatment contrast and identification assumptions
  justify an average-effect claim; differential-benefit wording additionally requires interaction evidence.

## Preset E — combined review and redesign

Return in this order: `what remains valid -> blocked or conditional claims -> why -> minimum repair -> redesigned
standard route -> optional conservative and ambitious variants -> revised claim/writing`. Never hide a STOP inside
brainstorming.

## Preset F — revision verification

- Freeze the original issue IDs, severity, closure criteria, claim ceilings, and evidence boundary before reading the response narrative.
- Compare the original and revised manuscript/data/code against the frozen yardstick first; use the
  response narrative afterward to locate additional real evidence, never as proof by itself.
- For each issue report `author action | inspected new evidence | exact revised location | VERIFIED / PARTIAL / NOT ADDRESSED / MADE WORSE / NOT VERIFIABLE | residual risk`.
- Keep newly discovered issues separate from the frozen yardstick; they may change the current decision but must not retroactively change whether an original criterion was met.
- Finish with `changed | preserved | newly affected or blocked | checks rerun | author input needed`, plus the current `PASS / CONDITIONAL / STOP` verdict and claim ceiling.

Use the reusable [revision trace matrix](../../templates/revision-trace-matrix.md) to preserve the
response-blind initial state, final state, adjustment basis and criterion-level closure evidence.

## Targeted revision loop

When the user redirects a plan, audit, ledger, figure narrative, or manuscript:

1. Identify the exact claim, paragraph, table, figure, gate, or action ID being changed.
2. Lock accepted elements and keep them unchanged unless dependency analysis requires otherwise.
3. Trace downstream dependencies through terminology, cohort counts, mapping, statistics, claims, figures, and text.
4. Revise the smallest affected nodes; explain before making a structural change that alters the estimand or story.
5. Re-run only affected integrity gates, then run one cross-artifact consistency sweep.
6. Return `changed | preserved | newly affected or blocked | checks rerun | author input needed`.
7. If feedback reveals that the core question, independent unit, comparator, or evidence premise was wrong, return
   to the request passport and re-route instead of patching a broken premise.

Keep terminology and claim IDs stable across rounds. Never claim an analysis, experiment, validation, or manuscript
change was completed unless the corresponding artifact was actually inspected or produced.
