# Scope-aware multi-omics integration

When you have several molecular layers (RNA, DNA/mutation, methylation, protein) — possibly
plus imaging features — you can analyse them jointly. Choose a **strategy** first, then a
method.

Start from `study_scope`. In `mechanism-only`, integrate only the measured molecular, pathology,
clinical or perturbational views that exist. In `imaging-mechanism`, imaging may be one view, but
patient/lesion/region/time compatibility must be established before fusion. Do not add a synthetic
imaging block to make a standalone study look multimodal.

Before choosing a method, define the independent unit, paired versus unpaired views, missing-view
pattern, preprocessing boundary, primary claim branch and held-out validation domain. Integration
does not increase biological n or repair non-overlapping specimens.

## Fusion strategies
- **Early (concatenation)** — stack all features into one matrix. Simple, but scale/
  dimensionality imbalance dominates; needs strong regularisation and block-scaling.
- **Intermediate (joint latent factors)** — learn a shared low-dimensional structure across
  views. Usually the best for discovery and interpretability.
- **Late (ensemble)** — model each view, combine predictions. Robust when views are
  redundant; loses cross-view interactions.

## Methods (unsupervised / discovery)
| Method | Idea | Tool |
|---|---|---|
| **MOFA / MOFA+** | Bayesian group factor analysis → interpretable latent factors, handles missing views | `MOFA2` (R/Python) |
| **iCluster / iClusterPlus / iClusterBayes** | joint latent clustering for subtype discovery | `iClusterPlus` (R) |
| **SNF** (Similarity Network Fusion) | fuse per-view patient-similarity networks | `SNFtool` (R) |
| **Joint NMF / intNMF** | non-negative joint factorisation | `intNMF` |
| **MultiVI / totalVI** | deep generative multi-omics (esp. single-cell) | `scvi-tools` |
| **Mowgli** | NMF + optimal transport for paired single-cell multi-omics integration (Nat Commun 2023;14:7890) | `mowgli` (Python) |

## Methods (supervised / toward an outcome)
| Method | Idea | Tool |
|---|---|---|
| **DIABLO** (mixOmics) | supervised multi-block discriminant analysis; selects correlated multi-omic signatures | `mixOmics` (R) |
| **Multi-block PLS / sparse CCA** | covariation between blocks (e.g. imaging ↔ expression) | `mixOmics`, `PMA` |
| **Group/sparse-group LASSO** | penalised prediction with block structure | `glmnet`, `SGL` |

## Where imaging fits — only when imaging is active
- Treat **imaging features as one view/block**. Sparse CCA / DIABLO are natural for
  "which imaging features co-vary with which genes/pathways."
- MOFA factors that load on **both** imaging and expression are the interpretable
  radiogenomic axes you want.

In `mechanism-only`, use the same logic for molecular–molecular or molecular–pathology blocks and
describe factors as cross-view covariation. Do not call a latent factor a mechanism unless a named
link is tested with scale-compatible orthogonal or perturbational evidence.

## Discipline
- **Scale/normalise per block**; control multiplicity; **fit integration on training**, apply
  to validation.
- Interpret factors/components with loadings + enrichment (GSEA on the gene loadings).
- Don't over-cluster: validate subtypes (silhouette, consensus clustering, and an external
  cohort).
- Compare the integrated model with every single-view model and a simple concatenation/clinical
  baseline; otherwise the added view has no demonstrated value.
- Report view-specific missingness, whether samples are paired at the biological-unit level, factor/
  component stability, tuning performed, and which operations saw validation data.
- Separate association or prediction from treatment-effect, mechanistic and causal claims.

## Reporting sentence skeletons

- `mechanism-only`: *"[RNA/protein/methylation] views from [N] independent [units] were integrated
  with [method] after view-specific QC. Factor [X] showed stable loadings on [programs] and its
  association with [endpoint] was evaluated in [validation domain]; this supports cross-view
  covariation rather than causal mechanism."*
- `imaging-mechanism`: *"Region/time-compatible [imaging] and [molecular] views from [N] matched
  independent units were integrated with [method]. Factor [X] loaded on [imaging phenotype] and
  [molecular program]; the frozen association was tested in [validation cohort/system]."*
