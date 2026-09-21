# Radiomics–Mechanism Bridge Canvas

Use this canvas when an imaging phenotype is connected to tissue, cellular, molecular, functional,
or clinical meaning. The bridge must show what was measured, what was inferred, and what remains
only proposed. Feature names, saliency maps, embeddings, and habitats do not carry intrinsic
biological meaning.

## 1. Anchor the imaging phenotype

| Field | Entry |
|---|---|
| Disease and clinical context | [AUTHOR_INPUT_NEEDED: context] |
| Imaging modality and acquisition | [AUTHOR_INPUT_NEEDED: modality, sequence/tracer, phase, protocol] |
| Segmentation or region definition | [AUTHOR_INPUT_NEEDED: ROI/habitat definition and blinding] |
| Phenotype definition | [AUTHOR_INPUT_NEEDED: feature, embedding, saliency region, habitat, or longitudinal change] |
| Phenotype direction and uncertainty | [AUTHOR_INPUT_NEEDED: observed direction, effect size/interval if available] |
| Imaging QC and stability evidence | [AUTHOR_INPUT_NEEDED: repeatability, segmentation robustness, site/scanner sensitivity] |
| Imaging analysis n | [AUTHOR_INPUT_NEEDED: patients, lesions, regions] |
| Biological linkage matched n | [AUTHOR_INPUT_NEEDED: same-patient/lesion/region/time n] |
| Primary inferential unit | [AUTHOR_INPUT_NEEDED: unit] |

## 2. Mapping and provenance

| Dimension | Entry | Compatibility |
|---|---|---|
| Patient identity | [AUTHOR_INPUT_NEEDED: matching method] | [AUTHOR_INPUT_NEEDED: aligned / partial / not aligned / unknown] |
| Lesion identity | [AUTHOR_INPUT_NEEDED: mapping] | [AUTHOR_INPUT_NEEDED: aligned / partial / not aligned / unknown] |
| Region/habitat ↔ tissue block/section | [AUTHOR_INPUT_NEEDED: mapping and registration] | [AUTHOR_INPUT_NEEDED: aligned / partial / not aligned / unknown] |
| Imaging-to-sampling interval | [AUTHOR_INPUT_NEEDED: interval] | [AUTHOR_INPUT_NEEDED: aligned / partial / not aligned / unknown] |
| Intervening treatment | [AUTHOR_INPUT_NEEDED: treatment/exposure] | [AUTHOR_INPUT_NEEDED: aligned / partial / not aligned / unknown] |
| Repeated observations | [AUTHOR_INPUT_NEEDED: patient-lesion-block-section-cell/spot hierarchy] | [AUTHOR_INPUT_NEEDED: handled / not handled / unknown] |

## 3. Cross-scale bridge

Characterize every layer with three independent fields: **Primary evidence state** records how the
evidence was produced (`measured`, `derived`, `estimated`, `associated`, `predicted`, or `perturbed`);
**Modality subtype** records the assay or operation-specific form; and **Claim-link
status** records whether that item supports the proposed bridge `direct`, `inferred`, or `proposed`.
For a proposed future observation, use `missing` only as an absence marker in the state field and set
claim-link status to `proposed`; `missing` is not a seventh positive state. Never encode an inferred
link as a measurement state.

