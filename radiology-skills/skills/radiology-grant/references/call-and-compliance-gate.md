# Funding-call intake and compliance gate

Read this for every full audit, submission-readiness request, or live eligibility/format question.
Administrative compliance is a separate outcome from scientific merit.

## 1. Build and freeze the call passport

Use `templates/grant-call-passport.md`. A passport is valid only for one named funder + mechanism +
cycle + programme/subcall + applicant/host configuration. Record:

- official call/NOFO/guideline title, identifier, cycle and status;
- applicant organization, PI role/career stage and relevant collaborators;
- eligibility, application/participation limits and overlap with active/submitted funding;
- research category/attribute, programme subtype and application code/topic;
- opening/deadline/time zone, project dates and duration;
- live form/template version, section map, page/character rules and attachment list;
- budget regime, cost categories/caps, indirect-cost treatment and required justification;
- human-subjects, animal, biosafety, privacy/security, data-sharing and other approvals;
- generative-AI, confidentiality, integrity and disclosure requirements;
- every official URL, publication/update date, retrieval timestamp, applicability and evidence state.

Create a passport ID such as `FUNDER-MECHANISM-CYCLE-PROGRAM-YYYYMMDD`; it is an identifier, not a
cryptographic proof. Any change to mechanism, cycle, form, applicant role or official notice makes
dependent compliance findings stale until reviewed.

## 2. Source hierarchy

Use the hierarchy declared by the funder. In its absence, prefer the most specific current official
authority: live call/NOFO and amendments → annual/programme guide → governing regulation/policy →
application-system instructions → institutional research-office implementation. Never treat a
university blog, commercial template, old funded proposal or social-media post as controlling.

NIH's current application page states its own hierarchy: NIH Guide policy notices take priority,
then the specific NOFO, then the general How to Apply guide. Preserve this order.

Evidence states come from `evidence-contract-and-stopping-rules.md`. If an official page is
unreachable, ambiguous or from the wrong cycle, mark the item `MISSING`, `CONFLICTING` or
`OFFICIAL_CYCLE_SNAPSHOT`; do not silently promote it to `VERIFIED_CURRENT`.

For NSFC use the fuller hierarchy and current conflicts in
`nsfc-2024-2026-change-map.md`. When an annual rule, later management measure and dynamic FAQ differ,
preserve issue dates and application-time applicability; authority hierarchy does not license an
unexplained eligibility choice.

## 3. Gate logic

| Outcome | Meaning |
|---|---|
| `ADMIN_PASS` | every applicable acceptance-critical item checked against current official evidence |
| `ADMIN_CONDITIONAL` | no known fatal defect, but named institution/funder confirmation or document remains |
| `ADMIN_FAIL` | an evidenced ineligibility, limit, deadline, missing mandatory component or prohibited practice blocks submission |
| `ADMIN_NOT_ASSESSABLE` | the call/applicant facts are too incomplete to judge |

Do not use `ADMIN_PASS` to imply scientific competitiveness, and do not downgrade a scientific idea
because a curable administrative input is absent. Report which authority or institutional office can
resolve each conditional item.

## 4. NSFC route: current authoritative anchors

### Administrative gate

The revised *Regulations on the National Natural Science Fund* (State Council Order No. 796,
effective 1 January 2025) requires applications to be based on the annual guide and makes the
applicant responsible for authenticity, completeness and legality. It separates preliminary
acceptance review from peer review. Non-acceptance grounds include applicant/participant
ineligibility, materials not conforming to the annual guide, applicable integrity/ethics bans, and
exceeding application-number limits.

The 2026 annual guide, application rules, application-and-completion notice and live system jointly
contain cycle-specific eligibility, limit-count, materials, budget, integrity, ethics/security and
application-code requirements. Before a compliance verdict lock application year, programme/type
and subtype, science division/office, year-bound candidate code, research attribute and any special
call/clinical track. The applicant chooses one of the two research attributes, and General, Young C
and Key use classified review linked to that choice. These are live-cycle rules: bind them to the
passport rather than copying them forward.

### Scientific merit gate

Article 16 of the revised regulations says experts independently judge **scientific value,
innovation, social impact and feasibility of the research plan**. They also consider the applicant
and participants' research experience, reasonableness of the funding-use plan, other support,
implementation of funded projects and need for continued support. Preserve these dimensions, but do
not manufacture an unofficial numeric weighting.

### 2026 generative-AI boundary

The official **2026 application and completion notice** states that when generative AI is used to
track research developments or collect/organize references, the applicant must manually verify
generated information and references, remain responsible for the content, truthfully declare use,
and mark it as required by national rules. It prohibits directly generated applications and
unverified generated content. The exact annual source matters: a searchable-text check found no
generative-AI term in the 2024 or 2025 annual application-rules PDFs, but that negative result covers
only those two PDFs and does not establish that every call, FAQ or system instruction was silent.

