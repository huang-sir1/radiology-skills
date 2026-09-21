---
name: radiology-health-economics
description: "Plan/audit imaging economic evaluation, decision models, budget impact, uncertainty and HTA reporting."
---

# Radiology Health Economics

Use this skill when a radiology technology, diagnostic strategy, imaging pathway or AI-supported
workflow must be compared in terms of both costs and consequences for a named decision maker. Its
unique responsibility is the economic decision problem, economic model and uncertainty—not the
clinical-effect estimate, grant budget, prediction-model utility analysis or reimbursement decision.

## Non-negotiable boundaries

- Lock the jurisdiction, decision maker and current reference case before claiming HTA or
  reimbursement relevance. If unresolved, provide only a generic scientific design and emit
  `STOP_REFERENCE_CASE_UNRESOLVED`.
- Perspective, population, comparator, time horizon, cost year/currency and outcome are structural
  inputs, not editorial details. Do not invent them or borrow a threshold from another jurisdiction.
- Diagnostic accuracy, AUC, sensitivity, specificity and decision-curve net benefit are intermediate
  or model-performance quantities. They are not QALYs, monetary net benefit or an economic evaluation.
- An imaging test usually affects health through downstream decisions, treatment, monitoring,
  false-positive/false-negative consequences, nondiagnostic examinations and incidental findings.
  Do not assign final health benefit directly to accuracy without a defensible pathway.
- A grant budget asks what a project costs to conduct; a budget impact analysis asks how adopting a
  technology changes a named payer/provider budget. Neither establishes cost-effectiveness.
- CHEERS improves reporting transparency. It does not validate model structure, guarantee
  cost-effectiveness or authorise coverage, procurement, payment or reimbursement.
- Never fabricate costs, utilities, transition probabilities, discount rates, thresholds or local
  rules. Preserve evidence, assumptions, derivations, scenarios, inferences and recommendations as
  separate statement classes.

## Route by mode

| Need | Mode | Read |
|---|---|---|
| define perspective, strategies, horizon, outcomes and economic question | `scope-plan` | [evaluation-design-and-imaging-pathway.md](references/evaluation-design-and-imaging-pathway.md) |
| plan/audit an economic evaluation alongside a study | `trial-based-evaluation` | [evaluation-design-and-imaging-pathway.md](references/evaluation-design-and-imaging-pathway.md) |
| build/audit a decision tree or state-transition/Markov model | `model-based-evaluation` | both method references |
| estimate affordability for a named budget holder and population | `budget-impact` | [modeling-uncertainty-and-hta.md](references/modeling-uncertainty-and-hta.md) |
| interpret deterministic/PSA/scenario uncertainty or value of information | `uncertainty-voi` | [modeling-uncertainty-and-hta.md](references/modeling-uncertainty-and-hta.md) |
| audit CHEERS/HTA reporting or freeze a handoff | `audit-reporting` | applicable method reference and [source-registry.md](references/source-registry.md) |

Use [health-economic-evaluation-passport.md](templates/health-economic-evaluation-passport.md) for
the decision problem and
[model-and-uncertainty-register.md](templates/model-and-uncertainty-register.md) for persistent
model inputs, assumptions and analyses. Do not load every reference for a narrow task.

## Input passport

Record before a claim-bearing calculation or recommendation:

1. jurisdiction, decision maker, policy question, reference-case source/version/access date and
   whether the request is research, HTA evidence, affordability planning or reimbursement advice;
2. population/subgroups, imaging strategy, comparators and the complete care pathway;
3. perspective, time horizon, cycle length if applicable, discounting and price year/currency;
4. evaluation type: cost-effectiveness analysis (CEA), cost-utility analysis (CUA),
   cost-consequence analysis, budget impact analysis (BIA) or value of information (VOI);
5. clinical-effect, test-performance, resource-use, cost and utility inputs with provenance;
6. model structure, assumptions, extrapolations, calibration/validation and implementation context;
7. uncertainty plan, structural scenarios, heterogeneity and decision threshold if applicable;
8. supplied artifacts, code/model version and evidence states.

Use `AUTHOR_INPUT_NEEDED` or `LIVE_VERIFICATION_REQUIRED`; do not fill gaps from convention.

## Required workflow

1. **Freeze the decision problem.** Define who decides, which mutually exclusive strategies are
   compared, for whom, where and for what adoption or research decision.
2. **Select the evaluation.** Use CEA for costs per natural health unit, CUA for costs per QALY,
   cost-consequence analysis when disaggregated outcomes are decision-relevant, and BIA for
   affordability. Use VOI only to ask whether reducing decision uncertainty may be worth further
   research.
3. **Build the imaging pathway.** Link acquisition/test -> result states -> downstream action ->
   treatment/monitoring -> health/resource consequences. Include nondiagnostic/equivocal results,
   repeat tests, incidental findings, false positives/negatives, radiation/contrast harms and delay.
