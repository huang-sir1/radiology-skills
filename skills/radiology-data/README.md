# radiology-data

**Data/Code Availability statements, DICOM de-identification, repository selection, dataset
citations, and FAIR checks** — for imaging and imaging+omics (radiogenomics) submissions to
_Radiology_.

## What it does
- Drafts submission-ready **Data Availability** and **Code/Model Availability** statements.
- Plans **DICOM de-identification** (header tags + burned-in pixel PHI + defacing).
- Chooses repositories: images (TCIA/Zenodo), features/code/models (Zenodo/GitHub + DOI),
  expression (GEO), controlled genomics (dbGaP/EGA).
- Writes DataCite-style dataset citations; runs a FAIR check; handles controlled-access
  wording.

## Reference files
```
references/
├── dicom-deidentification.md   DICOM tags, pixel PHI, defacing, standards/tools
├── repositories.md             where to deposit images / features / code / omics
└── availability-and-fair.md    statement templates, dataset citations, FAIR, 中文对齐
```

## Example prompts
- "Write the Data Availability statement; images go to TCIA, code to Zenodo, RNA-seq to GEO."
- "How do I de-identify and deface these brain MRIs before public release?"
- "We have dbGaP-controlled germline data — word the availability honestly."

## Integrity
Never overstates availability or invents accessions; describes restricted data honestly. Not
legal advice — confirm consent/DUA/IRB with your institution.
