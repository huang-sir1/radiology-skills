# Privacy, Governance, and Evaluation for Federated Imaging

Use this reference to convert “data stay local” into a testable threat model, assign governance
responsibilities, and evaluate whether federation improves performance without overstating
privacy, fairness, or external validity.

## Contents

1. Build a threat model before selecting controls
2. Map controls to threats
3. Assign governance and controller roles
4. Maintain a tamper-evident audit trail
5. Define the comparison ladder
6. Evaluate performance, calibration, and clinical utility
7. Match uncertainty to the inferential population
8. Evaluate fairness without hiding site effects
9. Distinguish federation from external validation
10. Reporting checklist

## 1. Build a threat model before selecting controls

List assets (images, labels, membership, site properties, model/update, credentials, audit
records), actors, trust assumptions, attack surfaces, and acceptable residual risks.

| Threat | Example in imaging federation | Relevant controls | Residual-risk question |
|---|---|---|---|
| Membership inference | Inferring whether a rare-case patient trained a site model | Regularization, access limits, privacy testing, differential privacy | Is the protected unit a study, patient, or site? |
| Gradient/update inversion | Reconstructing anatomy or attributes from an update | Secure aggregation, larger batches/local steps, clipping, differential privacy | Can the server or colluding clients observe individual updates? |
| Property inference | Inferring that a site treats a rare disease or uses a vendor/protocol | Secure aggregation, minimum cohort/round size, output minimization | Does the aggregate still reveal a small site's property? |
| Poisoning/backdoor | A compromised client inserts a trigger or degrades a subgroup | Authentication, provenance, robust aggregation, anomaly checks, quarantine | Can a malicious majority evade the control? |
| Model theft | Copying the global model or site-personalized head | Access control, key management, contractual controls, watermarking where justified | Who may retain models after withdrawal? |
| Collusion | Server and clients combine observations to isolate another site's update | Threshold secure aggregation, role separation, governance sanctions | What coalition size breaks the guarantee? |
| Metadata leakage | Participation, update size, timing, and failures reveal site activity | Traffic minimization/padding where needed, access-limited logs | Are metadata clinically or commercially sensitive? |
| Availability attack | A client or server prevents rounds from completing | Redundancy, timeouts, rate limits, rollback, incident response | What minimum safe federation remains? |

State whether the server is trusted, honest-but-curious, or potentially malicious; whether clients
can collude; and whether poisoning is in scope. “No raw data transfer” is a system property, not a
complete privacy analysis.

## 2. Map controls to threats

### Secure aggregation

Secure aggregation prevents the server from reading individual client updates while allowing an
aggregate to be computed. Specify:

- protocol and cryptographic implementation/version;
- minimum number of contributing clients and collusion threshold;
- authentication and key lifecycle;
- client-dropout tolerance and recovery;
- whether update size, timing, or participation remain visible;
- how rejected or anomalous updates can be investigated without exposing all updates.

Secure aggregation does not bound what the final model or aggregate reveals, stop malicious
updates, ensure consent, or create external validity. Small rounds and repeated differencing can
still expose information; set minimum aggregation groups and restrict queries/round composition.

### Differential privacy

Define the protected unit and adjacency relation first:

- **example/study-level DP** may not protect a patient with multiple correlated images;
- **patient-level DP** groups all patient contributions before clipping/accounting;
- **client/site-level DP** protects whether an entire site participated but usually requires much
  larger noise and a sufficient number of clients.

Declare the DP trust model and complete update path:

| DP model | Typical clipping/noise location | Who can see a pre-noise value? | Assumptions and trade-off |
|---|---|---|---|
| Central/curator DP | Trusted curator clips contributions or receives verifiably clipped contributions, aggregates, then adds noise before release | The curator may see individual updates unless secure aggregation hides them; even with secure aggregation it sees the pre-noise aggregate | Best utility at a fixed budget, but the curator and pre-release aggregate must be trusted/protected |
| Local DP | Each client clips and randomizes its update before transmission | No server sees that client's unnoised transmitted update; the client and its local environment do | Weak server-trust requirement but substantially more noise for equivalent protection; malicious clients may ignore the mechanism |
| Distributed DP | Clients clip locally and contribute noise shares, normally combined under secure aggregation | No single server should see individual pre-noise updates; the revealed aggregate is noisy if the threshold assumptions hold | Requires minimum honest/noncolluding participants, dropout-resilient noise generation, and explicit recovery when clients leave |

