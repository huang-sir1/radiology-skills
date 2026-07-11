# Venue style profiles from author guides and exemplar papers

Use this reference when the user supplies author guidelines, browser-printed PDFs, or classic articles for a target journal family and asks the skill to absorb the venue's writing, figure, and submission style. Keep this as a style profile, not a replacement for current live author-instruction verification.

## Source status

As of the local `Skill-guide` ingestion on 2026-07-09:

- Parsed: Nature Partner Journals guide to authors, Nature editorial policy checklist/reporting summary forms, European Radiology Manuscript Requirements Edition 2.1 (April 2025), European Radiology disclosure template, European Radiology graphical abstract template.
- User-supplied and learned: NEJM author-center pasted guide, Science author guide pasted text, and The Lancet Digital Health Information for Authors PDF (April 2026, image-only PDF rendered locally).
- Project rule from user: use The Lancet Digital Health guide as the default representative profile for the whole Lancet series unless a later supplied Lancet-journal-specific guide explicitly overrides it.
- Still blocked or not supplied as exact guides: ASCO/JCO family and NEJM AI/Catalyst-specific instructions. Use live verification or a supplied guide before enforcing exact limits for those venues.

## How to extract a new venue profile

For each journal guide or classic article set, extract:

| Dimension | What to capture |
|---|---|
| Editorial taste | Clinical vs methodological vs biological emphasis; specialist vs generalist readership |
| Article shape | Abstract type, key points, highlights, significance statement, methods placement, required sections |
| Word/display limits | Main text, abstract, figures, tables, supplementary/extended data, graphical abstract |
| Evidence bar | External validation, prospective data, reader study, calibration, DCA, biology, implementation |
| Writing voice | Sentence length, jargon tolerance, novelty language, clinical relevance language, limitations style |
| Figure style | Panel letters, background, palette, legend length, source data, graphical abstract style |
| Compliance artifacts | Reporting summary, checklists, ethics/consent, data/code availability, disclosures |
| Classic-paper patterns | Recurring figure architecture, abstract rhythm, result ordering, caption style |

Rules from author guides override patterns inferred from classic articles. Classic papers teach taste; author instructions set constraints.

## Nature Partner / npj family

**Editorial taste.** Broad scientific and clinical accessibility. The background, rationale, and main conclusions must be understandable to non-specialists. Technical jargon should be reduced or explained; abbreviations should be kept to a minimum and defined at first use.

**Article shape.** Initial submission is flexible, but final formatting expects a title page, required content-type sections, acknowledgements if used, author contributions, competing interests, references, figure legends, and tables. Research articles commonly follow abstract, introduction, results, discussion, and methods. Life-sciences submissions require a completed reporting summary and an editorial policy checklist.

**Data and reproducibility.** Original research must include a data availability statement describing the minimal dataset needed to interpret, replicate, and build on the work. Dataset citations should include DOI or accession codes when available.

**Figure taste.** Use white backgrounds, clear sans-serif lettering, lowercase bold panel letters, color-blind-safe palettes, and no decorative effects. Avoid unnecessary figures, excessive boxing, arbitrary color, red/green-only heatmaps, 3D histograms, and axis truncation that exaggerates differences. Figure legends start with a brief title, describe each panel and symbols, define error bars, and should be concise.

**Best fit.** Papers with broad importance, strong validation, reproducibility discipline, open data/code posture, and a clean generalist narrative. Purely local retrospective model-building needs careful down-tiering unless validation and clinical relevance are unusually strong.

## European Radiology

**Editorial taste.** Specialist radiology audience, high value on concise clinical specificity and operational clarity. Instructions marked "Must have" are submission-return risks, not optional style preferences.

**Title.** Keep short and concrete. Include body part, disease, technique, and/or problem. Highly recommended length is no more than 15 words. Avoid abbreviations except very common radiology abbreviations such as CT, MR, MRI, PET, US, BI-RADS, LI-RADS, and PI-RADS.

**Article limits.** Original articles: main text up to 3000 words, up to 6 figures, up to 5 tables, supplementary material allowed. Technical developments: up to 2000 words, up to 4 figures, up to 4 tables.

**Abstract.** Maximum 250 words. Use a structured shape with Objectives, Materials and Methods, Results, and Conclusion. Results should start with the enrolled/evaluated cohort and include numerical data, p values, and confidence intervals when appropriate. The conclusion must answer the objective and be derived from results; do not add broad implications.

**Key points and Clinical Relevance Statement.** Use three concise items:

- Question: 20-25 words explaining the unmet need or clinical problem.
- Findings: 20-25 words objectively summarizing the main result.
- Clinical Relevance Statement: maximum 40 words summarizing benefit for the patient and/or clinical relevance.

