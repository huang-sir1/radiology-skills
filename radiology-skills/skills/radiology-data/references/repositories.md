# Choosing repositories

Map each data type to a durable repository with a **persistent identifier**.

| Data type | Preferred repository | Identifier / notes |
|---|---|---|
| De-identified imaging (DICOM) | **TCIA**; or Zenodo/Figshare for smaller sets | TCIA collection DOI; follow TCIA de-id |
| Radiomic **feature tables** | **Zenodo** / Figshare (+ the IBSI parameter file) | DOI; share values, not just description |
| Code / pipelines | **GitHub/GitLab** + a **Zenodo release DOI** (archival) | tagged release → citable DOI |
| Trained models / weights | Zenodo / Hugging Face (license-aware) | DOI; state license + intended use |
| Bulk expression / array / seq | **GEO** (or BioStudies) | GSE accession |
| Controlled-access genomics (germline, raw) | **dbGaP** (US) / **EGA** (EU) | accession + **DUA**; honest restricted wording |
| Single-cell / spatial | GEO + Single Cell Portal / Zenodo; HCA | accession + processed objects |
| General/other | **Zenodo**, Dryad, OSF, Figshare | DOI |

> **Repository status notes.** ArrayExpress retired 2022; legacy accessions (E-MTAB etc.)
> resolve via BioStudies — cite it only as a legacy lookup, never as a deposition target. The
> HCA (Human Cell Atlas) Data Portal's long-term persistence and deposition capacity are
> uncertain — verify current deposition/retrieval status before committing.

## Principles
- Prefer **mandated/discipline-specific** repositories (TCIA for cancer imaging, GEO for
  expression) over a generic one when available.
- Get a **persistent identifier** (DOI/accession) — not a personal/lab URL.
- Match **license** to intent (e.g. CC-BY for data, an OSI license for code); state it.
- For radiogenomics, deposit imaging (TCIA), features (Zenodo), and omics (GEO/dbGaP)
  separately and **cross-reference** them in the availability statement.

## Restricted data
If data cannot be public (privacy/consent/DUA/commercial), state: the **reason**, the
**controller/steward**, the **review/access process**, and the **conditions/timeline** — not
just "on request."

## Nature-portfolio: Source Data is separate from all of the above
Figure-level raw values (Source Data) are not a "repository choice" like the table above — they
travel with the manuscript itself. Don't conflate "I deposited the dataset in TCIA/GEO" with
"I provided Source Data for Figure 2" — a reviewer may ask for both. See
`availability-and-fair.md` for the Extended Data / Supplementary Information / Source Data
distinction and the "condition of publication" wording.
