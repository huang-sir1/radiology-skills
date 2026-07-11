# Literature survey workflow

Use this reference when the user needs more than a quick paper lookup: field mapping, Introduction support, reviewer-defense literature, dataset discovery, or a systematic background scan.

## Survey modes

Start by choosing the mode. A single project may move through several modes, but do not mix them silently.

| Mode | Use when | Output |
|---|---|---|
| Intent | The question is unclear | Search objective, concepts, inclusion/exclusion boundaries |
| Triage | Need a quick map | Ranked set of key papers/datasets and why they matter |
| Deepen | Need to understand a subfield | Paper notes, method comparison, evidence gaps |
| Synthesize | Need manuscript-ready reasoning | Gap matrix, prior-work table, claim-ready citations |
| Expand | Need adjacent ideas or mechanisms | Related tasks, datasets, biological pathways, methods |

## Corpus depth defaults

Use these defaults when the user does not know how large the survey should be:

| Archetype | Triage scope | Deep-read targets | Craft-extraction targets | Best output |
|---|---:|---:|---:|---|
| Explorer | 50-100+ records | 8-15 papers | 2-3 exemplar papers | landscape map |
| Investigator | 10-25 records | 5-10 papers | 2-3 exemplar papers | method/comparator table |
| Validator | 15-30 records | 3-5 closest papers | 3-5 closest papers | novelty/positioning argument |
| Reviewer-defense | 20-50 records | strongest comparators | all target-journal comparators | objection register |
| Dataset scout | registry-first | datasets + linked papers | n/a | validation/data-access plan |

## Radiology survey archetypes

| Archetype | Main question | Extra fields to capture |
|---|---|---|
| Explorer | What is happening in this imaging topic? | modality, disease, endpoint, study design, year trend |
| Validator | Does prior work support this claim? | cohort size, validation type, CI, calibration/DCA, limitations |
| Method chooser | Which model/analysis should we use? | architecture, feature pipeline, leakage controls, benchmark |
| Reviewer-defense | What will reviewers compare us against? | strongest competing studies, why our study differs, likely objection |
| Dataset scout | Is there public data for validation or biology? | source, access, modality, labels, omics, license, accession |

## Working artifacts

For longer projects, maintain:

- `survey-intent.md`: question, target venue, dates, languages, source types, inclusion/exclusion.
- `corpus-log.md`: all searched sources and deduplicated records.
- `paper-note.md`: one note per key paper.
- `gap-matrix.md`: what prior work does and does not establish.
- `exemplar-craft.md`: useful framing, figure architecture, limitations language from top papers.
- `figure-pattern-bank.md`: recurring figure types and what claims they support.
- `paper-library-index.md`: local PDF/RAG index status if a paper database, PaperQA2, NotebookLM, or similar backend is available.

## Paper-note template

```text
Citation:
Question / clinical task:
Modality and data source:
Cohort size, dates, centers:
Reference standard / labels:
Model or analysis:
Validation design:
Primary metrics with CI:
Calibration / DCA / reader study:
Main claim:
Limitations relevant to our manuscript:
Useful figure/table pattern:
Citation role: background / method / comparator / limitation / guideline
```

## Three-pass reading

Do not spend the same effort on every paper.

| Pass | Use for | Extract |
|---|---|---|
| Pass 1 | broad triage | question, contribution, cohort, modality, relevance, why keep/drop |
| Pass 2 | core comparators | claims, evidence, design assumptions, limitations, metrics with CI |
| Pass 3 | exemplar or closest competitor | introduction moves, figure architecture, limitation wording, reviewer objections, how to position against it |

Pass 3 is where writing craft is harvested: title rhythm, abstract closing, figure order, result-to-claim mapping, and how the authors make limitations sound honest rather than fatal.

## Local paper/RAG ladder

If a local paper database, PaperQA2, NotebookLM, or paperpipe-style tool is available, use the cheapest reliable route first:

1. Exact text search for a known term, endpoint, dataset, gene, metric, or author.
2. Ranked keyword/BM25 search over local paper notes or PDFs.
3. Direct read of the known paper, section, table, equation, or figure.
4. RAG synthesis only when the question spans several papers or asks for a cited synthesis.

Every RAG answer must cite paper, section/page/figure/table when available. If the excerpts do not support the claim, say it is not supported by the provided corpus rather than guessing.

## Search progression

1. **Intent pass**: define concepts and exclusions before searching.
2. **Recall pass**: PubMed/MeSH for biomedical literature; arXiv for recent AI methods; Crossref for DOI metadata; dataset registries for public data.
3. **Precision pass**: screen by title/abstract, venue, cohort relevance, modality, endpoint, and validation quality.
4. **Deep read pass**: read methods/results/figures of key papers; capture the paper-note template.
5. **Synthesis pass**: build `gap-matrix.md` and identify what citations can support manuscript claims.

## Gap matrix

| Prior work | Population/modality | Strength | Limitation | How our study differs | Citation role |
|---|---|---|---|---|---|
| ... | ... | external validation | no calibration / small cohort | adds calibration + multicenter validation | comparator |

Avoid novelty claims such as "first" unless `radiology-citation` verifies them with a high-recall search.

## WYSIATI check

Before finishing, ask what evidence may be missing because "what you see is all there is":

- Are non-English or regional imaging studies relevant?
- Are negative studies or small validation studies being missed?
- Is the strongest comparator outside radiology journals?
- Are there guidelines, consensus statements, or reporting standards that should outrank ordinary papers?
- Does a public dataset exist that reviewers will expect us to know?

Route unresolved claim support to `radiology-citation`.

## Manuscript-ready synthesis

When handing off to `radiology-writing`, provide these compact artifacts:

| Artifact | Purpose |
|---|---|
| `Gap matrix` | what prior work establishes and what remains open |
| `Comparator table` | cohort, modality, validation, metrics, calibration/DCA, limitations |
| `Citation-role map` | background / method / comparator / limitation / guideline |
| `Exemplar craft notes` | venue-specific title, abstract, figure order, and limitation style |
| `Reviewer-objection register` | what skeptical reviewers will cite and how the manuscript should pre-answer |
