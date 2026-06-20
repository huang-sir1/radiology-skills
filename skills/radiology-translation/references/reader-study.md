# Reader (MRMC) study design

The standard evidence that AI changes radiologist performance. Design it so a biostatistician
accepts it; compute it with `radiology-stats`.

## Core design (multi-reader multi-case, MRMC)

- **Readers:** multiple radiologists spanning experience levels; report n and years.
- **Cases:** enough cases **and** readers for MRMC power (variance comes from both); pre-specify.
- **Arms:** radiologist **alone** vs radiologist **+ AI** (and optionally AI alone).
- **Washout:** separate the two readings (e.g. ≥4 weeks) so memory doesn't contaminate.
- **Randomisation:** randomise case order and arm assignment; counterbalance.
- **Blinding:** readers blinded to reference standard and to study hypothesis where possible.

## Outcomes

- Primary: change in performance (e.g. ΔAUC, sensitivity/specificity at a clinical threshold) —
  MRMC (Obuchowski-Rockette / DBM) → radiology-stats.
- Secondary: reading **time**, **confidence**, agreement, and harms (e.g. automation-induced
  errors).

## What reviewers check

- Are there enough readers **and** cases (not 3 readers on 50 cases)?
- Washout and randomisation present?
- Real prevalence / spectrum, or enriched (and acknowledged)?
- Reference standard independent of the AI and of the readers?
- Statistic accounts for reader **and** case variance (MRMC), not a naive average?

## Sequential vs fully-crossed

- **Fully-crossed:** every reader reads every case in both arms — strongest, costlier.
- State the design and why; the statistic must match it.

## Reporting sentence

*"In a fully-crossed MRMC study, [N] radiologists (range of experience) read [M] cases with and
without AI assistance, in randomised order with a 4-week washout. The primary outcome was the
change in AUC analysed with the Obuchowski-Rockette method; reading time and confidence were
secondary."*

## Handoff
MRMC power and analysis → `radiology-stats`; reader-study reporting (CLAIM, DECIDE-AI for
decision-support, CONSORT-AI for trials) → `radiology-reporting`; plots → `radiology-figure`.
