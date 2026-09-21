# Site readiness and imaging-specific operations

Use this reference for multicentre or multi-workstream imaging research. A site is ready only for the
scope supported by inspected evidence; one active service line does not clear all modalities,
populations, protocols or data flows.

## 1. Readiness domains

| Domain | Minimum evidence | Frequent STOP condition |
|---|---|---|
| governance | current site-specific approvals/coverage, contracts/DUA, registration and owner | absent/expired/out-of-scope authority |
| people | named trained roles, delegation where applicable, coverage and escalation | unqualified critical role or no backup |
| population | feasible source population, eligibility workflow and recruitment/retention plan | denominator unknown or target cannot answer study |
| acquisition | modality/protocol, scanner/software/reconstruction, dose/contrast/tracer, QC and deviation route | site cannot reproduce accepted measurement |
| transfer/privacy | DICOM export, de-identification, pixel-PHI screen, encryption, receipt and reconciliation | uncontrolled PHI or missing exam identity |
| reference/annotation | source, timing, blinding, readers, ontology, tools, adjudication and throughput | label process incompatible with target construct |
| data | common dictionary/schema, IDs, time zero, missing codes, edit checks and query route | site data cannot reconcile to participant/exam |
| compute/analysis | secure environment, access, storage, software/license, test protection and fallback | protected test exposed or compute cannot meet lock |
| safety/incident | downtime, adverse/unanticipated event, privacy/security and clinical fallback routes | no detectable fallback for a critical failure |

Return `READY`, `CONDITIONAL`, `NOT_READY` or `NOT_ASSESSABLE` per domain, each with source,
version, checked date, residual risk and release criterion. No composite green status can hide a
domain-level `NOT_READY`.

## 2. Site initiation and change control

Before first transfer/enrolment/acquisition, freeze the site profile and run a dry path with
authorized non-sensitive or minimal data where appropriate:

`eligibility -> order/scheduling -> acquisition -> series selection -> de-identification -> transfer
-> receipt reconciliation -> annotation/reference -> data query -> analysis-ready acceptance`.

Record scanner service, hardware/software/reconstruction upgrades, protocol changes, PACS/RIS/EHR
interfaces, transfer-agent updates and personnel turnover. Material changes trigger targeted
requalification; “same scanner model” does not prove protocol equivalence.

## 3. Recruitment, acquisition and annotation control

- Recruitment/retention monitoring uses protocol- or sponsor-approved goals and decision thresholds;
  no universal percentage is encoded here.
- Reconcile screened, eligible, consented/waived, enrolled, imaged, accepted, reference-complete,
  annotated and analysis-included counts.
- Separate planned examinations from acquired examinations and accepted series. Repeat, incomplete,
  corrupt and protocol-deviant examinations stay visible.
- Track annotation backlog by case/lesion and adjudication state, not only number of masks. Monitor
  reader drift, software/version, label amendments and rework.
- Track pathology/omics specimen availability and image-sample-time mapping for mechanism studies.

## 4. Operational drift and contingency

Monitor scanner/protocol mix, rejection/rework, missing fields, transfer latency, annotation
agreement, site query burden, assay failure, storage, compute queue and model/test access. Each alert
defines threshold provenance, owner, investigation, recovery, scientific consequence and re-freeze
need.

Fallbacks must preserve the intended inference or explicitly downgrade scope. Replacing a site,
sequence, reader, reference standard or assay can change the study rather than merely the schedule;
return such changes to the scientific owner.

