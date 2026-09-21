# Open-science and reproducibility gate for imaging research

Use this gate at D4 (lock), D5 (execute) and D9 (closeout). It converts broad promises such as
"reproducible" or "FAIR" into inspectable artifacts. It does not require unrestricted release of
protected data, and it never treats a complete-looking bundle as proof that an independent team can
reproduce the result.

## Evidence states

Assign one state per artifact:

| State | Meaning |
|---|---|
| `PLANNED` | named in the protocol but not yet produced |
| `PRESENT_UNVERIFIED` | a file/link exists but identity, completeness or replay is unverified |
| `IDENTITY_VERIFIED` | locator, version and digest match the registered artifact |
| `REPLAYED` | an authorized rerun reproduced the declared intermediate/final output within its criterion |
| `RESTRICTED_WITH_ROUTE` | unavailable publicly but controller, access conditions and request route are explicit |
| `MISSING` | required artifact absent; claim and gate consequence stated |

`REPLAYED` applies only to the tested path and environment. It is not universal reproducibility,
clinical validity, external validation or a correctness certificate.

Assign a separate cumulative computational result-level axis through `radiology-reproducibility`:

`TRACEABLE -> RERUNNABLE -> REPLAYED -> INDEPENDENTLY_REPRODUCED`.

Artifact presence and identity support the first two levels; they do not prove execution. `REPLAYED`
requires a frozen package, authorized execution on the identified inputs and a prespecified tolerance.
`INDEPENDENTLY_REPRODUCED` additionally requires a different operator/team without hidden author
state. Record `EXTERNALLY_REPLICATED_OR_TRANSPORTED` only on a separate scientific-validation axis:
it uses new governed data/site/population/protocol/time, need not be preceded by same-data independent
replay, and must return to the appropriate scientific design/translation owner. Never average levels
across results or interpret either axis as statistical correctness, causal validity or patient benefit.

## D4 — analysis-before-results lock

Freeze before outcome-aware modelling or protected-test access:

- protocol, task contract, SAP/preregistration status and amendment/deviation policy;
- cohort/series/reference-standard definitions and `radiology-acquisition-qc` measurement passport;
- patient-level split generation, immutable manifests, overlap/duplicate audit and test-access policy;
- input/output schemas, primary command/config, software/environment target and randomness policy;
- primary estimand/metric/CI, sample-size rationale, missingness, multiplicity and sensitivity plan;
- code/data/model/weights licensing, privacy/DUA constraints and planned public or controlled route;
- negative/failure-result preservation and reporting-guideline stack.

An editable undated document, unpinned package list or verbal promise does not pass D4.

## D5 — execution receipt

For every claim-bearing run preserve:

`run ID -> code commit/archive digest -> environment lock -> command/entry point -> config digest ->
seed/randomness -> input manifest/digests -> output manifest/digests -> software/hardware -> start/end ->
operator -> test-access events -> deviations/failures -> upstream/downstream Claim IDs`.

Also preserve:

- cohort, series, annotation and exclusion flow counts that reconcile across artifacts;
- learned preprocessing/tuning fit scope and protected-test boundary;
- logs sufficient to distinguish a failed run from one that never ran;
- raw/frozen primary results before adaptation, repair or selective rerun;
- negative controls, sensitivity results and materially adverse failure cases; and
- PHI/controlled-data exclusions without copying sensitive content into the release receipt.

Do not cherry-pick a successful seed or silently replace a failed environment. A notebook's visible
output is not a run receipt unless its inputs, state and execution identity are bound.

## D9 — closeout and reuse packet

Inventory, with states and exact locators:

1. protocol/SAP/registration, amendments, deviations and test-access ledger;
2. cohort, series, measurement, ground-truth, split and analysis manifests;
3. source code, commit/archive, environment/container/lock file, configs, commands and seeds;
4. raw-to-derived schemas, transformation graph, model/checkpoint and result/display crosswalk;
5. statistical outputs, source data behind figures/tables and claim/value register;
6. data/model cards, licenses, repository/accession or controlled-access request route;
7. failed/negative runs, known non-replayable steps, manual decisions and unresolved dependencies;
8. minimal replay command, expected checks/digests/tolerances and actual independent-replay state;
9. preservation owner, retention/version policy, security/privacy boundaries and reuse exclusions.

For restricted human imaging, reproducibility may use metadata, schemas, synthetic structural
fixtures, controlled-compute access or an executable request procedure. Do not weaken privacy or DUA
constraints merely to obtain a public-access badge.

## Gate verdict

- `PASS`: every claim-critical artifact is identity-verified; required replay is complete or the
  protocol explicitly limits the claim to non-replayed transparency; access routes and deviations are
  truthful.
- `CONDITIONAL`: a named noncritical artifact is restricted/unverified, with owner, repair and surviving
  claim stated.
- `STOP`: the result cannot be traced to frozen inputs/code/config; the protected test was used for
  selection; a required artifact is missing without a claim downgrade; or release would violate
  governance.

## Primary and authoritative sources

- Wilkinson MD, et al. [FAIR Guiding Principles](https://doi.org/10.1038/sdata.2016.18).
- Nosek BA, et al. [Transparency and Openness Promotion guidelines](https://doi.org/10.1126/science.aab2374).
- Collins GS, et al. [TRIPOD+AI](https://doi.org/10.1136/bmj-2023-078378).
- Tejani AS, et al. [CLAIM 2024 Update](https://doi.org/10.1148/ryai.240300).
- National Academies. [Reproducibility and Replicability in Science](https://doi.org/10.17226/25303).
- Chue Hong NP, et al. [FAIR Principles for Research Software](https://doi.org/10.15497/RDA00068).
- W3C. [PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/).

FAIR describes stewardship properties, while TOP and reporting guidelines address transparency and
reporting. None alone proves computational replay, scientific validity or compliance with data-use
authority; this gate therefore requires artifact-level evidence and preserves restricted-access paths.
