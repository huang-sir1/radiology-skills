# Research Decision Packet

## 1. Route and project scope

| Field | Entry |
|---|---|
| Study/version | [AUTHOR_INPUT_NEEDED] |
| Current decision state | [D0–D9] |
| Primary owner / collaborators | [AUTHOR_INPUT_NEEDED] |
| Scope and modality roles | [AUTHOR_INPUT_NEEDED] |
| Independent unit / hierarchy / usable intersection | [AUTHOR_INPUT_NEEDED] |
| Evidence inspected / unavailable | [AUTHOR_INPUT_NEEDED] |

## 2. Question–estimand and feasibility

| Question/Claim ID | Population/system | Exposure/intervention | Comparator | Endpoint/readout | Time | Estimand | Intended claim/use | Feasibility verdict | Limiting constraint | Nearest answerable question |
|---|---|---|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [PASS / CONDITIONAL / STOP] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |

## 3. Assumption register

| Assumption ID | Claim IDs | Category | Assumption | Why required | Evidence/diagnostic | Status | Consequence if false | Mitigation/claim boundary | Owner | Locator |
|---|---|---|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [identification / sampling / unit / measurement / preprocessing / missingness / model / mapping / transport / implementation] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [supported / working / violated / not-assessable] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |

## 4A. Experiment or primary-data analysis plan

Use this block for imaging, mechanism, combined, or other primary-data work. For
`study_scope=evidence-synthesis`, use 4B instead; do not disguise review reports or effect rows as
patients, specimens, experiments, or protected-test observations.

| Experiment ID | Hypothesis / rival | Observable | Unit / n rationale | Material/cohort/system | Intervention/exposure/comparator | Controls/blinding/randomization | Parameter/freeze | Primary metric/estimand | Success/failure | Negative control/sensitivity | Fallback | Cost/dependency | Status/artifacts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [planned / running / complete / invalid / stopped] |

## 4B. Evidence-synthesis decision plan (conditional)

Complete this block only when `study_scope=evidence-synthesis`. The independent synthesis unit is
the **study family**, not a paper, report, subgroup, arm, time point, outcome, or effect row. Preserve
the study-family -> report -> effect-row hierarchy and every dependence/overlap decision.

| Review ID | Review route | Question / estimand | Protocol / registration / amendment state | Eligibility version | Search sources, exact dates and strategy artifact | Screening process / conflict rule | RoB-applicability tool/version | Synthesis decision rule | Status |
|---|---|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED] | [scoping / systematic-narrative / diagnostic-accuracy-meta / prevalence-incidence-meta / observational-association-meta / reliability-agreement-method-comparison-meta / prediction-radiomics-ai-meta / prognostic-meta / intervention-meta / omics-mechanism-synthesis] | [AUTHOR_INPUT_NEEDED] | [prospective / amended / retrospectively reconstructed + locator] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [POOL / STRATIFY / NARRATIVE / STOP_FOR_REPAIR + criterion] | [planned / running / complete / invalid / stopped] |

| Review decision ID | Study-family ledger artifact | Companion-report / overlap map | Effect-row ledger artifact | Independent synthesis unit | Dependence / multiplicity handling | Pooling-feasibility verdict | Statistical handoff / code-result artifact | RoB / certainty / claim artifact |
|---|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED] | [ART-___ / path / digest] | [ART-___ / path / digest] | [ART-___ / path / digest] | study family | [AUTHOR_INPUT_NEEDED] | [POOL / STRATIFY / NARRATIVE / STOP_FOR_REPAIR] | [planned brief or verified result locator; never conflate them] | [ART-___ / path / digest] |

## 5. Iteration and protected-test access

For `evidence-synthesis`, use the same ledger for search updates, screening/extraction amendments,
newly visible reports and synthesis changes. In `Evidence visible`, state which reports/effect rows
were visible; in `Protected-test access`, record `not-applicable` and use the deviations column for
protocol/search/screen/synthesis access or amendment state.

| Iteration ID/date | What changed and why | Evidence visible | Protected-test access | Decision criterion | Deviations | Invalidated artifacts | Claim/analysis consequence | Owner | Locator |
|---|---|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [none / once-per-lock / repeated / unknown] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |

## 6. Parameter/method evaluation

For `evidence-synthesis`, record retrieval/eligibility assumptions, study-family deduplication,
effect compatibility, dependence, model choice, pooling feasibility, heterogeneity and sensitivity;
do not call a planned model a completed synthesis.

| Evaluation IDs / artifact | Parameters | Metrics/readouts | Methods/comparators | Evidence state | Verdict | Failure boundary | Claim consequence | Statistical handoff |
|---|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [PLANNED / AUTHOR_REPORTED / PARTLY_VERIFIED / VERIFIED / NOT_ASSESSABLE] | [PASS / CONDITIONAL / STOP] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |

## 7. Negative, null, discordant and failed evidence

| Failure ID | Planned object | Observation / locator | Evidence state | Technical diagnosis | Biological interpretation / rival | Criterion | Decision | Claim impact | Preserve/write/reuse location |
|---|---|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [invalid execution / uninformative / valid negative / heterogeneity / not-assessable] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [rerun / reanalyse / redesign / replicate / pivot / stop / retain] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |

## 8. Decision and next route

| Field | Entry |
|---|---|
| Decision | [proceed / refine / replicate / pivot / stop] |
| Governing evidence/criterion | [AUTHOR_INPUT_NEEDED] |
| Preserved strengths | [AUTHOR_INPUT_NEEDED] |
| Current claim ceiling | [AUTHOR_INPUT_NEEDED] |
| Minimum defensible route | [prerequisites / cost / failure / fallback / claim] |
| Standard publishable route | [prerequisites / cost / failure / fallback / claim] |
| Ambitious discriminating route | [prerequisites / cost / failure / fallback / claim] |
| Single next decision-bearing action / owner | [AUTHOR_INPUT_NEEDED] |

## 9. Reproducibility closeout and knowledge reuse

| Object | Versioned artifact / digest / access | Reuse boundary |
|---|---|---|
| Protocol/SAP and deviations | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |
| Evidence-synthesis protocol, registration and amendments (conditional) | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |
| Search strategies, dates, deduplication and screening trail (conditional) | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |
| Study-family / companion-report map and effect-row ledger (conditional) | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |
| RoB/applicability, synthesis code/results and certainty ledger (conditional) | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |
| Cohort/split/sample manifest | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |
| Code/environment/config/seeds/model | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |
| Source data/result tables/figures | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |
| Negative/failure/discordance register | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |
| What future projects should preserve/change/not infer | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |
