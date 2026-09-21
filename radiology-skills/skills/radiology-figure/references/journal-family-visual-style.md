# Journal-family visual style

Use this reference when the target journal family is known or when the user supplies classic articles and asks the figure set to feel like that venue. This file controls the "visual taste" layer; `chart-types.md`, `survival-figures.md`, and `figure-intent-and-render-qa.md` still control statistical integrity.

## Shared top-journal figure rule

Every venue prefers figures that survive reduction, explain one message, avoid decoration, and can be audited against source data. Do not make a figure more ornate than the journal can typeset.

## Nature Partner / npj visual profile

- Use a white background.
- Use clear sans-serif lettering throughout, preferably the same font size across the figure set.
- Use lowercase bold panel letters (`a`, `b`, `c`), placed consistently.
- Keep figure lettering lower-case except the first word of labels where appropriate.
- Use one- or two-column figure formats; build at final size.
- Keep legends concise: brief title first, then short panel descriptions and symbol definitions. For the parsed Nature Partner guide, use no more than 250 words unless the specific venue says otherwise.
- Define error bars and statistical treatment in the legend.
- Use scale bars rather than magnification factors; define scale-bar length in the legend.
- Avoid excessive boxing, decorative effects, 3D histograms, arbitrary color, heavy pixelation, and axis truncation that exaggerates differences.
- Recolor red/green-only heatmaps or arbitrary color schemes into color-blind-safe alternatives.
- Keep the thinnest final line at least about 1 pt when possible.
- Prepare source-data tables for every plotted number when the venue requires Source Data.

## European Radiology visual profile

- Treat figures as clinical explanation tools, not decorative summaries.
- Original articles should stay within the guide-level limit of up to 6 figures and 5 tables unless the current guide says otherwise.
- Use Figure 1 for the patient/study flowchart when appropriate.
- Number figures and tables in order of appearance.
- Keep figure captions self-contained but brief. Captions should explain symbols, arrows, arrowheads, asterisks, lines, color shades, abbreviations, and units.
- Use lowercase panel references in text and captions, such as Figure 1a and Figure 1b. In captions, address panels with the same lowercase letters.
- Do not embed figure numbers or captions inside the figure file.
- Use black or white symbols/visual aids unless color is explicitly needed.
- Do not over-describe images in captions; interpretation belongs in the main text.
- Tables should be self-contained, use consistent precision, define abbreviations/footnotes, and avoid colored highlights or decorative typeface changes.

### European Radiology graphical abstract

The local European Radiology graphical abstract template uses these blocks:

| Block | Content |
|---|---|
| Article title | Short title and citation metadata |
| Methodology | Very brief flowchart or up to 3 bullets, each under 6 words |
| Visual element | Image, illustration, or graph carrying the study's central visual |
| Hypothesis/Question | One short sentence, often adapted from the Question key point |
| Main finding/relevance | One short sentence under 20 words, often adapted from the Clinical Relevance Statement |
| Context tags | Patient cohort, modality/organ, single- or multicenter status |

Use this when creating a graphical abstract for European Radiology or a similar specialist venue.

## NEJM visual profile

- Use a white background and a restrained clinical-statistical layout.
- Treat every main figure as a reader-facing evidence display, not a decorative dashboard.
- Original Articles normally have a combined total of five figures and tables; push technical model details, feature stability plots, and exhaustive sensitivity figures to the Supplementary Appendix when needed.
- Data visualizations such as bar graphs, line graphs, scatter plots, dot plots, survival curves, box-and-whisker plots, forest plots, flow diagrams, timelines, and maps should be editable vector files such as AI, EPS, or SVG where possible.
- For scientific and medical images, document all brightness, contrast, color balance, cropping, compositing, annotation, and other digital adjustments. Keep original unprocessed files available.
- Do not use generative AI to create, alter, add, remove, or fabricate scientific or medical image content.
- Survival figures should show numbers at risk and should be backed by PH-assumption checks if HRs are presented. If competing risks are relevant, prefer cumulative-incidence displays over simple Kaplan-Meier event estimates.
- Forest plots should show log-scale CIs for ratio measures such as HRs, ORs, and RRs, and should avoid unplanned interaction p values when subgroup multiplicity was not prespecified.

## Science visual profile

- Build the figure set as a compact scientific story: 3 to 5 display items for a standard Research Article, with brief legends and strong figure-level messages.
- Each main figure should answer a different high-level question: discovery/overview, evidence, mechanism or validation, generalization, and implication.
- Keep methods-heavy plots, ablations, full feature inventories, and secondary cohorts in supplementary figures unless they are central to the advance.
- When an article is better suited to extended online format, plan up to 6 display items only when the cover letter can justify the extra space.
- Provide tabulated data underlying figures as machine-readable supplementary data when required, such as a `data S1` file.
- Summary figures for print summaries should be simple, explanatory, and captionable in no more than a short caption; avoid dense multi-panel statistical composites.
- Use broad-audience labels. Replace subspecialty acronyms with direct biological, clinical, or computational meaning when possible.

## Lancet family visual profile

Default proxy: The Lancet Digital Health Information for Authors, April 2026. Apply this visual profile across the Lancet series unless a supplied Lancet-journal-specific guide contradicts it.

- Use clean white academic figures with strong editorial discipline: no decorative gradients, no unnecessary card frames, no crowded legends, and no empty page-filling whitespace.
- The visual story should connect digital-health method to clinical or policy implication. A strong set usually includes: study flow or cohort map, model or intervention workflow, primary performance/utility, subgroup or equity/fairness assessment, and implementation or decision impact.
- Use a Research in context mindset for graphical summaries: the figure should make clear what was known, what this study adds, and why the implication matters.
- Photographs or image-based figure elements should be at least 300 dpi at final printed size, ideally TIFF or JPG.
- Trial profiles, study profiles, and CONSORT-style diagrams should be editable Word or PowerPoint files when requested.
- Non-photographic illustrations and line art should be editable vector files with selectable geometry and editable text: AI, EPS, vector PDF, PowerPoint, Word, or SVG.
- For annotated figures, provide an annotated copy and a non-annotated editable copy when feasible.
- Figure text should not be exported as outlined objects, especially in forest plots and dense statistical charts.
- Supplementary material should be one PDF with table of contents and numbered pages. Supplementary figures should still meet minimum legibility; figure headings and legends should be readable at final size.
- If reporting Kaplan-Meier curves, include numbers at risk at each timepoint and note censored participants as appropriate.
- If reporting AI interventions, make sure figure labels and captions align with CONSORT-AI or SPIRIT-AI where applicable.

## Classic article visual extraction

When the user supplies classic articles:

1. Identify the recurring first figure: flowchart, overview schematic, clinical imaging example, or primary-performance figure.
2. Record panel density, label case, legend length, color palette, and how uncertainty is shown.
3. Note how the article separates main figures from supplements.
4. Add durable patterns to the figure plan, but keep statistical chart construction honest and source-data driven.

## Pending exact profiles

ASCO/JCO-family and NEJM AI/Catalyst-specific visual limits are pending because exact guides were not supplied. Do not enforce exact panel/figure/artwork specifications until a printable guide is available locally or current instructions are verified live.
