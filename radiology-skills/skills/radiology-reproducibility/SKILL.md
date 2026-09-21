---
name: radiology-reproducibility
description: "Audit/package computational replay with manifests, environments, provenance and evidence levels."
---

# Radiology Computational Reproducibility

Use this skill to make a radiology analysis traceable, rerunnable, replayed or independently
reproduced through inspectable computational receipts, and to preserve—but not adjudicate—linked
external replication/transport evidence. Its unique
responsibility is the executable chain from frozen inputs through code/configuration/environment to
outputs. It does not own scientific design, statistical validity, data-sharing authority, software
security certification or external clinical validation.

## Non-negotiable boundaries

- Apply the cumulative **computational axis** exactly:
  `TRACEABLE -> RERUNNABLE -> REPLAYED -> INDEPENDENTLY_REPRODUCED`. Assign only the highest level
  actually evidenced per target result. Record `EXTERNALLY_REPLICATED_OR_TRANSPORTED` only on a
  separate scientific-validation axis owned by `radiology-design` / `radiology-translation`; it is
  neither the next computational level nor conditional on same-data independent replay.
- File existence, a repository URL or a container tag does not prove replay. A successful replay on
  the same inputs does not establish independent replication, transportability or clinical validity.
- Freeze code commit and dirty state, configuration, environment/container digest, input/output
  manifests, run ID, seeds, model weights, data version and expected tolerance before claim-bearing
  replay.
- Record exact evidence states: `ASSERTED`, `PRESENT_UNVERIFIED`, `IDENTITY_VERIFIED`,
  `EXECUTED`, `TOLERANCE_PASSED`, `INDEPENDENTLY_VERIFIED` and
  `EXTERNAL_DATA_VERIFIED`. Do not upgrade a link or author statement into execution evidence.
- Restricted data need not be public. Access controls, consent, DUA, licences and repository
  conditions override convenience; a synthetic fixture tests mechanics but does not reproduce a
  result obtained from unavailable real data.
- Never silently patch code, substitute data, relax tolerance or reuse hidden local state during a
  replay. A repair creates a new package version and a new receipt.
- Replay execution requires user authorisation, a safe workspace and available lawful inputs. An
  audit or package plan does not imply permission to run code, download restricted data or publish.

## Route by mode

| Need | Mode | Read |
|---|---|---|
| inventory code/data/environment/provenance and assign the current level | `trace-audit` | [replay-contract-and-levels.md](references/replay-contract-and-levels.md) |
| design a minimum replay package or repair missing artifacts | `package-plan` | both method references |
| perform or specify a frozen replay and issue a run receipt | `replay` | [replay-contract-and-levels.md](references/replay-contract-and-levels.md) |
| diagnose divergence without hiding failed runs | `discrepancy-diagnosis` | [replay-contract-and-levels.md](references/replay-contract-and-levels.md) |
| freeze licences, restricted-data access and a citable archive handoff | `archive-handoff` | [restricted-data-archiving-and-software.md](references/restricted-data-archiving-and-software.md) and [source-registry.md](references/source-registry.md) |

Use [reproducibility-passport.md](templates/reproducibility-passport.md) for the evidence-level
decision and
[minimum-replay-package-manifest.md](templates/minimum-replay-package-manifest.md) for a persistent
package. Do not load every reference for a narrow audit.

## Input passport

Record:

1. research object, target result/claim, package version, intended computational level and any
   separately supplied external-validation receipt;
2. executable entrypoint, source repository, immutable commit, dirty state and code licence;
3. complete configuration, command, working-directory assumptions and external services;
4. runtime, OS, hardware/CPU/GPU, drivers, CUDA, libraries/lockfiles and container tag plus digest;
5. input manifest with content identity/hash, format, hierarchy, data release/version, access class,
   preprocessing eligibility and no exposed identifiers;
6. seed(s), determinism settings, stochastic repeats, trained weights/checkpoint hash and training
   data/version relationship;
7. expected outputs, metrics, reference values, tolerance rule and whether tolerance was frozen
   before execution;
8. operator/team, timestamp, run ID, logs, exit state, output hashes and independent-environment
   details;
9. archive identifier, licences and restricted-data replay route.

Use `AUTHOR_INPUT_NEEDED`; never infer an input identity, model weight, DICOM series,
preprocessing version, environment or successful run from naming convention.

## Two-axis evidence verdict

- `TRACEABLE`: the claimed output can be linked to identifiable inputs, code/configuration and
  provenance, but executability has not been established.
- `RERUNNABLE`: an executable package, dependencies, instructions and lawful input route are
  present and identity-checked; no qualifying replay receipt yet exists.
- `REPLAYED`: the frozen package was executed on the same identified inputs and produced the
  prespecified outputs within the frozen tolerance. Operator independence is not required.
- `INDEPENDENTLY_REPRODUCED`: a different operator/team, without hidden author state, rebuilt or
  instantiated the documented environment and replayed the same input/code/method within tolerance.
The four-level computational axis is cumulative only while lower-level evidence remains valid.
Report a mixed state if one result is replayed and another is merely traceable; never average levels
across artifacts.

