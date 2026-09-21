---
name: radiology-consensus-guideline
description: "Design/audit consensus and evidence-to-recommendation products; not review synthesis or endorsement."
---

# Radiology Consensus and Guideline Development

Use this skill to design, run-plan or audit a consensus statement, appropriateness project,
practice parameter, technical standard or clinical practice guideline. It owns the panel/process,
evidence-to-decision record, consensus protocol, recommendation ledger and lifecycle plan. It does
not perform the underlying systematic review, confer society endorsement, set a legal standard of
care or let expert voting substitute for evidence.

## Choose the product and mode

First declare the product: `clinical-practice-guideline`, `appropriateness-criteria`,
`practice-parameter`, `technical-standard`, `expert-consensus-statement` or
`research-priority/definition-consensus`. Do not use these labels interchangeably.

| Mode | Use when | Required result |
|---|---|---|
| `scoping` | product, users, questions or authority are unsettled | scope, product decision, stakeholders, evidence needs and stop conditions |
| `protocol` | a versioned development plan is needed before evidence/panel decisions | panel, COI, evidence, consensus, consultation and update protocol |
| `evidence-to-decision` | a frozen evidence synthesis must become recommendation judgments | GRADE/compatible EtD ledger with explicit uncertainty |
| `formal-consensus` | Delphi, RAND/UCLA or nominal group work is planned or audited | prespecified rounds, thresholds, denominator, feedback, dissent and reporting record |
| `audit-update-retire` | an existing statement/guideline is reviewed for trustworthiness or currency | method audit, surveillance result, update/retirement and supersession map |

Read [references/evidence-to-recommendation.md](references/evidence-to-recommendation.md) for the
systematic-review handoff, GRADE/EtD and recommendation wording. Read
[references/formal-consensus-methods.md](references/formal-consensus-methods.md) only for a formal
consensus exercise. Read
[references/radiology-guidance-lifecycle.md](references/radiology-guidance-lifecycle.md) for
appropriateness criteria, practice parameters, technical standards, implementation, updating and
retirement. Verify methods and authority through
[references/source-registry.md](references/source-registry.md).

## Input passport

Record:

`product and mode | sponsor/developer and actual adoption authority | jurisdiction/organization |
scope, population, modality/test/intervention/comparator/outcomes/setting | intended users and
affected people | panel roles, patient/public members and COI records | frozen systematic-review
handoff/version/currency | certainty framework | consensus method and prespecified rule | draft and
consultation artifacts | implementation context | publication/update/retirement owner | user
authority for edits or external communication`.

Missing adoption authority, panel decisions, COI management, patient/public participation, evidence
certainty or official status remains `NOT_VERIFIED`. Advisory drafting is not an endorsed guideline.

Choose the evidence lane for the declared product. A clinical recommendation presented as
evidence-based requires the relevant systematic-review/EtD handoff. A research-priority or
definition-consensus exercise instead requires transparent item generation, search/mapping or
stakeholder evidence, panel judgments and limits; use `NOT_APPLICABLE_GRADE` when it makes no
clinical-effect or recommendation-strength claim. A generic Delphi protocol does not require an
invented effect synthesis or GRADE rating.

## Core evidence and recommendation states

- Evidence handoff: `EVIDENCE_READY`, `EVIDENCE_PARTIAL`, `EVIDENCE_ABSENT` or `EVIDENCE_STALE`.
- Recommendation: `DRAFT`, `CONDITIONAL`, `STRONG`, `NO_RECOMMENDATION`, `RESEARCH_ONLY`,
  `SUPERSEDED` or `RETIRED` only when defined by the selected framework and authorized process.
- Consensus result: `CONSENSUS_REACHED`, `CONSENSUS_NOT_REACHED`, `STABLE_DISAGREEMENT`,
  `ATTRITION_LIMITED` or `NOT_ASSESSABLE`.

Evidence certainty, recommendation strength and consensus percentage are different fields. A high
vote does not upgrade low/absent evidence, and a low-certainty body does not automatically prohibit a
strong recommendation when a transparent framework supports an exceptional case.

## Required workflow

1. **Lock the product and authority.** Define who will use the output, for which decision, and who
   can officially adopt/endorse it. Use “draft” or “advisory” until a verified process confers status.
2. **Scope the decision.** Specify population, imaging scenario, modality/test, comparator,
   downstream action, patient-important outcomes, setting, exclusions and equity/access questions.
3. **Constitute the panel.** Include relevant clinical disciplines, radiologists, referrers,
   technologists/medical physicists when technical decisions are material, methodologists,
   implementers and patients/public or other affected representatives. Record balance, recruitment,
   roles, COI assessment, management and recusals.
