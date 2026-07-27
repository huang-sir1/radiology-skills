---
name: radiology-foundation-models
description: "Use when an imaging study must select, adapt, fine-tune, or audit a pretrained medical imaging or vision-language foundation model. Covers zero-shot evaluation, linear probing, full fine-tuning, adapters, LoRA and other parameter-efficient tuning, prompt learning, domain adaptation, 2D/3D and image-text inputs, frozen tests, strong baselines, compute reporting, calibration, uncertainty, subgroups, and external validation. Warns against training a foundation model from scratch without adequate scale."
---

# Foundation-Model Adaptation for Medical Imaging

Use this skill when a model with broad pretraining intended for adaptability across tasks is central
to selection, adaptation, benchmarking, or audit. Treat it as a checkpoint with a specific
pretraining history, input contract, and license—not as automatic evidence of robustness or
clinical validity.

## Core stance

- Audit the model card, checkpoint, license, pretraining sources, deduplication, and possible
  evaluation overlap before adaptation.
- Match modality, anatomy, dimensionality, channels/sequences, text interface, spatial resolution,
  task, and prediction-time inputs before considering model size.
- Climb a prespecified adaptation ladder from the least trainable valid route. Include continued
  self-supervised or domain-adaptive pretraining only when authorized in-domain unlabeled data and
  a direct fine-tuning baseline make its added value testable.
- Separate every patient and all of that patient's repeated examinations, lesions, slices, patches,
  or frames across development and evaluation. Choose site-held-out or temporal separation when the
  transportability estimand requires it; a same-site internal test is valid when clearly labeled.
- Compare against strong task-specific and conventional transfer-learning baselines using identical
  eligible cohorts, split assignments, prediction-time information, and fair tuning rules.
- Report calibration, uncertainty or abstention, clinically relevant subgroups, external
  validation, compute, reproducibility, checkpoint identity, and license.
- Bound claims to the tested task, population, comparator, adaptation route, and validation domain.

## Required intake

Collect the intended use, endpoint, unit of analysis, reference standard, target population,
modality and input geometry, prediction-time inputs, paired text or prompts, cohort/site/time
structure, repeated measures, candidate model cards/checkpoints/licenses, pretraining sources,
labels/events, compute constraints, baselines, and validation material. Mark unknown pretraining
overlap, prompt provenance, incompatible licenses, and unavailable frozen tests as unresolved risks.

## When to open extra files

| File | Open when |
|---|---|
| [references/adaptation-strategies.md](references/adaptation-strategies.md) | Choosing or comparing zero-shot, linear probing, partial/full tuning, adapters, LoRA, prompt learning, continued pretraining, or domain adaptation; specifying text or spatial prompts |
| [references/evaluation-and-reporting.md](references/evaluation-and-reporting.md) | Auditing overlap/leakage, selecting patient/site/time splits, setting fair baselines and budgets, or reporting calibration, uncertainty, subgroups, external validation, compute, carbon, checkpoints, and licenses |

## Compact workflow

### 1. Define the estimand and model class

State the population, prediction time, available input, output, reference standard, intended use,
unit, and primary metric. Confirm that each candidate has broad pretraining intended to support
adaptability across tasks. Route a narrow single-task pretrained backbone and ordinary transfer
learning to `radiology-deep-learning`.

### 2. Audit provenance and compatibility

Record architecture, checkpoint/hash, license, objective, pretraining modalities and sources,
deduplication, intended use, limitations, and input contract. Match these to the downstream
modality, anatomy, 2D/3D/temporal structure, text or prompt interface, and output. Classify each
evaluation cohort as **overlap excluded**, **overlap removed**, **model-exposed**, or
**overlap unknown**.

### 3. Lock the adaptation ladder

Include only valid rungs and justify exclusions:

1. native zero-shot or prompt-based inference;
2. frozen encoder with a linear or shallow probe;
3. partial tuning;
4. adapters, LoRA, prompt learning, or other parameter-efficient tuning;
5. full fine-tuning;
6. continued self-supervised/domain-adaptive pretraining followed by downstream adaptation;
7. explicit domain adaptation for a prespecified source-target shift.

