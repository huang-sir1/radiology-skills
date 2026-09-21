# Table archetypes

Choose the smallest table that answers the scientific question. Do not combine unrelated evidence
merely to reduce table count.

| Archetype | Required core | Frequent failure |
|---|---|---|
| Cohort characteristics / Table 1 | cohort columns, n, variable, summary, missingness | p values without purpose; totals disagree with flowchart |
| Diagnostic/model performance | cohort, model, metric, estimate, 95% CI, comparator/test | AUC alone; no calibration; mixed thresholds |
| Logistic/Cox regression | variable/level, reference, effect estimate, 95% CI, p value, adjustment set | univariable and multivariable labels blurred |
| Feature-selection audit | stage, rule, input count, retained count, train-only status | counts do not reconcile; leakage not visible |
| Signature/coefficient table | feature, transformed name, coefficient/weight, unit/scaling, stability | weights copied without preprocessing context |
| Reader/MRMC table | arm, readers/cases, outcome, estimate/CI, paired comparison | treating readers/cases as independent |
| Segmentation/agreement | target, readers, metric/model, estimate/CI | ICC model or Dice aggregation omitted |
| Deep-learning ablation | component/configuration, split, metric/CI, parameter/training parity | unfair tuning across variants |
| Radiogenomics association | imaging feature, gene/pathway/cell type, effect, CI, raw p, adjusted p/q | discovery and validation mixed; FDR family unclear |
| Dataset/scanner protocol | cohort/site, scanner/vendor/field strength, sequence/acquisition | patient counts or units absent |
| Hyperparameter/reproducibility | software/version, seed, preprocessing, search space, chosen value | test-set-selected choices |
| Supplementary inventory | item, purpose, source, manuscript callout | orphaned tables not cited in manuscript |

## Table 1 rules

- Define the unit: patients, lesions, examinations, or images.
- State summary statistics: mean (SD), median (IQR), or n (%), chosen from distribution and design.
- Report missing values by variable or state the missing-data policy.
- For development/validation comparisons, prefer standardized mean differences when balance is the
  question; do not make automatic p-value testing the table's purpose.
- Keep dates, center role, and event counts outside the body only when clearly stated in title/footnote.

## Main versus supplement

Main tables carry cohort identity, primary analysis, major comparator, and clinical interpretation.
Supplementary tables carry full feature lists, hyperparameters, extended subgroup/sensitivity results,
scanner details, and checklist support. A main claim must not depend on a supplementary table the text
never calls out.

