# MR Spectroscopy and Spectroscopic Imaging

Load this playbook with `mr-acquisition-reconstruction.md` when single-voxel MRS or MRSI supplies a
metabolite signal, ratio, fitted concentration, spatial metabolic map or longitudinal change. A plotted
spectrum is a processed model input, not a direct assay of cellular abundance or mechanism.

## 1. Lock the spectroscopic object

Record:

- nucleus, field strength, system/software, transmit/receive coil and channel combination;
- single voxel versus MRSI, anatomical target, voxel/grid prescription, orientation, volume and the
  source images used for placement;
- sequence/localization family, TR, TE, mixing/inversion times, averages, bandwidth, dwell time,
  spectral points and acceleration;
- water/lipid suppression, outer-volume suppression, shimming method and achieved shim evidence;
- unsuppressed water or other reference acquisition, calibration phantom/reference and whether the
  output is an institutional unit, ratio, water-referenced estimate or another explicitly defined
  quantity.

Do not infer voxel placement, TE, reference or concentration unit from a spectrum screenshot or series
name. For longitudinal or lesion work, retain the prescription and image-to-voxel mapping at every
time point.

## 2. Preprocessing and fit provenance

Freeze before outcome interpretation:

`raw/FID source -> coil combination -> bad-average rejection -> frequency/phase correction -> eddy
current correction -> residual water/lipid handling -> baseline/macromolecule model -> basis set ->
lineshape/fitting algorithm -> tissue/reference correction -> reported metabolite or map`.

For each step record software/version, parameters and rejection rule. The basis set must match the
nucleus, field strength, localization sequence, TE and implemented pulse timing closely enough for the
claim; state whether it was simulated or acquired. Preserve fit range, lineshape, baseline flexibility,
macromolecule handling and all constrained/combined metabolites.

## 3. QC and uncertainty

Report definitions and distributions for linewidth, SNR, frequency drift, residual water/lipid,
fit residual, failed voxels and a fit-uncertainty measure where applicable. No universal linewidth,
SNR or relative Cramer-Rao lower-bound cutoff is supplied.

- A low relative fitting bound is not proof of accuracy, metabolite specificity or biological validity.
- Filtering only by a metabolite-relative uncertainty can preferentially remove low concentrations and
  bias group comparisons; prespecify the QC target and report excluded/failed spectra by group/site.
- For brain or heterogeneous lesions, record gray/white matter, CSF, tumour/necrosis or other tissue
  fractions and the exact correction assumption. A partial-volume correction is model-derived.
- Inspect source localization and spectrum together. A globally acceptable spectrum does not clear
  lipid contamination, misplacement or artifact in the target voxel.

## 4. Hierarchy, transport and claim boundaries

Patients are independent units unless the estimand explicitly models nested voxels, metabolites,
runs and time points. Multiple MRSI voxels or metabolites do not multiply patient n; control the
declared metabolite/voxel/contrast family.

- A metabolite ratio is not an absolute concentration and can change because either numerator or
  denominator changes.
- Water-referenced or phantom-referenced estimates remain conditional on relaxation, tissue,
  sequence, calibration and model assumptions.
- A metabolite peak can contain unresolved contributors; fitted labels are not automatically
  molecule-specific assays.
- An MRS association does not establish cell type, pathway activation, treatment response or mechanism.
- Cross-vendor/site or longitudinal equivalence requires sequence, shim, coil, reference, fit and
  task-matched phantom/test-retest evidence; post hoc site correction is adaptation.

## 5. Verdict and handoff

Return `STOP_FOR_REPAIR` when voxel identity/localization is unrecoverable, raw/reference relation is
unknown for a central quantitative claim, basis/fit provenance is incompatible or absent, artifact
dominates the target, failed spectra disappear from denominators, or technical change is inseparable
from the claimed longitudinal biology.

Return:

`spectroscopy object -> voxel/source-image map -> acquisition/reference -> preprocessing/fit chain ->
QC/failure denominator -> uncertainty/tissue correction -> repeatability/transport -> claim ceiling`.

Send disease or metabolic interpretation to `radiology-clinical-domain`, tissue/mechanism claims to
`radiology-radiogenomics`, numerical inference to `radiology-stats`, and accepted metabolite maps to
downstream imaging owners without promoting them to direct molecular measurements.

## Primary source entry points

- Wilson M, et al. [Methodological consensus on clinical proton MRS of the
  brain](https://doi.org/10.1002/mrm.27742).
- DICOM Standards Committee. [Current DICOM Standard](https://www.dicomstandard.org/current/).
- American College of Radiology. [Practice Parameters and Technical
  Standards](https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Practice-Parameters-and-Technical-Standards).

Verify the current sequence-, organ- and jurisdiction-specific source. A consensus citation does not
establish that a spectrum, fit or site meets its requirements.
