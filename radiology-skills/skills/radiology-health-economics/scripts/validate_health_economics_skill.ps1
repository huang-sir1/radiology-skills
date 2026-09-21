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
    Get-ChildItem -LiteralPath $skillRoot -Recurse -File |
        Where-Object {
            $_.Extension -in @('.md', '.yaml') -and
            $_.FullName -notmatch '\\scripts\\|\\tests\\'
        }
)
$runtimeText = ($runtimeFiles | ForEach-Object {
    Get-Content -LiteralPath $_.FullName -Raw
}) -join [Environment]::NewLine
$skillText = Get-Content -LiteralPath (Join-Path $skillRoot 'SKILL.md') -Raw
$yamlText = Get-Content -LiteralPath (Join-Path $skillRoot 'agents/openai.yaml') -Raw
$sourceText = Get-Content -LiteralPath (Join-Path $skillRoot 'references/source-registry.md') -Raw
$escapedBacktick = ([string][char]92) + ([string][char]96)
if ($runtimeText.IndexOf($escapedBacktick, [System.StringComparison]::Ordinal) -ge 0) {
    $errors.Add('Runtime Markdown contains an escaped backtick; use real inline-code delimiters.')
}

$requiredPhrases = @(
    'name: radiology-health-economics',
    '$radiology-health-economics',
    'perspective',
    'comparator',
    'time horizon',
    'cost-effectiveness analysis',
    'cost-utility analysis',
    'cost-consequence',
    'QALY',
    'ICER',
    'budget impact analysis',
    'decision tree',
    'state-transition',
    'Markov',
    'probabilistic sensitivity analysis',
    'PSA',
    'scenario',
    'value of information',
    'EVPI',
    'EVPPI',
    'EVSI',
    'HTA',
    'CHEERS 2022',
    'CHEERS-AI',
    'grant budget',
    'decision-curve net benefit',
    'OBSERVED_INPUT',
    'EXTERNAL_SOURCE',
    'ASSUMPTION',
    'MODEL_DERIVATION',
    'INFERENCE',
    'DECISION_RECOMMENDATION',
    'STOP_REFERENCE_CASE_UNRESOLVED',
    'STOP_DECISION_PROBLEM_INCOMPLETE',
    'STOP_INPUT_PROVENANCE',
    'STOP_INTERMEDIATE_OUTCOME_BRIDGE',
    'STOP_INVALID_INCREMENTAL_ANALYSIS',
    'STOP_AUTHORIZATION_REQUEST',
    'radiology-grant',
    'radiology-method-evaluation',
    'radiology-clinical-domain',
    'radiology-qualitative-mixed-methods'
)
foreach ($phrase in $requiredPhrases) {
    if ($runtimeText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing required contract phrase: $phrase")
    }
}

