# Submission Skill validation receipt

Validation date: 2026-09-04

Status: **PASS**  
Independent residual review: **0 blocker / 0 high / 0 medium**, last performed 2026-08-22 under the
published human-adjudication boundaries; the 2026-08-23 and 2026-09-04 receipt refreshes reran machine suites only.

The 2026-09-04 refresh binds the golden suite's synthetic CLI fixture date fix to its current bytes
and SHA-256. The submission module validator and PowerShell wrapper passed with all 88 structural
regression cases and 14 golden scenarios. Expired, future-dated and wrong-cycle counterexamples
remain enforced; the production seven-day freshness gate was not changed. No real-source access
dates or independent behavioral-review status were refreshed by this maintenance step.

## Frozen executable inputs

| Metric | Frozen value |
|---|---:|
| Canonical journal routes | 11 |
| Journal profiles | 11 |
| Journal evidence rows | 147 |
| Route contracts | 32 |
| Negative-contract fixtures | 10 |
| Structural regression cases | 88 |
| Cross-step golden scenarios | 14 |

The authoritative artifact list is the machine-verifiable block at the end of this receipt. It
freezes the registries, route fixtures, journal and conference manifest/intake/transfer/report
templates, the conference portal route reference/checker, contributor/disclosure handoff,
authorship/AI/public-access reference, production auditor, resolver, renderer, shared security helper,
both test suites, Skill entrypoint, validator and PowerShell wrapper by exact byte length and SHA-256.
The validator recalculates every value.

The evidence registry contains 131 journal-guide rows, four publisher-policy rows, 11 advisory
published exemplars and one non-authoritative portal placeholder. A published exemplar cannot create
a hard requirement.

## Executable coverage

| Stage | Exact journal/article routes |
|---|---:|
| initial | 11 |
| pre-review | 4 |
| revision | 11 |
| final-files | 6 |
| transfer | 0; fail closed until the actual target transfer route is profiled |

The 11 profiles are Radiology, Nature Medicine, Nature Communications, The Lancet Digital Health,
eClinicalMedicine, Cancer Cell, Cell Reports Medicine, npj Digital Medicine, npj Precision Oncology,
Advanced Science and JAMA Network Open. Coverage applies only to each profile's exact named primary
research article type; it is not a publisher-family wildcard.

## Historical executed validation (2026-08-22/23)

The broader cross-Skill and literature checks below retain their original validation scope/date;
the 2026-09-04 refresh above establishes only the current submission module's machine validation.

- `validate_submission_skill.py`: PASS; 11 journal profiles/routes plus one independent conference
  portal-finalization branch, 147 evidence rows, 32 journal route contracts, 10 negative-contract
  fixtures, 88 structural regression cases and 14 cross-step golden scenarios.
- PowerShell validation wrapper: PASS.
- Official Skill quick validator: PASS for `radiology-submission`, `radiology-radiogenomics` and
  `radiology-response`.
- Cross-Skill route validation: PASS; 40 radiogenomics routing cases, 43 rules and eight templates.
- Transcriptomics literature maps: PASS; bulk RNA 33, scRNA/snRNA 34 and spatial 33, 100 unique
  DOI/PMID pairs, with PubMed resolving 100/100.
- Transparent peer-review corpus: PASS; 100 strict current-JIF-eligible Nature Portfolio records,
  zero Cell Systems exceptions and a synchronized 100-row response evidence map.
- Response Skill: PASS; 26 response-contract cases.

## Closed adversarial findings

- `PORTAL_CURRENT` now requires a capture hash/date, exact journal/article/stage binding, screen label
  and concrete locator; generic notes and development portals cannot authorize a rule.
- Cell Press LaTeX routes require a mutually hash-bound `.tex` plus checked PDF and matching source,
  dependency and compile receipts; isolated compilation and rendered equivalence remain human gates.
- Lancet Digital Health and eClinicalMedicine raster, flowchart and vector rules are separate; a DOCX
  raster is rejected.
- npj ordinary-revision figure handling requires explicit exact-portal adjudication and cannot borrow
  final high-resolution rules.
- JAMA initial and revision figure formats are stage/type specific. Marked/unmarked clinical-image
  pairs use separate stage rules and a path-free receipt binding both manifest item IDs and SHA-256
  values; missing, generic, wrong-parent or hash-mismatched receipts fail.
