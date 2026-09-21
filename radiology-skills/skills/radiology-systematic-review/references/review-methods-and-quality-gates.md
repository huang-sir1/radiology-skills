# Review methods and quality gates

These gates prevent a polished meta-analysis from concealing an unstable review process. Evaluate
each gate as `PASS`, `CONDITIONAL`, `STOP`, or `NOT_ASSESSABLE`, with an artifact anchor.

## Gate 0 — Question and estimand

- The route, objective and question framework are explicit.
- Population/context, index/exposure/intervention, comparator/reference standard, outcome,
  time horizon and intended use are compatible with the claim.
- The study/report/effect and biological independent units are declared.

`STOP` if one pooled estimate would answer multiple incompatible questions.

## Gate 1 — Protocol, registration and amendments

- Protocol identifier, version/date, authorship and registration status are recorded.
- Status is one of `PROSPECTIVELY_REGISTERED`, `RETROSPECTIVELY_REGISTERED`, `UNREGISTERED`,
  `REGISTRATION_NOT_APPLICABLE`, or `NOT_VERIFIED`.
- Eligibility, primary outcomes, synthesis plan, subgroups/sensitivities and deviation policy are
  time-stamped. Amendments include date, reason, result-awareness state and affected outputs.

Registration cannot be inferred from a manuscript statement without a verifiable identifier.

## Gate 2 — Search handoff and currency

The protocol supplies `radiology-search` with concepts, controlled-vocabulary needs, source types,
eligible dates/languages/designs, grey-literature policy, complete strategy capture, deduplication
rules, last-search date and update trigger. The returned log must identify each source/platform,
exact strategy, run date, result count and deduplication output.

Record a search-strategy peer-review receipt for the complete source-specific strategy: strategy
version/date, reviewer role and conflict state, stated criterion or framework, review date, comments
locator, resolution/amendment locator, unresolved issues, closure state and whether a material change
requires re-review. Allowed states are `NOT_REVIEWED`, `REVIEWED_OPEN`, `REVIEWED_CLOSED`, and
`NOT_APPLICABLE`; do not infer review from an author's assertion that a librarian was involved.

Also record lifecycle as `STATIC`, `LIVING`, or `RETIRED`. A living review requires a source/update
trigger or cadence, responsibility, last completed update and decision consequences. A retired review
requires retirement date/reason and successor/archive locator. A lifecycle label is not evidence that
the search is current.

A search described only as keywords, with no source-specific strategy or date, is not reproducible.

## Gate 3 — Screening and flow

- Two independent reviewers are planned for title/abstract and full-text screening, or any
  alternative is transparently justified.
- Pilot/calibration and conflict resolution are documented.
- Full-text exclusions use a predefined mutually interpretable taxonomy.
- Counts reconcile across retrieval, deduplication, screening, retrieval failures, exclusion and
  inclusion for the PRISMA flow.
- Multiple reports from one underlying study/cohort share a `Study-family ID`.

Do not call a single-person screen “independent duplicate screening.”

For every AI-assisted or priority-screening route, record this frozen automation receipt before
production exclusions:

`automation ID | tool/provider | model ID | model/version snapshot | prompt/instructions version |
code/config version | input-corpus digest | pilot/calibration sample and sampling rule | reference
human decisions | calibration metrics/error classes | ranking/exclusion threshold | threshold frozen
on/by | low-priority audit sampling rule and n | recall safeguard and minimum acceptable value |
breach action | human override log | final human decision owner | immutable score/decision artifact`.

The model may rank or recommend; a named human remains finally responsible. Records below a priority
threshold may be excluded only under the prespecified protocol and after the frozen low-priority
audit shows the recall safeguard is met. A breach returns `STOP`: suspend automated exclusions,
human-screen the affected low-priority set, document misses and recalibrate prospectively. Preserve
the failed pilot and prior thresholds. Never tune the threshold to recover a preferred included set,
and never call one human plus a model “two independent reviewers.”

## Gate 4 — Extraction integrity

- Extraction fields implement the question and planned synthesis, not a post hoc favourite result.
- At least one reviewer extracts and another verifies decision-bearing fields; alternative processes
  are declared.
- Source location, extractor/verifier, query status and transformations remain traceable.
- Adjusted/unadjusted, model development/validation, patient/lesion, donor/cell/spot and distinct
  time horizons remain separate.
- Duplicate reports and overlapping cohorts are reconciled before counting evidence.

## Gate 5 — Risk of bias and applicability

Choose domains by design/question, not convenience:

| Evidence design/question | Domain family to consider |
|---|---|
| diagnostic accuracy | patient selection, index test, reference standard, flow/timing; comparative additions when needed |
| prevalence/incidence | sampling frame/representativeness, recruitment/non-response, condition/event ascertainment, denominator/person-time completeness, period and analysis/reporting |
| observational association | selection, exposure definition/contrast, outcome, temporal order, confounding/adjustment, missingness and selective analysis/reporting |
| reliability/agreement/method comparison | subject/object and reader/device selection, measurement protocol, order/blinding, metric/model/form, exclusions/missingness, unit/dependence, analysis/reporting and applicability to intended conditions |
| prediction/model evidence | participants, predictors, outcome, analysis; AI/model-specific extension when applicable |
| randomized intervention | randomization, deviations, missing outcomes, outcome measurement, selective reporting |
| nonrandomized intervention | confounding, selection, classification, deviations, missingness, measurement, reporting |
| prognostic factor/model | participation, attrition, factor/predictor, outcome, confounding and analysis/model domains |
| observational prevalence/association | selection, exposure/measurement, outcome, confounding, missingness and selective reporting |
| preclinical/animal/perturbation | allocation, blinding, attrition, target engagement, off-target/toxicity, outcome measurement and reporting |
| omics/spatial/mechanism | donor/tissue selection, assay/preprocessing, batch/composition, hierarchy, multiplicity, selective analysis and cross-scale applicability |

