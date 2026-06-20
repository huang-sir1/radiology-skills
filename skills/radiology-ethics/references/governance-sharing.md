# Governance & lawful sharing — consent must permit what you promise

The Ethics/consent and the **Data Availability** statement must be consistent: you cannot promise
open data the consent doesn't allow. This file frames the governance; statement templates and
repository choice live in `radiology-data`.

## Privacy frameworks (name the one that applies; defer specifics to the institution)

| Framework | Region | Imaging-relevant points |
|---|---|---|
| **HIPAA** | US | "Safe Harbor" (remove 18 identifiers) or "Expert Determination"; covered entities |
| **GDPR** | EU/EEA | Personal data incl. health; lawful basis; pseudonymisation ≠ anonymisation; cross-border transfer rules |
| **PIPL** | China | Personal information protection; sensitive-data consent; data-export assessment |
| Local/institutional | Everywhere | Hospital policy + DUA may be stricter than statute |

## Access tiers for shared research data

- **Open** — de-identified imaging, radiomic feature tables, code/models (after de-id) → public
  repository + accession.
- **Registered** — access after registration/light agreement.
- **Controlled** — genomic and some clinical data → data-access committee + DUA (dbGaP/EGA).
- **Restricted / not shareable** — name the controller and the conditions; avoid bare "available
  on reasonable request" (editors increasingly reject it).

## Data-use agreements (DUA)

- Govern transfer between institutions and to repositories; specify permitted use,
  re-sharing limits, and security.
- A multi-center study usually needs DUAs **before** pooling data; mention them when relevant.

## Consistency check (do this every time)

1. What does the **consent/waiver** permit (use, sharing, secondary use, genomics)?
2. What does the **Data Availability** statement promise (`radiology-data`)?
3. Do (1) and (2) match? If the statement promises more than consent allows → fix the statement
   (downgrade to controlled/restricted), not the ethics.

## Governance note template

```
Imaging data are available [openly via <repository>, accession XXX / under controlled access via
<committee>] following de-identification. Genomic data are available under controlled access
(<EGA/dbGaP>, accession XXX) subject to a data-use agreement, consistent with participant
consent and [HIPAA/GDPR/PIPL] and institutional policy. Code is available at <repo + DOI>.
```

## Handoff

- Repository selection, de-id mechanics, DataCite citations, FAIR → `radiology-data`.
- Reporting-guideline data/open-science items → `radiology-reporting`.
