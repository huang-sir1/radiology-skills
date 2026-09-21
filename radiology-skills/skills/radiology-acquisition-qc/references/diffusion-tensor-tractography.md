# Diffusion Tensor, Advanced Diffusion, and Tractography

Load this playbook with `mr-acquisition-reconstruction.md` when the active object is a diffusion tensor,
FA/MD or related scalar, DKI/NODDI or another compartment-model output, fiber-orientation estimate,
tractogram or tract-specific measurement. These are model-derived summaries of diffusion-weighted
signal; streamlines are not directly observed axons and a scalar is not a specific histological assay.

## 1. Lock acquisition and gradient identity

Record field strength, coil, sequence/readout, TR/TE, geometry, phase-encode direction, acceleration,
all b-values, number and distribution of directions per shell, b0 images, repetitions, partial Fourier
and any reverse-phase/field-map acquisition. Preserve raw/source relation and the exact `bval/bvec` or
gradient table.

After DICOM conversion, motion correction, axis permutation or image reorientation, verify that
gradient vectors were transformed consistently. A plausible FA map does not prove a correct gradient
table. Keep repeated acquisitions and derived maps nested within the patient/examination.

## 2. Correction and model chain

Freeze:

`source DWI -> denoising/Gibbs decision -> susceptibility correction -> eddy-current/motion/outlier
handling -> gradient-nonlinearity and bias correction -> registration/resampling -> model and fit ->
scalar/orientation field -> tractography/tract segmentation -> reported quantity`.

Record software/version, interpolation, outlier replacement, mask, fit method, constraints and failure
rule. Match model complexity to acquisition support: tensor, kurtosis, multi-compartment and
multi-shell orientation models require different b-values, directions and assumptions. Do not fit a
named model merely because software emits an output.

## 3. Tractography contract

Record seed/target/exclusion ROIs and their provenance, anatomical constraints, local orientation
model, deterministic/probabilistic algorithm, step size, curvature/angle, amplitude/FA or other stop
criterion, length range, number of seeds/streamlines, filtering/weighting and software/version.

- Streamline count, density or apparent bundle volume is algorithm-dependent and is not an axon count,
  connection strength or proof of an anatomical pathway.
- Failure to reconstruct a tract is not proof of anatomical absence; crossing fibres, edema, tumour,
  low SNR, distortion and parameter choices can suppress it.
- A reconstructed pathway does not establish direction, function, effective connectivity or causality.
- If ROIs or tract parameters were chosen after observing group/outcome differences, label the result
  exploratory and require independent confirmation.

## 4. QC, hierarchy and claim boundaries

Inspect motion/outlier burden, signal dropout, susceptibility and eddy residuals, target-level
registration, orientation plausibility, fit residuals and failed voxels/tracts. Preserve maps showing
QC and report excluded/non-evaluable patients rather than only successful tractograms.

- FA, MD, AD, RD, kurtosis and compartment fractions are model-derived and non-specific; changes can
  reflect multiple tissue, free-water, crossing-fibre, edema, acquisition or processing effects.
- Voxels, directions, fixels, streamlines, nodes and bilateral tracts are nested observations, not
  independent patients.
- Along-tract nodes, bundles, metrics, contrasts and parameter variants form a multiplicity family.
- Longitudinal change must exceed task-matched repeatability and remain bounded by registration,
  lesion/anatomy change and protocol stability.
- Cross-site equivalence requires gradient, coil, sequence, correction, model and task-matched
  phantom/test-retest evidence. Harmonising a scalar does not validate orientation or tract topology.

## 5. Verdict and handoff

Return `STOP_FOR_REPAIR` when gradient identity/orientation is unrecoverable, acquisition cannot
support the claimed model, distortion/registration breaks target localization, tract/ROI selection is
outcome-circular, failed tracts disappear from denominators, or a protocol/model change determines the
central longitudinal or cross-site result.

Return:

`diffusion object -> acquisition/gradient table -> correction/model chain -> tractography contract ->
QC/failure denominator -> hierarchy/multiplicity -> repeatability/transport -> claim ceiling`.

Send anatomical/disease interpretation to `radiology-clinical-domain`, mechanism claims to
`radiology-radiogenomics`, numerical inference to `radiology-stats`, and accepted maps/tracts to
downstream owners as model-derived objects, never direct fibers or histology.

## Primary source entry points

- Jones DK, et al. [White matter integrity, fiber count, and other fallacies: the do's and don'ts of
  diffusion MRI](https://doi.org/10.1016/j.neuroimage.2012.06.081).
- DICOM Standards Committee. [Current DICOM Standard](https://www.dicomstandard.org/current/).
- American College of Radiology. [Practice Parameters and Technical
  Standards](https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Practice-Parameters-and-Technical-Standards).

Verify the current acquisition-, model-, anatomy- and jurisdiction-specific source. A software output
or anatomically plausible rendering does not establish biological validity.
