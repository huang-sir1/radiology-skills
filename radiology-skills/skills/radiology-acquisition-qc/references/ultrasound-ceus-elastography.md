# Ultrasound, CEUS, and Elastography

Use this playbook for B-mode ultrasound, Doppler, contrast-enhanced ultrasound (CEUS), strain
elastography and shear-wave elastography. Ultrasound is a dynamic, operator-mediated acquisition:
a saved “best frame” does not fully specify probe placement, force, insonation, settings, motion or
the rejected observations.

## Lock the measurement object

| Object | Minimum identity | Frequent invalid upgrade |
|---|---|---|
| B-mode morphology/echogenicity | organ/lesion, plane, probe, frequency/preset, depth/focus/gain and frame/cine rule | treating display brightness as an absolute tissue property |
| spectral/color/power Doppler | vessel/ROI, mode, angle, sample volume, PRF/scale, wall filter and waveform rule | comparing velocities with unknown or non-equivalent angle/settings |
| CEUS enhancement/perfusion | agent/dose, injection and acquisition clocks, mechanical index, cine/timing and analysis algorithm | treating a selected frame or vendor curve as universal perfusion |
| strain elastography | compression method, reference, strain/ratio rule, ROI and quality criterion | calling strain a direct modulus |
| shear-wave speed/stiffness | mode, unit, ROI depth/size, acquisition quality, repeats and conversion assumption | pooling m/s and kPa or vendors without validation |

If decisive settings, dynamic source data or measurement units are unavailable, mark
`AUTHOR_INPUT_NEEDED` and narrow the claim.

## Reconstruct the acquisition chain

### Shared system and scanning fields

- system manufacturer/model, software version, transducer model/type and frequency range;
- patient preparation, position, breath/strain state, acoustic window and target depth;
- operator identity/experience category, probe orientation, contact/compression, sweep/plane rule and
  number of attempts;
- exam preset, transmit frequency/harmonics, depth, focus, gain, time-gain compensation, dynamic
  range, persistence/smoothing, spatial compounding, frame rate and zoom;
- saved format: raw/channel/RF data when available, cine loop, DICOM multiframe, still image,
  secondary capture or compressed export;
- target-level adequacy, excluded/repeated acquisitions and whether the selection rule was
  prespecified.

Do not infer console settings from pixel appearance. Do not treat multiple frames, views, loops or
measurements from one patient as independent patients.

### Doppler

- mode, transmit frequency, pulse-repetition frequency/velocity scale, wall filter, gain, color box,
  baseline and priority settings;
- vessel and sample-volume position/size, spectral trace length, insonation angle and angle-
  correction convention;
- cardiac/respiratory state and waveform selection/averaging rule;
- aliasing, blooming, spectral broadening, motion/clutter and inadequate angle/window checks.

For velocity claims, a displayed angle correction is not proof that the insonation geometry is
valid. Preserve the waveform and acquisition settings.

### CEUS

- contrast agent, concentration/dose, route, bolus/flush or infusion method, injection clock and
  timer synchronization;
- contrast-specific mode, transducer, mechanical index, gain/dynamic range, focus, depth, frame
  rate, acquisition duration and destructive/replenishment pulse protocol if used;
- motion/breath handling, cine-loop completeness, reference/target ROI, tracking/registration and
  rejected segments;
- time-intensity preprocessing, baseline, curve/model, input/reference, parameter definition,
  software/version and output unit.

Peak intensity, time-to-peak, wash-in/out descriptors and model-based perfusion parameters are
different estimands. A single post-contrast image cannot support a full time-intensity claim.

### Elastography

First distinguish:

- strain/strain-ratio imaging, which depends on deformation and reference/compression; from
- shear-wave measurements, which report propagation speed or a derived stiffness under model
  assumptions.

Record mode, unit (for example m/s versus kPa), frequency/preset, ROI size/location/depth, probe
pressure, patient/breath state, acquisition quality/confidence map, rejection rule, number and
spacing of repeats, aggregation statistic and software/version. If speed is converted to stiffness,
write the equation and tissue assumptions. Do not silently compare modes, units, organs or vendor
algorithms.

