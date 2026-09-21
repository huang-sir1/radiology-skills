---
name: radiology-writing
description: "Draft/restructure manuscripts or theses from fixed evidence; not polishing, review or rebuttal. CN: 论文写作、英文稿、结构化摘要"
---

# Venue-routed imaging and mechanism manuscript writing

Use this skill to **construct** imaging or mechanism-research prose — argument first, then
sentences — in the selected venue's real shape. _Radiology_ is the fallback only for an
imaging-centered manuscript whose venue is not yet selected; it is not the default shape for a
standalone bulk RNA, single-cell, spatial or perturbation paper. For sentence-level polish use
`radiology-polishing`.

## Core stance

- **Author evidence first.** Never invent results, metrics, p-values, cohort numbers,
  citations, mechanisms, or limitations. Missing input → explicit placeholder or a question.
- **Write the argument before the sentences.** One-sentence claim → section architecture →
  paragraph jobs → prose.
- **Match the selected venue family.** Use _Radiology_ Summary/Key Results only on the RSNA route;
  Nature/npj, Cell Press, JAMA Network, Lancet and Wiley routes are not interchangeable.
- **Preserve the scientific packet.** When a validated radiogenomics handoff exists, stable Claim
  IDs, modality roles, independent unit, matched n, evidence state, claim branch/verdict/ceiling and
  protected placement are immutable. Return conflicts to the scientific ledger.
- **Preserve the evidence-synthesis packet.** For `evidence-synthesis`, consume the frozen protocol,
  search, selection-flow, extraction, risk-of-bias/applicability, synthesis and certainty artifacts
  from `radiology-systematic-review`. Preserve the study-family/report/effect-row hierarchy and the
  `synthesized` claim ceiling; this route does not require a radiogenomics handoff.
- **Bound the claim.** Ambitious but evidence-bounded; calibrate verbs to evidence
  (demonstrate → suggest → may reflect).
- **Reporting-aware.** Every Methods/Results element should satisfy the relevant checklist
  item (CLAIM/TRIPOD+AI/CLEAR/STARD) — cross-check with `radiology-reporting`.

## When to use

- Draft/rebuild any section: title, abstract, Introduction, Methods, Results or Discussion, plus
  venue-specific front matter such as Summary statement/Key Results only when the selected route
  requires it.
- Turn Chinese lab notes / mixed drafts into submission-ready English.
- Chinese→English **translation/reconstruction of manuscript text** (language translation —
  not to be confused with `radiology-translation`, which is clinical/bench-to-bedside
  translation). Translate the argument and intent, not clause order; open
  `references/chinese-author-workflow.md` first.
- Restructure a rejected draft to the _Radiology_ argument shape.
- Build or audit a monograph thesis, article-based/cumulative thesis, chapter package,
  thesis-to-paper conversion or whole-thesis argument spine from fixed evidence. Institutional
  regulations and examiner decisions remain external human authority.
- 中文高频说法：“帮我把中文实验记录/组会思路写成英文投稿稿。”“按 Radiology 风格重构摘要和讨论。”

## When to open extra files

