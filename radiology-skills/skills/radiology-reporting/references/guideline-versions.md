# Guideline versions — single source of truth

Every reporting/quality/risk-of-bias guideline cited in this suite resolves here. **Other
files name the guideline; this file owns the version.** When a guideline revs, update this
table (and the routing notes in `guideline-router.md` if the stack changed) — do not scatter
version numbers across skills. Before citing any guideline in a real manuscript, re-verify
live (journal author instructions / EQUATOR / the publisher page) and update the
*Last verified* column.

Last full verification: **2026-07-25** (all rows checked against publisher/EQUATOR sources).
Targeted official-source re-verification: **2026-08-22** for STARD-AI and TRIPOD-Cluster and
**2026-08-23** for QUADAS-3/QUADAS-C; the evidence record appears below.
A targeted check does not silently re-date the other rows.

| Guideline | Current version | Canonical citation | Supersedes / notes |
|---|---|---|---|
| **CLAIM** | 2024 Update | Tejani AS, et al. *Radiol Artif Intell* 2024;6(4):e240300 | CLAIM 2020 (Mongan et al.). 2024 update = **44 items** (2020 had 42) |
| **TRIPOD+AI** | 2024 | Collins GS, et al. *BMJ* 2024;385:e078378 | TRIPOD 2015. **27 main items**; harmonised for regression AND ML/AI |
| TRIPOD+AI for Abstracts | 2024 | part of the TRIPOD+AI statement (Table 3) | no standalone "TRIPOD for Abstracts" checklist |
| **TRIPOD-LLM** | 2025 | Gallifant J, et al. *Nat Med* 2025;31:60–69 | LLM studies; 19 main / 50 sub-items (modular: 14 main / 32 sub-items apply across all study types) |
| **PROBAST+AI** | 2025 | Moons KGM, et al. *BMJ* 2025;388:e082505 | PROBAST 2019. Two parts: development (16 signalling questions) + evaluation (18); fairness embedded; regression AND AI/ML |
| **CLEAR** | 2023 | Kocak B, et al. *Insights Imaging* 2023;14:75 | radiomics reporting, **58 items**, ESR/EuSoMII-endorsed; E3 companion: CLEAR-E3 (*Eur Radiol Exp* 2024;8:72) |
| **METRICS** | 2024 | Kocak B, et al. *Insights Imaging* 2024;15:8 | radiomics methodological quality, **30 items / 9 categories**, % score bands; E3 companion: METRICS-E3 (*Insights Imaging* 2025;16:175); online tool: metricsscore.github.io |
| **RQS** | 1.0: 2017 — **2.0: 2025** | Lambin P, et al. *Eur J Cancer* 2017;72:S47 (1.0); Lambin P, et al. *Nat Rev Clin Oncol* 2025;22:831–846 (**2.0**) | 1.0 = 16 components, max 36 points. 2.0 = **42 criteria** with per-track maxima (hand-crafted **56** / deep-learning **52**), mapped onto Radiomics Readiness Levels (RRL 1–9); scoring tool: radiomics.world/rqs2. (66/61-point figures in some early reviews come from the pre-publication draft — do not use.) |
| **IBSI** | 1: 2020 — 2 (filters): 2024 | Zwanenburg A, et al. *Radiology* 2020;295:328–338 (IBSI 1, 169 features); *Radiology* 2024;310:e231319 (IBSI 2, convolutional filters) | standardisation initiative, NOT an EQUATOR reporting checklist — do not file it under "EQUATOR stack" |
| **STARD** | 2015 | Bossuyt PM, et al. *BMJ* 2015;351:h5527 | diagnostic accuracy, 30 items |
| **STARD-AI** | 2025 | Sounderajah V, et al. *Nat Med* 2025;31:3283–3289 | **40 checklist items total**; relative to STARD 2015, **4 items were modified and 14 new items added** (18 affected/new). At the main-item/subitem granularity, the publisher also describes the additions as **10 main items comprising 14 subitems**; do not mix these denominators. Covers dataset practices/partitioning, bias/fairness and subgroup performance |
| **PRISMA** | 2020 | Page MJ, et al. *BMJ* 2021;372:n71 | PRISMA 2009 |
| **PRISMA-ScR** | 2018 | Tricco AC, et al. *Ann Intern Med* 2018;169:467–473 | Scoping reviews/evidence maps; 20 essential and 2 optional items. Official PRISMA/EQUATOR pages rechecked 2026-08-22 |
| **PRISMA-S** | 2021 | Rethlefsen ML, et al. *Syst Rev* 2021;10:39 | Search-reporting extension; adjunct to the applicable PRISMA route, not a replacement |
| **PRISMA-P** | 2015 | Moher D, et al. *Syst Rev* 2015;4:1 | Protocol-whole-report checklist; official EQUATOR entry rechecked 2026-08-22 |
| **PRISMA-LSR** | 2024 | Akl EA, et al. *BMJ* 2024;387:e079183 | Living systematic review extension to PRISMA 2020; official EQUATOR entry rechecked 2026-08-22 |
| **PRISMA-COSMIN for OMIs** | 2024 | Elsman EBM, et al. *J Clin Epidemiol* 2024:111422 | Reviews of outcome measurement instruments; conditional specialist route, official EQUATOR entry rechecked 2026-08-22 |
| **PRISMA-DTA** | 2018 | Salameh JP, et al. *Syst Rev* 2018;7:100 (statement); McInnes MDF, et al. *JAMA* 2018;319:388–396 | DTA extension of PRISMA |
| **QUADAS-3** | **1.2 (2026)** | Whiting PF, Tomlinson E, Rutjes AWS, et al. *Ann Intern Med*. 2026. doi:10.7326/ANNALS-25-02104 | **Current recommended QUADAS tool.** Six phases; estimate-level assessment; Phase 5 domains are Participants, Index Test, Target Condition and Analysis. All four receive risk-of-bias judgments and the first three receive applicability judgments. Defines synthesis questions and an ideal test accuracy trial before assessment |
| **QUADAS-C** | 2021 companion tool | Yang B, Mallett S, Takwoingi Y, Davenport CF, et al. *Ann Intern Med* 2021;174:1592–1599. doi:10.7326/M21-2234 | Comparative accuracy only. Cannot be used alone; use **alongside QUADAS-3** with the adaptation described in the QUADAS-3 Explanation & Elaboration guidance. It assesses bias in within-study comparisons of two or more index tests, not indirect between-study comparisons, and it does not assess applicability |
| **QUADAS-2 (legacy)** | 2011 | Whiting PF, et al. *Ann Intern Med* 2011;155:529–536 | **Legacy/superseded by QUADAS-3.** Retain only when reconstructing or reporting a historical protocol/review that actually used the previous tool; do not select it as the current default |
| **CONSORT** | **2025** | Hopewell S, et al. co-published *BMJ* / *JAMA* / *Lancet* / *Nat Med* / *PLOS Med* 2025 (e.g. *PLOS Med* 22(4):e1004587) | CONSORT 2010. **30 items**; new open-science section. AI extension: **CONSORT-AI 2020** (*Nat Med* 2020;26:1364–1374) — still based on the 2010 wording, apply alongside |
| **SPIRIT** | **2025** | *BMJ* 2025;389:e081477 | SPIRIT 2013. Protocols of randomised trials. AI extension: **SPIRIT-AI 2020** (*Nat Med* 2020;26:1351–1363) |
| **CONSORT-AI / SPIRIT-AI** | 2020 | *Nat Med* 2020 (see above) | extensions to the 2010/2013 base versions; not yet re-based onto CONSORT/SPIRIT 2025 — use with the 2025 base and say so |
| **DECIDE-AI** | 2022 | Vasey B, et al. *Nat Med* 2022;28:924–933 | early, live clinical evaluation of AI decision support |
| **FUTURE-AI** | 2025 | Lekadir K, et al. *BMJ* 2025;388:e081554 | trustworthy/deployable AI consensus; 6 principles (Fairness, Universality, Traceability, Usability, Robustness, Explainability); 117 experts / 50 countries; 30 recommendations. Lifecycle frame, not an item checklist |
| **STROBE** | 2007 | von Elm E, et al. *Lancet* 2007;370:1453–1457 | observational studies |
| **REMARK** | 2005 | McShane LM, et al. *J Natl Cancer Inst* 2005;97:1180–1184 | tumour-marker prognostic studies |
| **AMSTAR-2** | 2017 | Shea BJ, et al. *BMJ* 2017;358:j4008 | appraisal of systematic reviews |
| **ROBIS** | 2016 | Whiting P, et al. *J Clin Epidemiol* 2016;69:225–234 | risk of bias in systematic reviews |
| **TRIPOD-Cluster** | 2023 | Debray TPA, et al. *BMJ* 2023;380:e071018 | Published standalone checklist with **19 main items** for prediction-model development/validation using clustered data (e.g. multiple datasets/centres or IPD meta-analysis); it is not the route for repeated measurements clustered within a person |
| **RIGHT** | 2017 | Chen Y, et al. *Ann Intern Med* 2017;166:128–132 | Whole-report practice-guideline reporting. EQUATOR listed RIGHT 2.0 as under development in 2026; do not treat it as final until officially released and verified |
| **AGREE II** | 2009, updated 2013 user manual | AGREE Next Steps Consortium. *AGREE II* | Guideline quality/appraisal instrument, not a reporting checklist and not a recommendation-development method |
| **ACCORD** | 2024 | Gattrell WT, et al. *PLoS Med* 2024;21:e1004326 | Reporting consensus methods in biomedicine; does not replace evidence synthesis or establish recommendation validity |
| **COREQ** | 2007 | Tong A, et al. *Int J Qual Health Care* 2007;19:349–357 | 32-item checklist for interviews/focus groups; not all qualitative designs |
| **SRQR** | 2014 | O'Brien BC, et al. *Acad Med* 2014;89:1245–1251 | Broader qualitative-research reporting standards |
| **CHEERS** | 2022 | Husereau D, et al. *BMJ* 2022;376:e067975 | Reporting health-economic evaluations; not a model-quality score or HTA/reimbursement decision. CHEERS-AI 2024 is a conditional AI-intervention extension |
| **StaRI** | 2017 | Pinnock H, et al. *BMJ* 2017;356:i6795 | Reporting implementation studies; use alongside the underlying design guideline(s), not as evidence of successful implementation |
| **GRIPP2** | 2017 | Staniszewska S, et al. *BMJ* 2017;358:j3453 | Reporting patient/public involvement; cannot create involvement that did not occur |

