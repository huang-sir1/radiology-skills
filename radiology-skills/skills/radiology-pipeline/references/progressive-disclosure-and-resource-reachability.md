# Progressive disclosure and resource reachability

The product exposes only each skill's `name` and concise `description` during discovery, loads
`SKILL.md` after selection, and opens a reference/template/script only when the entrypoint or an
already selected resource names it. Breadth belongs in reachable resources, not in an ever-growing
discovery string or entrypoint.

## Machine gates

`scripts/test_progressive_disclosure_contracts.py` enforces:

- a 4500-character aggregate discovery budget inside the platform's 5000-character ceiling;
- a conservative 5400-unit entrypoint ceiling computed as the larger of UTF-8 bytes/4 and
  whitespace words × 1.35;
- graph reachability of every runtime reference, template, asset and invoked script from the local
  `SKILL.md`; and
- canonical routing rather than links to legacy per-skill README files.

The context unit is explicitly a dependency-free surrogate, not a claim about an exact host-model
tokenizer. The design target remains below roughly 5000 tokens; when the surrogate approaches its
hard ceiling, move detailed schemas, examples and long checklists into conditionally opened files.

## Boundary

Reachability proves that a resource can be discovered through declared local instructions. It does
not prove that a model selected it correctly, that the resource is scientifically valid, or that a
host enforces permissions. Fields such as experimental `allowed-tools` metadata are not advertised
as a security boundary; state-changing actions still require the host's real authorization and an
execution receipt.

## Design provenance

- [Agent Skills specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx)
  defines metadata -> `SKILL.md` -> on-demand resources as progressive disclosure and recommends
  shallow file references.
- [Anthropic skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)
  likewise separates entry instructions from conditionally loaded resources and emphasizes
  behavior evaluation during iteration.

These projects informed the topology and test questions; they are not runtime dependencies and do
not validate this product's scientific content.
