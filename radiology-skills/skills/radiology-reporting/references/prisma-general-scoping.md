# General and scoping evidence-synthesis reporting

Use this contract only after `radiology-systematic-review` has fixed the review family and frozen
the protocol/search/screening/extraction/synthesis evidence. Reporting cannot repair an invalid
review by filling a checklist.

Official/current entry points (re-verify at submission or major revision):

- PRISMA 2020 statement and checklist: <https://www.prisma-statement.org/prisma-2020> and
  <https://www.prisma-statement.org/prisma-2020-checklist>
- PRISMA-ScR: <https://www.prisma-statement.org/scoping> and
  <https://www.equator-network.org/reporting-guidelines/prisma-scr/>
- PRISMA-S search-reporting extension:
  <https://www.equator-network.org/reporting-guidelines/prisma-s/>
- PRISMA-P protocol reporting:
  <https://www.equator-network.org/reporting-guidelines/prisma-protocols/>
- PRISMA-LSR living-review reporting:
  <https://www.equator-network.org/reporting-guidelines/prisma-lsr/>
- PRISMA-COSMIN for outcome measurement instrument reviews:
  <https://www.equator-network.org/reporting-guidelines/guideline-for-reporting-systematic-reviews-of-outcome-measurement-instruments-omis-prisma-cosmin-for-omis-2024/>

Record source URL, downloaded checklist identity/version, access date, target-journal overlay and
whether the article is an original, updated, living, static or retired review.

## Route gate

| Review object | Primary reporting contract | Important boundary |
|---|---|---|
| focused systematic review/meta-analysis | PRISMA 2020 | pooling is not required; infeasible pooling does not convert it into a scoping review |
| scoping review/evidence map | PRISMA-ScR | the goal is mapping/characterising evidence, not estimating a narrowly defined pooled effect |
| diagnostic-accuracy review | PRISMA-DTA in `stard-prisma-quadas.md` | do not replace its DTA items with the general-only table |
| search methods needing detailed reproducibility audit | applicable primary route + PRISMA-S | PRISMA-S is an adjunct, not the primary whole-report checklist |
| review protocol | PRISMA-P | protocol item audit does not prove registration, screening or completed-review conduct |
| living systematic review | PRISMA 2020 + PRISMA-LSR | report surveillance/update methods, each update, changed evidence and transition/retirement; a `LIVING` label alone is insufficient |
| outcome measurement instrument review | PRISMA-COSMIN for OMIs | activate only when measurement properties/instruments are the review object, not for every ICC or method-comparison meta-analysis |

## PRISMA 2020 items 1-27: item-by-item audit map

Audit each official item/sub-item, but use these compact prompts rather than copying checklist text.

| Item | Audit prompt |
|---|---|
| 1 | title identifies the report as a systematic review |
| 2 | abstract follows the PRISMA abstract elements |
| 3–4 | rationale and explicit objective/question are stated |
| 5 | eligibility criteria and grouping logic for syntheses are reproducible |
| 6 | every information source and its last-search/contact date is named |
| 7 | complete reproducible search strategies, limits and filters are supplied |
| 8 | selection process, reviewer number/independence and automation are reported |
| 9 | extraction process, reviewer number/independence, confirmation and automation are reported |
| 10a–10b | outcomes and all other sought variables, definitions and assumptions are stated |
| 11 | risk-of-bias method, reviewers and resolution process are reported |
| 12 | effect measures match each outcome/estimand |
| 13a–13f | eligibility for each synthesis, preparation, display, model, heterogeneity and sensitivity methods are traceable |
| 14–15 | reporting-bias and certainty-assessment methods are stated |
| 16a–16b | search/selection results and exclusions with reasons reconcile with the flow diagram |
| 17–18 | included-study characteristics and study-level risk-of-bias results are presented |
| 19–20a–20d | individual results, synthesis estimates/uncertainty/heterogeneity, investigations and sensitivities are reported |
| 21–22 | reporting-bias and certainty results are reported |
| 23a–23d | interpretation, evidence limitations, review-process limitations and implications are separated |
| 24a–24c | registration, protocol access and amendments are traceable |
| 25–27 | support/funder role, competing interests and availability of forms/data/code/materials are stated |

`PRESENT` requires an exact manuscript/supplement/registry location and agreement with frozen review
artifacts. A flow diagram whose counts do not reconcile is `PARTIAL` or `MISSING`, not present.

## PRISMA-ScR items 1-22: item-by-item audit map

| Item | Audit prompt |
|---|---|
| 1–4 | title/abstract/rationale/objectives clearly identify and justify a scoping approach with population/participants, concept and context as applicable |
| 5–8 | protocol/registration, eligibility, sources/dates and reproducible search are reported |
| 9–11 | source selection, charting process and charted variables/assumptions are traceable |
| 12 | if critical appraisal was performed, rationale, method and use are reported; if not, do not invent it |
| 13 | charted-data handling and summary methods match the mapping objective |
| 14–18 | selection counts, source characteristics, appraisal results if any, source-level results and mapped synthesis reconcile |
| 19–21 | main mapping findings, process limitations and evidence-based implications/next steps are separated |
| 22 | review funding, funder role and funding of included sources are reported as applicable |

Do not use AMSTAR-2 or ROBIS as a substitute for PRISMA-ScR. Critical appraisal can be optional for
a scoping review, but the choice and its consequence for interpretation must be explicit.

## Search-reporting adjunct

When search reproducibility is claim-bearing, add a PRISMA-S receipt covering named sources and
interfaces, full line-by-line strategies, dates, peer review, limits, deduplication, updates,
supplementary methods, contacts/grey literature and exact search files. Consume the frozen
search-strategy peer-review receipt from `radiology-systematic-review`; do not mark the search
complete from a narrative Methods sentence alone.

## Protocol, living-review and measurement-instrument overlays

- **PRISMA-P:** audit the official protocol checklist item-by-item for identity/registration,
  rationale/objectives, eligibility, sources/search, study records, outcomes, risk of bias,
  synthesis, meta-bias/certainty, amendments, contributors, support and conflicts. Bind each item to
  the frozen protocol version; later completed-review choices cannot be backfilled as if prespecified.
- **PRISMA-LSR:** add the official extension to PRISMA 2020 and bind the surveillance schedule,
  search/update triggers, screening/incorporation process, changed-study ledger, effect/certainty
  changes, version history, transition out of living mode and retirement. `LIVING`, `STATIC` and
  `RETIRED` are reported states with evidence, not branding.
- **PRISMA-COSMIN for OMIs:** when the review object is an outcome measurement instrument, audit the
  specialist official checklist and record construct, population/context, measurement properties,
  instrument versions, property-specific appraisal/synthesis and recommendation boundary. Do not
  force it onto ordinary reliability, segmentation-agreement or method-comparison reviews whose
  object is not an outcome measurement instrument.

## Output

Return `Guideline item | PRESENT/PARTIAL/MISSING/NA | exact location | frozen evidence locator |
conflict or omission | minimum repair | owner | closure evidence`. Then reconcile checklist counts,
flow diagram, excluded-study table, extraction/synthesis artifacts, abstract, main text,
supplement, registration and data/code availability.