$requiredRoutes = @(
    'references/evaluation-design-and-imaging-pathway.md',
    'references/modeling-uncertainty-and-hta.md',
    'references/source-registry.md',
    'templates/health-economic-evaluation-passport.md',
    'templates/model-and-uncertainty-register.md'
)
foreach ($route in $requiredRoutes) {
    if ($skillText.IndexOf($route, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("SKILL.md does not route to: $route")
    }
}

$sourceUrls = @(
    'https://www.ispor.org/heor-resources/good-practices/cheers',
    'https://doi.org/10.1016/j.jval.2024.05.006',
    'https://www.nice.org.uk/process/pmg36/chapter/economic-evaluation-2/',
    'https://www.nice.org.uk/process/pmg48/chapter/introduction',
    'https://www.who.int/publications/i/item/9789240110878',
    'https://www.ispor.org/docs/default-source/resources/outcomes-research-guidelines-index/conceptualizing_a_model-2.pdf',
    'https://www.ispor.org/docs/default-source/resources/outcomes-research-guidelines-index/state-transition_modeling-3.pdf',
    'https://doi.org/10.1016/j.jval.2013.08.2291',
    'https://www.ispor.org/publications/journals/value-in-health/abstract/Volume-23--Issue-2/Value-of-Information-Analysis-for-Research-Decisions-An-Introduction-Report-1-of-the-ISPOR-Value-of-Information-Analysis-Emerging-Good-Practices-Task-Force',
    'https://pubmed.ncbi.nlm.nih.gov/17099194/'
)
foreach ($url in $sourceUrls) {
    if ($sourceText.IndexOf($url, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing authoritative source entry: $url")
    }
}
foreach ($field in @('Claim-use', 'Version / status on access', 'Accessed')) {
    if ($sourceText.IndexOf($field, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Source registry lacks field/date: $field")
    }
}
if ($sourceText -notmatch '\b20\d{2}-\d{2}-\d{2}\b') { $errors.Add('Source registry lacks an ISO access date.') }

$descriptionMatch = [regex]::Match(
    $skillText,
    '(?m)^description:\s*"(?<value>[^"]+)"\s*$'
)
if (-not $descriptionMatch.Success) {
    $errors.Add('Quoted frontmatter description is required.')
} elseif ($descriptionMatch.Groups['value'].Value.Length -lt 40 -or
          $descriptionMatch.Groups['value'].Value.Length -gt 160) {
    $errors.Add('Frontmatter description must be concise and 40-160 characters.')
}
$shortMatch = [regex]::Match(
    $yamlText,
    '(?m)^\s*short_description:\s*"(?<value>[^"]+)"\s*$'
)
if (-not $shortMatch.Success -or
    $shortMatch.Groups['value'].Value.Length -lt 25 -or
    $shortMatch.Groups['value'].Value.Length -gt 64) {
    $errors.Add('short_description must be quoted and 25-64 characters.')
}
if ($yamlText.IndexOf('$radiology-health-economics',
        [System.StringComparison]::Ordinal) -lt 0) {
    $errors.Add('default_prompt must explicitly invoke $radiology-health-economics.')
}

$positiveCases = @($tests.positive_cases)
$boundaryCases = @($tests.boundary_cases)
$allIds = @($positiveCases.id + $boundaryCases.id)
if (($allIds | Sort-Object -Unique).Count -ne $allIds.Count) {
    $errors.Add('Routing case IDs must be unique.')
}
foreach ($case in $positiveCases) {
    if ($case.mode -notin @($tests.required_modes)) {
        $errors.Add("Case $($case.id) has invalid mode: $($case.mode)")
    }
    if ([string]::IsNullOrWhiteSpace($case.prompt) -or
        @($case.required_checks).Count -lt 6) {
        $errors.Add("Case $($case.id) needs a prompt and at least six required checks.")
    }
}
foreach ($mode in @($tests.required_modes)) {
    if ($mode -notin @($positiveCases.mode)) {
        $errors.Add("Missing positive mode coverage: $mode")
    }
}
$requiredBoundaryOwners = @(
    'radiology-grant',
    'radiology-method-evaluation',
    'radiology-stats',
    'radiology-clinical-domain',
    'local-hta-payer-authority',
    'responsible-clinical-team',
    'radiology-polishing'
)
foreach ($owner in $requiredBoundaryOwners) {
    if ($owner -notin @($boundaryCases.expected_owner)) {
        $errors.Add("Missing boundary owner coverage: $owner")
    }
}
foreach ($case in $boundaryCases) {
    if ([string]::IsNullOrWhiteSpace($case.required_boundary)) {
        $errors.Add("Boundary case $($case.id) lacks a required boundary.")
    }
}
if (@($tests.invariants).Count -lt 24) {
    $errors.Add('At least twenty-four health-economic invariants are required.')
}

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology-health-economics validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-health-economics validation' -ForegroundColor Green
Write-Host "Static contract cases: $($positiveCases.Count)"
Write-Host "Boundary cases: $($boundaryCases.Count)"
Write-Host "Modes covered: $(@($tests.required_modes).Count)"
Write-Host "Scientific invariants: $(@($tests.invariants).Count)"
Write-Host "Authoritative source entries: $($sourceUrls.Count)"
Write-Host 'Note: static validation does not run an economic model, verify local reimbursement rules, or authorize adoption.'
