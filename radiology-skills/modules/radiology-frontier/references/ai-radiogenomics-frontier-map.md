# AI and radiogenomics frontier map

Use this reference when the user asks what is worth doing in radiology AI or imaging-genomics over the next 12-24 months, especially when they have clinical imaging data and want a publishable direction rather than a generic hot-topic list.

## Field shift

The durable shift is:

```text
single-task / single-modality / single-center CNN
-> foundation models, self-supervision, vision-language, multimodal fusion
-> external validation, trustworthy inference, clinical value, and deployment evidence
```

Radiogenomics is shifting in parallel:

```text
handcrafted radiomics correlation
-> deep radiomics and hybrid radiomics + deep feature models
-> imaging + clinical + molecular + pathology fusion
-> mechanism-aware, externally validated, clinically bounded evidence
```

## Six frontier questions

Evaluate every proposed topic against these six questions:

| Question | What a good project must show | Weak version to avoid |
|---|---|---|
| Generalisability | External, temporal, geographic, multicenter, or federated validation | Random internal split presented as external |
| Supervision cost | SSL, weak labels, report supervision, or foundation-model transfer reduces labeling burden | No fair supervised baseline |
| Multimodal fusion | Imaging adds value beyond clinical/molecular/pathology alone, with missing-modality plan | Feature concatenation that underperforms the best single modality |
| Trustworthy inference | Calibration, UQ, XAI stability, OOD/failure analysis, subgroup performance | AUC only plus a decorative heatmap |
| External validation | Frozen pipeline performs on unseen site/time/protocol | Test-set tuning or re-fitting on validation data |
| Clinical-value evidence | Reader study, DCA, silent trial, workflow metric, or prospective endpoint | Retrospective AUC described as clinical readiness |

## Direction priority

| Priority | Direction | Best-fit data |
|---|---|---|
| 1 | Multicenter external validation with pre-defined endpoint | Any mature imaging-AI/radiomics project seeking top-tier credibility |
| 2 | Radiogenomics multimodal fusion | Matched imaging + clinical + molecular data, ideally with pathology or external validation |
| 3 | Foundation-model adaptation for 3D tumor tasks | 3D CT/MRI, limited labels, access to pretrained models, external testing |
| 4 | Uncertainty-aware / explanation-aware radiogenomics | Prediction tasks where abstention, failure analysis, and biological interpretability matter |
| 5 | Federated or distributed collaboration | Multiple institutions cannot share raw imaging/omics data |

## Disease areas with strong strategic fit

| Area | Why it fits | Common endpoints |
|---|---|---|
| Glioma | Multiparametric MRI, clear molecular labels, public/semipublic datasets, treatment relevance | IDH, MGMT, 1p/19q, grade, progression, survival |
| Lung cancer | Molecular status directly affects targeted/immunotherapy decisions | EGFR, ALK, KRAS, PD-L1, recurrence, response |
| Breast cancer | MRI/DBT/mammography/US can link with receptor status, subtype, NAC response, pathology | ER/PR/HER2, molecular subtype, pCR, recurrence |
| Prostate/liver/kidney/head-neck | Growing space when data and labels are strong | aggressiveness, subtype, treatment response, survival |

## Hot but often wrong

Reject or downgrade these ideas unless the data support them:

- Training a foundation model from scratch on a small local cohort.
- Claiming mechanism from saliency maps alone.
- Radiogenomics with no matched imaging-omics intersection count.
- Single-center high-AUC molecular prediction with no external validation.
- Report-generation study judged only by text-overlap metrics without expert error review.
- Multimodal fusion without showing incremental value over clinical/radiomics/deep baselines.

## Output pattern

When using this map, return:

```text
Direction:
Why it is frontier:
Data prerequisites:
Minimum publishable version:
Stronger 12-24 month version:
Main reviewer risk:
Live verification needed:
```

Concrete papers, dataset status, and regulatory facts must be verified with `radiology-search` before citation.
