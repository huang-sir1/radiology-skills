[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$skillRoot = Split-Path -Parent $PSScriptRoot
$testsPath = Join-Path $skillRoot 'tests/evaluation-cases.json'
$tests = Get-Content -LiteralPath $testsPath -Raw | ConvertFrom-Json

$errors = [System.Collections.Generic.List[string]]::new()

foreach ($relativePath in $tests.required_files) {
    $target = Join-Path $skillRoot $relativePath
    if (-not (Test-Path -LiteralPath $target -PathType Leaf)) {
        $errors.Add("Missing required file: $relativePath")
    }
}

$skillText = Get-Content -LiteralPath (Join-Path $skillRoot 'SKILL.md') -Raw
$referenceText = Get-Content -LiteralPath (Join-Path $skillRoot 'references/parameter-and-methodology-evaluation.md') -Raw
$templateText = Get-Content -LiteralPath (Join-Path $skillRoot 'templates/parameter-methodology-evaluation-matrix.md') -Raw
$runtimeText = $skillText + "`n" + $referenceText + "`n" + $templateText

$requiredPhrases = @(
    'name: radiology-method-evaluation',
    'parameters/settings',
    'evaluation metrics/readouts',
    'methodology',
    'PLANNED',
    'AUTHOR_REPORTED',
    'PARTLY_VERIFIED',
    'VERIFIED',
    'NOT_ASSESSABLE',
    'PASS',
    'CONDITIONAL',
    'STOP',
    'Do not average',
    'test set',
    'independent unit',
    'tuning budget',
    'experimental-design factors',
    'distinct analysis',
    'Methods',
    'Results',
    'Supplement',
    'Discussion',
    'AUTHOR_INPUT_NEEDED'
)
foreach ($phrase in $requiredPhrases) {
    if ($runtimeText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing required scientific contract phrase: $phrase")
    }
}

$positiveCases = @($tests.positive_cases)
$boundaryCases = @($tests.boundary_cases)
$allIds = @($positiveCases.id + $boundaryCases.id)
if (($allIds | Sort-Object -Unique).Count -ne $allIds.Count) {
    $errors.Add('Evaluation case IDs must be unique.')
}

$allowedModes = @('plan', 'audit', 'interpret', 'writing-package')
$allowedFocus = @('parameters', 'evaluation-metrics', 'methodology', 'combined', 'writing', 'verification')
foreach ($case in $positiveCases) {
    if ($case.mode -notin $allowedModes) {
        $errors.Add("Case $($case.id) has invalid mode: $($case.mode)")
    }
    if ($case.focus -notin $allowedFocus) {
        $errors.Add("Case $($case.id) has invalid focus: $($case.focus)")
    }
    if ([string]::IsNullOrWhiteSpace($case.prompt) -or @($case.required_checks).Count -lt 3) {
        $errors.Add("Case $($case.id) needs a prompt and at least three required checks.")
    }
}

$requiredModalities = @(
    'radiomics', 'deep-imaging', 'bulk-rna', 'single-cell', 'spatial',
    'pathology', 'multi-omics', 'perturbation', 'imaging-mechanism'
)
foreach ($modality in $requiredModalities) {
    if ($modality -notin @($positiveCases.modality)) {
        $errors.Add("Missing positive modality coverage: $modality")
    }
}
foreach ($focus in $allowedFocus) {
    if ($focus -notin @($positiveCases.focus)) {
        $errors.Add("Missing positive focus coverage: $focus")
    }
}

$requiredBoundaryOwners = @(
    'radiology-stats', 'radiology-deep-learning', 'radiology-writing',
    'radiology-prereview', 'radiology-submission'
)
foreach ($owner in $requiredBoundaryOwners) {
    if ($owner -notin @($boundaryCases.expected_owner)) {
        $errors.Add("Missing boundary owner coverage: $owner")
    }
}

if (@($tests.invariants).Count -lt 7) {
    $errors.Add('At least seven scientific invariants are required.')
}

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology-method-evaluation validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-method-evaluation validation' -ForegroundColor Green
Write-Host "Static contract cases: $($positiveCases.Count)"
Write-Host "Boundary cases: $($boundaryCases.Count)"
Write-Host "Scientific invariants: $(@($tests.invariants).Count)"
Write-Host "Modalities covered: $($requiredModalities.Count)"
Write-Host 'Note: static validation does not execute case prompts or prove model behavior.'
