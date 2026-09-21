# Analysis hierarchy and missingness

## Independent unit first

Name the unit that was independently sampled and randomized/observed. Patients are often the
independent unit even when the dataset contains many lesions, slices, sequences, timepoints, readers,
augmentations, or model runs.

| Structure | Risk | Typical remedy |
|---|---|---|
| Multiple lesions per patient | lesion-level pseudoreplication | patient-level split; cluster-robust/mixed model or patient-level estimand |
| Multiple timepoints | within-patient correlation | repeated-measures/mixed/survival landmark or longitudinal model |
| Multiple readers and cases | crossed clustering | MRMC method; do not average away reader/case variance |
| Multiple slices/patches | inflated n and leakage | patient-level partition; aggregate or hierarchical model |
| Repeated CV/model seeds | technical variability, not new subjects | summarize run variability separately from patient uncertainty |
| Multiple configurations/ablations | paired technical conditions on the same sampled units | compare paired patient/donor-level predictions or effects; model run/configuration variability separately; never t-test fold or seed means as if sampled subjects |
| Multiple omics features | multiplicity and correlation | pre-specified family, FDR/shrinkage, independent validation |
| Donor-derived cultures/organoids with wells/cells | donor and treatment-allocation hierarchy hidden by many subsamples | donor/independently assigned culture as justified unit; aggregate or use hierarchical model |
| Litter/cage/animal experiments | allocation may occur at litter or cage and animals may remain clustered | analyse at the actual assigned unit or use a cluster-aware model with defensible dependence inputs |

Report both the number of independent units and lower-level observations when relevant.

## Missing-data contract

Record by variable and cohort:

- amount and pattern of missingness;
- whether missingness occurs before/after cohort eligibility;
- assumptions (MCAR/MAR/MNAR as a modelling frame, not a proven fact);
- complete-case, single/multiple imputation, model-native handling, or explicit missing category;
- where imputation is fitted in resampling (training folds only for prediction pipelines);
- number of imputations and pooling method where applicable;
- sensitivity analyses for plausible departures.

Do not impute outcomes or use the full dataset to fit imputers in a predictive-validation pipeline
unless a defensible design explicitly permits it.

## Analysis populations and exclusions

Distinguish enrolled/eligible, imaged, analyzable, development, internal validation, external
validation, and complete-case populations. Reconcile them with the flow diagram and Table 1.

Post-hoc exclusions and outlier removal require a rule, timing, counts, and sensitivity analysis.
Never describe an exploratory exclusion as pre-specified.

## Deviation log

Compare planned versus executed analysis:

| Decision | Planned | Executed | Reason | Before/after outcome access | Impact/sensitivity |
|---|---|---|---|---|---|

Material deviations belong in Methods/Supplement and may limit confirmatory language. Route changed
cohorts, endpoints, or primary analyses back to `radiology-pipeline` for downstream staleness review.
