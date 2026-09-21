# NSFC 2024–2026 change map and conflict gates

Read this for a live NSFC application, a year-over-year comparison, or any advice that could affect
administrative acceptance. This is an operational map, not a substitute for the named cycle's live
guide, programme instructions or electronic form.

## Current-year lock

Before declaring a requirement or readiness state, record all six fields:

`application year | programme/type and subtype | science division/office | year-bound application
code candidate | research attribute | special call/clinical track/direction`

Also lock the applicant/host configuration and live form version in the grant call passport. If a
field is unknown, return `CALL_VERSION_UNRESOLVED` or `ADMIN_NOT_ASSESSABLE`; do not present a
historical rule as current.

## Authority and conflict order

Use this default hierarchy:

1. governing law and the current Regulations on the National Natural Science Fund;
2. current annual guide, programme/special-call guide, annual notice, writing outline and live
   electronic form;
3. current programme management measure;
4. NSFC dynamic FAQ and science-division/office pages;
5. NSFC journal management or discipline analyses;
6. institutional research-office implementation material;
7. training or expert experience.

Specific current rules normally outrank general or historical ones. If current official sources
conflict, do **not** silently select the convenient interpretation. Record exact clauses, issue dates
and application-time applicability as `CONFLICTING`; return `ADMIN_CONDITIONAL` and request written
confirmation from the host research office or NSFC.

## Three-year operational map

| Topic | 2024 | 2025 | 2026 | Skill rule |
|---|---|---|---|---|
| Research attribute | four scientific-problem attributes simplified to free-exploration and goal-oriented basic research; General, Young and Key classified review | continued | continued; current names are General, Young C and Key | choose from the research content, never by guessed success probability |
| Governing regulation | old regulation governed the application cycle; revised regulation issued late 2024 | revised regulation effective 2025-01-01 | revised regulation and current programme measures apply | do not interpret 2024 and post-2025 acceptance grounds as identical |
| General two-miss restriction | restriction cancelled | remained cancelled | remained cancelled | application-volume comparisons across the change are not a pure competitiveness trend |
| Application body | cycle-specific legacy form | no verified 2026-style general restructuring | General and Young C only: 立项依据, 研究内容, 研究基础; body in principle no more than 30 pages | never extend the three-block/30-page snapshot to Region, Key, Young A/B or special calls |
| Talent names | Young / Excellent Young / Distinguished Young | renamed from the 2025 cycle: Distinguished Young → A, Excellent Young → B, Young → C; early guide copies may retain old names | A/B/C continues | preserve historical aliases; do not date the rename to 2026 |
| Generative AI | no match for 人工智能/生成式/大模型/AI in the searchable 12-page annual application-rules PDF | no match in the searchable 13-page annual application-rules PDF | annual application-and-completion notice explicitly sets verification, responsibility, declaration, marking and prohibition boundaries | negative searches cover only those two PDFs; do not back-project or overgeneralize |
| Collaboration agreement | before plan submission; external-transfer focus | before plan submission for covered collaboration funding | host signs/seals; no later than one month after project-plan approval; broader transfer and agreement controls | bind agreement timing, scope and signatory to the cycle |
| Clinical programme | published 2024 guide and results | published 2025 guide and results | public index, as accessed 2026-08-28, lists no 2026 application parameters | output `NOT_ESTABLISHED` for 2026 quota, amount or special outline |

The 2025 rename is corroborated by the NSFC 2025 result notice's A/B/C categories and its
2025-03-11 Medicine notice naming A as the former Distinguished Young programme. The CAS Institute
of Atmospheric Physics 2025-01-24 implementation notice records all three system aliases and warns
that early guide copies still used old names. Keep that implementation evidence distinct from the
controlling funder source; see N25-3 to N25-5 in `source-registry.md`.

## 2026 generative-AI boundary

The controlling annual source is the **2026 application and completion notice**, not the 15-page
application-rules PDF. It permits generative AI as an aid for tracking research developments and
collecting/organizing references only under human verification, applicant responsibility, truthful
declaration and required marking. It prohibits directly generated applications and unverified
generated content.

Operationalize conservatively:

- provide diagnostic questions, evidence checks, logic maps, critique, missing-item registers and
  clearly labelled alternative language;
- label application prose `AI_ASSISTED_ADVISORY — applicant must verify and rewrite`;
- require human verification of every fact and reference plus an AI-use ledger;
- never represent AI text as applicant-authored or submission-ready;
- stop requests to conceal, bypass or falsely describe AI use.

These operational safeguards are skill policy, not a funder-endorsed safe harbor. Labelling an
entire generated application advisory, or asking for a superficial rewrite, does not cure the
prohibited generation. Use bounded examples around applicant-authored content/decisions, and do
not infer a complete official whitelist of editing tasks from the notice's named examples.

Do not rewrite this as “NSFC bans all AI assistance.”

## Current official conflict: in-service postgraduate eligibility

For 2024 and 2025, the annual application rules explicitly excluded in-service master's students
from applying for the Young programme. In 2026:

- the annual application rules and the Young C management measure use the broader phrase
  `在职攻读研究生学位人员`;
- the dynamic applicant-condition FAQ describes the exception as an in-service doctoral student;
- the FAQ also warns that policies may change and it is for reference.

Therefore, do not assert either “in-service master's students are clearly eligible” or “the doctoral
limit is an uncontested hard rule.” Use:

`CONFLICTING → ADMIN_CONDITIONAL → live system check + host research-office/NSFC written
confirmation`.

Note that the Young C measure was published after the 2026 centralized application deadline; record
the issue date before using it to characterize the March application-time rule.

## Collaboration agreement change

- 2024 application rules, collaboration external-transfer section: sign before plan submission.
- 2025 application rules, collaboration funding section: for covered external transfer, sign no
  later than plan submission.
- 2026 application rules: the host is the signing party, the agreement is signed and sealed no later
  than one month after project-plan approval, and it addresses transfer, amount, timing, use, tasks
  and breach; second-level onward transfers are prohibited.

Treat this as a change in signatory, coverage, timing and control, not a one-date substitution.

## Results and probability boundary

Official centralized-result notices report received/accepted counts and funded counts for listed
programme classes at a point in time; other programme types may still be under review. Do not call
the ratio an overall NSFC success rate, infer an H27 rate, or predict an individual's outcome. The
2024–2025 clinical-programme counts describe that programme only.

## No pseudo-rules

Never promote the following to NSFC hard requirements without an exact current source:

- exactly three aims, innovation points or key scientific questions;
- four or five work packages;
- a universal number or recent-year proportion of references;
- a fixed word count for 立项依据 or a universal 30-character title limit;
- a mandatory technical-route figure or mandatory mechanism hypothesis;
- fixed AUC, Dice, ICC, event-per-variable or sample-size thresholds;
- a university's internal deadline, training slide or old funded proposal.

## Current-state horizon

As of 2026-08-28, a general 2027 annual guide and centralized application notice were not published.
Some materials bearing a 2027 label concern specific international or major-project activities and
do not establish the general cycle. State this narrowly; never claim that no 2027-labelled material
exists.

See [source-registry.md](source-registry.md) for exact sources and retrieval date.
