# Biosafety, biosecurity and dual-use review

Use this reference to classify oversight and create a safe handoff for biological materials, genetic
manipulation or credible misuse risk. It deliberately stays at governance level. It must not be used
to create a laboratory SOP, assign containment, select conditions or provide operational pathogen or
toxin instructions.

## 1. High-level routing screen

Ask only what is needed to identify the local owner:

| Trigger category | Facts to obtain from the author | Default route to confirm locally |
|---|---|---|
| recombinant/synthetic nucleic-acid or gene-editing work | system/material class, site, funding/regulatory context and whether an institutional determination exists | IBC / institutional biosafety office / equivalent |
| viral or non-viral vector use | vector class and host/system at a high level; approved facility and record | IBC/equivalent; add human or animal branch as applicable |
| human/animal specimens with potential infectious risk | source, material class, known/unknown status, transfer/site and local risk record | biosafety officer/IBC/equivalent plus source ethics route |
| biological agents, toxins or genetically modified organisms | broad category, site and current local approval/registration only | IBC/equivalent and any regulator/facility owner identified locally |
| proposed environmental release, field deployment or cross-border transfer | broad material/activity class and destination | institutional biosafety, regulator and legal/material-transfer owners |
| methods, materials, models, data or results with credible high-consequence misuse potential | non-actionable summary of the concern and whether designated review occurred | institutional biosecurity/dual-use review entity, funder/regulator as applicable |

Do not decide that work is exempt, low risk or at a particular containment level from a conversational
description. Record `UNKNOWN_AUTHOR_INPUT_NEEDED` and route to the authorized local owner.

## 2. Governance evidence

Capture without inference:

- IBC/equivalent committee or biosafety-office name and responsible contact role;
- approval, registration, notification or exemption-determination identifier;
- version, decision and relevant dates;
- approved site/facility, investigator, system/material and high-level activity scope;
- locally assigned containment and work-practice requirements by reference to the controlled record,
  not by reproducing them;
- personnel training/occupational-health dependencies and current status;
- material-transfer/import/export or sponsor/regulator dependencies where applicable;
- amendment, incident, exposure, loss or deviation records and institutional closure;
- separate dual-use/biosecurity review and responsible-communication decision when applicable.

The exact containment level, engineering control and incident response are institution-only facts and
remain with trained local personnel.

## 3. Dual-use and high-consequence screen

At a non-operational level, ask:

1. Could the planned methods, materials, model, dataset or result reasonably enable serious misuse?
2. Would sharing detailed methods, code, model weights or data materially increase that risk?
3. Has the designated institutional owner documented applicability, risk-benefit review and a
   communication/access plan under the **current** policy?

If the answer to 1 or 2 is `yes` or genuinely uncertain and 3 is absent, return `STOP` for detailed
design assistance and unrestricted dissemination. Provide no threat-enabling explanation. Route the
non-actionable project summary to the local biosecurity/dual-use owner and request the documented
decision. A publication plan may require controlled access, staged disclosure or institutional review,
but this skill does not independently impose or waive those measures.

Policies in this area change. Verify the current institutional and jurisdictional source at the time of
use. For example, the NIH Office of Science Policy maintains a live biosafety/biosecurity policy entry
point at <https://osp.od.nih.gov/policies/biosafety-and-biosecurity-policy/>; it is not proof that a
specific project is covered, exempt or approved. WHO's risk-based biosafety programme entry point is
<https://www.who.int/publications/i/item/9789240011434>. Local authority remains controlling.

## 4. STOP conditions

Stop the affected work or assurance claim when:

- IBC/equivalent applicability, approval, registration or exemption status is unknown;
- the approved record is missing, expired, suspended, conflicting or outside the material/site/activity
  scope;
- locally required facility, containment, training or occupational-health confirmation is absent;
- a material change, transfer, incident or deviation lacks required review/closure;
- human or animal work is present but its parallel branch is unresolved;
- credible dual-use/high-consequence risk lacks designated institutional review;
- the request seeks a workaround, evasion or operational instructions for hazardous work.

Do not “repair” these gaps with cautious wording. Identify the owner and closure record, and withhold
text that claims compliant authorization.

## 5. Safe writing package

Use only document-supported placeholders:

```text
The [high-level biological/genetic activity] was reviewed by [IBC / institutional biosafety office /
equivalent full name] at [institution] under record [AUTHOR_INPUT_NEEDED], covering [site, system/
material and high-level activity scope] for the reported study period. Facility, training and risk-
management requirements followed the current institutionally approved record. [If applicable:
responsible communication/access was reviewed by <designated institutional owner>, decision
<AUTHOR_INPUT_NEEDED>.]
```

Do not include sensitive operational detail merely to make the ethics statement sound complete.
Methods detail must remain scientifically adequate while respecting the documented institutional
communication plan and journal requirements.

## 6. Safe handoffs

- Human participants, tissue source, consent or privacy -> `human-subjects` branch.
- Live animals or animal welfare endpoints -> `animal-welfare` branch.
- Experimental rationale and non-hazardous design structure -> `radiology-experiment-design` only
  after STOP gates are closed.
- Containment assignment, local SOP, incident response, veterinary care, legal interpretation and
  dual-use determination -> authorized current local owners, never another writing skill.