| Layer | Candidate observation/process | Primary evidence state | Modality subtype | Claim-link status | Evidence pointer | Unit and matched n | Main uncertainty |
|---|---|---|---|---|---|---|---|
| Image acquisition/physics | [AUTHOR_INPUT_NEEDED: acquisition or physical contributor] | [AUTHOR_INPUT_NEEDED: measured / derived / estimated / associated / predicted / perturbed; use missing only as an absence marker] | [AUTHOR_INPUT_NEEDED: sequence, tracer, phase, reconstruction, physical model, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: unit and n] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Image phenotype | [AUTHOR_INPUT_NEEDED: phenotype] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: handcrafted feature, embedding, saliency, habitat, longitudinal delta, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: unit and n] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Tissue architecture/process | [AUTHOR_INPUT_NEEDED: process] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: H&E, IHC, mIF, WSI-derived, spatial morphology, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: unit and n] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Cell source/state | [AUTHOR_INPUT_NEEDED: source/state] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: scRNA-seq, snRNA-seq, deconvolution, cytometry, lineage assay, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: unit and n] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Molecular programme | [AUTHOR_INPUT_NEEDED: pathway/programme] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: bulk RNA, gene set score, regulon, proteomics, metabolomics, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: unit and n] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Functional/perturbational response | [AUTHOR_INPUT_NEEDED: response] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: genetic perturbation, drug perturbation, organoid, animal model, longitudinal response, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: unit and n] | [AUTHOR_INPUT_NEEDED: uncertainty] |
| Clinical state/endpoint | [AUTHOR_INPUT_NEEDED: state/endpoint] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: diagnosis, response, survival, toxicity, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] | [AUTHOR_INPUT_NEEDED: pointer] | [AUTHOR_INPUT_NEEDED: unit and n] | [AUTHOR_INPUT_NEEDED: uncertainty] |

## 4. Competing hypothesis portfolio

At minimum include two biologically distinct explanations and one technical, sampling, or mapping
explanation. Do not rank them solely by narrative plausibility.

| Hypothesis | Type | Mechanistic chain | Prediction if true | Observation that discriminates it | Falsification condition | Primary evidence state | Modality subtype | Claim-link status |
|---|---|---|---|---|---|---|---|---|
| H1 | biological | [AUTHOR_INPUT_NEEDED: chain] | [AUTHOR_INPUT_NEEDED: prediction] | [AUTHOR_INPUT_NEEDED: test/observation] | [AUTHOR_INPUT_NEEDED: condition] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: assay or operation subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] |
| H2 | biologically distinct | [AUTHOR_INPUT_NEEDED: chain] | [AUTHOR_INPUT_NEEDED: prediction] | [AUTHOR_INPUT_NEEDED: test/observation] | [AUTHOR_INPUT_NEEDED: condition] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: assay or operation subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] |
| H3 | technical / sampling / mapping | [AUTHOR_INPUT_NEEDED: chain] | [AUTHOR_INPUT_NEEDED: prediction] | [AUTHOR_INPUT_NEEDED: negative control or sensitivity analysis] | [AUTHOR_INPUT_NEEDED: condition] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: QC, sensitivity analysis, negative control, or other subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] |
| Additional hypothesis | [AUTHOR_INPUT_NEEDED: type] | [AUTHOR_INPUT_NEEDED: chain] | [AUTHOR_INPUT_NEEDED: prediction] | [AUTHOR_INPUT_NEEDED: test/observation] | [AUTHOR_INPUT_NEEDED: condition] | [AUTHOR_INPUT_NEEDED: primary evidence state] | [AUTHOR_INPUT_NEEDED: assay or operation subtype] | [AUTHOR_INPUT_NEEDED: direct / inferred / proposed] |

## 5. Constraint ledger

