# Model evaluation — ROC/AUC, DeLong, calibration, decision-curve

A clinical prediction model needs **three** things reported: **discrimination**,
**calibration**, and **clinical utility**. AUC alone is not enough (TRIPOD+AI, PROBAST).

## Discrimination — ROC/AUC
- AUC with 95% CI (DeLong analytic CI, or bootstrap).
- Report sensitivity/specificity at a **pre-specified** operating point (chosen on the
  *training/validation* data, not the test set). Youden's J is a choice — but pre-specify it.

```python
import numpy as np
from sklearn.metrics import roc_auc_score, roc_curve
# DeLong (paired AUC comparison): use the `delong` implementations or R pROC::roc.test
# pip install delong  OR translate Sun & Xu (2014) fast DeLong; in R:
#   library(pROC); roc.test(roc1, roc2, method="delong", paired=TRUE)
```

## Comparing AUCs
- **Paired** (same cases): **DeLong** test (R `pROC::roc.test(..., paired=TRUE)`), or
  bootstrap the difference.
- **Unpaired** (different cohorts): DeLong unpaired or bootstrap.
- For models vs readers in a reader study → use **MRMC** (see agreement-mrmc.md), not a plain
  DeLong, because both readers and cases are random.

## Calibration (frequently missing → reviewer flag)
- **Calibration plot**: predicted probability (x) vs observed frequency (y), with a loess/
  binned curve; ideal = diagonal.
- **Calibration slope** (ideal 1) and **intercept / calibration-in-the-large** (ideal 0).
- **Brier score** (lower better); decompose if useful.
- Avoid relying on **Hosmer-Lemeshow** alone (low power, binning-dependent); show the curve.

```python
from sklearn.calibration import calibration_curve
import numpy as np
frac_pos, mean_pred = calibration_curve(y_true, y_prob, n_bins=10, strategy="quantile")
brier = np.mean((y_prob - y_true)**2)
```

## Clinical utility — decision-curve analysis (DCA)
- Plots **net benefit** vs threshold probability against "treat all"/"treat none".
- Answers "is using this model better than default strategies across plausible thresholds?"
- Python: `dcurves`; R: `dcurves`/`rmda`.

```python
# pip install dcurves
from dcurves import dca
import pandas as pd
df = pd.DataFrame({"y": y_true, "model": y_prob})
res = dca(data=df, outcome="y", modelnames=["model"], thresholds=np.arange(0,0.51,0.01))
```

## Threshold selection — say where it came from
Pre-specify (clinical target sensitivity), or derive on training/validation. **Never** pick
the threshold that maximises test-set accuracy.

## Reporting sentence
*"The model discriminated well (AUC 0.88; 95% CI: 0.84, 0.92) and was well calibrated
(slope 0.96, intercept 0.02; Brier 0.11). Decision-curve analysis showed positive net
benefit across threshold probabilities of 0.10–0.40."*

## Reviewer hot-spots
AUC-only; threshold tuned on test set; no calibration; optimistic (no external/independent
test); class imbalance ignored (report PR-AUC/sensitivity at clinical prevalence too).