- Advanced Science's public Editorial Manager development page is `PORTAL_PLACEHOLDER`, advisory only.
- Conditional N/A decisions require a dated, rule-bound human attestation; free text alone cannot
  close the gate.
- Reports record both evidence and route-contract SHA-256 provenance. Attachment/partial scopes are
  `INCOMPLETE_SCOPE`; structural failures are `BLOCKED_STRUCTURAL`; a structurally passing upload root
  is only `HUMAN_GATES_REQUIRED`. The deterministic auditor has no `READY` output path.
- `evidence-synthesis` is now a closed submission scope: it requires the systematic-review design
  token and a nonzero current prereview receipt, rejects a radiogenomics handoff, and freezes a
  dedicated intake template. The receipt points to seven review artifacts; machine validation does
  not authenticate them or recompute the synthesis.
- Conference/congress portal finalization is independent of the 11 journal routes. It requires exact
  venue/cycle/type current-call and live-portal receipts, a closed field/file manifest, frozen
  `radiology-dissemination` content, claim/embargo/disclosure/privacy/rights and author-approval
  gates, and stops at `HUMAN_PORTAL_ACTION_REQUIRED`; the checker cannot upload, attest or submit.

## Evidence boundary

The 100-paper transparent-review corpus is a purpose-built, criterion-sampled real-world Skill
evidence set for extracting reviewer concerns, author actions and documented closure. Published-paper
and full-public-review eligibility is deliberate for that purpose; the set is not designed as a
systematic review or journal-frequency estimate. All 100 records use current-JIF-eligible Nature Portfolio
journals under the frozen 2025 metrics; 62 are flagship/major-specialist records and 38 are Nature
Communications fallbacks with official full reviewer-report/author-response files. The dated status
screen records two corrections and one Editor's Note. Reviewer comments, responses, editorial
decisions and publication do not certify scientific truth, a clean paper or future acceptance.

Machine validation establishes inventory, byte/container, registry binding and explicitly modeled
cross-file conditions. It does not authenticate private portal captures or attestations, prove that a
conditional trigger is absent, replace full rendering, determine scientific validity, or issue the
final human submission verdict.

## Machine-verifiable receipt

The JSON below is authoritative for frozen counts and artifact identity. Do not edit it by hand
without rerunning the full validator and both test suites.