Report where clipping is performed, whether its bound is trusted, attested, or cryptographically
verified, where noise is generated, and whether the server, helper servers, clients, or colluding
coalitions can see individual updates or the pre-noise aggregate. State minimum participants,
dropout tolerance, collusion threshold, and what happens to privacy and utility if these
assumptions fail.

Report clipping norm, noise multiplier, sampling model, accountant, \(\varepsilon\), \(\delta\),
maximum rounds, and privacy-budget stopping rule. Include all exploratory releases and repeated
training runs in the governance of the privacy budget; do not report only the final run.

Evaluate the utility trade-off across a pre-specified privacy range:

- discrimination/task performance and uncertainty;
- calibration and decision thresholds;
- rare-class and small-site performance;
- subgroup fairness;
- convergence, rounds, and communication;
- empirical leakage tests without presenting attacks as proof of the formal guarantee.

Low epsilon is not automatically acceptable utility, and high epsilon is not automatically
meaningful protection. State the interpretation and residual risk agreed by governance and
privacy stakeholders.

### Check privacy-robustness compatibility

Plain secure aggregation reveals only a sum, which prevents the server from directly inspecting,
clipping, quarantining, or robustly aggregating individual updates. Do not simultaneously claim
update confidentiality and unconstrained per-client anomaly detection.

| Required capability | Compatibility with plain secure aggregation | Defensible option |
|---|---|---|
| Per-client anomaly inspection or attribution | Incompatible because individual updates are hidden | Client-side checks with attestation, a trusted execution environment, governed reveal/quarantine, or privacy-preserving MPC/zero-knowledge checks |
| Coordinate-wise median, trimmed mean, Krum-like robust aggregation | Generally incompatible with sum-only aggregation | Secure MPC/TEE implementation of the robust rule, or acknowledge that this defense is absent |
| Norm clipping for central/distributed DP | Server cannot verify hidden client clipping | Trusted/attested client clipping or cryptographically verified bounded updates |
| Dropout recovery | Compatible only within the protocol threshold | Pre-specify threshold, collusion model, noise-share recovery, and abort rule |
| Forensic investigation | Limited by confidentiality promise | Preserve signed provenance and aggregate diagnostics; define exceptional governed access before training |

Some secure-computation or trusted-hardware designs can reconcile these goals, but they change the
threat model and cost. Name the actual mechanism rather than listing secure aggregation, anomaly
detection, and robust aggregation as if they compose automatically.

### Complementary controls

Use transport encryption, mutual authentication, least-privilege access, signed code and
artifacts, secrets management, update validation, rate limits, secure execution where justified,
monitoring, and incident response. Cryptographic controls do not replace organizational controls,
and organizational controls do not replace technical threat analysis.

## 3. Assign governance and controller roles

Document roles using the applicable jurisdiction and agreements rather than assuming that the
coordinator is always the controller.

| Role/function | Decisions and responsibilities to assign |
|---|---|
| Local data controller/custodian | Eligibility, legal basis/consent, local access, data quality, subject rights, retention, breach response |
| Joint controllers, if applicable | Joint purposes/means, transparency, subject requests, allocation of obligations and liability |
| Processor/service provider | Documented instructions, security, subprocessors, deletion/return, audit cooperation |
| Coordinating center | Protocol/configuration release, client admission, round orchestration, model custody, deviations, publication record |
| Model owner/sponsor | Intended use, licensing, change control, validation, deployment authorization, post-study retention |
| Security/privacy lead | Threat model, control assurance, keys, incidents, privacy-budget approval, residual-risk acceptance |
| Independent monitoring/adjudication | Protocol deviations, serious incidents, fairness/safety review, stopping recommendations |

Agreements should address:

- permitted purpose and whether updates/models are personal or sensitive data;
- participating sites, subprocessors, hosting region, and cross-border transfer;
- model/update ownership, licensing, publication, intellectual property, and commercialization;
- site/patient withdrawal and whether already aggregated influence can be removed;
- retention and destruction of updates, checkpoints, logs, and keys;
- vulnerability disclosure, incident notification, suspension, and termination;
- audit rights, protocol amendments, and dispute resolution.

