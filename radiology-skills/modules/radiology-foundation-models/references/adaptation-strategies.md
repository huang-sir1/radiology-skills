# Foundation-Model Adaptation Strategies

Use this reference after the downstream task, input contract, pretraining provenance, overlap
status, frozen splits, and baseline ladder are defined. Choose the least complex strategy that can
answer the study question; parameter efficiency is a resource property, not evidence of better
generalization.

## Contents

- [Decision table](#decision-table)
- [Shared rules](#shared-rules)
- [Zero-shot evaluation](#1-zero-shot-evaluation)
- [Frozen encoder with linear or shallow probe](#2-frozen-encoder-with-linear-or-shallow-probe)
- [Partial fine-tuning](#3-partial-fine-tuning)
- [Full fine-tuning](#4-full-fine-tuning)
- [Adapters](#5-adapters)
- [LoRA and related parameter-efficient updates](#6-lora-and-related-parameter-efficient-updates)
- [Prompt learning](#7-prompt-learning)
- [Continued self-supervised or domain-adaptive pretraining](#8-continued-self-supervised-or-domain-adaptive-pretraining)
- [Domain adaptation](#9-domain-adaptation)
- [Selecting a route](#selecting-a-route)

## Decision table

| Strategy | Trainable component | Best-supported use | Main limitation | Minimum comparison |
|---|---|---|---|---|
| Zero-shot | None; prompts or label mappings may be selected on development data | The pretrained model exposes a valid native interface for the target labels, retrieval task, segmentation prompts, or image-text matching | Prompt and label semantics may not transfer; zero-shot is invalid when a new trained head is required | Native zero-shot versus simple task baseline; prompt variants chosen without test access |
| Linear probe | Linear classifier/regressor, or a simple task head, on frozen representations | Measure the accessibility of downstream information and establish a cheap adaptation baseline | A poor probe may reflect pooling or head limitations rather than absent information | Fixed features with prespecified pooling versus conventional transfer and task-specific baseline |
| Partial fine-tuning | Task head plus selected late blocks, normalization layers, or bias terms | Moderate labeled data and domain shift where full tuning is unstable or too costly | Layer choice adds tuning degrees of freedom and may cause partial forgetting | Frozen probe, prespecified partial variants, and full tuning when feasible |
| Full fine-tuning | All parameters | Sufficiently large/diverse labeled data, material task shift, and compute for robust tuning and repeated runs | Overfitting, catastrophic forgetting, high memory/compute, and poor reproducibility | Frozen/parameter-efficient routes and a strong task-specific model |
| Adapters | Small inserted bottleneck or residual modules, usually with backbone frozen | Multiple tasks or sites need compact, swappable trainable modules | Adapter placement/width adds choices; inference path changes | Same backbone with probe and matched-budget LoRA or partial tuning |
| LoRA/related low-rank updates | Low-rank matrices on selected weight projections | Memory-limited tuning of large encoders or vision-language models | Rank and target-module choices can hide substantial search; merged weights complicate provenance | Same backbone, rank/module ablations, parameter count, probe, and another tuning route |
| Prompt learning | Trainable text, visual, or multimodal prompt embeddings/tokens | A prompt-conditioned architecture already supports the target interface | Learned prompts may encode dataset-specific shortcuts and can be brittle to wording or site shift | Handcrafted zero-shot prompts, prompt ensemble where prespecified, and task baseline |
| Continued self-supervised/domain-adaptive pretraining | Backbone updated on authorized unlabeled in-domain inputs before downstream adaptation | A defined modality, anatomy, protocol, or institution shift may benefit from additional representation learning | High compute, forgetting, negative transfer, and target-development leakage | Same initial checkpoint directly fine-tuned on the downstream task under a fair budget |
| Domain adaptation | Alignment, reweighting, normalization, self-training, adversarial, or test-independent target adaptation components | A defined source-to-target shift is central and unlabeled or labeled target-development data are legitimately available | Target leakage, negative transfer, and a changed estimand if the target test distribution is used | Source-only model, simple target calibration/normalization, and shift-specific baselines |

## Shared rules

Apply these rules to every strategy:

1. split patients and keep every repeated examination, lesion, slice, patch, or frame from one
   patient in one partition; choose same-site, site-held-out, or temporal evaluation according to
   the estimand and label it accurately;
2. fit preprocessing, pooling, head selection, prompt selection, calibration, and thresholds using
   development data only;
3. state exactly which parameters train and which remain frozen;
4. use identical eligible samples, inputs, outcome definitions, augmentations where compatible,
   splits, metrics, and a prespecified tuning policy for comparisons;
5. report trainable and total parameters, memory, runtime, accelerator-hours, seeds, and variability
   across repeated runs;
6. preserve the original checkpoint identity and hash plus every adapter, delta, prompt, or merged
   checkpoint needed to reconstruct the result;
7. audit the license for modification, redistribution, commercial use, derivative checkpoints, and
   model-output restrictions before selecting a route.

## 1. Zero-shot evaluation

Use zero-shot evaluation only when the model has a native inference contract that maps to the
downstream task. Examples include image-text similarity for a defined label set, a promptable
segmenter, retrieval, or a model with documented zero-shot classification behavior.

Pre-specify:

- label names, synonyms, negation handling, prompt templates, prompt ensembling, and class mapping;
- image or volume aggregation, cropping, normalization, and text preprocessing;
- whether prompts were authored from general knowledge, tuned on development data, or transferred
  from another dataset;
- how ambiguous, unsupported, or out-of-vocabulary labels are handled.

Prompt selection on the test set is tuning, even when no model weights change. Do not call inference
zero-shot if outcome labels, examples, or target-cohort feedback were used to optimize prompts.
Report sensitivity to reasonable prompt variants and include a simple trained baseline when labels
are available.

For promptable segmentation, record the spatial prompt type and provenance for every evaluation:
points, boxes, scribbles, or masks; ground-truth annotation, simulated click, human operator, or
upstream detector/segmenter; and whether it is available at the intended prediction time. Quantify
human time, number of interactions, expertise, and upstream-model compute or error propagation.
Report oracle ground-truth-derived prompts separately from deployable human- or model-generated
prompts. An oracle box, centroid, or mask derived from the reference segmentation measures
conditional segmentation performance, not an autonomous or realistically prompted workflow.

## 2. Frozen encoder with linear or shallow probe

Use a linear probe to test whether the frozen representation makes task information accessible
without altering the backbone. Freeze the encoder in evaluation mode unless a prespecified
normalization update is the intervention being studied.

Specify the extracted layer, token or feature map, 2D-to-patient or patch-to-volume pooling,
normalization, probe family, regularization, imbalance handling, and tuning folds. Fit pooling
weights, feature selection, dimensionality reduction, and the probe inside training data. A deep
multilayer head is not a linear probe; label it a shallow-head adaptation and report its capacity.

Use the probe as both a scientific diagnostic and a baseline. Failure of one pooling rule or probe
does not prove the pretrained representation contains no useful information.

## 3. Partial fine-tuning

Use partial tuning when labeled data or compute do not support stable end-to-end optimization but a
frozen representation is insufficient. Candidate routes include:

- train the task head and last one or more encoder stages;
- unfreeze normalization parameters or biases;
- use discriminative learning rates with smaller updates in earlier layers;
- progressively unfreeze a prespecified sequence of blocks.

Define trainable blocks before viewing test results. Tune the number of unfrozen blocks within the
same development budget used for competing routes. Monitor training instability and representation
drift; retain the frozen probe as a comparator. Do not choose a favorable layer after repeated test
evaluation.

## 4. Full fine-tuning

Use full tuning only when the cohort size, label quality, domain diversity, compute, and repeated-run
budget support it. Pre-specify optimizer, layer-wise learning rates, weight decay, warm-up, schedule,
augmentation, precision, gradient accumulation, clipping, stopping, and checkpoint selection.

Protect against:

- overfitting to a small development cohort;
- catastrophic forgetting of transferable features;
- unstable results that depend on one seed;
- batch-normalization leakage across sites or test batches;
- silent resizing or channel conversion that removes clinically relevant information.

Compare with the frozen probe and at least one parameter-efficient or partial route when feasible.
If full tuning wins only after more searches or compute, report both the performance and resource
asymmetry.

## 5. Adapters

Adapters insert small trainable modules while retaining most backbone weights. State:

- adapter architecture, width or bottleneck, placement, activation, and residual route;
- whether normalization, biases, task head, or backbone parameters also train;
- per-task or per-site adapter ownership and how inference selects one;
- added parameters, memory, latency, and whether adapters can be distributed under the licenses.

Adapters are useful for modular multi-task or multi-site systems, but separate adapters do not prove
site robustness or personalization. Compare common versus site-specific adapters on held-out sites
and report how an unseen site is handled.

## 6. LoRA and related parameter-efficient updates

For LoRA, specify target modules, rank, scaling, dropout, initialization, trained biases or
normalization, and whether updates are kept separate or merged into the checkpoint. Report
trainable parameters and actual optimizer-state and activation-memory use; a small parameter count
does not guarantee a small training footprint.

Use rank and target-module choices selected inside development data. Include a rank sensitivity
analysis when the main claim depends on efficiency. Preserve the base-checkpoint hash and LoRA
delta hash. If weights are merged, document the merge procedure and resulting checkpoint hash.

Treat other low-rank, bias-only, or selective-update methods under the same rules: name the exact
trainable tensors, not only the umbrella term “parameter-efficient fine-tuning.”

## 7. Prompt learning

Prompt learning may optimize textual prompt embeddings, context tokens, visual prompts, or
multimodal tokens while freezing most or all model weights. It is appropriate only when the
architecture consumes such prompts meaningfully.

Specify prompt type, length, initialization, placement, class-specific versus shared context,
number of prompt candidates, regularization, and ensemble rule. Prevent patient labels, report
conclusions, or downstream outcomes from entering inference prompts unless they are legitimately
available at prediction time. Compare learned prompts with fixed clinically sensible prompts and
evaluate wording, label, and site sensitivity.

Prompt tuning is supervised adaptation when labels optimize prompt parameters; do not present it as
zero-shot evaluation.

## 8. Continued self-supervised or domain-adaptive pretraining

Use continued pretraining when authorized unlabeled in-domain images or image-text pairs may improve
the foundation representation before supervised downstream adaptation. Distinguish it from training
a foundation model from scratch and from ordinary downstream fine-tuning.

Pre-specify:

- the authorized unlabeled corpus, patient/site/date coverage, deduplication, and relation to every
  downstream development and evaluation cohort;
- the self-supervised or domain-adaptive objective, sampling, augmentations, masking or contrastive
  scheme, number of steps, stopping rule, and checkpoint-selection signal;
- whether text, metadata, pseudo-labels, or reports enter the objective and whether they expose the
  downstream target;
- the target-development boundary: continued pretraining may use only the unlabeled data authorized
  for development, never the frozen test or external cohort whose independence is being claimed;
- hardware, memory, trials, wall time, accelerator-hours, energy/carbon method, and checkpoint
  hashes before and after continued pretraining.

Always compare with the same initial checkpoint **directly fine-tuned on the downstream task**
without continued pretraining. Match downstream architecture, labels, splits, tuning policy, and
evaluation; report both the controlled comparison and total compute. Add a frozen probe when the
scientific question concerns representation quality.

Test for catastrophic forgetting and negative transfer: retain at least one prespecified source-like
or broad-capability task when relevant, report performance before and after continued pretraining,
and do not select the continued-pretraining checkpoint on the frozen downstream test. Improvement
on one in-domain task does not establish broader foundation-model quality.

## 9. Domain adaptation

Define the source and target domains, shift mechanism, available target information, and deployment
setting before choosing a method. Distinguish:

- **unsupervised domain adaptation:** unlabeled target-development inputs are available;
- **semi-supervised domain adaptation:** some target-development labels are available;
- **supervised transfer:** labeled target data drive ordinary adaptation;
- **domain generalization:** no target-domain data are used during fitting;
- **test-time adaptation:** model parameters or statistics update after deployment inputs arrive.

Possible routes include fixed normalization, importance weighting, feature alignment, adversarial
alignment, self-training/pseudo-labeling, style augmentation, or target-aware adapters. Fit and
tune them using authorized target-development data only. Never adapt on the frozen target test set
and then call its evaluation untouched or external.

Report negative transfer, target-label use, pseudo-label confidence and failure, class-prevalence
shift, and performance before and after adaptation. For test-time adaptation, define whether
updates occur per case or stream, whether batches mix patients, rollback behavior, and the
appropriate prospective or replay evaluation.

## Selecting a route

Choose using this sequence:

1. Is the pretrained interface valid for the task? If yes, run a locked zero-shot evaluation.
2. Are fixed representations sufficient for the estimand? Establish this with a linear or shallow
   probe.
3. Does performance improve reproducibly when late blocks or small parameter-efficient components
   train? Prefer the simplest route meeting the prespecified criterion.
4. Is full tuning supported by enough diverse data and repeated-run compute, and does it improve on
   fair baselines? If not, retain the simpler route.
5. Is authorized unlabeled in-domain data available and is representation adaptation itself
   testable? Compare continued pretraining with direct downstream fine-tuning.
6. Is source-target shift itself part of the question? Add domain adaptation as a distinct,
   leakage-controlled comparison rather than silently using target data.

Do not rank strategies from a single winning seed. Report performance, calibration,
transportability, parameter count, runtime, memory, and uncertainty together.
