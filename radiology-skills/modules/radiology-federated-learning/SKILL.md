---
name: radiology-federated-learning
description: "Use when multiple imaging centers cannot pool raw data and need a federated-learning research design. Chooses horizontal, vertical, split, or personalized federation; plans aggregation, non-IID handling, site weighting, secure aggregation, differential privacy, threat modeling, governance, communication, reproducibility, fairness, calibration, and centralized/local/external baselines. Never presents federated learning alone as proof of privacy or external validity."
---

# Federated Learning for Multi-Center Imaging

Use this skill to design or audit a federated imaging study when raw patient data cannot be
pooled. Treat federation as a distributed training architecture—not as automatic privacy,
regulatory compliance, fairness, or external validation.

The approved metadata lists horizontal, vertical, split, and personalized federation together,
but do **not** treat them as peer topology choices. Immediately decompose the design into
data-ownership, computation, coordination/trust, and output-objective axes as specified below.

## Core stance

- **Governance before algorithms.** Confirm that each site may compute and transmit the planned
  updates, that controller/processor roles are assigned, and that incident and withdrawal
  procedures exist. If this is infeasible, stop; do not solve a governance barrier with FedAvg.
- **Specify orthogonal design axes.** Describe data partition/ownership, computation architecture,
  coordination/trust, and output objective separately. Horizontal data can use full-model or split
  computation and can produce one global, clustered, or personalized model.
- **Keep a real baseline ladder.** Compare local-only models, a federated FedAvg baseline, a
  centralized pooled-data oracle when lawful or a clearly labeled simulation when not, and the
  proposed federated method.
- **Apply external evaluation as a layer.** After development is frozen, evaluate each eligible
  local, centralized, FedAvg, and proposed model on the same untouched external domain; external
  validation is not itself a comparator.
- **Model non-IID structure explicitly.** Scanner vendor, protocol, prevalence, referral pathway,
  annotation practice, sample size, and outcome availability can all differ by site.
- **Define the adversary.** Secure aggregation and differential privacy address different threats;
  neither protects against every leakage, poisoning, or governance failure.
- **Separate collaboration from transportability.** A center that trained the federation is not
  external validation, even if it never shared raw data.

## When to open extra files

| File | Open when |
|---|---|
| [references/federated-design.md](references/federated-design.md) | Selecting federation type, FedAvg and alternatives, site weighting, non-IID handling, communication/failure policy, or site-holdout design |
| [references/privacy-governance-evaluation.md](references/privacy-governance-evaluation.md) | Defining leakage threats, secure aggregation, differential privacy, controller roles, audit trails, fairness, calibration, baseline comparisons, or external-validity claims |

## Workflow

### 1. Establish governance feasibility

Create a site-by-site feasibility table covering data-controller roles, legal basis/consent,
permitted update types, cross-border restrictions, security review, model ownership, publication
rights, withdrawal/deletion, incident response, and approval status. Record unresolved items as
blocking decisions. Federation is not feasible until every participating site can execute the
same approved protocol or an explicitly justified site-specific variant.

### 2. Select the federation topology

Map patient overlap, feature overlap, label location, compute capacity, network constraints, and
trust boundaries. Specify four axes rather than forcing peer alternatives into one label:
(1) horizontal, vertical, or hybrid data partition/ownership; (2) full-model FL, split learning,
or SplitFed computation; (3) centralized/decentralized coordination and server/client trust; and
(4) global, clustered/multi-task, or personalized output. Explain the selected combination—for
example, horizontal data ownership + full-model synchronous coordination + honest-but-curious
server + personalized heads. State entity-resolution implications for cross-site patient linkage
and activation/update flows for the computation architecture.

### 3. Freeze the baseline ladder

Pre-specify:

1. each site's local-only model;
2. a pooled centralized oracle if lawful, or a clearly labeled centralized simulation;
3. FedAvg as the primary federated baseline;
4. the proposed heterogeneity-aware or personalized method.

Use the same eligible population, preprocessing family, architecture capacity, tuning budget, and
endpoint definition wherever the comparison permits. Do not call a comparison fair when the
proposed model receives more data, tuning, or compute.

### 4. Specify the training protocol

Lock patient-level partitions before preprocessing. Declare participating clients per round,
client sampling, local epochs/steps, batch size, optimizer and learning rate, server aggregation,
site weighting, number and stopping rule of communication rounds, checkpoint selection,
hyperparameter-search boundary, random seeds, update compression, encryption, timeout, retry,
dropout, and recovery rules. Never use the final test or held-out center to choose rounds,
hyperparameters, aggregation, or personalization.

