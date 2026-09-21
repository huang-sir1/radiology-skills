# Reporting routes for guidelines, qualitative/mixed methods, economics and implementation

Select the reporting artifact by study/output type. Reporting completeness never proves valid
methods, low bias, good recommendations, economic value or successful implementation.

## Route table

| Output/study | Primary reporting route | Separate appraisal/method owner | Boundary |
|---|---|---|---|
| health-care practice guideline | RIGHT 2017 whole-report checklist | AGREE II for guideline quality/appraisal; `radiology-consensus-guideline` owns recommendation development | RIGHT is reporting; AGREE appraisal does not create a recommendation |
| biomedical consensus process | ACCORD 2024 | `radiology-consensus-guideline` owns Delphi/RAND/NGT/panel methods | a reported vote does not replace evidence or establish guideline quality |
| interviews/focus groups | COREQ 2007 (32 items) where its scope fits | `radiology-qualitative-mixed-methods` | COREQ completion does not prove sampling adequacy, reflexivity or analytic credibility |
| broader qualitative study | SRQR 2014 | `radiology-qualitative-mixed-methods` | select by actual method; do not force COREQ onto all qualitative designs |
| mixed-methods study | design-specific quantitative guideline + SRQR/COREQ for the qualitative component; explicitly report integration/joint display | `radiology-qualitative-mixed-methods` plus `radiology-stats` | two parallel checklists without integration do not report mixed-method inference |
| full health economic evaluation | CHEERS 2022; add current CHEERS-AI where an AI intervention is in scope | `radiology-health-economics` | CHEERS is not a model-quality score or HTA/reimbursement approval |
| implementation study | StaRI 2017 plus design-specific guideline(s) | `radiology-translation` implementation mode | StaRI reporting is not evidence of adoption, fidelity, equity, effectiveness or sustainability |
| patient/public involvement | GRIPP2 2017, short/long route as applicable | `radiology-design` owns the involvement and decision-impact evidence | reporting cannot create involvement that did not occur |

## Guideline/consensus stack

For a recommendation-bearing document, record separately:

1. evidence synthesis and certainty (`radiology-systematic-review`);
2. panel/COI/EtD/consensus/recommendation process (`radiology-consensus-guideline`);
3. whole-report completeness (RIGHT, with current extensions only when applicable);
4. quality/appraisal (AGREE II or authorized appraisal route);
5. implementation/public version/update plan.

RIGHT 2.0 was listed by EQUATOR as under development in 2026, not a released replacement. Until an
official final version is verified, use RIGHT 2017 for current audits and mark any claimed newer
version `VERIFY_FROM_CURRENT_SOURCE`.

## Audit output

Return `study/output classification -> guideline stack and version/status/source/access date -> item
matrix with location -> missing/partial items -> method/appraisal owner handoff -> reporting-only
claim boundary`.

## Authoritative registries and primary sources

Verified against EQUATOR/official pages on 2026-08-23; re-verify before a real submission:

- [RIGHT](https://www.equator-network.org/reporting-guidelines/right-statement/)
- [AGREE II instrument](https://www.agreetrust.org/resource-centre/agree-ii/)
- [ACCORD](https://www.equator-network.org/reporting-guidelines/accord-accurate-consensus-reporting-document-a-reporting-guideline-for-consensus-methods-in-biomedicine/)
- [COREQ](https://www.equator-network.org/reporting-guidelines/coreq/)
- [SRQR](https://www.equator-network.org/reporting-guidelines/srqr/)
- [CHEERS 2022](https://www.equator-network.org/reporting-guidelines/cheers/)
- [StaRI](https://www.equator-network.org/reporting-guidelines/stari-statement/)
- [GRIPP2](https://www.equator-network.org/reporting-guidelines/gripp2-reporting-checklists-tools-to-improve-reporting-of-patient-and-public-involvement-in-research/)
