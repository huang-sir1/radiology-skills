# CT Acquisition and Reconstruction

Use this playbook when CT supplies the primary image, a quantitative CT value, a longitudinal
change, or the attenuation/anatomic component of a hybrid examination. It owns the physical
acquisition-to-image chain. Disease eligibility, response definitions, annotation, feature
extraction and statistical inference remain with their dedicated owners.

## Start with the measurement object

Name one primary object before inspecting performance or outcome:

| Object | Minimum identity lock | Frequent invalid upgrade |
|---|---|---|
| attenuation or Hounsfield-unit measurement | material/tissue, phase, energy representation, ROI rule, calibrated unit | treating a vendor-derived value as universal HU |
| morphology, diameter or volume | lesion/object, source series, slice geometry, reconstruction kernel, segmentation/measurement rule | treating thin/thick or sharp/smooth reconstructions as interchangeable |
| enhancement or perfusion | pre/post phases, contrast protocol, clock/trigger, motion/registration and kinetic derivation | calling an unknown phase “arterial” from a filename |
| spectral/dual-energy/photon-counting quantity | acquisition mode, energy bins, material basis, monoenergetic level, algorithm/version and unit | treating iodine/material maps as direct scanner-independent truth |
| opportunistic biomarker | anatomy, calibration basis, reconstruction, posture/breath state and analysis location | extending a single-protocol association to absolute cross-platform measurement |

If the intended series or unit cannot be identified from source evidence, mark
`AUTHOR_INPUT_NEEDED`. Do not select a series because it gives the strongest association.

## Reconstruct the chain

Record the following in the imaging measurement passport. Use DICOM attributes, protocol exports,
scanner dose reports, reconstruction records and physicist QC artifacts in preference to prose.

### Examination and acquisition

- manufacturer, model, detector/hardware options, station and software version;
- exam date/time, anatomy, patient position, breath instruction, cardiac/respiratory gating and
  whether the acquisition is diagnostic, localizer, monitoring or derived;
- acquisition mode: axial/helical, single/dual/spectral/photon-counting energy mode, tube potential,
  tube current or exposure-control method, rotation time, collimation and pitch;
- scan and reconstruction field of view, matrix, acquired detector/sample geometry, slice
  thickness/increment and overlap;
- contrast agent concentration, dose basis, injection rate, saline flush, injection and acquisition
  clocks, bolus trigger/test bolus, delay and phase rule;
- CTDIvol, DLP and dose-report provenance when dose is material. Treat CTDIvol/DLP as standardized
  scanner-output/protocol descriptors, not a patient-specific absorbed-dose estimate.

### Reconstruction and derived objects

- source acquisition UID and the exact series/instance inclusion rule;
- reconstruction kernel/family, iterative or deep-learning reconstruction product, version and
  strength, slice thickness/increment, field of view and matrix;
- rescale slope/intercept or real-world value mapping used to obtain the reported unit;
- multiplanar, maximum-intensity, subtraction, perfusion, monoenergetic or material-decomposition
  derivation, including input phases, registration, algorithm/version and unit;
- whether multiple reconstructions arise from the same raw acquisition. Keep them paired inside the
  patient/exam; they are not independent samples.

For PET/CT or SPECT/CT, also declare whether CT is diagnostic, localization-only, attenuation
correction, or more than one of these. Load the nuclear medicine playbook for tracer quantification.

## Series-selection lock

Freeze these rules before viewing outcomes or model performance:

1. intended anatomy, contrast phase and acquisition type;
2. preferred and fallback reconstruction kernel, thickness and algorithm;
3. rules for missing, duplicated, reformatted, derived or motion-degraded series;
4. one-series versus paired/multiphase use and how repeat reconstructions are grouped;
5. adjudication method and log for ambiguous series.

A series description is a hint, not proof. Confirm against DICOM acquisition/reconstruction
attributes and, when needed, protocol or console evidence.

## Physical-confounder and artifact map

