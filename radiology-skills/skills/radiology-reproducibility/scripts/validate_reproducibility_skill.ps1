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
    'name: radiology-reproducibility',
    '$radiology-reproducibility',
    'TRACEABLE',
    'RERUNNABLE',
    'REPLAYED',
    'INDEPENDENTLY_REPRODUCED',
    'EXTERNALLY_REPLICATED_OR_TRANSPORTED',
    'separate scientific-validation axis',
    'code commit',
    'dirty state',
    'configuration',
    'environment',
    'container',
    'digest',
    'input manifest',
    'output manifest',
    'run ID',
    'seed',
    'weights',
    'data version',
    'independent',
    'tolerance',
    'restricted data',
    'licence',
    'archive',
    'minimum replay package',
    'ASSERTED',
    'PRESENT_UNVERIFIED',
    'IDENTITY_VERIFIED',
    'EXECUTED',
    'TOLERANCE_PASSED',
    'INDEPENDENTLY_VERIFIED',
    'EXTERNAL_DATA_VERIFIED',
    'STOP_INPUT_IDENTITY',
    'STOP_CODE_CONFIG_IDENTITY',
    'STOP_ENVIRONMENT_UNRESOLVED',
    'STOP_TOLERANCE_NOT_FROZEN',
    'STOP_DATA_AUTHORIZATION',
    'STOP_LICENSE_OR_ARCHIVE',
    'STOP_REPLAY_NOT_AUTHORIZED',
    'radiology-data',
    'radiology-ethics',
    'radiology-acquisition-qc',
    'radiology-stats',
    'radiology-pipeline'
)
foreach ($phrase in $requiredPhrases) {
    if ($runtimeText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing required contract phrase: $phrase")
    }
}

$requiredRoutes = @(
    'references/replay-contract-and-levels.md',
    'references/restricted-data-archiving-and-software.md',
    'references/source-registry.md',
    'templates/reproducibility-passport.md',
    'templates/minimum-replay-package-manifest.md'
)
foreach ($route in $requiredRoutes) {
    if ($skillText.IndexOf($route, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("SKILL.md does not route to: $route")
    }
}

$sourceUrls = @(
    'https://nap.nationalacademies.org/catalog/25303/reproducibility-and-replicability-in-science',
    'https://www.grants.nih.gov/policy-and-compliance/policy-topics/reproducibility',
    'https://datascience.nih.gov/tools-and-analytics/best-practices-for-sharing-research-software-faq',
    'https://www.rd-alliance.org/groups/fair-research-software-fair4rs-wg/outputs/?output=94498',
    'https://www.w3.org/TR/prov-o/',
    'https://specs.opencontainers.org/image-spec/',
    'https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content',
    'https://grants.nih.gov/grants/guide/notice-files/not-od-21-013.html',
    'https://www.go-fair.org/resources/faq/what-fair-is-not/',
    'https://doi.org/10.1148/ryai.240300',
    'https://doi.org/10.1148/radiol.2020191145',
    'https://www.dicomstandard.org/current/'
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
if ($yamlText.IndexOf('$radiology-reproducibility',
        [System.StringComparison]::Ordinal) -lt 0) {
    $errors.Add('default_prompt must explicitly invoke $radiology-reproducibility.')
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
    if ($case.expected_level -notin @($tests.required_computational_levels)) {
        $errors.Add("Case $($case.id) has invalid evidence level: $($case.expected_level)")
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
foreach ($level in @($tests.required_computational_levels)) {
    if ($level -notin @($positiveCases.expected_level)) {
        $errors.Add("Missing positive evidence-level coverage: $level")
    }
}
$requiredBoundaryOwners = @(
    'radiology-acquisition-qc',
    'radiology-stats',
    'radiology-data',
    'radiology-ethics',
    'radiology-deep-learning',
    'radiology-translation',
    'responsible-software-security-team',
    'radiology-pipeline'
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
if (@($tests.invariants).Count -lt 28) {
    $errors.Add('At least twenty-eight reproducibility invariants are required.')
}

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology-reproducibility validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-reproducibility validation' -ForegroundColor Green
Write-Host "Static contract cases: $($positiveCases.Count)"
Write-Host "Boundary cases: $($boundaryCases.Count)"
Write-Host "Modes covered: $(@($tests.required_modes).Count)"
Write-Host "Computational levels covered: $(@($tests.required_computational_levels).Count); external validation remains a separate axis"
Write-Host "Scientific invariants: $(@($tests.invariants).Count)"
Write-Host "Authoritative source entries: $($sourceUrls.Count)"
Write-Host 'Note: static validation does not execute code, grant data access, or prove external clinical validity.'
