# Evidence-synthesis routing

Choose the scientific question before choosing the review label or statistical model. This router
defines the primary review branch, the minimum extraction needed, and the boundary of the claim.

## Routing algorithm

1. If the primary purpose is to map concepts, methods, evidence types or gaps rather than estimate a
   single answer, use `scoping`.
2. If the question is focused and systematic but effect estimates cannot be made commensurate, use
   `systematic-narrative`.
3. If the target is index-test performance against a reference standard, use
   `diagnostic-accuracy-meta`.
4. If the target is a population proportion, prevalence or event incidence/rate with a defined
   denominator or person-time, use `prevalence-incidence-meta`.
5. If the target is a non-interventional association between an exposure, imaging feature,
   measurement or state and an outcome, use `observational-association-meta`.
6. If the target is repeatability/reproducibility, inter-/intra-reader reliability, quantitative
   agreement or method/device/segmentation comparison, use
   `reliability-agreement-method-comparison-meta`. If the methods classify a target condition against
   a reference standard, retain `diagnostic-accuracy-meta` instead.
7. If the target is development/validation performance or incremental value of a prediction,
   radiomics or AI model, use `prediction-radiomics-ai-meta`.
8. If the target is association with a future time-bound outcome, use `prognostic-meta`.
9. If an intervention is assigned or compared to estimate benefit/harm, use `intervention-meta`.
10. If the target is biological explanation across bulk RNA, sc/snRNA, spatial, pathology,
   perturbation or imaging bridges, use `omics-mechanism-synthesis`.

A hybrid project can use parallel branches. For example, a radiomics test may require a diagnostic
accuracy branch for index-test performance and a prediction-model branch for calibration and
external validation. Do not merge their estimands into one pooled answer.

## Route contracts

### Scoping review

- **Frame:** population/concept/context, objectives and a transparent inclusion boundary.
- **Extract:** terminology, evidence/design types, modality, population, methods, outcomes, data
  availability and research gaps.
- **Synthesis:** map counts and characteristics, evidence-gap matrix and concept taxonomy; use
  qualitative grouping rather than a forced summary effect.
- **Claim ceiling:** coverage of the retrieved evidence map, not effectiveness, accuracy, causality
  or certainty unless a separate systematic branch supports it.

### Systematic narrative synthesis

- **Frame:** focused PICO/PIRD/PECO/PICOS or otherwise explicit question and estimand.
- **Extract:** direction, magnitude and precision—not only statistical significance—plus design,
  population, measurement, unit and risk of bias.
- **Synthesis:** group by prespecified question-bearing dimensions; describe consistency,
  heterogeneity, methodological limitations and contradictory evidence.
- **Claim ceiling:** bounded qualitative conclusion. “Most studies were significant” is not an
  effect estimate and must not be used as vote counting.

### Diagnostic-accuracy meta-analysis

- **Frame:** PIRD: participants, index test, reference standard, target condition; specify use case,
  threshold and per-patient/per-lesion unit.
- **Extract:** paired 2 × 2 data when available; threshold, prevalence/spectrum, reference standard,
  blinding/flow/timing, uninterpretable results and clustered/multiple-reader structure.
- **Bias/applicability:** diagnostic-accuracy domains such as patient selection, index test,
  reference standard, flow/timing and applicability to the intended setting.
- **Pooling candidate:** joint bivariate/HSROC-type modelling when thresholds and data support it;
  send implementation to `radiology-stats`. Never average sensitivity and specificity separately
  without evaluating threshold effects and within-study pairing.
- **Claim ceiling:** performance within represented populations, settings, thresholds and reference
  standards; not clinical benefit.

### Prevalence and incidence meta-analysis

- **Frame:** target population/sampling frame, setting, state/event definition, ascertainment,
  denominator and calendar/follow-up period. Separate point, period and lifetime prevalence from
  cumulative incidence and incidence rate.
- **Extract:** numerator, eligible/analyzed denominator or person-time, sampling design, recruitment,
  outcome ascertainment, time window, repeated observations, clustering, zero events, missingness,
  weighting and estimate uncertainty.
- **Bias/applicability:** population representativeness, sampling/non-response, case definition and
  ascertainment, denominator completeness, time-window compatibility and selective reporting.
- **Pooling candidate:** only compatible quantity, population, period, definition and sampling frame.
  State the proportion/rate scale and transformation candidate; statistical implementation and any
  back-transformation remain with `radiology-stats`.
- **Claim ceiling:** the named prevalence or incidence quantity in represented settings and periods;
  not a universal disease burden, individual risk or causal explanation.

### Observational association meta-analysis

- **Frame:** PECO-like population, exposure/feature and operational contrast, comparator, outcome,
  temporal relation, estimand and prespecified confounder/adjustment class.
- **Extract:** design, recruitment, exposure and outcome definitions, contrast/cut point, effect scale,
  adjusted and unadjusted estimates separately, covariates, unit, clustering/repeated measures,
  missingness, selection, follow-up or simultaneity and estimate uncertainty.
- **Bias/applicability:** selection, exposure/outcome measurement, temporal order, confounding,
  missingness, selective analysis/reporting and transportability of the contrast.
- **Pooling candidate:** compatible estimand, exposure contrast, outcome/horizon, effect measure and
  adjustment class. Do not mix correlations, mean differences, odds/risk/rate ratios and hazard
  ratios as if they answered the same question.
