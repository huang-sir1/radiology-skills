# 深度

Use this file for medical imaging deep learning, including classification, segmentation,
detection, prognosis, multimodal learning, foundation-model adaptation, explainability,
uncertainty quantification, OOD/robustness testing, and trustworthy-AI framing.

For detailed work, load `modules/radiology-deep-learning/SKILL.md`. If the request mentions
foundation models, ViT, self-supervision, VLM/report generation, uncertainty, explainability,
OOD, fairness, deployment-grade AI, or FUTURE-AI, open the detailed module instead of relying
on this concise reference.

## Workflow

1. Define task: diagnosis, detection, segmentation, staging, response, recurrence,
   survival, workflow triage, or report generation.
2. Define label source: pathology, expert annotation, registry, report-derived label,
   follow-up, molecular test, or weak label.
3. Define analysis unit: patient, study, series, image, slice, lesion, or voxel.
4. Split data by patient before augmentation, preprocessing that can leak, tuning, or
   model selection.
5. Specify architecture and input representation: 2D, 2.5D, 3D, video/sequence,
   transformer, CNN, hybrid, foundation model, or multimodal fusion.
6. Document preprocessing, augmentation, class imbalance, training schedule,
   hyperparameter search, seeds/folds, and compute environment.
7. Evaluate with test-set discipline, confidence intervals, calibration, subgroup
   performance, failure cases, and external validation when possible.
8. Add interpretability and uncertainty only with bounded claims: Grad-CAM/SHAP/attention
   can support plausibility checks, not biological proof; uncertainty must be calibrated
   and tied to a clinical or workflow action if it is claimed as useful.
9. For high-impact or deployment-facing studies, stress-test robustness, OOD behavior,
   shortcut learning, scanner/site shift, and fairness; use FUTURE-AI as a framing layer
   when discussing trustworthy AI.

## Model route choices

| Situation | Reasonable route |
|---|---|
| Small labeled cohort | Transfer learning, self-supervised pretraining, simpler baseline, nested CV |
| Many unlabeled scans | Self-supervised or foundation-model adaptation |
| Paired reports | Vision-language or report-supervised model, with label-noise audit |
| Segmentation masks limited | Weak/semi-supervised segmentation, active learning, reader QA |
| Multi-center shift | Domain generalization/adaptation plus site-held-out validation |
| Clinical deployment claim | Calibration, DCA, subgroup analysis, uncertainty, workflow endpoint |
| Foundation-model claim | Pretraining/adaptation details, baseline ladder, frozen external validation, shortcut audit |
| Trustworthy-AI claim | Explainability, uncertainty, robustness/OOD, fairness, traceability, and failure analysis |

## Reporting minimum

- dataset source, inclusion/exclusion, patient count, center count
- split method and patient-level grouping
- label definition and adjudication
- preprocessing and augmentation
- model architecture and initialization
- training settings and hyperparameter search
- comparison baselines
- performance metrics and uncertainty
- interpretability method and bounded interpretation
- uncertainty/OOD/robustness plan when clinical or high-impact claims depend on it
- external validation and subgroup analysis
- code/model/data availability where possible

## Red flags

- Slice-level random split.
- Test set used for model selection.
- No external validation but broad deployment language.
- No baseline comparison.
- No calibration while claiming decision support.
- Report-generated labels treated as gold standard without audit.
- Attractive Grad-CAM examples used as proof of mechanism.
- Uncertainty scores reported without calibration or any threshold-to-action rule.
- Foundation model mentioned without describing pretraining source, adaptation, and baselines.
