# Re-identification risk in imaging + omics

Re-identification is a spectrum. Identify the specific risks in the data and the mitigation for
each. De-identification *mechanics* live in `radiology-data`; this file is the *risk read*.

## Risk sources

| Source | Risk | Mitigation |
|---|---|---|
| **DICOM metadata** | Names, IDs, dates, institution, device serials, private tags | De-id headers to a standard (e.g. DICOM PS3.15 profile); remove/replace; keep an audit |
| **Burned-in pixel text** | PHI rendered into the image (US, screenshots) | Detect and redact pixel PHI before sharing |
| **Facial reconstruction** | Head CT/MRI can reconstruct a recognisable face | **Defacing / skull-stripping** for head imaging |
| **Dates & ages** | Exact dates + rare events can re-identify | Date-shift consistently per patient; cap extreme ages (e.g. ≥89) |
| **Small / rare-disease cohorts** | Few patients → uniqueness | Aggregate, suppress small cells, or controlled access |
| **Geography / site** | Small-area + rare disease | Coarsen location; avoid identifying small centers |
| **Genomic data** | Inherently identifying; cannot be fully anonymised | **Controlled access** (dbGaP/EGA); never open-post raw germline |
| **Linkage** | Combining quasi-identifiers across tables | Minimise shared quasi-identifiers; review joint risk |

## Imaging-specific must-dos before any sharing

1. Strip DICOM header PHI (and private tags) to a recognised profile.
2. Remove burned-in pixel PHI.
3. **Deface** head imaging.
4. Shift dates consistently; generalise extreme ages.
5. Re-check after conversion (NIfTI metadata can re-introduce identifiers).

## Genomics + imaging (radiogenomics) note

- Genomic data are **not** anonymisable; pairing them with imaging raises joint risk.
- Default to **controlled access** for the molecular layer (dbGaP/EGA), with a data-access
  committee; imaging may be shareable separately after de-identification.
- The consent must cover genomic data generation and sharing (→ approval-consent.md).

## Risk-read output

```
Data types & identifiers present:
Re-identification risks (ranked):
Mitigations applied / planned:   [de-id profile, defacing, date-shift, suppression, controlled access]
Residual risk & access model:    [open / registered / controlled / not shareable]
```

## Reporting sentence

*"All imaging was de-identified (DICOM headers per [profile]; burned-in PHI removed) and head
studies were defaced; dates were shifted per patient. Genomic data are available under controlled
access (EGA, accession [XXX]) via a data-access committee, consistent with participant consent."*
