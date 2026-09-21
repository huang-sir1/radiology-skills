# Modeling, Uncertainty, VOI and HTA

Use for `model-based-evaluation`, `budget-impact`, `uncertainty-voi` and
`audit-reporting`.

## 1. Model selection and conceptualisation

Start with a diagram agreed against the decision problem and clinical pathway.

- A **decision tree** fits short, one-off, acyclic pathways where timing and recurrent events are
  not material.
- A **cohort state-transition/Markov model** fits recurring events or longer horizons when
  mutually exclusive/exhaustive states and cycle transitions adequately represent history.
- Individual simulation, discrete-event or other structures require a stated need; greater
  complexity does not make a model more credible.

Record population, states/events, transitions, time/cycle, memory assumptions, competing risks,
half-cycle or tunnel-state handling when used, extrapolation, calibration targets and structural
alternatives. A model should be as simple as possible while retaining decision-relevant mechanisms.

## 2. Model credibility audit

Separate:

1. **face/conceptual validity** — structure reflects the decision and pathway;
2. **verification** — equations, code, units and implementation match the specification;
3. **input validity** — evidence is applicable and transformations are traceable;
4. **calibration** — fitted targets, process and retained uncertainty are reported;
5. **internal validation** — model reproduces expected identities/benchmarks;
6. **external validation** — predictions are compared with independent evidence where feasible;
7. **cross-model validity** — material differences from relevant models are explained.

Do not call a model “validated” without naming the level and receipt.

## 3. Uncertainty contract

| Uncertainty | Minimum response |
|---|---|
| parameter | deterministic range/source and PSA distribution with justified parameters |
| correlation | preserve joint sampling or state why independence is defensible |
| structural | alternative pathway/model/scenario, not just wider parameter ranges |
| methodological | reference-case analysis plus clearly labelled alternatives |
| heterogeneity | decision-relevant subgroup analyses with interaction/transport caveats |
| stochastic | enough simulations, convergence/Monte Carlo error and reproducible seed |

For PSA, preserve the distribution rationale, correlations, draws, seed, run ID and output. Present
cost-effectiveness planes/acceptability summaries when appropriate, but do not interpret probability
cost-effective as probability clinically effective or as an approval probability.

## 4. Budget impact analysis

BIA is payer/provider-specific affordability analysis. Record:

- eligible and treated population by period, incident/prevalent entry and exit;
- current and future technology mix, uptake, access restrictions and displacement;
- budget-holder perspective and short policy-relevant horizon;
- acquisition, implementation, recurring and downstream condition-related costs;
- annual and cumulative budget impact plus scenario analyses;
- relationship to, but separation from, the CEA/CUA assumptions.

A project grant budget, hospital quotation or price list is not a BIA. A favourable BIA does not
establish cost-effectiveness; a favourable ICER does not prove affordability.

## 5. Value of information

Use VOI only after a coherent decision model and uncertainty distribution exist.

- EVPI bounds the value of eliminating all decision uncertainty for the relevant population/time.
- EVPPI identifies value attached to parameter groups.
- EVSI compares candidate study designs after accounting for the information they may generate.
- Research cost, delay, implementation and population horizon belong in the research-decision
  interpretation.

VOI does not prove a study is ethical, feasible, fundable or the best scientific design. Do not
present a positive EVPI as an automatic recommendation for data collection.

## 6. HTA and reporting

Before jurisdiction-specific advice, retrieve the current official manual and record:

- agency/programme, technology route and scope;
- current version/update date and applicable reference case;
- perspective, comparator, outcome, horizon, discounting and threshold/decision process;
- required sensitivity, subgroup/equity, stakeholder and submission fields;
- confidentiality, model access and validation requirements.

Use CHEERS 2022 to audit reporting. For AI-enabled interventions, consider CHEERS-AI in addition
when applicable. Neither framework determines whether assumptions are correct. WHO's medical-device
HTA guidance frames HTA as multidisciplinary; economic results alone do not cover clinical, ethical,
organisational or social consequences.

## 7. Decision-curve and reimbursement boundary

Decision-curve analysis estimates a model's clinical net benefit across threshold probabilities. It
does not include the full opportunity cost, resource use, time horizon or monetary valuation needed
for health-economic evaluation. Hand it to `radiology-method-evaluation` / `radiology-stats`.

This skill may map evidence to a current HTA framework. It cannot issue a payer decision, tariff,
coverage determination, procurement approval, reimbursement code or patient-level authorisation.