| File | Open when |
|---|---|
| [references/article-architecture.md](references/article-architecture.md) | Section order, argument flow, and the _Radiology_ manuscript skeleton |
| [references/structured-abstract.md](references/structured-abstract.md) | Writing the structured abstract + Summary statement + Key Results box |
| [references/methods.md](references/methods.md) | Materials and Methods for imaging/AI/radiomics studies (what must appear, in order) |
| [references/results.md](references/results.md) | Results narrative: flow, performance with CIs, comparisons, validation |
| [references/discussion.md](references/discussion.md) | Structured Discussion (key-finding first → context → limitations → conclusion) |
| [references/chinese-author-workflow.md](references/chinese-author-workflow.md) | Notes are Chinese / mixed / lab-note style; translate intent and argument, not clause order |
| [references/nature-family-shape.md](references/nature-family-shape.md) | Target is Nature Medicine / Nature Biomedical Engineering / Nature Communications / npj Digital Medicine, etc. — unstructured abstract, no Summary statement/Key Results box, different Methods placement |
| [references/cell-jama-wiley-shape.md](references/cell-jama-wiley-shape.md) | Target is Cancer Cell, Cell Reports Medicine, JAMA Network Open or Advanced Science; keeps the families distinct and fails closed when the exact shape is unverified |
| [references/argument-spine-and-stage-gates.md](references/argument-spine-and-stage-gates.md) | Full manuscript rebuild, rejected-paper rescue, unclear contribution, high-impact submission, or a draft whose story/figures/results do not yet lock together |
| [references/journal-family-writing-style.md](references/journal-family-writing-style.md) | Target journal family is known, or the user supplied author-guide PDFs/classic papers and wants the manuscript to carry that venue's writing style |
| [references/section-contract-and-style-profile.md](references/section-contract-and-style-profile.md) | Full-section drafting, multiple coauthors, author-voice calibration, or when prose keeps drifting beyond the allowed evidence |
| [../radiology-radiogenomics/references/scientific-handoff-contract.md](../radiology-radiogenomics/references/scientific-handoff-contract.md) | A prior radiogenomics/mechanism task supplies a shared-state packet; validate it and return a Claim-ID drift ledger |
| [../radiology-method-evaluation/references/parameter-and-methodology-evaluation.md](../radiology-method-evaluation/references/parameter-and-methodology-evaluation.md) | Drafting or placing parameter provenance, metric/method comparison, ablation, sensitivity, robustness, failure or efficiency evidence; do not convert a planned/unverified evaluation into Results prose |
| [../radiology-systematic-review/references/review-methods-and-quality-gates.md](../radiology-systematic-review/references/review-methods-and-quality-gates.md) | Drafting a systematic/scoping review or meta-analysis from a fixed writing handoff; verify the protocol/search/flow/extraction/RoB/synthesis/certainty chain and keep study families distinct from reports/effect rows |
| [references/thesis-and-dissertation-architecture.md](references/thesis-and-dissertation-architecture.md) | Monograph or article-based thesis, chapter drafting/revision, thesis-to-paper conversion, synthesis chapter, whole-thesis audit or defense handoff |

## Intake (identify before drafting)

- **Target venue/shape**: resolve RSNA, Nature/npj, Cell Press, JAMA Network, Advanced/Wiley,
  European, NEJM, Science or Lancet before finalising front matter. For Cancer Cell, Cell Reports
  Medicine, JAMA Network Open or Advanced Science, open `cell-jama-wiley-shape.md`. If venue is
  undecided, use a reversible journal-neutral scientific spine; use the _Radiology_ fallback only
  for an imaging-centered paper.
- **Scientific state**: if a mechanism or radiogenomics packet is supplied, record its path,
  canonical `packet_sha256`, distinct physical file SHA-256 when transported, source-manifest digest
  and `writing_handoff_status`; validate it before consuming `W-HANDOFF-READY`. If no packet exists,
  build a local map of scope, modality roles, independent unit, usable n, material Claim IDs,
  evidence locations, evidence states and wording ceilings from the supplied artifacts. Mark
  unresolved fields `AUTHOR_INPUT_NEEDED`; do not block traceable sections merely because another
  module was not invoked first. An untraceable Results or mechanism claim receives a visible scaffold
  or `W-RETURN-TO-LEDGER`, never invented science.
- **Evidence-synthesis state**: for `study_scope=evidence-synthesis`, record the review route,
  lifecycle, protocol/search/selection-flow/extraction/risk-of-bias-applicability/synthesis/certainty
  artifact IDs, versions and SHA-256s, study-family hierarchy, pooling decision, certainty and
  supported/forbidden wording. If a decision-bearing artifact is missing or not fixed, write only a
  visible Methods/Results scaffold and return the affected item to `radiology-systematic-review`.
- **Section(s)** requested.
- **Study type**: diagnostic-accuracy, prediction model, radiomics, radiogenomics, reader
  study, observational, trial, scoping review, systematic narrative synthesis, or meta-analysis.
- **Core claim**: what the study actually shows.
- **Evidence**: cohorts (n, source, dates), metrics with CIs, comparisons, validation.
- **Method-evaluation state**: Evaluation IDs, parameter/configuration IDs, benchmark/ablation
  artifacts, selection/freeze points, evidence state and claim consequence when the paper makes a
  methodological or robustness claim.
- **Boundary**: where the claim stops (single-centre? retrospective? prevalence?).
- **Limits**: target word/figure counts (verify against current author instructions).
- **Thesis state when applicable**: degree/programme, monograph versus article-based form,
  institutional rule source/date, included-paper status and reuse rights, chapter/version map,
  cross-chapter claim IDs, contribution statement, examination/defense milestone and embargo route.

If core claim, evidence, or boundary is missing, surface the gap and offer a scaffold with
placeholders rather than inventing content.

## Writing workflow

0. **For full manuscripts or high-impact rebuilds**, open
   `argument-spine-and-stage-gates.md` and establish the project context, contribution-first
   gate, and results-as-validation map before drafting long prose.
