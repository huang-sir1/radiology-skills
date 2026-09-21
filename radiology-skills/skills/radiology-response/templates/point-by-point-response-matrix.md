# Point-by-Point Response Planning Matrix

Use this before drafting fluent reviewer-facing prose. Preserve the original comment order and create
one row per atomic commitment. Do not state that pending work is complete.

## 1. Revision contract

| Field | Entry |
|---|---|
| Manuscript ID, title and revision round | [AUTHOR_INPUT_NEEDED] |
| Decision type and date | [AUTHOR_INPUT_NEEDED: major/minor revision] |
| Deadline and required files | [AUTHOR_INPUT_NEEDED] |
| Audit mode | [AUTHOR_INPUT_NEEDED: working / final] |
| Study scope | [AUTHOR_INPUT_NEEDED: imaging-only / mechanism-only / imaging-mechanism / evidence-synthesis] |
| Original manuscript artifact ID/version/digest | [AUTHOR_INPUT_NEEDED] |
| Revised manuscript artifact ID/version/digest | [AUTHOR_INPUT_NEEDED] |
| Decision/review letter artifact IDs/rounds/versions/digests | [AUTHOR_INPUT_NEEDED] |
| Figures/tables/supplement/data/code inspected | [AUTHOR_INPUT_NEEDED] |
| Materials unavailable | [AUTHOR_INPUT_NEEDED or none] |
| Frozen scientific review/claim ceiling | [AUTHOR_INPUT_NEEDED: artifact/IDs or unavailable; for evidence-synthesis bind protocol/search/selection-flow/extraction/risk-of-bias-applicability/synthesis/certainty] |
| Project state digest | [AUTHOR_INPUT_NEEDED: canonical nonzero 64-character SHA-256] |
| Modality role digest | [AUTHOR_INPUT_NEEDED: canonical nonzero 64-character SHA-256] |
| Analysis lock digest | [AUTHOR_INPUT_NEEDED: 64-character SHA-256] |
| Claim registry digest | [AUTHOR_INPUT_NEEDED: 64-character SHA-256] |
| Scientific handoff digest | [AUTHOR_INPUT_NEEDED: 64-character SHA-256 / exactly not-applicable for evidence-synthesis] |
| Source scientific prereview state | [AUTHOR_INPUT_NEEDED: SCIENTIFIC_PREREVIEW_PASS / SCIENTIFIC_PREREVIEW_CONDITIONAL / SCIENTIFIC_PREREVIEW_FAIL] |
| Post-revision scientific prereview state | [AUTHOR_INPUT_NEEDED: SCIENTIFIC_PREREVIEW_PASS / SCIENTIFIC_PREREVIEW_CONDITIONAL / SCIENTIFIC_PREREVIEW_FAIL] |
| Source scientific prereview receipt digest | [AUTHOR_INPUT_NEEDED: nonzero 64-character SHA-256] |
| Post-revision scientific prereview receipt digest | [AUTHOR_INPUT_NEEDED: nonzero 64-character SHA-256] |
| Source scientific prereview receipt path | [AUTHOR_INPUT_NEEDED: exact validated JSON path] |
| Post-revision scientific prereview receipt path | [AUTHOR_INPUT_NEEDED: exact validated JSON path] |

## 2. Comment and commitment ledger

