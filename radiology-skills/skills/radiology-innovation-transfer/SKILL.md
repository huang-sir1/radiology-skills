---
name: radiology-innovation-transfer
description: "Assess disclosure, prior-art handoff, rights and transfer readiness; not patentability, FTO or legal advice."
---

# Radiology Innovation Transfer

Use this skill to organize research assets for responsible transfer from an imaging laboratory to a
technology-transfer, development or partnership decision. It owns invention-disclosure preparation,
patent-landscape research framing, readiness evidence, value hypotheses, rights/dependency mapping,
non-confidential summaries and diligence handoffs. It does not give patentability, freedom-to-operate,
ownership, inventorship, regulatory, quality-system, contracting or investment advice.

## Non-negotiable boundaries

- **Protect before publicizing.** Record prior/public disclosure dates, planned abstracts/papers,
  presentations, repositories, demonstrations and partner conversations. If potentially protectable
  confidential information has not been reviewed by the institutional TTO/IP owner, return
  `STOP_PUBLIC_DISCLOSURE`; prepare only a non-public disclosure packet.
- **Landscape is not a legal opinion.** A patent landscape describes search scope, patent families,
  classifications, assignees, claims/topics and trends. It is not a patentability, validity,
  inventorship, ownership or freedom-to-operate (FTO) opinion. Preliminary searches are incomplete.
- **Maturity axes remain separate.** TRL, MRL, scientific validity, clinical validity/validation, clinical
  utility, regulatory status, quality-system readiness, interoperability and commercial adoption are
  not interchangeable. Use evidence-backed exit criteria for each axis.
- **Market interest is not adoption.** Interviews, letters, clicks, citations, pilots and investor interest
  are different signals. None alone proves willingness to pay, procurement, reimbursement, sustained
  use or patient benefit.
- **Rights before value claims.** Map employment/sponsor obligations, foreground/background IP,
  software and model licenses, training/validation data rights, annotation rights, consent/governance,
  open-source obligations, vendor dependencies and collaboration agreements. Do not infer ownership.
- **Current facts are live.** Patent status, legal rules, assignees, licensing terms, regulatory
  classification, reimbursement, competitors, prices and market size require
  `LIVE_VERIFICATION_REQUIRED` with jurisdiction, source and access date.
- **No confidential fabrication.** Never invent dates, contributors, disclosures, performance,
  customers, costs, regulatory status, patent families or market evidence.

## Input passport

Use [innovation-disclosure-passport.md](templates/innovation-disclosure-passport.md) to record:

- asset/invention version, concise problem/solution and intended use;
- contributors, affiliations, employment, funding, sponsor and collaboration context;
- conception/development evidence, dated records and public/planned disclosures;
- code, algorithms, model weights, data, labels/masks, documentation, hardware and know-how;
- scientific/technical evidence, comparator, failure modes and unresolved reproduction;
- TRL/MRL and separate clinical, regulatory, quality, interoperability and deployment states;
- third-party/open-source/data/model licenses and access/consent/governance constraints;
- prior-art/landscape objective, concepts, synonyms, CPC/IPC classes, jurisdictions and dates;
- target users, workflow, payer/procurer, alternatives, benefits, burdens and adoption assumptions;
- confidentiality tier, authorized recipients and institutional TTO/legal contacts.

Do not send confidential material to an external search, model, partner or public tool unless the user
has authority and the channel is approved for that material.

## Route by mode

| Need | Mode | Main output |
|---|---|---|
| Prepare an institutional invention disclosure | `disclosure-triage` | evidence-backed disclosure passport, contributor/dependency questions and TTO handoff |
| Map prior art and patent activity | `patent-landscape` | reproducible search protocol, family-level landscape and legal-opinion boundary |
| Assess technical/manufacturing maturity | `readiness-assessment` | evidence/exit-criteria matrix across TRL, MRL and separate medical-product axes |
| Test clinical/customer value assumptions | `value-proposition` | user/workflow/problem/alternative/benefit hypothesis and evidence gaps |
| Map IP, data, model, partnership or license constraints | `rights-and-partnership` | dependency/rights matrix and questions for authorized owners |
| Prepare safe external-facing material | `nonconfidential-summary` | reviewed non-confidential problem/solution/evidence/status summary |
| Prepare a diligence or transfer decision | `diligence-handoff` | claim-source evidence map, red flags, open questions and TTO/regulatory/quality handoffs |

