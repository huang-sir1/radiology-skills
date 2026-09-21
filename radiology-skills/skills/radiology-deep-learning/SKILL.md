---
name: radiology-deep-learning
description: "Design/train/audit imaging DL pipelines, splits, tuning and validation; not deployment studies."
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
- **Validation must match the claim.** Freeze the pipeline before evaluation. Internal patient-level
  resampling can support bounded development or feasibility claims; temporal, geographic, external,
  or deployment claims require a genuinely untouched population representing that transport step
  (→ radiology-design/validation-strategy).
- **Report fit-for-purpose performance.** Include uncertainty and failure cases. Use calibration for
  probabilistic predictions and decision-analytic utility only when a real decision and threshold
  range are defined (→ radiology-stats).
- **Select trustworthiness analyses by risk and use.** Interpretability, predictive uncertainty,
  OOD/robustness and fairness analyses are required when they answer a named failure mode, support a
  proposed use, or are part of a foundation/deployment evaluation; do not add them as ceremonial
  high-impact-journal checkboxes (→ `interpretability-uncertainty.md`).
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
| [references/foundation-model-data-genealogy-and-privacy.md](references/foundation-model-data-genealogy-and-privacy.md) | Pretraining sources are reused, closed or uncertain; audit patient/derivative overlap, contamination wording, memorisation/privacy threats, provider retention or federated leakage |
| [references/experiment-and-model-card.md](references/experiment-and-model-card.md) | Freezing experiment provenance, model/data cards, run manifests, negative results, test-set access, compute/environment, or a final reproducibility package |

## Workflow

1. **Confirm the design** (reuse `radiology-design`) — task, endpoint, unit (patient-level),
   cohorts, validation type, realistic capacity given n.
2. **Choose architecture** (architecture-choice.md) — dimension, family, task head; justify
   capacity vs cohort size; pick the **baseline(s)** to beat.
3. **For foundation/trustworthy-AI designs**, open `foundation-models-trustworthy-ai.md` and, when
   pretraining sources are reused, closed or uncertain,
   `foundation-model-data-genealogy-and-privacy.md`. Specify the overlap-evidence state,
   adaptation, baseline ladder, calibration, UQ, XAI stability, OOD/robustness, equity/fairness,
   privacy threat model, and shortcut/confounder audits.
4. **Define inputs** (multimodal-inputs.md) — channels/crops/fusion; missing-modality rule;
   leakage-safe use of masks and clinical/text/molecular data.
5. **Set training** (training-protocol.md) — transfer/SSL/scratch, patient-level splits,
   augmentation, imbalance handling, loss/optimizer/schedule, nested-CV hyperparameter search,
   seeds, checkpoint selection (on validation, never test).
6. **Validate** — use patient-level internal evaluation and add temporal/geographic/external
   evaluation when the intended claim requires that transport step; keep the pipeline frozen and
   report claim-relevant performance, uncertainty and **failure cases** (→ radiology-stats).
7. **Run justified trustworthiness analyses** (interpretability-uncertainty.md) — name the failure
   mode or decision each XAI/UQ/OOD/robustness analysis addresses, choose a method matched to the
   architecture, and report bounded results rather than only flattering examples.
8. **Freeze experiment provenance** (`experiment-and-model-card.md`) — data/split manifest,
   configurations, seeds, compute/environment, checkpoint rule, test-access log, model card,
   failure/negative-result log, and deviations.
9. **Audit leakage** (dl-leakage-audit.md) and **write Methods** to CLAIM 2024.

## Output contract

1. **`Model design`** — architecture, task head, capacity rationale, baseline(s).
2. **`Input spec`** — how each modality enters; fusion point; missing-modality handling.
3. **`Training protocol`** — pretraining strategy, splits, augmentation, imbalance, loss/optim/
   schedule, hyperparameter search, seeds, checkpoint rule — reproducibly.
4. **`Validation plan`** — internal evaluation plus any claim-required transport evaluation;
   fit-for-purpose metrics, uncertainty and failure cases.
5. **`Interpretability & uncertainty`** — when justified, the named risk/use, method, parameters,
   quantitative check, and bounded claim it supports (→ interpretability-uncertainty.md).
6. **`Trustworthiness modules`** — for foundation/VLM/deployment-grade models: calibration,
   UQ, OOD/fairness, XAI stability, shortcut/confounder audit, pretraining-overlap state and a
   use-specific privacy threat model; do not infer fairness from subgroup AUC alone.
7. **`Leakage audit`** — pass/fail per item + fix.
8. **`Experiment/model record`** — data/split/run manifests, model card, configuration and
   checkpoint provenance, environment/compute, negative results, and deviations actually available.
9. **`Table handoff`** — baseline/ablation/performance/calibration/fairness value keys and
   configuration rows for `radiology-table`.
10. **`Methods paragraph`** — CLAIM-aligned prose (+ 待确认 for Chinese authors).

## Quality bar

A good DL design is reproducible from the protocol, splits at the patient level, beats a fair
baseline, freezes the pipeline before claim-matched evaluation, and reports relevant uncertainty
and failure cases — not a single AUC from a slice-level split.

## Handoffs

- Series/phase/sequence qualification, acquisition/reconstruction, quantitative transforms,
  artifacts, dose, phantom/test-retest and protocol drift → `radiology-acquisition-qc`; consume its
  accepted-image gate and deviations before training/evaluation.
- Hand-crafted feature comparison / deep-feature extraction context → `radiology-radiomics`.
- Segmentation/detection ground-truth mask SOP and reader reproducibility → `radiology-annotation`.
- CLAIM/TRIPOD+AI audit, FUTURE-AI/TRIPOD-LLM edge cases → `radiology-reporting`.
- Metrics, CIs, DeLong, calibration, MRMC, sample size → `radiology-stats`.
- Hyperparameter/configuration sensitivity, matched benchmark fairness, component ablation,
  seed/run failure boundaries and efficiency evidence → `radiology-method-evaluation`; this skill
  still owns model/training implementation.
- Validation-type design (external/temporal/multi-center) → `radiology-design`.
- Biological interpretation of deep features → `radiology-radiogenomics`.
- Reader study / prospective deployment / monitoring for drift → `radiology-translation`.
- Figures (architecture, ROC, calibration, Grad-CAM, uncertainty plots) → `radiology-figure`.
- Tables (performance, ablation, subgroup/fairness, hyperparameters, failure cases) →
  `radiology-table`.
- Reframing this as a funding proposal instead of / alongside a paper → `radiology-grant`.
- Full-project state, provenance, and cross-artifact consistency → `radiology-pipeline`.