If a right-to-erasure or withdrawal request may require retraining, state the technical and
governance procedure before enrollment.

## 4. Maintain a tamper-evident audit trail

Audit records should permit reconstruction without containing patient-level data. Record:

- approved protocol, software/container hashes, dependencies, model initialization, and seeds;
- site/client identity or governed pseudonym, authorization status, and software version;
- round ID, timestamp, selected/completed/failed clients, and failure reason;
- aggregation rule, effective weights, update acceptance/rejection, anomaly alerts, and overrides;
- secure-aggregation threshold/status and key events without recording secrets;
- differential-privacy parameters, accountant state, cumulative budget, and releases;
- validation request, metric definition, result provenance, and who accessed it;
- checkpoint/model hash, deployment/retirement status, deviations, incidents, and approvals.

Use role-based access, retention limits, integrity protection, time synchronization, and a process
for correcting records without overwriting history. Test that the federation can resume from an
approved checkpoint and produce the same result within declared numerical tolerances.

## 5. Define the comparison ladder

At minimum compare:

| Comparator | Question answered | Required fairness condition |
|---|---|---|
| Local-only model at each site | Does collaboration improve over each site's own data? | Same local eligibility, architecture family/tuning budget, and test set |
| FedAvg | Does the proposed complexity beat standard federation? | Same clients, partitions, rounds/communication budget, architecture, and tuning access |
| Proposed federated method | Does heterogeneity/privacy/personalization handling help? | Pre-specified mechanism and matched compute/communication where possible |
| Centralized pooled oracle | What is the performance gap if lawful pooling were possible? | Same eligible pooled cohort and pipeline; label as oracle, not deployable if pooling is forbidden |
| Centralized simulation | Does the implementation reproduce a pooled reference in a sandbox? | Label clearly; simulation does not establish cross-institution governance or real-world feasibility |

Report paired differences with confidence intervals when predictions share the same test patients.
Avoid declaring federation superior from separate confidence intervals or from each method's best
uncontrolled run. Include convergence and communication/compute costs, not only predictive
performance.

External validation is a separate **evaluation layer**, not another model in this ladder. Freeze
the local-only, centralized oracle/simulation, FedAvg, and proposed models, then run every eligible
model on the same untouched external data with no refitting, threshold selection, recalibration,
or preprocessing estimation. Present a model-by-evaluation-domain matrix. If governance or input
availability prevents a model from running externally, mark that cell unavailable and explain why;
do not replace it with a differently tuned model.

## 6. Evaluate performance, calibration, and clinical utility

Use patient-level inference and uncertainty. Select task-appropriate metrics:

- classification: sensitivity, specificity, AUC/AUPRC where appropriate, predictive values at
  clinically relevant prevalence, and thresholded confusion matrices;
- segmentation/detection: case-level and lesion-level metrics, false positives per case, and
  clinically meaningful size/location strata;
- prognosis: discrimination, calibration over time, and decision-analytic utility with censoring
  handled correctly.

Calibration must be assessed overall and per site using calibration-in-the-large/intercept, slope,
reliability plots or flexible calibration curves, and a proper scoring rule such as Brier score.
Do not infer calibration from AUC. If thresholds or recalibration are site-specific, fit them on
local training/validation data and evaluate on disjoint test patients.

Report clinical utility at pre-specified thresholds where possible. A federated model can improve
average AUC while worsening calibration or net benefit at a small center.

## 7. Match uncertainty to the inferential population

State the estimand and both sampling units before choosing confidence intervals:

- **Conditional on the observed sites:** sites are fixed; uncertainty concerns new patients from
  these institutions. Resample patients within site (site-stratified bootstrap), preserve each
  site's contribution, and use paired patient resampling for model comparisons.
- **Generalization to a population of new sites:** sites are sampled units as well as patients.
  Use a cluster bootstrap that resamples sites with all their patients, a hierarchical bootstrap
  that samples sites and then patients within sampled sites, a site-level
  random-effects/hierarchical model, or another justified site-clustered analysis. With few sites,
  site-level uncertainty is intrinsically imprecise; show site estimates and avoid asymptotic
  certainty.
