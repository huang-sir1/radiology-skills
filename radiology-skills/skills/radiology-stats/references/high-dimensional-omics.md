# High-dimensional statistics — radiomics & multi-omics

The defining problem is often **features far exceed independent sampled units**. The exact counts
vary by study; no universal sample-size threshold makes a high-dimensional analysis adequate.
This breaks naive analysis in three ways: multiplicity, overfitting/optimism, and leakage.

## 1. Multiple testing
- **Family-wise error (FWER)**: Bonferroni (strict), **Holm** (uniformly better than
  Bonferroni). Use when any false positive is costly / few tests.
- **False discovery rate (FDR)**: **Benjamini-Hochberg** (independent/positively dependent),
  Benjamini-Yekutieli (arbitrary dependence), Storey **q-values**. Use for discovery across
  many features/genes.
- **Pre-specification prevents outcome-driven selection; it does not by itself erase
  multiplicity.** One genuinely single primary hypothesis tested once may use the full planned
  alpha. Multiple primary endpoints, contrasts, time points, subgroups, or co-primary hypotheses
  form one or more declared families and need a pre-specified error-control strategy (e.g. Holm,
  alpha allocation, or hierarchical gatekeeping). Treat feature-wide discovery scans as
  exploratory and FDR-controlled.
- Report the **family** (how many tests) and the method.

```python
from statsmodels.stats.multitest import multipletests
rej, q, _, _ = multipletests(pvals, alpha=0.05, method="fdr_bh")
```

## 2. Overfitting & optimism
- With p ≫ n, in-sample performance is meaningless. Report **honest validation**:
  - **Nested cross-validation** — outer loop estimates performance; inner loop does feature
    selection + tuning. Single-loop CV with selection on all data is **optimistically
    biased**.
  - **Bootstrap optimism correction** (Harrell) for apparent vs optimism-corrected
    performance.
- **Dimensionality control**: pre-filter by reproducibility (ICC), then a principled selector
  (LASSO/elastic-net, mRMR, stability selection) **inside** the CV.
- Watch **events-per-variable** — see sample-size.md (Riley).

## 3. Leakage (the silent killer)
Everything data-dependent must be fit on the **training fold only**, then applied to
validation/test:
- feature scaling/normalisation, **discretisation** choices, **ComBat harmonisation**,
  feature selection, class-balancing (SMOTE), imputation, and threshold selection.
- **Patient-level** splits; never let the same patient (or augmented copies) span folds.
- Temporal/site leakage: prefer temporal or external validation for the headline claim.

## 4. Batch / scanner effects (radiomics & sequencing)
- Radiomic features and gene-expression both carry strong **batch/scanner** signal.
- **ComBat** (and `neuroCombat`/`ComBatHarmonization`; for RNA-seq counts,
  `sva::ComBat_seq`) estimates batch-specific parameters while attempting to preserve declared
  biological covariates. Preserving a covariate in the design does not prove that biology and batch
  were separable.
- Distinguish the validation setting before saying “fit on training, transform test”:
  - **Held-out samples from batch/site levels represented in training:** fit every data-dependent
    step inside the training fold and use only an implementation that explicitly supports applying
    frozen parameters to those represented levels.
  - **A wholly unseen external site/batch:** ordinary/transductive ComBat has no estimated parameters
    for that new batch. Do not assume the derivation transform can be applied. Prefer an untouched
    raw-scale external primary analysis, or a pre-specified inductive/reference method with evidence
    that it handles unseen batches.
  - Estimating or re-estimating harmonisation parameters with the external cohort—even without its
    outcomes—uses the external distribution. Label the result adapted/transductive rather than an
    untouched external validation, and retain a raw-scale sensitivity analysis when meaningful.
- If site/batch is inseparable from outcome or biology, harmonisation cannot identify the desired
  effect. Do not “correct” away the confounding; redesign, stratify, collect overlap, or lower the
  claim.
- Always test whether your "signal" is actually scanner/site: stratify, adjust, or show the
  effect survives harmonisation.

## 5. Correlation, not causation; and stability
- Report **effect sizes + CIs**, not just stars.
- Show **feature stability** (selection frequency across resamples) — a feature picked in 5%
  of bootstraps is not a biomarker.

## Reporting sentence
*"Of [N] IBSI-compliant features that met the pre-specified reproducibility criterion, [K]
remained associated with the outcome after Benjamini-Hochberg control at FDR [Q]. A [MODEL]
signature built with all selection and tuning nested inside resampling achieved [METRIC] [ESTIMATE]
([INTERVAL]). For represented scanner levels, [HARMONISER/IMPLEMENTATION] was fit within each
training split and its frozen parameters were applied to held-out samples; the wholly unseen-site
external cohort was analysed [ON THE RAW SCALE / WITH A PRE-SPECIFIED INDUCTIVE METHOD]. Results
from any external-cohort adaptation were labelled separately."*

## Reviewer hot-spots
Selection/harmonisation on all data; single-loop CV reported as validation; thousands of
tests with no correction; SMOTE before the split; "AUC 0.99" on n = 40 with 800 features;
batch effect not addressed.
