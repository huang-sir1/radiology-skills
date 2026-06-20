# Diagnostic accuracy — estimates, CIs, paired comparison

## The 2×2 and its metrics
From TP, FP, FN, TN against a reference standard:
- **Sensitivity** = TP/(TP+FN); **Specificity** = TN/(TN+FP).
- **PPV/NPV** depend on **prevalence** — report the prevalence; if the sample is enriched
  (e.g. 1:1), compute PPV/NPV at a realistic prevalence using Bayes, and say so.
- **Accuracy** is prevalence-dependent and usually uninformative alone.
- **Likelihood ratios**: LR+ = sens/(1−spec); LR− = (1−sens)/spec. Prevalence-independent;
  reviewers like them.

## Confidence intervals (do not use plain Wald for proportions)
- Proportions (sens, spec, PPV, NPV): **Wilson** (good default) or **Clopper-Pearson**
  (exact, conservative). Avoid Wald near 0/1.
- Likelihood ratios: log-based CI (or bootstrap).
- Report counts with each estimate (e.g. `0.87 (130/149)`).

```python
import numpy as np
from statsmodels.stats.proportion import proportion_confint

def diag_metrics(tp, fp, fn, tn, method="wilson"):
    sens = tp/(tp+fn); spec = tn/(tn+fp)
    sens_ci = proportion_confint(tp, tp+fn, method=method)
    spec_ci = proportion_confint(tn, tn+fp, method=method)
    ppv = tp/(tp+fp); npv = tn/(tn+fn)
    ppv_ci = proportion_confint(tp, tp+fp, method=method)
    npv_ci = proportion_confint(tn, tn+fn, method=method)
    lr_pos = sens/(1-spec); lr_neg = (1-sens)/spec
    return dict(sens=(sens,sens_ci), spec=(spec,spec_ci),
                ppv=(ppv,ppv_ci), npv=(npv,npv_ci),
                lr_pos=lr_pos, lr_neg=lr_neg)
```

## Comparing two tests on the SAME patients (paired)
- **Sensitivity/specificity** (binary calls): **McNemar's test** on the discordant pairs
  (within the diseased subset for sensitivity, non-diseased for specificity).
- Do **not** use a chi-square for independent groups when the same cases were read twice.

```python
from statsmodels.stats.contingency_tables import mcnemar
# table = [[both_correct, A_correct_B_wrong],[A_wrong_B_correct, both_wrong]]
print(mcnemar(table, exact=True))   # exact for small discordant counts
```

## Clustered data (multiple lesions per patient)
Lesions within a patient are correlated. Use cluster-robust / GEE / mixed-effects, or
analyse at the patient level. Reporting per-lesion accuracy as if independent **inflates
significance** — a common reviewer catch.

## Reporting sentence
*"At the pre-specified threshold, sensitivity was 0.87 (95% CI: 0.81, 0.92; 130/149) and
specificity 0.79 (95% CI: 0.72, 0.85; 158/200); disease prevalence was 0.27. The model and
radiologists differed in sensitivity (P = .02, McNemar)."*

## Reviewer hot-spots
Threshold chosen on the test set; PPV/NPV quoted from an enriched sample as if clinical;
independence assumed for clustered lesions; missing CIs; "accuracy" headline hiding poor
sensitivity at clinical prevalence.
