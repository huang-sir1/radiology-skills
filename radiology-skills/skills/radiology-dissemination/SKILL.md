---
name: radiology-dissemination
description: "Create traceable posters, conference abstracts, summaries and media; not papers, decks or figures."
---

# Radiology Dissemination

Use this skill to translate a frozen research evidence base into an audience-specific communication
product without inflating its scientific maturity. It owns the communication decision, audience
action, claim-source trace, release risks and channel adaptation. It does not own the underlying
analysis, manuscript, standalone scientific figure, slide deck or institutional release authority.

## Non-negotiable boundaries

- **Audience action before format.** Name who should understand, discuss, decide or do what after
  receiving the product. Awareness is not an action unless the user explicitly wants awareness.
- **One evidence base, multiple honest summaries.** Every material sentence resolves through a
  `claim-source ledger` to a frozen artifact and evidence state. Simpler wording may reduce detail;
  it may not increase certainty, causality, generalisability, clinical utility or deployment status.
- **Plan is not product.** Record `PLAN_ONLY`, `DRAFT_TEXT`, `CREATE_ARTIFACT` or `AUDIT`. A content
  plan is not an abstract submission, poster file, published brief, press release or social post.
  Create or publish an artifact only when explicitly requested and authorized.
- **Current venue and channel rules are live facts.** Verify word limits, formats, deadlines,
  embargoes, disclosures, copyright grants and accessibility requirements from the named current
  source. Otherwise mark `LIVE_RULE_UNVERIFIED` and do not claim release readiness.
- **Privacy and rights are independent gates.** PHI removal, participant consent/governance,
  copyright ownership, license scope, attribution and venue reuse permission each require evidence.
  A citation is not reuse permission; a PowerPoint crop or black box is not de-identification.
- **Public communication is not medical advice.** Explain population-level evidence and uncertainty;
  do not diagnose, recommend an examination or change an individual patient's care.
- **No promotional laundering.** Citation counts, statistical significance, regulatory status,
  preliminary findings or market interest do not by themselves establish patient benefit.

## Input passport

Before drafting, record in the [dissemination brief](templates/dissemination-brief.md):

- mode, artifact scope, audience, literacy/language needs and intended action;
- venue/channel, deadline, length/format, review chain, embargo and disclosure rules;
- project/material version, evidence maturity, Claim IDs and source-owner approvals;
- population, setting, comparator, denominators, uncertainty, limitations and unresolved findings;
- image provenance, modality/sequence/view, orientation/laterality, transformations and caption state;
- PHI/consent/governance, copyright/license/attribution and accessibility state;
- whether the deliverable is internal, participant-facing, clinical, public, policy or media-facing.

If the evidence base is not frozen, retain `SOURCE_LOCK_MISSING`; produce only a bounded planning
brief and return the missing inputs to the scientific owner.

## Route by mode

| Need | Mode | Read | Primary output |
|---|---|---|---|
| Scientific meeting poster | `conference-poster` | [modes-and-audience-actions.md](references/modes-and-audience-actions.md), [rights-privacy-accessibility.md](references/rights-privacy-accessibility.md) | poster content architecture, claim/image ledger and production brief |
| Meeting or congress abstract | `conference-abstract` | [modes-and-audience-actions.md](references/modes-and-audience-actions.md), then verify the current call | structured abstract draft and compliance gaps |
| Plain-language research summary | `plain-language-summary` | [modes-and-audience-actions.md](references/modes-and-audience-actions.md) | stand-alone question/findings/limits summary |
| Participant, patient or public explanation | `patient-public-explanation` | both references above | actionable explanation with safety and uncertainty boundary |
| Evidence brief for clinicians or service leaders | `clinical-evidence-brief` | [modes-and-audience-actions.md](references/modes-and-audience-actions.md) | decision-context evidence brief, not a guideline |
| Policy brief | `policy-brief` | [modes-and-audience-actions.md](references/modes-and-audience-actions.md) | problem/options/evidence/implementation brief |
| Press release or social-media package | `press-social` | both references above and live embargo/channel rules | bounded media copy, caveats, links and release gate |
| Correct, reissue, withdraw or update an already released derivative | `derivative-lifecycle` | [modes-and-audience-actions.md](references/modes-and-audience-actions.md) (correction/contact route and released-wording archive), then the same release gates | affected-derivative ledger, corrected artifact plan and release/withdrawal plan |

Use the [source registry](references/source-registry.md) to choose authoritative guidance and verify
every entry marked `LIVE_VERIFICATION_REQUIRED`. Do not load every reference for a narrow request.

## STOP gates

Return an explicit STOP state before external release when any applies:

- `STOP_SOURCE`: a material claim lacks a resolvable source, denominator, uncertainty or owner;
- `STOP_CLAIM`: wording exceeds the frozen evidence state or hides a negative/discordant result;
- `STOP_PHI`: pixels, metadata, filenames, notes, hidden content or linked files may expose PHI;
- `STOP_RIGHTS`: ownership, permission, license, attribution or participant image reuse is unresolved;
- `STOP_EMBARGO`: journal, meeting, sponsor or institutional publicity timing is unresolved;
- `STOP_ACCESSIBILITY`: the intended public channel lacks a reasonable accessible alternative;
- `STOP_AUTHORITY`: institutional, sponsor, patient-communications, policy or media approval is absent;
- `STOP_SAFETY`: copy could reasonably be read as individual clinical advice or autonomous use.

A STOP blocks release, not safe internal analysis or a clearly labelled repair plan.

## Workflow and output contract

1. Lock the passport, artifact scope and intended audience action.
2. Build the [claim-source ledger](templates/claim-source-ledger.md); preserve source wording,
   evidence state, population, effect/accuracy, uncertainty, limitations and permitted reuse.
3. Choose the mode-specific information order. Keep results, interpretation, recommendation and
   proposed action distinct.
4. Adapt language, numbers and images without changing scientific meaning. Explain absolute risk,
   prevalence and false-positive/false-negative consequences when relevant.
5. Run scientific, privacy, rights, accessibility, venue and release-authority gates separately.
6. Return: `Scope and audience`, `Evidence/claim ledger`, `Draft or production brief`, `Radiology
   image ledger`, `Risk and STOP ledger`, `Live-rule verification`, and `Release status`.

Release status is one of `PLAN_COMPLETE`, `DRAFT_FOR_SCIENTIFIC_REVIEW`,
`READY_FOR_AUTHORIZED_PRODUCTION`, `READY_FOR_AUTHORIZED_RELEASE`, or `STOP`. For a derivative
already released, the same gates govern correction, reissue, withdrawal or update: preserve the
released wording/version archive and a correction/contact route, and record the affected-derivative
ledger and release/withdrawal plan before any external action.

## Handoffs and non-ownership

- Slide decks and PPTX, including talks and proposal defences → `radiology-paper2ppt`.
- Standalone scientific figures and quantitative plots → `radiology-figure`; tables →
  `radiology-table`; manuscript sections → `radiology-writing`.
- Scientific reporting checklist selection → `radiology-reporting`; evidence synthesis and its
  conclusions → `radiology-systematic-review`; corpus retrieval → `radiology-search`.
- Disease pathway/reference-standard truth → `radiology-clinical-domain`; image measurement and
  acquisition validity → `radiology-acquisition-qc`; data/consent/governance →
  `radiology-data` / `radiology-ethics`.
- Final press, policy, patient-facing or institutional release remains with the authorized human
  communications, clinical, legal, sponsor or policy owner. This skill cannot submit or publish.
