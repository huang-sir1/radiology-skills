# Foundation-model data genealogy, contamination and privacy

Use this contract for pretrained, self-supervised, multimodal, vision-language, hosted or federated
models when any development or evaluation image, report, label or derivative may have appeared in
pretraining. Geographic externality and pretraining independence are different axes; report both.

## 1. Freeze the model and data genealogy

Record the exact model/checkpoint/version and retrieval date, provider, licence, declared training
cutoff, known corpora, excluded corpora, adaptation data and every evaluation cohort. At the finest
lawful resolution available, compare patient, encounter, exam, series, image, report, annotation,
patch and transformed/near-duplicate derivatives. A filename or dataset-title comparison alone is
not a patient-overlap audit.

Assign one evidence state to each evaluation cohort:

| State | Required meaning | Permitted wording |
|---|---|---|
| `VERIFIED_NO_OVERLAP` | versioned source manifests and an appropriate identifier/near-duplicate audit found no overlap at the declared units | no overlap was detected by the named audit |
| `PARTLY_ASSESSABLE` | some sources or units were checked, but the genealogy is incomplete | no overlap was detected in the assessable sources; residual contamination is unknown |
| `CONTAMINATION_NOT_ASSESSABLE` | closed, undisclosed or unavailable pretraining genealogy prevents a meaningful audit | external task-cohort evaluation; pretraining contamination could not be assessed |
| `KNOWN_OVERLAP` | the patient, exam, report, image or a materially equivalent derivative is known to be present | reused/pretraining-overlapped evaluation; no untouched-test claim |

`VERIFIED_NO_OVERLAP` is scoped to the model version, source manifests, matching units and methods.
It is not proof that no undisclosed copy exists. Under `PARTLY_ASSESSABLE` or
`CONTAMINATION_NOT_ASSESSABLE`, a cohort may still test a named site/population/protocol transport
contrast, but it must not be called completely unseen, untouched or independent of pretraining.

## 2. Contamination controls

1. Freeze the evaluation cohort and model version before inspection.
2. Reconcile public dataset aliases, releases, mirrors, report/image derivatives and temporal
   subsets; where authorised, use privacy-preserving patient/exam identifiers plus perceptual or
   embedding near-duplicate checks.
3. Log suspected matches, matching method/threshold, adjudication and exclusions. Do not tune the
   duplicate threshold on favorable model results.
4. If a contaminated cohort is used for development, reserve a separate real patient-level final
   evaluation set. A synthetic or re-rendered copy is not independent.
5. Report sensitivity analyses with suspected overlaps removed when feasible.

Return `STOP_UNTOUCHED_CLAIM` for `KNOWN_OVERLAP`, and
`CONTAMINATION_NOT_ASSESSABLE` rather than a clean-overlap claim when provenance is closed.

## 3. Privacy threat-model contract

De-identification/authorisation governs whether data may be processed; it does not establish that a
model cannot reveal training information. For each use, freeze the protected asset, adversary,
access, attack surface, success criterion, evaluation data and residual risk.

| Surface | Questions and controls | Claim boundary |
|---|---|---|
| memorisation/copying | can prompts, nearest-neighbour search or repeated sampling reproduce training images, reports or rare strings? | failure to elicit a copy with one prompt set is not proof of non-memorisation |
| membership inference/model inversion | black/grey/white-box access, realistic nonmember controls, repeated runs and uncertainty | report attack-specific results, not universal privacy |
| hosted model/RAG | provider retention, secondary training, region, logging, cache, deletion, subprocessors and output review | do not send PHI/controlled data without documented authority and approved terms |
| prompts/outputs/artifacts | scrub examples, traces, embeddings, vector stores, screenshots, logs and exported checkpoints | de-identified input does not guarantee safe output |
| federated/distributed training | gradients, updates, telemetry, secure aggregation, malicious-client/server assumptions | federated learning is not automatically private |
| differential privacy | implementation, clipping/noise, accounting unit, sampling, epsilon/delta and composition | a DP claim is only for the declared mechanism, adjacency unit and budget |

Use `PRIVACY_CLAIM_UNRESOLVED` when the adversary or access model is not declared. Escalate research
authorisation, controlled-data access, vendor terms and re-identification risk to
`radiology-ethics`; escalate security testing beyond the study team's competence to qualified
privacy/security review.

## 4. Required output

Return:

`model/version card -> pretraining knowledge map -> cohort-by-unit overlap state -> matching and
near-duplicate method -> suspected-overlap ledger -> externality axis -> permitted evaluation wording
-> privacy threat model -> authorisation/provider-term state -> residual risk -> claim ceiling`.

## Primary and official sources

- NIST. [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and
  Mitigations (AI 100-2e2025)](https://www.nist.gov/publications/adversarial-machine-learning-taxonomy-and-terminology-attacks-and-mitigations-0).
- NIST. [Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence
  Profile (AI 600-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence).
- EDPB. [Anonymisation and pseudonymisation](https://www.edpb.europa.eu/topics/ai-and-technology/anonymisation-pseudonymisation_en).

These sources provide threat and governance frames, not proof that a particular model, provider or
cohort is private or uncontaminated.
