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
