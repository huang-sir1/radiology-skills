# Imaging interoperability and site acceptance

Use this reference for local PACS/RIS/EHR/worklist integration and end-to-end site acceptance of an
imaging/AI intervention. `radiology-acquisition-qc` owns input image/measurement validity;
`radiology-data` owns provenance/de-identification/data flows; this reference owns clinical-system
exchange, display, orchestration, fallback and acceptance evidence.

## 1. Integration passport

Freeze `site/environment | intervention release | source modalities/systems | DICOM/IHE profiles and
their status/version | SOP Classes/roles/transfer syntaxes | input/output objects | identity keys |
trigger/worklist | destinations/display | latency/capacity | failure/fallback | audit/security |
test cases/expected result | owner/approval/date`.

DICOM explicitly states that DICOM itself does not guarantee interoperability; conformance statements
support a first comparison and must be followed by validation with the actual equipment. IHE profiles
also carry lifecycle states. At the 2026-08-23 check, the IHE Radiology page lists Revision 23.0 as
normative framework and AIR/AIRA/AIW-I under trial implementation; re-verify profile status before a
real acceptance claim.

## 2. End-to-end acceptance cases

Test normal, boundary and failure paths using site-approved fixtures/cases:

1. correct patient, accession, study, series, frame, laterality, body part and prior association;
2. intended input selection across modality/vendor/protocol, missing/corrupt/duplicate/late series;
3. trigger, routing, queue/worklist state, retries, idempotency and concurrency/capacity;
4. output object/schema and semantics: image/secondary capture, DICOM SEG/SR, measurement, result,
   alert or report integration; units, codes, uncertainty/abstention and version visible;
5. PACS/viewer/report/worklist display on representative clients, layouts and user roles;
6. latency clocks from acquisition/availability through processing, delivery, opening and action;
7. failure/timeout/downtime/maintenance/recovery: no silent success, stale output or wrong fallback;
8. audit log, access control, encryption/security review, PHI boundary and incident trace;
9. rollback/previous version, mixed-version prevention and post-update regression suite.

A synthetic test proves only the tested path. Confirm with authorized representative workflows and
document residual vendor/site/version limitations.

## 3. Acceptance receipt

For every test record:

`case ID | environment/release | precondition/input IDs | trigger | expected objects/semantics/display |
observed output/timestamps/logs | result PASS/CONDITIONAL/FAIL | evidence locator/digest | deviation |
owner/action/retest | residual claim`.

Site acceptance is `STOP` for wrong/ambiguous identity, unvalidated output semantics, inaccessible
failure state, unsafe fallback, unbounded latency/capacity, missing auditability, unresolved
privacy/security or a material release mismatch. A paper model card, DICOM statement or vendor demo
cannot close these failures.

## Official sources

- DICOM. [PS3.2 Conformance](https://dicom.nema.org/medical/dicom/current/output/chtml/part02/chapter_1.html)
  and [interoperability remarks](https://dicom.nema.org/medical/dicom/current/output/chtml/part02/sect_n.3.3.html)
  (current page checked 2026-08-23).
- IHE. [Radiology Technical Framework and profiles](https://profiles.ihe.net/RAD/) (profile status
  snapshot checked 2026-08-23).
- DICOM. [Current standard](https://www.dicomstandard.org/current/).

Local clinical engineering, IT, cybersecurity, privacy and safety owners authorize acceptance and
go-live. This skill produces evidence and unresolved actions, not that authorization.
