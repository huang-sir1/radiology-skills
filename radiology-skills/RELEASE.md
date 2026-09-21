# Standalone release boundary

Publish this product from an allowlisted source tree. The research corpus, downloaded articles,
OCR intermediates, dependency caches and local audit products are development evidence, not plugin
runtime assets and may have separate redistribution rights.

## Allowed release surface

The single release allowlist is `release-allowlist.txt`. It contains the Claude and Codex plugin
manifests, all 40 standalone `skills/`, the behavior-evaluation harness, user documentation, license
and release validators. It is an exact top-level set: unapproved additions, rooted/dot/parent paths,
reparse points, hidden/system/dot-prefixed payloads and forbidden generated or executable artifacts
fail the gate. Do not package
the repository by recursively zipping the current working directory. The validator fails when an
allowlisted path contains development/cache directories, Python caches, compiled binaries or local
log/temp artifacts named in the exclusion contract; it does not silently treat a dirty source tree
as a clean release. It also requires `.claude-plugin/plugin.json`, its marketplace entry and
`.codex-plugin/plugin.json` to agree on name, version and description, and requires all 40 modules to
contain `SKILL.md` plus `agents/openai.yaml`.

Run before creating a tag or archive:

```powershell
$ReleasePython = 'C:\Users\<你的用户名>\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
pwsh -NoProfile -File scripts/validate_release_boundary.ps1 `
    -ProductRoot 'C:\radiology-Skill' `
    -PythonExecutable $ReleasePython
```

This fail-closed command runs the Codex skill-creator `quick_validate.py` for every skill, validates
the Codex plugin and every `agents/openai.yaml`, parses release JSON/YAML without duplicate JSON keys,
checks local Markdown links, runs discovered Python regression tests and PowerShell skill-contract
validators, and enforces the allowlisted archive boundary. The exact Python-test and PowerShell-
validator paths are frozen in `scripts/release-test-inventory.json`; missing or unregistered gates
fail rather than producing a zero-test pass. It requires the locally installed Codex
`skill-creator` and `plugin-creator` validators; their paths may be supplied explicitly with
`-QuickValidatePath` and `-PluginValidatorPath` when Codex is installed elsewhere.
The Python preflight requires Python 3.10+ and successful imports of `yaml`, `pypdf` and `Pillow`.
The path
above is the interpreter verified on this workstation; another machine must supply its own real
interpreter path rather than copying this machine-specific path blindly.

The official builder copies only the allowlist into a new, non-existing staging directory, reruns
the complete gate inside that clean copy, emits a per-file size/SHA-256 manifest and release-tree
digest, records the Python dependencies and hashes of the two external validators, and can create a
deterministic ZIP plus archive SHA-256:

```powershell
& $ReleasePython scripts/build_release.py `
    --source-root 'C:\radiology-Skill' `
    --staging-dir 'C:\radiology-release-staging\radiology-skill-vNEXT' `
    --python $ReleasePython `
    --archive 'C:\radiology-release-staging\radiology-skill-vNEXT.zip'
```

The receipt is a structural identity record, not an authenticated behavior or scientific release
decision. Never reuse an existing staging/archive path: the builder fails instead of overwriting it.
The current workspace's
`.git` state is not evidence that a release repository exists; verify `git status` and the intended
remote before committing or publishing.

The pipeline adversarial-case validator and `behavior-evals/` asset tests validate registries,
schemas, prompt hashes and receipt mechanics only. They do not execute prompts against a model. A
release evaluation must run the frozen `behavior-evals/cases.json` prompts against the packaged
Skill, preserve raw output files and SHA-256s, and obtain qualified human adjudication before making
a behavioral-performance claim. The bundled validator does not authenticate a reviewer identity,
qualification or signature, so `release_claim_eligible` remains `false` even for a structurally
complete human-adjudication record; a trusted signed release decision is external to this harness.
No such authenticated claim is bundled in this release tree.

## Explicit exclusions

- `research/` and `tmp/`, including downloaded PDFs and derived text/OCR artifacts;
- `node_modules`, vendored local runtimes and compiled scientific/Python binaries;
- `__pycache__`, `.pyc`, local logs, temporary render output and audit caches;
- credentials, controlled data, patient data and institution-only experience records populated
  from the blank templates.

Public release templates must remain blank or synthetic. Populate local experience registries only
in an institution-controlled copy unless their evidence and permissions have been reviewed.
