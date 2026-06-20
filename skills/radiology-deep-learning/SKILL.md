---
name: radiology-deep-learning
description: "Design and audit imaging deep-learning studies to Radiology (RSNA) / CLAIM 2024 standard — architecture choice (2D/2.5D/3D CNN, Transformer/ViT, segmentation/detection nets, prognostic models), transfer learning vs self-supervised pretraining vs training from scratch, how images/masks/clinical/text/molecular inputs enter the model, data splitting and augmentation, class imbalance, hyperparameter search, baselines, and external validation — with patient-level partition hygiene throughout. Use when the user plans or reviews a CNN/Transformer/3D/segmentation/detection/foundation/multimodal imaging model, mentions transfer learning, self-supervised, nnU-Net, ViT, data augmentation, class imbalance, or \"影像深度学习/深度学习模型\". Produces a model+training+validation design, a leakage audit, and Methods text. Never fabricates performance or training details."
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

## Workflow

1. **Confirm the design** (reuse `radiology-design`) — task, endpoint, unit (patient-level),
   cohorts, validation type, realistic capacity given n.
2. **Choose architecture** (architecture-choice.md) — dimension, family, task head; justify
   capacity vs cohort size; pick the **baseline(s)** to beat.
3. **Define inputs** (multimodal-inputs.md) — channels/crops/fusion; missing-modality rule;
   leakage-safe use of masks and clinical/text/molecular data.
4. **Set training** (training-protocol.md) — transfer/SSL/scratch, patient-level splits,
   augmentation, imbalance handling, loss/optimizer/schedule, nested-CV hyperparameter search,
   seeds, checkpoint selection (on validation, never test).
5. **Validate** — internal (patient-level CV) + external/temporal/geographic with the pipeline
   frozen; report discrimination, calibration, utility, **failure cases**, CIs (→ radiology-stats).
6. **Audit leakage** (dl-leakage-audit.md) and **write Methods** to CLAIM 2024.

## Output contract

1. **`Model design`** — architecture, task head, capacity rationale, baseline(s).
2. **`Input spec`** — how each modality enters; fusion point; missing-modality handling.
3. **`Training protocol`** — pretraining strategy, splits, augmentation, imbalance, loss/optim/
   schedule, hyperparameter search, seeds, checkpoint rule — reproducibly.
4. **`Validation plan`** — internal + external; metrics incl. calibration/utility + failure cases.
5. **`Leakage audit`** — pass/fail per item + fix.
6. **`Methods paragraph`** — CLAIM-aligned prose (+ 待确认 for Chinese authors).

## Quality bar

A good DL design is reproducible from the protocol, splits at the patient level, beats a fair
baseline, validates externally with the pipeline frozen, and reports calibration and failure
cases — not a single AUC from a slice-level split.

## Handoffs

- Hand-crafted feature comparison / deep-feature extraction context → `radiology-radiomics`.
- CLAIM/TRIPOD+AI audit → `radiology-reporting`.
- Metrics, CIs, DeLong, calibration, MRMC, sample size → `radiology-stats`.
- Validation-type design (external/temporal/multi-center) → `radiology-design`.
- Biological interpretation of deep features → `radiology-radiogenomics`.
- Reader study / prospective deployment → `radiology-translation`.
- Figures (architecture, ROC, calibration, Grad-CAM) → `radiology-figure`.