### 5. Write the threat model

Name protected assets, trusted components, adversaries, capabilities, attack surfaces, and
acceptable residual risk. At minimum assess membership inference, gradient/update inversion,
property inference, malicious-client poisoning/backdoors, model theft, collusion, and metadata
leakage. Map each control—transport security, authentication, secure aggregation, clipping,
differential privacy, anomaly detection, access control, and audit logging—to a named threat.
For differential privacy, declare central, local, or distributed trust; clipping/noise location;
who can see pre-noise individual or aggregate updates; and dropout/collusion assumptions. State
whether secure aggregation prevents update-level anomaly inspection or robust aggregation and
what privacy-preserving substitute is used. Report unmitigated threats rather than asserting that
“data never leave the hospital.”

### 6. Analyze heterogeneity

Profile each site before training: population, prevalence, scanner/vendor/field strength,
acquisition and reconstruction, annotation protocol, missingness, outcome ascertainment, sample
size, and compute/network capability. Quantify label, feature, quantity, and concept shift.
Compare FedAvg with a justified option such as FedProx, SCAFFOLD, FedBN, clustered FL, or local
fine-tuning/personalization. Treat site weighting as an estimand choice, not a convenience.

### 7. Evaluate performance and transportability

Report patient-level metrics with uncertainty overall and by site: discrimination or task
accuracy, calibration, clinically relevant thresholds/utility, failure modes, and subgroup
fairness. Define whether inference is conditional on the observed sites or targets a population
of new sites; name patient and site sampling units and use site-stratified, site-clustered, or
hierarchical resampling accordingly. Include local-versus-federated and
centralized-versus-federated paired comparisons. Use leave-one-site-out retraining or an untouched
nonparticipating center to test transportability; account for dependence across leave-one-site-out
folds because their training sets overlap. Label participating-site evaluation as internal, even
when updates rather than raw data were shared. Treat the external set as an evaluation layer:
apply it without refitting to every frozen local, centralized, FedAvg, and proposed model that can
lawfully and technically be run there, and report unavailable cells rather than changing the
comparator set.

### 8. Make the federation reproducible

Version code, containers, model initialization, preprocessing, ontology/label rules, configuration,
site manifests, dependency lockfiles, seeds, and aggregation logic. Hash approved artifacts and
record round-level participation, failures, update acceptance/rejection, privacy parameters,
checkpoints, and deviations in a tamper-evident audit trail. Provide a rerun plan that does not
require exporting patient-level data.

## Output contract

1. **`Governance feasibility matrix`** — site approvals, roles, permitted flows, unresolved blockers.
2. **`Federation topology`** — the selected ownership, computation, coordination/trust, and output
   axes, including their combined data flows and linkage assumptions.
3. **`Baseline ladder`** — local, centralized/simulated, FedAvg, and proposed models.
4. **`Training protocol`** — partitions, clients/round, local/server optimization, weighting,
   communication, stopping, failure handling, and tuning boundary.
5. **`Threat-control matrix`** — assets, adversaries, attacks, controls, and residual risks.
6. **`Heterogeneity plan`** — site/scanner shifts, diagnostics, method choice, and sensitivity tests.
7. **`Evaluation plan`** — overall/site/subgroup metrics, calibration, utility, target inferential
   population, site/patient sampling units, dependence handling, true site holdout, and the
   external-evaluation matrix applied across frozen models.
8. **`Reproducibility record`** — versions, hashes, seeds, manifests, audit events, and deviations.
9. **`Bounded claims`** — what federation, privacy controls, and validation do and do not establish.

## Quality bar

A defensible study can be reconstructed from approved artifacts, compares against local and
FedAvg baselines, survives client failure without changing the estimand silently, quantifies
site-level heterogeneity and calibration, and tests a genuinely unseen center. It never equates
federated learning with anonymization, differential privacy, fairness, or external validity.

## Handoffs

- Cohort construction, patient-level splitting, and external-validation design → `radiology-design`.
- CNN/Transformer architecture, optimization, and imaging input pipelines → `radiology-deep-learning`.
- Diagnostic metrics, confidence intervals, calibration, fairness, and model comparison →
  `radiology-stats`.
- Ethics, consent, privacy language, and governance statements → `radiology-ethics`.
- DICOM de-identification, data/code availability, and FAIR metadata → `radiology-data`.
- CLAIM/TRIPOD+AI and protocol reporting audits → `radiology-reporting`.
- Prospective deployment, reader studies, monitoring, and rollback → `radiology-translation`.
