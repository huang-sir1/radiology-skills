# Argument spine and manuscript stage gates

Use this reference when a manuscript needs more than sentence-level drafting: full paper rebuild, rejected-paper rescue, Nature/Radiology submission, unclear contribution, or a paper whose figures/results exist but whose story feels loose.

## Required working artifacts

Create or update these lightweight artifacts before drafting long prose:

| Artifact | Purpose |
|---|---|
| `project-context.md` | One-page memory of the study: clinical problem, population, modality, endpoint, cohort, validation, target venue, reporting stack, available figures/tables, and missing inputs |
| `confirmed-contribution.md` | The exact contribution the paper is allowed to claim, with evidence and boundaries |
| `results-validation.md` | Map from promised contribution to the result/figure/table that validates it |
| `writing-rationale-matrix.md` | Why each section/paragraph exists and what evidence it uses |

These files can be created in a user-selected working folder. If no folder is provided, return them as tables in the response.

## Structured brainstorming gate

Use this gate when the paper idea is still fuzzy, the Introduction sounds generic, or the user has results but cannot state why the paper matters. Walk through these six phases before drafting:

| Phase | Project question | Output |
|---|---|---|
| Problem discovery | Which patient, radiologist, oncologist, workflow, or biological question suffers now? | clinical stakes + failure mode |
| Contribution crystallization | What exactly does this paper add: diagnostic, prognostic, biological, workflow, dataset, method, or implementation value? | one-sentence contribution + boundary |
| Evidence design | Which cohort, metric, reader study, calibration, DCA, survival, omics, or external validation proves the contribution? | results-as-validation map |
| Positioning | Which prior imaging, assay or mechanism papers will reviewers compare against, and what assumption or limitation do they leave open? | comparator table + positioning sentence |
| Architecture and constraints | Which decisions are fixed: modality, ROI, endpoint, model, split, feature pipeline, omics layer, threshold, or clinical action? | locked decisions + open questions |
| Narrative spine | What is the shortest story from clinical need to evidence-backed conclusion? | title logic + abstract closing claim |

Do not accept vague answers such as "better model" or "more accurate." Translate them into who benefits, what decision changes, and what evidence proves it.

## Contribution-first gate

Do not write the final Introduction or Discussion until this gate is explicit:

```text
In [population/setting], using [modality/data type], we show [clinical/methodological advance],
validated by [cohort/metric/CI/comparison], with the boundary that [limitation].
```

For radiology studies, the contribution must include:

- **Clinical problem**: diagnosis, prognosis, treatment response, workflow, or biological insight.
- **Imaging asset**: CT/MRI/PET/US/mammography/pathology slide/multimodal input.
- **Method**: radiomics, deep learning, radiogenomics, reader study, conventional model, or hybrid.
- **Validation**: internal, temporal, external, multicenter, prospective, reader comparison, or biological validation.
- **Claim boundary**: retrospective, single center, enrichment, event count, scanner/protocol limits, or missing prospective/reader evidence.

For mechanism-only studies, replace the imaging checklist with:

- **Biological question/system**: disease state, tissue, cell population or perturbation context.
- **Assay and evidence role**: active bulk RNA, sc/snRNA, spatial, pathology or perturbation evidence;
  external/generated/proposed layers stay explicitly separate.
- **Independent unit/hierarchy**: donor/patient/specimen/section/cell-or-spot nesting and matched n.
- **Validation**: orthogonal assay, independent cohort, spatial localization, perturbation or other
  evidence actually performed—not an imagined imaging/clinical requirement.
- **Claim boundary**: descriptive/association/localization/mechanistic/causal ceiling inherited from
  the validated scientific handoff packet.

If the contribution cannot pass this gate, route imaging design gaps to `radiology-design`/
`radiology-stats` and mechanism truth gaps to `radiology-radiogenomics`; route reporting gaps to
`radiology-reporting` before writing.

## Incremental work → defensible claim menu

Most accepted imaging papers are not "first." When the study is finished and the method is
not new, the contribution is usually one of five legitimate non-novelty claims. Pick **one**
primary claim and at most one supporting claim, and verify the claim is still open with a
live literature check (→ `radiology-search`) before writing it anywhere.

| Claim type | Positioning sentence (use) | Overclaim reviewers will reject (avoid) |
|---|---|---|
| **Largest / most representative cohort** | "In the largest reported cohort of [population] imaged with [modality] (n = X, from [setting]), we establish [estimate with 95% CI] for [task] — the most precise estimate to date." | "This is the first and definitive study of [task]." (unverifiable; invites a counterexample) |
| **First multi-vendor / multi-centre external validation** | "We provide the first external validation of [model/approach] across [N] centres and [M] scanner vendors, with calibration reported per site." | "Our model generalises to all clinical settings." (the sites shown are not all settings) |
| **Strongest validation design** | "Where prior [task] studies relied on internal cross-validation, we evaluate [model] with [temporal/geographic validation + calibration + decision-curve analysis], the most rigorous assessment of [task] to date." | "Prior studies of [task] are invalid." (they answered different questions; disrespect draws fire) |
| **Methodological improvement** | "We introduce [specific change — e.g. a leakage-safe patient-level pipeline / harmonisation protocol / IBSI-compliant reproducibility package], which [measurable effect: removes X points of optimism / enables exact replication]." | "A novel framework that revolutionises [task]." (an increment is not a revolution) |
| **Data / resource contribution** | "We release [annotated cohort / benchmark / annotation SOP] (n = X, with [labels]), enabling reproducible comparison for [task]; as a reference baseline, [model] achieves [metric with 95% CI]." | "Our dataset is the new standard for [task]." (adoption makes standards, not authors) |

