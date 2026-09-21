# MR Acquisition and Reconstruction

Use this playbook when MR images or derived maps are intended as measurements. MR contrast is a
sequence-, hardware-, preparation- and reconstruction-dependent signal; a series name such as
“T1,” “DWI” or “ADC” is not a sufficient measurement specification.

## Start with the measurement object

| Object | Identity required before use | Claim ceiling warning |
|---|---|---|
| anatomic or contrast-weighted image | sequence family, weighting/preparation, contrast state, geometry and reconstruction | signal intensity is not automatically an absolute tissue property |
| DWI/ADC | b-values, directions/trace method, fitting inputs, distortion correction, map derivation and units | ADC maps from different b-value/fitting choices are not interchangeable |
| DCE/perfusion | temporal sampling, contrast protocol, baseline/preload, input function and model/algorithm | a color map is not direct perfusion truth |
| quantitative T1/T2/T2*/PD/MT or other mapping | preparation/readout, sampling, fit/model, corrections, calibration and units | “quantitative” in a series label does not prove traceability |
| MRS/MRSI spectrum or metabolite estimate | localization, water/reference acquisition, preprocessing, basis/model and QC | a fitted peak, ratio or concentration estimate is not a direct chemical assay |
| task/rest BOLD fMRI signal | task/state/timing, preprocessing, physiological/motion handling and statistical model | BOLD is an indirect haemodynamic contrast, not direct neuronal activity or causal proof |
| DTI/advanced diffusion/tractography output | gradient table and orientation, correction, diffusion model, tracking/ROI parameters and QC | a streamline is not an axon or proof of an anatomical connection |
| AI/accelerated reconstruction output | raw/source relation, acceleration, product/version, training/intended-use evidence | visual similarity does not establish measurement equivalence |

Mark missing decisive fields `AUTHOR_INPUT_NEEDED` and narrow the claim rather than imputing a
typical protocol.

## Reconstruct the chain

### System, subject and acquisition

- manufacturer, model, field strength, bore/gradient configuration, software version, RF
  transmit/receive coil and coil-channel configuration;
- anatomy, position, preparation, breath-hold/free-breathing, cardiac/respiratory gating, sedation
  if methodologically material, and contrast agent/dose/timing;
- sequence family and preparation pulses; 2D/3D; TR, TE, TI, flip angle, echo train/readout,
  bandwidth and fat-suppression method;
- field of view, acquired/reconstructed matrix, in-plane resolution, slice thickness/gap,
  orientation, number of averages and partial-Fourier choice;
- parallel imaging/compressed-sensing/other acceleration method and factor;
- acquisition time and temporal resolution for dynamic measurements.

### Reconstruction, correction and map derivation

- source series or raw/k-space provenance, reconstruction product/version/strength, coil
  combination and intensity normalization;
- gradient-nonlinearity, bias-field, motion, eddy-current, susceptibility/distortion, denoising,
  Gibbs-ringing or other corrections, including order and version;
- registration/interpolation between sequences or time points;
- input images, fit domain, mathematical model, constraints, rejection/QC rule and output unit for
  every derived map;
- whether multiple reconstructions or maps share the same acquisition. Keep them paired within the
  examination rather than counting them as independent patients.

Screenshots, secondary captures and colorized maps may discard quantitative scaling. Prefer the
source quantitative object and verify DICOM real-world value mapping or accompanying derivation.

## Sequence-specific execution

### Conditional specialized routes

Load these playbooks only when their measurement object is active, in addition to this MR core:

- MRS or MRSI, metabolite peaks, ratios or concentration estimates: load
  [mr-spectroscopy.md](mr-spectroscopy.md).
- Task or resting-state BOLD fMRI, activation, connectivity or network claims: load
  [functional-mri.md](functional-mri.md).
- DTI, DKI, NODDI, fixel analysis, tractometry or tractography: load
  [diffusion-tensor-tractography.md](diffusion-tensor-tractography.md).

Do not answer these specialized measurement questions from generic MR fields alone. The dedicated
playbook supplies the object-specific QC and claim ceiling; this file still supplies hardware,
geometry, reconstruction, transport and nesting provenance.

### DWI and ADC

1. Record all nonzero and reference b-values, number/direction scheme, averaging, fat suppression,
   phase-encode direction, acceleration and geometry.
2. State whether the displayed DWI is acquired, trace/derived or synthesized and which images enter
   the ADC fit.
3. Record motion, eddy-current and susceptibility correction plus cross-sequence registration.
4. Confirm the ADC fit/model, excluded points, unit (commonly area/time, with scale explicit), map
   version and ROI rule.
5. Inspect distortion and signal floor in the target, not only global image appearance.