- **Claim ceiling:** bounded observational association in represented populations. Cross-sectional
  correlation does not establish temporal direction, diagnosis, prognosis, treatment effect or
  mechanism.

### Reliability, agreement and method-comparison meta-analysis

- **Frame:** measured object/construct, methods/devices/readers/raters, repeat conditions, intended
  unit and decision threshold; declare whether the question is repeatability, reproducibility,
  reliability, categorical agreement, quantitative agreement, segmentation overlap or systematic
  method difference.
- **Extract:** exact metric name and definition, ICC model/type/form, kappa weighting, overlap metric
  variant, bias/limits-of-agreement or repeatability formulation, number and sampling of subjects,
  readers/devices/repeats, unit hierarchy, blinding/order, interval, missing/uninterpretable results,
  estimate uncertainty and dependence among metrics.
- **Bias/applicability:** spectrum/range, subject and reader selection, acquisition/measurement
  protocol, order/memory effects, reference/comparator role, exclusions, model/threshold selection,
  unit mismatch and incomplete uncertainty.
- **Pooling candidate:** only the same construct and compatible metric definition/model/form,
  measurement protocol, unit and dependence. A high correlation can coexist with poor agreement;
  diagnostic target-condition classification routes to DTA rather than this branch.
- **Claim ceiling:** reliability or agreement under the represented measurement conditions; not
  interchangeability, diagnostic accuracy, clinical utility or biological validity unless those are
  separately evaluated.

### Prediction, radiomics and AI meta-analysis

- **Frame:** prediction-specific domains such as source/population, outcome, candidate predictors,
  sample size, missing data, model development, validation and performance; distinguish model-level
  from method-class questions.
- **Extract:** development versus internal/temporal/geographic/external validation; task, endpoint,
  horizon, model identity/version, split, preprocessing/feature selection, sample/events, optimism
  handling, discrimination, calibration, clinical utility, threshold, uncertainty and availability.
- **Bias/applicability:** prediction-model risk domains; add radiomics/AI leakage, patient-level
  partitioning, tuning/test isolation, scanner/site confounding and reproducibility fields.
- **Pooling candidate:** only commensurate model/version, endpoint, horizon, population and
  validation type. Avoid a naive mean of AUCs with incompatible tasks or development estimates.
- **Claim ceiling:** observed performance and transportability evidence; not clinical utility from
  discrimination alone, and not a universal statement about an architecture class.

### Prognostic-factor or prognostic-model meta-analysis

- **Frame:** population, prognostic factor/model, comparator/contrast, outcome and explicit time
  horizon; define estimand and confounder set.
- **Extract:** adjusted and unadjusted estimates separately, adjustment variables, scale/contrast,
  cut point, follow-up, censoring, competing events, events/sample and estimate precision.
- **Bias/applicability:** participation, attrition, factor measurement, outcome measurement,
  confounding, analysis/reporting or model-specific domains as appropriate.
- **Pooling candidate:** compatible estimand, effect scale, contrast, horizon and adjustment class.
  Do not combine hazard ratios, odds ratios and risk ratios as if interchangeable.
- **Claim ceiling:** prognosis/association in represented populations; observational association is
  not an intervention effect or causal mechanism.

### Intervention meta-analysis

- **Frame:** PICO with outcome hierarchy, follow-up windows, estimand, adverse events and intended
  treatment policy.
- **Extract:** assignment, comparator, adherence/crossover, outcomes, follow-up, effect data,
  cluster/crossover/multi-arm structure and analysis population.
- **Bias/applicability:** match to randomized, nonrandomized or preclinical intervention design;
  preserve deviations, missing outcomes, measurement and selective reporting.
- **Pooling candidate:** compatible intervention/comparator, outcome definition, effect scale,
  follow-up and unit; account for multi-arm and cluster dependence.
- **Claim ceiling:** intervention effects depend on design validity and setting. Preclinical
  perturbation effects do not directly establish patient benefit.

### Omics and mechanism evidence synthesis

- **Frame:** PECO/PICOS-like biological question plus tissue, assay/modality, cell/spatial scale,
  disease state, treatment/time context and proposed directional mechanism.
- **Extract:** patient/donor/sample hierarchy, matchedness, tissue/source, assay platform,
  preprocessing, composition/batch, contrast, effect direction/magnitude/uncertainty, multiplicity,
  cell annotation, pseudobulk/spatial unit, perturbation, target engagement, rescue and validation.
- **Bias/applicability:** selection, tissue handling, measurement, batch/confounding, multiplicity,
  outcome-aware analysis, donor-level inference, selective reporting and cross-scale alignment.
- **Synthesis branches:** keep bulk abundance, cell-state/composition, spatial colocalization,
  pathology, perturbation and imaging association distinct, then build a convergence/discordance
  matrix. Use quantitative pooling only for truly commensurate effects and units.
- **Claim ceiling:** enrichment, association and colocalization support plausibility; causal language
  requires appropriate perturbation, target engagement, rescue and independent biological
  validation. Inferred or generated molecular layers are not measured validation.

## Route decision record

Record:

`Route ID | Primary/secondary | Question framework | Estimand | Independent unit | Eligible designs | Required effect/readout | Bias/applicability tool family | Pooling candidate | Reporting handoff | Claim ceiling`

If the route cannot be chosen because the objective mixes incompatible questions, split the
protocol before continuing.
