# International funding bodies (NIH / ERC / Wellcome and other cross-border routes)

**NSFC (国自然) is this skill's primary, most-developed track — see `grant-architecture.md`,
`reframe-and-innovation.md`, `feasibility-and-pitfalls.md`.** Use this file when the user is also
targeting (or considering) an international funder. The scientific-question-first, closed-loop,
honest-feasibility discipline from the main workflow **carries over unchanged** — only the section
architecture, evaluation criteria, and — critically — **who is actually eligible to apply** differ
by funder. Verify every figure below live before a real submission; funding-body rules change
often (NIH's foreign-collaboration rules changed twice in the ~10 months before this file was
written, and ERC's own proposal structure changed for the 2026 call round).

Treat all scheme facts in this file as orientation until a
`templates/grant-call-passport.md` binds the current official call, applicant/host configuration and
retrieval date. For compliance and review, `call-and-compliance-gate.md` is controlling; do not
preserve a historical section length, eligibility rule or review rubric merely because it is
written here.

Provincial natural-science funds are separate funders. Their calls do not automatically inherit
NSFC eligibility, forms, AI-use rules or limits.

## Eligibility first — read this before drafting anything

An avoidable failure is drafting a Significance/Innovation/Approach
narrative for a mechanism the applicant's institution or citizenship cannot actually access as lead
PI. Check eligibility **before** investing writing effort, the same way `radiology-design` checks
feasibility before designing a study.

| Funder / mechanism | Who can be the lead/contact PI | What this means for a China-based team |
|---|---|---|
| **NIH direct R01 application** | Eligibility is NOFO-specific. As checked 2026-09-04, **PA-25-301 Section III allows foreign organizations to apply directly**. Its restriction on foreign subawards/subcontracts does not remove this direct-applicant eligibility. Verify participating Institute/Center, project scope, registrations, foreign-organization requirements and current notices. | A China-based institution may have a direct application route where the exact NOFO permits it. Do not reject it merely because the host is outside the U.S.; do not guarantee eligibility or funding from the general rule. |
| **NIH funded international collaboration (PF5/UF5 or another designated mechanism)** | **NOT-OD-25-155** governs the new structure for covered due dates from 25 January 2026. **PA-26-002** is a PF5 call with a U.S. domestic prime, at least one domestic Research Project and at least one International Project; its first submission date is 25 April 2026. A multi-PD/PI plan applies when multiple overall PD/PIs are proposed. | A foreign team's funded component follows the call's International Project and linked-award rules. Unfunded collaborations, foreign consultants and permitted foreign components do not automatically require this mechanism. Distinguish the financial/organizational arrangement before routing. |
| **ERC Starting / Consolidator / Advanced** | The Host Institution must meet the current EU Member State/associated-country or eligible international European research-organisation rule. | Check an eligible host appointment or relocation route; PI nationality alone does not decide eligibility. |
| **ERC Synergy** | The scheme has a specific exception: **one PI per group may be hosted or engaged outside the EU or associated countries**. Check the current work programme, corresponding PI/host and all group requirements. | A mainland-China-based PI may participate through this exception without relocating. It does not make every Chinese host or the whole group automatically eligible. |
| **Wellcome Trust** (major discovery-research schemes) | The current official eligibility page lists UK, Republic of Ireland and eligible LMIC administering organizations, while explicitly excluding mainland China and India. Scheme pages announce a narrower location rule from **29 October 2026** (UK plus eligible LMIC organizations in Africa, South Asia and South-East Asia; Republic of Ireland no longer eligible). | Mainland China is not an eligible lead host under either the current or announced route. Check the exact scheme, administering organization and submission date live; other Wellcome mechanisms may differ. |

Separate direct applicant, corresponding/overall PI, component leader, collaborator and host
organization. Neither nationality nor a rule for one mechanism establishes eligibility across a
funder. Preserve viable direct and consortium routes while verifying the exact call.

### NIH clinical-trial scope gate — independent of organization eligibility

As checked 2026-09-04, **PA-25-301** is **Clinical Trial Not Allowed**, whereas
**PA-26-002** is **Clinical Trial Optional**. Foreign-organization eligibility does not establish
study eligibility. Record both checks separately in the grant call passport.

Classify each study/aim using the current NIH definition and decision tool, bound to the application
due date: human participation, prospective assignment, intervention-effect evaluation, and the
applicable health-related outcome definition. Do not classify from “prospective,” “imaging,” or
“reader study” alone; one qualifying aim can trigger the trial branch. Record `YES / NO / UNRESOLVED`
and the study-design evidence, then match the exact NOFO's trial designation:

- `NOT_ALLOWED`: a confirmed NIH-defined trial makes this application route `ADMIN_FAIL`.
- `REQUIRED`: an application without an NIH-defined trial fails this route's trial requirement.
- `OPTIONAL` (trials allowed, not required): either classification may fit; this does not waive
  scope, Institute/Center participation, organization, component or other requirements.
- Unresolved classification or rule: `ADMIN_NOT_ASSESSABLE` or `ADMIN_CONDITIONAL`, with the
  exact question for the program contact. Bounded scientific review can continue.

Keep the **BESH due-date transition** separate: NOT-OD-26-067 applies the non-trial classification
to competing applications with due dates on or after **25 May 2026**. BESH-only applications may
then use Not Allowed or Optional calls unless the call says otherwise; a separate NIH-defined trial
still requires a trial-permitting call. Earlier due dates and existing award terms must not be
retroactively reclassified. Human-subjects protections and other applicable obligations remain;
“not a clinical trial” does not mean “no human-subjects forms or ethics review.”

## NIH R01 — structure (after exact NOFO eligibility is checked)

This is the R01 architecture, whether the eligible applicant is domestic or foreign. PF5 uses
multi-component instructions and call-specific limits; do not paste the R01 section table into it.

For covered NIH research project grants with due dates on or after 25 January 2025, review uses the
simplified framework: Factor 1 Importance of the Research (Significance + Innovation, 1–9), Factor
2 Rigor and Feasibility (Approach, 1–9), and Factor 3 Expertise and Resources (sufficiency/gaps,
not a criterion score). Confirm activity-code and NOFO applicability live. The Research Strategy
headings below remain application architecture; they must not be mistaken for five separately
scored legacy criteria.

| Section | Length | Content |
|---|---|---|
| **Specific Aims** | **1 page** | Gap → objective/question or hypothesis → justified aims, expected outcomes and overall impact. Two or three aims is a writing heuristic, not a universal NIH requirement; verify exact call limits. |
| **Research Strategy** | **12 pages** total, three headed sections | **Significance** (≈立项依据: gap, importance, why now), **Innovation** (≈创新点: specific, defensible increment — same "avoid hollow superlatives" rule as `reframe-and-innovation.md`), **Approach** (≈技术路线: organized aim-by-aim, with preliminary data, methods, expected results, rigor/reproducibility, and alternative/contingency plans per aim). |
| **Rigor and reproducibility** | Within Approach | NIH explicitly scores this — scientific premise, rigorous design, biological variables (sex as a variable, etc.), authentication of key resources. This maps directly onto this suite's leakage-audit/reporting-guideline discipline (`radiology-reporting`, `radiology-stats`) — reuse it, don't rewrite it. |
| **Biosketch, budget, human subjects/vertebrate animals** | Per current NIH forms | Administrative; confirm current page/format rules live — NIH updates its application guide regularly. |

### Reframing NSFC content into NIH shape
`关键科学问题` → the question or hypothesis anchoring Specific Aims. `立项依据` → Significance.
`技术路线` (the closed loop) → Approach, but **reorganized per-aim** rather than as one continuous
narrative — NIH reviewers expect to find Aim 1's method/results/pitfalls together, not scattered.
`创新点` → Innovation. Under the current simplified framework, Importance and Rigor/Feasibility
each receive a criterion score and both inform overall impact; that does **not** imply an arithmetic
weighting. An NSFC proposal that leans hard on innovation with thin methodological detail
under-serves an NIH review.

## ERC — structure (2026 call structure; verify current cycle live)

Use the exact ERC scheme and cycle, including the Synergy host exception above. The 2026 structure
changed materially from prior years; confirm the current work programme and applicant instructions.

- **Sole evaluation criterion: excellence** — of the research project *and* of the PI (intellectual
  capacity, creativity, track record). There is no separate "impact" or "implementation" criterion
  the way many national schemes score it. Starting/Consolidator/Advanced use two evaluation steps;
  Synergy uses three, including a final interview and assessment of the group's synergy.
- **Part I (2026: 5 pages)** — current knowledge, the original scientific idea, questions,
  objectives and the **overall approach or research strategy** for achieving them. Explain the
  high-level logic that makes the question answerable. Detailed implementation and feasibility
  belong in Part II; this does not exclude the overall scientific approach from Part I.
- **Part II (2026: 7 pages for Starting/Consolidator/Advanced; 10 for Synergy)** — implementation: methodology, work plan,
  risk assessment and mitigation. This is where 技术路线-style closed-loop
  reasoning belongs, plus explicit risk/contingency per work package. The budget/resources
  justification is outside this page limit; verify its placement in the exact call template.
- **CV and track record** — assessed alongside Part I at Step 1; the PI's own publication/impact
  record carries real weight (ERC evaluates the *person* as well as the *idea*).

### Reframing NSFC content into ERC shape
The "innovation must be specific and defensible" discipline in `reframe-and-innovation.md` maps
almost directly onto ERC's "ground-breaking nature" language. For either funder, test the claimed
gap against relevant international literature (→ `radiology-frontier`, `radiology-search`),
without assuming a weaker novelty standard for a domestic scheme.
Retain the high-level research strategy in Part I, while placing detailed methodology,
implementation, resources and feasibility in Part II. Feasibility is assessed at Step 2; that
evaluation change does not remove the requirement to explain the overall approach at Step 1.

## Wellcome Trust — structure (scheme-dependent; verify current scheme and eligibility live)

Less rigidly page-limited than NIH/ERC; assessed more holistically by committee plus interview for
several schemes.

- Typical weighting (Career Development Award as an example — **confirm per scheme**): research
  proposal ≈50%, applicant's skills/experience ≈25%, research environment ≈25%.
- The "research environment" weighting has no strong analogue in NSFC's structure — it rewards a
  credible account of institutional support, mentorship, and infrastructure, which this suite's
  `feasibility-and-pitfalls.md` "team/data/ethics" feasibility evidence partially covers but should
  be expanded for a Wellcome-style application.
- Significance is framed around the research *question*, similarly to NSFC's 立项依据, but with
  more explicit narrative about the PI's leadership trajectory.
- **Confirm current eligibility for the specific scheme and the applicant's location before
  drafting** — see the eligibility table above; Wellcome schemes differ from each other and change.

## More directly reachable cross-border routes for a China-based team

Before defaulting to NIH/ERC/Wellcome as "the" international goal, these are generally more
directly accessible to a China-based PI and worth checking first (verify current terms live for
all of them — this list is orientation, not a closed set):

- **NSFC 国际（地区）合作与交流项目** — NSFC's own international collaboration line; stays inside
  the NSFC system this skill already covers in depth, while funding genuine cross-border work.
- **RGC (Hong Kong Research Grants Council)** joint schemes — several RGC schemes have mainland
  China collaboration tracks (e.g. joint research schemes with NSFC itself); a realistic bridge for
  Greater China-based collaboration.
- **Marie Skłodowska-Curie Actions (MSCA)**, distinct from ERC — several MSCA strands fund
  *mobility and collaboration* (incoming/outgoing fellowships, staff exchange) with different
  eligibility logic than ERC's host-institution requirement; worth checking case-by-case.
- **Major foundations** (e.g. Bill & Melinda Gates Foundation, Chan Zuckerberg Initiative) —
  mission-driven global-health/biomedical-AI funders whose eligibility is typically about the
  research topic and institutional capacity rather than PI nationality; terms vary by program and
  must be confirmed live.
- **Bilateral/consortium programs** (e.g. Sino-X joint research centers, Newton Fund-style
  programs where still active) — confirm current status; many bilateral science programs have
  wound down or changed since original launch and must be verified rather than assumed active.

## Output (international track)

```
Target funder/mechanism:
Eligibility check:        [PI/institution eligible as lead? co-I route needed? verified live?]
NIH trial scope, if applicable: [study classification + exact NOFO designation + match/uncertainty]
Section mapping:          [NSFC section -> funder section, per the tables above]
Reframed scientific Q:    [same one-question discipline, funder-appropriate framing]
Reframed innovation:      [same specificity discipline, calibrated to the funder's peer pool]
Feasibility evidence:     [funder-specific weighting, e.g. "research environment" for Wellcome]
待核验 (author-only):      [current page limits, forms, deadlines, eligibility — all funder sites change]
```

## Handoffs
- NSFC-specific architecture and the core reframing workflow → `grant-architecture.md` /
  `reframe-and-innovation.md` (same discipline, reused).
- Whether the underlying science is strong enough for either track → `radiology-design` /
  `radiology-frontier`.
- Verify current call deadlines, page limits, and eligibility rules live → `radiology-search`.
- This file orients; it is not a substitute for the funder's current official guidelines or the
  host institution's sponsored-programs/grants office — eligibility and forms must be confirmed
  before submission.

## Current official orientation anchors (re-open for every real call)

- NIH international-collaboration structure, NOT-OD-25-155:
  https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-155.html
- NIH direct R01 eligibility and foreign-subaward distinction, PA-25-301 Section III (checked 2026-09-04):
  https://grants.nih.gov/grants/guide/pa-files/PA-25-301.html
- NIH foreign-organization application guidance (checked 2026-09-04):
  https://grants.nih.gov/new-to-nih/information-for/foreign-grants
- NIH clinical-trial definition and decision tool (checked 2026-09-04):
  https://grants.nih.gov/policy-and-compliance/policy-topics/clinical-trials/definition
- NIH BESH classification implementation and due-date transition, NOT-OD-26-067 (checked 2026-09-04):
  https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-067.html
- PF5 PA-26-002 full announcement, official Grants.gov attachment (checked 2026-09-04):
  https://files.simpler.grants.gov/opportunities/3df028f3-f97a-4cdf-9359-1c6515d091ce/attachments/32095b88-f093-488f-aa71-1b39ce517067/PA-26-002-Full-Announcement.html
- NIH PF5 activity-code overview:
  https://grants.nih.gov/funding/activity-codes/PF5
- ERC 2026 proposal/evaluation changes:
  https://erc.europa.eu/news-events/news/changes-2026-and-2027-work-programmes
- ERC Synergy host exception and three-step evaluation (checked 2026-09-04):
  https://erc.europa.eu/apply-grant/synergy-grant
- Wellcome applicant/organization eligibility:
  https://wellcome.org/research-funding/guidance/prepare-to-apply/eligibility-information-grant-applicants