Apply a QIBA DWI/ADC performance claim only to the profile-defined setting and conditions; do not
generalize it to different organs, b-values, field strengths, fit models or software.

This subsection covers scalar DWI/ADC. When the claim uses tensor, higher-order, microstructural,
fixel or tractography outputs, always load the dedicated DTI/tractography playbook.

### DCE, DSC, ASL and other perfusion

- lock temporal resolution/coverage and time-zero convention;
- record contrast dose/rate/timing for contrast methods or labeling/post-label delay for ASL;
- identify baseline T1 or other calibration, arterial/input function, leakage/dispersion correction,
  kinetic model and parameter units;
- inspect motion and temporal registration; retain the signal-versus-time or concentration-versus-
  time provenance;
- keep semi-quantitative curve descriptors distinct from model-based physiological parameters.

### Quantitative mapping

- record preparation/readout and sampled inversion, echo, saturation or other encoding points;
- state fit/model, bounds, corrections, B0/B1 handling, calibration/reference and rejection rule;
- verify that reported physical units are supported by the stored object and method;
- require phantom or test-retest evidence for the exact task when absolute or longitudinal change is
  central.

## Physical-confounder and artifact map

| Threat | Likely effect | Required response |
|---|---|---|
| receive-coil sensitivity/bias field or intensity normalization | spatially varying signal/texture | record coil and normalization; bias-field sensitivity; avoid raw intensity equivalence claims |
| susceptibility and geometric distortion | displaced anatomy/ROI mismatch, especially EPI/DWI | field/phase-encode evidence, distortion map or anatomical alignment check |
| motion, ghosting, flow or pulsation | blur, false dynamic change, fitting error | target-level grade; correction provenance; prespecified exclusion/sensitivity |
| B0/B1 inhomogeneity and imperfect fat suppression | regional contrast/map bias | shimming/correction evidence; map or phantom QC when material |
| gradient nonlinearity | spatial geometry or diffusion bias | correction status and target location; phantom/spatial sensitivity |
| Gibbs ringing, truncation, denoising or interpolation | edge/texture/map bias | retain native primary; paired processing sensitivity |
| vendor/software/reconstruction or acceleration change | non-equivalent noise, sharpness, signal and maps | version lock; paired or repeatability evidence; protocol-level analysis |
| registration across sequence/time | false colocalization or change | transform provenance, interpolation and failure review |

## Series-selection and transport gates

- Freeze sequence, contrast state, orientation, geometry, reconstruction and derived-map version
  before outcomes are consulted.
- Treat repeat sequences/reconstructions/maps as nested within patient and examination.
- For longitudinal work, compare field strength, coil, sequence parameters, contrast/gating,
  reconstruction and correction software. A stable series name is not evidence of stability.
- For cross-site work, enumerate represented and wholly unseen vendor/model/software/protocol
  levels. Any recalibration or normalization using evaluation-site data is adaptation, not untouched
  external validation.
- Load the common phantom/test-retest/protocol-shift playbook when absolute, longitudinal or
  cross-platform equivalence is claimed.

## Verdict and handoff

- `PASS` when the sequence-to-map chain, units, artifact/QC state, any conditionally required
  specialist playbook and task-matched repeatability or transport evidence are traceable.
- `CONDITIONAL` for a clearly bounded within-sequence/within-site relative use, or when sensitivity
  analyses bound a non-central uncertainty.
- `STOP` when the decisive sequence/map is unidentified, units or fit inputs are invalid, distortion
  breaks target localization, outcome-dependent series selection occurs, or an unbounded
  hardware/software/protocol change determines the claim.

Send geometry/distortion constraints to `radiology-annotation`; the accepted source/map and
preprocessing boundary to `radiology-radiomics` or `radiology-deep-learning`; measurement
comparisons to `radiology-method-evaluation` and `radiology-stats`; biological meaning to
`radiology-radiogenomics` only after physical alternatives are retained; and clinical use to
`radiology-translation`.

## Authoritative source ledger

- DICOM Standard Committee. [Current DICOM Standard](https://www.dicomstandard.org/current/).
- RSNA QIBA. [Profiles index](https://qibawiki.rsna.org/index.php/Profiles). Confirm the active MR
  profile, stage and conformance conditions.
- RSNA QIBA. [Diffusion-Weighted MRI and ADC Profile
  2022](https://doi.org/10.1148/QIBA/20221215).
- American College of Radiology. [Practice Parameters and Technical
  Standards](https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Practice-Parameters-and-Technical-Standards).
  Verify the current MR technical standard and local applicability.

These sources define information models or profile/technical-standard expectations. Citing them
does not prove that the dataset, reconstruction or site is conformant.