Rules:

- The claim must still pass the contribution-first gate above — cohort size and validation
  strength count only when the manuscript's tables and figures prove them.
- "Largest" and "first external validation" are literature claims and they expire: verify
  live at writing time and again at revision time. A counterexample found by a reviewer is
  costlier than a smaller honest claim.
- Place the positioning sentence in the Introduction's final paragraph; echo it, bounded,
  in the Discussion context paragraph and the cover letter. One claim repeated consistently
  beats three claims competing with each other.
- If none of the five survives an honest check, the problem is design, not prose — route
  back to `radiology-design` / `radiology-frontier` rather than inflating the writing.

## Results-as-validation gate

Every Results subsection should validate a promise made by the Introduction/Methods.

| Promise | Result/Figure/Table | Metric/CI or evidence | Boundary | Status |
|---|---|---|---|---|
| Clinical discrimination | Figure 2 ROC / Table 2 | AUC with 95% CI | External cohort absent | Supported / needs input |
| Calibration/reliability | Figure 3 calibration | Slope, intercept, Brier if available | Bootstrap only | Supported / needs input |
| Clinical utility | Figure 4 DCA | Threshold range, net benefit | Decision threshold not prespecified | Supported / needs input |
| Method superiority | Benchmark table/figure | paired difference with uncertainty under matched cases/splits/preprocessing and fair tuning budget | unmatched implementation or compute | Supported / needs input |
| Component contribution | Ablation table | prespecified component/modality contrasts with patient/donor-level uncertainty | current pipeline/data only; not universal necessity | Supported / needs input |
| Parameter robustness | Sensitivity figure/Supplement | conclusion across justified values/ranges plus failure boundary | changing the estimand/object is a distinct analysis | Supported / needs input |
| Biological plausibility | Figure 5 radiogenomics | Association, adjusted model, FDR | Observational | Supported / needs input |
| Cell-state association | Figure 3 / Supplement | donor-aware effect, uncertainty, multiplicity | cells are nested; no causal claim | Supported / needs input |
| Spatial localization | Figure 4 | prespecified region/adjacency statistic and spatial null | section/spot coverage limits | Supported / needs input |
| Perturbation mechanism | Figure 5 | intervention, control, biological replication and actual readout | model-system transport | Supported / needs input |

If a result does not validate a paper-level promise, either remove it, demote it to supplement, or revise the promise.

## Introduction twice

1. **Draft 0 Introduction**: before full drafting, write a sparse argument skeleton:
   - clinical or biological stakes
   - known limitation of the current imaging/workflow/assay evidence
   - methodological, mechanistic or translational gap
   - objective/hypothesis
2. **Final Introduction**: after the figure plan and Results are stable, rewrite the last paragraph so it matches the actual evidence and target venue.

Never let an early aspirational Introduction survive unchanged after the results are known.

## Topic-sentence chain

Before filling paragraphs, write only the topic sentences for the target section. Read them in order as a miniature paper. They should form a coherent argument without the supporting details.

| Section | Topic sentence | What it advances | Evidence to insert | Risk |
|---|---|---|---|---|
| Introduction P1 | ... | clinical stakes | guideline / epidemiology | too broad |
| Introduction P2 | ... | current imaging gap | comparator studies | unfair novelty |
| Results P2 | ... | primary claim | Figure/Table + CI | unsupported metric |
| Discussion P1 | ... | meaning of findings | primary + validation results | overclaim |

If the topic sentences read like a list of topics rather than claims, rewrite before drafting prose.

## Paragraph job discipline

Before drafting each section, make a table:

| Paragraph | Job | Topic sentence | Evidence source | Risk |
|---|---|---|---|---|
| Intro 1 | Clinical stakes | ... | guideline / epidemiology citation | over-broad disease burden |
| Intro 2 | Gap | ... | prior imaging/radiomics studies | unfair novelty claim |
| Results 1 | Cohort | ... | Table 1 / flow diagram | missing dates/exclusions |
| Discussion 2 | Context | ... | verified citations | unsupported comparison |

Each paragraph should have one job. If a paragraph does two jobs, split it. If it has no job, delete or move it.

## Writing rationale matrix

Use this when a paper feels "well written but not convincing."

| Section | Claim being advanced | Evidence used | Reviewer risk | Needed fix |
|---|---|---|---|---|
| Abstract conclusion | ... | ... | overclaim / no CI / no external validation | soften or add boundary |
| Methods model | ... | ... | leakage / unclear split | route to radiology-radiomics/deep-learning |
| Discussion limitation | ... | ... | missing major limitation | add explicit limitation |

This matrix turns writing into an evidence audit, not prose decoration.

## Final stage gates

Before marking a manuscript draft as publication-ready:

1. **Contribution gate passed**: exact clinical, methodological or biological contribution is explicit and bounded.
2. **Results gate passed**: every major claim maps to a result, figure, or table.
3. **Citation gate passed**: important background, novelty, and comparison claims have verified support.
4. **Figure gate passed**: figure messages match the manuscript claims.
5. **Reporting gate passed**: correct checklist stack has no unresolved material item.
6. **Fresh-reader gate passed**: a reviewer who did not draft the section can state the contribution, evidence, boundary, and next action after one read.

If any gate fails, route back to the responsible skill rather than polishing around the gap.