4. **Accept the product-appropriate evidence handoff.** For an evidence-based clinical
   recommendation, require search currency, study-family/effect-row identity, risk-of-bias/
   applicability, synthesis and certainty from `radiology-systematic-review`. For priorities or
   definitions, record item sources, mapping/search limits, stakeholder input and traceable revision;
   a full effect review is required only if the intended claim needs it. Do not relabel selected
   references or panel memory as a systematic review.
5. **Run the applicable decision process.** For clinical recommendations, record benefits/harms,
   certainty, values/preferences, resources, equity, acceptability and feasibility. Link diagnostic
   accuracy to downstream management and patient outcomes. For priorities or definitions, report
   explicit selection criteria, content/semantic judgments and dissent without inventing clinical
   effects, GRADE certainty or recommendation strength.
6. **Use formal consensus only for its declared purpose.** Prespecify method, panel, rounds,
   anonymity/interactions, feedback, denominator, threshold, stability, attrition, tie/disagreement
   handling and stopping. Use
   [templates/consensus-guideline-protocol.md](templates/consensus-guideline-protocol.md).
7. **Draft atomic recommendations or consensus items.** Each clinical recommendation states population/scenario, action,
   comparator/conditions, strength, certainty, rationale, harms/burden, implementation conditions,
   exceptions, dissent and research gaps. Use
   [templates/recommendation-etd-ledger.md](templates/recommendation-etd-ledger.md).
   For priorities/definitions, use the item register and formal-consensus result sections instead;
   include wording, provenance, scope, rationale and status, with clinical EtD fields not applicable.
8. **Consult and quality-control.** Preserve stakeholder comments, responses, panel changes,
   unresolved disagreement and external review. Reporting-checklist completion does not prove
   method quality or endorsement.
9. **Plan implementation and lifecycle.** Define dissemination, feasibility tools, monitoring,
   surveillance, update triggers, versioning, supersession and retirement. Imaging technology,
   contrast/tracers, dose, reconstruction, AI versions and clinical standards can make guidance stale.

## Stop and escalation gates

Return `GUIDANCE_STOP_AND_REFRAME` when product or adoption authority is misrepresented; scope or
decision scenarios are undefined; the evidence packet is missing/stale for a claim presented as
evidence-based; material panel COI cannot be managed; affected patients/public or essential
disciplines are systematically excluded without justification; consensus thresholds are chosen after
results; attrition, dissent or denominator is hidden; expert votes are used to manufacture evidence;
or a current clinical recommendation could expose patients to unreviewed harm.

Escalate formal endorsement, legal/regulatory interpretation and individual patient decisions to the
responsible society, institution, regulator or clinical team. The skill may prepare evidence and
drafts but cannot adopt, endorse or implement official guidance.

## Output contract

1. `Product, scope and authority passport`
2. `Panel/stakeholder/patient-public and COI matrix`
3. `Product-appropriate evidence handoff and currency verdict` — systematic review for the clinical
   evidence claim, or item-generation/mapping/stakeholder evidence for priorities and definitions
4. `Question/outcome and imaging-scenario map`
5. `GRADE or compatible evidence-to-decision ledger` when applicable; otherwise
   `NOT_APPLICABLE_GRADE` plus the item-selection/definition rationale
6. `Consensus protocol and result` — rounds, thresholds, denominator, attrition and dissent
7. `Recommendation or consensus-item ledger` — strength, certainty and consensus kept separate;
   clinical strength/certainty is not invented for a terminology or research-priority item
8. `Implementation, equity, monitoring and research-gap plan`
9. `Consultation, external-review and change-response record`
10. `Version, update, supersession and retirement plan with exact non-endorsement boundary`

## Handoffs and non-ownership

- Search, screening, extraction, risk of bias, synthesis and evidence certainty ->
  `radiology-systematic-review`; current clinical facts -> `radiology-clinical-domain`.
- Quantitative Delphi/RAND agreement or comparative inference -> `radiology-stats`; CEA/CUA,
  budget impact, ICER/QALY, PSA/VOI and economic-model evidence consumed by an EtD ->
  `radiology-health-economics`. This skill weighs the supplied economic evidence in a recommendation;
  it does not build or authorize the economic model.
- Reporting guideline/quality checklist -> `radiology-reporting`; prose, tables, figures and decks
  -> their artifact owners.
- Society boards, institutions, regulators and clinical teams retain endorsement, adoption,
  implementation, legal and patient-care authority.
