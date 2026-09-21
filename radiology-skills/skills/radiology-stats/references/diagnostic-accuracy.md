# Diagnostic accuracy — estimates, CIs, paired comparison

## The 2×2 and its metrics
From TP, FP, FN, TN against a reference standard:
- **Sensitivity** = TP/(TP+FN); **Specificity** = TN/(TN+FP).
- **PPV/NPV** depend on **prevalence**. Report the observed sample prevalence. If the sample is
  enriched (e.g. case-control or 1:1 sampling), label the sample PPV/NPV as sample quantities and
  calculate separate target-setting scenarios with Bayes; do not present transported values as
  directly observed clinical performance.
- **Accuracy** is prevalence-dependent and usually uninformative alone.
- **Likelihood ratios**: LR+ = sens/(1−spec); LR− = (1−sens)/spec. Prevalence-independent;
  reviewers like them.

## Confidence intervals (do not use plain Wald for proportions)
- Proportions (sens, spec, PPV, NPV): **Wilson** (good default) or **Clopper-Pearson**
  (exact, conservative). Avoid Wald near 0/1.
- Likelihood ratios: log-based CI (or bootstrap).
- Report counts with each estimate (e.g. `0.87 (130/149)`).

```python
from math import sqrt

def wilson_interval(successes, total, z=1.959963984540054):
    """Two-sided Wilson score interval; z=1.95996 gives a nominal 95% interval."""
    if total <= 0 or successes < 0 or successes > total:
        raise ValueError("require 0 <= successes <= total and total > 0")
    proportion = successes / total
    denominator = 1 + z**2 / total
    center = (proportion + z**2 / (2 * total)) / denominator
    margin = z * sqrt((proportion * (1 - proportion) + z**2 / (4 * total)) / total) / denominator
    return center - margin, center + margin

def predictive_values_at_prevalence(sensitivity, specificity, prevalence):
    """Bayes-transport PPV/NPV to a specified target-prevalence scenario."""
    if not 0 < prevalence < 1:
        raise ValueError("target_prevalence must be strictly between 0 and 1")
    if not 0 <= sensitivity <= 1 or not 0 <= specificity <= 1:
        raise ValueError("sensitivity and specificity must be between 0 and 1")
    ppv_denom = sensitivity * prevalence + (1 - specificity) * (1 - prevalence)
    npv_denom = specificity * (1 - prevalence) + (1 - sensitivity) * prevalence
    if ppv_denom == 0 or npv_denom == 0:
        raise ValueError(
            "PPV or NPV is undefined because the classifier predicts no cases in that class"
        )
    return {
        "ppv": sensitivity * prevalence / ppv_denom,
        "npv": specificity * (1 - prevalence) / npv_denom,
    }

def diag_metrics(tp, fp, fn, tn, target_prevalence=None):
    counts = (tp, fp, fn, tn)
    if any(value < 0 or int(value) != value for value in counts):
        raise ValueError("tp, fp, fn, and tn must be non-negative integer counts")
    if tp + fn == 0 or tn + fp == 0 or tp + fp == 0 or tn + fn == 0:
        raise ValueError("all sensitivity, specificity, PPV, and NPV denominators must be non-zero")

    sensitivity = tp / (tp + fn)
    specificity = tn / (tn + fp)
    sample_ppv = tp / (tp + fp)
    sample_npv = tn / (tn + fn)
    sample_prevalence = (tp + fn) / sum(counts)
    target = None
    if target_prevalence is not None:
        target = {
            "prevalence": target_prevalence,
            **predictive_values_at_prevalence(sensitivity, specificity, target_prevalence),
        }

    return {
        "sensitivity": {
            "estimate": sensitivity,
            "ci": wilson_interval(tp, tp + fn),
        },
        "specificity": {
            "estimate": specificity,
            "ci": wilson_interval(tn, tn + fp),
        },
        "sample": {
            "prevalence": sample_prevalence,
            "ppv": {
                "estimate": sample_ppv,
                "ci": wilson_interval(tp, tp + fp),
            },
            "npv": {
                "estimate": sample_npv,
                "ci": wilson_interval(tn, tn + fn),
            },
        },
        # Point estimates only: see the uncertainty boundary below before reporting.
        "target_scenario": target,
        "lr_positive": float("inf") if specificity == 1 else sensitivity / (1 - specificity),
        "lr_negative": float("inf") if specificity == 0 else (1 - sensitivity) / specificity,
    }
```

## Target-prevalence transport boundary

- A target-setting PPV/NPV assumes that sensitivity and specificity transport to the target
  population's spectrum, setting, threshold, and verification process. A prevalence substitution
  does not repair spectrum bias, referral bias, partial verification, calibration drift, or dataset
  shift.
- The code returns point estimates for the target scenario. Do **not** attach the sample PPV/NPV
  Wilson intervals to them. Propagate uncertainty in sensitivity, specificity, and—when estimated—
  target prevalence using a justified joint bootstrap, posterior draws, or another method that
  respects the study design and clustering.
- PPV is undefined when no positive classifications are possible, and NPV is undefined when no
  negative classifications are possible. The example raises an explicit error for either degenerate
  classifier instead of returning a divide-by-zero artifact.
- If target prevalence is uncertain or varies by pathway, report a pre-specified plausible range or
  several decision-relevant scenarios. Label the prevalence source, population, period, and whether
  it was fixed or estimated. These scenarios are transported estimates, not new validation data.

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
specificity was 0.79 (95% CI: 0.73, 0.84; 158/200). The enriched evaluation sample prevalence
was 42.7% (149/349). Assuming sensitivity and specificity transport to the intended setting,
Bayes-standardised PPV and NPV at the pre-specified 27% target-prevalence scenario were 0.61 and
0.94, respectively; uncertainty in performance and target prevalence must be propagated before
inferential reporting. The model and radiologists differed in sensitivity (P = .02, paired
McNemar test)."*

## Reviewer hot-spots
Threshold chosen on the test set; PPV/NPV quoted from an enriched sample as if clinical;
independence assumed for clustered lesions; missing CIs; "accuracy" headline hiding poor
sensitivity at clinical prevalence.