Record each domain as `LOW`, `SOME_CONCERNS`, `HIGH`, or the exact labels of the selected verified
tool. Preserve signalling answers and anchors. Overall judgment follows the tool logic; do not
compute an unvalidated mean score. Applicability is a separate question.

## Gate 6 — Pooling feasibility

Build candidate synthesis groups and assess:

1. clinical compatibility: disease spectrum, setting, prior treatment and intended use;
2. design compatibility: eligible designs, sampling and validation type;
3. intervention/index/exposure/model compatibility;
4. comparator/reference-standard compatibility;
5. outcome/target-condition definition and time horizon;
6. effect measure, threshold and scale/contrast;
7. independent unit and clustering/dependence;
8. availability of estimate and valid uncertainty/reconstructable data;
9. overlapping populations/reports; and
10. risk-of-bias patterns that would make a single average misleading.

For prevalence/incidence also require compatible denominator/person-time and period. For
observational association require compatible exposure contrast and adjustment class. For
reliability/agreement require the same construct, metric definition/model/form, measurement
conditions and reader/device/repeat hierarchy; correlation alone does not establish agreement.

Return one decision per group:

- `POOL`: a common estimand and defensible statistical synthesis exist.
- `STRATIFY`: compatible only after prespecified separation.
- `NARRATIVE`: evidence can be synthesized but not as a defensible common effect.
- `STOP_FOR_REPAIR`: missing/contradictory extraction or unresolved duplicate/dependence prevents
  synthesis.

Statistical heterogeneity does not repair conceptual incompatibility, and a random-effects model is
not permission to average unrelated questions.

## Gate 7 — Statistical synthesis handoff

For each eligible effect row, supply `radiology-stats`:

`Study-family ID | Effect ID | estimate | effect scale/transformation or exact reliability/agreement metric definition/model/form | standard error/CI or raw data | numerator/denominator/person-time where relevant | direction convention | threshold/horizon/measurement period | adjusted status | independent unit | readers/devices/repeats/clusters/nesting | shared comparator/multiple effects | covariance information | risk-of-bias state`

Also supply the planned model candidate, uncertainty method, heterogeneity outputs, subgroup and
meta-regression hypotheses, sensitivity exclusions, influence diagnostics, small-study assessment,
multiplicity family and software/version expectations. Statistical implementation remains with the
statistics owner.

Subgroups require a plausible effect-modification question and sufficient studies; comparing
“significant” versus “not significant” subgroups is not an interaction test. Meta-regression with a
small evidence base is exploratory and vulnerable to ecological bias.

## Gate 8 — Non-pooling synthesis

When quantitative pooling is not justified:

- group studies by prespecified population/design/modality/exposure/outcome dimensions;
- show effect direction, magnitude and precision when available;
- integrate risk of bias and applicability into the conclusion;
- explain concordance, discordance and missing evidence;
- avoid vote counting by p-value; and
- state the reason pooling was rejected and what future evidence would make it possible.

For omics/mechanism, use a modality-by-mechanism convergence matrix with measured versus inferred,
matched versus unmatched, patient/donor n, spatial/temporal alignment, perturbation, rescue and
external validation kept visible.

## Gate 9 — Certainty and claim ceiling

Use GRADE or another verified, appropriate certainty framework for intervention, diagnostic/
prognostic or other questions when applicable; otherwise provide an explicit confidence rationale
rather than mislabeling a score. Do not call an informal confidence judgment GRADE. Consider risk
of bias, inconsistency, indirectness/applicability, imprecision, publication bias/small-study and
reporting concerns, effect magnitude and other framework-specific domains.

Separate these claim types:

- descriptive mapping;
- prevalence/incidence in the represented population and period;
- observational association;
- reliability, repeatability or agreement under the represented measurement conditions;
- association/enrichment;
- diagnostic performance;
- prediction performance/transportability;
- prognosis;
- intervention effect;
- biological plausibility;
- causal mechanism; and
- clinical utility/patient benefit.

The conclusion cannot exceed the weakest decision-bearing link. High-impact venues and large cell
or spot counts do not raise the ceiling.

## Gate 10 — Reporting and writing handoffs

The reporting handoff contains route, verified guideline/checklist version request, protocol/
registration and lifecycle state, search dates/log, search-strategy peer-review receipt, PRISMA
counts, selection/extraction process, risk-of-bias tool, synthesis decisions, certainty and
deviations. `radiology-reporting` owns the item-by-item audit.

The writing handoff contains stable claim IDs, supported wording, effect results with uncertainty,
heterogeneity, certainty, limitations, display/source anchors and forbidden stronger wording.
`radiology-writing` owns the manuscript prose; planned or unverified analyses stay out of Results.
