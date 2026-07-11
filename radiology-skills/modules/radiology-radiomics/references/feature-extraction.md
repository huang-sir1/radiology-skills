# Feature extraction

Produce a documented, versioned feature matrix that another lab could regenerate.

## Feature families (IBSI nomenclature)

| Family | Captures |
|---|---|
| **First-order / intensity** | Histogram statistics (mean, entropy, skewness, kurtosis) |
| **Shape (2D/3D)** | Volume, surface area, sphericity, elongation — independent of intensity |
| **GLCM** | Gray-level co-occurrence (texture) |
| **GLRLM / GLSZM / GLDM / NGTDM** | Run-length, size-zone, dependence, neighbouring-tone-difference textures |
| **Filtered (LoG/wavelet/…)** | Any family computed on transformed images |

## PyRadiomics settings to pin (or equivalent tool)

- `binWidth` **or** `binCount` (match preprocessing-ibsi.md) — never both.
- `resampledPixelSpacing`, `interpolator`.
- `normalize`, `normalizeScale` (MRI).
- `imageType` (Original, LoG with sigma, Wavelet, …).
- Enabled feature classes.
- `geometryTolerance` (alignment), `label` (mask value).
- **Save the parameter file** (YAML) and the software version — share it (CLEAR open-science).

## Aggregation

- 2D vs 3D extraction; how directional texture matrices are averaged.
- Per-region (whole tumour, sub-regions, peritumoral, habitats) — keep regions labelled.

## Output: the feature matrix

- Rows = patients (or lesions, with the aggregation rule); columns = features with IBSI names.
- Carry IDs that map to the data dictionary (→ radiology-data).
- Version it; record the exact pipeline that produced it.

## Delta / longitudinal radiomics

When the question is about **change** (treatment response, progression) rather than a single
timepoint, extract features identically at each timepoint and derive delta features explicitly —
don't bolt this on after the fact:

- **Identical pipeline at every timepoint** — same preprocessing, discretisation, filters,
  software/version (preprocessing-ibsi.md); a pipeline change between baseline and follow-up
  masquerades as biological change.
- **Registration**: if comparing voxel/region-level change (not just whole-lesion aggregate
  features), co-register timepoints and report the method and QC; state when only aggregate
  (whole-lesion) delta is used specifically because registration is not reliable.
- **Delta definition** — state it explicitly and keep it consistent: absolute difference
  (`follow-up − baseline`), relative/percent change (`(follow-up − baseline) / baseline`), or a
  rate (per week/cycle). Relative change is undefined near zero-valued baseline features — flag
  or exclude those features rather than silently producing infinities/large outliers.
- **Reproducibility of the delta itself**: a feature can be individually reproducible (high ICC at
  one timepoint) yet the *difference* of two reproducible measurements can still be noisy —
  before trusting a delta feature, its measurement error should be small relative to the
  biological change of interest (→ test–retest below).
- **Timepoint alignment with treatment**: record the exact interval and treatment exposure between
  scans (same discipline as `radiology-radiogenomics/sample-to-image-mapping.md`'s timing rules);
  don't compare patients whose baseline-to-follow-up interval or treatment exposure differs
  systematically without accounting for it.
- **Modelling**: decide whether delta features are used alone or alongside baseline features (the
  two are often correlated); pre-specify which, and keep selection inside training only, same as
  any other radiomics feature (→ `selection-modelling.md`).

## Test–retest / phantom repeatability

`radiology-annotation/reproducibility-qc.md` covers **segmentation** reproducibility (does the
mask change across readers). This is the complementary, less commonly done check: does the
**feature value itself** change on a re-scan of the same object with no real change?

- **Phantom repeatability**: scan a physical phantom (or digital phantom per IBSI) repeatedly, or
  across scanners/protocols/sites, and compute per-feature reproducibility (e.g. concordance
  correlation coefficient, coefficient of variation, or ICC across repeats) — this isolates
  scanner/acquisition noise from segmentation variability.
- **Test–retest in patients**: where feasible (and ethically/practically justified — this adds
  scan burden), a short-interval repeat scan with no true biological change between scans, same
  protocol, to estimate the combined acquisition + reconstruction + (if masks are refreshed)
  segmentation noise floor for each feature.
- **Use of the result**: features that fail a pre-specified repeatability threshold are dropped
  or down-weighted **before** selection/modelling, the same way low-ICC segmentation-reproducibility
  features are filtered in `radiology-annotation/reproducibility-qc.md` — state whether the two
  filters (segmentation ICC and test–retest/phantom repeatability) were combined or applied
  separately.
- **This is a scored RQS/RQS 2.0 item** ("test–retest / phantom" and "multiple segmentations") —
  reporting it, even as "not performed, and here is why," is stronger than silence
  (→ `radiology-reporting/clear-metrics-rqs.md`).

## Quick PyRadiomics invocation (illustrative)

```python
from radiomics import featureextractor
extractor = featureextractor.RadiomicsFeatureExtractor("params.yaml")  # pins all settings
result = extractor.execute(image_path, mask_path, label=1)
# persist result + params.yaml + pyradiomics.__version__ for reproducibility
```

## Reporting sentence

*"For each lesion, [N] IBSI-compliant features (first-order, shape, GLCM/GLRLM/GLSZM/GLDM/NGTDM,
plus LoG- and wavelet-filtered) were extracted with PyRadiomics vX.Y using a fixed parameter
file (provided in the supplement)."*
