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
    'name: radiology-qualitative-mixed-methods',
    '$radiology-qualitative-mixed-methods',
    'interviews',
    'focus groups',
    'observation',
    'workflow ethnography',
    'think-aloud',
    'purposeful sampling',
    'information power',
    'saturation',
    'reflexivity',
    'reflexive thematic analysis',
    'framework analysis',
    'qualitative content analysis',
    'negative',
    'member checking',
    'audit trail',
    'convergent',
    'explanatory sequential',
    'exploratory sequential',
    'joint display',
    'discordance',
    'FORMATIVE_FEEDBACK_ONLY',
    'SOURCE_EVIDENCE',
    'ANALYTIC_INTERPRETATION',
    'META_INFERENCE',
    'RECOMMENDATION',
    'STOP_ETHICS_OR_PRIVACY',
    'STOP_NO_ANALYSABLE_RECORD',
    'STOP_DESIGN_METHOD_MISMATCH',
    'STOP_UNSUPPORTED_ADEQUACY',
    'STOP_NO_INTEGRATION',
    'radiology-translation',
    'radiology-stats',
    'radiology-ethics',
    'radiology-data'
)
foreach ($phrase in $requiredPhrases) {
    if ($runtimeText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing required contract phrase: $phrase")
    }
}

$requiredRoutes = @(
    'references/methods-and-rigor.md',
    'references/mixed-methods-integration.md',
    'references/source-registry.md',
    'templates/qualitative-mixed-methods-passport.md',
    'templates/joint-display-and-discordance-ledger.md'
)
foreach ($route in $requiredRoutes) {
    if ($skillText.IndexOf($route, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("SKILL.md does not route to: $route")
    }
}

$sourceUrls = @(
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC4097839/',
    'https://obssr.od.nih.gov/sites/g/files/mnhszr296/files/Best_Practices_for_Mixed_Methods_Research.pdf',
    'https://www.equator-network.org/reporting-guidelines/srqr/',
    'https://www.equator-network.org/reporting-guidelines/coreq/',
    'https://www.apa.org/pubs/journals/resources/apa-style-jars',
    'https://doi.org/10.1177/1049732315617444',
    'https://doi.org/10.1186/1471-2288-13-117',
    'https://doi.org/10.1080/14780887.2020.1769238',
    'https://doi.org/10.1177/16094069221104564',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC4639381/'
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
if ($yamlText.IndexOf('$radiology-qualitative-mixed-methods',
        [System.StringComparison]::Ordinal) -lt 0) {
    $errors.Add('default_prompt must explicitly invoke $radiology-qualitative-mixed-methods.')
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
    'radiology-translation',
    'radiology-stats',
    'radiology-ethics',
    'radiology-data',
    'responsible-clinical-team',
    'radiology-polishing',
    'radiology-design'
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
if (@($tests.invariants).Count -lt 20) {
    $errors.Add('At least twenty qualitative/mixed-methods invariants are required.')
}

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology-qualitative-mixed-methods validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-qualitative-mixed-methods validation' -ForegroundColor Green
Write-Host "Static contract cases: $($positiveCases.Count)"
Write-Host "Boundary cases: $($boundaryCases.Count)"
Write-Host "Modes covered: $(@($tests.required_modes).Count)"
Write-Host "Scientific invariants: $(@($tests.invariants).Count)"
Write-Host "Authoritative source entries: $($sourceUrls.Count)"
Write-Host 'Note: static validation does not execute fieldwork, analyse participant data, or certify qualitative rigor.'