4. **Choose a model that fits time and events.** A decision tree may fit a short, one-off pathway.
   Use a state-transition/Markov or another justified structure when time-varying risks, recurrent
   events or long horizons matter. Complexity is not evidence of validity.
5. **Trace every input.** Label `OBSERVED_INPUT`, `EXTERNAL_SOURCE`, `ASSUMPTION`,
   `MODEL_DERIVATION`, `SCENARIO`, `INFERENCE` or `DECISION_RECOMMENDATION`.
   Record population, period, units, transformations and uncertainty.
6. **Analyse incrementally.** Order strategies, identify strict and extended dominance, and compare
   each remaining strategy with the next least costly relevant alternative. Present incremental
   costs and outcomes before ICERs. Do not report a ratio without its quadrant and uncertainty.
7. **Characterise uncertainty.** Use deterministic analyses for influential inputs, scenario
   analyses for structural/policy choices, probabilistic sensitivity analysis (PSA) with justified
   distributions/correlation, and heterogeneity analyses where decision-relevant. A seed or many
   simulations does not cure a wrong model.
8. **Apply the local decision boundary.** Present results and residual uncertainty. Do not convert a
   research model into coverage, reimbursement, procurement or individual-care authorisation.

## STOP gates

- `STOP_REFERENCE_CASE_UNRESOLVED`: current local HTA/payer methods or applicability cannot be
  verified for a jurisdiction-specific claim.
- `STOP_DECISION_PROBLEM_INCOMPLETE`: perspective, population, relevant comparator or decision
  context is absent.
- `STOP_INPUT_PROVENANCE`: a material cost, utility, effect, transition or resource input lacks an
  identifiable source/assumption state.
- `STOP_INTERMEDIATE_OUTCOME_BRIDGE`: diagnostic or model performance is treated as final health
  benefit without a downstream pathway.
- `STOP_INVALID_INCREMENTAL_ANALYSIS`: ICER/QALY claims use incompatible outcomes, omit relevant
  comparators/dominance or otherwise lack a valid incremental basis.
- `STOP_AUTHORIZATION_REQUEST`: the user requests a reimbursement, coverage, procurement or
  individual patient decision that this skill cannot make.

A STOP blocks the affected economic/decision claim. It does not prevent an input inventory,
transparent scenario shell or handoff to the responsible authority.

## Radiology-specific cost and consequence map

Consider only applicable items and avoid double counting:

- scanner time, room/technologist/radiologist/physicist time, contrast/tracer, consumables and dose;
- capital, installation, integration, storage, networking, software licence, maintenance, quality
  assurance, cybersecurity, monitoring, model updates and staff training;
- nondiagnostic/rejected studies, repeats, recalls, confirmatory tests, biopsy/procedures,
  incidental-finding work-up, delay, false-positive and false-negative pathways;
- reporting/triage time, queue and capacity effects, after-hours workflow, downstream treatment and
  follow-up;
- patient time, travel, caregiving and productivity only when the chosen perspective includes them;
- unequal access, site capability and subgroup consequences when decision-relevant.

Accuracy improvement is not automatically a resource saving. A time saving is not a monetary saving
unless the capacity, displacement and valuation mechanism are explicit.

## Output contract

1. `Route and passport status` — mode, jurisdiction/reference-case state and STOP gate.
2. `Decision problem` — population, strategies, perspective, horizon and decision maker.
3. `Imaging pathway and model` — structure, downstream consequences and excluded pathways.
4. `Input evidence ledger` — source/assumption class, units, period, transformations and
   uncertainty.
5. `Base-case incremental results` — costs, consequences, dominance and ICER/QALY only when valid.
6. `Uncertainty, heterogeneity and scenarios` — deterministic, PSA, structural and VOI if used.
7. `Claim and decision boundary` — evidence, model inference and recommendation separated.
8. `Reporting/HTA handoff` — CHEERS fields, live local checks and unique external owner.

## Handoffs and non-ownership

- Clinical pathway, current care and outcomes -> `radiology-clinical-domain`; effect estimation,
  utilities/statistical uncertainty and quantitative design -> `radiology-stats` /
  `radiology-design`.
- Diagnostic/model performance and decision-curve interpretation/metric fit ->
  `radiology-method-evaluation`; prespecified DCA/net-benefit computation and uncertainty ->
  `radiology-stats`; acquisition/resource measurement -> `radiology-acquisition-qc`.
- Data provenance/release -> `radiology-data`; participant governance -> `radiology-ethics`;
  stakeholder qualitative work -> `radiology-qualitative-mixed-methods`.
- A project grant budget -> `radiology-grant`; manuscript reporting -> `radiology-reporting` /
  `radiology-writing`; project receipts -> `radiology-pipeline`.
- Coverage, reimbursement, tariff, procurement and financial approval remain with the current local
  HTA body, payer, provider and authorised institutional officers. This skill never guarantees an
  adoption or payment decision.