| Canonical issue ID | Source finding ID (`finding_id`) | Affected Claim IDs (`affected_claim_ids`) | Source review state (`source_review_state`) | Source occurrence ID | Parent ID | Round | Source document/version/digest + locator | Reviewer label as printed | Lineage + prior commitment IDs | Quote status | Reviewer/editor wording | Atomic commitment | Request class or N/A—NON_ACTIONABLE | Editorial obligation + editor quote/locator | Governing criterion | Author decision + authority source/approver/date | Feasibility | Action code | Required evidence | Planned locations | Closure criterion |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED: CI-#] | [AUTHOR_INPUT_NEEDED: stable upstream Finding ID] | [AUTHOR_INPUT_NEEDED: non-empty Claim ID list] | [AUTHOR_INPUT_NEEDED: VERIFIED/PARTIAL/NOT ADDRESSED/MADE WORSE/NOT VERIFIABLE] | [AUTHOR_INPUT_NEEDED: RR#-R#-# / ROUND_UNKNOWN-…] | [AUTHOR_INPUT_NEEDED: parent or —] | [AUTHOR_INPUT_NEEDED: RR# / ROUND_UNKNOWN] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED: new/continues/narrows/reopens/supersedes + IDs] | [AUTHOR_INPUT_NEEDED: exact / bounded excerpt / labelled paraphrase] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED: one verifiable request or N/A] | [AUTHOR_INPUT_NEEDED: defect / clarification / optional / preference / scope-contested / N/A—NON_ACTIONABLE] | [AUTHOR_INPUT_NEEDED: MUST_FIX/SHOULD_FIX/CONSIDER/UNKNOWN + decision/editor evidence] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED: accept / partially accept / contest / cannot address + author/email/meeting/date] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED or N/A—NO_MANUSCRIPT_CHANGE_JUSTIFIED] | [AUTHOR_INPUT_NEEDED: observable condition] |

## 3. Evidence-before-writing record

| Commitment ID | Source finding ID | Affected Claim IDs | Source review state | Evidence origin | Action/method actually completed | Result/evidence produced | Artifact ID/version/digest + locator | Verification method/verifier | Response closure state | State-change evidence | Claim consequence | Residual limitation | Response status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED: non-empty Claim ID list] | [AUTHOR_INPUT_NEEDED: VERIFIED/PARTIAL/NOT ADDRESSED/MADE WORSE/NOT VERIFIABLE] | [AUTHOR_INPUT_NEEDED: original-existing/newly-generated/newly-reported-existing/author-attested-only/no-new-work] | [AUTHOR_INPUT_NEEDED or N/A—NO_NEW_WORK] | [AUTHOR_INPUT_NEEDED: estimate/direction/finding, pending, or N/A—NO_NEW_WORK] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED: VERIFIED/PARTIAL/NOT_VERIFIED/MADE_WORSE/NOT_APPLICABLE] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED: retain/narrow/remove] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED: draftable/pending/blocked] |

## 4. Response block draft

For a commitment with new work or a manuscript change, use this order:

> **[ID] Reviewer/editor comment:** [original wording]
>
> **Response:** We [agree / partially agree / respectfully disagree / cannot complete the request]
> because [criterion-linked rationale]. We [action] using [method]. [Result/evidence with direction,
> estimate or finding]. We revised [section/page/line/figure/table/supplement] to [exact change].
> [Residual limitation and resulting claim boundary].
>

Do not put an author-self-certified closure label in the editor-facing response. Keep artifact
fulfillment in the internal verification record.

For a legitimate no-new-work route, use the applicable conditional block:

> **Response:** We [acknowledge / answer from the existing record / cross-reference CI-# /
> respectfully disagree] because [criterion-linked rationale]. The relevant existing evidence is
> [versioned artifact and locator]. [No new analysis was performed / no manuscript change was made /
> this source occurrence is answered by CI-#]. [Residual boundary, if any.]

Record method/result/location as `N/A—NO_NEW_WORK` or
`N/A—NO_MANUSCRIPT_CHANGE_JUSTIFIED`; never invent them to fit the template.

Use visible placeholders only in `working` mode. In `final` mode any unresolved placeholder forces
`NOT_READY_FOR_SUBMISSION_ASSEMBLY`.

## 5. Author decisions still required

| Decision ID | Question | Why it changes the response | Options and trade-offs | Recommended option | Deadline |
|---|---|---|---|---|---|
| [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] | [AUTHOR_INPUT_NEEDED] |
