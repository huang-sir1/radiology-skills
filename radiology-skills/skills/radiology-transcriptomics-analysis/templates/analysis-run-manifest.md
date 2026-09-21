# Analysis run manifest

- Run ID: [AUTHOR_INPUT_NEEDED]
- Plan/analysis-lock ID and version: [AUTHOR_INPUT_NEEDED]
- Modality/question/contrast: [AUTHOR_INPUT_NEEDED]
- State: [CODE_READY/RUNNING/RUN_COMPLETE/RUN_FAILED/REPRODUCED]
- Execution authority/source: [AUTHOR_INPUT_NEEDED]

## Runtime

- Command: `[exact command]`
- Working directory: `[absolute path]`
- Output root: `[absolute path]`
- Environment/lock path: `[path]`
- Critical versions/hardware: [details]
- Code/config identity: [commit/checksum/path]
- Seeds and determinism class: [details]
- Start/end/exit status: [details]
- stdout/stderr/log: [paths]

## Inputs

| Input ID | Path | Schema/dimensions | Checksum/integrity | Identity-map version |
|---|---|---|---|---|
| [ID] | [path] | [details] | [details] | [version] |

For a raw-read run, also bind FASTQ/sample-sheet/library-index manifests, chemistry/read structure,
reference bundle/index/annotation checksums, cell/spot calling or image-decoding configuration and
raw-to-matrix QC outputs. For a matrix/object entry, record the upstream evidence state and do not
claim those steps were rerun.

## Outputs

| Artifact ID | Expected path | Exists/readable | Schema/dimensions | Checksum | Verification state |
|---|---|---|---|---|---|
| [ID] | [path] | [yes/no] | [details] | [value] | [state] |

## Deviations and failures

| Time | Original decision | Event/error | Action and authority | Affected artifacts/claims | Resolution state |
|---|---|---|---|---|---|
| [time] | [decision] | [event] | [action] | [scope] | [open/closed] |

## Completion assertion

`RUN_COMPLETE` is allowed only if the process exited successfully and every required artifact is
readable, structurally checked and attributable to this run. Verdict: [state + rationale]
