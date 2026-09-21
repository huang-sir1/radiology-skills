# Functional MRI: Task, Resting-State, and BOLD Measurement

Load this playbook with `mr-acquisition-reconstruction.md` when the active measurement is task fMRI,
resting-state fMRI, BOLD activation, functional connectivity or a derived functional map. BOLD is a
hemodynamic signal shaped by acquisition, physiology and neurovascular coupling; it is not a direct
measurement of neuronal firing, cognition or causal network direction.

## 1. Freeze the functional estimand

State whether the target is task activation/contrast, resting connectivity, network organization,
laterality, longitudinal change, prediction or another named quantity. Record the patient-level
estimand, anatomical scope, contrast/network definition, time point and intended claim before choosing
ROIs, thresholds or a favorable map.

For task fMRI record stimulus/task version, timing, blocks/events, response device, instructions,
practice, accuracy/reaction-time or other compliance evidence, language/handedness where material and
the information available to the analyst. Nonperformance is not equivalent to absent activation.

For resting-state fMRI record instructions, eyes open/closed/fixation, vigilance/sedation, run duration,
discarded volumes and physiological/behavioral state. “Rest” is not a standardized biological state.

## 2. Acquisition and preprocessing chain

Record field strength, coil, pulse sequence, TR/TE/flip angle, multiband/acceleration, phase-encode
direction, voxel geometry, slice timing/order, run length, field map or reverse-phase images,
structural reference and cardiac/respiratory monitoring when available.

Freeze:

`DICOM/raw runs -> distortion and motion correction -> slice-time decision -> susceptibility/anatomic
registration -> nuisance/physiology model -> censoring/scrubbing -> temporal/spatial filtering ->
first-level model or time series -> subject map/connectivity -> group model`.

Record software/version, transforms, interpolation, smoothing kernel, temporal filter, motion metrics,
nuisance regressors, global-signal decision, censoring threshold and lost volumes. Different valid
preprocessing choices can answer different estimands; disclose primary and sensitivity pipelines
rather than selecting the most favorable result.

## 3. Circularity, multiplicity and independent units

- Define anatomical/functional ROIs from independent data, training data or a nested procedure. Do not
  select voxels using the same contrast and report their effect as independent confirmation.
- State voxel/cluster/edge/network multiplicity control and the complete tested family. A thresholded
  color map is not the inferential result.
- Runs, volumes, voxels, edges and repeated contrasts are nested within participants; they do not
  replace patient-level replication.
- Keep exploratory whole-brain discovery separate from a locked ROI/contrast confirmation.
- Resting correlation, anticorrelation, Granger-style direction or effective-connectivity model output
  remains model-dependent; association is not anatomical connection or causal influence.

## 4. Artifact, physiology and disease boundaries

Audit motion and motion-by-group differences, susceptibility dropout/distortion, vascular lesions,
medication, caffeine, sedation, pain, sleep/vigilance, breathing/cardiac variation and scanner/run
drift. In tumours, stroke, vascular disease or treatment studies, altered neurovascular coupling can
change BOLD without the claimed neuronal change.

For longitudinal/multicentre claims, compare task version/performance, coil, sequence, phase encoding,
physiology capture, preprocessing and software. Require task-matched repeatability and retain failed or
noncompliant runs in the denominator. Evaluation-site denoising, atlas tuning or threshold selection is
adaptation, not untouched external validation.

## 5. Verdict and handoff

Return `STOP_FOR_REPAIR` when participant/run identity is broken, task timing or compliance is central
but unavailable, motion/distortion dominates the target, first-level contrasts are unreconstructable,
ROI/threshold selection is circular, failed runs vanish from the cohort flow, or preprocessing/site
change determines the central result without a bounded sensitivity.

Return:

`functional estimand -> task/rest state -> acquisition/run hierarchy -> preprocessing/design matrix ->
motion/physiology/failure audit -> ROI/multiplicity boundary -> patient-level inference ->
repeatability/transport -> claim ceiling`.

Clinical localization or individual presurgical decisions remain with qualified clinical teams.
Numerical group inference routes to `radiology-stats`; biological/network interpretation routes to
`radiology-clinical-domain` or `radiology-radiogenomics` at the surviving evidence ceiling.

## Primary source entry points

- Nichols TE, et al. [Best practices in data analysis and sharing in neuroimaging using MRI
  (COBIDAS)](https://doi.org/10.1038/nn.4500).
- DICOM Standards Committee. [Current DICOM Standard](https://www.dicomstandard.org/current/).
- American College of Radiology. [Practice Parameters and Technical
  Standards](https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Practice-Parameters-and-Technical-Standards).

Verify the current task-, disease- and jurisdiction-specific source. Reporting a preprocessing package
or threshold does not establish measurement validity.
