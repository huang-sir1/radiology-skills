---
name: radiology-deep-learning
description: "Design and audit imaging deep-learning studies to Radiology (RSNA) / CLAIM 2024 standard, or to Nature-portfolio / FUTURE-AI trustworthy-AI standard — architecture choice (2D/2.5D/3D CNN, Transformer/ViT, segmentation/detection nets, prognostic models), transfer learning vs self-supervised pretraining vs training from scratch, how images/masks/clinical/text/molecular inputs enter the model, data splitting and augmentation, class imbalance, hyperparameter search, baselines, external validation, interpretability/explainability (Grad-CAM, SHAP, attention), uncertainty quantification (MC dropout, ensembles, conformal prediction), and robustness/OOD testing — with patient-level partition hygiene throughout. Use when the user plans or reviews a CNN/Transformer/3D/segmentation/detection/foundation/multimodal imaging model, mentions transfer learning, self-supervised, nnU-Net, ViT, data augmentation, class imbalance, explainability, uncertainty, robustness, or \"影像深度学习/深度学习模型\". Produces a model+training+validation design, a leakage audit, and Methods text. Never fabricates performance or training details."
---

# Imaging Deep-Learning Study Design

Use this skill to design (or audit) an imaging **deep-learning** study so it is reproducible,
honestly validated, and CLAIM-compliant. DL imaging papers get torn apart for slice-level
splits, patient overlap, test-set tuning, no external validation, and baselines that are too
weak to make "deep learning wins" mean anything. This skill encodes the architecture/training
choices and the partition hygiene reviewers enforce.

## Core stance

- **Patient-level everything.** Splits, augmentation, and any data-dependent step respect the
  patient boundary — slices/lesions/sequences/timepoints from one patient never span sets.
- **Right capacity for the data.** Small cohorts → transfer learning, self-supervised
  pretraining, strong simple baselines, heavy augmentation, and **nested CV** — not a giant model
  trained from scratch on 200 images.
- **Beat a real baseline.** "DL is better" needs a fair comparator: a radiomics/clinical model,
  a strong simpler network, or radiologists — tuned as carefully as the proposed model.
- **Inputs declared.** State exactly how images, masks, clinical variables, text, and molecular
  data enter the model (channels, crops, fusion point), and how missing modalities are handled.
- **External validation is the headline, not a footnote.** Internal CV alone is weak; freeze the
  pipeline and validate on an unseen site/period (→ radiology-design/validation-strategy).
- **Report calibration + utility**, failure cases, and CIs — not just AUC/Dice (→ radiology-stats).
- **Explain, quantify uncertainty, and stress-test.** A high-AUC model with no interpretability,
  no confidence estimate, and no robustness check is under-built for a high-impact venue — RQS 2.0
  (2025) scores explainability/fairness directly, and reviewers increasingly ask (→
  `interpretability-uncertainty.md`).
- **Integrity.** Never invent performance, training curves, or hyperparameters; mark what must be
  run.

## When to use

- "Design a CNN/Transformer/3D/segmentation/detection/prognostic imaging model." / "影像深度学习课题设计。"
- "Transfer learning vs self-supervised vs from scratch for my cohort size?"
- "How should images + clinical + pathology/text enter the model (multimodal fusion)?"
- "Augmentation, class imbalance, hyperparameter search, baselines — how to set up?"
- "Audit my DL Methods for slice-level leakage / patient overlap / test-set tuning."

## When to open extra files

| File | Open when |
|---|---|
| [references/architecture-choice.md](references/architecture-choice.md) | Choosing 2D/2.5D/3D CNN, Transformer/ViT, segmentation/detection/prognostic heads; foundation models; capacity vs cohort size |
| [references/training-protocol.md](references/training-protocol.md) | Transfer/SSL/from-scratch, splits, augmentation, class imbalance, loss/optimizer/schedule, hyperparameter search, checkpointing, seeds |
| [references/multimodal-inputs.md](references/multimodal-inputs.md) | How images/masks/clinical/text/molecular inputs enter the model; fusion strategies; missing-modality handling |
| [references/dl-leakage-audit.md](references/dl-leakage-audit.md) | The DL-specific leakage/validity checklist reviewers weaponise |
| [references/interpretability-uncertainty.md](references/interpretability-uncertainty.md) | Explainability (Grad-CAM/SHAP/attention) reported without overclaiming; uncertainty quantification (MC dropout, ensembles, conformal prediction); robustness/OOD testing; FUTURE-AI framing |
| [references/foundation-models-trustworthy-ai.md](references/foundation-models-trustworthy-ai.md) | Foundation models, ViT, SSL, VLM/report generation, 3D radiology models, adapter/LoRA, UQ/XAI/causal robustness, or deployment-grade trustworthy AI |