0. **For radiogenomics or mechanism work**, validate an existing packet and establish a Claim-ID
   drift ledger. Without a packet, create the bounded local scientific-state map described above and
   continue wherever evidence is traceable; escalate only affected scientific uncertainties to
   `radiology-radiogenomics`.
0. **For evidence synthesis**, select `study_scope=evidence-synthesis`, consume the fixed
   `radiology-systematic-review: writing-handoff`, and verify all seven review-artifact roles plus
   the study-family/report/effect-row map before drafting Results or certainty language. Planned,
   author-reported or unresolved pooling output stays out of Results. Route a changed eligibility,
   extraction, bias, synthesis or certainty decision back to the review owner rather than creating a
   radiogenomics packet.
0. **For target-venue writing taste**, open `journal-family-writing-style.md` after confirming
   the venue family; use it to adjust article shape, title/abstract rhythm, key points, and
   clinical relevance language.
0. **For parameter or methodology evidence**, consume a completed
   `radiology-method-evaluation` matrix when available. If the evaluation is missing, separate
   Methods reporting facts from the unproven Results claim and return only the affected question to
   that module.
0. **For thesis/dissertation work**, open `thesis-and-dissertation-architecture.md`; freeze the
   institution/programme rule passport and choose `monograph`, `article-based`, `chapter-draft`,
   `thesis-to-paper` or `whole-thesis-audit`. Keep a thesis-wide contribution spine, stable Claim IDs,
   included-paper/version/reuse-rights map and cross-chapter non-duplication ledger. Do not convert a
   defense outcome, examiner judgment or repository/embargo decision into a writing-model verdict.
1. **One-sentence argument**: *"In [population/modality], we show [advance] using [approach],
   supported by [key result with CI], with [boundary]."*
2. **Pick the architecture conditionally** — RSNA/_Radiology_ route →
   `article-architecture.md` and, when applicable, `structured-abstract.md`; Nature/npj route →
   `nature-family-shape.md`; Cancer Cell/Cell Reports Medicine/JAMA Network/Advanced-Wiley route →
   `cell-jama-wiley-shape.md`. For other verified families, use the applicable current guide/style
   reference. If the family is unknown or its exact shape is unverified, retain a reversible
   journal-neutral scientific spine and mark `VENUE_SHAPE_UNVERIFIED`.
3. **Map each paragraph to one job**: context / gap / objective / design / cohort / technique
   / analysis / result / comparison / validation / interpretation / limitation.
4. **For full sections**, define the section contract (purpose, inputs, allowed/forbidden claims,
   evidence and validation) and, when author samples exist, the style profile from
   `section-contract-and-style-profile.md`.
5. **For full sections**, draft the topic-sentence chain first, carrying the stable Claim ID beside
   each material sentence. If the claims do not flow,
   revise the chain before writing full paragraphs.
6. **Draft from evidence outward** — keep claims next to the numbers that support them.
7. **Calibrate verbs** to evidence; remove unsupported novelty/"first" claims.
8. **Fit only the selected venue-family shape** — require abstract headings, Summary statement, Key
   Results and the _Radiology_ Discussion pattern only on the RSNA/_Radiology_ route. Do not import
   those elements into Nature/npj, Cell Press, JAMA Network, Lancet or Wiley routes unless the
   current target-journal instructions independently require them.
9. **Self-review** against the section contract and relevant reporting checklist; flag unmet
   items. For full manuscripts, use a fresh-reader/adversarial pass before final prose ships.

## RSNA / _Radiology_ route defaults

Apply this section only after the RSNA/_Radiology_ route is selected. Other routes use their own
shape reference; an undecided venue keeps the journal-neutral scientific spine.

- **Title** — concrete: population/condition + modality/method + finding/role. State AI/
  radiomics if central. Avoid slogans and "novel."
- **Structured abstract** — Background → Purpose → Materials and Methods → Results →
  Conclusion; report design, cohort sizes/dates, primary metric(s) **with CIs**, a bounded
  conclusion. (structured-abstract.md)
- **Summary statement** — a single declarative sentence of the main finding.
- **Key Results** — up to **3** results/conclusions, **≤ 75 words**, with summary data; don't
  repeat the Summary statement; avoid vague language and abbreviations.
- **Introduction** — field/clinical stakes → specific gap → objective/hypothesis. Short; no
  results dump.
- **Materials and Methods** — design + ethics/registration → participants/flow → imaging
  technique → image analysis/reference standard/readers → model/feature pipeline →
  statistical analysis. (methods.md)
