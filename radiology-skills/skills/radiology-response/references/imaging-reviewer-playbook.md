# Imaging-AI/radiomics reviewer playbook

The asks that recur in imaging-AI/radiomics/radiogenomics reviews, and how to respond
honestly.

| Reviewer ask | Honest response path and closure evidence |
|---|---|
| "No **external validation**." | Add a frozen-model independent/temporal/geographic test if available and report the result; if impossible, acknowledge the gap and soften every affected claim — don't rename internal CV as external. |
| "Possible **data leakage**." | Confirm patient-level split and train-only fitting of preprocessing/selection/harmonisation; if a leak existed, re-run, report corrected performance and propagate changes to all locations. |
| "Report **calibration / clinical utility**." | Add applicable calibration (slope/intercept and plot) and decision-curve evidence with results; do not substitute AUC or claim workflow benefit without utility evidence. |
| "**Reader comparison** is weak." | Use MRMC (Obuchowski-Rockette/DBM) with reader-population inference; report difference + CI + test (radiology-stats). |
| "**Radiomics not reproducible** (IBSI?)." | State discretisation/resampling/filters, software+version, IBSI compliance, segmentation ICC, harmonisation; share the feature file (radiology-reporting/ibsi). |
| "**Sample size / overfitting**." | Give EPV/Riley rationale; show nested CV / optimism correction; limit features (radiology-stats). |
| "**Class imbalance / prevalence**." | Report prevalence; PPV/NPV at clinical prevalence; PR-AUC/sensitivity; avoid 1:1-sampled accuracy as if clinical. |
| "**Fairness/subgroups**." | First establish subgroup relevance and adequate n; report estimates/uncertainty and failure cases rather than an unstable fishing exercise. |
| "**Code/data not available**." | Deposit + cite (radiology-data); or justify restriction honestly. |
| "**Causation** overstated (radiogenomics)." | Soften to association; bound interpretation (radiology-polishing). |

## Difficult cases
- **Impossible/unreasonable experiment** — explain why (cost, ethics, data), offer the best
  feasible alternative, and acknowledge the limitation; don't claim it was done.
- **Reviewer factually wrong** — `DISAGREE_WITH_REASON`: cite evidence, stay courteous, and
  offer a clarifying edit so the next reader doesn't share the misunderstanding.
- **Conflicting reviewers** — reconcile to one defensible change; explain to both.
- **Pressure to overclaim** — never; keep claims bounded even if a reviewer invites more.
- **Algorithm paper asks for benchmarks/ablations** — use current, applicable comparators with matched
  splits/tuning and an ablation that isolates the claimed contribution. A clinical association paper
  does not need ritual algorithmic ablations when no component-level novelty is claimed.
- **Only wording was changed after a validity concern** — mark `PARTIAL` or `NOT_FULFILLED` unless
  claim reduction genuinely removes the unsupported inference.
