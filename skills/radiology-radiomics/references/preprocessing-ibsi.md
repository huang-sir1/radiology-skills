# Preprocessing to IBSI standard

Every preprocessing choice changes the features. Fix them a priori, apply uniformly, and report
to IBSI so the features are reproducible.

## Resampling (voxel size)

- Resample to a common voxel spacing (often isotropic, e.g. 1×1×1 mm) so texture features are
  comparable across scanners/protocols.
- Interpolator: image → B-spline/linear (state which); **mask → nearest-neighbour**.
- Report the target spacing and interpolators.

## Intensity normalisation / handling

| Modality | Typical handling |
|---|---|
| **CT** | HU are quantitative — usually no rescaling; may clip to a window (state it) |
| **MRI** | Intensities are **not** standardised — normalise (e.g. z-score, or histogram matching); state method |
| **PET** | Use SUV; state the SUV normalisation |

State whether normalisation is fit per-image or using training statistics (must not use test).

## Gray-level discretisation (the decision that moves every texture feature)

- **Fixed bin width** (e.g. 25 HU) — preserves intensity meaning; preferred for CT/PET by many.
- **Fixed bin count** (e.g. 32/64 bins) — fixes dynamic range; common for MRI.
- Choose **one**, state the value, justify, and keep it constant across all cases.
- Report both the bin parameter and the resulting effect (IBSI requires the discretisation
  method + value).

## Filters / image transforms

- LoG (state sigma), wavelet (state family/levels), square/exponential, etc.
- Each filter multiplies the feature count — declare which filters and account for multiplicity
  downstream (→ radiology-stats).

## Mandatory IBSI reporting (cross-ref radiology-reporting/ibsi-features.md)

- Image interpolation + resampled spacing.
- Intensity normalisation / re-segmentation range / outlier handling.
- Discretisation method + value (bin width or count).
- Filters + parameters.
- Feature aggregation (2D vs 3D, averaging across directions).
- Software + version + IBSI compliance statement.

## Reporting sentence

*"Images were resampled to 1×1×1 mm (B-spline; masks nearest-neighbour); CT intensities were
discretised with a fixed bin width of 25 HU. LoG (σ = 1,2,3 mm) and wavelet (Coiflet, 1 level)
filters were applied. Features were extracted in 3D with PyRadiomics vX.Y, IBSI-compliant."*
