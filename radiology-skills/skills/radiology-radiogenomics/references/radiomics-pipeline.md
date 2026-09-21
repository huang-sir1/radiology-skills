# The imaging side — radiomics, deep features, and habitats

If the imaging features are not reproducible, every downstream gene association is noise.
Build this side to **IBSI/CLEAR** standard (cross-ref radiology-reporting).

The output of this pipeline is a reproducible **imaging phenotype**, not a biological mechanism.
Feature names, deep embeddings, saliency maps and habitats do not carry intrinsic tissue, cellular
or molecular meaning. When biology is part of the question, open `radiomics-mechanism-bridge.md`
after imaging QC and generate competing mechanisms plus discriminating evidence before selecting a
molecular analysis.

## 1. Segmentation
- Define the ROI (whole tumour, enhancing core, necrosis, peritumoural edema). For
  radiogenomics, the ROI should be **spatially meaningful** relative to the sampled tissue.
- Method (manual/semi/auto + software), number of segmenters, and **inter-/intra-observer
  ICC**; drop features with ICC below a pre-specified threshold (e.g. < 0.75–0.90).

## 2. Hand-crafted radiomics (IBSI-compliant)
- Report HU/SUV/MR-intensity handling, **resampling**, **discretisation (bin width vs count
  + value)**, filters, feature families, aggregation, software + version, IBSI compliance.
- See radiology-reporting/references/ibsi-features.md for the full checklist.

## 3. Deep features
- Pretrained or trained encoders produce embeddings. Report architecture, pretraining,
  layer, pooling. Beware: deep features are **less interpretable** and **more scanner-
  sensitive** — harmonise and validate.

## 4. Spatial **habitats** (the radiogenomics-specific move)
Tumours are heterogeneous; a single whole-tumour feature vector blurs biology. **Habitat
imaging** clusters voxels into sub-regions by their multi-parametric signature (e.g. ADC +
perfusion + T1c), yielding regions that can be matched to **regional** or **spatial** omics.

- Voxel-wise clustering (k-means/GMM) across co-registered sequences → habitat maps.
- Per-habitat radiomics, habitat volume fractions, and habitat adjacency/topology.
- Habitats align naturally with **spatial transcriptomics** and with **biopsy-localised**
  omics (single-cell-spatial.md).

## 5. Multi-parametric & multi-sequence registration
- Co-register sequences (rigid/deformable) before habitat clustering or feature fusion;
  report the registration method and QC. Misregistration creates spurious features.

## 6. Harmonisation (scanner/site)
- Radiomic features carry strong scanner/protocol signal. Treat harmonisation as an estimand- and
  deployment-dependent option, not a universal repair. Fit any learned transform without held-out
  outcomes and preserve declared biological covariates.
- A transform learned for **batch/site levels represented in training** may be frozen and applied to
  held-out samples from those seen levels when the implementation supports it. A wholly unseen
  external site has unknown batch parameters: standard ComBat/neuroCombat cannot be described as a
  frozen transform for that new level. Predefine an appropriate reference/frozen-harmonisation
  method, use a no-harmonisation/site-adjusted sensitivity route, or label external recalibration as
  adaptation rather than untouched validation.
- Show whether the target association survives the declared harmonisation and site sensitivities.

## 7. Feature QC before linkage
- Remove non-reproducible (low-ICC) and unstable features; optionally pre-filter by variance;
  log-transform/standardise as appropriate (fit on training).
- Carry forward a **documented, versioned** feature matrix (share it — CLEAR open-science).

## Reporting sentence
*"Tumours were segmented into enhancing, necrotic, and edematous sub-regions; voxel-wise
k-means on co-registered T1c/T2/ADC defined three habitats. [N] IBSI-compliant features per
region (PyRadiomics vX.Y) were filtered using the prespecified stability rule. [If actually used:
name the harmonisation implementation, covariates, training-only fit, represented batch levels and
the handling of any unseen external site.]"*
