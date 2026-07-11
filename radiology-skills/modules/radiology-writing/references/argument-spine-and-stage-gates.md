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

| Phase | Radiology-specific question | Output |
|---|---|---|
| Problem discovery | Which patient, radiologist, oncologist, workflow, or biological question suffers now? | clinical stakes + failure mode |
| Contribution crystallization | What exactly does this paper add: diagnostic, prognostic, biological, workflow, dataset, method, or implementation value? | one-sentence contribution + boundary |
| Evidence design | Which cohort, metric, reader study, calibration, DCA, survival, omics, or external validation proves the contribution? | results-as-validation map |
| Positioning | Which prior imaging papers will reviewers compare against, and what assumption or limitation do they leave open? | comparator table + positioning sentence |
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

If the contribution cannot pass this gate, route to `radiology-design`, `radiology-stats`, or `radiology-reporting` before writing.

## Results-as-validation gate

Every Results subsection should validate a promise made by the Introduction/Methods.

| Promise | Result/Figure/Table | Metric/CI or evidence | Boundary | Status |
|---|---|---|---|---|
| Clinical discrimination | Figure 2 ROC / Table 2 | AUC with 95% CI | External cohort absent | Supported / needs input |
| Calibration/reliability | Figure 3 calibration | Slope, intercept, Brier if available | Bootstrap only | Supported / needs input |
| Clinical utility | Figure 4 DCA | Threshold range, net benefit | Decision threshold not prespecified | Supported / needs input |
| Biological plausibility | Figure 5 radiogenomics | Association, adjusted model, FDR | Observational | Supported / needs input |

If a result does not validate a paper-level promise, either remove it, demote it to supplement, or revise the promise.

## Introduction twice

1. **Draft 0 Introduction**: before full drafting, write a sparse argument skeleton:
   - clinical stakes
   - known limitation of current imaging/workflow
   - methodological or translational gap
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

1. **Contribution gate passed**: exact clinical/methodological contribution is explicit and bounded.
2. **Results gate passed**: every major claim maps to a result, figure, or table.
3. **Citation gate passed**: important background, novelty, and comparison claims have verified support.
4. **Figure gate passed**: figure messages match the manuscript claims.
5. **Reporting gate passed**: correct checklist stack has no unresolved material item.
6. **Fresh-reader gate passed**: a reviewer who did not draft the section can state the contribution, evidence, boundary, and next action after one read.

If any gate fails, route back to the responsible skill rather than polishing around the gap.
