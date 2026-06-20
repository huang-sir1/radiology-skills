# Radiogenomics statistical analysis plan

Use this file when drafting a protocol, Methods section, preregistration, or pre-submission audit.
A radiogenomics paper becomes credible when the primary analysis is clear before the discovery
scan begins.

## 1. Define the primary question
Specify:

`Imaging phenotype | Molecular endpoint | Patient population | Primary estimand/effect | Validation cohort | Success criterion`

Examples:
- ADC habitat texture associated with hypoxia pathway activity.
- CT radiomic signature predicting EGFR mutation status.
- MRI habitat factor associated with macrophage fraction estimated from RNA-seq deconvolution.

## 2. Separate confirmatory and discovery analyses
- **Confirmatory**: one pre-specified feature/signature/pathway/mutation and one primary test.
  Report effect size, CI, and p value.
- **Discovery**: feature-by-gene, feature-by-pathway, or multi-omics scan. Control FDR and treat
  results as hypothesis-generating unless replicated.
- Do not present a selected discovery result as if it had been the primary hypothesis.

## 3. Covariates and confounders
Pre-specify covariates based on biology and design, not p-value fishing:

`Age | sex | stage/grade | tumour volume | site/scanner | acquisition protocol | sequencing batch | tumour purity | treatment status | molecular subtype`

Avoid adjusting for a variable that lies downstream of the tested biology unless the estimand
requires it. For batch correction, preserve the biological covariate of interest.

## 4. Multiplicity
- Feature-gene grids require FDR control, usually BH-FDR/q-values, across the declared family of
  tests.
- Define the test family in advance: all features x all genes, selected features x Hallmark
  pathways, or one imaging factor x candidate gene set.
- Report the number of tests, FDR method, threshold, and whether validation was required.

## 5. Prediction models
If the output is an individual-level prediction score, route to TRIPOD+AI and radiology-stats.
- Split by patient, site, or time. Never split by slice, patch, lesion region, or omics sample
  when they share a patient.
- Feature selection, scaling, ComBat, imputation, threshold choice, and hyperparameter tuning must
  occur inside training folds.
- Use nested CV for tuning in small cohorts and reserve external validation where possible.
- Report discrimination, calibration, decision-curve analysis when clinically relevant, and CIs.

## 6. Validation hierarchy
Rank evidence strength:
1. Independent external cohort with same pipeline and frozen model/feature definition.
2. Temporal or geographic validation.
3. Cross-platform molecular validation or orthogonal biology, such as IHC or spatial subset.
4. Internal resampling only. This supports exploration but rarely supports strong claims.

Validation should check direction and effect size, not only statistical significance.

## 7. Sensitivity and negative controls
Consider, when data permit:
- Batch-only model or site-only classifier.
- Association after scanner/omics batch adjustment.
- Permutation or label-shuffle analysis.
- Tumour-volume-adjusted analysis.
- Excluding post-treatment or out-of-window cases.
- Repeating with alternative segmentation or robust feature set.
- Negative-control genes/pathways not expected to relate to the phenotype.

## SAP output template
Return:

1. `Primary hypothesis`
2. `Analysis populations`: discovery, validation, exclusions
3. `Variables`: imaging, omics, clinical covariates
4. `Preprocessing`: train-only steps marked
5. `Primary analysis`: model/test, effect size, CI, success criterion
6. `Discovery analysis`: test family and FDR
7. `Validation`: cohort and replication rule
8. `Sensitivity/negative controls`
9. `Reporting guideline`: CLEAR/IBSI, TRIPOD+AI if predictive, STROBE/REMARK/omics standards as applicable