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

$runtimeFiles = @($tests.required_files | Where-Object { $_ -match '\.(md|yaml)$' })
$runtimeText = ($runtimeFiles | ForEach-Object {
    $target = Join-Path $skillRoot $_
    if (Test-Path -LiteralPath $target -PathType Leaf) {
        Get-Content -LiteralPath $target -Raw
    }
}) -join "`n"

$requiredPhrases = @(
    'name: radiology-ethics',
    'human-subjects',
    'animal-welfare',
    'biosafety-biosecurity',
    'IRB',
    'IACUC',
    'IBC',
    'equivalent',
    '3Rs',
    'dual-use',
    'gene editing',
    'potentially infectious',
    'author-only facts',
    'current local',
    'jurisdiction',
    'institution',
    'DOCUMENT_VERIFIED',
    'AUTHOR_REPORTED',
    'UNKNOWN_AUTHOR_INPUT_NEEDED',
    'CONFLICTING',
    'NOT_APPLICABLE_LOCAL_OWNER_CONFIRMED',
    'PASS',
    'CONDITIONAL',
    'STOP',
    'containment level',
    'dangerous experimental instructions',
    'responsible communication',
    'risk- and use-specific',
    'skull stripping is not a synonym or substitute for defacing',
    'measurement sensitivity',
    'controlled access alternative',
    'radiology-experiment-design',
    'radiology-data'
)
foreach ($phrase in $requiredPhrases) {
    if ($runtimeText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing required governance contract phrase: $phrase")
    }
}

$positiveCases = @($tests.positive_cases)
$boundaryCases = @($tests.boundary_cases)
$allIds = @($positiveCases.id + $boundaryCases.id)
if (($allIds | Sort-Object -Unique).Count -ne $allIds.Count) {
    $errors.Add('Routing case IDs must be unique.')
}

$allowedModes = @('classify', 'audit', 'draft', 'mentor', 'submission-handoff')
$allowedBranches = @('human-subjects', 'animal-welfare', 'biosafety-biosecurity')
foreach ($case in $positiveCases) {
    if ($case.mode -notin $allowedModes) {
        $errors.Add("Case $($case.id) has invalid mode: $($case.mode)")
    }
    $branches = @($case.branches)
    if ($branches.Count -eq 0) {
        $errors.Add("Case $($case.id) must name at least one branch.")
    }
    foreach ($branch in $branches) {
        if ($branch -notin $allowedBranches) {
            $errors.Add("Case $($case.id) has invalid branch: $branch")
        }
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
foreach ($branch in $allowedBranches) {
    $covered = $false
    foreach ($case in $positiveCases) {
        if ($branch -in @($case.branches)) { $covered = $true; break }
    }
    if (-not $covered) {
        $errors.Add("Missing positive branch coverage: $branch")
    }
}

$multiBranchCount = @($positiveCases | Where-Object { @($_.branches).Count -gt 1 }).Count
if ($multiBranchCount -lt 3) {
    $errors.Add('At least three positive cases must exercise parallel multi-branch review.')
}

$requiredBoundaryOwners = @(
    'authorized-local-biosafety-biosecurity-owner',
    'authorized-local-biosafety-owner',
    'authorized-local-animal-ethics-owner',
    'radiology-data',
    'radiology-experiment-design',
    'radiology-stats',
    'institutional-legal-compliance-owner',
    'authorized-local-veterinarian'
)
foreach ($case in $boundaryCases) {
    if ([string]::IsNullOrWhiteSpace($case.prompt) -or
        [string]::IsNullOrWhiteSpace($case.expected_owner) -or
        [string]::IsNullOrWhiteSpace($case.required_response)) {
        $errors.Add("Boundary case $($case.id) is incomplete.")
    }
}
foreach ($owner in $requiredBoundaryOwners) {
    if ($owner -notin @($boundaryCases.expected_owner)) {
        $errors.Add("Missing boundary owner coverage: $owner")
    }
}
if ('no-dangerous-operational-detail' -notin @($boundaryCases.id)) {
    $errors.Add('A no-dangerous-operational-detail boundary case is required.')
}

if (@($tests.invariants).Count -lt 10) {
    $errors.Add('At least ten governance and safety invariants are required.')
}

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology-ethics validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-ethics validation' -ForegroundColor Green
Write-Host "Static contract cases: $($positiveCases.Count)"
Write-Host "Boundary cases: $($boundaryCases.Count)"
Write-Host "Modes covered: $($allowedModes.Count)"
Write-Host "Branches covered: $($allowedBranches.Count)"
Write-Host "Parallel-review cases: $multiBranchCount"
Write-Host "Governance invariants: $(@($tests.invariants).Count)"
Write-Host 'Note: static validation does not execute case prompts or prove model behavior.'
