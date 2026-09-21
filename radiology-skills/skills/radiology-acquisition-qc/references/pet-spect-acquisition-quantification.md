# PET and SPECT Acquisition and Quantification

Use this playbook for PET, PET/CT, PET/MR, SPECT or SPECT/CT. Keep PET and SPECT measurement chains
separate: both are emission imaging, but tracer physics, collimation/detection, corrections,
calibration and reconstruction are not interchangeable. For hybrid studies, also load the CT or MR
playbook whenever that component contributes to the claim.

## Lock the claim and component roles

State whether the requested object is:

- visual/ordinal uptake or distribution;
- static PET SUV or another normalized uptake quantity;
- dynamic PET kinetic/macroparameter output;
- SPECT count concentration, activity concentration, uptake ratio or perfusion/functional score;
- lesion/organ morphology from the hybrid CT/MR;
- attenuation-correction-only versus diagnostic CT/MR;
- longitudinal response or cross-scanner/site comparability.

Name the radionuclide, radiopharmaceutical, target tissue, acquisition window, reconstruction and
reported unit. If these are not recoverable, use `AUTHOR_INPUT_NEEDED`; do not infer them from
appearance.

## PET chain

### Administration and patient state

- radiopharmaceutical and radionuclide, assay/injection timestamps, assayed and administered
  activity, residual/extravasation evidence and clock synchronization;
- uptake interval, scan start/time per bed or frame, patient preparation, fasting and glucose when
  relevant to the tracer/protocol;
- body mass and the exact normalization basis used for SUV or other normalized metrics;
- patient position, respiratory/cardiac gating, motion and intervention/treatment timing.

### Acquisition, corrections and reconstruction

- system manufacturer/model, detector configuration, software and acquisition mode;
- static/dynamic/list-mode, axial coverage, bed duration/overlap, frame boundaries and gating;
- attenuation, scatter, randoms, decay, normalization, dead-time and motion corrections;
- CT/MR attenuation-map method, metal/contrast/truncation/misregistration review and whether the
  hybrid component is low-dose localization, attenuation correction, diagnostic imaging, or mixed;
- reconstruction algorithm, iterations/subsets, regularization/penalty, filter, matrix/FOV, voxel
  size, point-spread-function/resolution recovery and time-of-flight settings/version;
- scanner calibration and dose-calibrator cross-calibration status, QC date and relevant service or
  software events.

### Static and dynamic quantification

- write the exact SUV or normalization formula, numerator/denominator, decay convention and unit;
- state segmentation/peak/maximum/mean definition and partial-volume or recovery correction;
- for dynamic PET, preserve frame timing, input-function source/correction, metabolite handling when
  applicable, kinetic model, fit method, parameter units and rejection/QC rule;
- keep semi-quantitative uptake, absolute activity concentration and model-derived kinetic
  parameters as different claims.

Uptake-time drift, glucose/patient-state differences, extravasation, attenuation-map error,
calibration drift, reconstruction changes and lesion-size-dependent recovery can all mimic
biological change.

## SPECT chain

### Administration and acquisition

- radiopharmaceutical/radionuclide, administered activity and residual, administration and scan
  timestamps, preparation and physiologic state;
- gamma-camera/SPECT system model/software, detector heads, collimator, orbit, radius, angular
  range, number of projections, dwell time/count target, matrix, zoom and pixel size;
- photopeak and scatter energy windows, gating, patient/organ motion and CT component role;
- planar versus tomographic versus hybrid acquisition and whether multiple views/frames are nested
  within the same examination.

### QC, correction, reconstruction and calibration

- flood/uniformity, energy peaking, center-of-rotation, detector alignment and other applicable
  camera QC status;
- attenuation, scatter, decay, dead-time, motion and resolution-recovery corrections;
- iterative algorithm, iterations/subsets, filters, regularization, matrix/voxel and software
  version;
- calibration factor and traceability for any activity-concentration/absolute-quantification claim;
- CT attenuation-map artifacts, registration and truncation review for SPECT/CT.

Absolute or cross-site SPECT quantification is `STOP` without a traceable calibration/correction
chain and task-matched evidence. A relative regional score may survive as `CONDITIONAL` if its
protocol and limitations are explicit.

