# Transparent peer-review lessons for research, writing and review (2024–2026)

Use this reference when a manuscript, writing plan, revision or mentoring decision should be
stress-tested against the public reviewer–author exchanges in
[the canonical 100-paper corpus](transparent-peer-review-corpus-2024-2026.tsv). It converts that
criterion-sampled, real-world experience corpus into applicable scientific questions; it is not a
universal checklist. Publication is not evidence that every residual concern was resolved.

## Evidence base and limits

The unit is one published paper paired with an official full reviewer-report/author-response file and
a page-located concern–action record. The publication window is 2024-08-22 through 2026-08-22.
The final set contains 100 unique DOIs:

| Journal | Papers | Selection note |
|---|---:|---|
| Nature | 12 | flagship |
| Nature Methods | 22 | major methods journal |
| Nature Genetics | 15 | major genetics journal |
| Nature Biomedical Engineering | 11 | major imaging/engineering journal |
| Nature Medicine | 2 | major clinical journal |
| Nature Communications | 38 | current-JIF>=10 multidisciplinary journal with official review files |

The primary strata are imaging AI 30, spatial 34, digital pathology 9, multi-omics 8,
perturbation 4, imaging–mechanism 6, single-cell 7, radiomics 1 and bulk RNA 1. A primary stratum
is an indexing device, not the only modality in a paper. In particular, the two one-paper strata
must not be treated as frequency estimates for radiomics or bulk-RNA reviewing.

