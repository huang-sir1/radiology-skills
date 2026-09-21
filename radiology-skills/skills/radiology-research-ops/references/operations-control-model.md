# Operations control model

Use this reference to build a project control book without taking over scientific or institutional
decision rights.

## 1. Work-package contract

Each work package records:

`WP ID | objective | locked scientific input | deliverable | acceptance evidence | responsible role |
accountable role | consulted/informed roles | predecessor/dependency | duration range | resource and
access requirement | critical-to-quality factor | decision milestone | fallback | status | artifacts`.

- Use roles before names; bind a name only from a verified team record.
- One work package has one accountable role. Multiple responsible roles are allowed when interfaces
  are explicit.
- RACI describes responsibility; it does not create delegation, employment, authorship, approval or
  signature authority.
- A deliverable is complete only when its acceptance evidence exists.

## 2. Critical path and dependency map

Map regulatory/access lead time, site startup, acquisition, annotation, assay, data cleaning,
analysis, validation and review dependencies. For each estimate record basis, optimistic/most likely/
adverse duration, capacity, external queue and uncertainty.

Do not report a deterministic completion date when access, recruitment, scanner time, pathology,
assay, compute or external validation remains uncertain. Identify:

- critical path and near-critical paths;
- hard predecessors and optional sequencing;
- resource contention and single points of failure;
- decision dates after which a downstream milestone becomes infeasible; and
- scientific consequences of compression, substitution or reduced scope.

Schedule slack cannot compensate for inadequate events, invalid labels or an unapproved activity.

## 3. Operational status and forecasting

Use evidence-backed states: `PLANNED`, `EVIDENCED_READY`, `ACTIVE`, `AT_RISK`, `BLOCKED`,
`FROZEN`, `PAUSED`, `TERMINATED`, `CLOSED`.

For each throughput stream report:

`period | eligible denominator | planned | actual | accepted | rejected/rework | cumulative | rate |
capacity | variance explanation | forecast range | threshold source | next decision`.

Track participants, examinations, series, lesions, readers, specimens, slides and runs separately.
Do not convert images, lesions, patches or technical replicates into participants.

## 4. Resource and budget-capacity map

Record quantity, unit, required window, verified availability, owner, lead time, backup and affected
work packages for:

- clinical/research staff and protected effort;
- scanner/sequence/reconstruction and phantom time;
- contrast, tracer, tissue, reagents, pathology and molecular assays;
- annotation/readers/adjudication;
- storage, secure transfer, GPU/CPU/RAM and licensed software;
- statistics, data management, monitoring and publication/repository costs.

Costs are estimates or author-provided facts until finance verifies them. This skill checks alignment
and capacity; it does not approve procurement, payroll, contracts or expenditure.

## 5. Decision meeting receipt

Record `decision ID | date | decision question | evidence packet/version | options | criteria |
participants/roles | COI or recusal | decision | rationale | dissent | actions/owners/dates |
artifacts invalidated | next review`.

Minutes are not proof that an action happened. Close an action only with its specified evidence.

