# Federated Imaging Study Design

Use this reference to choose a federation structure, define fair baselines, handle imaging-site
heterogeneity, and pre-specify communication and site-holdout evaluation.

## Contents

1. Specify federation on orthogonal design axes
2. Define the estimand before choosing weights
3. Use FedAvg as the primary federated baseline
4. Select heterogeneity-aware alternatives for a stated mechanism
5. Characterize imaging non-IID data
6. Pre-specify communication and failure behavior
7. Keep partitioning and tuning leakage-safe
8. Design site holdout to answer the intended question
9. Minimum design record

## 1. Specify federation on orthogonal design axes

Start with a table whose rows are institutions and whose columns are patients, images, clinical
features, labels, and compute capability. Mark overlap and the party permitted to access each
element.

Do not place horizontal/vertical FL, split learning, and personalization in one mutually exclusive
menu. They answer different questions:

| Axis | Options | Selection question | Main failure |
|---|---|---|---|
| Data partition and ownership | Horizontal, vertical, hybrid | Are patients disjoint or overlapping, and are features/labels aligned or partitioned? | Mislabeling different modalities across disjoint patients as vertical FL |
| Computation architecture | Full-model FL, split learning, SplitFed | Does each client train a full model, exchange cut-layer activations, or combine split learning with federated client/server aggregation? | Activation leakage, cut-layer bottlenecks, or unreported server-side training |
| Coordination and trust | Central server, hierarchical coordinators, peer/decentralized; trusted, honest-but-curious, or malicious actors | Who schedules, observes, aggregates, and can collude? | A claimed privacy control assumes a more trusted coordinator than governance permits |
| Output objective | One global model, clustered/multi-task models, shared representation plus local heads, local fine-tuning/personalization | Is one decision function clinically appropriate across sites, and what adaptation is available at deployment? | Post-hoc personalization overfits small local validation sets |

Horizontal FL means similar features/labels across different patients. Vertical FL means features
or labels are partitioned across parties for overlapping patients and therefore requires
privacy-preserving entity resolution and explicit linkage governance. If different centers hold
different patients with different modalities, the design is usually horizontal FL with
heterogeneous or missing features—not vertical FL.

The axes are conceptually orthogonal, but not every combination is technically appropriate.
Horizontal ownership can use full-model FL, split learning, or SplitFed. Vertical ownership
usually requires entity resolution plus split or other secure joint computation; ordinary
independent full-model FedAvg is not valid when no party has a complete feature vector. SplitFed
combines a split network with federation across multiple client-side models and, depending on the
variant, server-side components; specify which parameters and activations are shared, averaged,
or kept local. A global, clustered, or personalized objective can sit on top when its required
components and adaptation data exist at deployment.

Write the final design as an explicit combination, for example:

> Horizontal ownership + full-model synchronous FL + central honest-but-curious coordinator with
> threshold secure aggregation + global backbone with locally calibrated heads.

Then diagram every image, feature, activation, gradient, model update, aggregate, and metric flow.
Verify that every local or personalized component can be estimated and maintained at deployment.

## 2. Define the estimand before choosing weights

State whose performance the model should optimize:

- **Patient-average estimand:** weight sites approximately by eligible training patient count.
  Large sites dominate, matching the average participating patient but potentially neglecting
  small centers.
- **Site-average estimand:** give sites equal or capped influence. This targets performance across
  institutions but no longer estimates the pooled patient average.
- **Target-population estimand:** weight by a pre-specified deployment population. Document the
  external target weights and uncertainty.
- **Fairness- or robustness-constrained objective:** protect the worst site or subgroup. Report the
  accuracy trade-off and avoid choosing constraints from the test set.

Sample-size weighting is not automatically unbiased when sites differ in labels, measurement, or
case mix. Pre-specify caps, normalization, and the treatment of clients with zero eligible cases
in a round.

## 3. Use FedAvg as the primary federated baseline

For round \(t\), the server distributes parameters \(w_t\). Each selected site \(k\) performs the
declared local optimization and returns \(w_{t+1}^{(k)}\) or an update. The server computes:

\[
w_{t+1} = \sum_{k \in S_t} \alpha_k w_{t+1}^{(k)}, \qquad
\sum_{k \in S_t}\alpha_k = 1.
\]

Declare:

- how \(S_t\) is sampled and whether every clinical site must participate;
- whether \(\alpha_k\) is based on patient count, site equality, effective sample size, or a target
  population;
- local epochs/steps, batch size, optimizer, learning rate, augmentation, and imbalance handling;
- whether optimizer state is local, reset, or aggregated;
- the validation-only stopping rule and checkpoint selection;
- how missing, late, corrupt, or rejected updates change the denominator.

FedAvg must be tuned with the same care as the proposed method. An intentionally weak FedAvg
configuration is not a valid baseline.

## 4. Select heterogeneity-aware alternatives for a stated mechanism

