# Diagnosis and triage study contract

Use this contract for an index test that classifies a target condition or prioritizes examinations.
Keep two estimands separate:

- **diagnostic accuracy:** how the test agrees with an independent reference standard;
- **triage impact:** how using the test changes workflow, timeliness, errors or resource use.

A retrospective classifier can support the first in a bounded cohort; it cannot by itself establish the
second.

## 1. Diagnostic-use card

| Field | Required specification |
|---|---|
| Population/pathway | screening, symptomatic work-up, emergency, referral or surveillance; eligibility and spectrum |
| Index test | exact model/test version, inputs available at use, output and failure/abstention state |
| Target condition | operational definition and clinically relevant alternatives/mimics |
| Reference standard | method, timing, information available, adjudication and uncertainty |
| Intended role | replacement, add-on, triage, rule-out, rule-in or concurrent decision support |
| Unit | patient/examination; state lesion, side, series and repeat-exam nesting |
| Primary estimand | sensitivity/specificity, likelihood ratio, predictive value or paired test difference at a frozen threshold |
| Consequence | action after positive/negative/abstain and cost of false result/delay |

If the task changes only worklist order, do not call a shorter simulated ranking metric a patient-
outcome benefit.

## 2. Sampling and reference-standard safeguards

- Prefer a consecutive or otherwise pathway-representative cohort. If case-control or enriched,
  describe the sampling fractions and bound prevalence-dependent quantities.
- Verify all or a prespecified unbiased sample with the same credible standard. Differential,
  partial or delayed verification can bias estimates; model it/sensitize or narrow the claim.
- Keep index-test results blinded from reference assessment where possible. If incorporation is
  unavoidable, state it and test an independent/alternative standard.
- Define discordant, indeterminate, technically failed and lost-to-verification states. Excluding them
  from numerator and denominator without a flow table is not acceptable.
- Align index test, reference and clinical episode in time; intervening treatment/disease change can
  invalidate the contrast.

## 3. Model and partition contract

- Keep patients and linked examinations/lesions out of multiple partitions. Use temporal or site-held-
  out testing for the corresponding claim.
- Freeze preprocessing, feature/model selection, calibration and thresholds before test access.
- Compare with the actual standard test/reader/clinical model and a simple baseline. An AI-only AUC
  without pathway comparator is not a clinical advantage.
- Audit acquisition/protocol, report text, post-diagnosis variables, pathology dates and follow-up
  metadata for leakage.

## 4. Accuracy analysis

Report at the intended-use operating point:

- sensitivity, specificity and CIs; predictive values at observed and relevant target prevalence;
- likelihood ratios or risk strata when they match the decision;
- ROC/PR summaries as secondary context, not a replacement for threshold performance;
- calibration when the output is interpreted as probability;
- non-evaluable/abstention rate and performance conditional on versus including abstentions;
- paired comparison for tests/readers on the same cases, with patient/reader/center clustering handled;
- site, scanner/protocol and prespecified clinical subgroup estimates with uncertainty.

Select the threshold in development data from a prespecified action/cost or sensitivity/specificity
constraint. A threshold selected on the test set cannot yield an untouched test estimate.

## 5. Triage-impact route

Choose the design that identifies the intended effect:

| Question | Minimum design |
|---|---|
| Does ordering improve on a fixed historical case set? | controlled simulation; report as simulation only |
| Does AI alter reader decisions? | randomized/counterbalanced MRMC with washout and paired inference |
| Does triage shorten time to review/action? | prospective silent or active workflow study with prespecified clocks and failure handling |
| Does triage improve patient outcomes/resources? | randomized/pragmatic or credible quasi-experimental impact design |

For live studies, define queue state, start/stop timestamps, overnight/weekend handling, concurrent
workflow changes, alert failures, overrides, contamination and cluster/time effects. Report safety
endpoints such as delayed critical cases, not only median turnaround.

## 6. Sample size, sensitivity and stop gates

Base recruitment on positive/negative counts, desired interval precision or paired effect, prevalence,
non-evaluable/verification loss and clustering. Workflow studies also need site/shift/reader variance
and secular-trend assumptions. Use scenario ranges when nuisance inputs are uncertain.

Required sensitivities include alternative indeterminate handling, verified-only versus bias-adjusted
analysis, site/time strata, threshold stability and inclusion of technical failures.

Return `STOP_FOR_REPAIR` for post-test threshold selection, reference incorporation without an explicit
bias boundary, patient leakage, missing denominator reconciliation or an unidentifiable workflow clock.
Return `BIOSTATISTICIAN_REQUIRED` for unresolved verification-bias correction, cluster trial/ITS design
or paired reader inference.

## 7. Claim boundary and handoff

- Accuracy in an enriched retrospective cohort does not establish population predictive values.
- External accuracy does not establish changed reader behavior or workflow benefit.
- Faster worklist movement does not establish improved patient outcome or safety.

Return: `diagnostic-use card -> sampling/reference-standard protocol -> cohort flow -> split/test-access
manifest -> threshold and endpoint contract -> accuracy/impact analysis plan -> safety/failure endpoints
-> claim ceiling -> deviations`.

## Primary and official sources

- Bossuyt PM, et al. [STARD 2015](https://doi.org/10.1136/bmj.h5527).
- Sounderajah V, et al. [STARD-AI](https://doi.org/10.1038/s41591-025-03953-8).
- Tejani AS, et al. [CLAIM 2024 Update](https://doi.org/10.1148/ryai.240300).
- Vasey B, et al. [DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9).
