# Grant review modes and criterion findings

Select one primary mode. A more intensive mode does not grant permission to rewrite the applicant's
files or to invent missing call rules.

## Mode router

### `triage/targeted`

Use for one section, one aim, a short concept note or a rapid fatal-flaw screen. State the exact
scope and do not imply whole-proposal clearance. Check:

1. whether the call is identified enough for the requested question;
2. one proposal-spine inconsistency that would make polishing wasteful;
3. the requested criterion/section;
4. obvious radiology inference breakers;
5. the next minimum artifact needed.

Output at most the material findings plus a `not assessed` list.

### `full audit`

Use only when the call passport and a substantially complete application are available. Run the
administrative gate, proposal-spine audit, every applicable funder criterion, radiology feasibility,
aim/milestone/risk/budget alignment and readiness boundary. Missing sections receive
`NOT_ASSESSABLE`; they are not reconstructed from context.

### `mock panel`

Use when the user asks for simulated review, pre-panel challenge or competitive positioning. Use
`lens-separated` passes by default; reserve `independent` for demonstrably isolated reviewers:

- **Seat A — scientific value/premise/innovation**;
- **Seat B — imaging methods, measurement, data and statistics**;
- **Seat C — clinical significance, feasibility, team/environment and execution**.

For independent mode, each seat must have an isolated context, receive the same frozen proposal
version and call passport, see no other report, and freeze its output before synthesis. Record the
input/output digests and isolation evidence. Multiple roles in one shared context remain
`lens-separated`. The chair maps findings to funder criteria, groups duplicates, preserves minority
concerns and states that the simulation is `NOT_CALIBRATED`. Do not impersonate real named reviewers,
predict a percentile or claim that a simulated score equals the funder's outcome.

### `revision/resubmission`

Require prior critiques and the revised application (or an explicit revision plan). Build a matrix:

| Critique | Criterion | Author response/decision | Proposal change + locator | Evidence | Status | Residual risk |
|---|---|---|---|---|---|---|

Classify `RESOLVED`, `PARTIAL`, `UNRESOLVED`, `DISAGREED_WITH_RATIONALE`, or `NOT_VERIFIABLE`.
Re-run every criterion affected by a change; revising an aim can stale sample size, budget,
milestones, ethics, acquisition and downstream sections. Do not reward polite rebuttal language when
the proposal itself remains unchanged.

## Criterion finding contract

Write one finding per decision-relevant issue:

```text
Finding ID:
Priority: P0 / P1 / P2 / P3
Funder criterion:
Verdict: PASS / CONDITIONAL / FAIL / NOT_ASSESSABLE
Proposal evidence anchor: [section/page/table/quoted short span]
External evidence anchor and state: [if applicable]
Finding: [observation, not a generic preference]
Why it changes review: [compliance, inference, competitiveness or clarity]
Smallest valid repair:
Owner / dependency:
Residual uncertainty:
```

No anchor means an unanswered review question, not a negative fact. Distinguish:

- **evidence** — what the proposal/source directly shows;
- **inference** — what follows with stated assumptions;
- **recommendation** — an author decision, not an automatic edit.

## Priority and verdict

- `P0`: acceptance-critical, integrity/ethics/security or prohibited-practice defect.
- `P1`: invalidates the central inference or makes a key aim infeasible.
- `P2`: material competitive weakness but the project remains interpretable.
- `P3`: clarity, compression, navigation or presentation improvement.

Use `PASS` only for an actually inspected criterion, not silence. `CONDITIONAL` names the missing
evidence/decision. `FAIL` states the exact broken rule or inference. `NOT_ASSESSABLE` is correct when
the necessary material is absent.

## Funder-criterion routing

### NSFC

Keep administrative acceptance separate. For scientific review, use the revised regulation's
dimensions: scientific value, innovation, social impact and feasibility; also examine relevant
research experience, reasonable funding-use plan, other support/overlap, prior implementation and
continued need. Bind research attribute, programme and any special direction to the live passport.
Do not invent numeric weights or demand obsolete headings.

### NIH covered RPG mechanisms

Use the current simplified factors only after confirming applicability:

- Factor 1 Importance (Significance + Innovation), 1–9;
- Factor 2 Rigor and Feasibility (Approach), 1–9;
- Factor 3 Expertise and Resources, sufficiency/gaps;
- overall impact plus applicable additional review criteria/considerations.

Report the scale only when the user requests a score and the live NOFO supports it. A simulated
number remains `NOT_CALIBRATED`; categorical findings should carry the reasoning.

### Other funders

Extract exact criteria and scoring/decision rules from the current official call. Build a crosswalk
from proposal functions to those criteria. If the call uses excellence, impact, implementation,
career trajectory, team science or stakeholder engagement differently, preserve that distinction.
Never average incompatible criteria across funders or claim one proposal is compliant everywhere.

## Synthesis rules

1. P0 and P1 findings precede strengths and stylistic edits.
2. Do not cancel a fatal weakness by counting unrelated strengths.
3. Keep criterion-level uncertainty and panel disagreement visible.
4. Separate `current proposal state` from `repair potential`.
5. End with the strongest supportable readiness state, not “fundable/unfundable.”