**Introduction.** Keep under 400 words. Use short paragraphs. Avoid generic disease background; position the precise scientific question, gap, relevance, and how the study addresses it.

**Methods.** First sentence should address IRB approval and informed consent. State retrospective/prospective design, date ranges, patient enrollment/retrieval method, inclusion/exclusion criteria, consecutive/random selection, index test, reference standard, evaluation process, instruments/drugs/contrast, and statistical methods. Consider a statistical guarantor and sample-size calculation when applicable.

**Results.** Start with the final cohort after exclusions. Use Figure 1 for the flowchart where appropriate. Mirror Methods subheadings, report all collected statistical analyses rather than only positive results, cite figures/tables in order, and avoid interpretation or unsupported trend language.

**Discussion.** Use a four-part rhythm: key results and interpretation, comparison with literature, limitations/biases and mitigation, short conclusion with clinical implication supported by the results.

**References.** Use square-bracket numerical citations in text. References are listed in order of appearance. Published/accepted sources must have DOI available. Use all authors for six or fewer; first three plus et al. for seven or more.

**Figures and tables.** Figure captions must be self-contained but brief, explain symbols/visual aids, define abbreviations and units, use lowercase panel letters in text and captions, and avoid embedding figure numbers/captions inside the figure file. Tables should be self-contained, explain abbreviations/footnotes, keep consistent precision, and avoid decorative colored cells or meaningless typeface changes.

**Graphical abstract.** The European Radiology template uses: article title, authors/DOI, methodology, visual element/image/illustration/graph, hypothesis/question, main finding or relevance statement, patient cohort, modality/organ, and single/multicenter status.

**Compliance paragraph.** The disclosure template expects funding, scientific guarantor, conflicts of interest, statistics/biometry, informed consent, ethics approval, cohort overlap, and methodology language.

## NEJM

**Editorial taste.** NEJM wants work that can change clinical practice and teach something new about disease biology or care. The opening frame must be clinically consequential rather than merely technical. For imaging AI, radiomics, or radiogenomics, the pitch should translate the model into patient-level or decision-level consequence and avoid local workflow claims unless they affect practice.

**Article shape.** Original research uses a concise four-part abstract: Background, Methods, Results, Conclusions, with a 250-word cap and trial registration when applicable. Submission materials can include cover letter text, main text, tables, figures, supplementary appendix, clinical trial protocol, and statistical analysis plan. The main manuscript text file should compile text, references, figure legends, and tables.

**Display items.** Original Articles normally allow a combined total of five figures and tables. Put extensive technical tables, feature lists, model details, and sensitivity analyses into the supplementary appendix rather than crowding the main paper.

**Statistical evidence bar.** NEJM is unusually strict about reproducibility of the analysis plan. A protocol or equivalent and an SAP should be supplied; the SAP should be detailed enough for another analyst to replicate the analysis in a similar dataset. Multiplicity must be prespecified for confirmatory analyses; without adjustment, secondary/exploratory results should be presented as estimates with 95% CIs and non-definitive interpretation.

**Radiology-AI translation.** For prediction, diagnostic, and survival work, report absolute event counts or rates before relative measures when possible. Distinguish clinical importance from statistical significance. Avoid causal language in observational work unless using justified causal inference methods and diagnostics.

**Survival-specific gates.** If reporting HRs, address the proportional hazards assumption and provide supporting evidence. If competing events can make censoring dependent, replace simple Kaplan-Meier event-time estimates with cumulative incidence and use association measures that account for competing risks.

**Missing data.** Report missingness for baseline variables and all analysis variables. Complete-case analysis is generally not acceptable as the primary analysis unless missingness is rare; describe assumptions and methods such as multiple imputation, inverse-probability weighting, or appropriate models, plus sensitivity analyses when needed.

**Figures and image integrity.** Data visualizations should be submitted as editable vector files when possible. Scientific and medical images require full disclosure of digital adjustments and AI-assisted processing; generative AI must not create, alter, add, remove, or fabricate scientific/medical image content. Original unprocessed image files may be requested.

**Best fit.** Multicenter, prospectively planned, practice-changing imaging evidence; trials or robust observational studies with SAP-level statistical discipline; radiomics/radiogenomics only when the clinical action and validation are strong enough for a general medical audience.

## Science

**Editorial taste.** Science prioritizes influential work that substantially advances scientific understanding and is important within or across fields. The manuscript must be legible to a broad scientific readership. For radiology AI or radiogenomics, the central claim should be a scientific or translational advance, not just incremental model performance.

**Article shape.** Research Articles normally cap main text at 3000 words, with an abstract, 3 to 5 display items, brief legends, about 50 main-text references, and structured acknowledgments. Main text should use brief subheadings. Materials and Methods normally move to supplementary materials and must be sufficiently detailed for replication.

