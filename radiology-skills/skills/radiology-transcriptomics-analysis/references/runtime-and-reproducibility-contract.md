# Runtime and reproducibility contract

## Execution authority

Before running code, identify the exact command or approved entry point, working directory, input
roots, output root, environment, expected resource class and timeout/monitoring plan. A user request
to analyze supplied data authorizes normal in-scope implementation, but not upload to external
services, raw-data overwrite, access outside the stated roots, or silent expansion to unrelated
datasets.

Return `RUN_BLOCKED` when the output path could overwrite inputs, identity mapping is ambiguous,
credentials/controlled-data authority is unresolved, or the command has a materially destructive
side effect.

## Run manifest minimum

- stable Run ID, modality, question/contrast and analysis-lock version;
- code/config commit or checksum when available;
- exact command, working directory, environment lock and critical package/tool versions;
- input artifact paths/checksums/dimensions and donor-sample map version;
- output root, expected artifacts and success assertions;
- seeds and deterministic/stochastic/environment-sensitive classification;
- start/end timestamps, exit status, log/stdout/stderr paths and warning summary;
- deviations, retries and manual interventions—never hide a failed first attempt;
- produced artifact paths, schemas/dimensions/checksums and verification status.

## Build and dry checks

Code must fail clearly on missing columns/files, duplicate IDs, dimension mismatch, unestimable
contrasts and non-writable outputs. Prefer a small explicit dry check that reads metadata/schema and
writes only to a temporary or approved test output. A successful import or dry check is
`CODE_READY`, not `RUN_COMPLETE`.

Do not silently substitute packages, references, parameters or files. Record any approved change as
a deviation linked to the affected decision and outputs.

## Reproduction classes

| Class | Required comparison | Allowed verdict |
|---|---|---|
| deterministic | same input/code/environment/seed; exact table/schema and checksum where expected | `REPRODUCED` or `MISMATCH` |
| stochastic | same locked process; compare prespecified estimates/distributions across declared seeds/tolerance | `REPRODUCED_WITH_VARIATION`, `MISMATCH`, or `CANNOT_VERIFY` |
| environment-sensitive | preserve critical versions/hardware details; compare scientific outputs, not wall time | `REPRODUCED_WITH_ENVIRONMENT_CAVEAT`, `MISMATCH`, or `CANNOT_VERIFY` |

There is no universal numeric tolerance. Define it from the scientific object before comparing;
otherwise report differences descriptively. Never choose tolerance after seeing whether the rerun
matches.

## Artifact verification states

- `PLANNED`: named in the workflow but not created.
- `PRODUCED_UNCHECKED`: file exists but schema/content attribution is not checked.
- `VERIFIED_FROM_RUN`: output exists, is readable, matches expected structure and is linked to the
  recorded run.
- `AUTHOR_REPORTED`: asserted by the author without inspectable execution evidence.
- `PARTLY_VERIFIED`: some but not all required evidence is inspectable.
- `NOT_ASSESSABLE`: missing/incompatible evidence prevents a judgment.

Do not collapse these states into a generic “completed.”

## Protected evidence and test access

If the study has a protected validation/test set, record every access. It cannot select QC rules,
features, normalization, integration, references, thresholds, methods, seeds, figures or favourable
claims. Discovery decisions are frozen before protected access; post-access changes create a new
exploratory analysis version and cannot retain the original confirmatory label.

## Writing and review handoff

Methods receive the frozen workflow, versions, decisions and unit hierarchy. Results receive only
verified outputs and prespecified/explicitly exploratory labels. Figures/tables receive source-data
paths. Supplement receives full QC, exclusions, sensitivity, environment and deviations. Discussion
receives limitations, failure boundaries and alternative explanations. Abstract/title cannot exceed
the weakest link in sampling independence, evidence status and validation.

## Mentor and writing-handoff receipts

A mentor receipt distinguishes what is required to make the current analysis interpretable from
what would merely make it larger. For each route record `why -> minimum defensible repair -> stronger
route -> resource/time burden -> failure signal -> fallback -> closure evidence -> surviving claim`.
The learner chooses among explicit trade-offs; the skill does not hide uncertainty behind a package
name or fashionable optional analysis.

A writing-handoff receipt binds each text location to immutable evidence:

| Manuscript location | Required source | Prohibited shortcut |
|---|---|---|
| Methods | workflow/config, reference, unit hierarchy, decisions, versions | reconstructing settings from memory |
| Results | verified run artifacts and prespecified/exploratory state | reporting planned or unchecked outputs |
| Figures/tables | source-data locator and producing run | copying values from rendered plots |
| Supplement | QC/exclusion, raw-to-matrix provenance, sensitivity, environment, deviations | hiding failed runs or post hoc rules |
| Discussion | alternatives, residual confounding, failure boundary | converting association/estimate into mechanism |
| Abstract/title | weakest validated claim ceiling | stronger wording than the full evidence chain |
