# Sample size, power and precision for imaging studies

Sample-size planning is input-driven. Do not substitute a universal EPV, event-count, subject-count,
reader-count or replicate threshold for a design-specific calculation. Record the estimand, effect
worth detecting or precision target, endpoint distribution, allocation/hierarchy, multiplicity,
attrition and feasibility before returning a number.

## Common input contract

For every calculation record:

- target estimand and planned analysis model/test;
- type-I error/multiplicity policy and target power or interval precision supplied by the protocol;
- effect worth detecting, expected performance or margin, with rationale and plausible range;
- variance, prevalence/event probability, censoring, rate/person-time or other nuisance inputs;
- paired correlation, cluster ICC, cluster-size distribution, repeated-measure covariance or reader/
  case variance components when applicable;
- allocation ratio, validation design and analysis population;
- non-evaluable cases, attrition and missingness scenarios;
- input provenance, uncertainty and feasible information size.

Use `AUTHOR_INPUT_NEEDED` for unknown inputs. If a decision-bearing input cannot be supported or
bounded, return `BIOSTATISTICIAN_REQUIRED` instead of a final sample size.

## Diagnostic accuracy

Sensitivity is informed by target-condition-positive cases and specificity by target-condition-
negative cases. Total recruitment therefore depends on the intended population prevalence/spectrum,
verification and non-evaluable examinations.

Possible objectives include:

- precision of sensitivity, specificity, PPV/NPV or likelihood ratios;
- testing against a prespecified clinically meaningful target/margin;
- paired comparison of two tests at a frozen threshold;
- cluster-aware patient/lesion or multi-reader designs.

Choose an exact/binomial or justified approximation from the actual target value and desired interval;
then propagate prevalence, verification and attrition uncertainty to total recruitment. A symbolic
normal approximation for sensitivity precision is
`n_positive ~= z^2 * Se * (1 - Se) / half_width^2`; it is not a default final calculation and must be
checked against the selected interval method and plausible inputs.

## AUC and paired model comparison

Inputs include expected AUCs, effect worth detecting, target-condition prevalence, paired prediction
correlation, allocation and validation design. Use a method matched to independent versus paired AUCs
and to the intended DeLong/bootstrap or MRMC analysis. Do not use an independent-AUC formula for the
same cases or a simple DeLong calculation when multiple readers and cases are crossed.

## Prediction-model development and validation

Rules of thumb based only on events per variable or a fixed event count are insufficient. Use an
input-driven framework that considers:

- outcome type and prevalence/event rate;
- candidate-parameter complexity and anticipated shrinkage/optimism;
- expected model fit/performance and desired precision of overall risk, calibration and
  discrimination;
- censoring and competing risks for time-to-event models;
- external-validation targets for calibration and performance intervals;
- missingness, clustering, site structure and validation design.

Tools such as `pmsampsize` or `pmvalidsize` can implement a supported plan; verify the package/version
and supply all assumptions. An EPV value may be reported descriptively, but it is not the design rule.

## MRMC reader studies

Power depends jointly on readers, cases, modality/condition assignment, figure-of-merit difference,
reader/case variance components and design crossing. Use pilot or external variance components with
uncertainty and a method aligned with the planned OR/DBM/JAFROC-type analysis. Explore feasible reader
and case combinations; do not declare a universal minimum number of either.

## Clustered, repeated and experimental studies

Use [the experimental inference and power contract](experimental-inference-and-power.md). Donor,
litter, cage, animal, culture and repeated-measure structure can change effective information and the
analysis model. A design-effect shortcut is acceptable only when its assumptions match the allocation
and cluster structure; otherwise use model-based simulation or scenario analysis.

## High-dimensional radiomics/omics

There is no single sample size that powers all exploratory features. Define the primary estimand and
power/precision target; treat wide feature scans as multiplicity-controlled discovery and plan honest
validation. Model complexity, outcome information, shrinkage, resampling and external validation are
part of the design—not post hoc decorations.

## Reporting contract

Report:

`objective/estimand -> planned model -> effect or precision target -> nuisance inputs and sources ->
allocation/hierarchy -> multiplicity -> attrition -> calculation/simulation method and version ->
scenario range -> required and feasible independent units -> unresolved assumptions`.

Never copy a worked-example number. Do not use observed post hoc power to reinterpret a completed
non-significant result; report the estimate and interval, information limits and prospective design
implication instead.

## Reviewer hot-spots

- no design-specific justification or unsupported single-point assumptions;
- technical replicates/cells/images counted as independent units;
- cluster, paired, reader/case or repeated-measure correlation ignored;
- a universal EPV/event/replicate cutoff substituted for calibration/precision and design inputs;
- attrition inflation presented as correction of attrition bias;
- a pilot point estimate used without plausible-range sensitivity;
- final sample size reported despite a `BIOSTATISTICIAN_REQUIRED` blocker.
