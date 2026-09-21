# Segmentation and quantitative-measurement study contract

Use this contract for delineating anatomy/pathology and for measurements derived from a contour or
voxel map: volume, diameter, burden, composition, dose-volume quantity or quantitative biomarker.
Separate **geometric agreement**, **measurement accuracy/repeatability** and **downstream clinical
utility**; success in one does not prove the others.

## 1. Freeze the construct

| Field | Required specification |
|---|---|
| Population/pathway | intended patients, setting and disease spectrum |
| Modality/input | series, phases/views, reconstruction and any prior/clinical information |
| Target object | structure/lesion/subregion, boundary convention, inclusion/exclusion of necrosis, vessels, cavities, edema or artifacts |
| Output | binary/multiclass mask, surface, instance set, probability map or scalar measurement |
| Independent unit | patient/examination; record lesion/organ/timepoint nesting |
| Intended purpose | planning, burden estimation, response tracking, feature extraction, visualization or research-only |
| Primary estimand | geometric, measurement or downstream-task contrast with target population |
| Tolerance | clinically/physically justified distance, volume or change threshold; never chosen from the test result |

For longitudinal work, state whether the task is independent timepoint segmentation, propagated
segmentation or change measurement; each has different registration and error propagation.

## 2. Reference-standard contract

- Use **reference standard**, not an assertion of error-free ground truth. Specify reader number,
  expertise, training/calibration, information available, blinding, independent reads, consensus and
  adjudication.
- Preserve individual masks before consensus when inter-reader variability is part of the validity
  argument. A consensus mask alone hides the attainable agreement range.
- Define how uncertain boundaries, multifocal/merged lesions, absent targets and non-evaluable images
  are represented. Do not force uncertainty into a falsely precise contour.
- For model-assisted annotation, record the initial model/version, what readers saw, editing/QC rules
  and whether the same assistance was used for development and testing references.
- Validate DICOM/NIfTI/DICOM-SEG/RTSTRUCT geometry: patient, frame of reference, series, spacing,
  origin, direction, slice order, interpolation and label values. Geometry failure is a stop condition.

## 3. Data, partitions and preprocessing

- Split by patient and keep lesions, timepoints, slices, patches and augmentations together.
- Freeze resampling, intensity normalization, cropping, registration, post-processing and connected-
  component rules. Fit learned steps on training data only.
- Characterize site, vendor, field strength, slice thickness, reconstruction, contrast phase, image
  quality and target-size distribution. Test the named transport domain untouched.
- If contour quality controls select cases after seeing model error, report the selection as a
  result-aware deviation rather than a prespecified eligibility rule.

## 4. Endpoint stack

Do not rely on a single overlap number.

| Evidence layer | Candidate measures | Required interpretation |
|---|---|---|
| Overlap | Dice/Jaccard, class-wise and macro/micro rule | size dependence and handling of absent class |
| Boundary | HD95, average/symmetric surface distance, surface Dice | physical units and prespecified tolerance |
| Detection/instances | lesion sensitivity, false positives/exam, matched-instance rule | separate missed lesions from poor contours |
| Quantification | bias, absolute/relative error, Bland-Altman limits, repeatability coefficient | units, scale dependence and clinically meaningful change |
| Downstream | planning/feature/model/reader effect | separate prespecified downstream analysis with uncertainty |

- Report distributions and CIs, not only means. Patient-level or cluster-aware inference must respect
  multiple lesions/classes/timepoints.
- Empty-reference/empty-prediction cases require an explicit convention and separate counts.
- A surface tolerance must come from clinical use, acquisition resolution or a justified measurement
  requirement—not from maximizing test performance.
- Compare algorithm error with inter-/intra-reader variability without declaring equivalence from
  overlapping CIs. Use a prespecified margin and paired analysis if equivalence/non-inferiority is the
  claim.
- For quantitative biomarkers, evaluate bias, repeatability, reproducibility across sites/scanners and
  sensitivity to segmentation. Route formal measurement inference to `radiology-stats`.

## 5. Validation and robustness

Minimum evidence:

1. frozen held-out patient-level test;
2. simple/established segmentation comparator and reader variability benchmark;
3. size, morphology, site/scanner/protocol and image-quality strata;
4. failure cases including total misses, leakage into adjacent anatomy and wrong-instance merges;
5. perturbation tests for resampling, registration, post-processing and contour uncertainty;
6. external/temporal testing for transport claims.

If the intended use is planning or intervention, geometric performance alone is insufficient: test the
decision-bearing derived quantity and its safety-relevant failure modes with qualified local experts.

## 6. Sample-size and stop gates

Plan around the primary patient-level estimand, paired correlation, lesion/class prevalence,
non-evaluable rate, reader variability and desired precision/margin. Tiles and slices are not sample
size. Return `BIOSTATISTICIAN_REQUIRED` when equivalence margins, clustered precision or repeated-
measurement variance inputs remain unsupported.

Return `STOP_FOR_REPAIR` for frame-of-reference mismatch, test-set-assisted contour editing, changed
boundary definitions after test access, patient leakage, unresolved absent-class conventions or an
unreconstructable denominator.

## 7. Claim boundary and handoff

- Geometric agreement supports contour similarity under the tested reference process.
- Quantitative agreement supports the named measurement within its repeatability/reproducibility range.
- Downstream or prospective evidence is required for clinical utility or safety claims.

Return: `construct card -> annotation/reference-standard protocol -> geometry receipt -> split manifest
-> metric/tolerance contract -> measurement and sample-size brief -> robustness/failure matrix ->
downstream validation -> claim ceiling -> deviations`.

## Primary and official sources

- Tejani AS, et al. [CLAIM 2024 Update](https://doi.org/10.1148/ryai.240300).
- Taha AA, Hanbury A. [Metrics for evaluating 3D medical image segmentation](https://doi.org/10.1186/s12880-015-0068-x).
- RSNA QIBA. [Profiles and conformance resources](https://qibawiki.rsna.org/index.php/Profiles).
- DICOM Standards Committee. [Current DICOM Standard](https://www.dicomstandard.org/current/).
- Sullivan DC, et al. [Metrology standards for quantitative imaging biomarkers](https://doi.org/10.1148/radiol.2015142202).
