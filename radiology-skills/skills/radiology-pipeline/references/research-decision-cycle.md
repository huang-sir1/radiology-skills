# Research decision cycle: from idea to reusable knowledge

Publication is one output of research, not the organizing logic of the science. Use this cycle for
full projects, learner mentoring, uncertain or negative results, and any project that must decide
whether to proceed, refine, pivot or stop.

## The ten decision states

| State | Decision to make | Required artifact | Primary owner by scope | Gate |
|---|---|---|---|---|
| D0 Question | What exact population/system, contrast, endpoint, time, estimand and intended claim are being studied? | question–estimand card; review work uses review-question/estimand card | imaging: `radiology-design`; mechanism/combined: `radiology-radiogenomics`; evidence synthesis: `radiology-systematic-review` | one claim maps to one observable/contrast or review estimand and real independent unit |
| D1 Feasibility | Can available samples, events, labels, tissue, assays, sites, compute, time, governance or retrievable eligible evidence answer it? | feasibility/stop–go receipt with minimum and stronger routes | scope design owner; evidence synthesis uses `radiology-systematic-review` + `radiology-search`; add clinical/experiment/stats/ethics owners as needed | limiting resource and nearest answerable question explicit; review work states expected coverage and pooling may remain infeasible |
| D2 Assumptions | Which identification, image-formation/measurement, sampling, mapping, model, transport, retrieval, eligibility or synthesis assumptions could invalidate the claim? | assumption register; imaging adds candidate acquisition/QC passport | domain owner + `radiology-method-evaluation`; image measurement: `radiology-acquisition-qc`; review route: `radiology-systematic-review` | every decision-bearing assumption has evidence, diagnostic or claim boundary |
| D3 Discriminating plan | What smallest experiment, acquisition-sensitivity analysis, analysis or evidence-synthesis plan distinguishes the main hypothesis from serious alternatives? | experiment/analysis plan with controls, success/failure and fallback; imaging adds acquisition/reconstruction/phantom/test-retest plan; review protocol with search/screen/extraction/RoB/synthesis plan | computational execution owner, `radiology-acquisition-qc` or `radiology-experiment-design`; evidence synthesis: `radiology-systematic-review`; `radiology-method-evaluation` judges evidence design | controls or review procedures target named failure modes; no decorative analysis list |
| D4 Lock | What is fixed before outcome/test access or study screening/synthesis? | protocol/SAP, task contract, measurement passport, split manifest, parameter/search contract and analysis lock | `radiology-pipeline` records; design/acquisition/domain/stats owners define; review protocol owned by `radiology-systematic-review` | estimand, unit, primary endpoint/eligibility, accepted images, acquisition/reconstruction/QC deviations, selection data, freeze/test-access or search/screen/synthesis policy locked |
| D5 Execute | What actually ran, on which material/version, and what deviated? | acquisition-QC receipt, run manifest plus iteration/test-access log; review search/screen/extraction/change log | image formation/QC: `radiology-acquisition-qc`; downstream domain execution owner; bulk/sc/snRNA/spatial uses `radiology-transcriptomics-analysis`; evidence synthesis uses `radiology-search` for retrieval and `radiology-systematic-review` for selection/extraction; physical wet-lab work remains with trained local staff | provenance, accepted/excluded series, protocol deviations, software/config/seeds or search strings/dates/decisions, exclusions and deviations traceable |
| D6 Evaluate | Are parameters, metrics and methods fit; are comparisons, ablations, synthesis assumptions and sensitivities decisive and fair? | parameter/method-evaluation matrix; review pooling-feasibility and synthesis audit | `radiology-method-evaluation` + `radiology-stats`; review scientific owner remains `radiology-systematic-review` | evidence state and failure boundary visible; protected test remains protected; no pooling merely because studies were found |
| D7 Interpret | Which hypothesis survived, which alternative remains, and what claim ceiling or certainty follows? | claim–evidence–alternative ledger; review claim-certainty ledger | domain scientific owner; evidence synthesis: `radiology-systematic-review` | measured/derived/estimated/associated/predicted/perturbed/synthesized states remain separate |
| D8 Decide | Proceed, refine, replicate, pivot or stop? | decision receipt with cost, benefit, new evidence and stale artifacts | `radiology-pipeline` + current scientific owner | decision tied to prespecified or explicitly revised criteria—not narrative preference |
| D9 Preserve and reuse | Can another team rerun the work and can future projects learn from failures and decisions? | reproducibility/closeout packet plus reusable knowledge memo | `radiology-pipeline`; domain/data owners supply artifacts; review route preserves full search/screen/extraction/synthesis/update trail | code/config/data/access or queries/selection/effect data, negative results, deviations, limitations and reuse boundary archived |

