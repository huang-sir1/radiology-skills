# 12-24 month AI/radiogenomics study roadmap

Use this reference when a team wants a realistic publication plan for radiology AI, deep radiomics, or radiogenomics rather than a one-off model. It is best for teams with access to clinical imaging and at least some labels, clinical variables, molecular data, or external collaborators.

## Strategic principle

Do not start with "let us build a big model." Start with:

```text
single disease -> one clinically meaningful endpoint -> frozen data definition
-> strong baseline ladder -> external validation -> trustworthy/clinical-value evidence
```

The strongest 12-24 month projects usually have:

- clear clinical question
- trustworthy label/reference standard
- public benchmark or comparator
- multi-center, temporal, or external validation path
- reporting-guideline route from day 1

## Recommended staged plan

| Time window | Goal | Expected outputs | Skills to route |
|---|---|---|---|
| 0-3 months | Define clinical problem, endpoint, reference standard, inclusion/exclusion, data dictionary, governance | Protocol, data-flow diagram, label SOP, draft SAP | `radiology-design`, `radiology-ethics`, `radiology-reporting` |
| 3-6 months | Build frozen research cohort, de-identification, split plan, imaging QC, segmentation/ROI pipeline | Cohort lock, QC report, baseline radiomics pipeline | `radiology-data`, `radiology-annotation`, `radiology-radiomics` |
| 6-9 months | Establish strong baselines: clinical model, IBSI radiomics, CNN/ViT or nnU-Net model | Reproducible baseline, internal test, failure-case library | `radiology-stats`, `radiology-deep-learning`, `radiology-figure` |
| 9-12 months | Add multimodal fusion and trustworthiness modules | First method paper draft; calibration/UQ/XAI; pre-external-test model card | `radiology-radiogenomics`, `radiology-deep-learning`, `radiology-writing` |
| 12-18 months | External/multicenter/temporal validation; site heterogeneity analysis; optional federated/split-learning prototype | External validation paper, center-effect analysis, model card | `radiology-design`, `radiology-stats`, `radiology-prereview` |
| 18-24 months | Silent deployment, reader-assist, workflow/time/error endpoint, or prospective validation preparation | Prospective/reader study, CLAIM/TRIPOD/STARD package, regulatory-readiness notes | `radiology-translation`, `radiology-reporting`, `radiology-journal` |

## Topic templates with high fit

| Template | Minimum viable design | Stronger version |
|---|---|---|
| Glioma MRI -> MGMT/IDH/1p19q | clinical + radiomics + deep baseline; patient-level split; external public or institutional test | radiopathomics or molecular/pathway fusion; UQ; survival/therapy-response endpoint |
| Lung CT -> EGFR/ALK/KRAS/PD-L1 | radiomics/deep hybrid with clinical variables; external center; calibration and DCA | multicenter fusion, pathology or genomics validation, reader/MDT decision study |
| Breast MRI/DBT/US -> subtype or NAC response | clinical + imaging model; pathology-confirmed endpoint; temporal validation | pathology/omics fusion, pCR/recurrence endpoint, reader-assist trial |
| Generic imaging foundation-model adaptation | pretrained encoder + fair task-trained baseline; external test | adapter/LoRA prompt tuning, site robustness, OOD/failure analysis |

## Baseline ladder

For high-impact claims, compare in this order where feasible:

1. Clinical-only model.
2. Conventional radiology variables/reader baseline.
3. IBSI-aligned radiomics model.
4. CNN/ViT/deep-feature model.
5. Hybrid radiomics + deep + clinical model.
6. Multimodal molecular/pathology/foundation-model fusion.

If the complex model does not beat a strong simpler baseline, shift the manuscript angle or simplify the model.

## Evidence ladder

| Evidence level | What it supports | What it does not support |
|---|---|---|
| Internal retrospective | Feasibility and method development | Clinical utility or broad generalization |
| Temporal/geographic/external retrospective | Generalisability under new site/time/protocol | Real-world workflow benefit |
| Reader-assist or silent deployment | Human-AI interaction, workflow, error/time endpoints | Autonomous use |
| Prospective clinical impact | Clinical utility in intended pathway | Unbounded use outside setting |

## Avoid these roads

- Single-center small-n AUC paper with no external validation.
- Model stacking without a clinical question or failure mechanism.
- Radiogenomics without a matched-n flow diagram.
- UQ/XAI added after results only as cosmetic panels.
- Foundation-model claim with no fair baseline or pretraining-leakage audit.

## Output pattern

```text
Recommended 12-24 month track:
Current starting point:
Binding constraint:
First paper:
Second paper:
External/prospective evidence path:
Resource gap:
Do-not-do list:
```
