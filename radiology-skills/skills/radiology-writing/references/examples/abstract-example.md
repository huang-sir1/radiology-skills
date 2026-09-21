# Worked example — structured abstract + Summary statement + Key Results

**All cohort details, settings, methods, numbers and findings below are synthetic teaching
placeholders, not real data or reusable evidence.** The example demonstrates shape only.

## Structured abstract
> **Background:** Preoperative identification of IDH mutation status in glioma informs
> management, but tissue sampling is invasive and may miss heterogeneity. **Purpose:** To
> evaluate whether an MRI radiomic model predicts IDH mutation status and to test it in an
> external cohort. **Materials and Methods:** In this retrospective study (January
> 2015–December 2021), 314 patients with newly diagnosed glioma and preoperative 3-T MRI
> were analyzed; IDH status from sequencing served as the reference standard. IBSI-compliant
> features were extracted from segmented tumor habitats (PyRadiomics v3.1); an elastic-net
> model was built with patient-level partition and 10×10 nested cross-validation, then
> validated externally (n = 96). The primary metric was AUC (DeLong CI); calibration and
> decision-curve analysis were assessed. **Results:** The model achieved an AUC of 0.88 (95%
> CI: 0.84, 0.92) internally and 0.85 (95% CI: 0.79, 0.90) externally, with a calibration
> slope of 0.96 and positive decision-curve net benefit at the prespecified example threshold
> probabilities of 0.10–0.40 under the stated hypothetical decision assumptions.
> **Conclusion:** In this synthetic example, frozen model performance was evaluated in a named
> external cohort; replacement of molecular testing, workflow benefit and patient benefit were not
> evaluated.

## Summary statement
> In this synthetic example, a frozen MRI radiomic model had an AUC of 0.85 in the named
> external test cohort; no clinical-use claim was evaluated.

## Key Results (≤ 75 words)
> - In 314 patients with glioma on 3-T MRI, the radiomic model predicted IDH status with an
>   AUC of .88.
> - In the named synthetic external-cohort example, the frozen model AUC was .85.
> - The example calibration slope was 0.96; decision-curve net benefit was positive only across
>   the prespecified hypothetical threshold range.

(Key Results carry summary data **without 95% CIs**, per the RSNA *Scientific Style Guide* —
the CIs stay in the abstract Results above. Bounded statistics shown in _Radiology_-final,
no-leading-zero form; → `radiology-polishing/stat-reporting.md`.)