## Operator and reader variability are separate

Design and report:

1. acquisition variability—operator, probe placement, pressure, window and repeated loops;
2. measurement/reader variability—ROI placement, frame choice, trace/curve rule and interpretation;
3. system/protocol variability—transducer, preset, software and post-processing.

A study in which one operator acquires once and many readers measure the same saved frame does not
estimate acquisition repeatability.

## Artifact and confounder map

| Threat | Likely effect | Required check |
|---|---|---|
| anisotropy, refraction, shadowing or enhancement | apparent lesion/tissue contrast or missing boundary | alternate plane/window; target-level adequacy |
| depth, focus, gain/TGC, frequency and processing | brightness, texture, penetration/resolution shift | setting lock; phantom/paired sensitivity |
| probe pressure and patient motion/breath | geometry, flow, perfusion or stiffness change | acquisition instruction; repeat/reposition evidence |
| Doppler angle/PRF/filter/gain | velocity bias, aliasing or missing slow flow | parameter and waveform review |
| CEUS timer/MI/bolus/motion mismatch | non-biological curve change | synchronized clocks; complete cine; motion sensitivity |
| elastography quality/depth/ROI/vendor conversion | invalid or non-equivalent stiffness/speed | quality-map rule; repeated measures; exact unit/mode validation |
| selective “best frame” retention | optimism and hidden failure rate | prespecified retention rule; count attempted/rejected loops |

## Repeatability and transport gates

- Freeze operator instructions, target plane/window, setting ranges, frame/cine retention and
  measurement rule before outcome review.
- For quantitative CEUS or elastography, include repositioned repeated acquisitions—not only
  repeated ROI placement—and report invalid/failed acquisition rates.
- Separate same-operator, different-operator and different-system reproducibility.
- A QIBA shear-wave profile claim applies only to its specified biomarker, organ/use case, actors and
  conditions. Do not transfer a numeric performance claim across modes or vendors without evidence.
- For multicentre work, record represented and wholly unseen system/transducer/software/preset
  levels. Reprocessing evaluation-site data or tuning thresholds on them is adaptation.
- Load the common phantom/test-retest/protocol-shift playbook when quantitative, longitudinal or
  cross-platform claims are intended.

## Verdict and handoff

- `PASS` when the dynamic acquisition, settings, operator/plane rule, measurement algorithm/unit,
  quality state and task-matched repeatability/transport evidence are traceable.
- `CONDITIONAL` for a narrower visual, ordinal, relative, within-operator or within-system claim with
  explicit failure and uncertainty boundaries.
- `STOP` when only selectively retained frames exist for a dynamic claim, a central setting/unit is
  unknown, CEUS timing is invalid, Doppler geometry is non-identifiable, elastography quality fails,
  or protocol/operator shift determines the result without bounding evidence.

Send target geometry and admissible frames to `radiology-annotation`; accepted images/loops and
settings to `radiology-radiomics` or `radiology-deep-learning`; reliability inference to
`radiology-method-evaluation` and `radiology-stats`; disease meaning to
`radiology-clinical-domain`; and workflow/operator failure states to `radiology-translation`.

## Authoritative source ledger

- DICOM Standard Committee. [Current DICOM Standard](https://www.dicomstandard.org/current/).
- RSNA QIBA. [Profiles index](https://qibawiki.rsna.org/index.php/Profiles).
- RSNA QIBA. [Ultrasound Measurement of Shear Wave Speed for Estimation of Liver Fibrosis, Profile
  2024](https://doi.org/10.1148/QIBA/20240115).
- American College of Radiology and American Association of Physicists in Medicine.
  [Technical Standard for Medical Physics Performance Monitoring of Diagnostic Ultrasound
  Equipment](https://gravitas.acr.org/PPTS/GetDocumentView?docId=118).
- American College of Radiology. [Practice Parameters and Technical
  Standards](https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Practice-Parameters-and-Technical-Standards).
  Use the portal to verify the current applicable ultrasound, CEUS and elastography documents.

Verify source version, profile stage, organ/use case and jurisdiction. A cited profile or equipment
standard does not prove dataset, actor or site conformance.