Define trainable components, prompts, objective, preprocessing, optimizer, tuning space, stopping,
seeds, and checkpoint selection before test access. Use
[adaptation strategies](references/adaptation-strategies.md) for route-specific controls.

### 4. Freeze development and evaluation boundaries

Split by patient and keep all repeated or nested observations together. Let the estimand determine
whether evaluation is same-site internal, temporal, site-held-out, or fully external; label it
accurately. Fit preprocessing, prompt selection, representation pooling, calibration, and
thresholds using authorized development data only. Keep the final test sealed until the pipeline
is locked.

### 5. Lock fair baselines and resources

Include a clinically meaningful comparator when available, a strong task-specific model,
conventional transfer learning, a frozen-feature baseline, and adaptation ablations needed to
isolate the contribution. Use identical patients, splits, outcomes, prediction-time inputs, and a
prespecified tuning-budget policy. Record actual parameters, trials, failures, hardware, memory,
runtime, accelerator-hours, energy/carbon method when available, software, seeds, and hashes.

### 6. Evaluate reliability and transportability

Report task-appropriate performance with confidence intervals and paired comparisons. Add
calibration and threshold behavior, uncertainty or abstention utility, prespecified subgroup and
site/scanner results, and external evaluation when transportability is claimed. Follow
[evaluation and reporting](references/evaluation-and-reporting.md) for exposure, split, compute,
checkpoint, and license disclosures.

### 7. Bound conclusions

State what the comparison supports and what remains untested. Retrospective metric improvement does
not establish generality, causal understanding, clinical utility, fairness, safety, or deployment
readiness. Unknown pretraining overlap prevents an unqualified independence claim.

## Output contract

Return the applicable sections:

1. **`Task and input contract`** — intended use, endpoint, unit, modality, geometry, and
   prediction-time inputs.
2. **`Model-card and overlap audit`** — foundation-model eligibility, provenance, license,
   compatibility, overlap class, and unresolved risks.
3. **`Adaptation ladder`** — included/excluded rungs, prompts, continued-pretraining objective,
   trainable components, budget, and rationale.
4. **`Frozen validation design`** — patient/repeated-measure separation, estimand-driven
   site/time choice, train-only operations, test label, and external cohort.
5. **`Baseline and budget table`** — comparators, identical inputs/splits, search policy,
   parameters, and compute.
6. **`Reliability evaluation`** — task metrics, uncertainty, calibration, subgroups, shifts, and
   external results or plans.
7. **`Reproducibility and release record`** — versions, hashes, seeds, hardware, runtime,
   energy/carbon, access, and licenses.
8. **`Bounded claims and missing inputs`** — supported conclusion, prohibited extrapolations,
   failure modes, and required information.

## Boundary, routes, and red lines

- Use this module only when broad pretrained-model adaptability, adaptation, or exposure is central.
  Route narrow single-task pretrained backbones, ordinary ImageNet transfer, CNN/Transformer design,
  optimization, task heads, and input pipelines to `radiology-deep-learning`.
- Route cohort design to `radiology-design`; performance inference to `radiology-stats`;
  annotation and reference standards to `radiology-annotation`; sharing and FAIR metadata to
  `radiology-data`; checklist audits to `radiology-reporting`; deployment and reader studies to
  `radiology-translation`; and evidence verification to `radiology-search`.
- Never split repeated observations from one patient across development and evaluation.
- Never call same-site internal evaluation external; do not require site or time separation when
  the estimand is internal performance.
- For promptable segmentation, never conceal whether points, boxes, or masks came from ground truth,
  a human, or an upstream model; oracle prompts are not deployable prompts.
- Never adapt on a frozen test set or call a model-exposed/unknown-overlap evaluation unqualified
  independent validation.
- Never call ordinary supervised fine-tuning a newly trained foundation model or recommend
  foundation-model training from scratch without commensurate scale, diversity, compute,
  governance, and validation.
- Never invent provenance, prompt effort, overlap checks, performance, compute, or validation.

This skill supports research design and audit, not patient-specific diagnosis, treatment advice,
or authorization to use restricted data or checkpoints.
