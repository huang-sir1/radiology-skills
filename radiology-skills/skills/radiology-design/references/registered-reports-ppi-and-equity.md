# Registered Reports, patient/public involvement and equity in imaging design

Use this reference when the design may enter a Registered Reports route, when patients/public or
clinical stakeholders shape the study, or when representativeness and access could change the
estimand, workflow or harm balance.

## 1. Keep four activities distinct

| Activity | Primary purpose | What it does not establish |
|---|---|---|
| clinical-trial registration | public trial identity and required results-reporting route | protocol quality, ethics approval or publication acceptance |
| preregistration | time-stamped question/design/analysis lock | peer review, journal acceptance or protocol adherence |
| Registered Report | journal Stage 1 peer review before outcomes and possible in-principle acceptance (IPA) | ethics/funding approval, correct results or unconditional final publication |
| protocol publication | citable protocol report | registration, IPA or prospective lock unless those separately occurred |

A Registered Report route is available only when the target journal/article type currently supports
it. Verify the journal policy and freeze `venue | article type | Stage 1 requirements | policy URL |
version/date | accessed date`. Use `JOURNAL_ROUTE_UNVERIFIED` until checked.

## 2. Registered Report workflow

1. Freeze question, estimand, hypotheses, sampling, image-acquisition/accepted-series gate,
   reference standard, exclusions, sample-size rationale, primary analysis, stopping rule, quality
   checks, protected-test policy and interpretation rules before outcome inspection.
2. Submit a Stage 1 manuscript only under the verified venue contract. Record editorial/reviewer
   conditions as immutable commitments or explicit amendments.
3. Track status as `NOT_APPLICABLE`, `JOURNAL_ROUTE_UNVERIFIED`, `STAGE1_DRAFT`,
   `STAGE1_SUBMITTED`, `IPA_GRANTED`, `IPA_DECLINED`, `WITHDRAWN` or `STAGE2_COMPLETE`.
4. After IPA, bind protocol version, approved deviations and quality-assurance conditions. Do not
   optimize the confirmatory analysis after viewing outcomes.
5. At Stage 2, report all registered outcomes and deviations. Null/negative results do not revoke
   the scientific obligation to report; venue quality/adherence/reporting conditions still apply.

The Center for Open Science describes qualifying Registered Reports as peer-reviewed before outcomes,
with IPA not revoked because results are unfavorable, but potentially affected by quality assurance,
failure to follow the registered protocol or unresolvable reporting problems. The current journal
policy remains authoritative for a real submission.

## 3. Separate involvement, participation and engagement

- **PPI/involvement:** patients/public work *with* the team on priorities, design, interpretation or
  dissemination; they are not necessarily research participants.
- **Participation:** people provide research data or undergo study procedures under ethics/consent.
- **Engagement/dissemination:** information about research is communicated to an audience.

Do not claim PPI from participant recruitment, a one-way information session or investigator
assumptions. If no involvement occurred, say so and record the consequence instead of inventing it.

## 4. PPI and stakeholder decision ledger

For each participant group record:

`group and whom represented | recruitment/selection | diversity/representation limits | project
stage | decision question | information supplied | decision authority | compensation/access support |
input | team response | study change/no-change rationale | residual disagreement | reporting owner`.

Include patients/public, radiologists, technologists, referring clinicians, nurses/allied health,
PACS/IT/clinical engineering, statisticians/methodologists, privacy/governance and implementation
owners as applicable. Consultation does not transfer formal safety, regulatory or ethics authority.

## 5. Imaging-specific questions that can change the design

- scan time, positioning, radiation, contrast/tracer, repeat imaging and incidental findings;
- acceptability of image sharing, defacing/de-identification and controlled access;
- clinically meaningful outcomes and horizons rather than convenient labels;
- false-positive/false-negative, delayed diagnosis, downstream testing and inequitable access harms;
- threshold-to-action choices and how uncertainty/abstention are communicated;
- disability, language, digital access, referral pathway, scanner/vendor/site and cost barriers;
- plain-language return of aggregate results and post-study communication.

Freeze an equity estimand where a subgroup/access contrast is decision-bearing: target population,
actual sample, intersectional groups, measurement/reference-standard comparability, missingness,
uncertainty, minimum acceptable performance/harm criterion and action if it fails. A post hoc subgroup
dashboard does not repair an unrepresentative design.

## 6. Stop gates and output

Return `registration-route matrix -> Registered Report status/commitments -> PPI/stakeholder ledger ->
equity and access estimands -> imaging burden/harm decisions -> changes to protocol/SAP -> unresolved
representation/authority -> claim ceiling`.

Stop a Registered Report readiness claim when venue support is unverified, outcomes/protected test were
already examined without disclosure, Stage 1 commitments are unavailable, or material deviations are
hidden. Stop an equity or PPI adequacy claim when the represented groups, decision authority or impact
cannot be evidenced.

## Primary and official sources

- Center for Open Science. [Registered Reports](https://www.cos.io/initiatives/registered-reports)
  (verified 2026-08-23; framework and qualifying features, not a substitute for venue policy).
- OSF. [Registrations](https://help.osf.io/article/330-welcome-to-registrations) (verify platform
  workflow at use).
- SPIRIT–CONSORT Group. [Patient and public involvement](https://www.consort-spirit.org/item11-patient-publicinvolvement)
  (verify current checklist wording at protocol/report freeze).
- World Medical Association. [Declaration of Helsinki, 2024](https://www.wma.net/policies-post/wma-declaration-of-helsinki/).
- EQUATOR. [GRIPP2 reporting checklists](https://www.equator-network.org/reporting-guidelines/gripp2-reporting-checklists-tools-to-improve-reporting-of-patient-and-public-involvement-in-research/).

`radiology-ethics` retains participant rights/authorization; `radiology-research-integrity` retains
selective-reporting and deviation-integrity review; `radiology-consensus-guideline` owns formal panel
recommendations. This design reference owns study-question, estimand and protocol changes caused by
involvement/equity evidence.
