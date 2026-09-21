# Data lifecycle management plan for imaging research

Use this reference when the requested artifact is a funder-facing DMP/DMS plan or a living
project data-lifecycle plan. A Data Availability statement describes access at publication; it
does not replace management, preservation, cost, retention, destruction or change control.

## 1. Freeze a policy passport before drafting

Record `funder/institution/jurisdiction | award/call | policy title | official URL | policy status |
effective/due date | application/report type | accessed date | local owner`.

Use these states:

- `VERIFIED_CURRENT`: the exact official source and applicability were checked for this submission.
- `VERIFY_FROM_CURRENT_POLICY`: the source, date, award type or local overlay is unresolved.
- `NOT_APPLICABLE`: the rule was checked and does not govern this project; retain the reason.
- `STOP_POLICY_UNRESOLVED`: an unresolved live rule changes required format, sharing, cost or timing.

As of the 2026-08-23 verification, NIH states that the 2023 DMS Policy remains in force while the
required plan format changed in 2026. The current page requires the 2026 format for competing and
non-competing awards and asks about maximum appropriate sharing, timing, preservation, justified
limitations, participant protection/access control, expected data types/repositories and applicable
genomic-sharing obligations. Re-verify this snapshot for every real application; do not transplant it
to another funder or institution.

## 2. Build the lifecycle inventory

Give every object class a stable ID and classify at least:

| Dimension | Required decision |
|---|---|
| Object | raw DICOM, derived DICOM/SR/SEG, NIfTI, masks, annotations, clinical/pathology, omics, features, code, container, weights, logs, figures/source data |
| Role | source, intermediate, analysis input, claim-bearing output, release derivative, destruction candidate |
| Identity | patient/exam/series/specimen linkage, version, checksum/manifest and authoritative copy |
| Format/metadata | open or domain standard, data dictionary, units, controlled terms, provenance graph |
| Sensitivity | PHI, quasi-identifiers, genomic/sensitive attributes, consent/DUA/IP/licence restrictions |
| Location/control | primary storage, backup, encryption, access role, steward and recovery test |
| Lifecycle | collection, QC, freeze, analysis, sharing, preservation, retention review, destruction |

For imaging, preserve the raw acquisition separately from analysis derivatives; bind series selection,
quantitative transforms, de-identification, defacing/pixel-PHI checks, resampling and segmentation to
the source series. A converted NIfTI or feature table without the DICOM/source-series lineage is not a
complete provenance record.

## 3. Decide management, sharing and preservation separately

For each object specify:

1. collection/ingest, QC, naming, identifiers and authoritative-copy rule;
2. storage, encrypted transfer, backup cadence, restore test and incident owner;
3. role-based access, approval evidence, least privilege, offboarding and access review;
4. metadata/standards, transformation lineage, versioning and quality controls;
5. sharing trigger, repository/controller, open or controlled route, request criteria and embargo;
6. preservation duration, repository retention, local record-retention rule and preservation cost;
7. destruction trigger, legal/ethics hold check, approval, method, audit receipt and derivative scope;
8. accountable owner, budget line, review cadence and amendment history.

`FAIR` does not mean unrestricted public access. Restricted imaging or genomic data may be made
findable and interoperable through metadata and reusable through an authorized controlled route.
Never weaken consent, privacy, community governance, DUA, security or IP restrictions to obtain an
open-data label.

## 4. Change control and access requests

Review the plan at award activation, site/data-source addition, consent/DUA change, new data type,
new repository, analysis freeze, publication/preprint, access request, security event, project closeout
and retention/destruction decision. Each amendment records old/new text, trigger, affected objects,
policy/authorization evidence, approver, effective date and downstream artifacts made stale.

A post-publication request is not automatically approvable. Verify requester, purpose, requested
variables/images, consent/DUA/repository terms, privacy/security environment, agreement, decision owner,
release manifest and expiration/destruction duties. Return `STOP_FOR_AUTHORIZED_DATA_STEWARD` when the
skill cannot verify authority.

## 5. Output and stop gates

Return:

`policy passport -> object/lifecycle inventory -> management and access controls -> sharing/repository
route -> preservation/retention/destruction schedule -> roles/costs -> amendment log -> unresolved
authority and claim boundary`.

Stop when the governing policy/format is unresolved, sharing conflicts with consent/DUA, PHI/pixel PHI
or re-identification risk is unaudited, no accountable steward exists, an accession/repository is
invented, or destruction is proposed without retention/hold/authorization checks.

## Authoritative sources and live status

| Source | Status checked 2026-08-23 | Rule used here |
|---|---|---|
| [NIH Writing a Data Management and Sharing Plan](https://www.grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/dms/writing-dms-plan) | current official NIH page; 2026 format required | policy passport, current format/elements, justified limitations and appropriate sharing |
| [NIH Final DMS Policy, NOT-OD-21-013](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-21-013.html) | governing 2023 policy; format updated separately | planning, preservation and sharing obligation |
| [FAIR Guiding Principles](https://doi.org/10.1038/sdata.2016.18) | stable primary publication | findable, accessible, interoperable and reusable stewardship properties |
| [DICOM PS3.15](https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html) | live standard; verify edition at release | imaging confidentiality profiles and de-identification planning |

This reference does not decide legal retention, consent, DUA or institutional records policy. Those
decisions remain with the authorized institution, ethics/privacy office and data steward.