**Extended format.** Some Research Articles can use an extended online format with up to 6000 words, as many as 6 display items, and up to 100 main-text references when justified in the cover letter. Articles that are not a good fit for print format may need a one-page print summary with Introduction, Rationale, Results, and Conclusion, plus a summary figure and a short caption.

**Data and code posture.** All data must be available in the main text, supplementary materials, or a public repository cited in the paper. Tabulated data underlying figures should be supplied as a machine-readable supplementary data file such as data S1. Persistent repository identifiers should be cited where possible; Dryad deposition can be linked through the submission system.

**Submission package.** The initial submission requires a manuscript file and a combined PDF containing the complete main manuscript, figures, tables, and supplementary materials. Cover letter is required and should state the paper title and main point, fair-review context, related submissions, presubmission discussions, prior sharing, exclusivity, human/animal assurances, data availability and restrictions, and any additional review materials.

**Fit bar.** A Science-targeted imaging AI paper needs more than high AUC. It needs a broadly important mechanism, resource, benchmark, biological insight, or clinical paradigm shift; the figure set should read as a compact scientific story rather than a conventional diagnostic-performance report.

## Lancet family

Default proxy: The Lancet Digital Health Information for Authors, April 2026. Per user instruction, apply this profile as the default Lancet-series style unless a supplied guide for a specific Lancet journal contradicts it.

**Editorial taste.** Lancet-series papers should read as clinically consequential, practice- or policy-relevant, transparent, equity-aware, and useful to a broad health readership. For digital health and imaging AI, this includes AI/ML in health care, telemedicine, computational medicine, biomedical analytics, data management, security, digital trials, wearables, precision medicine, genomics, diagnostics, prognostics, prediction, and classification.

**First submission package.** Include a covering letter, manuscript with tables and panels, figures, Research in context panel for primary research Articles, author statement form, declaration of interests and funding statements, accepted in-press papers where applicable, protocols and CONSORT details for randomized trials, and any relevant prior editorial correspondence.

**Article shape.** Original Articles can be up to 3500 words, or 4500 words for randomized controlled trials, with about 30 references. The abstract is a semistructured summary of up to 300 words using Background, Methods, Findings, Interpretation, and Funding. The electronic submission system may request this section separately.

**Research in context.** All research papers, including systematic reviews and meta-analyses, require a no-reference panel with: Evidence before this study, Added value of this study, and Implications of all the available evidence. This is not decoration; editors and reviewers use it at the first assessment stage.

**Reporting guidelines.** Randomized trials follow CONSORT, cluster trials CONSORT extensions, harms reporting extended CONSORT, diagnostic accuracy STARD, observational studies STROBE, genetic association STREGA, systematic reviews/meta-analyses PRISMA, global health estimates GATHER, AI intervention trials CONSORT-AI, and AI trial protocols SPIRIT-AI.

**Digital health ethics and transparency.** AI use in manuscript preparation must be declared when beyond basic grammar/spelling checks. AI tools cannot be listed as authors or cited as authors. For figures, generative AI should be limited to brainstorming or suggesting concepts, not producing unattributed internet-derived visual content. Protect unpublished manuscripts, prompts, confidential data, and patient-identifiable content.

**Data sharing.** All submitted research Articles require a data sharing statement specifying whether data and dictionaries will be available, which data/documents will be shared, timing, location, access criteria, and restrictions. Authors may be required to provide raw data during review and for up to 10 years after publication.

**Equity and representativeness.** Human, animal, model-organism, and eukaryotic-cell research should address sex-based and gender-based analyses where relevant. For race and ethnicity, define categories, explain assignment, avoid race-based biological overinterpretation, and discuss representativeness and structural context.

**Survival-specific gate.** When reporting Kaplan-Meier survival data, include the number at risk at each timepoint and report censored participants where appropriate.

**Best fit.** Clinical, oncology, digital health, and imaging-AI work with clear practice/policy consequences, transparent reporting, strong external validation or trial/implementation logic, and a concise evidence-before/evidence-added/evidence-implication story.

## Pending profiles

Use these only as placeholders until the actual PDFs are supplied locally:

| Family | Current status | Rule |
|---|---|---|
| NEJM AI / NEJM Catalyst | Specific guide not supplied | Do not enforce exact limits; require supplied guide or live verification |
| ASCO / JCO family | Direct PDFs blocked by 403 | Do not enforce exact limits; require supplied guide or live verification |

## Classic article learning

When the user supplies classic articles for a journal:

1. Sample at least 3-5 comparable articles by study type.
2. Extract title rhythm, abstract opening/closing pattern, introduction gap logic, result ordering, figure architecture, caption density, and limitation style.
3. Separate house style from study-specific content.
4. Add only durable, reusable patterns to the relevant writing/figure/polishing references.
5. Never infer an exact word or figure limit from published articles; use author instructions for exact constraints.