| Method family | Use when | What to pre-specify | Main caution |
|---|---|---|---|
| FedProx | Local objectives drift because distributions or local work differ | Proximal coefficient and tuning data | Does not by itself solve label mismatch or scanner confounding |
| SCAFFOLD/control variates | Client drift under non-IID sampling is a central concern | Control-state storage, update equations, and extra communication | More state and implementation complexity; compare at matched communication cost |
| FedBN/local normalization | Scanner/style shift appears in feature statistics | Which normalization parameters remain local | Deployment at a new site needs an adaptation rule; local BN may encode site identity |
| Server adaptive optimization | Aggregated updates vary greatly in scale/direction | Server optimizer, momentum, learning rate, and initialization | Gains may reflect extra tuning rather than robustness |
| Clustered/multi-task FL | Stable groups of sites require different optima | Clustering inputs, update frequency, minimum cluster size | Do not learn clusters from test performance |
| Local fine-tuning | A global initializer transfers but local calibration differs | Frozen layers, steps, regularization, and local validation split | Small sites can overfit; evaluate both before and after adaptation |
| Shared backbone + local head | Representation can be shared but labels/prevalence differ | Shared/local parameter boundary and head training | A local head cannot repair incompatible endpoint definitions |
| Meta-learning/personalized objectives | Rapid adaptation to new clients is the estimand | Adaptation data budget and unseen-client protocol | Requires genuine unseen-client evaluation |

Add one alternative only when the observed or anticipated heterogeneity supports its mechanism.
Retain FedAvg and local-only comparators. Match the communication, compute, architecture, and
tuning budget when interpreting gains.

## 5. Characterize imaging non-IID data

Build a pre-training site profile:

| Dimension | Examples | Diagnostic |
|---|---|---|
| Quantity shift | Site size, rare-class counts, follow-up completeness | Counts, effective sample size, class support |
| Label shift | Disease prevalence, referral enrichment | Site-wise prevalence with uncertainty |
| Covariate shift | Age, sex, severity, comorbidity | Standardized differences and distribution plots |
| Acquisition shift | Vendor, model, field strength, sequence, dose, reconstruction kernel | Protocol/vendor tables; image-intensity or embedding summaries |
| Annotation shift | Reader specialty, contour protocol, report-derived labels | Inter-reader/site agreement and adjudication audit |
| Concept shift | Same image pattern maps differently to label/management | Site interactions, residual/failure analysis |
| Missingness shift | Absent sequences, incomplete clinical variables, loss to follow-up | Site-by-variable missingness and missingness mechanism |
| Compute/network shift | GPU memory, bandwidth, uptime | Capability and round-duration profile |

Keep harmonization and preprocessing inside each training fold and site. Never use the held-out
site to fit intensity normalization, feature harmonization, label mappings, thresholds, or
personalization. If harmonization requires pooled statistics, specify a privacy-preserving
protocol and include its messages in the threat model.

Recommended sensitivity analyses:

- equal-site versus patient-count weighting;
- balanced versus naturally imbalanced client participation;
- one local epoch versus more local work to expose client drift;
- vendor/protocol/site-stratified performance and calibration;
- removal of the largest site;
- removal of sites with incompatible label or annotation processes;
- global model versus site-personalized model;
- matched communication-cost comparison of alternatives.

## 6. Pre-specify communication and failure behavior

Report both **round count** and **transmitted bytes**, plus wall-clock time when systems claims are
made. Include model/update size, compression or quantization, secure-aggregation overhead, client
selection, and synchronization mode.

For synchronous training, define:

- minimum clients required to complete a round;
- timeout and straggler policy;
- whether a late update is discarded or used later;
- retry count and checkpoint rollback;
- secure-aggregation dropout tolerance;
- deterministic aggregation order or numerical-tolerance policy.

For asynchronous training, define:

- staleness measure and weighting;
- maximum accepted staleness;
- replay/duplicate detection;
- how rapidly contributing sites are prevented from dominating;
- validation and stopping under a continuously changing model.

Failure injection should cover client dropout, network interruption, corrupt update, incompatible
software/model version, exhausted privacy budget, and server restart. Record whether each event
aborts, skips, retries, quarantines, or rolls back the round. Never silently alter site weights
after failure.

## 7. Keep partitioning and tuning leakage-safe

- Split patients locally before any data-dependent preprocessing.
- Keep all studies, lesions, slices, timepoints, and derived variants for one patient in one
  partition.
- Reserve local validation sets for global choices; do not relay test-derived metrics to tune the
  federation.
- Treat repeated rounds as repeated access to validation information. Pre-specify stopping and
  limit adaptive experimentation.
- Fit site-specific personalization and thresholds on training/validation data only.
- If architecture or hyperparameters are selected across sites, use nested or otherwise
  leakage-safe federated validation.
- Freeze the complete pipeline before opening a site-holdout or external test set.

## 8. Design site holdout to answer the intended question

Three designs answer different questions:

1. **Participating-site internal evaluation:** local test patients at sites that contributed
   updates. This measures new-patient performance within collaborating domains, not external
   transportability.
2. **Leave-one-site-out federation:** train a fresh federation excluding one site, freeze the
   pipeline, and test on that site. Repeat by site when feasible. This estimates transport to a
   new center but requires full retraining for each fold.
3. **Untouched nonparticipating external center:** finalize all choices using participating sites,
   then evaluate once at a center that supplied no updates, preprocessing statistics, thresholds,
   or tuning feedback. This is the clearest external test.

For personalization at a new site, separate zero-shot performance from adaptation performance.
Declare the adaptation sample size and labels, keep a disjoint test set, and show the learning
curve versus adaptation budget.

## 9. Minimum design record

Record the following before training:

- clinical question, endpoint, unit of analysis, target population, and deployment site type;
- site eligibility, ownership matrix, federation type, and trust assumptions;
- selected data-ownership, computation, coordination/trust, and output axes plus their combination;
- local and global partition manifests without patient identifiers;
- architecture and fair baseline ladder;
- client/round sampling, local work, aggregation, weighting, stopping, and failure policy;
- heterogeneity hypotheses and pre-specified alternative;
- site-holdout or external evaluation protocol;
- compute, communication, reproducibility, and audit requirements.
