# Source freshness and normative-artifact governance

The machine-readable policy is [`../../../scripts/source-freshness-registry.json`](../../../scripts/source-freshness-registry.json).
It inventories every `source-registry.md`, records its last maintenance date in `accessed_on`, source class, volatility,
`max_age_days`, artifact-hash state, supersession state and the last online-verification state.

## What the offline release gate proves

- every source registry is declared exactly once;
- every source row carries its own ISO date in the `Accessed` column;
- neither registry maintenance nor source access is future-dated, no source access follows its
  registry maintenance date, and each source independently satisfies the age limit; and
- a missing normative-artifact SHA-256 remains explicitly `NOT_CAPTURED_LIVE_SOURCE`.

This is `OFFLINE_FRESHNESS_PASS`, not proof that a URL is reachable, an exact normative artifact is
current, a source is authoritative for the intended claim, or a rule applies to the project.

## Live verification states

An online gate must preserve materially different outcomes:

- `REACHABLE_EXACT_ARTIFACT`: exact artifact/version retrieved and, when retained, hashed;
- `HTTP_404_OR_410`: source reports removal;
- `NETWORK_UNAVAILABLE`: transport/DNS/TLS failure prevents a judgment;
- `RATE_LIMITED_403_OR_429`: access policy or throttling prevents a judgment;
- `PORTAL_OR_AUTH_REQUIRED`: public automation cannot reach the controlled source; and
- `NOT_RUN_OFFLINE`: no network claim was attempted by the release gate.

A reachable landing page is not verification of a linked guideline, call, standard or policy.
Version-specific use requires the normative identifier, exact artifact or section locator, access
date, supersedes/superseded-by relation and SHA-256 when the artifact may lawfully be retained.

## Refresh workflow

Before the age limit or at every live-use gate (whichever comes first): retrieve the exact official
source, classify the result above, record version/status and supersession, update only the Markdown
rows actually rechecked, then update `accessed_on` in the machine registry to the maintenance date.
Mixed access dates are expected after a partial refresh. Advancing the maintenance date does not
refresh older rows; their original access dates still drive staleness. Never stamp unvisited sources
with today's date or change only a validator's expected date. Publication dates and dates in URLs
are not access evidence.