| Threat | Likely measurement effect | Required check or sensitivity |
|---|---|---|
| motion, breath-state or cardiac-phase mismatch | blur, displacement, false size/density change | inspect source images; stratify/exclude by prespecified rule; register only with documented method |
| partial volume and anisotropic voxels | biased density, diameter and volume | resolution/size analysis; consistent thickness/kernel; phantom or resampling sensitivity |
| beam hardening, metal, photon starvation or truncation | regional HU/texture bias or missing anatomy | artifact grade, spatial overlap with target, reconstruction/MAR sensitivity |
| contrast timing or cardiac-output variation | apparent enhancement/perfusion difference | clock/trigger evidence; phase-specific analysis; timing sensitivity |
| sharp/smooth kernel, iterative/DL strength or software upgrade | altered noise, edges, texture and sometimes quantitative values | paired reconstruction analysis; version lock; do not pool silently |
| energy/material-decomposition choice | non-equivalent HU or material quantity | name energy/material basis and unit; validate the exact derived product |
| display/window only | changes presentation, not source pixel values | distinguish pixels for processing from screenshots/exported presentation pixels |

Do not “correct” an unexplained artifact with a downstream model and then claim restored physical
validity. Preserve the raw/native primary analysis and label any correction as a sensitivity or
adaptation.

## Quantitative and longitudinal gates

- Verify unit conversion from stored pixel values; record whether values are HU, concentration,
  perfusion parameters, density, dimensions or algorithm-specific scores.
- For serial scans, compare phase, breath state, acquisition geometry, contrast protocol,
  reconstruction and software. Biological change is not identifiable when technical change can
  explain the effect and no bounding evidence exists.
- Use a task-matched phantom, same-subject test-retest, or paired reconstruction study when the
  claim depends on measurement repeatability. Load the common phantom/shift playbook.
- A QIBA profile claim is conditional on the named profile, actors, procedures and conformance
  conditions. Do not transfer its numeric performance claim to a different lesion size, protocol,
  algorithm or use case.
- There is no universal reconstruction-independent HU, texture, volume or spectral equivalence.

## Verdict and handoff

- `PASS` only when acquisition, phase, reconstruction, unit, series rule and task-relevant QC are
  traceable, and repeatability/transport evidence matches the proposed quantitative claim.
- `CONDITIONAL` when the data support a narrower within-protocol, within-site or relative comparison
  with the unresolved source explicitly bounded.
- `STOP` for an unidentified/wrong phase, unknown central reconstruction, invalid unit conversion,
  result-dependent series choice, failed target-overlapping QC, or unbounded protocol change that
  determines the central measurement.

Send the frozen series and geometry to `radiology-annotation`; accepted input objects and shift
limits to `radiology-radiomics` or `radiology-deep-learning`; parameter comparisons to
`radiology-method-evaluation`; disease interpretation to `radiology-clinical-domain`; and the final
measurement state, never an upgraded claim, to `radiology-translation`.

## Authoritative source ledger

- DICOM Standard Committee. [Current DICOM Standard](https://www.dicomstandard.org/current/).
  Use the current Parts 3, 4, 6 and 16 as applicable to identify information objects, attributes,
  services and coded terms; verify the edition used.
- RSNA QIBA. [Profiles index](https://qibawiki.rsna.org/index.php/Profiles). Select the exact current
  CT profile and verify status rather than treating the index as conformance evidence.
- RSNA QIBA. [CT Small Lung Nodule Volume Assessment and Monitoring in Low Dose CT Screening,
  Profile 2023](https://doi.org/10.1148/QIBA/20231219).
- RSNA QIBA. [CT Tumor Volume Change Profile 2022](https://doi.org/10.1148/QIBA/20220721).
- American College of Radiology. [Practice Parameters and Technical
  Standards](https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Practice-Parameters-and-Technical-Standards).
  Verify the current CT standard, jurisdiction and local applicability.

The source ledger supports protocol design and audit; it does not by itself establish that a
dataset, device, site or actor conforms.
