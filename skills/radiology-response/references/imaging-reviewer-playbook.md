# Imaging-AI/radiomics reviewer playbook

The asks that recur in imaging-AI/radiomics/radiogenomics reviews, and how to respond
honestly.

| Reviewer ask | Honest response path |
|---|---|
| "No **external validation**." | Add an independent/temporal/geographic cohort if available (route: radiology-stats); if impossible, acknowledge as a limitation and soften claims — don't pretend internal CV is external. |
| "Possible **data leakage**." | Confirm patient-level split; show preprocessing/selection/harmonisation fit on training only; if a leak existed, re-run and report corrected results (radiology-radiogenomics/radiology-stats). |
| "Report **calibration / clinical utility**." | Add calibration (slope/intercept, plot) + decision-curve; do not substitute AUC (radiology-stats/figure). |
| "**Reader comparison** is weak." | Use MRMC (Obuchowski-Rockette/DBM) with reader-population inference; report difference + CI + test (radiology-stats). |
| "**Radiomics not reproducible** (IBSI?)." | State discretisation/resampling/filters, software+version, IBSI compliance, segmentation ICC, harmonisation; share the feature file (radiology-reporting/ibsi). |
| "**Sample size / overfitting**." | Give EPV/Riley rationale; show nested CV / optimism correction; limit features (radiology-stats). |
| "**Class imbalance / prevalence**." | Report prevalence; PPV/NPV at clinical prevalence; PR-AUC/sensitivity; avoid 1:1-sampled accuracy as if clinical. |
| "**Fairness/subgroups**." | Add pre-specified subgroup performance (TRIPOD+AI fairness). |
| "**Code/data not available**." | Deposit + cite (radiology-data); or justify restriction honestly. |
| "**Causation** overstated (radiogenomics)." | Soften to association; bound interpretation (radiology-polishing). |

## Difficult cases
- **Impossible/unreasonable experiment** — explain why (cost, ethics, data), offer the best
  feasible alternative, and acknowledge the limitation; don't claim it was done.
- **Reviewer factually wrong** — `DISAGREE_WITH_REASON`: cite evidence, stay courteous, and
  offer a clarifying edit so the next reader doesn't share the misunderstanding.
- **Conflicting reviewers** — reconcile to one defensible change; explain to both.
- **Pressure to overclaim** — never; keep claims bounded even if a reviewer invites more.
