# Fusion Architecture

Choose the architecture only after defining the analysis objective, patient-by-modality
availability matrix, matched n, validation groups, and modalities available at
deployment. Define an endpoint for supervised prediction, but do not force one onto
unsupervised discovery. A method name is not a justification.

## Architecture comparison

| Approach | Primary use | Data requirement | Main failure mode |
|---|---|---|---|
| **Early fusion** | Prediction from one concatenated feature matrix | Mostly matched patients; aggressive block-wise scaling and dimension control; enough events for the combined feature space | The largest or noisiest block dominates; collinearity, batch effects, and p >> n overfitting are hidden inside one matrix |
| **Intermediate fusion** | Joint embeddings or block-specific encoders followed by a shared model | Sufficient matched n to learn each representation and the joint layer; nested representation learning | Flexible embeddings memorize site, batch, or outcome proxies; weak blocks are suppressed without transparent contribution |
| **Late fusion** | Combine calibrated block-specific predictions | Each block can support a stable model; predictions can be aligned for the same endpoint; weights tuned inside resampling | Misses cross-block interactions; unstable or overfit base models contaminate the ensemble; complete prediction vectors may still be required |
| **SNF** | Unsupervised patient-subtype discovery from fused similarity networks | Matched samples across included views; meaningful per-view distance and neighborhood choices | Clusters reflect scale, batch, or tuning choices; subtype stability and outcome association are mistaken for validation |
| **MOFA / MOFA+** | Interpretable latent factors across heterogeneous views | Aligned samples and adequately informative blocks; factor number and sparsity selected without outcome leakage; can accommodate some missing views | Factors capture technical variation, dominant blocks, or low-variance structure; post hoc factor selection inflates outcome associations |
| **DIABLO** | Supervised multi-block signatures for classification | Matched labeled samples, correlated signal across blocks, and nested component/feature tuning | Outcome-guided selection overfits small n; forced cross-block correlation can discard complementary but uncorrelated predictors |
| **iCluster family** | Joint latent subtype discovery, especially across molecular blocks | Largely matched samples, compatible block models, and enough n for latent-variable estimation | Convergence and cluster instability; imaging or clinical blocks violate distributional assumptions; clusters are treated as fixed biological entities |
| **Graph fusion** | Encode known sample, pathway, spatial, or cross-modal relationships | A justified graph whose edges are external or training-derived; enough data to estimate graph parameters; edge construction nested when learned | The graph imports circular outcome information, database bias, arbitrary edges, or site structure; graph complexity overwhelms matched n |
| **Deep multimodal fusion** | Nonlinear joint representations, cross-attention, or generative multimodal models | Large matched n or credible pretraining, rigorous regularization, realistic missing-modality training, and independent validation | Capacity outruns n; shortcuts encode site/batch; attention is called explanation; modality dropout masks weak complete-case performance |

## Selection rules

1. **Start with the objective.** Use latent-factor or network methods for discovery,
   supervised methods for a pre-specified endpoint, and do not select subtypes by how
   well they separate an outcome later.
2. **Match complexity to the limiting count.** The universal limiting count is the
   patients available to the fitted joint component, not the total number in any one
   source; endpoint events are an additional limit only for supervised outcome models.
   If support is weak, prefer late fusion, pre-specified summaries, or fewer blocks.
3. **Respect missingness.** Late or pattern-specific models may be more defensible when
   blocks are often absent. MOFA can estimate factors with some missing views, but that
   capability does not remove selection bias or create an observed assay.
4. **Protect block identity.** Normalize and reduce each block separately. Do not let
   thousands of transcripts outweigh a small clinical block simply by feature count.
5. **Require deployable inputs.** A model that needs pathology, sequencing, or spatial
   assays at inference is not an imaging-only model. State the intended input set.
6. **Nest all learned choices.** Similarities, factors, components, encoders, graphs,
   features, fusion weights, and hyperparameters belong inside training resampling.

## Unsupervised discovery branch

SNF, MOFA/MOFA+, and iCluster may be used to discover patient structure without a
predictive endpoint. In that branch:

1. lock preprocessing, similarity or factor construction, component or cluster number,
   and tuning rules without using outcomes;
2. quantify resampling and perturbation stability rather than choosing the solution with
   the most favorable survival curve or p value;
3. define a **prespecified cluster assignment** or factor-projection rule that can be
   applied to new patients without reclustering the discovery and replication cohorts;
4. require independent replication of the structure when claims extend beyond
   exploration;
5. use outcomes only as secondary associations, not for cluster or factor selection;
6. report cluster sizes, assignment uncertainty, cluster/factor alignment after block
   removal, resampling stability, site/batch enrichment, replication, and failure to
   replicate.

Calibration and predictive comparators are not mandatory for a genuinely unsupervised
aim. If the discovered representation is later used for prediction, evaluate that
downstream model as a separate supervised analysis with nested training and the baseline
ladder below.

## Baseline ladder

Every predictive fusion study should report:

1. clinical-only;
2. each single modality;
3. strongest single modality plus clinical variables;
4. simple regularized early fusion or calibrated late fusion;
5. proposed architecture.

Compare the locked models on the same evaluation patients. Report uncertainty and
calibration as well as discrimination or prediction error. Added complexity is
justified only when it gives reproducible added value over the simple fusion baseline.

## Interpretation boundaries

- A shared factor, graph edge, attention weight, or selected cross-block signature is
  an association unless independently corroborated.
- Test only pre-specified interactions as confirmatory; label data-driven interactions
  exploratory and validate them independently.
- Correlated blocks can make marginal ablation misleading. Pair leave-one-block-out
  results with single-block performance and conditional or grouped permutation analyses.
- Stable internal resampling does not replace temporal, geographic, site-held-out, or
  external validation.