| Constraint | Could mimic or break which link? | Planned check | Result/status | Consequence |
|---|---|---|---|---|
| Scanner/site/protocol | [AUTHOR_INPUT_NEEDED: link] | [AUTHOR_INPUT_NEEDED: check] | [AUTHOR_INPUT_NEEDED: result or not measured] | [AUTHOR_INPUT_NEEDED: consequence] |
| Tumour/lesion volume | [AUTHOR_INPUT_NEEDED: link] | [AUTHOR_INPUT_NEEDED: check] | [AUTHOR_INPUT_NEEDED: result or not measured] | [AUTHOR_INPUT_NEEDED: consequence] |
| Segmentation/registration | [AUTHOR_INPUT_NEEDED: link] | [AUTHOR_INPUT_NEEDED: check] | [AUTHOR_INPUT_NEEDED: result or not measured] | [AUTHOR_INPUT_NEEDED: consequence] |
| Tissue sampling/purity | [AUTHOR_INPUT_NEEDED: link] | [AUTHOR_INPUT_NEEDED: check] | [AUTHOR_INPUT_NEEDED: result or not measured] | [AUTHOR_INPUT_NEEDED: consequence] |
| Omics/pathology batch | [AUTHOR_INPUT_NEEDED: link] | [AUTHOR_INPUT_NEEDED: check] | [AUTHOR_INPUT_NEEDED: result or not measured] | [AUTHOR_INPUT_NEEDED: consequence] |
| Timing/treatment | [AUTHOR_INPUT_NEEDED: link] | [AUTHOR_INPUT_NEEDED: check] | [AUTHOR_INPUT_NEEDED: result or not measured] | [AUTHOR_INPUT_NEEDED: consequence] |
| Repeated units/pseudoreplication | [AUTHOR_INPUT_NEEDED: link] | [AUTHOR_INPUT_NEEDED: check] | [AUTHOR_INPUT_NEEDED: result or not measured] | [AUTHOR_INPUT_NEEDED: consequence] |

## 6. Validation ladder

| Tier | Question resolved | Required data/assay | Inferential unit and minimum matched structure | Discriminating control | Feasibility | Claim ceiling if completed |
|---|---|---|---|---|---|---|
| Minimum viable | [AUTHOR_INPUT_NEEDED: question] | [AUTHOR_INPUT_NEEDED: data/assay] | [AUTHOR_INPUT_NEEDED: unit and matching] | [AUTHOR_INPUT_NEEDED: control] | [AUTHOR_INPUT_NEEDED: feasibility] | [AUTHOR_INPUT_NEEDED: ceiling] |
| Standard | [AUTHOR_INPUT_NEEDED: question] | [AUTHOR_INPUT_NEEDED: data/assay] | [AUTHOR_INPUT_NEEDED: unit and matching] | [AUTHOR_INPUT_NEEDED: control] | [AUTHOR_INPUT_NEEDED: feasibility] | [AUTHOR_INPUT_NEEDED: ceiling] |
| Mechanism-advancing | [AUTHOR_INPUT_NEEDED: question] | [AUTHOR_INPUT_NEEDED: data/assay] | [AUTHOR_INPUT_NEEDED: unit and matching] | [AUTHOR_INPUT_NEEDED: control/perturbation] | [AUTHOR_INPUT_NEEDED: feasibility] | [AUTHOR_INPUT_NEEDED: ceiling] |

## 7. Bridge judgement and writing ceiling

| Field | Entry |
|---|---|
| Issue severity, if auditing | [AUTHOR_INPUT_NEEDED: P0 / P1 / P2; classify impact only, not evidence sufficiency] |
| Bridge gate verdict | [AUTHOR_INPUT_NEEDED: PASS / CONDITIONAL / STOP; judge evidence sufficiency only] |
| Weakest link | [AUTHOR_INPUT_NEEDED: link and reason] |
| Strongest measured link | [AUTHOR_INPUT_NEEDED: link and evidence] |
| Claim ceiling | [AUTHOR_INPUT_NEEDED: strongest defensible wording] |
| Wording to avoid | [AUTHOR_INPUT_NEEDED: unsupported mechanism or causal wording] |
| Results wording | [AUTHOR_INPUT_NEEDED: observation-first, evidence-bounded sentence] |
| Discussion wording | [AUTHOR_INPUT_NEEDED: interpretation plus alternative and limitation] |
| Claim-changing stop condition | [AUTHOR_INPUT_NEEDED: condition] |

## 8. STOP rescue, if required

| Rescue element | Entry |
|---|---|
| Blocked mechanism claim | [AUTHOR_INPUT_NEEDED: claim] |
| Broken bridge link | [AUTHOR_INPUT_NEEDED: link] |
| Nearest answerable association or concordance question | [AUTHOR_INPUT_NEEDED: question] |
| Minimum new evidence needed | [AUTHOR_INPUT_NEEDED: evidence] |
| Wording currently allowed | [AUTHOR_INPUT_NEEDED: wording] |
