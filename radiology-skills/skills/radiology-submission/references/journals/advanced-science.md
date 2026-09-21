# Advanced Science — conservative submission profile

Snapshot checked: 2026-08-22. Scope: `Research Article`. The journal-specific Wiley Author Guidelines
URL returned Cloudflare 403, while the official Advanced Portfolio policy exposed the applicable data-
reporting-checklist rule. File extensions and the real submission portal remain deliberately
fail-closed.

## Official routes and accessibility state

- `AS-GUIDE`: [Advanced Science Author Guidelines](https://advanced.onlinelibrary.wiley.com/hub/journal/21983844/author-guidelines) — official, but content inaccessible (403) at snapshot.
- `AS-POLICY`: [Advanced Portfolio Editorial Policies](https://advanced.onlinelibrary.wiley.com/hub/editorial-policies) — official portfolio route used for the checklist obligation.
- `AS-DATA-CHECKS`: [Wiley Data Reporting Checklists](https://onlinelibrary.wiley.com/products/journals/data-checklists-chemistry)
- `AS-ML-CHECK`: [Machine Learning Research Data Reporting Checklist](https://onlinelibrary.wiley.com/pb-assets/hub-assets/chemistry-europe/checklists/Machine_Learning_Data_Reporting_Checklist-1695894214660.pdf)
- `WILEY-DATA`: [Wiley data sharing policies](https://authorservices.wiley.com/author-resources/Journal-Authors/open-access/data-sharing-citation/data-sharing-policy.html)
- `WILEY-ETHICS`: [Wiley publishing ethics](https://authors.wiley.com/ethics-guidelines/index.html)
- `AS-EM-DEV`: [Public Editorial Manager page](https://www.editorialmanager.com/advancedscience/) —
  currently says the site is under development. Classify it as non-authoritative
  `PORTAL_PLACEHOLDER`/advisory discovery only: it is not the genuine submission instance, cannot be
  relabeled `PORTAL_CURRENT`, and cannot establish an upload designation, extension or required field.
- `AS-ALT-GUIDE`: [Instructions for Authors target linked by that development page](https://www.advancedscience.com/authorguidelines) —
  the current link could not be securely retrieved (timeout plus TLS hostname mismatch in an
  independent command-line check). Do not disable certificate verification or use it as rule evidence.

## Portfolio signals and verified policy facts

- Official Advanced Portfolio indexing indicated Free Format for new submissions and single-
  anonymized review, but the journal-specific guide/real portal did not independently close those
  fields at this snapshot. Treat both as
  `UNVERIFIED_CURRENT` until refreshed from an accessible current page or genuine portal. Even when
  reconfirmed, Free Format relaxes style conformance only; it cannot establish accepted extensions or
  waive title, abstract, authorship, ethics or declarations.
- Current original-research route is Research Article. A historical editorial cannot establish 2026
  numeric limits.
- New Research Articles use the applicable Data Reporting Checklist as a submission cover sheet.
  Machine-learning research uses the downloadable official ML checklist PDF; biological/biomedical
  work uses the `Biological and Biomedical Sciences Data Reporting Checklist`. The latter's accepted
  upload extension is not published on the accessible page and must be resolved in the genuine exact
  portal. Imaging AI may activate both, so determine scope rather than assuming only one.
- ML checklist review covers algorithm/language, rationale versus simpler methods, ethics, code or
  nonsharing rationale, baseline comparisons, reproducibility scripts, train/validation/test
  implementation, dataset versions/cleaning/exclusions, multisource handling, bias mitigation, leakage
  prevention and metrics.
- Wiley research/review content requires a Data Availability Statement. The Advanced Science-specific
  sharing-policy tier was not accessible, so an open-repository link is not a universal hard rule.
- GenAI used to create manuscript content must be transparently described in Methods or a disclosure/
  Acknowledgment. Apply official human/animal ethics and design-reporting requirements by study type.

## Fail-closed material matrix

| Stage | Material | Classification at snapshot |
|---|---|---|
| initial | manuscript file type/title-page packaging | `UNVERIFIED_CURRENT_GUIDE` — Free Format does not reveal accepted extensions |
| initial | cover letter | `UNVERIFIED_CURRENT_GUIDE`; preprint disclosure belongs in cover when applicable |
| initial | Biological and Biomedical Sciences Data Reporting Checklist | conditional hard policy; accepted extension exact-portal unresolved |
| initial | Machine Learning checklist | conditional hard policy for ML research; official downloadable PDF |
| manuscript | Data Availability Statement | hard publisher policy |
| initial/revision | figures/tables/SI types, sizes, resolution | `UNVERIFIED_CURRENT_GUIDE` |
| revision | clean/marked manuscript, response, final figures | exact live-portal check; decision letter requires separate human adjudication |
| portal | upload labels and metadata | `UNVERIFIED`; public EM development page is advisory `PORTAL_PLACEHOLDER`, not route evidence |

Any final package audit remains `INCOMPLETE` until the current Advanced Science guide or genuine
exact-journal live portal establishes the machine-resolvable file types and required materials. A decision
letter remains a human-adjudicated gate until the validated contract is maintained. Never borrow an
Advanced Materials, Advanced Healthcare Materials or other Wiley sibling rule. The development page
cannot close this gap, even when its URL resembles a production Editorial Manager route.

## Published exemplars — advisory only

- [In Vivo Intelligent Fluorescence Endo-Microscopy by Varifocal Meta-Device and Deep Learning](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202307837) (2024).
- [Unsupervised Segmentation of 3D Microvascular Photoacoustic Images Using Deep Generative Learning](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202402195) (2024).

These demonstrate published presentation only; they cannot close the inaccessible guide gap.
