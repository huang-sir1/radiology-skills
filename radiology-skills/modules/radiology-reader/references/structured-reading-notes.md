# Structured reading notes

Use this reference when reading papers for more than translation: literature review, journal club, paper comparison, gap discovery, or writing-style extraction.

## Reading depth

| Pass | Goal | Output |
|---|---|---|
| Pass 1 | Decide relevance | one-paragraph note, paper type, modality, cohort, endpoint, key result, keep/drop reason |
| Pass 2 | Understand evidence | claim-evidence table, methods assumptions, labels/reference standard, validation, statistics, limitations |
| Pass 3 | Learn craft and positioning | introduction moves, figure architecture, wording patterns, reviewer objections, how to cite or compete with it |

Do not force Pass 3 for every paper. Reserve it for top-journal exemplars, closest competitors, or papers the user wants to emulate.

## Imaging paper note

```text
Citation:
Study type:
Clinical task:
Population / centers / dates:
Modality / protocol:
Annotation or reference standard:
Model / radiomics / omics pipeline:
Validation design:
Primary metrics with CI:
Calibration / DCA / reader study / survival:
Main claim:
Claim boundary:
Key figure/table:
Limitations reviewers would notice:
Citation role:
Craft pattern worth borrowing:
```

## Calibration check

After translation or extraction, compare:

| Item | Reader's understanding | Paper-supported wording | Gap |
|---|---|---|---|
| Main contribution | ... | quote or close paraphrase with block ID | too broad / accurate |
| Primary result | ... | metric + CI + cohort | missing CI / wrong cohort |
| Limitation | ... | source limitation | omitted / softened |

If the user's intended takeaway is broader than the paper supports, flag it before handing the paper to `radiology-writing` or `radiology-citation`.

## Craft extraction

For high-value exemplars, extract:

- Title rhythm: population, modality, method, outcome, or claim order.
- Abstract close: how the authors bound the result.
- Introduction moves: clinical stakes, gap, technical/biological premise, objective.
- Figure order: flowchart, overview, primary result, validation, subgroup/biology/utility.
- Limitation style: what is admitted and how it is made non-fatal.

These notes feed `radiology-writing/references/argument-spine-and-stage-gates.md`.
