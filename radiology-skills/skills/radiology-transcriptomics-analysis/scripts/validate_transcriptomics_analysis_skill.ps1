[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$skillRoot = Split-Path -Parent $PSScriptRoot
$tests = Get-Content -LiteralPath (Join-Path $skillRoot 'tests/routing-cases.json') -Raw | ConvertFrom-Json
$errors = [System.Collections.Generic.List[string]]::new()

foreach ($relativePath in $tests.required_files) {
    if (-not (Test-Path -LiteralPath (Join-Path $skillRoot $relativePath) -PathType Leaf)) {
        $errors.Add("Missing required file: $relativePath")
    }
}

$runtimeText = @(
    'SKILL.md',
    'references/modality-execution-workflows.md',
    'references/runtime-and-reproducibility-contract.md',
    'templates/transcriptomics-analysis-plan.md',
    'templates/analysis-run-manifest.md',
    'templates/local-transcriptomics-runtime-profile.md',
    'templates/local-analysis-experience-registry.md',
    'templates/qc-decision-log.md'
) | ForEach-Object { Get-Content -LiteralPath (Join-Path $skillRoot $_) -Raw }
$runtimeText = $runtimeText -join "`n"

$requiredPhrases = @(
    'name: radiology-transcriptomics-analysis', 'PLAN_ONLY', 'CODE_READY', 'RUN_COMPLETE',
    'RUN_FAILED', 'AUDIT_ONLY', 'REPRODUCED', 'bulk RNA', 'sc/snRNA', 'spatial',
    'independent unit', 'pseudobulk', 'protected test', 'exact command', 'exit status',
    'artifact', 'AUTHOR_INPUT_NEEDED', 'inferred', 'not causal proof', 'FASTQ',
    'reference bundle', 'raw droplets', 'imaging-based spatial', 'mentor', 'writing-handoff',
    'minimum defensible', 'Abstract/title', 'local analysis experience'
)
foreach ($phrase in $requiredPhrases) {
    if ($runtimeText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing execution-contract phrase: $phrase")
    }
}

$positive = @($tests.positive_cases)
$boundary = @($tests.boundary_cases)
$ids = @($positive.id + $boundary.id)
if (($ids | Sort-Object -Unique).Count -ne $ids.Count) { $errors.Add('Case IDs must be unique.') }

$allowedModes = @('plan', 'build', 'run-audit', 'reproduce', 'interpret-handoff', 'mentor', 'writing-handoff')
$requiredModalities = @('bulk-rna', 'scrna', 'snrna', 'spatial')
foreach ($case in $positive) {
    if ($case.mode -notin $allowedModes) { $errors.Add("Invalid mode in $($case.id): $($case.mode)") }
    if ($case.modality -notin $requiredModalities) { $errors.Add("Invalid modality in $($case.id): $($case.modality)") }
    if ([string]::IsNullOrWhiteSpace($case.prompt) -or @($case.required_checks).Count -lt 4) {
        $errors.Add("Case $($case.id) needs a prompt and four checks.")
    }
}
foreach ($modality in $requiredModalities) {
    if ($modality -notin @($positive.modality)) { $errors.Add("Missing modality coverage: $modality") }
}
foreach ($mode in $allowedModes) {
    if ($mode -notin @($positive.mode)) { $errors.Add("Missing mode coverage: $mode") }
}

$requiredOwners = @('radiology-radiogenomics', 'radiology-method-evaluation', 'radiology-stats', 'radiology-experiment-design', 'radiology-writing')
foreach ($owner in $requiredOwners) {
    if ($owner -notin @($boundary.expected_owner)) { $errors.Add("Missing boundary owner: $owner") }
}
if (@($tests.invariants).Count -lt 10) { $errors.Add('At least ten invariants are required.') }

if ($errors.Count -gt 0) {
    Write-Host "FAIL: radiology-transcriptomics-analysis validation ($($errors.Count) issue(s))" -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-transcriptomics-analysis validation' -ForegroundColor Green
Write-Host "Static contract cases: $($positive.Count)"
Write-Host "Boundary cases: $($boundary.Count)"
Write-Host "Modes covered: $($allowedModes.Count)"
Write-Host "Modalities covered: $($requiredModalities.Count)"
Write-Host "Scientific invariants: $(@($tests.invariants).Count)"
Write-Host 'Note: static validation does not execute case prompts or prove model behavior.'
