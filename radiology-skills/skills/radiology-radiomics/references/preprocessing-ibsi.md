# Preprocessing to IBSI standard

Every preprocessing choice changes the features. Fix it a priori, apply it without test/outcome
leakage and report it using IBSI definitions. IBSI conformance is a definition/configuration and
reporting contract; it is not proof of implementation equivalence or empirical repeatability on the
study's segmentations, scans, scanners and protocols.

## Resampling (voxel size)

- Resampling may place images on a common computational grid; it does **not** make scanners,
  reconstructions, slice profiles or protocols biologically/technically equivalent. Interpolation
  can itself change intensity and texture.
- Choose target spacing from the native-spacing distribution, smallest relevant anatomy/lesion,
  task and interpolation error—not from a universal isotropic default. When the claim depends on
  spacing, preserve a native/raw or task-justified primary analysis and add prespecified spacing and
  interpolation sensitivity analyses.
- Interpolator: image → B-spline/linear (state which); **mask → nearest-neighbour**.
- Report the target spacing and interpolators.

## Intensity normalisation / handling

| Modality | Typical handling |
|---|---|
| **CT** | HU are quantitative — usually no rescaling; may clip to a window (state it) |
| **MRI** | Intensities are **not** standardised — normalise (e.g. z-score, or histogram matching); state method |
| **PET** | Use SUV; state the SUV normalisation |

State whether normalisation is fit per-image or using training statistics (must not use test).

- **Re-segmentation** (the IBSI "re-segmentation range" item): mask the ROI to a justified
  intensity range **before** discretisation/extraction when the target construct requires it.
  Values such as −150…+400 HU or ±3 SD are illustrative only, **not recommended defaults**;
  derive and justify the actual rule from anatomy, acquisition, endpoint and a sensitivity check.
- Use it when air, bone, or artefact voxels inside the ROI would distort intensity statistics;
  report the range and method (mandatory IBSI list below).

## Gray-level discretisation (the decision that moves every texture feature)

- **Fixed bin width** (illustrative examples sometimes use 25 HU) — can preserve a fixed intensity
  scale when the modality and preprocessing support that interpretation.
- **Fixed bin count** (illustrative examples sometimes use 32/64 bins) — fixes the number of gray
  levels while making the effective width depend on the observed range.
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

Add separate evidence for implementation verification and empirical stability when those claims are
made: reference values/digital phantom where applicable; software/build comparison; segmentation
sensitivity; phantom/test-retest; protocol/scanner/spacing sensitivity; and the resulting feature
disposition. A complete IBSI checklist cannot replace these results.

## Reporting sentence

*"Based on the prespecified native-spacing distribution and target-lesion scale, images were
resampled to [task-justified spacing] ([image interpolator]; masks nearest-neighbour); the primary
feature set used [discretisation method/value]. Native/alternative-spacing sensitivity and
[implementation/phantom/test-retest evidence] are reported in [location]. Features were extracted
in [2D/3D aggregation] with [software/build], using named IBSI definitions."*
