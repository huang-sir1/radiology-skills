# Responsible-research governance routing

The pipeline registers and hands off governance artifacts; it does not become their scientific or
institutional owner.

## Required satellite artifacts for a full project

| Artifact | Unique owner | Minimum state carried in the manifest |
|---|---|---|
| team charter / RACI / decision and escalation path | `radiology-research-ops` | version, contributors, decision authority, review date, unresolved role conflict |
| prospective CRediT/authorship and contribution-change ledger | `radiology-research-integrity` | contribution evidence, ICMJE eligibility state, agreement/dispute/escalation state |
| AI-use ledger | `radiology-research-integrity` | tool/version/date, purpose, input classification/authorization, human verification, modification, disclosure location |
| integrity evidence manifest | `radiology-research-integrity` | observation/signal/allegation/finding state, preserved source digest, access chain and institutional handoff |
| DMP/DMS and amendment log | `radiology-data` | policy passport, object lifecycle, sharing/retention state, unresolved authority |
| PPI/stakeholder/equity decision ledger | `radiology-design` | representation, authority, input, decision impact, residual disagreement |
| reproducibility/replay receipt | `radiology-reproducibility` | level, exact run bundle, replay actor/environment/result/tolerance and residual boundary |

Register these as versioned artifacts in the common `artifact_manifest.csv`; do not force their
domain-specific fields into the core project-state schema. Link affected decisions and Claim IDs.
Changes to authorship/contribution, authority, cohort/use population, AI input policy, DMP, protocol,
analysis or replay evidence can stale downstream proposal, deck, manuscript, review, dissemination,
innovation-transfer and submission artifacts.

## AI and sensitive-input stop gate

Before unpublished manuscripts, PHI, controlled genomic data, confidential grant/proposal material,
patent-sensitive disclosure or restricted code/data are sent to any external AI/service, verify the
institutional policy, contract, consent/DUA, journal/funder terms and user authorization. Unknown is
`STOP_EXTERNAL_PROCESSING_UNAUTHORIZED`. Redaction or de-identification must itself be evidenced;
do not assume that removing a name makes an imaging/genomic record safe.

AI cannot be an author or evidence source. Humans remain responsible for accuracy, attribution,
permissions, confidentiality, code/results and disclosure. An AI detector creates at most an
`INTEGRITY_SIGNAL`; it does not prove misconduct.

## Team and authorship boundary

CRediT describes contribution and does not decide authorship eligibility. ICMJE authorship requires
all four criteria; funding, administration or general supervision alone is insufficient. Discuss and
revisit contribution/order early, at protocol/data/analysis/manuscript/submission/major-change gates.
The skill records disagreement and routes it to the project/institutional process; it does not impose
an author order or adjudicate a dispute.

## Sources

- ICMJE. [Defining the Role of Authors and Contributors](https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html).
- NISO. [CRediT taxonomy](https://credit.niso.org/).
- ICMJE. [Use of Artificial Intelligence in Publishing](https://www.icmje.org/recommendations/browse/artificial-intelligence/).
- National Academies. [The Science of Team Science, 2025 interactive report](https://nap.nationalacademies.org/resource/29043/interactive/).
- HHS ORI. [Guidance documents](https://ori.hhs.gov/guidance-documents).

Official sources were routed/checked 2026-08-23. Local institutional, sponsor and journal rules remain
authoritative for actual disputes, confidential processing and disclosures.
