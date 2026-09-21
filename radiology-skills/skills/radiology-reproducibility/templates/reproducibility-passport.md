# Computational Reproducibility Passport

Assign a level per target result. Missing evidence remains `AUTHOR_INPUT_NEEDED`.

## Target and authority

| Field | Value |
|---|---|
| target result / claim / locator | [AUTHOR_INPUT_NEEDED] |
| package version | [AUTHOR_INPUT_NEEDED] |
| mode | trace-audit / package-plan / replay / discrepancy-diagnosis / archive-handoff |
| requested computational level | TRACEABLE / RERUNNABLE / REPLAYED / INDEPENDENTLY_REPRODUCED |
| separate scientific-validation state | NOT_ASSESSED / AUTHOR_REPORTED / EXTERNALLY_REPLICATED_OR_TRANSPORTED |
| scientific-validation owner / receipt | [AUTHOR_INPUT_NEEDED / NOT_APPLICABLE] |
| replay/data/archive authority | [AUTHOR_INPUT_NEEDED] |
| stop state | NONE / STOP_INPUT_IDENTITY / STOP_CODE_CONFIG_IDENTITY / STOP_ENVIRONMENT_UNRESOLVED / STOP_TOLERANCE_NOT_FROZEN / STOP_DATA_AUTHORIZATION / STOP_LICENSE_OR_ARCHIVE / STOP_REPLAY_NOT_AUTHORIZED |

## Identity and provenance

| Object | Identifier / version / hash | Evidence state | Locator | Missing / risk |
|---|---|---|---|---|
| code commit and dirty state | [AUTHOR_INPUT_NEEDED] | ASSERTED / PRESENT_UNVERIFIED / IDENTITY_VERIFIED | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |
| entrypoint and resolved configuration | [AUTHOR_INPUT_NEEDED] | ASSERTED / PRESENT_UNVERIFIED / IDENTITY_VERIFIED | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |
| environment / lockfile / container digest | [AUTHOR_INPUT_NEEDED] | ASSERTED / PRESENT_UNVERIFIED / IDENTITY_VERIFIED | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |
| data release / input manifest | [AUTHOR_INPUT_NEEDED] | ASSERTED / PRESENT_UNVERIFIED / IDENTITY_VERIFIED | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |
| seed / determinism / weights | [AUTHOR_INPUT_NEEDED] | ASSERTED / PRESENT_UNVERIFIED / IDENTITY_VERIFIED | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |
| expected output / reference | [AUTHOR_INPUT_NEEDED] | ASSERTED / PRESENT_UNVERIFIED / IDENTITY_VERIFIED | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |

Provenance chain: input -> preprocessing -> intermediate -> analysis/model -> output

Radiology hierarchy and version boundary: [AUTHOR_INPUT_NEEDED]

## Frozen tolerance

| Target field | Reference | Rule / formula | Unit | Frozen before run? | Failure rule |
|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | exact hash / absolute / relative / distributional / geometry | [AUTHOR_INPUT_NEEDED] | YES / NO / UNVERIFIED | [AUTHOR_INPUT_NEEDED] |

## Run receipt

| Field | Value |
|---|---|
| run ID / operator / team | [NOT_RUN / AUTHOR_INPUT_NEEDED] |
| independent from original team/state? | NOT_RUN / YES / NO / UNVERIFIED |
| start/end / command / workspace | [NOT_RUN / AUTHOR_INPUT_NEEDED] |
| OS/runtime/hardware/drivers | [NOT_RUN / AUTHOR_INPUT_NEEDED] |
| resolved dependencies / container digest | [NOT_RUN / AUTHOR_INPUT_NEEDED] |
| exit code and stdout/stderr locator | [NOT_RUN / AUTHOR_INPUT_NEEDED] |
| output manifest / hashes | [NOT_RUN / AUTHOR_INPUT_NEEDED] |
| comparison result | NOT_RUN / EXECUTED / TOLERANCE_PASSED / FAILED |

## Discrepancy ledger

| Observation | Evidence | Class | Hypothesised cause | Verification test | Repair version |
|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | IDENTITY / ENVIRONMENT / DEPENDENCY / NONDETERMINISM / NUMERICAL / DATA_ACCESS / EXTERNAL_SERVICE / HARDWARE / ALGORITHMIC | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | NOT_REPAIRED |

## Verdict

Highest supported computational level: [AUTHOR_INPUT_NEEDED]

Separate external replication/transport state and owner: [AUTHOR_INPUT_NEEDED]

Evidence receipt: [AUTHOR_INPUT_NEEDED]

Prohibited upgrade: [AUTHOR_INPUT_NEEDED]

Observed evidence: [AUTHOR_INPUT_NEEDED]

Causal inference about discrepancy: [AUTHOR_INPUT_NEEDED]

Recommended next action and unique owner: [AUTHOR_INPUT_NEEDED]
