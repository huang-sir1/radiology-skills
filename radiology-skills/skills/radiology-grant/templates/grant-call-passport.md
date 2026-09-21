# Grant call passport

> One passport applies to one funder + mechanism + cycle + programme/subcall + applicant/host
> configuration. Do not reuse it after a material change without revalidation.

## Identity and status

- Passport ID:
- Status: `VERIFIED_CURRENT / CALL_VERSION_UNRESOLVED / STALE / CONFLICTING`
- Funder:
- Mechanism / funding opportunity identifier:
- Cycle / deadline round:
- Programme, subcall or special direction:
- Proposal/application version under review:
- Passport created/revalidated at (timezone):
- Reviewer and review mode:

## Applicant configuration

- Applicant organization / host:
- Lead/contact PI role and career stage:
- Key participating organizations and PI roles:
- Eligibility evidence and status:
- Application/participation limit calculation:
- Active/submitted/overlapping support and distinction:
- Required institutional confirmation:

## Scientific routing

- Application year:
- Programme/type and subtype:
- Science division/office:
- Research attribute/category:
- Year-bound application code candidate/topic/panel route:
- Clinical/research domain:
- Special call/clinical track/direction and status:
- Any call-specific scope exclusion:
- Special review criteria or priorities:

For NSFC, lock the application year, programme/type, science division/office, research attribute,
year-bound application code, and special-call/clinical-track applicability before a compliance
verdict. Record a justified `NOT_APPLICABLE` where appropriate; do not invent a special track.
Historical code or call parameters cannot be `VERIFIED_CURRENT`.

### NIH study/clinical-trial scope, if applicable

- Application due date and applicable NIH definition/policy version:
- Study/aim-level clinical-trial classification: `YES / NO / UNRESOLVED`, with design evidence:
- BESH applicability and due-date transition check, if relevant:
- Exact NOFO clinical-trial designation and official wording: `NOT_ALLOWED / REQUIRED / OPTIONAL / UNRESOLVED`:
- Classification-to-NOFO match and applicable component/Institute/Center restrictions:
- Human-subjects study records, trial-specific forms and other required safeguards:
- Unresolved classification question / institutional or NIH program-contact confirmation:

Foreign-organization eligibility is not study eligibility. `YES + NOT_ALLOWED`, or an application
without a trial under `REQUIRED`, fails the selected route. `OPTIONAL` allows trials but does not
require them or waive other eligibility checks. Unknown classification cannot become `ADMIN_PASS`;
bounded scientific review may continue. Use the due-date-specific BESH rule in
`references/international-grants.md`; non-trial status does not remove human-subjects obligations.

## Submission contract

| Item | Current rule | Applicability | Official evidence + update date | Retrieved at | State / unresolved action |
|---|---|---|---|---|---|
| Opening/deadline/time zone |  |  |  |  |  |
| Project start/duration |  |  |  |  |  |
| Form/template version |  |  |  |  |  |
| Required sections |  |  |  |  |  |
| Page/character/layout limits |  |  |  |  |  |
| Mandatory attachments |  |  |  |  |  |
| Budget regime/categories/caps |  |  |  |  |  |
| Human subjects/ethics |  |  |  |  |  |
| Privacy/security/data sharing |  |  |  |  |  |
| Other regulatory requirements |  |  |  |  |  |
| Generative-AI/disclosure rule |  |  |  |  |  |
| Current official-source conflicts |  |  |  |  |  |
| Collaboration-agreement timing/signatory |  |  |  |  |  |
| Submission system/institution step |  |  |  |  |  |

## Review criteria lock

| Criterion/factor | Official wording/source | Rating/score rule | Application location(s) | Applicability verified? |
|---|---|---|---|---|
|  |  |  |  |  |

Do not invent missing weights or convert criteria into another funder's rubric.

## Source ledger

| Source ID | Official title | URL | Issued/updated | Retrieved at | Applies to | Evidence state |
|---|---|---|---|---|---|---|
| S1 |  |  |  |  |  |  |

Source priority/contradiction resolution:

## Gate decision

- Administrative status: `ADMIN_PASS / ADMIN_CONDITIONAL / ADMIN_FAIL / ADMIN_NOT_ASSESSABLE`
- Acceptance-critical findings and anchors:
- Items reserved for institutional/funder confirmation:
- Scientific review permitted despite administrative uncertainty:
- Readiness statement prohibited until:

## NSFC AI-use ledger, if applicable

| AI-assisted task | Material supplied | Advisory output used? | Human verification | Applicant rewrite | Disclosure/marking status |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Any AI-suggested application language remains `AI_ASSISTED_ADVISORY — applicant must verify and
rewrite`; this passport does not make it submission-ready.
