# IBSI — making radiomic features reproducible

The **Image Biomarker Standardisation Initiative** (Zwanenburg et al.) standardises (1)
radiomic **feature definitions/nomenclature** and (2) the **image-processing pipeline**, so
that "GLCM contrast" means the same thing across software. _Radiology_-grade radiomics must
be **IBSI-compliant and explicitly reported**; "we used PyRadiomics defaults" is not enough.

## Two IBSI chapters
- **IBSI 1** — feature nomenclature + reference values for ~169 features and the standard
  processing chain (validated against digital phantoms).
- **IBSI 2** — standardisation of **image filters / convolutional filters** (e.g. Laplacian
  of Gaussian, wavelets, Laws) used before feature extraction.

## What to report (the IBSI-aligned processing chain)
1. **Image type & conversion** — modality; for CT report HU; for MR/PET state intensity
   units and any **standardisation** (MR has arbitrary units → normalise; PET → SUV).
2. **Interpolation / resampling** — target voxel size (isotropic?), interpolation algorithm
   (e.g. trilinear, B-spline), and how ROI masks are resampled.
3. **Re-segmentation / intensity clipping** — range (e.g. CT HU window) and partial-volume
   handling.
4. **Discretisation** — **fixed bin width** vs **fixed bin count** — *state which and the
   value*. This single choice changes texture features dramatically; report and justify;
   keep consistent across the cohort and (for MR/PET) appropriate to intensity scale.
5. **Filters (IBSI 2)** — any LoG sigma, wavelet family/levels, etc., with parameters.
6. **Feature families extracted** — first-order, shape, GLCM, GLRLM, GLSZM, GLDZM, NGTDM,
   NGLDM; report aggregation method (2D/2.5D/3D, how directional matrices are merged).
7. **Software + version + IBSI compliance** — name the tool (PyRadiomics, LIFEx, MIRP,
   CERR, etc.), its version, and which IBSI features it has been validated against.

## Reproducibility add-ons reviewers expect
- **Segmentation reproducibility** — multiple segmenters or perturbation; keep features with
  **ICC above a pre-specified threshold** (commonly ≥ 0.75–0.90); report how many were
  dropped.
- **Test–retest / phantom repeatability** where available (also scores on RQS).
- **Scanner/protocol harmonisation** — ComBat (or equivalent), fit on **training only**;
  report covariates preserved (e.g. biological signal) vs. removed (batch).
- **Provide feature definitions / parameter file** (e.g. the PyRadiomics `.yaml`) and the
  **extracted feature values** as supplementary data.

## Quick audit checklist
`HU/SUV/intensity units reported? · resampling stated? · discretisation type+value stated? ·
filters parameterised? · feature families + aggregation stated? · software+version+IBSI
compliance? · segmentation ICC + filtering threshold? · harmonisation method + train-only fit?
· feature file / values shared?`

Any "no" is a reproducibility gap; the most common Blocker is **unstated discretisation** and
**no segmentation ICC**.
