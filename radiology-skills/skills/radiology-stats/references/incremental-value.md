# Incremental value — testing the added information and its intended use

Define the claim before choosing a test: added outcome information during model development,
improved prediction on independent patients, or higher decision-analytic net benefit under a
specified action. These are distinct questions. A higher AUC point estimate alone is insufficient.

## The discipline

- Name the primary comparator (e.g. current clinical model) and the added feature/modality.
  Include the imaging-only and clinical-only components when a fusion/complementarity claim needs
  them. Improvement over one component does not establish improvement over the other; superiority
  over both is not required for a narrower, explicitly comparator-specific claim.
- Use the same evaluation patients, outcome definition and resampling partitions for paired model
  comparison. Report missing-modality selection and the comparable population. A comparison across
  different cohorts mixes model effects with case-mix effects.
- Record whether models are nested, how they were fit/selected, and whether predictions are apparent,
  out-of-fold or from a frozen model on independent data. A shared patient ID alone does not establish
  the assumptions of a particular comparison test.

## The evidence package

| Element | Method | What it shows |
|---|---|---|
| Binary ROC discrimination on independent evaluation cases | Paired DeLong for its ordinary binary-ROC setting, or a justified paired/cluster bootstrap | ΔAUC with CI for frozen scores; account for patient clusters |
| Censored survival discrimination | Censoring-aware comparison of the prespecified C-index or time-dependent AUC, with paired subject-level uncertainty | Define estimator, horizon, comparable pairs and censoring assumptions; ordinary ROC DeLong is not a test for censored C-index differences |
| Added information in fitted nested regression | Standard **likelihood-ratio test** only for compatible nested likelihood models fitted on the same development observations with its regularity assumptions | Conditional association during development, not external predictive gain |
| Calibration and overall prediction error | Calibration slope/intercept/curve, and an outcome-appropriate Brier score with uncertainty | Report calibration separately from overall error and explain any trade-off |
| Decision-analytic net benefit, when an action is defined | **DCA**: paired net-benefit difference over a justified, prespecified threshold range | Model-based consequences under stated assumptions, not observed clinical utility |
| Reclassification, optional auxiliary analysis | A justified NRI/IDI definition with uncertainty | Only when it adds an interpretable question beyond the primary performance measures |

- **Same-data nested fitting:** do not use ordinary DeLong on apparent fitted scores as an automatic
  test of added information. Model estimation and the nested null can invalidate that test. Use a
  justified nested-model association test where applicable; estimate predictive performance with
  the prespecified validation/optimism procedure.
- **Selected, penalized or non-likelihood models:** do not automatically use a standard chi-square
  LRT or compare arbitrary software likelihoods. State selection/penalty and model assumptions;
  use a validated inference method or limit the comparison to appropriately validated prediction.
- **Out-of-fold predictions:** preserve the shared training/selection dependence. An ordinary DeLong
  test on pooled out-of-fold scores does not automatically include development uncertainty; use a
  justified procedure that repeats the relevant fitting/selection when that uncertainty is targeted.
- **External evaluation:** apply frozen models and compare their predictions. Do not repeat a
  development LRT on frozen external predictions; they are not maximum-likelihood fits to that
  cohort. Fitting a calibration diagnostic is allowed without changing model predictions; any
  recalibration/update is separate and needs further protected evaluation for the updated model.
- **Decision gate:** require population, action, comparator strategies, threshold meaning, error
  consequences and censoring/competing-event handling before DCA. Otherwise omit it and bound the
  claim to association/prediction. Positive net benefit does not demonstrate patient benefit,
  workflow impact or observed clinical utility (see [model evaluation](model-evaluation.md)).

```r
# Development only: prespecified, unpenalized compatible nested likelihood models,
# fit to identical observations; verify regularity/selection assumptions first.
anova(fit_clinical, fit_combined, test = "LRT")
# Independent evaluation: frozen binary scores on the same independent cases.
# Not censored survival, apparent nested fits, or an automatic pooled-CV test.
pROC::roc.test(roc_clinical, roc_combined, method = "delong", paired = TRUE)
```

## NRI / IDI — correct use and abuse

Correct use:

- Do not default to **category-free (continuous) NRI**. It counts arbitrarily small upward/downward
  changes equally and can overstate a clinically unimportant increment; calibration alone does not
  resolve that limitation. Omitting NRI/IDI is acceptable.
- If category NRI answers a real decision question, freeze clinically meaningful categories first;
  report event and nonevent components separately and show the reclassification table. Do not read
  the overall NRI as the percentage of all patients correctly reclassified.
- Check calibration of both models, target prevalence, outcome/horizon and censoring assumptions.
  IDI depends on the risk-distribution setting; neither metric is a universal clinical-effect scale.
- Report a justified bootstrap CI that preserves pairing/hierarchy and includes fitting/selection
  uncertainty when relevant. Keep NRI/IDI auxiliary; neither establishes utility or rescues an
  otherwise unsupported claim.

Abuse list (reviewer red flags):

- NRI/IDI reported without a confidence interval.
- Category NRI with self-selected cutpoints.
- NRI used to rescue a non-significant ΔAUC with no calibration or net-benefit support.
- Reclassification computed on the training data only.

## Reporting template

*"On [independent evaluation population], the frozen combined model was compared with [primary
comparator]. The difference in [prespecified performance measure] was [estimate and CI, named
method]. Calibration and overall prediction error were [verified results]. [If applicable:
decision-analytic net benefit differed by [results] over the prespecified [range], under [action
and consequence assumptions]; observed clinical impact was not evaluated.]"*

Fill every value from real output; never copy the magnitudes.

## If the combined model does not win

A combined model that does not beat its components is a result, not a failure — simplify the
model or reframe the paper (→ `radiology-design/weak-result-pivot.md`, exit 4).

## Reviewer hot-spots

Combined compared only against the weaker component; AUCs from different patient subsets;
NRI/IDI as the sole increment evidence; calibration worse in the combined model and not
discussed; increment claimed on training data with no validation.

## Primary methodological sources

- Demler OV, et al. [Misuse of DeLong test to compare AUCs for nested models](https://pmc.ncbi.nlm.nih.gov/articles/PMC3684152/).
- Kerr KF, et al. [Net reclassification indices for evaluating risk prediction instruments: a critical review](https://pubmed.ncbi.nlm.nih.gov/24240655/).
- Han X, et al. [On comparing two correlated C indices with censored survival data](https://pmc.ncbi.nlm.nih.gov/articles/PMC5909734/).

Checked 2026-09-04. These sources resolve specific method assumptions; their publication dates are
not universal rules requiring or prohibiting every possible future estimator.
