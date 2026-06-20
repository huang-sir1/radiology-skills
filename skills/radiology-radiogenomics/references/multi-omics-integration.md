# Multi-omics integration (with imaging as a view)

When you have several molecular layers (RNA, DNA/mutation, methylation, protein) — possibly
plus imaging features — you can analyse them jointly. Choose a **strategy** first, then a
method.

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
| **MultiVI / totalVI / Mowgli** | deep generative multi-omics (esp. single-cell) | `scvi-tools` |

## Methods (supervised / toward an outcome)
| Method | Idea | Tool |
|---|---|---|
| **DIABLO** (mixOmics) | supervised multi-block discriminant analysis; selects correlated multi-omic signatures | `mixOmics` (R) |
| **Multi-block PLS / sparse CCA** | covariation between blocks (e.g. imaging ↔ expression) | `mixOmics`, `PMA` |
| **Group/sparse-group LASSO** | penalised prediction with block structure | `glmnet`, `SGL` |

## Where imaging fits
- Treat **imaging features as one view/block**. Sparse CCA / DIABLO are natural for
  "which imaging features co-vary with which genes/pathways."
- MOFA factors that load on **both** imaging and expression are the interpretable
  radiogenomic axes you want.

## Discipline
- **Scale/normalise per block**; control multiplicity; **fit integration on training**, apply
  to validation.
- Interpret factors/components with loadings + enrichment (GSEA on the gene loadings).
- Don't over-cluster: validate subtypes (silhouette, consensus clustering, and an external
  cohort).

## Reporting sentence
*"MRI-habitat radiomics and RNA-seq were integrated with MOFA+ (10 factors); Factor 3 loaded
on rim-enhancement texture and a hypoxia gene module (GSEA FDR < 0.05) and separated survival
groups, replicated in the validation cohort."*
