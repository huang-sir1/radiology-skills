# The evidence layer — publication patterns, not a fixed citation list

This file supplies search hypotheses about venue fit and task-specific evidence needs. These
heuristics are not a measured publication-pattern study or current editorial requirements. Verify
material claims with primary literature and the named venue's current instructions before using
them to rank a current research opportunity. Never present a remembered paper as verified.

## How to use this layer honestly

1. State the candidate fit and the question whose value is being assessed.
2. Retrieve current primary studies and, when venue fit matters, the current scope and article-type
   instructions. Record query, date, eligibility, source locators and limited-search status.
3. Map the user's question to verified evidence and task-specific methodological requirements.
   Keep untested venue generalizations and open-gap claims `PROVISIONAL_SHORTLIST`; verify them
   before presenting a current recommendation, not only before manuscript drafting.

## Journal publication-pattern heuristics (orientation; confirm with current scope + live search)

| Venue (orientation only) | Candidate fit to investigate | Evidence questions to verify for the task/article type |
|---|---|---|
| **Radiology / Radiology: AI** (specialty flagship) | Clinically framed imaging-AI/radiomics, technical development and data resources | Validation matched to intended claim; calibration for risk estimates, DCA only for a defined threshold-to-action decision, reader evidence where relevant, and applicable reporting/measurement frameworks |
| **Lancet Digital Health / Lancet Oncology** (clinical, high) | Clinical impact, generalisability, prospective or strong multi-center | Large/multi-center, external or prospective validation, clinical-utility framing |
| **Nature Medicine** (clinical, top) | Clinically transformative, often prospective / multi-cohort | Strong external/prospective evidence, fairness, clinical readiness |
| **Nature Communications / Cell Reports Medicine** (broad, high) | Methodological novelty + biological/clinical insight | Solid validation + mechanism or broad significance |
| **npj Digital Medicine / npj Precision Oncology** (digital/precision) | Digital-health or precision-oncology angle, translational | Validation + clinical/biological relevance, open science |
| **eClinicalMedicine / eBioMedicine** (clinical/translational) | Clinically useful, translational studies | Clear clinical question, adequate validation |

> These are **patterns**, not guarantees. Scope, fit, and current preferences must be checked
> against the journal's live aims (see `radiology-search` and `radiology-citation` scope files),
> and journal tiering for a finished paper belongs to `radiology-journal`.

## Task-specific evidence questions

- External validation supports transport claims. Internal-only development can support a bounded
  development or feasibility claim; do not infer a universal venue downgrade from that feature.
- Evaluate calibration when predicted probabilities or risks are used. DCA requires a defined
  decision, defensible action thresholds/error trade-offs and appropriate population prevalence;
  it is not a generic checklist item for reconstruction, segmentation or every classifier.
- Select CLAIM, TRIPOD+AI, CLEAR/METRICS or other reporting frameworks by study/task scope;
  IBSI concerns radiomic measurement standardisation and is not a universal submission checklist.
  Verify the exact venue requirement and current version rather than stacking every framework.
- Code, models, data availability and controlled-access options should support reproducibility
  within consent and licence conditions. Public patient-data release is not a universal requirement.
- Subgroups, scanner/site variation and external evidence must match the intended population and
  claim. Reader, prospective and patient-impact studies answer different questions.
- Molecular/pathology evidence is relevant to a biological claim; adding an omics analysis does not
  automatically validate a prediction study or improve its scientific value.

## Primary verification entry point

- [Radiology: Artificial Intelligence author instructions](https://pubs.rsna.org/page/ai/author-instructions)
  (accessed 2026-09-04): article types and applicable reporting checklists differ. Use the current
  section for the actual submission type; this source does not establish the preferences of other
  journals or require DCA for every imaging-AI study.

## What "evidence basis" must NOT become

- A list of invented PMIDs or "a 2024 Radiology study found…" with no live verification.
- Treating a handful of seed papers as a systematic review.
- Asserting a gap is open without checking it is still open today.

## Output for an evidence-grounded recommendation

```
Direction:
Scientific value and task-specific evidence need:
Verified venue fit, if relevant (source/date/article type), or provisional hypothesis:
Does the user's data support the question and intended claim? (yes / conditional / no — why):
Evidence checked and remaining search (query/date/coverage/verified seeds → radiology-search):
```
