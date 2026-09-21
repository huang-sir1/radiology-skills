# Mechanism-only reviewer and revision playbook

Use this for manuscript review, rebuttal and frozen-yardstick revision verification when the evidence
comes from bulk RNA, single-cell or single-nucleus assays, spatial transcriptomics, pathology, other
omics or perturbation experiments without an imaging claim. Do not request radiology acquisition,
segmentation, radiomics features, scanner harmonisation or sample-to-image mapping.

## Reviewer domains

| Domain | Questions that must be resolved | Minimum repair when weak |
|---|---|---|
| Question and system | Biological contrast, model system, context and claim ceiling explicit? | Rewrite objective and causal diagram |
| Units and replication | Donors, patients, specimens, regions, cells and technical observations separated? | Reanalyse at biological-unit level |
| Sampling | Timing, treatment, tissue/region selection and attrition documented? | Flow and sampling table |
| Assay validity | Preanalytics, platform QC, filtering, normalization and reference versions reported? | Complete assay-specific QC |
| Batch and composition | Condition separable from batch and cell/tissue composition? | Balanced/sensitivity analysis |
| Statistics | Estimand, multiplicity, uncertainty and nested structure handled? | Prespecified contrasts and hierarchical model |
| Evidence state | Measured, derived, estimated, predicted and perturbed layers distinguished? | Correct evidence ledger and wording |
| Validation | Independent, orthogonal or perturbational evidence appropriate to the claim? | Add feasible validation or lower claim |
| Alternative mechanisms | At least one competing explanation tested or bounded? | Add discriminating analysis/experiment |
| Reproducibility | Accession, metadata, code, environments and full results available as allowed? | Complete provenance package |

Load the active modality playbook for its detailed QC. For causal or perturbation claims, also use
`perturbation-causal-review.md`; inferred regulons, ligand-receptor scores, pseudotime, deconvolution,
virtual knockout or generated cell states do not by themselves constitute experimental perturbation.

## Claim boundaries

- Differential abundance or expression supports a condition-associated difference, not a mechanism.
- Pathway enrichment and network inference nominate explanations but do not identify a unique causal
  chain.
- Cell-level observations do not replace donor-level replication.
- Spatial co-localization supports localization or concordance, not molecular causation.
- Perturbation supports a causal contrast only when assignment, efficiency, target engagement,
  specificity, controls, dose-time order and replication are adequate.

## Reviewer output

Use the atomic contract in `constructive-manuscript-review-chain.md`:
`Finding ID | class | review dimension/lens | P0/P1/P2 | obligation | typed evidence anchor |
observed problem | governing criterion | why it matters | claim consequence | minimum feasible remedy |
optional stronger route | cost/trade-off | closure evidence | confidence/scope limit`. For each
mechanistic statement, identify the strongest directly supported
link, the missing link and the most plausible rival explanation. Offer conservative, standard and
advanced repair paths when the user seeks guidance, but label optional experiments separately from
defects in the current work.

## Revision verification

Freeze the original finding IDs and evaluation criteria. Compare the response letter, revised text,
figures, supplement and analysis outputs. Use VERIFIED, PARTIAL, NOT ADDRESSED, MADE WORSE or
NOT VERIFIABLE.
Verify sample counts, effect directions, evidence-state labels and causal verbs across all locations.
Do not invent an imaging requirement during verification or turn a proposed future imaging study into
a condition for accepting a mechanism-only manuscript.

## Rebuttal wording

When a reviewer requests an absent modality, determine whether it is required to support the actual
claim. If not, explain the scope, add a bounded limitation and describe the request as future work. If
the evidence gap is real, give the smallest assay, control, reanalysis or claim reduction that closes
it. Every claimed change must include the method, result, exact location and residual limitation.
