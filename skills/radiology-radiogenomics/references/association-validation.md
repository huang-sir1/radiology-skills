# Association, enrichment, and validation

## 1. Feature ↔ molecular association (discovery)
- Continuous feature vs continuous expression: Spearman (robust) with **FDR** across the
  feature×gene grid; report rho + CI, not just p.
- Feature vs categorical label (mutation/subtype): rank-sum / logistic; effect size + CI.
- The test grid is large (features × genes) → **Benjamini-Hochberg / q-values**; pre-specify
  the primary phenotype (radiology-stats/high-dimensional-omics.md).

## 2. From genes to biology — enrichment
- **GSEA / ssGSEA / GSVA** on ranked gene lists or per-sample scores; **ORA** (hypergeometric)
  on a gene set. Use curated collections (MSigDB Hallmark, Reactome, GO).
- Report the collection, the ranking metric, FDR, and normalised enrichment scores.
- Per-sample pathway scores (ssGSEA/GSVA) can themselves be associated with imaging — often
  more stable than single genes.

## 3. Building a radiogenomic signature (prediction)
- If predicting a molecular label from imaging: this is a **prediction model** → TRIPOD+AI,
  calibration, decision-curve, and **external validation** (radiology-reporting, radiology-stats).
- Penalised / stability selection inside **nested CV**; report optimism-corrected performance
  and feature-selection frequency.

## 4. Validation (non-negotiable for _Radiology_)
- **Independent cohort** (another institution/dataset/time). Re-extract features with the
  *same* pipeline; apply the *frozen* model/harmonisation transform.
- Report whether the **association direction and effect size** replicate, not only the p-value.
- Where biology is claimed, orthogonal validation (IHC, an independent omics modality, or
  spatial corroboration) strengthens it.

## 5. Interpretation discipline
- Correlation is a **hypothesis**. Avoid mechanistic language unless supported. Distinguish
  "imaging reflects X biology" from "imaging causes/measures X."
- Multiple comparisons, small n, and batch effects all inflate apparent associations — state
  how each was handled.

## Reporting sentence
*"Across 1218 features × 18 421 genes, 312 feature–gene pairs were significant
(BH-FDR < 0.05); the leading axis enriched for hypoxia and EMT Hallmark sets (NES 2.1/1.9,
FDR < 0.01). A 12-feature elastic-net signature predicted the subtype with optimism-corrected
AUC 0.78 (nested CV) and AUC 0.74 (95% CI: 0.66, 0.82) in the independent cohort, with
concordant effect direction."*