Operational rule for this skill:

1. For NSFC, default to review, diagnostic questions, evidence tables, structural coaching and
   clearly labelled alternative language.
2. Mark any suggested text `AI_ASSISTED_ADVISORY — applicant must verify and rewrite`; do not output
   a clean document represented as ready to submit.
3. Keep an AI-use ledger: task, input class, output used, human verification, author rewrite and
   disclosure/marking status.
4. If the user asks to bypass, conceal or falsely describe AI use, stop that route.

The advisory label and suggested author rewrite are this skill's workflow safeguards, not an
official NSFC safe harbor. A label, later verification or superficial rewriting does not authorize
generating a whole application. Limit alternative language to bounded examples tied to an author's
own text or decisions; preserve the applicant's substantive authorship and verify current rules for
the requested use. The notice's named assistance examples do not establish an exhaustive official
list of every permitted or prohibited editorial operation.

### 2026 application architecture

Use `nsfc-application-content-playbook.md` and `grant-architecture.md`. The current General
Program/Young C working snapshot differs from older prescriptive templates. Verify the three-part
form and principle-based 30-page limit in the live electronic template before treating them as
requirements. Never apply the snapshot to Region, Key, Young A/B or a special call without an exact
source. Do not flag the absence of an old heading as noncompliance when its scientific function is
present under the current form.

### 2026 known conflict and changed agreement timing

- In-service postgraduate eligibility for Young C is `CONFLICTING`: the annual rules and a later
  management measure use broader language, while the dynamic FAQ describes the exception as an
  in-service doctoral student. Return `ADMIN_CONDITIONAL` and obtain live system plus written
  institutional/NSFC confirmation; do not infer an in-service master's eligibility outcome.
- Collaboration-agreement controls changed across 2024–2026. The 2026 route makes the host the
  signing party and sets a latest point of one month after project-plan approval, with broader
  transfer, task and onward-transfer controls. Do not carry forward the 2024/2025 pre-submission
  timing.

## 5. NIH route: current simplified review framework

For covered research project grant activity codes with due dates on or after 25 January 2025, NIH's
official simplified framework reorganizes the five regulatory criteria into:

- **Factor 1 — Importance of the Research** (Significance + Innovation), scored 1–9;
- **Factor 2 — Rigor and Feasibility** (Approach), scored 1–9;
- **Factor 3 — Expertise and Resources** (Investigators + Environment), evaluated for sufficiency
  and specific gaps rather than given a criterion score.

All three inform the overall impact score. Factor 1 includes the importance of the gap, rationale
and rigor of the scientific background; novelty can strengthen importance but is not mandatory for
important work. Factor 2 covers unbiased/reproducible design, controls, justified sample size,
analysis/reporting, relevant biological variables and achievability/contingencies. Factor 3 asks
whether task-relevant expertise and resources are adequate, not whether the team is prestigious.

Confirm the activity code, due date, NOFO-specific criteria and current form before applying this
framework. Do not apply a 1–9 score to Factor 3 or back-convert these factors into an NSFC score.

## 6. Primary/official sources (verified 2026-08-28)

- NSFC 2026 annual guide landing page:
  https://www.nsfc.gov.cn/p1/2931/3971/3972/qy2026.html
- NSFC 2026 application rules page and official PDF:
  https://www.nsfc.gov.cn/p1/2931/3971/3974/sqgd2.html
  and https://www.nsfc.gov.cn/u/cms/www/202601/161125020ts3.pdf
- NSFC 2026 reform measures:
  https://www.nsfc.gov.cn/p1/2931/3971/3973/2026ndgjzrkxjjggjc.html
- NSFC 2026 application and completion notice, including the generative-AI boundary:
  https://www.nsfc.gov.cn/p1/3381/2824/99667.html
- NSFC 2026 application restructure notice:
  https://www.nsfc.gov.cn/p1/3381/2821/99242.html
- Revised NSFC Regulations, State Council Order No. 796:
  https://www.nsfc.gov.cn/p1/2871/2873/69510.html
- NIH simplified review framework, NOT-OD-24-010:
  https://grants.nih.gov/grants/guide/notice-files/NOT-OD-24-010.html
- NIH current Write Application guidance and authority hierarchy:
  https://grants.nih.gov/grants/how-to-apply-application-guide/format-and-write/write-your-application.htm

The year-by-year NSFC, Medicine and methodology set is maintained in `source-registry.md`. These
sources support the framework above; they do not freeze a future call. Re-open the relevant official
page for a real application and record the new retrieval timestamp.