## Targeted verification evidence

| Guideline | Canonical publisher record | DOI | Checked | Fact reconciled |
|---|---|---|---|---|
| STARD-AI | [Nature Medicine guideline](https://www.nature.com/articles/s41591-025-03953-8) | `10.1038/s41591-025-03953-8` | 2026-08-22 | 2025 publication; 40 total checklist items; 4 modified plus 14 new items, with the added material also described as 10 main items comprising 14 subitems |
| TRIPOD-Cluster | [BMJ checklist](https://www.bmj.com/content/380/bmj-2022-071018) and [explanation/elaboration](https://www.bmj.com/content/380/bmj-2022-071058) | `10.1136/bmj-2022-071018`; `10.1136/bmj-2022-071058` | 2026-08-22 | Published 7 February 2023 in volume 380 as e071018; checklist contains 19 main items; scope and clustering boundary verified |
| QUADAS-3 | [University of Bristol QUADAS hub](https://www.bristol.ac.uk/population-health-sciences/projects/quadas/), [tool page](https://www.bristol.ac.uk/population-health-sciences/projects/quadas/quadas-3/) and [resources/latest version](https://www.bristol.ac.uk/population-health-sciences/projects/quadas/quadas-3/resources/) | `10.7326/ANNALS-25-02104`; E&E `10.7326/ANNALS-25-04943` | 2026-08-23 | Bristol identifies QUADAS-3 as the current recommended tool and v1.2 as latest; six phases, estimate-level assessment, ideal test accuracy trial, four Phase-5 domains and formal overall judgment verified |
| QUADAS-C | [University of Bristol QUADAS-C](https://www.bristol.ac.uk/population-health-sciences/projects/quadas/quadas-c/) | `10.7326/M21-2234` | 2026-08-23 | Bristol states that QUADAS-C cannot be used alone, recommends it alongside QUADAS-3 with E&E adaptation, limits it to within-study comparative accuracy, excludes indirect between-study comparisons and does not assess applicability |
| QUADAS-2 (legacy) | [University of Bristol QUADAS-2 history](https://www.bristol.ac.uk/population-health-sciences/projects/quadas/history/quadas-2/) | `10.7326/0003-4819-155-8-201110180-00009` | 2026-08-23 | Bristol explicitly marks the previous tool as superseded by QUADAS-3; retained only for historical-method fidelity |
| RIGHT / AGREE II / ACCORD | [EQUATOR RIGHT](https://www.equator-network.org/reporting-guidelines/right-statement/), [AGREE II](https://www.agreetrust.org/resource-centre/agree-ii/), [EQUATOR ACCORD](https://www.equator-network.org/reporting-guidelines/accord-accurate-consensus-reporting-document-a-reporting-guideline-for-consensus-methods-in-biomedicine/) | `10.7326/M16-1565`; `10.1371/journal.pmed.1004326` | 2026-08-23 | reporting, appraisal and consensus-method roles separated; RIGHT 2.0 remains under development rather than a current final replacement |
| COREQ / SRQR / CHEERS / StaRI / GRIPP2 | [EQUATOR reporting-guideline registry](https://www.equator-network.org/reporting-guidelines/) | see canonical rows | 2026-08-23 | current named versions and scope boundaries verified; reporting completeness explicitly separated from method quality and success |

## Maintenance rule

- A new version of any row → update this file, then grep the suite for the old version string
  and reconcile each hit (route text, examples, denominators like "31/42").
- Examples in other files that embed counts derived from a checklist (e.g. "CLAIM 31/44
  present") must use the denominator from this table.
- If a row cannot be re-verified, mark it `VERIFY_FROM_CURRENT_SOURCE` rather than deleting
  it, and say so in the audit output.
- For each targeted update, record the publisher page/DOI, access date, and the exact fact changed.
  Do not advance the “full verification” date after checking only selected rows.