- **Performance at one named external site:** inference is conditional on that site unless the
  protocol samples multiple external sites. Resample its patients; do not describe a single
  convenience center as a random sample of institutions.

Identify whether the metric is patient-weighted (micro-average), site-weighted (macro-average),
or target-population weighted. The patient is the sampling unit for new-patient inference; the
site is the cluster and sampling unit for new-site inference. For repeated images, lesions, or
timepoints, resample at the patient level or use an appropriate multilevel model.

Leave-one-site-out (LOSO) predictions are out-of-site for each held-out center, but fold estimates
are not independent because their training federations overlap. Do not treat the \(K\) folds as
\(K\) independent experiments, average fold-specific standard errors, or apply a naive paired
t-test across folds. Analyze pooled out-of-fold patient predictions with site clustering when the
estimand is patient-weighted, summarize held-out-site effects with an explicitly site-level or
hierarchical model when targeting new sites, and report per-site results. Repeated training seeds
measure algorithmic variability, not additional independent sites or patients.

## 8. Evaluate fairness without hiding site effects

Define protected or clinically vulnerable subgroups from the intended-use context. For each site
and subgroup with adequate support, report:

- sample size and outcome/event count;
- discrimination/task performance and uncertainty;
- sensitivity/specificity or error rates at the intended threshold;
- calibration and predictive values;
- abstention/failure rates where applicable.

Show intersectional analyses when scientifically and statistically supportable. Suppress or pool
unstable estimates transparently rather than presenting noisy rankings. Examine whether privacy
noise, equal-site weighting, personalization, or client dropout disproportionately harms small
sites or rare subgroups.

Choose the fairness target explicitly—equalized error rates, calibration, worst-site robustness,
or another clinically justified criterion—and acknowledge incompatibilities and trade-offs.
Fairness on participating sites does not guarantee fairness at a new site.

## 9. Distinguish federation from external validation

Federation describes **how model parameters are learned**. External validation describes **where
an untouched model is evaluated**. They are orthogonal.

Evaluation patients must never contribute training updates/data, preprocessing estimates,
hyperparameter or stopping feedback, threshold selection, or calibration to the model being
evaluated. Separately ask whether **other patients from the same site/domain** influenced
development:

| Evaluation data | Evaluation patients influenced the model? | Evaluation site/domain influenced development through other patients? | Valid interpretation |
|---|---:|---:|---|
| New held-out patients at a training site | No | Yes | Internal participating-site generalization |
| Held-out patients at every participating site | No | Yes | Multi-site internal evaluation |
| Site excluded from a fresh leave-one-site-out federation | No | No, for that retraining fold | Geographic/site holdout for that fold |
| Nonparticipating center opened once after freeze | No | No | External validation |
| Disjoint test patients at a new site after local personalization | No | Yes, through separate adaptation patients | Site-adaptation evaluation; report zero-shot external performance separately |

Never write “externally validated across five federated sites” if all five sites contributed
updates. Instead state that performance was tested on held-out patients at participating sites.
External validation requires a center, period, or population that had no influence on model,
preprocessing, hyperparameter, stopping, threshold, or calibration choices.

## 10. Reporting checklist

- State why raw pooling was prohibited and whether a pooled oracle/simulation was possible.
- Describe controller/processor roles, agreements, approvals, and unresolved governance limits.
- Publish the threat model and map each claimed protection to a control.
- Report secure-aggregation assumptions and differential-privacy parameters where used.
- State the protected unit and account for repeated training/release.
- Report local, FedAvg, proposed, and centralized/simulated model comparisons.
- Apply the same frozen-model set as an external-evaluation layer and report the
  model-by-evaluation-domain matrix, including unavailable cells.
- Report overall, site-level, and justified subgroup performance with uncertainty.
- State whether inference is conditional on observed sites or targets new sites; identify site and
  patient sampling units, resampling/modeling method, and LOSO-fold dependence handling.
- Include calibration, clinically relevant thresholds/utility, failure cases, communication, and
  compute.
- Label participating-site, leave-one-site-out, adaptation, and external results correctly.
- Record software/model hashes, round participation, deviations, incidents, and privacy budget.
- Bound conclusions: federation reduces raw-data movement; it does not alone prove privacy,
  compliance, fairness, robustness, or transportability.
