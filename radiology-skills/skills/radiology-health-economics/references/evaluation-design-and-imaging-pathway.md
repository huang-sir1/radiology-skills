# Economic Evaluation Design and Imaging Pathway

Use for `scope-plan`, `trial-based-evaluation` and the pathway portion of
`model-based-evaluation`.

## 1. Decision-problem frame

Freeze a health-economic PICO plus decision fields:

- population and decision-relevant subgroups;
- imaging/intervention strategy and all relevant mutually exclusive comparators;
- setting, jurisdiction and decision maker;
- perspective and included cost sectors;
- time horizon long enough to capture material differences;
- health and non-health outcomes;
- policy/adoption question, reference case and decision threshold if applicable.

The comparator is current practice for the named decision context, not automatically “no imaging”
or the best published technology. Verify current practice live. Perspective controls which costs and
consequences enter; it cannot be decided after seeing the preferred result.

## 2. Choose the analysis type

| Analysis | Primary output | Suitable use | Boundary |
|---|---|---|---|
| CEA | incremental cost per natural health unit | same outcome is meaningful across strategies | natural units may not support allocation across disease areas |
| CUA | incremental cost per QALY | health-related length/quality effects and cross-program comparison | QALY valuation, mapping and local methods require explicit sources |
| cost-consequence | disaggregated costs and consequences | several outcomes matter and aggregation would hide trade-offs | does not itself produce one cost-effectiveness decision rule |
| BIA | annual budget change for a named budget holder | affordability, eligible population and uptake | not cost-effectiveness; read the BIA section in the other reference |
| VOI | expected value of reducing decision uncertainty | prioritising further evidence after a valid decision model | not a generic “more research is valuable” statement |

Cost minimisation is acceptable only when equivalent relevant outcomes are already well supported;
failure to detect a difference is not equivalence.

## 3. Imaging strategy-to-outcome bridge

Construct an explicit pathway:

`eligible population -> acquisition/test -> result state -> action -> treatment/monitoring ->
patient outcome and resource use`

Include when material:

- diagnostic, prognostic, triage, screening, monitoring or image-guided role;
- technically failed, nondiagnostic, equivocal and indeterminate examinations;
- sensitivity/specificity or other performance conditional on threshold and population;
- false-positive/false-negative action, repeat/confirmatory testing and delay;
- incidental findings and overdiagnosis where applicable;
- radiation, contrast, tracer, sedation and procedure consequences;
- capacity, waiting time, referral, reporting and escalation changes;
- downstream treatment effectiveness, adherence and monitoring;
- implementation drift, software/model updates and site capability.

Accuracy is an intermediate input. If no defensible downstream bridge exists, report a
cost-consequence or early model with the limitation; do not manufacture QALYs.

## 4. Costs and resource use

For each item record quantity, unit cost, source, jurisdiction, period, price year, currency,
inflation/conversion method, perspective, uncertainty and whether it is one-off or recurring.

Radiology-specific candidates:

- equipment acquisition, depreciation/annuitisation when required, room build, installation and
  acceptance;
- scanner/room time, technologist, radiologist, physicist, nursing and administrative time;
- contrast/tracer, supplies, dose monitoring, anaesthesia/sedation and adverse-event management;
- PACS/RIS/EHR integration, storage, networking, licence, vendor support, cybersecurity, QA,
  monitoring, retraining and updates;
- repeats, recalls, additional imaging, laboratory tests, biopsy/procedures and treatment;
- patient time/travel and productivity only under an inclusive perspective.

Do not equate minutes saved with cash released. State whether saved capacity is idle, redeployed,
used for additional throughput or actually reduces spending.

## 5. Outcomes, QALYs and ICERs

- State the utility instrument/source, respondent, valuation set, mapping and timing.
- Avoid double counting a test-process utility and downstream health-state utility.
- Report undiscounted and discounted quantities when the applicable reference case requires it.
- Order strategies by cost, remove strictly dominated strategies, assess extended dominance and
  compute ICERs against the next relevant non-dominated option.
- Dominant or dominated strategies should be described with incremental costs/effects; a negative
  ICER is not self-interpreting.
- Present incremental cost and outcome scatter/uncertainty. A point ICER alone is insufficient.
- A willingness-to-pay threshold is jurisdiction- and decision-specific. Never transfer one as a
  universal scientific constant.

## 6. Trial-based economic evaluation

Predefine resource-use collection, price year, missing-data handling, time horizon, utility timing,
within-trial and extrapolated components, clustering/repeated measures, censoring, subgroup
analyses and uncertainty. Preserve randomised assignment in the economic analysis.

Trial follow-up may be too short for downstream imaging consequences; any extrapolation becomes an
explicit model layer. Protocol-driven resource use may differ from routine practice. Report both the
observed trial evidence and the assumptions required for decision use.

## 7. Equity and stakeholder relevance

When the decision asks about unequal access or outcomes, describe subgroup prevalence, uptake,
test performance, downstream care and opportunity costs separately. Do not claim equity from equal
average performance. Patient/public involvement can improve relevance but does not validate utility
weights or the model; route qualitative work to `radiology-qualitative-mixed-methods`.
