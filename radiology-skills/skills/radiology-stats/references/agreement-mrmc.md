# Agreement & multi-reader multi-case (MRMC)

## Pick the agreement statistic by data type
| Data | Statistic |
|---|---|
| 2 readers, nominal categories | **Cohen's kappa** |
| 2 readers, **ordered** categories (e.g. BI-RADS, Likert) | **weighted kappa** (linear or quadratic — state which) |
| ≥ 3 readers, nominal | **Fleiss' kappa** |
| Continuous (size, SUV, volume) | **ICC** + **Bland-Altman** |
| Ordinal/continuous, rank concordance | Kendall's W (≥3 raters; for 2 readers use weighted kappa / tau-b) |

- Report **kappa with 95% CI** and an interpretation band, but note kappa depends on
  prevalence/marginal distributions (report observed agreement too).
- For continuous measurements, **kappa is wrong** — use ICC and Bland-Altman.

## ICC — you must specify the model
Report the full specification (McGraw & Wong / Koo & Li form), e.g. *"ICC(2,1), two-way
random-effects, absolute agreement, single rater."* Choices:
- **Model**: one-way random / two-way random (raters are a sample) / two-way mixed (these
  specific raters).
- **Type**: absolute agreement vs consistency.
- **Unit**: single rater vs mean of k raters.
Using "consistency" when you need "absolute agreement" silently hides systematic bias.
Specify model, agreement definition and single/average unit separately; a two-way mixed model is
not automatically an absolute-agreement or consistency coefficient. Confirm that the selected
software row implements the intended combination, including its confidence-interval assumptions.

```python
import pingouin as pg          # pip install pingouin
icc = pg.intraclass_corr(data=long_df, targets="case", raters="reader", ratings="value")
# select the row matching your design, e.g. ICC2 (two-way random, absolute agreement, single)
```

## Bland-Altman (continuous, two methods/readers)
Plot mean vs difference; report **bias** (mean difference) and **95% limits of agreement**
(bias ± 1.96·SD). Check for proportional bias (trend vs magnitude). Hand the plot to
`radiology-figure`.

## MRMC — the right framework for reader studies
When **multiple readers** read **multiple cases** (e.g. AI-vs-no-AI or comparing modalities),
preserve the actual crossed/nested/partially crossed dependence and the intended inference target.
Averaging reader scores and applying ordinary DeLong does not automatically account for the
reader/case dependence or estimate the intended reader-averaged performance contrast.

- **Inference target:** choose random versus fixed readers and cases from the sampling design and
  claim. Random readers target a represented reader population under model/sampling assumptions;
  fixed-reader inference is conditional on those named readers and cannot generalize to all
  radiologists. Apply the same distinction to fixed versus sampled cases. Do not make a factor
  random merely because several observed levels exist.
- **Designs:** fully crossed, partially crossed, split-plot, sequential and parallel designs have
  different workload, overlap and carryover properties. Fully crossed is not universally most
  powerful under a fixed resource budget. Compare designs using the estimand, variance components,
  missingness and number of independent readers/cases and total readings; preserve their distinct
  estimands. Follow the [reader-study design lock](../../radiology-translation/references/reader-study.md).
- **Analysis:** **Obuchowski-Rockette (OR)** and **Dorfman-Berbaum-Metz (DBM)** approaches,
  **iMRMC** or R **`RJafroc`** may support particular AUC/figure-of-merit designs. Verify the exact
  implementation's endpoint, fixed/random factor, design and missingness support. Use a different
  justified hierarchical analysis for endpoints or designs outside that method's scope.
- **Endpoints**: ROC AUC, or location-specific (JAFROC/wAFROC) when localisation matters
  (detection tasks).
- **Reader-averaged** estimate with CI when it is the estimand; state whether uncertainty and the
  conclusion concern a reader/case population or are conditional on the sampled fixed factors.
- **Power/sample size** before the study (number of readers × cases) — see sample-size.md.

```r
# R example for a compatible ROC design; verify package/version and factor assumptions.
# Research software availability is not FDA endorsement or approval of a study/device.
library(RJafroc)
result <- StSignificanceTesting(dataset, FOM = "Wilcoxon", method = "OR")
```

## Reporting sentences
*"Inter-reader agreement was substantial (ICC, 0.82; 95% CI: 0.75, 0.87; two-way
random-effects, absolute agreement, single rater)."*
*"In the MRMC analysis (6 readers, 300 cases, fully crossed), reader-averaged AUC improved
from 0.81 to 0.87 with AI assistance (difference 0.06; 95% CI: 0.02, 0.10; P = .005;
Obuchowski-Rockette)."*

## Reviewer hot-spots
ICC model unspecified; kappa used for continuous data; readers averaged then DeLong'd;
fixed-reader conclusion generalised to all radiologists; no pre-study power for the reader
study.

## Primary methodological sources

- [MRMC analysis software and fixed/random factor choices](https://pmc.ncbi.nlm.nih.gov/articles/PMC7190386/).
- [FDA iMRMC regulatory science tool: supported designs, endpoints and limitations](https://cdrh-rst.fda.gov/imrmc-software-do-multi-reader-multi-case-statistical-analysis-reader-studies).

Checked 2026-09-04. Verify support in the actual analysis implementation; a tool description does
not establish study validity, regulatory clearance or that a generic code example matches the data.
