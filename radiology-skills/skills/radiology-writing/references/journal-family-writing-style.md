# Journal-family writing style

Use this reference after the target venue or venue family is known, especially when the user supplies author guides or classic papers and asks for the manuscript to have the journal's "taste." This file controls writing voice and article shape; use `radiology-figure/references/journal-family-visual-style.md` for visual design.

## First rule

Do not write a generic "high-impact" paper. Pick the venue family and adjust:

| Family | Writing center of gravity |
|---|---|
| Radiology / RSNA | Structured, clinical imaging evidence, Summary statement + Key Results |
| European Radiology | Specialist radiology clarity, short clinical relevance; the official guide mixes Must-haves with Highly-recommended and Nice-to-have items — check each item's level below, not everything is a hard gate |
| Nature Partner / npj | Broadly intelligible scientific story, reproducibility, data availability, generalist readability |
| Cell Press | Results-led biological/clinical story with exact-title methods/resources/final components; never a Nature proxy |
| JAMA Network Open | Clinical IMRaD, structured abstract and Question/Findings/Meaning Key Points |
| Advanced Science / Wiley | Interdisciplinary scientific advance; exact house shape remains guide-bound |
| NEJM | Practice-changing clinical evidence, SAP-level statistical discipline, restrained conclusions |
| Science | Broad scientific advance, compact display-item story, generalist-readable mechanism or paradigm shift |
| Lancet family | Practice/policy impact, Research in context, transparent AI/data/reporting declarations; use The Lancet Digital Health guide as the default proxy |
| ASCO / JCO families | Exact local guide pending; use only broad instincts and verify before final formatting |

For Cell Press, JAMA Network Open and Advanced Science, read
`cell-jama-wiley-shape.md`. Do not route Cell Reports Medicine through the Nature-family profile.

## European Radiology writing shape

Use when the target is European Radiology or a similar European specialist radiology venue.

### Title

- Aim for 15 words or fewer — **Highly recommended** level in the official guide, not a Must-have; treat as a strong target, not a hard gate.
- Include body part, disease, technique, and/or clinical problem.
- Avoid abbreviations except very common radiology abbreviations such as CT, MR, MRI, PET, US, BI-RADS, LI-RADS, and PI-RADS.
- Avoid vague labels such as "pilot" or "preliminary" unless the design truly qualifies.

### Abstract

Use a 250-word structured abstract:

```text
Objectives
Materials and Methods
Results
Conclusion
```

The Results first sentence should identify the evaluated cohort, with age/sex summary if available. Report numerical results, p values, and CIs when appropriate. The Conclusion answers the objective only; do not add speculative importance.

### Key points and Clinical Relevance

Use exactly this logic:

| Item | Length | Job |
|---|---|---|
| Question | 20-25 words | Name the unmet need or clinical problem |
| Findings | 20-25 words | Objectively summarize the main result |
| Clinical Relevance Statement | max 40 words | State patient or clinical benefit |

Do not use unexplained subspecialty abbreviations in these items.

### Introduction

Keep under 400 words — **Nice-to-have** level in the official guide, not a Must-have; treat as a target and flag overruns rather than blocking on them. Use short paragraphs. Start with the specific clinical/scientific question, not broad disease epidemiology. End with a precise aim; prospective studies can state a hypothesis, retrospective studies should state the aim.

### Methods / Results / Discussion

- Methods must open with ethics/IRB/consent and then state design, dates, retrieval, inclusion/exclusion, index test, reference standard, evaluation, instruments/drugs/contrast, and statistics.
- Results should mirror the Methods structure and report all collected analyses, not only positive findings.
- Discussion uses four paragraphs: key interpretation, literature comparison, limitations/biases, and short clinical conclusion.

## Nature Partner / npj writing shape

Use when the target is npj Digital Medicine, npj Precision Oncology, Nature Communications-adjacent partner journals, or other Nature Partner Journals.

### Voice

- Write for an expert who may not be a radiologist.
- Explain background, rationale, and main conclusion clearly.
- Minimize jargon and abbreviations; define unavoidable technical terms at first use.
- Keep the title and abstract intelligible outside the subspecialty.

### Manuscript structure

Initial submission can be flexible, but the final article should clearly support:

- title page
- abstract
- introduction
- results
- discussion
- methods
- acknowledgements if used
- author contributions
- competing interests
- data availability
- references
- figure legends
- tables

Life-sciences submissions need a Reporting Summary and editorial policy checklist. Data availability should identify the minimal dataset needed to interpret, replicate, and build on the study, with DOI/accession codes where available.

### Argument style

Lead with why the result matters beyond a single department or scanner. Keep claims broad enough to interest a generalist but bounded by validation quality. If validation is retrospective/local, the closing claim should be translationally cautious.

## NEJM writing shape

