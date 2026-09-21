# Post-publication lifecycle and staleness

Publication is a versioned event, not the end of research governance. Use this reference for
production queries, public-access deposit, data/code requests, correspondence, corrections,
retractions, living updates, dissemination updates, deployment evidence and project retirement.

## 1. Published-output passport

Freeze `work/DOI/PMID/preprint IDs | accepted/published versions and digests | publisher/current-
status URLs | official publication date | licence/copyright | funder/public-access route/status |
data/code/model repository/access | corrections/retractions/updates | responsible author/steward |
last status check | next surveillance/review date`.

Use explicit states: `PUBLISHED_CURRENT`, `UPDATE_OR_CORRECTION_PENDING`, `CORRECTED`,
`EXPRESSION_OF_CONCERN`, `RETRACTED`, `WITHDRAWN`, `SUPERSEDED`, `LIVING_UPDATE_DUE`,
`RETIRED` and `STATUS_UNVERIFIED`. Do not erase earlier versions or convert debate/new science into an
error finding.

## 2. Owner and propagation map

| Event/decision | Unique owner | Required propagation |
|---|---|---|
| error/integrity signal, correction/retraction evidence and institutional/editorial escalation | `radiology-research-integrity` | preserve evidence/version chain; no misconduct adjudication by the skill |
| citation/current-status check and corrected citation | `radiology-citation` | update claim-source status and cite current version |
| data/code/model access request, repository update, retention/destruction | `radiology-data` | authority/request/release manifest and access/closeout receipt |
| living review surveillance, update transition or retirement | `radiology-systematic-review` | new search/corpus/flow/extraction/RoB/synthesis/certainty and changed-claim ledger |
| public/patient/clinical/policy/media correction | `radiology-dissemination` | reissue/withdraw/update every audience artifact and source ledger |
| deployed intervention monitoring/change/retirement | `radiology-translation` | production/CAPA/revalidation/rollback state |
| citation/network/portfolio analysis | `radiology-bibliometrics` | time/database-normalized analysis; no quality/impact inference from counts |
| invention/public disclosure/IP milestone | `radiology-innovation-transfer` | current patent/public-disclosure/TTO handoff state |
| production-file/public-access package | `radiology-submission` | final files, accepted-manuscript/deposit and portal evidence |
| operational closeout and retained obligations | `radiology-research-ops` | owner, deadline, risk/issue and closure log |
| whole-project registry/staleness | `radiology-pipeline` | mark affected claims, proposals, decks, manuscripts, reviews and impact outputs stale |

## 3. Correction/update workflow

1. Capture the observation without changing the source artifact; freeze affected published/current
   versions, data/code/logs, Claim IDs and evidence.
2. Triage whether it is debate/new evidence, a correctable error, potentially pervasive invalidity,
   safety issue or integrity signal. Do not infer intent.
3. Route to journal/editor, institution/RIO, funder, regulator/safety owner or repository as required;
   record their authority and decision separately.
4. Publish/register/link the authorized notice/version; preserve prior versions and exact changes.
5. Propagate the status to citations, datasets/code/models, systematic-review conclusions,
   dissemination products, guideline/consensus recommendations, deployed systems and innovation
   materials. Mark dependent artifacts stale until their owner closes them.

ICMJE says honest factual errors require correction, prior versions should remain archived and newer
versions should be signposted; serious invalidating errors may require retraction. Crossmark helps
surface updates but its presence is not itself a guarantee. Journal/institutional decisions remain
authoritative.

## 4. Living-review and knowledge-retirement gate

For living evidence products predefine surveillance source/query/cadence, update trigger, new-study
deduplication, status-change/retraction check, reanalysis threshold, certainty/claim-change rule,
communication and retirement criteria. `No new study found` is a dated search result, not permanent
currency. On retirement, preserve last search/date, reason and residual evidence boundary.

## 5. Output and sources

Return `published-output passport -> current status/source/date -> event/evidence state -> authorized
decision/handoff -> affected Claim/artifact staleness -> public/data/deployment/living-update actions ->
closure/next surveillance date`.

- ICMJE. [Corrections and Version Control](https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html),
  official recommendations accessed 2026-08-23.
- Crossref. [Crossmark](https://www.crossref.org/documentation/crossmark/), status/update metadata
  documentation accessed 2026-08-23.
- NIH. [Public Access](https://grants.nih.gov/policy-and-compliance/policy-topics/public-access),
  current official overview accessed 2026-08-23.
- EQUATOR. [PRISMA-LSR record](https://www.equator-network.org/reporting-guidelines/prisma-lsr-extension/)
  (verify current source/version at each update).
