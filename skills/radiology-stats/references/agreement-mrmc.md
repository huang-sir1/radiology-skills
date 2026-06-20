# Agreement & multi-reader multi-case (MRMC)

## Pick the agreement statistic by data type
| Data | Statistic |
|---|---|
| 2 readers, nominal categories | **Cohen's kappa** |
| 2 readers, **ordered** categories (e.g. BI-RADS, Likert) | **weighted kappa** (linear or quadratic — state which) |
| ≥ 3 readers, nominal | **Fleiss' kappa** |
| Continuous (size, SUV, volume) | **ICC** + **Bland-Altman** |
| Ordinal/continuous, rank concordance | Kendall's W |

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
When **multiple readers** each read **multiple cases** (e.g. AI-vs-no-AI, or comparing
modalities), both readers and cases are random effects. Averaging readers and running a
plain DeLong **underestimates variance** and overstates significance.

- **Designs**: fully crossed (every reader reads every case) is most powerful; report the
  design.
- **Analysis**: **Obuchowski-Rockette (OR)** and **Dorfman-Berbaum-Metz (DBM)** (now unified,
  "OR-DBM") for AUC/figure-of-merit differences; **iMRMC** (FDA) or R **`RJafroc`**.
- **Endpoints**: ROC AUC, or location-specific (JAFROC/wAFROC) when localisation matters
  (detection tasks).
- **Reader-averaged** estimate with CI; conclusion about the **reader population**, not just
  these readers.
- **Power/sample size** before the study (number of readers × cases) — see sample-size.md.

```r
# R, FDA-endorsed:
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