Read [transfer-modes-and-evidence-gates.md](references/transfer-modes-and-evidence-gates.md) for
readiness/value decisions and [patent-readiness-and-diligence.md](references/patent-readiness-and-diligence.md)
for patent and diligence controls. Consult [source-registry.md](references/source-registry.md) and
recheck every dynamic source.

## STOP gates

- `STOP_PUBLIC_DISCLOSURE`: protectable/confidential material could be released before TTO/IP review;
- `STOP_CONFIDENTIAL_CHANNEL`: proposed tool, repository, email or partner channel is not approved;
- `STOP_RIGHTS`: material data/code/model/contract rights or sponsor obligations are unresolved;
- `STOP_IDENTITY`: contributor, inventorship or ownership facts are disputed or missing;
- `STOP_EVIDENCE`: claimed performance/readiness/value lacks a source artifact and exit criterion;
- `STOP_LEGAL_OPINION`: user requests patentability, validity, FTO, ownership or contract advice;
- `STOP_REGULATED_CLAIM`: medical-device, clinical, quality or marketing claims lack qualified review;
- `STOP_MARKET_FACT`: current competitor, price, market-size, reimbursement or deal fact is unverified;
- `STOP_PHI`: patient/image data, DICOM headers, burned-in text or linked artifacts may expose PHI.

STOP blocks the unsafe release or conclusion, not a bounded internal gap analysis.

## Radiology-specific diligence

- Define intended input/output, modality, anatomy, acquisition/reconstruction, DICOM objects,
  PACS/RIS/worklist integration, latency, failure/fallback and human oversight.
- Separate algorithm/model IP from training data, labels/masks, pretrained weights, third-party code,
  scanner/vendor components, deployment stack and tacit clinical/engineering know-how.
- Trace dataset permissions across centers, consent/waiver, data-use agreements, de-identification,
  secondary use, commercial use, cross-border transfer and model/derived-artifact clauses.
- Preserve measurement validity: protocol/scanner shift, QIBA/phantom/test-retest evidence,
  reference-standard quality and external/local validation remain scientific gates.
- Distinguish a research prototype from a maintainable product: cybersecurity, logging, versioning,
  monitoring, update/change control, service support and rollback require owners and evidence.
- A radiology AI model with high AUC or a prospective pilot is not automatically patentable,
  regulatory-authorized, reimbursable, interoperable, manufacturable or adoptable.

## Workflow and output contract

1. Freeze the passport, confidentiality tier and decision being supported.
2. Build a claim-source ledger inside [diligence-evidence-map.md](templates/diligence-evidence-map.md):
   claim, exact artifact, status, owner, date, restrictions and unresolved verification.
3. Choose the mode. Search patent literature at family/claim/classification level where authorized;
   include non-patent literature and record query/date/database/coverage.
4. Score no maturity level without evidence and explicit exit criteria. Record the chosen framework
   and any medical-imaging adaptation.
5. Separate evidence from hypotheses in the value proposition. Test workflow burden, alternative,
   decision maker, buyer/payer, resource effect and adoption barrier.
6. Run confidentiality, IP/rights, scientific, clinical, regulatory/quality, interoperability,
   operational and market gates independently.
7. For external material use [nonconfidential-summary.md](templates/nonconfidential-summary.md) and
   obtain the authorized TTO/legal/communications release decision.

Return `Decision and scope`, `Disclosure passport`, `Evidence/claim map`, `Landscape or readiness
method`, `Rights/dependency matrix`, `Value hypotheses`, `Red flags and STOP ledger`, `Qualified-owner
handoffs`, and `Decision status`.

Decision status is `INTERNAL_TRIAGE`, `READY_FOR_TTO_REVIEW`, `READY_FOR_QUALIFIED_DILIGENCE`,
`READY_FOR_AUTHORIZED_NONCONFIDENTIAL_USE`, or `STOP`—never “patentable”, “FTO clear” or “investment ready”.

## Handoffs and non-ownership

- Patentability, FTO, validity, inventorship, ownership, filing and contracts → institutional TTO and
  qualified patent/legal counsel.
- Intended use, clinical validation/utility, human factors and deployment → `radiology-translation`;
  formal regulatory and QMS decisions → qualified regulatory/quality owners.
- Imaging acquisition/measurement → `radiology-acquisition-qc`; disease pathway →
  `radiology-clinical-domain`; data/consent/governance → `radiology-data` / `radiology-ethics`.
- Underlying study design/statistics → `radiology-design` / `radiology-stats`; grant proposal →
  `radiology-grant`; manuscript → `radiology-writing`.
- Public adaptation of an authorized non-confidential source → `radiology-dissemination`; this skill
  prepares the source but does not publish or market it.
