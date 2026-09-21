# Projection Radiography, Mammography, and DBT

Use this playbook for general projection radiography, portable/mobile radiography, full-field
digital mammography, digital breast tomosynthesis (DBT), synthetic 2D images and
contrast-enhanced mammography. The examination is a multi-view event; a projection, DBT slice or
synthetic image is not an independent patient.

## Lock the measurement and presentation object

| Object | Minimum identity lock | Frequent invalid upgrade |
|---|---|---|
| general radiographic finding or geometry | body part, projection/view, position, source-detector geometry, exposure system and processing version | treating AP/PA, supine/upright or mobile/fixed images as exchangeable |
| serial chest or device-position comparison | view/position, inspiration, geometry, detector/processing and prior-selection rule | calling projection/position change biological progression |
| mammographic finding/density | modality, breast/laterality, CC/MLO/additional view, compression and processing | treating views as independent or synthetic 2D as acquired FFDM |
| DBT lesion/architectural measurement | acquisition arc/system, reconstruction/version, slice geometry and view set | treating reconstructed slices as independent observations |
| contrast-enhanced mammography quantity | agent/dose/timing, low/high energy pair, recombination/subtraction algorithm and unit | treating recombined intensity as universal concentration |

Identify whether pixels are original/for-processing, for-presentation, synthetic, recombined,
secondary capture or screenshot. If provenance is absent, mark `AUTHOR_INPUT_NEEDED`.

## General projection radiography chain

Record:

- CR/DR/mobile/fixed system, manufacturer/model, detector, acquisition station and software;
- body part, projection (AP/PA/lateral/oblique/etc.), patient position, weight-bearing/upright status,
  laterality, source-to-image distance, object-to-detector geometry, centering and collimation;
- grid use, tube potential, tube current-time/exposure, automatic exposure control and exposure
  index/deviation index with the vendor/standard convention;
- detector pixel matrix/spacing, binning, anti-scatter/processing settings and rejected/repeated
  exposures when available;
- image-processing algorithm/version, presentation intent, photometric interpretation, shutters,
  annotations/markers and burned-in content;
- dose descriptors when present, with exact meaning and provenance rather than a patient-dose
  inference.

Exposure index is not interchangeable across undefined conventions and is not a direct patient-dose
measurement. Window/level or display processing can change appearance without changing acquired
signal; screenshots may discard source dynamic range and metadata.

### Mobile and serial radiography

Explicitly model:

- mobile versus department acquisition, detector/system and processing;
- AP versus PA, supine/semi-upright/upright, inspiration, rotation and source distance;
- tubes/lines/devices, laterality markers, bed/ICU background and portable-machine artifacts;
- clinical location and acquisition period as potential outcome-correlated shortcuts;
- which prior image/time point is available and whether prior selection mirrors intended use.

A model can learn site, device, marker or care-setting signatures. Artifact masking alone does not
repair an outcome-confounded acquisition pathway.

## Mammography and DBT chain

### Examination and positioning

- FFDM, DBT, synthetic 2D, contrast-enhanced mammography or combination;
- breast/laterality, CC/MLO and additional/spot/magnification views, implant/displacement status and
  prior-exam availability;
- positioning/tissue inclusion, nipple profile, pectoral coverage where applicable, motion/fold/
  artifact adequacy and repeat/reject status;
- compressed breast thickness, compression force and paddle/geometry when available.

### Acquisition, reconstruction and presentation

- system/detector/model/software, target/filter or spectral mode, kVp/mAs, AEC and detector
  calibration/QC state;
- average glandular dose or other displayed dose descriptor with its source and limitation;
- for DBT: acquisition arc/projections if recoverable, reconstruction algorithm/version, slice
  thickness/spacing, slab/synthetic outputs and image-processing version;
- for synthetic 2D: the source DBT series and synthesis product/version—never label it acquired
  FFDM;
- for contrast-enhanced mammography: agent/dose, injection and acquisition timestamps, low/high
  energy pairing, subtraction/recombination method/version and motion/registration;
