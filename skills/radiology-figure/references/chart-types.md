# Choosing & parameterising the chart

Map the **message** to the chart; reviewers expect specific ones for specific claims.

| Message / claim | Chart | Must include |
|---|---|---|
| Discrimination of a classifier | **ROC** curve | AUC + 95% CI; diagonal; square aspect; (DeLong p if comparing) |
| Discrimination at clinical prevalence / imbalance | **Precision-Recall** | AUPRC; baseline = prevalence |
| Reliability of predicted risk | **Calibration** plot | diagonal; binned/loess curve; slope+intercept; histogram of predictions |
| Clinical usefulness | **Decision-curve (net benefit)** | treat-all / treat-none reference lines; sensible threshold range |
| Agreement (continuous) | **Bland-Altman** | bias + 95% limits of agreement; check proportional bias |
| Time-to-event | **Kaplan-Meier** | numbers-at-risk table; censoring ticks; log-rank p; HR+CI |
| Meta-analysis effect per study | **Forest** | per-study estimate+CI; pooled diamond; heterogeneity (I²) |
| DTA meta-analysis | **SROC** | summary point + confidence/prediction region; study points sized by n |
| Group comparison of a measure | **Box/violin + points** | show data points; n per group; test |
| Feature/sample structure | **Heatmap / clustermap** | clear colorbar with units; clustering method noted |
| Multi-omics latent structure | **Factor/loadings plot** | factor variance explained; top loadings |
| Cell-type composition | **Stacked bar** | fractions sum to 1; consistent cell-type colors |
| Patient selection | **CONSORT/STARD/PRISMA flow** | counts at each in/exclusion step |
| Confusion of classes | **Confusion matrix** | counts + row/col normalised option |

## Defaults to enforce
- **ROC**: don't smooth; plot empirical steps or a faithful curve; annotate operating point
  if one is chosen (and say where the threshold came from).
- **Calibration**: quantile bins (e.g. deciles) or loess; always show the prediction
  distribution (rug/hist) — a curve over empty probability ranges is misleading.
- **Decision curve**: clip y-axis sensibly; show treat-all and treat-none.
- **Kaplan-Meier**: numbers-at-risk is expected by _Radiology_; align time axis with the
  table.
- **Forest/SROC**: order studies meaningfully; show pooled estimate and heterogeneity.
- **Heatmap**: choose a perceptually-uniform or diverging map (center diverging maps at 0,
  e.g. z-scores); always label the colorbar.

## Comparison plots
When comparing models/readers, prefer **paired** visual encodings (same cases) and annotate
the **difference + CI + test** (DeLong for AUC). Send the statistic to `radiology-stats`.