## Assumption register

Record one row per claim-bearing assumption:

`Assumption ID | Claim IDs | category | statement | why required | evidence/support | diagnostic or
falsification | status: supported/working/violated/not-assessable | consequence if false | mitigation |
owner | artifact locator | next review point`.

Categories include identification/causal, sampling/selection, independent-unit/hierarchy,
measurement/reference, preprocessing, missingness, model/distribution, mapping/space/time,
transport/generalisation and implementation. Do not call an unstated assumption “standard.”

## Experiment/analysis plan

Every decision-bearing experiment or analysis records:

`Experiment ID | hypothesis and rival explanation | observable/readout | independent unit and n
rationale | material/cohort/system | intervention/exposure/comparator | randomization/blinding/controls |
parameters/freeze | primary metric/estimand | success/failure criterion | negative control | sensitivity |
expected failure mode | fallback/pivot | owner | cost/time/dependency | status | artifacts`.

For perturbation, dose/time/guide/engagement are experimental factors. For observational mechanism
work, an analysis cannot be relabelled an experiment. For prediction, the protected test is an
evaluation resource, not an iterative development surface.

## Iteration and test-access discipline

An iteration log records what changed, why, which evidence was visible, whether the protected test
was accessed, the decision criterion, artifacts invalidated and whether the analysis/claim changed.
Unlogged repeated test access converts the affected confirmation claim to exploratory. A pilot can
debug feasibility or measurement, but cannot silently become the confirmatory cohort.

## Negative, null and failure evidence

For every failed run, null result, discordance or non-transport event decide among:

1. **invalid execution** — repeat only after a traceable technical defect and repair;
2. **uninformative design/readout** — redesign or choose a closer observable;
3. **valid negative evidence** — retain it and update the hypothesis/claim;
4. **heterogeneity/boundary condition** — stratify only with a defensible interaction or scope rule;
5. **project stop/pivot** — preserve the result and nearest answerable question.

Record `Failure ID | planned object | observation | evidence state | technical diagnosis | biological
interpretation | rival explanation | criterion | decision | rerun/reanalyse/pivot/stop | claim impact |
artifact | manuscript/reuse placement`. Do not delete an unfavourable configuration or validation.

## Learner-facing guidance

Use [the academic tutor state machine](tutor-state-machine.md) for `direct-expert` versus
`guided-learning`, baseline reasoning, targeted feedback, teach-back, transfer and mastery. Preserve
its learner fields across every specialist handoff; do not infer mastery from a polished answer.

For students, return three routes when genuinely available:

- **minimum defensible** — answers the narrowest important question with current resources;
- **standard publishable** — adds the comparator, validation and reproducibility expected for the
  claim;
- **ambitious/discriminating** — adds evidence that separates mechanisms or supports transport.

For each route state prerequisites, trade-offs, likely failure signal, fallback and allowed claim.
Do not equate “more omics/more AI/more experiments” with a better project.

Use [the research-decision packet](../assets/research-decision-packet.template.md) when a durable
artifact helps. Register it in `artifact_manifest.csv`; it is stage-applicable rather than mandatory
for every one-off request.
