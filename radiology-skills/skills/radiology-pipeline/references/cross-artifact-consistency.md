# Cross-artifact consistency audit

Run this audit after evidence freeze, after major revision, before a proposal or scientific deck is
frozen, and immediately before submission.

## Canonical consistency keys

Check at minimum:

- total, development, validation, external, and excluded patient/lesion counts;
- events, censoring, follow-up summary, time horizons, and endpoint definitions;
- center/scanner counts and cohort dates;
- model/signature names, reference categories, thresholds, and risk-group cut points;
- AUC/C-index/HR/OR estimates, CIs, p values, calibration and DCA summaries;
- feature counts at extraction, stability, correlation, selection, and final-model stages;
- figure/table numbering, panel labels, supplementary IDs, and manuscript callouts;
- software/version, seed, split and validation labels;
- ethics, consent, registration, accession, data/code availability, and funding statements.
- active funder/call/mechanism/year, eligibility state, review criteria, aims, milestones, budget
  assumptions and proposal evidence/claim boundaries;
- deck audience/decision, evidence-maturity labels, slide titles, speaker-note claims, image
  transformations/PHI status, source locators and rehearsal/render QA state.

## Audit order

1. Treat `reported_values.csv` as the canonical numerical source.
2. Reconcile analysis outputs and source-data files to the registry.
3. Reconcile tables and figures to the registry.
4. Reconcile proposal aims/sections/reviewer findings and deck slide map/artifact/notes/source ledger
   to the same design, claims and values.
5. Reconcile abstract, Key Results/highlights, Results, Discussion, legends, and supplement.
6. Reconcile submission forms, cover letter, checklist locations, and response letter.

## Required output

| Consistency key | Canonical value | Locations checked | Status | Action |
|---|---|---|---|---|
| development cohort n | `VAL-001` | Abstract; Fig 1; Table 1; Methods | match/mismatch | ... |

Classify mismatches:

- `BLOCKER`: changes scientific meaning, cohort identity, endpoint, or primary result.
- `MAJOR`: changes interpretation, uncertainty, figure/table linkage, or compliance.
- `MINOR`: style/rounding difference that does not alter interpretation but still needs one policy.

## Final rules

- One estimate must not appear with competing precision across outputs.
- A CI never travels without its estimate, cohort, endpoint, and timepoint.
- Internal and external validation labels are not interchangeable.
- Table 1, cohort flow, abstract, and Methods must use the same denominators.
- Figure/table edits invalidate any prose that cites their prior values.
- A changed call, criterion, aim, design lock, result, canonical value or claim ceiling invalidates
  dependent proposal text/review closure and scientific slide titles, visuals, notes and rehearsal.
- A successful deck render checks the artifact, not the science; a proposal mock-panel opinion is not
  an official funder score or funding-probability estimate.
- Response-letter claims of change must be checked against the actual revised file.

Run `../scripts/validate_research_project.py --mode submission` for structural checks, then perform
the semantic audit above. A script pass does not replace reading the content.
