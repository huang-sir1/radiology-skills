[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$skillRoot = Split-Path -Parent $PSScriptRoot
$testsPath = Join-Path $skillRoot 'tests/routing-cases.json'
$tests = Get-Content -LiteralPath $testsPath -Raw | ConvertFrom-Json

$errors = [System.Collections.Generic.List[string]]::new()

foreach ($relativePath in $tests.required_files) {
    $target = Join-Path $skillRoot $relativePath
    if (-not (Test-Path -LiteralPath $target -PathType Leaf)) {
        $errors.Add("Missing required file: $relativePath")
    }
}

$runtimeFiles = @(
    'SKILL.md',
    'agents/openai.yaml',
    'references/evidence-synthesis-routing.md',
    'references/review-methods-and-quality-gates.md',
    'templates/systematic-review-protocol.md',
    'templates/data-extraction-and-synthesis-matrix.md',
    'templates/risk-of-bias-applicability-matrix.md'
)
$runtimeText = ($runtimeFiles | ForEach-Object {
    Get-Content -LiteralPath (Join-Path $skillRoot $_) -Raw
}) -join "`n"

$requiredPhrases = @(
    'name: radiology-systematic-review',
    'Protocol first',
    'PICO',
    'PIRD',
    'CHARMS',
    'prevalence-incidence-meta',
    'observational-association-meta',
    'reliability-agreement-method-comparison-meta',
    'numerator',
    'person-time',
    'correlation is not agreement',
    'registration status',
    'search-strategy peer-review receipt',
    'REVIEWED_CLOSED',
    'STATIC',
    'LIVING',
    'RETIRED',
    'radiology-search',
    'independent',
    'conflict resolution',
    'PRISMA',
    'Study-family ID',
    'risk of bias',
    'applicability',
    'pooling-feasibility',
    'POOL',
    'STRATIFY',
    'NARRATIVE',
    'STOP_FOR_REPAIR',
    'pseudoreplication',
    'heterogeneity',
    'subgroup',
    'sensitivity',
    'small-study',
    'publication bias',
    'GRADE',
    'certainty',
    'claim ceiling',
    'radiology-citation',
    'radiology-stats',
    'radiology-reporting',
    'radiology-writing',
    'AUTHOR_INPUT_NEEDED',
    'PLANNED',
    'VERIFIED',
    'NOT_ASSESSABLE'
    'tool, model, prompt and version'
    'pilot/calibration'
    'low-priority exclusion audit'
    'recall safeguard'
    'human override'
    'final human responsibility'
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
    $errors.Add('Routing case IDs must be unique.')
}

$allowedModes = @('protocol', 'audit', 'mentor', 'synthesis-handoff', 'writing-handoff')
$allowedRoutes = @(
    'scoping',
    'systematic-narrative',
    'diagnostic-accuracy-meta',
    'prevalence-incidence-meta',
    'observational-association-meta',
    'reliability-agreement-method-comparison-meta',
    'prediction-radiomics-ai-meta',
    'prognostic-meta',
    'intervention-meta',
    'omics-mechanism-synthesis'
)
foreach ($case in $positiveCases) {
    if ($case.mode -notin $allowedModes) {
        $errors.Add("Case $($case.id) has invalid mode: $($case.mode)")
    }
    if ($case.route -notin $allowedRoutes) {
        $errors.Add("Case $($case.id) has invalid route: $($case.route)")
    }
    if ([string]::IsNullOrWhiteSpace($case.prompt) -or @($case.required_checks).Count -lt 4) {
        $errors.Add("Case $($case.id) needs a prompt and at least four required checks.")
    }
}
foreach ($mode in $allowedModes) {
    if ($mode -notin @($positiveCases.mode)) {
        $errors.Add("Missing positive mode coverage: $mode")
    }
}
foreach ($route in $allowedRoutes) {
    if ($route -notin @($positiveCases.route)) {
        $errors.Add("Missing positive review-route coverage: $route")
    }
}

$requiredBoundaryOwners = @(
    'radiology-search',
    'radiology-citation',
    'radiology-stats',
    'radiology-reporting',
    'radiology-writing',
    'radiology-prereview'
)
foreach ($owner in $requiredBoundaryOwners) {
    if ($owner -notin @($boundaryCases.expected_owner)) {
        $errors.Add("Missing boundary owner coverage: $owner")
    }
}

if (@($tests.invariants).Count -lt 21) {
    $errors.Add('At least twenty-one scientific invariants are required.')
}

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology-systematic-review validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-systematic-review validation' -ForegroundColor Green
Write-Host "Static contract cases: $($positiveCases.Count)"
Write-Host "Boundary cases: $($boundaryCases.Count)"
Write-Host "Modes covered: $($allowedModes.Count)"
Write-Host "Review routes covered: $($allowedRoutes.Count)"
Write-Host "Scientific invariants: $(@($tests.invariants).Count)"
Write-Host 'Note: static validation does not execute case prompts or prove model behavior.'
