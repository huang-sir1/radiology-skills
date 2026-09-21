# Foundation models and trustworthy AI in radiology

Use this reference when the user mentions foundation models, ViT, self-supervision, vision-language models, report generation, 3D/2D radiology models, uncertainty, explainability, causal robustness, or deployment-grade AI.

## Model family positioning

| Family | Best role | Reviewer's first question |
|---|---|---|
| CNN / U-Net / nnU-Net | Strong clinical baseline, segmentation, stable small-to-medium data model | Did you compare against this fairly? |
| ViT / Transformer | Pretrained visual encoder, long-range context, foundation-model adaptation | Is the data large enough or is pretraining justified? |
| Self-supervised model | Reduce label burden using unlabeled images, reports, temporal/multiview structure | Is the supervised baseline fair, and did test data leak into pretraining? |
| Vision-language model | Image-report alignment, report generation, VQA, weak supervision | Was evaluation clinically meaningful beyond NLP metrics? |
| 3D radiology foundation model | 3D CT/MRI and multimodal tasks | Does it work on real local multi-sequence/multi-protocol data? |
| Promptable segmentation model | ROI/mask generation, annotation acceleration, radiomics input improvement | Was segmentation quality audited for downstream task impact? |

## Practical architecture rules

- Small single-center cohorts: prefer transfer learning, linear probe, adapter/LoRA, or a simple CNN baseline. Avoid training large models from scratch.
- 3D MRI/CT radiogenomics: 3D context matters, but memory and sample size often force patching, 2.5D, pretrained encoders, or ROI/habitat summaries.
- Evaluate foundation-model adaptation against a prespecified strong baseline for the named benefit
  (for example transfer, label efficiency, robustness or workflow); journal acceptance is not a
  scientific endpoint and must not be predicted from architecture choice.
- Report pretraining-data knowledge state, frozen/fine-tuned layers, adaptation method,
  hyperparameter selection, and test-set isolation. Open
  [foundation-model-data-genealogy-and-privacy.md](foundation-model-data-genealogy-and-privacy.md)
  whenever pretraining sources are reused, closed or only partly disclosed.

## Trustworthiness modules

| Module | Minimum expectation | Stronger expectation |
|---|---|---|
| Calibration | calibration curve, intercept/slope or Brier where appropriate | site/subgroup calibration and recalibration plan |
| Uncertainty | MC dropout, ensembles, TTA, evidential, or conformal prediction | abstention/referral rule tied to human review |
| Explainability | Grad-CAM/attention/SHAP with bounded language | stability check, failure cases, agreement with ROI/pathology/reference standard |
| OOD/robustness | scanner/site/protocol subgroup performance | drift test, OOD detection, stress-test dataset |
| Fairness/equity | predeclared groupwise discrimination, calibration, error and missingness audit where lawful | affected-group input, representation/access/threshold/consequence estimands and mitigation evaluation through the equity gate |
| Causal/shortcut audit | identify plausible confounders and shortcuts | sensitivity analysis, site-aware model, causal graph, negative controls |

## Report-generation caution

For report generation or VLM tasks, do not rely only on text-overlap metrics. Add:

- clinical error taxonomy
- expert blinded preference or MRMC-style evaluation where possible
- finding-level metrics when appropriate
- workflow endpoint such as editing time, confidence, or error reduction

## Radiogenomics-specific warning

High performance on a molecular label does not prove a molecular mechanism. For imaging-genomics tasks:

- adjust or stratify by age, grade/stage, site, scanner, protocol, treatment exposure, and tumor volume where appropriate
- audit whether the model is predicting hospital/source artifacts or obvious clinical confounders
- interpret saliency or attention as hypothesis-generating unless supported by pathology, omics, pathway, or spatial evidence

## Data genealogy, contamination and privacy

- Apply the four-state pretraining-overlap contract in
  `foundation-model-data-genealogy-and-privacy.md`. A closed or incompletely documented corpus does
  not earn a `VERIFIED_NO_OVERLAP` claim.
- An external task cohort remains geographically or institutionally external when that is true, but
  unknown pretraining overlap must be disclosed as `CONTAMINATION_NOT_ASSESSABLE`; do not call the
  cohort completely unseen or untouched.
- Privacy and non-memorisation are separate from de-identification and research authorisation. Bind
  any privacy claim to a named adversary, access level, attack/evaluation and residual risk.
- Subgroup performance alone is not a fairness determination. Hand representation, access,
  differential consequences and affected-group decisions to the radiology-design equity gate.

## Output pattern

```text
Architecture choice:
Why this capacity matches the data:
Baseline ladder:
Pretraining/adaptation plan:
Trustworthiness modules:
Leakage/shortcut risks:
Clinical claim allowed:
```