The [2025 official Nature Portfolio metrics](https://www.nature.com/nature-portfolio/about-journals/journal-metrics)
are: Nature 56.1, Nature Medicine 52.5,
Nature Methods 28.3, Nature Genetics 25.5, Nature Biomedical Engineering 26.3 and Nature
Communications 18.1. The frozen corpus now has no historical-impact exception: every record is
from Nature, a Nature specialist journal, or Nature Communications with a current official JIF
above 10. Six former Cell Systems exception records were replaced only after the official article
page and full reviewer-report/author-response PDF for each replacement had been downloaded,
hashed and page-audited.

Acceptance, publication and availability of a full public review file are deliberate eligibility
criteria for this use, not a defect in the evidence source. They make it possible to reconstruct a
real reviewer concern, the author's actual action and the documented closure evidence. Therefore,
use these records directly for qualitative review, writing, revision and mentoring lessons; do not
prepend a generic “selection bias” disclaimer to ordinary case-guided advice.

Apply a denominator boundary only when the question changes from lesson extraction to population
estimation or causal attribution. Because the corpus has neither all submitted manuscripts nor a
rejected-manuscript comparison set, it cannot estimate concern prevalence across all submissions,
identify general causes of rejection, calculate acceptance probability, recover confidential
editor/reviewer discussion, or prove that a published paper has no defect. Nature states that its
public files may exclude confidential discussion in its
[peer-review policy](https://www.nature.com/nature/editorial-policies/peer-review), and its
[editorial criteria](https://www.nature.com/nature/for-authors/editorial-criteria-and-processes)
require point-by-point responses while allowing editors to decide which requests govern revision.

Tag every extracted instruction as one of three evidence types:

1. **Formal journal requirement** — supported by the current official author or editorial guidance.
2. **Recurrent empirical pattern** — observed across several page-audited reviewer–author exchanges.
3. **Case-derived example** — a useful concern–action–closure sequence from one paper.

The latter two are legitimate Skill evidence, but they must not be rewritten as universal journal
requirements. Conversely, their publication-conditioned origin is not a reason to discard them as
practical experience.

The dated post-publication screen found no targeted official notice signal for 97 records, linked
author corrections for TPR055 and TPR083, and an Editor's Note for TPR059. The TPR059 note states that
concerns were raised about data reliability and that an investigation was ongoing; therefore, use it
only as an example of reviewer/response structure while flagging the live reliability concern. A
`NO_NOTICE_SIGNAL_FOUND` result is a one-time metadata/page screen, not proof that undisclosed or
future concerns do not exist.

## What reviewers repeatedly stress-tested

The primary counts below use versioned canonical concern families, not the 59 source-specific raw
codes. One paper can enter several families, so counts overlap. The auditable one-to-one crosswalk is
[ontology v1.0.0](transparent-peer-review-concern-ontology-v1.tsv); raw codes remain in the row-level
corpus for provenance and fine-grained examples, not as a supposedly synonym-free taxonomy.

| Canonical concern family (v1.0.0) | Papers | Representative raw signals | The question the skill must ask |
|---|---:|---|---|
| COMPARATOR_CONTROL_ABLATION | 68 | benchmark/comparator fairness, controls, component or modality ablation | What is the nearest credible baseline, is it evaluated on matched data/splits/tuning, and which component creates the gain? |
| EXTERNAL_VALIDATION_ROBUSTNESS | 60 | external validation, generalizability/OOD, robustness, failure analysis | What object was frozen, what distribution changed, and does the result transport beyond the development setting? |
| CONTRIBUTION_CLAIM_CALIBRATION | 44 | novelty/contribution, claim calibration/scope, reporting or figure clarity | Does each title/abstract/result/discussion claim stay within the actual design, endpoint and validation boundary? |
| STATISTICAL_INFERENCE_CONFOUNDING | 44 | statistical rigor/inference, multiplicity, batch/missingness, subgroup fairness | What is the biological independent unit, how is hierarchy handled, and are uncertainty, confounding, multiplicity and sensitivity results shown? |
| REPRODUCIBILITY_OPENNESS | 40 | methods/model transparency, data/code availability, reconstructability | Can another team reconstruct the cohort, split, assay, model and analysis from versioned artifacts and exact methods? |
| MULTIOMICS_ALIGNMENT_ANNOTATION | 39 | multi-omics integration, multiscale alignment, cell annotation, interaction inference | Are labels, programs and cross-modal links measured, inferred or generated, and what alternative explanation remains viable? |
| MECHANISM_FUNCTION_PERTURBATION | 33 | mechanism/causality, functional/orthogonal validation, perturbation/rescue, trajectory/time | Does the evidence discriminate the proposed mechanism from alternatives through target engagement, controls, rescue or an explicit claim reduction? |
| COHORT_LABEL_UNIT_LEAKAGE | 35 | provenance, sample size/power, replication unit, leakage, reference labels/readers | What is truly independent, where do labels come from, and are cohort flow and splits leakage-safe? |
| MEASUREMENT_QC_SPATIAL_TRUTH | 34 | assay/image QC, spatial resolution/segmentation, specificity, ground truth | Who or what defines truth, at what physical resolution and mapping error, and do preprocessing/QC choices change the conclusion? |
| CLINICAL_ETHICS_FEASIBILITY | 16 | clinical workflow/utility, ethics/privacy, feasibility boundaries | Is the claimed use evaluated at its decision point with burden, risk and feasibility visible? |
| INTERPRETABILITY_ALTERNATIVES | 13 | interpretability, alternative explanation, model error | Is an attribution stable and decision-relevant, and has a technical or biological alternative been tested? |

Do not mechanically request every item. Start from the paper's material claims and activate only the
dimensions that could change a conclusion, evidence tier, use case or reproducibility judgment.

## Reviewer-first chain for a manuscript

1. **Reconstruct the contribution.** Write one sentence each for the object, comparator, delta and
   intended use. If the delta disappears against the nearest baseline, novelty rhetoric cannot rescue it.
2. **Freeze the evidence topology.** Record cohort intersections, patient/donor/lesion/region/cell
   hierarchy, split timing, sample-to-image mapping, interventions and external references.
3. **Test measurement validity.** Audit acquisition, segmentation, assay QC, labels, ground truth,
   batch effects and missingness before interpreting downstream biology or performance.
4. **Test identification and incremental value.** Require applicable controls, fair baselines,
   ablations and negative controls that isolate the claimed source of value.
5. **Test transport and robustness.** Distinguish internal resampling, temporal validation, external
   site/platform/population validation and true prospective evaluation. State what remained frozen.
6. **Test biological attribution.** Enumerate at least two biological alternatives and one technical
   or sampling alternative. Association, localization, perturbation and rescue support different ceilings.
7. **Audit statistics and uncertainty.** Use the biological unit; report effect size/interval and
   assumption/sensitivity results; do not substitute cells, spots, tiles or folds for independent samples.
8. **Audit reproducibility.** Verify deposited objects rather than promises: accession, code/model,
   versions, preprocessing, splits and usable restrictions.
9. **Audit claim placement.** Follow every material claim across title, abstract, Results, figures,
   Discussion and supplement; remove drift and unsupported generalization.
10. **Write constructive findings.** For each decision-bearing issue give the evidence anchor,
    governing criterion, consequence, minimum feasible repair, optional stronger route,
    cost/trade-off, allowed wording now and closure evidence.

## Scope adapters: what to guide, review and write

| Scope | Reviewer stress test | Minimum defensible repair | Writing consequence | Corpus anchors |
|---|---|---|---|---|
| Imaging AI | patient-level leakage; label quality; same-data baseline; calibration; site/scanner/OOD transport; actual workflow endpoint | correct split/label audit, matched comparator and ablation, uncertainty and bounded validation statement | distinguish retrospective discrimination from prospective utility; name validation type and frozen object | TPR001, TPR003, TPR004 |
| Radiomics | segmentation and preprocessing stability; feature reduction inside resampling; clinical baseline; external validation; interpretability ceiling | locked IBSI-aware pipeline, nested feature selection, clinical comparator, independent validation or discovery-only wording | never turn feature names/SHAP into mechanism; report feature provenance and stability | TPR021; interpret cautiously because this stratum has one primary paper |
| Digital pathology | patient/slide/tile hierarchy; staining/lab shift; hallucination/artifact; reference standard; workflow value | patient-separated validation, artifact/failure audit, matched pathology baseline and inspectable output | report the real inference unit and pathology adjudication; separate visual plausibility from biological truth | TPR002, TPR011, TPR025 |
| Bulk RNA | donor-level replication; composition/batch; differential model and multiplicity; pathway over-interpretation; external cell reference role | sample-level model/QC, sensitivity to composition, calibrated pathway language and targeted validation of a central node | deconvolution or atlas mapping is an estimate, not newly measured cells; pathways nominate mechanisms | TPR088, TPR095, TPR096; primary-stratum frequency is not generalizable |
| Single-cell | donor versus cell unit; annotation validity; batch integration; rare-state support; trajectory/communication inference | donor-aware models, marker/reference/orthogonal annotation, sensitivity across integration choices and bounded trajectory language | state whether identities are observed, transferred or predicted; pseudotime is not time and communication scores are not signaling events | TPR055, TPR062, TPR063, TPR097, TPR100 |
| Spatial | physical resolution; segmentation/registration; spot mixture; spatial null; cross-section/donor replication; inspectability | report resolution/error, patient-aware spatial statistics, null/sensitivity analysis, orthogonal staining or explicit proof-of-principle boundary | distinguish co-location, neighbourhood association, direction and causality; write single-case findings as hypothesis generating | TPR046, TPR047, TPR048, TPR098, TPR099 |
| Multi-omics | blockwise QC; sample intersection; integration baseline; modality ablation; latent-factor meaning; incremental value | compare unimodal/paired blocks under matched units, perturb integration choices and validate the claimed cross-modal bridge | a latent factor is derived; describe association before mechanism and identify which modality adds value | TPR051, TPR061, TPR065, TPR095, TPR096 |
| Perturbation | assignment/efficiency; dose-time; target engagement; off-target controls; rescue; generalization beyond one context | verify perturbation and controls, add discriminating functional evidence, or explain infeasibility and lower the causal claim | predicted perturbation is not intervention; negative or incomplete rescue changes the mechanism ceiling and must be reported | TPR057, TPR070, TPR086 |
| Imaging–mechanism | matched n; image–sample–time bridge; spatial scale; generated modality status; fusion ablation; biological alternatives | validate both sides and the bridge, quantify mapping error, compare unimodal blocks and add orthogonal/functional evidence or a bounded association claim | explicitly label measured versus generated biology; do not let outcome gain or saliency substitute for mechanism | TPR007, TPR020, TPR030, TPR095 |

## Request triage and constructive advice

The corpus was curated to one decisive request class per paper: 67 manuscript-grounded defects,
24 clarification-needed items, 5 reviewer preferences, 4 optional strengthening requests and 0
scope-contested/infeasible request. These are analyst classifications for this evidence map, not
publisher labels and not estimates of all reviewer comments.

For review or mentoring, classify before recommending work:

| Class | Reviewer output | Mentor output |
|---|---|---|
| Manuscript-grounded defect | identify the failed criterion and consequence; require the minimum repair or claim reduction | show the nearest executable analysis/experiment, prerequisites, stopping rule and wording allowed now |
| Clarification needed | specify the missing reconstructability or ambiguity; do not demand new data by default | give the exact Methods, Results, legend or availability statement that would expose the evidence |
| Optional strengthening | label it optional and separate it from the publication-bearing defect | explain expected information gain, cost and what decision it could change |
| Reviewer preference | test whether the current valid method answers the estimand; request sensitivity rather than ritual replacement | compare alternatives and preserve a defensible original method when conclusions are robust |
| Scope-contested/infeasible | state what cannot be inferred, then accept a reasoned alternative only if the claim is narrowed | propose the nearest interpretable control or triangulation and make residual uncertainty explicit |

Every finding should end in a verifiable closure condition. “Add more validation” is not sufficient;
name the data unit, comparator/intervention, result needed, manuscript surface and claim consequence.

## Writing chain derived from reviewer scrutiny

Use this after the scientific claim ledger is frozen:

`claim -> evidence object -> inferential unit -> comparator/alternative -> result with uncertainty ->
scope boundary -> target section -> reviewer stress test -> closure-ready location`

- **Title and abstract:** contain only the contribution and claim level that survived validation;
  remove “generalizable”, “mechanistic”, “causal”, “clinical” or “foundation” when their governing
  evidence is absent.
- **Introduction:** define the unmet knowledge or decision problem and nearest prior baseline; novelty
  is the defensible delta, not a list of technologies.
- **Methods:** make cohort/sample flow, hierarchy, splits, QC, mapping, comparator eligibility,
  model/assay versions and statistics reconstructable.
- **Results:** use the shortest sufficient chain: primary estimate -> uncertainty -> applicable
  comparator/ablation -> sensitivity/validation -> bounded interpretation. Do not hide the key repair
  only in the supplement.
- **Figures and legends:** expose independent n, units, conditions, uncertainty, statistical test and
  links to source data; visual examples do not replace distributional evidence.
- **Discussion:** distinguish what was observed, derived, predicted and perturbed; address serious
  alternatives; state transport, measurement and causal limits next to the affected conclusion.
- **Supplement and availability:** hold reconstructive detail and secondary sensitivity work, while
  the main text retains the evidence necessary to understand the headline claim.

Before prose polishing, run five material-claim questions: contribution, identification, attribution,
transport and traceability. A failed question returns the claim to the scientific ledger; it is not a
language-editing problem.

## Revision and response-letter closure

The coded closure states are: 32 experiment-or-analysis added, 31 analysis-or-evidence added,
24 text-or-claim revised, 2 author-response documented, 2 partially addressed, 4 reviewer confirmed,
1 evidence-based pushback
and 4 declined with an explicit boundary. This shows that public author responses frequently combine
new work with reporting and scope calibration; it does **not** mean that every request requires a new
experiment.

For response-writing analysis only, assigning one dominant architecture per paper yields 49
accept-and-repair, 24 clarify/rewrite, 22 partially accept and 5 evidence-based contest/infeasibility
routes. This is a forced local classification of mixed responses, not a publisher field or an
acceptance-probability model.

Use one stable chain for each atomic comment:

`comment -> request class -> author decision -> rationale -> action/method -> actual result/evidence ->
exact revised location -> residual limitation -> closure status`

An author may accept, partially accept, contest or be unable to perform a request. A defensible
pushback supplies the governing criterion, feasibility or interpretability reason, nearest alternative
evidence and a corresponding claim reduction. Courtesy is useful but never substitutes for the
method, result and location. A response is still pending if it says “we performed” without reporting
what happened or if its location cannot be independently found.

For the dedicated drafting and verification workflow, hand the frozen issue/claim ledger to
`radiology-response`; do not let that skill silently change the scientific verdict.

## Provenance and update boundary

- Canonical row-level map: [transparent-peer-review-corpus-2024-2026.tsv](transparent-peer-review-corpus-2024-2026.tsv).
- Search by `record_id`, DOI, stratum or concern code; do not load all rows merely to answer one case.
- Public files were downloaded, hashed and text-extracted; the corpus records page locators and the
  extraction method. Page-level sampling and post-publication-status screening are separate audits.
- Recompute counts whenever the corpus changes. Never carry these counts into a new time window or
  journal set without re-screening.
