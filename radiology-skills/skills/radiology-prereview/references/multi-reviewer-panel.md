# Multi-reviewer panel

Use one frozen manuscript fact base, then select and declare one panel mode. Different emphases are
allowed; invented reviewer names, institutions, seniority, or biographies are not.

## Panel modes and naming

### `lens-separated` (default)

One agent or person may apply the three lenses in separate sections while sharing conversation or
reasoning context. Freeze each lens report before synthesis and preserve minority findings, but do
not call the reports or reviewers independent. The honest label is “three lens-separated reviews.”

### `independent`

Use this label only when all of the following are evidenced:

1. each reviewer runs in an isolated context and cannot inspect another review, intermediate
   synthesis, editor preference or evolving recommendation;
2. every reviewer receives the same frozen fact base and the same source-artifact versions and
   SHA-256s, plus only the instructions for that review lens;
3. reviewer identity/role and conflicts are recorded without invented biography;
4. each report is completed and frozen with report ID, version, completion time and output SHA-256
   before any report is revealed to the editor/synthesizer; and
5. editor synthesis begins only after all required frozen reports exist.

If any isolation or freeze evidence is missing, downgrade the label to `lens-separated`; do not infer
independence from three headings, three prompts, subagent names or sequential execution.

## Shared fact base

Extract once:

- study question, population, modality, endpoint, design, cohorts, centers, dates, events;
- primary model/analysis, validation, comparator, main numerical results and uncertainty;
- claimed contribution, intended clinical/biological meaning, target venue, and reporting stack;
- materials not provided and therefore not assessable.

## Reviewer lenses

### Reviewer 1: Clinical radiology and significance

Assess clinical question, target population/spectrum, reference standard, workflow relevance,
reader comparison, threshold-to-action logic, generalisability, and whether the conclusion changes
practice or only reports technical performance.

### Reviewer 2: Methods, statistics, and reporting

Assess estimand, sample size/events, clustering, missing data, multiplicity, split/resampling,
calibration, DCA, survival assumptions, uncertainty, reporting guidelines, and result consistency.

### Reviewer 3: Imaging AI/radiomics/radiogenomics and reproducibility

Assess preprocessing, annotation, leakage, harmonisation, feature/model selection, baselines,
external validation, explainability/UQ/robustness, biological mapping, code/data/run provenance, and
reproducibility artifacts.

## Per-review output

Each reviewer returns:

1. overall assessment and assessment boundary;
2. strongest contribution and who would care;
3. blocker/major/minor concerns with locations and fixes;
4. evidence needed to establish the authors' case;
5. recommendation posture without pretending to be the editor.

For `independent` mode, also record:

`review ID | lens | frozen fact-base digest | source-artifact digest set | isolated context ID |
conflict state | completed on | report path | report SHA-256 | released to synthesis on`.

## Editor synthesis

Only after all three reports are frozen, synthesize:

- consensus strengths and decisive weakness;
- concerns raised by two or more lenses;
- legitimate differences in weighting;
- broad readership/clinical importance and venue-fit risk;
- smallest set of fixes that changes the recommendation;
- readiness verdict.

Do not average away a blocker because the other reviewers did not mention it. Preserve minority
technical findings when they are evidence-backed.
