# High-dimensional statistics — radiomics & multi-omics

The defining problem: **features ≫ samples**. Matched imaging+omics cohorts are small
(often n < 100), while features run to thousands (radiomics) or tens of thousands (genes).
This breaks naive analysis in three ways: multiplicity, overfitting/optimism, and leakage.

## 1. Multiple testing
- **Family-wise error (FWER)**: Bonferroni (strict), **Holm** (uniformly better than
  Bonferroni). Use when any false positive is costly / few tests.
- **False discovery rate (FDR)**: **Benjamini-Hochberg** (independent/positively dependent),
  Benjamini-Yekutieli (arbitrary dependence), Storey **q-values**. Use for discovery across
  many features/genes.
- **Pre-specify** the primary hypothesis (escapes correction); treat the feature-wide scan as
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
- **ComBat** (and `neuroCombat`/`ComBatHarmonization`; for RNA-seq, `sva::ComBat_seq`)
  removes batch while **preserving biological covariates** — include the biology in the model
  so it is not removed. Fit on training, transform test.
- Always test whether your "signal" is actually scanner/site: stratify, adjust, or show the
  effect survives harmonisation.

## 5. Correlation, not causation; and stability
- Report **effect sizes + CIs**, not just stars.
- Show **feature stability** (selection frequency across resamples) — a feature picked in 5%
  of bootstraps is not a biomarker.

## Reporting sentence
*"Of 1218 IBSI-compliant features (each ICC > 0.80 across two segmentations), 47 associated
with the outcome after Benjamini-Hochberg control (FDR < 0.05). A LASSO signature built
inside 10×10 nested cross-validation achieved an optimism-corrected AUC of 0.79 (95% CI:
0.71, 0.86); ComBat harmonisation (fit on training) removed scanner effects while preserving
the outcome covariate."*

## Reviewer hot-spots
Selection/harmonisation on all data; single-loop CV reported as validation; thousands of
tests with no correction; SMOTE before the split; "AUC 0.99" on n = 40 with 800 features;
batch effect not addressed.
