# The evidence layer — publication patterns, not a fixed citation list

This file encodes **how high-impact venues tend to publish imaging-AI work** so recommendations
are grounded in evidence, not taste. It is deliberately **citation-free**: durable patterns are
stated here; concrete recent papers (PMID/DOI) are retrieved and verified **live** via
`radiology-search`. Never present a specific paper from memory as verified.

## How to use this layer honestly

1. State the **pattern** (what kind of study this venue rewards and the bar it meets).
2. Map the user's question to the pattern (does it clear the bar?).
3. Emit a **Verify-now** item: the exact live search to confirm currency, the open gap, and any
   specific recent claim before it is written into a manuscript.

## Journal publication-pattern heuristics (orientation; confirm with current scope + live search)

| Venue (tier) | Tends to reward | Methodological bar it enforces |
|---|---|---|
| **Radiology / Radiology: AI** (specialty flagship) | Clinically framed imaging-AI/radiomics with rigorous reporting | External/independent validation, calibration + DCA, reader context, EQUATOR (CLAIM/CLEAR/TRIPOD+AI), reproducible features |
| **Lancet Digital Health / Lancet Oncology** (clinical, high) | Clinical impact, generalisability, prospective or strong multi-center | Large/multi-center, external or prospective validation, clinical-utility framing |
| **Nature Medicine** (clinical, top) | Clinically transformative, often prospective / multi-cohort | Strong external/prospective evidence, fairness, clinical readiness |
| **Nature Communications / Cell Reports Medicine** (broad, high) | Methodological novelty + biological/clinical insight | Solid validation + mechanism or broad significance |
| **npj Digital Medicine / npj Precision Oncology** (digital/precision) | Digital-health or precision-oncology angle, translational | Validation + clinical/biological relevance, open science |
| **eClinicalMedicine / eBioMedicine** (clinical/translational) | Clinically useful, translational studies | Clear clinical question, adequate validation |

> These are **patterns**, not guarantees. Scope, fit, and current preferences must be checked
> against the journal's live aims (see `radiology-search` and `radiology-citation` scope files),
> and journal tiering for a finished paper belongs to `radiology-journal`.

## Cross-cutting patterns that travel across venues (2023–2026 direction of travel)

- **External/independent validation is increasingly a baseline expectation**, not a bonus —
  internal-only studies are pushed down-tier.
- **Calibration and decision-curve / net-benefit** are expected for clinical prediction models,
  alongside discrimination.
- **Reporting-guideline compliance** (CLAIM 2024, TRIPOD+AI, CLEAR/METRICS, IBSI) is checked by
  reviewers and required at submission for top venues.
- **Open science** (code, models, feature tables, data-availability) is weighted more heavily.
- **Generalisability and fairness** (multi-center, subgroup, scanner robustness) attract scrutiny.
- **Clinical utility / reader studies / prospective evidence** distinguish top-tier from solid.
- **Biological grounding** (radiogenomics / mechanism) strengthens otherwise correlational work.

## What "evidence basis" must NOT become

- A list of invented PMIDs or "a 2024 Radiology study found…" with no live verification.
- Treating a handful of seed papers as a systematic review.
- Asserting a gap is open without checking it is still open today.

## Output for an evidence-grounded recommendation

```
Direction:
Publication pattern (venue tier + what it rewards + the bar):
Does the user's question clear the bar? (yes / conditional / no — why):
Verify now (live search):  query → confirm gap → fetch & verify seed PMIDs (→ radiology-search)
```
