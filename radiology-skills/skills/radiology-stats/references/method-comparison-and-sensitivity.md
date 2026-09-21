# Statistical inference for method comparison and parameter sensitivity

Use this reference only after `radiology-method-evaluation` has defined the scientific claim,
comparators, decision-bearing settings, matched conditions and evidence state. This file estimates
differences and uncertainty; it does not decide which methods or parameter ranges are scientifically
necessary.

## Preserve three uncertainty layers

1. **Sampled-unit uncertainty** — patients, donors or other independently sampled units. This is the
   main inferential layer for a population claim.
2. **Dataset/split uncertainty** — variation from sampling or resampling the available cohort.
3. **Algorithm/run uncertainty** — seeds, initialization, stochastic augmentation, checkpoints or
   implementation. These are technical conditions, not additional patients.

Do not use folds, seeds, patches, cells, spots, tiles or model runs as the sample size for a
patient/donor-level significance test. When feasible, use a hierarchical or nested resampling design
that preserves the sampled unit and reports run variability separately.

## Fair paired comparisons

- Compare predictions/effects on the same independent units and preserve pairing.
- Keep the external/test set locked; tuning and configuration selection stay inside development or
  nested resampling.
- Estimate the **difference** between methods/configurations, not whether each is individually
  significant.
- Match the method to the endpoint: paired bootstrap/DeLong for discrimination as appropriate;
  paired bootstrap for calibration, net benefit or other derived metrics; cluster bootstrap or a
  hierarchical model for nested lesions/regions/cells; donor-aware effects for omics.
- For efficiency, match hardware, precision, software, preprocessing and measurement window; report
  distributions or uncertainty across real runs without calling runs independent biological samples.

## Parameter curves and failure boundaries

For ordered or continuous settings, show the primary estimate and uncertainty across a justified
range rather than testing every point against the winner. Predefine the clinically or scientifically
meaningful change and the boundary at which the conclusion, ranking, label, localization or action
changes. A setting that changes the estimand, population, spatial scale, cell identity or decision
threshold is a separate analysis, not another point on the same sensitivity curve.

## Multiplicity

Declare the primary configuration/method contrast, primary metric and primary cohort. Treat the
remaining parameter values, ablations, metrics, subgroups and cohorts as a named family. Use an
appropriate adjustment or label the analysis exploratory. Do not select the most favourable seed,
metric, subgroup or range and report it as prespecified.

## Minimum handoff back

Return:

`Evaluation ID | Claim ID | independent unit/n | paired objects | estimand/delta | interval method |
resampling hierarchy | run variability | multiplicity family/adjustment | estimate/CI/p if applicable |
assumptions/diagnostics | evidence locator | interpretation boundary`.

If only aggregate fold/seed means are supplied and unit-level paired data are unavailable, report
technical variability descriptively and mark patient/donor-level comparison `NOT_ASSESSABLE`.