## Workflow

1. **Confirm the design** (reuse `radiology-design`) — task, endpoint, unit (patient-level),
   cohorts, validation type, realistic capacity given n.
2. **Choose architecture** (architecture-choice.md) — dimension, family, task head; justify
   capacity vs cohort size; pick the **baseline(s)** to beat.
3. **For foundation/trustworthy-AI designs**, open `foundation-models-trustworthy-ai.md`
   and specify pretraining/adaptation, baseline ladder, calibration, UQ, XAI stability,
   OOD/robustness, fairness, and shortcut/confounder audits.
4. **Define inputs** (multimodal-inputs.md) — channels/crops/fusion; missing-modality rule;
   leakage-safe use of masks and clinical/text/molecular data.
5. **Set training** (training-protocol.md) — transfer/SSL/scratch, patient-level splits,
   augmentation, imbalance handling, loss/optimizer/schedule, nested-CV hyperparameter search,
   seeds, checkpoint selection (on validation, never test).
6. **Validate** — internal (patient-level CV) + external/temporal/geographic with the pipeline
   frozen; report discrimination, calibration, utility, **failure cases**, CIs (→ radiology-stats).
7. **Explain + quantify uncertainty + stress-test** (interpretability-uncertainty.md) — pick a
   method matched to the architecture; report bounded, with failure cases, not only flattering
   examples.
8. **Audit leakage** (dl-leakage-audit.md) and **write Methods** to CLAIM 2024.

## Output contract

1. **`Model design`** — architecture, task head, capacity rationale, baseline(s).
2. **`Input spec`** — how each modality enters; fusion point; missing-modality handling.
3. **`Training protocol`** — pretraining strategy, splits, augmentation, imbalance, loss/optim/
   schedule, hyperparameter search, seeds, checkpoint rule — reproducibly.
4. **`Validation plan`** — internal + external; metrics incl. calibration/utility + failure cases.
5. **`Interpretability & uncertainty`** — method, parameters, quantitative check, and the bounded
   claim it supports (→ interpretability-uncertainty.md).
6. **`Trustworthiness modules`** — for foundation/VLM/deployment-grade models: calibration,
   UQ, OOD/fairness, XAI stability, shortcut/confounder audit.
7. **`Leakage audit`** — pass/fail per item + fix.
8. **`Methods paragraph`** — CLAIM-aligned prose (+ 待确认 for Chinese authors).

## Quality bar

A good DL design is reproducible from the protocol, splits at the patient level, beats a fair
baseline, validates externally with the pipeline frozen, and reports calibration and failure
cases — not a single AUC from a slice-level split.

## Handoffs

- Hand-crafted feature comparison / deep-feature extraction context → `radiology-radiomics`.
- Segmentation/detection ground-truth mask SOP and reader reproducibility → `radiology-annotation`.
- CLAIM/TRIPOD+AI audit, FUTURE-AI/TRIPOD-LLM edge cases → `radiology-reporting`.
- Metrics, CIs, DeLong, calibration, MRMC, sample size → `radiology-stats`.
- Validation-type design (external/temporal/multi-center) → `radiology-design`.
- Biological interpretation of deep features → `radiology-radiogenomics`.
- Reader study / prospective deployment / monitoring for drift → `radiology-translation`.
- Figures (architecture, ROC, calibration, Grad-CAM, uncertainty plots) → `radiology-figure`.
- Reframing this as a funding proposal instead of / alongside a paper → `radiology-grant`.
