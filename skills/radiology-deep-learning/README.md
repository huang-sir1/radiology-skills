# radiology-deep-learning

**Stage 3 — Modeling & Analysis.** Design or audit imaging deep-learning studies to CLAIM 2024
standard — reproducible, patient-level, externally validated.

## What it does

- **Model design** — 2D/2.5D/3D CNN, Transformer/ViT, segmentation (U-Net/nnU-Net), detection,
  prognostic heads, foundation-model transfer; capacity matched to cohort size; a fair baseline
  to beat.
- **Input spec** — how images, masks, clinical variables, text, and molecular data enter the
  model; early/intermediate/late fusion; missing-modality handling; leakage traps (report-text,
  post-outcome variables).
- **Training protocol** — transfer/self-supervised/from-scratch, patient-level splits, nested CV,
  augmentation, class imbalance, loss/optimizer/schedule, hyperparameter search, seeds,
  checkpoint rule.
- **Leakage & validity audit** — partition, fit-on-training, tuning, input integrity, evaluation.
- **Methods paragraph** — CLAIM-aligned prose.

## Trigger examples

- "影像深度学习课题设计（CNN/Transformer/3D/分割/预后）。"
- "Transfer learning vs self-supervised vs from scratch for my cohort?"
- "Audit my DL Methods for slice-level leakage / patient overlap."

## Reference files

| File | Use |
|---|---|
| `references/architecture-choice.md` | Dimension, family, task head, capacity vs cohort |
| `references/training-protocol.md` | Pretraining, splits, augmentation, imbalance, tuning, seeds |
| `references/multimodal-inputs.md` | How modalities enter; fusion; missing-modality rule |
| `references/dl-leakage-audit.md` | The DL leakage/validity checklist |

## Handoffs

`radiology-radiomics` (feature comparison) · `radiology-reporting` (CLAIM/TRIPOD+AI) ·
`radiology-stats` (metrics, CIs, calibration, MRMC, sample size) · `radiology-design`
(validation type) · `radiology-radiogenomics` (deep-feature biology) ·
`radiology-translation` (reader study/prospective) · `radiology-figure` (architecture, ROC,
Grad-CAM).
