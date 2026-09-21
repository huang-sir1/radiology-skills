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
    'references/mechanism-experiment-workflow.md',
    'references/assay-control-matrix.md',
    'templates/mechanism-experiment-plan.md',
    'templates/local-assay-capability-profile.md',
    'templates/local-mechanism-validation-experience-registry.md',
    'templates/failure-decision-log.md'
)
$runtimeText = ($runtimeFiles | ForEach-Object {
    Get-Content -LiteralPath (Join-Path $skillRoot $_) -Raw
}) -join "`n"

$requiredPhrases = @(
    'name: radiology-experiment-design',
    'plan',
    'audit',
    'mentor',
    'interpret',
    'writing-handoff',
    'target engagement',
    'rescue',
    'experimental-design factors',
    'independent unit',
    'biological replicate',
    'technical replicate',
    'applicable context',
    'counterexample boundary',
    'randomization',
    'blinding',
    'dose',
    'time',
    'toxicity',
    'PASS',
    'CONDITIONAL',
    'STOP',
    'AUTHOR_INPUT_NEEDED',
    'radiology-radiogenomics',
    'radiology-method-evaluation',
    'radiology-stats',
    'radiology-ethics',
    'human-subjects',
    'animal-welfare',
    'biosafety-biosecurity',
    'IACUC',
    'IBC',
    'Approval in one branch does not authorize another',
    'radiology-writing',
    'Title/Abstract',
    'Data Availability',
    'Code Availability',
    'Reagent/Model Availability',
    'Source Data',
    'causal or translational upgrade'
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

$allowedModes = @('plan', 'audit', 'mentor', 'interpret', 'writing-handoff')
$requiredSystems = @('tissue', 'cell-line', 'organoid', 'animal', 'mixed')
foreach ($case in $positiveCases) {
    if ($case.mode -notin $allowedModes) {
        $errors.Add("Case $($case.id) has invalid mode: $($case.mode)")
    }
    if ($case.system -notin $requiredSystems) {
        $errors.Add("Case $($case.id) has invalid system: $($case.system)")
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
foreach ($system in $requiredSystems) {
    if ($system -notin @($positiveCases.system)) {
        $errors.Add("Missing positive system coverage: $system")
    }
}

$requiredBoundaryOwners = @(
    'radiology-radiogenomics',
    'radiology-method-evaluation',
    'radiology-stats',
    'radiology-ethics',
    'radiology-writing'
)
foreach ($owner in $requiredBoundaryOwners) {
    if ($owner -notin @($boundaryCases.expected_owner)) {
        $errors.Add("Missing boundary owner coverage: $owner")
    }
}

$ethicsBoundary = @($boundaryCases | Where-Object { $_.id -eq 'biosafety-and-animal-ethics' })
if ($ethicsBoundary.Count -ne 1 -or @($ethicsBoundary[0].required_handoff_checks).Count -lt 4) {
    $errors.Add('The biosafety-and-animal-ethics boundary must require a four-part three-branch governance handoff.')
}

if (@($tests.invariants).Count -lt 8) {
    $errors.Add('At least eight scientific invariants are required.')
}

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology-experiment-design validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-experiment-design validation' -ForegroundColor Green
Write-Host "Static contract cases: $($positiveCases.Count)"
Write-Host "Boundary cases: $($boundaryCases.Count)"
Write-Host "Scientific invariants: $(@($tests.invariants).Count)"
Write-Host "Modes covered: $($allowedModes.Count)"
Write-Host "Systems covered: $($requiredSystems.Count)"
Write-Host 'Note: static validation does not execute case prompts or prove model behavior.'
