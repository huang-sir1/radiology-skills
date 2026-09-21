[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$skillRoot = Split-Path -Parent $PSScriptRoot
$testsPath = Join-Path $skillRoot 'tests/routing-cases.json'
$tests = Get-Content -LiteralPath $testsPath -Raw | ConvertFrom-Json
$errors = [System.Collections.Generic.List[string]]::new()

foreach ($relativePath in @($tests.required_files)) {
    $target = Join-Path $skillRoot $relativePath
    if (-not (Test-Path -LiteralPath $target -PathType Leaf)) {
        $errors.Add("Missing required file: $relativePath")
    }
}

$runtimeFiles = @(
    'SKILL.md',
    'agents/openai.yaml',
    'references/meta-analysis-inference.md',
    'references/experimental-inference-and-power.md',
    'references/sample-size.md',
    'references/analysis-hierarchy-and-missingness.md',
    'references/incremental-value.md',
    'references/quantitative-imaging-measurement-science.md',
    'references/causal-and-clinical-impact-inference.md',
    'references/longitudinal-and-multistate-imaging.md',
    'templates/meta-analysis-statistical-brief.md',
    'templates/experimental-inference-power-brief.md'
)
$runtimeText = ($runtimeFiles | ForEach-Object {
    Get-Content -LiteralPath (Join-Path $skillRoot $_) -Raw
}) -join "`n"

$requiredPhrases = @(
    'name: radiology-stats',
    'single-study-inference',
    'meta-analysis-inference',
    'experimental-inference-power',
    'quantitative-measurement',
    'causal-clinical-impact',
    'longitudinal-multistate',
    'plan',
    'audit',
    'compute',
    'interpret',
    'mentor',
    'writing-handoff',
    'executable statistical brief',
    'BIOSTATISTICIAN_REQUIRED',
    'AUTHOR_INPUT_NEEDED',
    'random-effects',
    'dependent effects',
    'bivariate',
    'HSROC',
    'prevalence',
    'incidence',
    'person-time',
    'HR, OR, RR',
    'ICC',
    'kappa',
    'agreement',
    'prediction performance',
    'calibration',
    'heterogeneity',
    'publication bias',
    'continuous',
    'binary',
    'count',
    'donor',
    'litter',
    'cage',
    'cluster',
    'repeated measures',
    'mixed',
    'attrition',
    'effect worth detecting',
    'no universal'
)
foreach ($phrase in $requiredPhrases) {
    if ($runtimeText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing required statistical contract phrase: $phrase")
    }
}

$positive = @($tests.positive_cases)
$boundary = @($tests.boundary_cases)
$allIds = @($positive.id + $boundary.id)
if (($allIds | Sort-Object -Unique).Count -ne $allIds.Count) {
    $errors.Add('Routing case IDs must be unique.')
}

$allowedModes = @('plan', 'audit', 'compute', 'interpret', 'mentor', 'writing-handoff')
$allowedRoutes = @(
    'single-study-inference', 'meta-analysis-inference', 'experimental-inference-power',
    'quantitative-measurement', 'causal-clinical-impact', 'longitudinal-multistate'
)
foreach ($case in $positive) {
    if ($case.mode -notin $allowedModes) {
        $errors.Add("Invalid mode in $($case.id): $($case.mode)")
    }
    if ($case.route -notin $allowedRoutes) {
        $errors.Add("Invalid route in $($case.id): $($case.route)")
    }
    if ([string]::IsNullOrWhiteSpace($case.prompt) -or @($case.required_checks).Count -lt 4) {
        $errors.Add("Case $($case.id) needs a prompt and at least four checks.")
    }
}
foreach ($mode in $allowedModes) {
    if ($mode -notin @($positive.mode)) {
        $errors.Add("Missing positive mode coverage: $mode")
    }
}
foreach ($route in $allowedRoutes) {
    if ($route -notin @($positive.route)) {
        $errors.Add("Missing positive route coverage: $route")
    }
}

$requiredBoundaryOwners = @(
    'radiology-systematic-review',
    'radiology-experiment-design',
    'radiology-method-evaluation',
    'radiology-figure',
    'radiology-reporting',
    'radiology-writing'
)
foreach ($owner in $requiredBoundaryOwners) {
    if ($owner -notin @($boundary.expected_owner)) {
        $errors.Add("Missing boundary owner coverage: $owner")
    }
}

if (@($tests.invariants).Count -lt 19) {
    $errors.Add('At least nineteen scientific invariants are required.')
}

$forbiddenThresholdPatterns = @(
    '\bEPV\s*(?:>=|>|≥|≤|<)\s*\d+',
    '\b(?:events?|subjects?|patients?|donors?|animals?|litters?|cages?|clusters?|readers?|replicates?)\s*(?:>=|>|≥|≤|<)\s*\d+',
    '\bat\s+least\s+\d+\s+(?:events?|subjects?|patients?|donors?|animals?|litters?|cages?|clusters?|readers?|replicates?)\b'
)
$thresholdAuditText = (Get-ChildItem -LiteralPath $skillRoot -Recurse -File | Where-Object {
    $_.Extension -in @('.md', '.yaml', '.yml')
} | ForEach-Object {
    Get-Content -LiteralPath $_.FullName -Raw
}) -join "`n"
foreach ($pattern in $forbiddenThresholdPatterns) {
    if ([regex]::IsMatch($thresholdAuditText, $pattern, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)) {
        $errors.Add("Forbidden universal sample-size threshold pattern found: $pattern")
    }
}

if ($errors.Count -gt 0) {
    Write-Host "FAIL: radiology-stats validation ($($errors.Count) issue(s))" -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-stats validation' -ForegroundColor Green
Write-Host "Static contract cases: $($positive.Count)"
Write-Host "Boundary cases: $($boundary.Count)"
Write-Host "Modes covered: $($allowedModes.Count)"
Write-Host "Routes covered: $($allowedRoutes.Count)"
Write-Host "Scientific invariants: $(@($tests.invariants).Count)"
Write-Host 'Universal sample-size threshold guard: PASS'
Write-Host 'Note: static validation does not execute case prompts or prove model behavior.'
