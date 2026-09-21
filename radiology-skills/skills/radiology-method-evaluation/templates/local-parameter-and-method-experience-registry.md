# Local parameter and method experience registry

Use this registry for institution-, laboratory-, platform-, tissue- or workflow-specific experience.
It is a source of auditable practice knowledge, not a universal default table.

## Registry governance

- Registry ID/version/owner/date: [LOCAL_INPUT_NEEDED]
- Institution/laboratory/team: [LOCAL_INPUT_NEEDED]
- Allowed users and privacy/de-identification rule: [LOCAL_INPUT_NEEDED]
- Evidence classes: `LOCAL_RUN_VERIFIED`, `AUTHOR_REPORTED`, `DOCUMENTED_EXTERNAL`,
  `SUPERSEDED`, `NOT_ASSESSABLE`
- Every row states scope, evidence locator, limits and author confirmation. A popular value or a
  successful prior paper is not sufficient evidence outside that recorded scope.
- Keep failed, null and unstable configurations. Do not retain only the setting that produced a
  favourable result.

## Parameter/configuration experience

| Experience ID | Domain/modality | Platform/tissue/data state | Scientific object and unit | Parameter/config/method | Values/range/units | Selection timing and data | Comparator/alternative | Observed stability/failure | Evidence locator/run IDs | Evidence class | Applicability | Non-applicability | Confirmed by/date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LPM-001 | [scope] | [context] | [object/unit] | [item] | [values] | [timing] | [alternative] | [result or failure] | [path/ID] | [class] | [where it transfers] | [where it does not] | [owner/date] |

## Method-comparison experience

| Experience ID | Question/estimand | Methods compared | Matched conditions | Primary metric/readout | Independent unit/N | Sensitivity/negative result | Decision taken | Cost/trade-off | Closure evidence | Claim consequence | Evidence class | Confirmed by/date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LMM-001 | [question] | [methods] | [conditions] | [metric] | [unit/N] | [result] | [decision] | [cost] | [locator] | [claim] | [class] | [owner/date] |

## Reuse rule

Before reusing an experience row, compare platform, specimen/tissue, acquisition/assay, data state,
preprocessing, endpoint, unit, cohort composition and intended claim. If a material field differs,
the row is a hypothesis/rationale source only and the new study needs its own evaluation.