Use when the target is NEJM or a NEJM-like general medical venue.

### Voice

- Lead with clinical practice, not algorithm novelty.
- Use restrained, declarative language; avoid promotional words such as "breakthrough" or "revolutionary."
- Separate statistical significance from clinical importance.
- For observational imaging AI, state associations and predictive performance; avoid causal verbs unless causal methods and assumptions are explicit.
- Keep technical radiomics/model details in Methods or Supplementary Appendix unless they change clinical interpretation.

### Abstract

Use the four labeled paragraphs:

```text
Background
Methods
Results
Conclusions
```

Keep to no more than 250 words unless the current guide differs. Include trial registration when applicable. Results should report absolute counts/rates where possible, effect estimates, CIs, and only those p values that are appropriate under the multiplicity plan.

### Methods and statistics

Open Methods around design, participants, protocol/SAP, primary and secondary endpoints, sample-size/power rationale when applicable, analysis population, missing-data method, multiplicity handling, and survival assumptions if time-to-event endpoints are used. For radiomics/radiogenomics, the SAP should distinguish prespecified confirmatory endpoints from exploratory feature/omics discovery.

### Results

Report the analysis cohort and missingness before model performance. Prefer absolute event frequencies before relative estimates. For survival outcomes, do not present HRs without PH-assumption support; if competing events are relevant, use cumulative incidence and appropriate competing-risk measures.

### Discussion

Start with the clinical meaning of the result, then the evidence that makes it credible, then limitations that could change practice interpretation. The closing sentence should say what the findings support now, not what the technology might someday do.

## Science writing shape

Use when the target is Science or a similarly broad, high-impact scientific audience.

### Voice

- Write for a scientifically literate non-radiologist.
- Make the advance conceptual, mechanistic, biological, translational, or resource-level.
- Keep jargon and modality-specific shorthand out of the title and abstract unless unavoidable.
- Let figures carry the evidence; each main-text section should explain why the evidence changes understanding.

### Research Article structure

Default shape:

- main text up to 3000 words
- abstract
- 3 to 5 display items
- about 50 main-text references
- brief section subheadings
- Materials and Methods in supplementary materials with enough detail for replication
- structured acknowledgments

Extended online format can be considered only when the story genuinely needs it; justify additional length in the cover letter.

### Argument style

The opening must answer "What changes in science if this is true?" before "What model did we train?" For radiogenomics, lead with the biological or disease-state insight. For imaging foundation models, lead with the generalizable capability, benchmark, or failure mode that teaches beyond a single dataset.

### Data and supplement style

Treat reproducibility as part of the story. Plan figure-underlying data as machine-readable supplementary data, and cite repository identifiers where available. Keep Methods sufficiently detailed for replication even when moved out of the main text.

## Lancet family writing shape

Use when the target is The Lancet, The Lancet Oncology, The Lancet Digital Health, eClinicalMedicine, or another Lancet-family venue. Per user instruction, use The Lancet Digital Health Information for Authors, April 2026, as the default representative guide unless a later supplied journal-specific Lancet guide explicitly overrides it.

### Voice

- Write around digital-health consequence: practice, policy, safety, equity, workflow, or implementation.
- Make the manuscript clinically readable, but keep the digital method transparent enough to audit.
- State AI use, data sharing, ethics, role of funder, and conflicts plainly rather than hiding them in generic boilerplate.
- Discuss representativeness, sex/gender, race/ethnicity, and structural context when relevant.

### Article shape

For original Articles, use a semistructured abstract:

```text
Background
Methods
Findings
Interpretation
Funding
```

Default limits from the supplied April 2026 guide are up to 3500 words, or 4500 words for randomized controlled trials, with about 30 references. Treat these as target-specific rules and recheck before final submission.

### Research in context panel

Add this panel for primary research, systematic reviews, and meta-analyses:

```text
Evidence before this study
Added value of this study
Implications of all the available evidence
```

Do not include references inside the panel. In "Evidence before this study," state databases or sources searched, dates, criteria, terms, evidence quality, and pooled estimates when relevant. In "Added value," name exactly what this study contributes. In "Implications," connect the new evidence to practice, policy, or future research.

### Methods and reporting

Route the design to its required guideline: STARD for diagnostic accuracy, STROBE for observational designs, PRISMA for reviews/meta-analyses, CONSORT-AI for AI interventions, and SPIRIT-AI for AI trial protocols. For survival work, include numbers at risk at each Kaplan-Meier timepoint and report censoring.

## Pending exact profiles

For ASCO/JCO-family targets and NEJM AI/Catalyst-specific targets, do not enforce exact word counts, figure counts, or reference style from memory. Ask for the browser-printed guide or route to `radiology-journal` to verify current instructions. You may still draft a clinically consequential, generalist-readable version, but label formatting limits as `VERIFY FROM GUIDE`.
