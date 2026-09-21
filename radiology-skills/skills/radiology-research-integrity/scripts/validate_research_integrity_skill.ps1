[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$skillRoot = Split-Path -Parent $PSScriptRoot
$skillsRoot = Split-Path -Parent $skillRoot
$tests = Get-Content -LiteralPath (Join-Path $skillRoot 'tests/routing-cases.json') -Raw | ConvertFrom-Json
$errors = [System.Collections.Generic.List[string]]::new()

foreach ($relativePath in @($tests.required_files)) {
    if (-not (Test-Path -LiteralPath (Join-Path $skillRoot $relativePath) -PathType Leaf)) {
        $errors.Add("Missing required file: $relativePath")
    }
}

$runtimeFiles = @(Get-ChildItem -LiteralPath $skillRoot -Recurse -File | Where-Object {
    $_.Extension -in @('.md', '.yaml') -and $_.FullName -notmatch '\\scripts\\'
})
$runtimeText = ($runtimeFiles | ForEach-Object { Get-Content -LiteralPath $_.FullName -Raw }) -join "`n"
$skillText = Get-Content -LiteralPath (Join-Path $skillRoot 'SKILL.md') -Raw
$openaiText = Get-Content -LiteralPath (Join-Path $skillRoot 'agents/openai.yaml') -Raw
$descriptionMatch = [regex]::Match($skillText, '(?m)^description:\s*"([^"]+)"')
if (-not $descriptionMatch.Success -or $descriptionMatch.Groups[1].Value.Length -lt 40 -or $descriptionMatch.Groups[1].Value.Length -gt 160) {
    $errors.Add('Frontmatter description must be concise and 40-160 characters.')
}
$escapedBacktick = ([string][char]92) + ([string][char]96)
if ($runtimeText.IndexOf($escapedBacktick, [System.StringComparison]::Ordinal) -ge 0) { $errors.Add('Runtime Markdown contains an escaped backtick.') }

foreach ($phrase in @(
    'name: radiology-research-integrity', '$radiology-research-integrity',
    'OBSERVATION', 'INTEGRITY_SIGNAL', 'ALLEGATION', 'INSTITUTIONAL_FINDING',
    'STOP_AND_ESCALATE', 'authorship', 'CRediT', 'COI', 'sponsor', 'AI',
    'selective-reporting', 'DICOM', 'window/level', 'laterality', 'publication-state map',
    'does not decide whether misconduct occurred', 'institution', 'publisher'
)) {
    if ($runtimeText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing required integrity contract phrase: $phrase")
    }
}

foreach ($route in @(
    'references/evidence-states-and-escalation.md',
    'references/authorship-disclosure-and-selective-reporting.md',
    'references/provenance-and-publication-record.md',
    'references/source-registry.md',
    'templates/integrity-audit-report.md',
    'templates/authorship-coi-ai-ledger.md'
)) {
    if ($skillText.IndexOf($route, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("SKILL.md does not route to: $route")
    }
}

if ($openaiText.IndexOf('$radiology-research-integrity', [System.StringComparison]::Ordinal) -lt 0) {
    $errors.Add('agents/openai.yaml default_prompt must mention $radiology-research-integrity.')
}
$shortMatch = [regex]::Match($openaiText, '(?m)^\s*short_description:\s*"([^"]+)"')
if (-not $shortMatch.Success -or $shortMatch.Groups[1].Value.Length -lt 25 -or $shortMatch.Groups[1].Value.Length -gt 64) {
    $errors.Add('openai short_description must be 25-64 characters.')
}

$sourceText = Get-Content -LiteralPath (Join-Path $skillRoot 'references/source-registry.md') -Raw
$sourceUrls = @(
    'https://ori.hhs.gov/definition-research-misconduct',
    'https://ori.hhs.gov/federal-research-misconduct-policy',
    'https://www.icmje.org/recommendations/',
    'https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html',
    'https://www.icmje.org/recommendations/browse/roles-and-responsibilities/author-responsibilities--conflicts-of-interest.html',
    'https://www.niso.org/publications/z39104-2022-credit',
    'https://doi.org/10.24318/cope.2019.1.4',
    'https://doi.org/10.24318/cope.2019.3.3',
    'https://www.crossref.org/documentation/crossmark/'
)
foreach ($url in $sourceUrls) {
    if ($sourceText.IndexOf($url, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing authoritative source entry: $url")
    }
}
if ([regex]::Matches($sourceText, '\|\s*20\d{2}-\d{2}-\d{2}\s*\|').Count -lt $sourceUrls.Count) {
    $errors.Add('Every authoritative source entry must record an ISO access date; central freshness policy enforces age.')
}

$positiveCases = @($tests.positive_cases)
$boundaryCases = @($tests.boundary_cases)
$allIds = @($positiveCases.id + $boundaryCases.id)
if (($allIds | Sort-Object -Unique).Count -ne $allIds.Count) { $errors.Add('Routing case IDs must be unique.') }
foreach ($case in $positiveCases) {
    if ($case.mode -notin @($tests.required_modes)) { $errors.Add("Case $($case.id) has invalid mode: $($case.mode)") }
    if ([string]::IsNullOrWhiteSpace($case.prompt) -or @($case.required_checks).Count -lt 6) {
        $errors.Add("Case $($case.id) needs a prompt and at least six required checks.")
    }
}
foreach ($mode in @($tests.required_modes)) {
    if ($mode -notin @($positiveCases.mode)) { $errors.Add("Missing positive mode coverage: $mode") }
}
foreach ($case in $boundaryCases) {
    if ($case.expected_owner -like 'radiology-*') {
        if (-not (Test-Path -LiteralPath (Join-Path $skillsRoot "$($case.expected_owner)/SKILL.md") -PathType Leaf)) {
            $errors.Add("Boundary case $($case.id) names unknown skill: $($case.expected_owner)")
        }
    }
}
foreach ($owner in @('radiology-ethics', 'radiology-prereview', 'radiology-data', 'radiology-submission', 'radiology-reproducibility', 'NO_SKILL')) {
    if ($owner -notin @($boundaryCases.expected_owner)) { $errors.Add("Missing boundary owner coverage: $owner") }
}
foreach ($escalation in @('authorized-institutional-research-integrity-process', 'authorized-records-and-research-integrity-owner')) {
    if ($escalation -notin @($boundaryCases.required_escalation)) { $errors.Add("Missing escalation coverage: $escalation") }
}
if (@($tests.invariants).Count -lt 18) { $errors.Add('At least eighteen integrity invariants are required.') }

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology-research-integrity validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-research-integrity validation' -ForegroundColor Green
Write-Host "Static contract cases: $($positiveCases.Count)"
Write-Host "Boundary cases: $($boundaryCases.Count)"
Write-Host "Modes covered: $(@($tests.required_modes).Count)"
Write-Host "Integrity invariants: $(@($tests.invariants).Count)"
Write-Host "Authoritative source entries: $($sourceUrls.Count)"
Write-Host 'Note: static validation does not execute prompts, investigate people, or prove integrity-review behavior.'
