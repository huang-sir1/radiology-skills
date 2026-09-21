# Translation and deployment source registry

This registry anchors rule-bearing translation claims. Each row records its own checked date;
volatile regulatory, interoperability and reporting requirements must be refreshed
from the linked official source for the target jurisdiction, device, site and study date.

| Source | Official URL | Version/status | Accessed | Claim use |
|---|---|---|---|---|
| FDA iMRMC research tool | https://cdrh-rst.fda.gov/imrmc-software-do-multi-reader-multi-case-statistical-analysis-reader-studies | official research-tool page; fully and non-fully-crossed designs, sizing and endpoint-specific functions described | 2026-09-04 | reader/case covariance and design-matched analysis; not a universal reader count, washout interval or design ranking |
| FDA AI-enabled device software lifecycle draft guidance | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing | January 2025 draft; not for implementation | 2026-08-23 | separates lifecycle evidence, submission content, transparency and monitoring; never present draft text as binding law |
| FDA AI PCCP final guidance | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence | August 2025 final guidance | 2026-08-23 | change description, modification protocol and impact assessment for planned AI changes |
| FDA QMSR | https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-management-system-regulation-qmsr | effective 2026-02-02 | 2026-08-23 | current US quality-system status; applicability and compliance remain qualified-owner decisions |
| FDA AI postmarket monitoring research programme | https://www.fda.gov/medical-devices/medical-device-regulatory-science-research-programs-conducted-osel/methods-and-tools-effective-postmarket-monitoring-artificial-intelligence-ai-enabled-medical-devices | current programme page | 2026-08-23 | monitoring methods and denominator/label-delay/change questions; not a compliance certificate |
| IMDRF SaMD clinical evaluation N41 | https://www.imdrf.org/documents/software-medical-device-samd-clinical-evaluation | final 2017 | 2026-08-23 | valid clinical association, analytical/technical validation and clinical validation as distinct evidence |
| IMDRF GMLP N88 | https://www.imdrf.org/documents/good-machine-learning-practice-medical-device-development-guiding-principles | final 2025 | 2026-08-23 | lifecycle-oriented ML principles and multidisciplinary responsibility |
| DICOM current standard | https://www.dicomstandard.org/current/ | continuously maintained current edition | 2026-08-23 | conformance statement and object/transaction specifications; conformance does not guarantee interoperability |
| DICOM PS3.2 interoperability statement | https://dicom.nema.org/medical/dicom/current/output/chtml/part02/sect_n.3.3.html | current PS3.2 | 2026-08-23 | explicit boundary that DICOM conformance alone does not guarantee interoperability |
| IHE Radiology Technical Framework | https://profiles.ihe.net/RAD/ | current published/trial profile index | 2026-08-23 | profile/transaction route for local integration testing; trial status must remain visible |
| FDA human factors guidance | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/applying-human-factors-and-usability-engineering-medical-devices | final guidance 2016 | 2026-08-23 | users, use environments, critical tasks, use-related risk and validation framing |
| NIST AI RMF 1.0 | https://www.nist.gov/itl/ai-risk-management-framework | voluntary framework 1.0 | 2026-08-23 | governance/map/measure/manage framing; not regulatory approval |
| DECIDE-AI | https://doi.org/10.1038/s41591-022-01772-9 | reporting guideline 2022 | 2026-08-23 | early-stage live clinical evaluation reporting and human/workflow context |
| CONSORT-AI / SPIRIT-AI | https://www.consort-spirit.org/published-statements | published AI extensions; verify current page | 2026-08-23 | AI trial protocol/reporting route; reporting compliance does not validate design or impact |
| RE-AIM | https://re-aim.org/ | current official framework site | 2026-08-23 | reach, effectiveness, adoption, implementation and maintenance; framework use does not prove success |
| StaRI | https://www.equator-network.org/reporting-guidelines/stari-statement/ | final reporting guideline | 2026-08-23 | implementation-strategy reporting; not an implementation-effectiveness certificate |

## Use rules

- Record `SOURCE_EVIDENCE`, `OBSERVED_LOCAL_EVIDENCE`, `MODELLED_INFERENCE`, `ASSUMPTION` and
  `DECISION_RECOMMENDATION` separately.
- A framework, reporting checklist, conformance statement, model card, vendor demonstration or
  regulatory submission concept is not site acceptance, clinical benefit or authorization.
- When the target jurisdiction or site is known, record the current exact authority, document
  status/effective date, access date and qualified human owner. Use `LIVE_VERIFICATION_REQUIRED`
  when current applicability is unresolved.
