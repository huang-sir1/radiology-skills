# Transcriptomics literature evidence map, 2024–2026

Use this index to understand how the screened literature changes the skill. Do not load all 100
rows for an ordinary question. Open the relevant modality playbook first, then inspect only the
evidence rows cited by its execution card when provenance, limitations or manuscript citations are
needed.

For an imaging–mechanism question, first use
[radiomics-mechanism-bridge.md](radiomics-mechanism-bridge.md) to decide which biological uncertainty
bulk, single-cell or spatial evidence is meant to resolve. The corpus supports the assay-specific
link; it does not by itself establish that a molecular process generated the radiomic phenotype.

## Corpus contract

| Modality | Articles | Research guidance | Row-level evidence map |
|---|---:|---|---|
| Bulk RNA | 33 | [bulk-rna-research-guidance.md](bulk-rna-research-guidance.md) | [bulk-rna-literature-map-2024-2026.tsv](bulk-rna-literature-map-2024-2026.tsv) |
| scRNA/snRNA | 34 | [single-cell-research-guidance.md](single-cell-research-guidance.md) | [single-cell-literature-map-2024-2026.tsv](single-cell-literature-map-2024-2026.tsv) |
| Spatial transcriptomics | 33 | [spatial-transcriptomics-research-guidance.md](spatial-transcriptomics-research-guidance.md) | [spatial-transcriptomics-literature-map-2024-2026.tsv](spatial-transcriptomics-literature-map-2024-2026.tsv) |
| **Total** | **100** | stage-gated, modality-specific guidance | auditable unique DOI/PMID rows |

The inclusion contract is:

- formal publication date from 2024-08-21 through 2026-08-21;
- Nature Portfolio and Cell Press prioritized; another field-leading journal is eligible only when
  its screening-date latest verifiable JIF is at least 10;
- article content must change a decision, constraint, review check, interpretation boundary,
  repair action or writing requirement;
- DOI, PMID, article type and publication date are checked; preprints, corrections, duplicates,
  generic descriptive papers and prestige-only inclusions are excluded;
- method and benchmark evidence is interpreted within its tested tissue, platform, endpoint and
  validation domain rather than converted into a universal winner.

## What the 100 articles concretely add

### Bulk RNA: from count matrix provenance to clinical use

The 33 articles contribute five linked evidence groups:

1. **What was measured:** raw-read discovery, reference choice, assembly QC, targeted panels,
   absolute calibration, long-read isoforms, allele-specific expression and splicing events.
2. **Whether the contrast is estimable:** pre-analytic tissue artifacts, biological replication,
   small-count/complex-design inference, effect-size thresholds and multiplicity.
3. **Whether mixture creates the signal:** transcriptome-size bias, batch/reference shift,
   community deconvolution benchmarks, incomplete references, tumour cell states and uncertainty.
4. **Whether programs and signatures transfer:** co-expression versus regulation, stress programs,
   RNA-to-protein prediction, public perturbation resources, subtype consensus and cohort reuse.
5. **Whether a clinical or multimodal claim is justified:** targeted diagnostic utility,
   prognostic versus treatment-predictive interaction, assay translation, radiotranscriptomic
   incremental value and independent validation.

These contents require the skill to review feature generation before DE, composition before cell-
specific interpretation, and trial/validation design before clinical wording.

### scRNA/snRNA: from data layers to generalizable perturbation claims

The 34 articles contribute six evidence groups:

1. **Measurement and preprocessing:** chemistry/platform trade-offs, doublets, lncRNA-sensitive
   processing, feature selection, nascent/mature RNA and data-layer permissions.
2. **Integration and annotation:** biology preservation, multi-omics integration, reference models,
   unseen populations, consensus/LLM annotation, metacell rigor and uncertainty.
3. **Cohort inference:** patient-level heterogeneity, weak disease labels, malignant-cell evidence,
   RNA-derived CNV limits, sample-aware abundance and pseudobulk differential expression.
4. **Dynamics:** pseudotime differential programs, transient events, transcriptional kinetics,
   multi-omic velocity and lineage-tracing-constrained maps.
