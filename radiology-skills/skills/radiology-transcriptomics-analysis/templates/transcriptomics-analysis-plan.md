# Transcriptomics analysis plan

## Scope

- Plan ID/version/date: [AUTHOR_INPUT_NEEDED]
- Mode and primary modality: [plan/build/run-audit/reproduce/interpret-handoff/mentor/writing-handoff] / [bulk-rna/scrna/snrna/spatial]
- Question, contrast and Claim IDs: [AUTHOR_INPUT_NEEDED]
- Intended inference/use: [AUTHOR_INPUT_NEEDED]
- Donor/patient hierarchy and independent unit: [AUTHOR_INPUT_NEEDED]
- Protected-test state: [none/locked/accessed/unknown]
- Current execution state: [PLAN_ONLY/CODE_READY/RUNNING/RUN_COMPLETE/RUN_FAILED/AUDIT_ONLY/REPRODUCED]

## Inputs and identity

| Artifact | Path | Type/schema/dimensions | Producer/version | Integrity evidence | Status |
|---|---|---|---|---|---|
| [item] | [exact path] | [details] | [details] | [checksum/assertion] | [state] |

Donor -> specimen -> region/section -> library -> cell/spot map: [locator]

## Raw-read entry, when applicable

- Entry state: [FASTQ/BCL/matrix/object]
- FASTQ/sample-sheet/library-index manifest and checksums: [locator/state]
- Chemistry/read/barcode/UMI/feature structure: [details]
- Reference bundle/index/annotation and checksums: [locator]
- Raw-to-matrix branch and expected outputs: [bulk/sc-sn/spot-spatial/imaging-spatial/NOT_APPLICABLE]
- Upstream evidence when skipped: [AUTHOR_REPORTED/PARTLY_VERIFIED/VERIFIED + locator]

## Locked workflow

| Step | Input | Output | Decision and rationale | Alternatives | Assumption/unit | Freeze state | Failure/stop condition |
|---|---|---|---|---|---|---|---|
| T0 | [input] | [output] | [decision] | [alternatives] | [assumption] | [planned/frozen] | [condition] |

## Expected artifacts

| Artifact ID | Path | Schema/dimensions | Success assertion | Downstream consumer |
|---|---|---|---|---|
| [ID] | [path] | [expected] | [check] | [module/decision] |

## Execution plan

- Approved command/entry point: [AUTHOR_INPUT_NEEDED]
- Working directory/output root: [AUTHOR_INPUT_NEEDED]
- Environment/runtime profile: [locator]
- Seeds/determinism class: [details]
- Monitoring/timeout/resource plan: [details]
- Raw-input overwrite prevention: [check]

## Handoffs and next action

- Statistical inference packet: [locator/NOT_NEEDED]
- Method-evaluation packet: [locator/NOT_NEEDED]
- Mechanism interpretation packet: [locator/NOT_NEEDED]
- Writing/review packet: [locator/NOT_READY]
- Single next decision-bearing action: [action]

## Mentor or writing receipt, when requested

- Minimum defensible / standard publishable / ambitious route: [rationale, resources, failure,
  fallback, closure evidence, allowed claim]
- Methods / Results / figures-tables / Supplement / Discussion / Abstract-title placement map:
  [Claim or Result ID -> source locator -> allowed wording -> prohibited upgrade]