- **Results** — patient flow + characteristics → primary performance with CIs → comparisons →
  validation/subgroups. Past tense, quantitative. (results.md)
- **Discussion** — **first paragraph = concise summary of key findings**, then relation to
  prior work, then **limitations**, then a bounded conclusion. (discussion.md)

## Output format

1. **`Draft`** — the requested prose in the selected venue-family shape, or the reversible
   journal-neutral scientific spine when the venue is unresolved.
2. **`Section outline`** — 3–7 compact bullets (for a full section).
3. **`Topic-sentence chain`** — for full sections or major rewrites, the claim sequence before
   paragraph expansion.
4. **`Section contract`** — purpose, inputs, allowed/forbidden claims, validation, and word/display
   budget for full sections.
5. **`Claim–evidence map`** — `Claim ID | Claim | Evidence (with CI) | immutable ceiling |
   Status: supported / needs input`.
6. **`Stage gates`** — for full manuscripts: contribution gate, results-as-validation gate,
   citation/figure/reporting gates that are passed or still open.
7. **`Venue style check`** — if the target family is known: abstract shape, title/key-points
   logic, clinical relevance language, and any guide-derived limits or `VERIFY FROM GUIDE`.
8. **`Style calibration`** — journal/discipline rules applied first; author-profile traits used
   only where compatible and based on actual samples.
9. **`Assumptions / missing inputs`** — only material gaps.
10. **`Reporting check`** — checklist items this draft does/doesn't satisfy (→ radiology-reporting).
11. **`Claim-ID drift ledger`** — for a scientific handoff: immutable fields preserved, editorial
    changes, any return-to-ledger request, and the packet digest consumed.
12. **`Method-evaluation placement map`** — when applicable: Evaluation/Parameter IDs and exact
    Methods, Results, Figure/Table, Supplement/config/code and Discussion locations, preserving each
     evidence state and claim consequence.
13. **`Evidence-synthesis placement map`** — for review manuscripts: stable Claim ID, study-family
    unit, protocol/search/flow/extraction/RoB/synthesis/certainty source anchor, evidence state,
    supported wording, forbidden stronger wording, and exact Methods/Results/display/Supplement/
    Discussion placement.
14. **`Thesis architecture packet`** — when applicable: thesis mode and rule passport, contribution
    spine, chapter jobs/dependencies, included-paper/version/reuse-rights map, cross-chapter
    claim/display/method overlap ledger, synthesis/conclusion ceiling and defense/repository handoff.

For Chinese notes: polished English first, then brief Chinese notes on structural choices.

## Handoffs
- Sentence-level polish / house style → `radiology-polishing`.
- Statistics/CIs/tests behind the numbers → `radiology-stats`.
- Parameter/metric/method fit, fair benchmark, ablation and sensitivity evidence design or audit →
  `radiology-method-evaluation`; this writing skill consumes fixed evidence but does not certify an
  unrun evaluation.
- Frozen Methods/Results handoffs from execution skills (`radiology-acquisition-qc`,
  `radiology-annotation`, `radiology-radiomics`, `radiology-deep-learning`,
  `radiology-transcriptomics-analysis` writing-handoff outputs) are consumed as fixed evidence:
  integrate and reconcile them, never silently upgrade their claim ceilings.
- Checklist compliance → `radiology-reporting`.
- Figures/legends → `radiology-figure`.
- Publication tables and table footnotes → `radiology-table`.
- Finding/verifying citations to support a claim in Introduction/Discussion → `radiology-citation`.
- Draft scientific review is scope-aware: `imaging-only` → `radiology-prereview`;
  `mechanism-only` → `radiology-radiogenomics: manuscript-review`; `imaging-mechanism` → mechanism/
  bridge review in `radiology-radiogenomics` first, then imaging/editor synthesis in
  `radiology-prereview`; `evidence-synthesis` → `radiology-systematic-review: audit/writing-handoff`,
  then `radiology-prereview: evidence-synthesis-review` with
  `scientific_handoff_digest=not-applicable`. Do not treat any scientific review as all-files
  submission readiness.
- Full-project artifact state → `radiology-pipeline`; upload-ready package (cover letter
  included — template at `radiology-submission/assets/cover-letter-brief.template.md`) →
  `radiology-submission`.
- Thesis defense deck and rehearsal artifact → `radiology-paper2ppt`; examiner or institutional
  approval stays with the graduate programme; thesis repository/access/embargo operations route to
  `radiology-data` / `radiology-research-ops` as applicable.