On the separate scientific axis, `EXTERNALLY_REPLICATED_OR_TRANSPORTED` means a governed analysis on
new data, site, population, protocol or time supports a prespecified external claim. It can coexist
with any computational level and requires the appropriate design/translation owner. A new-site result
without a reproducible package may carry external evidence while remaining only `TRACEABLE`
computationally; conversely, independent same-data replay is not external validation.

## Required workflow

1. **Freeze the target.** Name the exact table, figure, model metric, image/segmentation derivative or
   decision artifact and its expected values/tolerance before replay.
2. **Construct the provenance graph.** Link input entity -> preprocessing/activity -> intermediate ->
   analysis/model -> output, with responsible agent, version, time and identifiers.
3. **Verify identities.** Hash physical files where lawful, record dataset/release and code commit,
   verify config/weights, and distinguish tag/name from immutable digest.
4. **Audit the environment.** Capture OS/runtime, lockfile, system libraries, drivers/hardware,
   locale/timezone and external service versions. A container reduces—but does not erase—hardware,
   data, service and nondeterminism dependencies.
5. **Run only when authorised.** Use a fresh controlled workspace; invoke the documented entrypoint;
   preserve stdout/stderr, command, resource state, start/end, exit code and every produced output.
   Failed and negative runs remain visible.
6. **Compare against frozen tolerance.** Check expected files, schemas, row/subject counts, numeric
   tolerance/distribution and hashes as appropriate. Seeds alone do not guarantee deterministic GPU
   or parallel execution.
7. **Diagnose discrepancies by class.** Use `IDENTITY`, `ENVIRONMENT`, `DEPENDENCY`,
   `NONDETERMINISM`, `NUMERICAL`, `DATA_ACCESS`, `EXTERNAL_SERVICE`, `HARDWARE` or
   `ALGORITHMIC`. Do not repair in place.
8. **Issue the receipt and level.** Separate observed artifact/run evidence, inference about cause
   and recommended repair. Archive the frozen package only after licence/privacy review.

## STOP gates

- `STOP_INPUT_IDENTITY`: input release/object identity or hierarchy is unresolved.
- `STOP_CODE_CONFIG_IDENTITY`: executable entrypoint, immutable code state, full config or model
  weights are missing/ambiguous.
- `STOP_ENVIRONMENT_UNRESOLVED`: required runtime/dependency/hardware state cannot be recreated or
  assessed.
- `STOP_TOLERANCE_NOT_FROZEN`: acceptance tolerance was absent or changed after observing replay
  output.
- `STOP_DATA_AUTHORIZATION`: restricted input, model derivative, credential, consent, DUA or
  transfer authority is unresolved.
- `STOP_LICENSE_OR_ARCHIVE`: licence conflict, embedded secret/identifier or non-versioned archive
  prevents lawful reusable release.
- `STOP_REPLAY_NOT_AUTHORIZED`: execution or required data access is outside current permission.

A STOP limits the replay/level claim. Return a trace inventory and smallest lawful repair where
possible.

## Radiology-specific provenance

- Preserve patient -> examination/time point -> series/acquisition -> reconstruction -> derived
  image/map -> ROI/segmentation -> feature/model/output hierarchy without embedding direct
  identifiers in a public manifest.
- Freeze modality, phase/sequence/tracer/view, reconstruction, resampling, registration,
  normalisation, harmonisation, segmentation/annotation, radiomics definition and software version.
- For deep learning preserve split/cohort version, preprocessing, architecture/config, weights,
  training checkpoint, random state, inference mode and hardware/runtime.
- A DICOM/NIfTI filename or series description does not verify the pixel object. A checksum verifies
  identity, not acquisition quality, correct series selection or authorisation.
- Harmonising or recalibrating on external data is adaptation. It cannot retain an untouched
  external-transport claim.

## Output contract

1. `Route and target` — mode, object, package version, supplied artifacts and authority.
2. `Provenance and identity map` — code/config/environment/input/activity/output chain.
3. `Replay readiness matrix` — present, verified, missing and STOP states.
4. `Run receipt` — command, operator, environment, timing, exit, logs and outputs when executed.
5. `Tolerance and discrepancy report` — frozen rule, observed difference, class and evidence.
6. `Two-axis verdict` — highest supported computational level per result, separate supplied
   external-validation state/owner and prohibited cross-axis upgrade.
7. `Restricted-data/licence/archive plan` — access route, reusable components and persistent ID.
8. `Handoff` — evidence vs causal inference vs recommendation and unique receiving owner.

## Handoffs and non-ownership

- Data identity, de-identification, DMS/repository and access -> `radiology-data`; consent/DUA and
  participant governance -> `radiology-ethics`.
- Acquisition/reconstruction/series validity -> `radiology-acquisition-qc`; segmentation ->
  `radiology-annotation`; radiomics implementation -> `radiology-radiomics`; model training ->
  `radiology-deep-learning`.
- Statistical methods, tolerance justification and scientific inference -> `radiology-stats`;
  method-performance comparison -> `radiology-method-evaluation`.
- New-site/population clinical validation -> `radiology-design` / `radiology-translation`;
  project-level state and cross-skill receipts -> `radiology-pipeline`.
- This skill does not certify cybersecurity, regulatory software compliance, data-sharing
  permission, statistical correctness or external clinical validity.
