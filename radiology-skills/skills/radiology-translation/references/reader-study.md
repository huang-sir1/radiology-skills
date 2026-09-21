# Reader-study design matched to the estimand

Use controlled reader studies to estimate how a defined image, algorithm or assistance condition
changes performance under the tested reading conditions. They do not by themselves establish live
workflow effects or patient benefit. For active clinical studies also read
[clinical-impact-study-design.md](clinical-impact-study-design.md).

## Design lock

Record intended use, target readers/cases, intervention/comparator, information available at reading,
case enrichment, reference standard, primary estimand, assignment structure and supported population.

- Fully crossed designs expose every reader to every case/condition; partially crossed or split-plot
  designs trade workload and coverage under a specified assignment scheme. Neither is universally
  strongest. Preserve the actual reader/case/condition overlap for analysis.
- Sequential unaided-then-aided reading estimates the effect of assistance within that sequence;
  independent, parallel or crossover reads answer different questions. Do not interchange their
  estimands or pretend a same-session sequential design has independent reads.
- Randomize and counterbalance order where the design permits. Record learning, carryover, case
  familiarity and training. If repeated reading needs washout, justify its duration for case
  recognizability, workload and the task; a fixed four-week interval does not guarantee no memory.
- Freeze the interface, image/prior-clinical information, AI version/threshold, training and failure
  handling. Blind readers to the reference standard and hypothesis where feasible; document limits.
- Preserve patient -> exam -> lesion/case and reader/site hierarchy. Repeated lesions or readings
  do not become independent participants.

## Endpoint and analysis

- Select the primary endpoint from intended use: accuracy, sensitivity at a specified specificity,
  critical-error rate, localization, reading time, or another justified decision measure. AUC is one
  choice, not a universal primary endpoint.
- An efficiency study may use time as primary with a prespecified accuracy/safety constraint and
  estimand; faster reading alone does not demonstrate maintained accuracy or patient benefit.
- For non-inferiority/equivalence, justify and freeze the margin and analysis before results; lack
  of statistical superiority is not evidence of either.
- Record confidence, agreement, incorrect aided reversals, false-alert workload, failures and
  abstentions when relevant. Do not remove harmful assistance outcomes from the main denominator.
- Match clustered/MRMC inference to the actual outcome and assignment. Obuchowski-Rockette/DBM or
  iMRMC may suit particular ROC designs; do not use a named method merely because there are readers.
  Route quantitative analysis and sample-size calculation to `radiology-stats`.

## Precision and sample size

Justify numbers of readers and cases using the effect/precision target, variance components,
reader/case correlation, prevalence/enrichment, design, multiplicity, failures and missingness.
Pilot data or defensible assumptions may support simulation; report sensitivity to them. There is
no universal minimum such as a blanket rejection of three readers or fifty cases. A small study may
be a feasibility study with wide uncertainty and a restricted claim; a broad population claim needs
adequate reader and case sampling plus appropriate precision.

## Reporting fields

Use supplied facts only:

`[design and sequence] | [reader/case populations and sampling] | [N readers/M independent cases] |
[assignment and overlap] | [order/carryover controls and washout if applicable] | [primary estimand] |
[outcome-appropriate inference] | [effect and uncertainty] | [controlled-study claim limit]`.

Apply CLAIM or the relevant diagnostic-study guideline according to task; DECIDE-AI applies to
early live clinical evaluation, and CONSORT/CONSORT-AI applicability follows the actual trial.
`radiology-reporting` selects the appropriate framework rather than treating every laboratory reader
study as a live clinical trial.

## Primary methods source

[FDA iMRMC research tool](https://cdrh-rst.fda.gov/imrmc-software-do-multi-reader-multi-case-statistical-analysis-reader-studies)
(accessed 2026-09-04) describes MRMC sizing/analysis, non-fully-crossed designs, missing data and
endpoint-specific functions. A method/tool's availability does not validate a particular study;
verify the supported design and endpoint before use.
