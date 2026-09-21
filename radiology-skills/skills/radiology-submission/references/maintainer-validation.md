# Maintainer validation

This file is for maintainers changing the skill itself, not for agents auditing an author package.

After changing a journal route, evidence row, manifest schema or structural gate, run
`scripts/validate_submission_skill.py`. It requires all 11 profiles, blocks exemplar-derived hard
rules, checks source domains, verifies that every negative contract has an executable regression test,
executes the package-auditor regression suite, then runs the cross-step golden scenarios for intake,
routing, manifest audit and human-report rendering.

The current frozen validation evidence and published coverage boundary are recorded in
[validation-receipt-2026-08-22.md](validation-receipt-2026-08-22.md). The
validator also checks that receipt's machine-readable counts, byte lengths and SHA-256 values against
the current registries, templates, production scripts and test suites; a stale receipt is a validation
failure, not historical proof of the current code state. Refresh the receipt only after the full
regression and golden suites pass and the executable inputs are frozen.
