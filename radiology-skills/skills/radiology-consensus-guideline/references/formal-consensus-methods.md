# Formal consensus methods

Use this reference only when a consensus exercise is itself part of the method. Prespecify the route
before panel results are seen. ACCORD improves transparent reporting but does not select or validate
the method.

## Shared protocol fields

`purpose | scope/items and generation source | steering group | panel eligibility/recruitment and
representation | patient/public role | COI and recusal | sample-size rationale | pilot | method and
rounds | anonymity/interactions | scale | denominator | consensus/disagreement/stability thresholds |
feedback | missing/attrition | item modification/addition/deletion | stopping | dissent | analysis |
ethics/data governance | registration/version | reporting`.

There is no universal 70%, 75% or 80% threshold. Choose and justify the threshold, denominator,
number of rounds, stability and disagreement rules before results. Report every denominator,
attrition and post-protocol change.

## 1. Delphi

Use when geographically or professionally distributed participants should iteratively reconsider
judgments with controlled feedback and relative anonymity.

- Preserve anonymity level: anonymous to peers, steering group or neither.
- Predefine item source, rating scale, consensus and disagreement, feedback statistics/text, round
  count, stopping and whether accepted items are re-rated.
- Report invited/eligible/participating/completing counts per round and how panel composition changes.
- Do not treat attrition as agreement or feed only favorable comments back to the panel.
- Separate agreement at one round from stability across rounds. Preserve `STABLE_DISAGREEMENT`.

## 2. RAND/UCLA Appropriateness Method

Use for scenario-specific appropriateness when best available evidence must be combined with a
structured expert panel. Follow the actual manual/current adaptation rather than calling any
two-round survey “RAND/UCLA.”

- Build explicit, mutually interpretable clinical scenarios and evidence summaries.
- Preserve first-round individual ratings, structured discussion, second-round ratings, median and
  the selected disagreement rule.
- Appropriate, uncertain and inappropriate are method-defined categories, not benefit/harm effect
  estimates or legal standards.
- For imaging, specify clinical variant, modality/protocol, patient factors, contraindications,
  alternatives, availability and downstream management.

## 3. Nominal group technique

Use for structured generation, clarification, prioritization and ranking in an interactive group.

- Predefine independent idea generation, round-robin sharing, clarification/discussion, ranking and
  aggregation.
- NGT is not anonymous deliberation; document facilitation, dominance safeguards and dissent.
- Do not relabel an ordinary meeting, show of hands or chair decision as NGT.

## 4. Informal consensus

Informal deliberation may be appropriate for some committee decisions but must be labelled. Record
participants, evidence considered, assumptions, decision process, dissent and chair role. When no
consensus is reached, document why and use wording/status that reflects uncertainty.

## Stop gates

Return `CONSENSUS_METHOD_INVALID` when thresholds were chosen after results; panel eligibility or
COI is undisclosed; affected stakeholders were systematically excluded; voting items changed without
a versioned amendment; denominators/attrition are missing; disagreement was removed; or expert vote
is presented as empirical evidence. Preserve the exercise as exploratory where possible; do not
retroactively call it a valid Delphi, RAND/UCLA or NGT.

