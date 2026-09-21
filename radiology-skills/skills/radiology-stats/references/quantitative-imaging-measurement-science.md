# Quantitative imaging measurement science

Use this reference when the endpoint is a quantitative imaging biomarker or measurement—HU, SUV,
ADC, size, volume, perfusion, flow, density, radiomic feature or an algorithm-derived quantity—and the
question is bias, repeatability, reproducibility, agreement or change. Prediction accuracy and high ICC
do not establish measurement validity.

## 1. Define the measurand and conditions

Record before choosing a statistic:

| Field | Required specification |
|---|---|
| Measurand | exact quantity, tissue/lesion/region, units, scale and biological meaning |
| Measurement procedure | acquisition, reconstruction, calibration, preprocessing, segmentation, algorithm/software and version |
| Unit/hierarchy | patient/phantom, lesion/ROI, reader, scanner/site and repeat nested structure |
| Conditions | same session/operator/device for repeatability; named changed conditions for reproducibility |
| Reference | traceable/reference method, consensus or no accepted reference; uncertainty and timing |
| Intended decision | absolute value, ranking, threshold classification or change monitoring |
| Allowable difference/change | clinically/physically justified tolerance or smallest relevant change |
| Primary estimand | bias, limits, within-subject variation, repeatability/reproducibility coefficient or reliability |

Do not call a feature a biomarker solely because it is numeric. Link the measurand to a defined use and
measurement procedure.

## 2. Keep concepts separate

- **Bias/accuracy:** systematic difference from a reference value/method, when a defensible reference
  exists.
- **Agreement:** closeness between methods/readers/devices, including bias and limits of differences.
- **Repeatability:** variation when relevant conditions remain the same over a short interval.
- **Reproducibility:** variation when named conditions change—site, scanner, operator, reconstruction,
  reader or software.
- **Reliability/ICC:** proportion of total variance attributable to between-subject differences in the
  sampled population; it depends on heterogeneity and may be high despite clinically unacceptable
  absolute error.
- **Responsiveness/change validity:** ability to detect change beyond measurement error; it is not
  demonstrated by cross-sectional discrimination.

Always report absolute error in meaningful units alongside relative/reliability quantities.

## 3. Study design

- Recruit subjects spanning the intended value, anatomy, disease severity, body size and protocol
  distribution. A deliberately broad range can inflate ICC; preserve the target-population context.
- Obtain true repeats without relevant biological change for repeatability. If time/treatment can alter
  the measurand, the observed difference mixes biology and measurement error.
- Randomize/counterbalance acquisition, reconstruction or reader order where possible and blind readers
  to prior values/reference/condition.
- Use multiple subjects under each condition; repeated reconstructions/slices from one subject do not
  replace independent subjects.
- For reproducibility, cross or otherwise identify subject, site/scanner, operator/reader, protocol and
  repeat effects. Avoid complete confounding of condition with subject or disease state.
- Predefine non-evaluable/failed measurements and include failure rate as a result.

## 4. Core analysis routes

### Two methods or conditions

- Plot paired differences versus the mean/reference and report mean bias with CI.
- Estimate limits of agreement with uncertainty using a model that respects repeated/nested data.
- Check proportional bias, nonlinearity and heteroscedasticity. Use transformation, regression-based
  limits or scale-stratified reporting when justified; do not apply constant limits blindly.
- Correlation/regression alone measures association, not agreement.

### Repeatability/reproducibility

- Estimate within-subject SD and, for positive ratio-scale data, within-subject coefficient of variation
  when assumptions are appropriate.
- Under an approximately normal difference model with comparable repeat error, a repeatability
  coefficient is commonly derived from the SD of differences/within-subject SD. State the formula,
  multiplier and assumptions rather than copying a universal number.
- Fit variance-component/mixed models when reader, scanner/site, protocol and repeats are crossed or
  nested. Report each variance source and the target conditions being generalized over.
- Specify ICC model, agreement versus consistency and single versus average measurement; pair it with
  absolute agreement/error.

### Change and thresholds

- Define the smallest detectable/real change from the fitted error model and desired confidence, then
  compare it with the clinically important change. Measurement detectability is not clinical importance.
- For percent change, address denominator instability and scale dependence.
- Threshold classification needs sensitivity/specificity and misclassification around the threshold in
  addition to continuous agreement.

## 5. Imaging-specific components

Quantify contributions from acquisition, reconstruction/filter/kernel, calibration, contrast timing,
registration, segmentation/reader, software/version and analysis choices. Use phantom/site-qualification
evidence where appropriate, but confirm performance in representative patient images when the claim is
clinical.

Radiomic-feature robustness screens should:

- predefine perturbations/conditions and stability rule;
- fit selection only in development data;
- report the full feature family and multiplicity/selection consequences;
- test whether stability survives site/protocol transport;
- avoid claiming biological validity from technical stability.

## 6. Sample size and uncertainty

Plan from the primary agreement/repeatability estimand, target interval width or margin, expected
within-/between-subject variance, number of conditions/readers/repeats, missing/failure rate and desired
generalization. Use simulation for unbalanced crossed designs. There is no universal subject, repeat or
ICC sample-size cutoff.

Bootstrap/resampling must sample at the independent subject level and preserve paired/nested structure.
Return `BIOSTATISTICIAN_REQUIRED` when variance components, allowable limits, heteroscedastic model or
unbalanced crossed design cannot be supported.

## 7. Sensitivity and stop gates

Predefine analyses for outliers, scale/transform, proportional bias, value range, lesion size, site/
scanner/protocol, reader/segmentation, failed measurements and biologic-change exclusion.

Return `STOP_FOR_REPAIR` when units/measurand differ across methods, repeats may contain material
biological change with no separation strategy, subject IDs/pairing are lost, conditions are confounded,
or ICC/correlation is the only evidence for an absolute-agreement claim.

## 8. Reporting contract

Return:

`measurand/use -> measurement procedure/version -> repeatability/reproducibility conditions -> design
and hierarchy -> reference/tolerance -> bias and absolute agreement -> within-subject/variance
components -> failure rate -> sensitivity -> detectable versus important change -> claim ceiling`.

## Primary and official sources

- Sullivan DC, et al. [Metrology standards for quantitative imaging biomarkers](https://doi.org/10.1148/radiol.2015142202).
- Raunig DL, et al. [Statistical methods for quantitative imaging biomarker technical performance](https://doi.org/10.1177/0962280214537344).
- Bland JM, Altman DG. [Agreement between two methods of clinical measurement](https://doi.org/10.1016/S0140-6736(86)90837-8).
- RSNA QIBA. [Profiles and conformance resources](https://qibawiki.rsna.org/index.php/Profiles).

Use the current modality/profile-specific conformance requirements; this reference supplies no
universal acceptance limit.
