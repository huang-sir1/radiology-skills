# Local transcriptomics analysis experience registry

Record one inspectable local case per row. This registry supports failure diagnosis and learner
guidance; it does not turn one laboratory's choice into a universal default.

| Case ID | Modality/platform/chemistry | Tissue/system and donor structure | Entry data state | Question/workflow step | Failure or uncertainty observed | Diagnosis evidence | Repair/change and authority | Closure evidence/result | Code/environment/reference locator | Applicability boundary | Counterexample/residual risk | Owner and reconfirmed on |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LOCAL-TX-001 | [details] | [details] | [FASTQ/matrix/object] | [step] | [observation] | [log/QC/artifact] | [change + approver] | [verified evidence] | [path/version/checksum] | [platform/tissue/data-state limits] | [where it may fail] | [owner/date] |

## Use rule

- Cite the Case ID and evidence locator whenever a recommendation relies on local experience.
- Keep failed, null and superseded cases; mark their state rather than deleting them.
- A recurring pattern may justify a diagnostic priority, not a fixed QC threshold or claim.
- Reconfirm after meaningful changes in chemistry, reference, software, tissue handling or compute
  environment. If no matching case exists, return `NO_LOCAL_EXPERIENCE_MATCH`.