- workstation/display/hanging protocol and whether interpretation uses source-resolution images,
  priors and the full view set.

Preserve the patient/exam/view hierarchy. Paired breasts or views can be legitimate analysis units
only with an estimand and model that retain within-patient dependence.

## Series/view-selection lock

Before outcomes or model performance are inspected, freeze:

1. required exam types and complete view set;
2. diagnostic versus screening, standard versus additional views and prior-image policy;
3. original/for-processing versus presentation/synthetic/recombined object rule;
4. inclusion/exclusion for motion, positioning, implants, missing views and repeats;
5. DBT slice/slab/volume sampling and how multiple objects are grouped;
6. adjudication and logging for ambiguous views or incomplete exams.

Do not select one “most suspicious” view with knowledge of the label unless that selection is the
prespecified clinical workflow being evaluated.

## Artifact and shift map

| Threat | Likely effect | Required action |
|---|---|---|
| projection/position/inspiration/rotation | anatomy and apparent severity change | view/position lock; stratified or paired sensitivity |
| collimation, distance, magnification or detector geometry | scale and context change | geometry metadata; calibration and measurement rule |
| under/overexposure or processing/version shift | noise, contrast, texture and visibility change | exposure/processing ledger; raw/presentation sensitivity |
| motion, folds, skin lines, grid/processing artifacts | false or obscured finding | target-level QC and repeat/reject rule |
| marker, text, border, device or site background | shortcut and leakage | audit association with site/outcome; preserve raw primary |
| mammographic positioning/tissue exclusion | missed anatomy and density/lesion bias | exam-level adequacy; failure rate; qualified review |
| FFDM/DBT/synthetic/recombined mixing | non-equivalent information content | object-type stratification; version lock; paired evidence |
| software/detector/system upgrade | transport and longitudinal shift | change ledger; phantom/clinical bridging; temporal holdout |

## Verdict and handoff

- `PASS` when exam/view completeness, projection/position, detector/exposure, object type,
  processing/reconstruction, presentation and target-level QC are traceable and fit the claim.
- `CONDITIONAL` for a narrower acquisition type, site, view, presentation object or relative claim
  with explicit incomplete/nondiagnostic handling.
- `STOP` for wrong/unknown view or object type, label-informed view selection, missing central
  exam components, non-identifiable processing, severe target-overlapping inadequacy, or an
  unbounded mobile/site/system shift that determines the claim.

Send disease/exam eligibility to `radiology-clinical-domain`; admissible view/lesion geometry to
`radiology-annotation`; accepted presentation/source objects to `radiology-deep-learning` or
`radiology-radiomics`; reader display/presentation and nondiagnostic workflow to
`radiology-translation`; and comparative inference to `radiology-method-evaluation` and
`radiology-stats`.

## Authoritative source ledger

- DICOM Standard Committee. [Current DICOM Standard](https://www.dicomstandard.org/current/).
- American College of Radiology. [Practice Parameters and Technical
  Standards](https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Practice-Parameters-and-Technical-Standards).
  Verify the current standards for radiographic equipment, digital radiography, mammography and
  breast tomosynthesis.
- American College of Radiology, American Association of Physicists in Medicine, and Society for
  Imaging Informatics in Medicine. [Practice Parameter for Determinants of Image Quality in
  Mammography](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/dig-mamo.pdf).
- American College of Radiology. [Technical Standard for Diagnostic Medical Physics Performance
  Monitoring of Radiographic
  Equipment](https://gravitas.acr.org/PPTS/GetDocumentView?docId=120).
- American College of Radiology. [Practice Parameter for the Performance of Screening and
  Diagnostic
  Mammography](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/Screen-Diag-Mammo.pdf).

Verify the live document version, approval status, jurisdiction and whether it applies to the
specific FFDM, DBT, synthetic or contrast-enhanced object. A technical-standard citation is not
dataset or device conformance evidence.