5. **Mechanistic hypotheses:** gene-regulatory networks, causal-network inference and two forms of
   cell-cell communication evidence without equating expression compatibility to signaling.
6. **Perturbation and foundation models:** observed Perturb-seq effects, heterogeneous responses,
   pathway signatures, unseen-context prediction, simple baselines, evaluation metrics, scaling,
   model reuse and drug-response transfer.

These contents require the skill to separate cells from donors, embeddings from count inference,
weak labels from cell truth, observed perturbations from predictions, and interpolation from OOD
generalization.

### Spatial transcriptomics: from tissue coordinates to spatially bounded claims

The 33 articles contribute seven evidence groups:

1. **Platform and reproducibility:** cross-platform benchmarks, effective resolution, targeted versus
   whole-transcriptome coverage, sensitivity/specificity and cross-site concordance.
2. **Spatial QC and cellularization:** local artifacts, segmentation, segmentation-free analysis,
   transcript assignment, reconstruction and downstream error propagation.
3. **Spatial estimands:** overall and cell-type-specific spatially variable genes, domains, gradients,
   subcellular localization, spatial nulls and multiplicity.
4. **Integration and mapping:** fine-grained deconvolution, multi-sample/multi-source integration,
   interpretable or foundation-model representations and scRNA-to-space mapping.
5. **Niches and communication:** neighbourhood enrichment, ligand-receptor dynamics, relay networks,
   clone neighbourhoods and the boundary between compatibility and functional signaling.
6. **Generated spatial layers:** expression imputation, histology-associated gradients,
   histology-foundation models, super-resolution and the requirement for held-out measured spatial
   validation.
7. **Space through depth and time:** multi-slice and 3D reconstruction, spatial velocity,
   spatiotemporal trajectories, perturbation, lineage, RNA-derived CNA, clone phylogeography,
   developmental/cross-species atlases and radiology/pathology registration.

These contents require the skill to define the spatial estimand before choosing an algorithm,
propagate segmentation/registration uncertainty, and label every deconvolved, mapped, imputed or
virtual layer as inferred.

## Evidence-to-guidance conversion

Every TSV row records this chain:

```text
concrete_content -> decision_changed -> constraints -> skill_action -> writing_requirement
```

- `concrete_content` states what the paper actually studied or benchmarked.
- `decision_changed` states which research choice changes because of that evidence.
- `constraints` prevents transfer beyond the paper's tissue, platform, design or validation domain.
- `skill_action` tells the skill what to expand, review, explain, judge or help repair.
- `writing_requirement` carries the same boundary into Methods, Results, legends or Discussion.

The remaining fields preserve modality, theme, title, formal date, journal, DOI, PMID, evidence
type and JIF provenance. JIF is an eligibility gate, not an evidence-strength score.

## How to use the evidence map

1. Route to the applicable execution card in the modality playbook.
2. Open only its cited evidence IDs in the companion TSV.
3. Use the paper's `concrete_content` and `constraints` to test transfer to the user's data.
4. Apply the card's decision rule and issue `PASS`, `CONDITIONAL` or `STOP`.
5. Produce the repair or writing artifact requested by the user.
6. Cite the primary paper for a manuscript claim; do not cite this internal map as scientific
   evidence and do not cite all 100 papers indiscriminately.

## Deterministic audit

Run from the skill directory or repository root:

```powershell
& scripts/audit_transcriptomics_literature_maps.ps1 -VerifyPubMed
```

The audit requires 33 + 34 + 33 rows, the full field contract, unique IDs/DOIs/PMIDs, dates inside
the declared window, recorded JIF values of at least 10, HTTPS metric sources, resolvable PubMed IDs
and DOI agreement between each row and PubMed.

## Boundaries of the corpus

- This is a deliberately selective recent high-impact corpus, not a systematic review of every
  valid transcriptomics method.
- Journal impact is a screening constraint requested by the user; it does not replace study-design,
  benchmark-domain or evidence-strength appraisal.
- A newer metric release can change journal eligibility. Preserve the recorded JIF year/source and
  re-audit before extending the publication window.
- The maps guide scientific decisions; they do not establish that a method will work on a new
  dataset without task-matched diagnostics, baselines and validation.
