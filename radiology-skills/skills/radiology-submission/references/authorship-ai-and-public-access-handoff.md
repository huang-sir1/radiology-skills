# Authorship, AI disclosure and public-access handoff

Use this reference during final package reconciliation. It checks whether the package carries
versioned human attestations and current policy routes; it does not decide authorship disputes,
verify institutional authority or make a funder-compliance determination.

## 1. Declaration passport

For each requirement record:

`requirement ID | authority/journal/funder | official URL | version/status/effective date | accessed |
applies/conditional/NA with rationale | responsible human | artifact/portal location | attestation |
cross-file consistency | unresolved action`.

Minimum rows:

- author list/order, ICMJE eligibility confirmation and final approval;
- CRediT roles with contributor confirmation; acknowledgments/permissions;
- corresponding-author/contact/ORCID/affiliations and author-change documentation;
- relationships/activities, COI, funding and sponsor/data-analysis/publication roles;
- AI tool/version/purpose, input authorization, human verification and disclosure locations;
- ethics/consent or waiver, trial/registration/protocol IDs as applicable;
- data/code/model availability, DMP/DMS compliance route and repository/access status;
- public-access obligation, accepted-manuscript route, timing, identifier/status and rights/licence;
- copyright, third-party image/material permissions and preprint/overlap disclosures.

CRediT describes contributions and does not determine authorship. ICMJE recommends four authorship
criteria that all authors meet; author order is a collective author-group decision, and unresolved
disputes route to the institution rather than the journal or this skill.

## 2. AI-use reconciliation

Bind the project AI-use ledger from `radiology-research-integrity` to the cover letter, manuscript
acknowledgment/Methods, figures/supplements, code/data and portal questions. ICMJE's current
recommendations say AI is not an author; humans remain responsible; authors should disclose the tool
and purpose, with writing assistance acknowledged and data collection/analysis/figure generation
described in Methods as applicable.

Return `STOP_AI_USE_UNRECONCILED` when material AI use, sensitive-input authority, tool/version,
human verification or required disclosure cannot be reconciled. Do not use an AI detector as proof
of authorship or misconduct.

## 3. Keep open-science obligations separate

| Obligation | Question | Not equivalent to |
|---|---|---|
| public access | when/how must the accepted publication become publicly accessible? | data sharing, open licence or APC payment |
| data sharing/DMP | what scientific data are managed, shared/preserved, restricted and requested? | public access to the paper |
| code/model/weights | what software/model artifacts and licences/access routes exist? | raw patient-data release |
| trial registration/results | what registry and results-reporting duty applies? | preregistration or Registered Reports |
| licence/copyright | what reuse rights exist for text, figures, data, code and third-party material? | mere online availability |

NIH snapshot verified 2026-08-23: its official page states that the 2024 Public Access Policy applies
to Author Accepted Manuscripts accepted on or after 2025-07-01, requires submission to PMC upon
acceptance, and public availability without embargo on the official publication date. Re-verify
award/manuscript applicability and the current submission route for every real package; do not apply
this to another funder or claim that it creates an open licence.

## 4. Package gate

A machine can check that declarations/attestations are present, current and cross-file consistent;
only authorized humans can confirm contributor agreement, COI completeness, sponsor independence,
funder applicability, permissions and portal attestations.

Return `STOP_DECLARATION_UNVERIFIED` for unresolved author approval/change, missing contributor/COI
attestation, undisclosed material sponsor/AI role, conflicting ethics/registration identifiers,
unsupported public-access compliance, invented repository/accession or absent permissions for reused
patient images/third-party content.

## Official sources

- ICMJE. [Authors and contributors](https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html)
  and [AI in publishing](https://www.icmje.org/recommendations/browse/artificial-intelligence/),
  official recommendations accessed 2026-08-23.
- NISO. [CRediT](https://credit.niso.org/), taxonomy/status accessed 2026-08-23.
- NIH. [Public Access](https://grants.nih.gov/policy-and-compliance/policy-topics/public-access),
  official policy overview accessed 2026-08-23.
- NIH. [Writing a DMS Plan](https://www.grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/dms/writing-dms-plan),
  current DMS format route accessed 2026-08-23.