## Shared artifact and hierarchy checks

| Threat | Measurement impact | Required action |
|---|---|---|
| injection-to-scan or frame timing error | biased uptake/kinetics | reconcile clocks and timestamps; sensitivity if bounded |
| dose-calibrator/scanner calibration mismatch | global quantitative bias | cross-calibration evidence; phantom/QC date |
| patient motion or PET/SPECT-to-CT/MR mismatch | attenuation error and false localization | alignment review; correction/reconstruction sensitivity |
| metal, contrast, truncation or MR attenuation-map defect | focal or regional uptake bias | inspect attenuation map and non-attenuation-corrected data when available |
| partial-volume/recovery and lesion size | size-dependent underestimation/algorithm dependence | task/size-matched recovery evidence; report method |
| reconstruction/filter/PSF/TOF or software change | altered uptake, resolution and texture | paired reconstruction or repeatability study; version lock |
| uptake physiology and preparation | biological-looking technical/physiologic shift | protocol evidence; stratify/narrow/exclude by prespecified rule |

Patients—not beds, frames, lesions, projections, gates, reconstructions or hybrid components—define
the primary independent unit unless the estimand explicitly models clustering.

## Longitudinal and multicentre gates

1. Freeze tracer, preparation, administration, timing, acquisition, corrections, reconstruction,
   segmentation and normalization rules before reading response outcomes.
2. For response, compare the observed change against a task- and protocol-matched repeatability
   boundary; statistical significance or a percentage alone is not proof of biological response.
3. For multicentre use, record calibration chain, phantom/QC, vendor/model/software and protocol.
4. Distinguish represented scanner/protocol levels from wholly unseen levels. Recalibration,
   harmonisation or threshold adjustment using evaluation-site images is adaptation.
5. Apply a QIBA profile claim only when its specified tracer, use case, actors, procedures and
   conformance conditions apply.

Load the common phantom/test-retest/protocol-shift playbook for quantitative response, absolute
quantification or transport claims.

## Verdict and handoff

- `PASS` when tracer administration/timing, acquisition, corrections, calibration, reconstruction,
  unit, QC and task-matched repeatability/transport are traceable.
- `CONDITIONAL` for a narrower visual, ordinal, relative or within-protocol claim whose unresolved
  source is bounded.
- `STOP` for unknown tracer/timing, invalid normalization, non-traceable absolute calibration,
  dominant attenuation/motion artifact, outcome-dependent reconstruction choice, or unbounded
  protocol shift central to the claim.

Send hybrid component image validity to the CT/MR playbook; disease/response definitions to
`radiology-clinical-domain`; lesion localization rules to `radiology-annotation`; quantitative
inputs to `radiology-radiomics` or `radiology-deep-learning`; comparative inference to
`radiology-method-evaluation` and `radiology-stats`; and clinical workflow to
`radiology-translation`.

## Authoritative source ledger

- DICOM Standard Committee. [Current DICOM Standard](https://www.dicomstandard.org/current/).
- RSNA QIBA. [Profiles index](https://qibawiki.rsna.org/index.php/Profiles).
- RSNA QIBA. [FDG-PET/CT as an Imaging Biomarker Measuring Response to Cancer Therapy, Profile
  2023](https://doi.org/10.1148/QIBA/20230615).
- International Atomic Energy Agency. [Quality Assurance for SPECT Systems, IAEA Human Health
  Series No. 6](https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1394_web.pdf).
- European Association of Nuclear Medicine. [Physics, instrumentation and data-analysis guideline
  index](https://eanm.org/publications/guidelines/overview/physics-instrumentation-data-analysis/).
- Society of Nuclear Medicine and Molecular Imaging. [Cardiac SPECT/CT and PET/CT procedure
  standard](https://snmmi.org/Web/Web/Clinical-Practice/Procedure-Standards/Standards/Cardiac-SPECT-CT-and-PET-CT-1.0.aspx).
- American College of Radiology. [Practice Parameters and Technical
  Standards](https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Practice-Parameters-and-Technical-Standards).

Verify the current profile/guideline version, status, tracer, organ/use case and jurisdiction.
A source citation or routine site QC does not establish profile conformance or clinical validity.
