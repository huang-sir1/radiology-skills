# Replay Contract, Tolerances and Evidence Levels

Use for `trace-audit`, `replay` and `discrepancy-diagnosis`.

## 1. Freeze one replay target

A replay target is not “the paper” or “the model.” Name one result and its complete derivation:

- table/figure/panel, metric and cohort/split;
- image/map/segmentation/feature artifact;
- trained checkpoint or inference output;
- expected schema, cardinality, values/hashes and tolerance;
- code/config/input/environment package version.

Each target receives its own status. One replayed table does not upgrade untested figures.

## 2. Identity contract

| Object | Minimum identity |
|---|---|
| source code | repository, immutable commit/release, dirty state, patch if dirty, entrypoint |
| configuration | full resolved config and command-line overrides; no hidden defaults |
| environment | OS/runtime, dependency lock, system libraries, hardware/drivers and locale/timezone |
| container | registry, tag for readability and immutable manifest/image digest for identity |
| data | dataset/release, access class, physical or repository checksum, unit hierarchy and inclusion manifest |
| images | examination/series/object identity, modality/sequence/phase/view/tracer/reconstruction without public PHI |
| labels/ROI | annotation protocol, reader/adjudication version, geometry and file hash |
| model | architecture/config, training split/data version, checkpoint/weight hash and inference mode |
| output | target path/schema, content hash where deterministic, metric values and run ID |

A checksum supports content identity, not correctness, ethics approval, clinical validity or
acquisition quality.

## 3. Environment and execution receipt

Capture:

- clean working directory and exact invocation;
- resolved config after defaults/overrides;
- package manager lock and runtime version;
- OS, architecture, CPU/GPU, RAM, drivers, CUDA/cuDNN or equivalent;
- deterministic flags, seeds, thread/process counts and known nondeterministic operations;
- external service/API/model version and cached artifact identity;
- start/end timestamps, operator/team, run ID, exit code, stdout/stderr and resource failures;
- output list, sizes, hashes/schema, counts and numerical comparisons.

Containerisation packages userspace but may still depend on host kernel, hardware, driver,
accelerator libraries, external services and mounted data. A container tag can move; record the
digest.

## 4. Tolerance contract

Freeze tolerance before replay. Choose a rule that fits the object:

- exact checksum for deterministic byte-identical output;
- schema, keys, row/subject counts plus elementwise absolute/relative tolerance;
- metric confidence/Monte Carlo tolerance;
- distributional or repeated-run envelope for stochastic training;
- image geometry/affine, voxel count and numerical tolerance for imaging derivatives.

Record reference value, comparator, unit, absolute/relative formula, aggregation and failure rule.
Do not choose tolerance after seeing the discrepancy. If no defensible tolerance exists, report
`STOP_TOLERANCE_NOT_FROZEN` and preserve exploratory differences without a pass verdict.

Seed equality is not deterministic equivalence. GPU kernels, library changes, parallel reductions,
data-loader order and hardware can change results. For stochastic outputs, predefine repeated runs
and the distributional decision rule.

## 5. Clean replay protocol

Run only with authorisation and lawful inputs:

1. create a fresh bounded workspace;
2. instantiate the documented environment from frozen artifacts;
3. verify input/config/code/weight identities before execution;
4. invoke only the documented entrypoint without copying unlisted caches or outputs;
5. preserve all failed attempts and environmental changes;
6. compare outputs with the frozen contract;
7. sign the receipt with operator, time, package and output identities.

For independent reproduction, a different operator/team must be able to follow the package without
private coaching or hidden author state. Clarifications become versioned documentation and require a
new independent run.

## 6. Discrepancy diagnosis

Do not patch first. Classify and test:

| Class | Typical evidence | Next test |
|---|---|---|
| IDENTITY | wrong data release, commit, config, weights or series | recompute/verify identifiers and inclusion manifest |
| ENVIRONMENT / DEPENDENCY | runtime, package, locale, driver or system library mismatch | compare resolved environment and minimal diagnostic |
| NONDETERMINISM | seed/order/kernel/thread differences | controlled repeats and deterministic settings |
| NUMERICAL | precision, device, solver/tolerance differences | localise first divergence and compare within frozen tolerance |
| DATA_ACCESS | missing/filtered restricted records or changed snapshot | verify access receipt, counts and release |
| EXTERNAL_SERVICE | mutable API/model/vendor response | pin version/cache lawful response and record service state |
| HARDWARE | device-specific algorithm or memory path | reproduce on declared hardware or narrow portability claim |
| ALGORITHMIC | code implements a different method or contains a defect | evidence-preserving issue and versioned repair |

Separate observed difference, hypothesised cause and recommended repair. A plausible explanation is
not a verified cause.

## 7. Two-axis evidence decision

| Level | Required receipt | What it does not establish |
|---|---|---|
| TRACEABLE | identity-linked provenance for the target | executability |
| RERUNNABLE | complete identity-checked package and lawful input route | successful execution |
| REPLAYED | executed frozen package, same input, prespecified output/tolerance pass | operator independence or new-data validity |
| INDEPENDENTLY_REPRODUCED | different operator/team, no hidden state, same-input replay pass | external population/site validity |

Record external replication/transport separately:

| Scientific-validation state | Required receipt | Computational implication |
|---|---|---|
| `NOT_ASSESSED` | no governed new-data/site/protocol/time claim was reviewed | none |
| `EXTERNALLY_REPLICATED_OR_TRANSPORTED` | prespecified external protocol, new governed contrast, analysis/validation receipt and scientific-owner verdict | none automatically; record the actual computational level independently |

The external state is a handoff to scientific design/method/translation owners. It is not the fifth
computational level and does not require same-data independent replay first. This skill may preserve
the external receipt and its computational provenance but cannot certify the external claim alone.
