# Model evaluation — ROC/AUC, DeLong, calibration, decision-analytic net benefit

A clinical prediction model needs **three** things reported: **discrimination**,
**calibration**, and—when a real decision is defined—**decision-analytic consequences**. AUC alone
is not enough, but a decision curve is not observed clinical utility (TRIPOD+AI, PROBAST).

## Discrimination — ROC/AUC
- AUC with 95% CI (DeLong analytic CI, or bootstrap).
- Report sensitivity/specificity at a **pre-specified** operating point (chosen on the
  *training/validation* data, not the test set). Youden's J is a choice — but pre-specify it.

```python
import numpy as np
from sklearn.metrics import roc_auc_score, roc_curve
# DeLong (paired AUC comparison): R canonical path is pROC::roc.test:
#   library(pROC); roc.test(roc1, roc2, method="delong", paired=TRUE)
# Python: no canonical PyPI package — use `MLstatkit` (DelongTest) or bootstrap CIs;
# verify any package name live before installing.
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

## Decision-analytic net benefit — decision-curve analysis (DCA)
- Plots **net benefit** vs threshold probability against "treat all"/"treat none".
- Under an explicit threshold/action and relative-error weighting, asks whether the model has higher
  calculated net benefit than named default strategies across a prespecified plausible range.
- Compute it only when the target population, decision, action, comparator strategies, threshold
  meaning and consequences of false positives/false negatives are defensible. Report prevalence,
  censoring/competing-event handling and uncertainty as applicable.
- DCA does **not** observe patient benefit, workflow impact, safety, cost-effectiveness or adoption.
  Those require the corresponding active impact, implementation or economic design. Do not label a
  positive net-benefit curve as demonstrated “clinical utility.”
- Python: `dcurves`; R: `dcurves`/`rmda`.

```python
# pip install dcurves
from dcurves import dca
import pandas as pd
df = pd.DataFrame({"y": y_true, "model": y_prob})
res = dca(data=df, outcome="y", modelnames=["model"], thresholds=np.arange(0,0.51,0.01))
```

## Threshold provenance & optimism correction

Every reported operating point needs a stated origin. Three compliance tiers, strongest
first:

1. **Pre-registered / clinical-target threshold** — fixed before analysis from a clinical
   requirement (e.g. sensitivity ≥ 0.90 for a rule-out tool) or prior literature. Strongest;
   announce it in the protocol.
2. **Training-derived, frozen** — derive on derivation data (Youden's J or a target operating
   point), lock it, apply unchanged to validation/test. The default for most retrospective
   studies; state where it came from.
3. **Same-data selection (last resort)** — if the threshold must be chosen on the data being
   reported, the selected point's performance is optimistically biased. Bootstrap-correct it
   (resample → re-select the threshold → re-evaluate; report the optimism-corrected value)
   and show a **threshold-sensitivity range** (performance across a band around the chosen
   point), not a single lucky number.

**Never** pick the threshold that maximises test-set accuracy — at any tier.

### Survival high/low-risk stratification

The KM split obeys the same rules:

- Derive the cutpoint on the **training cohort** (median, tertile, or a pre-specified value),
  **freeze** it, and apply it unchanged to the external cohort — no re-optimising per cohort.
- Report the **continuous** score (HR per unit/SD) alongside the stratified KM; the
  dichotomised analysis is a display, not the primary evidence.
- Never search for the cutpoint that maximises the log-rank statistic on the reported cohort
  (the "optimal cutpoint" bias — see survival-prognostic.md).
- State the cutpoint source in Methods: *"The risk-score cutpoint was defined as the
  training-cohort median and applied unchanged to the validation cohort; the score was also
  analysed as a continuous variable."*

## Rare outcomes / class imbalance

Do not route modelling choices through a universal event-count threshold. Diagnose the actual
information available: event/non-event counts by split/site, separation, effective model complexity,
resampling stability, interval width, calibration precision and the intended operating point.

| Information state | Candidate response | Avoid |
|---|---|---|
| sparse or separation-prone for the prespecified model | simplify the model, use justified penalized/shrinkage methods, report instability and reconsider the estimand/design | declaring adequacy from an EPV/event rule or generating synthetic validation information |
| estimable but uncertain | preserve a locked simple model, quantify interval/calibration uncertainty and run scenario/sensitivity checks | resampling before the split or presenting balanced-sample metrics as clinical |
| sufficiently informative for the prespecified model under diagnostics | retain the frozen analysis and honest validation; still report class-specific information and uncertainty | adding complexity because a generic count threshold was crossed |

Metric discipline:

- Headline **PR-AUC** and **sensitivity/specificity at the clinical prevalence**, with
  MCC/balanced accuracy as secondary. **Never headline accuracy** at 15% prevalence —
  predicting "no" for everyone already scores 85%.
- PPV/NPV must be computed at the real prevalence (Bayes adjustment if the sample is
  enriched — see diagnostic-accuracy.md).
- **Resampling breaks probabilities.** Any operation that changes the class distribution
  (SMOTE, over-/undersampling) distorts predicted probabilities: evaluate **calibration and
  DCA on the original-distribution data** (or recalibrate back to prevalence), and state the
  resampling in Methods.
- Report the real prevalence and per-class n — every leakage audit asks
  (→ `radiology-radiomics/leakage-audit.md`).

## Reporting sentence
*"The model discriminated well (AUC 0.88; 95% CI: 0.84, 0.92) and was well calibrated
(slope 0.96, intercept 0.02; Brier 0.11). Decision-curve analysis showed positive net
benefit across threshold probabilities of 0.10–0.40."*

## Reviewer hot-spots
AUC-only; threshold tuned on test set; no calibration; optimistic (no external/independent
test); class imbalance ignored (report PR-AUC/sensitivity at clinical prevalence too).