<!-- BEGIN MACHINE-VERIFIABLE RECEIPT -->
```json
{
  "schema_version": "1.0",
  "validation_date": "2026-09-04",
  "counts": {
    "routes": 11,
    "profiles": 11,
    "evidence_rows": 147,
    "route_contracts": 32,
    "negative_contracts": 10,
    "regression_cases": 88,
    "golden_scenarios": 14
  },
  "artifacts": {
    "journal_evidence_registry": {
      "path": "references/journal-requirements-evidence.tsv",
      "bytes": 50289,
      "sha256": "B6BF95CA12E4F6D1F181CE81425B34C7BF5CF77C5AA817461F49B7FBC66F5854"
    },
    "route_contract_registry": {
      "path": "references/journal-required-materials.json",
      "bytes": 23493,
      "sha256": "A23EE91D926C76830F85C7E0DEB28D922EA7433416CC10723E40C29945D4C25D"
    },
    "routing_cases": {
      "path": "tests/submission-routing-cases.json",
      "bytes": 5791,
      "sha256": "071DED0AE3889F40995C66A0A8E3A89AA4309EC71AB6E78A36C9C54952B63130"
    },
    "manifest_template": {
      "path": "assets/submission-manifest.template.csv",
      "bytes": 595,
      "sha256": "1D9C4FE92423EDFD3A773D39BDC541C23C64E786465ED6F82B6DECA1E0572DD6"
    },
    "intake_template": {
      "path": "assets/submission-intake.template.json",
      "bytes": 1027,
      "sha256": "115EB9D0F54D6ADDF6E21C4F406B0B21B565D7B90A9BF20A56E46EFC8AC0EC96"
    },
    "evidence_synthesis_intake_template": {
      "path": "assets/submission-intake.evidence-synthesis.template.json",
      "bytes": 1053,
      "sha256": "FF4864BFABCC8098BBDE340C08635047ECD60C4A894E65AB43E3F309526A2FD2"
    },
    "transfer_template": {
      "path": "assets/submission-transfer-context.template.json",
      "bytes": 557,
      "sha256": "308F907CB772E89EB18268CF8819AFB50E9A4829C8C35449FC89F6B1C4330D00"
    },
    "audit_report_template": {
      "path": "assets/submission-audit-report.template.md",
      "bytes": 7775,
      "sha256": "578A018FCA1D46BFF75BEF3FAC253E8B39C113A7D00FF0089DB91278FBA5487A"
    },
    "contributor_disclosure_handoff_template": {
      "path": "assets/contributor-disclosure-handoff.template.csv",
      "bytes": 657,
      "sha256": "1D7861F6A64CF1717F9A350EB3D112C8D0A8E42D28D7083A49A27D86DE465998"
    },
    "conference_portal_intake_template": {
      "path": "assets/conference-portal-intake.template.json",
      "bytes": 2056,
      "sha256": "45B4CC6CC387595B55EC0AC5EA155D782206CF5A929AC21EABBC4867138CD111"
    },
    "conference_portal_manifest_template": {
      "path": "assets/conference-portal-manifest.template.csv",
      "bytes": 411,
      "sha256": "B54BD1E32B3D818BF28EC626449A60C4A394ADC6231D2B4F1C1D33468473059D"
    },
    "conference_portal_route_reference": {
      "path": "references/conference-portal-finalization.md",
      "bytes": 7897,
      "sha256": "BD16B60380EA884ADA3FBF42CE31DFFF8A855684BB4925F86FC5D95CA6EC2258"
    },
    "conference_portal_package_validator": {
      "path": "scripts/validate_conference_portal_package.py",
      "bytes": 20947,
      "sha256": "D601D200766681890D3458FB3F9C227B0A2644AC1F5BFAE01AEA0BC986131635"
    },
    "authorship_ai_public_access_reference": {
      "path": "references/authorship-ai-and-public-access-handoff.md",
      "bytes": 4898,
      "sha256": "2A86DFE291E3C14769DEE81661E6AA070205C38FBB9766B8497409DED27CA536"
    },
    "structural_auditor": {
      "path": "scripts/audit_submission_package.py",
      "bytes": 139425,
      "sha256": "D3EEA208B9D91DC553730EDF1AC192934F95D4BD96CCFF50BCF72A1542EBFCAA"
    },
    "regression_suite": {
      "path": "scripts/test_audit_submission_package.py",
      "bytes": 101765,
      "sha256": "168821B91B7AB0B8E6072A7A3EAB2C39E50B8FF3F8E16B761F734B83D9E21AE4"
    },
    "golden_suite": {
      "path": "scripts/test_submission_golden_scenarios.py",
      "bytes": 45403,
      "sha256": "532DC7A8965B4DEC2950597BE1A45D5F15FD6CD8E83A3B8D4AC6053139CF1BC2"
    },
    "intake_resolver": {
      "path": "scripts/resolve_submission_intake.py",
      "bytes": 30751,
      "sha256": "DBF5C454BB35C6996E141D3EF535FA9E51DA8632D677839E166C1D40615C133B"
    },
    "report_renderer": {
      "path": "scripts/render_submission_audit_report.py",
      "bytes": 21638,
      "sha256": "57668C4B089614CCA26F36966921911C88A4B270D46EB508BFCDE95A515FE9EA"
    },
    "security_helper": {
      "path": "scripts/submission_security.py",
      "bytes": 8399,
      "sha256": "D23699D6DABA70F1AAA6B8B2356AEA7AAC575167576E946D312B6B653ABE5761"
    },
    "skill_entrypoint": {
      "path": "SKILL.md",
      "bytes": 21150,
      "sha256": "1B2732E5D74CD4DECE69F81BCCE1AC5F4FE9C26E03FF86ECDFC22B5C61631271"
    },
    "validator": {
      "path": "scripts/validate_submission_skill.py",
      "bytes": 54099,
      "sha256": "CA31BEF7814B6EEEE067A5EAFDE7E5A6BA936A31B57F1FAD9C6908425A30E73D"
    },
    "validation_wrapper": {
      "path": "scripts/validate_submission_skill.ps1",
      "bytes": 864,
      "sha256": "F8AE6AF60ADD7253638D85657EC1FAA61EE269954222613CD5744E3B92AA46E2"
    }
  }
}
```
<!-- END MACHINE-VERIFIABLE RECEIPT -->
