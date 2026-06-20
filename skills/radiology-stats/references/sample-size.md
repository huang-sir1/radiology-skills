# Sample size & power for imaging studies

Pre-specify and **justify** sample size (CLAIM, TRIPOD+AI, STARD all ask). Below are the
common cases.

## Diagnostic accuracy (sensitivity/specificity)
Sensitivity is estimated only in **diseased** patients, specificity in **non-diseased** — so
prevalence drives how many *total* patients you need.

- To estimate a sensitivity `Se` with half-width `w` at 95%:
  `n_diseased ≈ 1.96² · Se(1−Se) / w²`, then `n_total ≈ n_diseased / prevalence`.
- Or power a hypothesis (sensitivity ≥ a target). Tools: R `presize`, `MKpower`, `pwr`.

```python
import math
def n_for_sensitivity(se=0.90, half_width=0.05, prevalence=0.15, z=1.96):
    n_dis = (z**2 * se*(1-se)) / half_width**2
    return math.ceil(n_dis), math.ceil(n_dis / prevalence)
# e.g. Se 0.90, ±0.05, prev 0.15 -> diseased and total n
```

## AUC
Power to detect an AUC vs 0.5, or a difference between two AUCs (Hanley-McNeil / Obuchowski).
Inputs: expected AUCs, correlation (paired), allocation, prevalence. R `pROC::power.roc.test`,
`MCPmod`, or Obuchowski formulas.

## Prediction models — EPV and Riley
- Rule of thumb: **events-per-variable (EPV) ≥ 10** (development) — but this is crude.
- Use **Riley et al. minimum sample size** for prediction models: targets small optimism,
  precise overall risk, and a calibration-slope ~1. R **`pmsampsize`** (dev) and
  **`pmvalidsize`** (validation). For **external validation**, target enough **events**
  (often ≥ 100 events and ≥ 100 non-events) for stable calibration.

```r
library(pmsampsize)
pmsampsize(type="b", cstatistic=0.80, prevalence=0.2, parameters=20)
```

## MRMC reader studies
Power depends on **#readers × #cases**, the AUC difference, and variance components
(between-reader, within-reader). Use **OR/DBM** power tools: R `RJafroc::SsPowerGivenJK` or
FDA **iMRMC**. Pilot variance estimates make this far more reliable.

## High-dimensional radiomics/omics
No single n powers thousands of features. Pre-specify the **primary** comparison and power
that; treat the feature scan as FDR-controlled discovery; plan an **independent validation**
cohort rather than relying on one small cohort.

## Reporting sentence
*"A sample of 210 patients (≈ 32 events expected at 15% prevalence) provides a 95% CI
half-width of 0.05 for a sensitivity of 0.90; the prediction model meets the Riley minimum
sample size for 20 candidate predictors (pmsampsize)."*

## Reviewer hot-spots
No sample-size justification; EPV ≪ 10; "post-hoc power"; reader study with too few readers;
validation cohort with too few events for calibration.
