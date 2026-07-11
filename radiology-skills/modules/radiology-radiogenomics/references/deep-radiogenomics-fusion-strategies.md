# Deep radiogenomics fusion strategies

Use this reference when a radiogenomics project goes beyond handcrafted radiomics and needs deep features, foundation-model embeddings, pathology, molecular layers, clinical variables, or pathway constraints.

## First principle

The best current radiogenomics designs are rarely "image only" or "omics only." They define a clinical/molecular endpoint and compare a baseline ladder:

```text
clinical model
-> IBSI radiomics
-> deep image features
-> hybrid radiomics + deep + clinical
-> imaging + molecular/pathology/clinical fusion
```

## Fusion strategy menu

| Strategy | Use when | Strength | Watch-out |
|---|---|---|---|
| Early fusion | Matched modalities are complete and n is modest | Simple, interpretable, easy to benchmark | High-dimensional overfitting |
| Late fusion / stacking | Each modality has a useful standalone model | Robust for small n and missing modalities | Weak cross-modal interaction |
| Joint embedding / cross-attention | Enough matched cases and meaningful interactions expected | Learns imaging-omics/pathology interactions | Sample hungry; alignment quality critical |
| Graph/pathway-informed fusion | Gene pathways, patient similarity, spatial/habitat structure matter | Adds biological priors and interpretability | Reproducibility and pathway choice can be challenged |
| Radiopathomics / cross-scale fusion | Matched radiology + WSI/pathology available | Strong bridge from image phenotype to tissue biology | Spatial and time mismatch; WSI preprocessing burden |
| Foundation-model embeddings + adapter | Small task labels but strong pretrained image/pathology/text models available | Efficient and publishable if externally validated | Must rule out pretraining leakage and weak baselines |

## Disease-specific high-yield endpoints

| Disease | Imaging | Molecular/clinical endpoint | Design note |
|---|---|---|---|
| Glioma | multiparametric MRI | IDH, MGMT, 1p/19q, grade, survival, progression | Strong public-resource ecosystem; sample-to-image mapping and treatment timing matter |
| Lung cancer | CT/PET-CT | EGFR, ALK, KRAS, PD-L1, response, recurrence | High clinical appeal; need external validation across scanners/protocols |
| Breast cancer | MRI, DBT, mammography, US | ER/PR/HER2, subtype, pCR, recurrence | Good clinical story if linked to NAC response or decision pathway |
| Prostate/liver/kidney/head-neck | mpMRI/CT/PET | aggressiveness, subtype, response, survival | Growing space; stronger if tied to treatment decision |

## Minimum viable paper

A credible paper should include:

- matched-cohort flow diagram with imaging, omics/pathology, intersection, exclusions, and validation
- clinical-only and radiomics/deep baselines
- train-only feature selection and hyperparameter tuning
- external/temporal validation or a clearly bounded feasibility claim
- calibration and subgroup/site/scanner error analysis for predictive tasks
- biological interpretation calibrated as association unless pathway/spatial/pathology evidence supports more

## Stronger paper

A high-tier version adds:

- multicenter or public external cohort
- radiopathomics or pathway-informed fusion
- UQ/XAI integrated into the model or decision rule
- model card and source-data/code availability plan
- silent deployment, reader-assist, or clinical utility endpoint when a clinical claim is made

## Small-n guardrails

For small paired imaging-omics cohorts:

- keep the primary hypothesis narrow
- reduce feature space before modeling with train-only rules
- use penalized models, nested CV, and external validation if at all possible
- avoid deep end-to-end multimodal models unless pretrained embeddings are used and baselines are strong
- report uncertainty and instability honestly

## Claim language

| Evidence | Safer claim |
|---|---|
| Internal association only | imaging phenotype was associated with molecular feature |
| Internal prediction only | model showed feasibility for predicting molecular status |
| External validation | model generalized to an independent cohort |
| Pathway/spatial/pathology support | findings suggest biologically plausible imaging-molecular linkage |
| Prospective/reader utility | model may support a defined clinical workflow under radiologist oversight |

Never say that imaging replaces molecular testing unless a prospective clinical utility study and regulatory pathway support that claim.
