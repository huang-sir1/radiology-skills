# Reconstruction and image-enhancement study contract

Use this contract for reconstruction, denoising, artifact correction, super-resolution, acceleration,
low-dose synthesis, harmonisation or other image-to-image transformation. The scientific target is not
automatically pixel similarity: define the diagnostic/quantitative task and the acceptable failure
boundary before choosing an image-quality metric.

## 1. Freeze the technical and clinical task

| Field | Required specification |
|---|---|
| Modality/acquisition | raw/projection/k-space/image-domain input, scanner, protocol, dose/time and reconstruction chain |
| Transformation | exact algorithm/version, inputs, output, stochasticity and post-processing |
| Comparator | routine reconstruction/acquisition and any established alternative |
| Intended use | lower dose/time, artifact reduction, visualization, quantitative measurement or downstream task |
| Unit | patient/examination; record series/slice/repeat/phantom nesting |
| Primary endpoint | task-based observer performance, quantitative bias/repeatability or justified image-quality metric |
| Margin/tolerance | clinically and physically justified superiority/non-inferiority or measurement boundary |
| Failure policy | abstention, fallback reconstruction and prohibited use cases |
| Claim ceiling | technical feasibility, task performance, reader effect or workflow/patient impact |

State whether output is reconstructing acquired information, estimating missing information or
generating a plausible image. A plausible image is not proof that a displayed structure was measured.

## 2. Reference and data contract

- Prefer prospectively paired acquisitions/reconstructions, retained raw data, validated phantoms or
  another reference appropriate to the intended task. Misregistered or differently timed scans are not
  pixel-level truth.
- Record acquisition/reconstruction parameters, dose/exposure, contrast timing, motion, calibration,
  coil/kernel/filter and software versions. Preserve raw-to-output provenance and DICOM identifiers.
- Split by patient and acquisition episode. Derived dose levels, adjacent slices, repeated
  reconstructions and paired raw data stay in one partition.
- Audit public/pretraining sources for patient and derived-image overlap. Synthetic training pairs must
  not be evaluated as if they were independent real acquisitions.
- Define image-quality exclusions before viewing algorithm errors; report failure rates and reasons.

## 3. Evaluation hierarchy

Use the highest layer required by the claim:

| Layer | Evidence | Boundary |
|---|---|---|
| Physical/technical | resolution/MTF, noise/NPS, contrast, uniformity, artifact and phantom measures | modality- and protocol-specific; no universal metric set |
| Perceptual similarity | SSIM/PSNR or learned perceptual measure | may reward blur or miss clinically important hallucination |
| Quantitative biomarker | bias, limits of agreement, repeatability/reproducibility for HU/SUV/ADC/volume or named quantity | units, reference and allowable change required |
| Diagnostic task | lesion detectability/classification or reader confidence/time with paired analysis | requires cases and reference standard representing the task |
| Clinical/workflow impact | dose/time reduction, repeats, downstream decisions or outcomes | prospective/impact design required |

Do not select metrics after seeing which favor the method. Report the routine comparator first and use
paired patient-level uncertainty. Slices, patches, noise realizations and folds are not independent
patients.

## 4. Hallucination, bias and stress tests

Predefine tests for:

- insertion, deletion, displacement or smoothing of small/subtle findings;
- motion, metal, implants, truncation, low counts/dose, unusual anatomy and out-of-distribution protocols;
- lesion-present and lesion-absent cases, with local error maps and expert adjudication;
- scanner/vendor/site, dose/count level, body size and clinically relevant subgroup;
- stochastic variability, seed dependence and repeated reconstructions;
- quantitative drift and downstream-model sensitivity;
- missing/corrupt input and safe fallback behavior.

If a generative method can invent plausible structures, name that risk, expose uncertainty where
possible and prohibit stronger “restoration of truth” language without direct evidence.

## 5. Validation and reader route

- Freeze algorithm, windowing/display, comparator and primary margin before the untouched test.
- Use external scanner/site/protocol testing for transport claims; performance after local fine-tuning
  is adaptation and requires a new test set.
- Reader studies require randomized/counterbalanced presentation, blinding, washout when repeated,
  paired MRMC/task-based analysis and capture of confidence, time and enhancement-induced errors.
- For non-inferiority, justify the margin clinically and analyze according to a prespecified framework;
  failure to reject difference is not equivalence.

## 6. Sample size and stop gates

Plan from the primary independent-unit estimand, paired variance, target prevalence/task difficulty,
reader/case variance, repeat acquisitions and margin/precision. Phantom or slice counts cannot replace
patient/task cases.

Return `STOP_FOR_REPAIR` for patient/derived-pair leakage, post-test metric/margin selection, missing
raw-to-output provenance, materially misregistered references, hidden failed cases or a claim based only
on perceptual similarity when the intended use is diagnostic/quantitative. Return
`BIOSTATISTICIAN_REQUIRED` for unsupported non-inferiority, MRMC or repeatability design inputs.

## 7. Claim boundary and handoff

- Better PSNR/SSIM supports only the named similarity result.
- Phantom/technical conformance supports performance under that profile/protocol.
- Quantitative agreement supports only the named biomarker and measurement conditions.
- Reader or prospective evidence is required for diagnostic/workflow benefit.

Return: `technical-use card -> acquisition/raw-data provenance -> paired reference and partition
manifest -> metric/margin contract -> phantom/quantitative/task-based plan -> stress/failure matrix ->
reader/impact handoff -> claim ceiling -> deviations`.

## Primary and official sources

- RSNA QIBA. [Profiles and conformance resources](https://qibawiki.rsna.org/index.php/Profiles).
- DICOM Standards Committee. [Current DICOM Standard](https://www.dicomstandard.org/current/).
- Sullivan DC, et al. [Metrology standards for quantitative imaging biomarkers](https://doi.org/10.1148/radiol.2015142202).
- Tejani AS, et al. [CLAIM 2024 Update](https://doi.org/10.1148/ryai.240300).

Modality-specific acceptance limits must come from the applicable live profile, standard and qualified
local imaging-physics owner; this contract intentionally supplies no universal cutoff.
