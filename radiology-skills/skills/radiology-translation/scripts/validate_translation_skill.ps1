[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$skillRoot = Split-Path -Parent $PSScriptRoot
$testsPath = Join-Path $skillRoot 'tests/routing-cases.json'
$errors = [System.Collections.Generic.List[string]]::new()

try {
    $tests = Get-Content -LiteralPath $testsPath -Raw | ConvertFrom-Json
} catch {
    Write-Error "Cannot parse routing cases: $($_.Exception.Message)"
    exit 1
}

foreach ($relativePath in @($tests.required_files)) {
    if (-not (Test-Path -LiteralPath (Join-Path $skillRoot $relativePath) -PathType Leaf)) {
        $errors.Add("Missing required file: $relativePath")
    }
}

$runtimeFiles = @(Get-ChildItem -LiteralPath $skillRoot -Recurse -File | Where-Object {
    $_.Extension -in @('.md', '.yaml') -and $_.FullName -notmatch '\\scripts\\|\\tests\\'
})
$runtimeText = ($runtimeFiles | ForEach-Object { Get-Content -LiteralPath $_.FullName -Raw }) -join "`n"
$skillText = Get-Content -LiteralPath (Join-Path $skillRoot 'SKILL.md') -Raw
$yamlText = Get-Content -LiteralPath (Join-Path $skillRoot 'agents/openai.yaml') -Raw
$sourceText = Get-Content -LiteralPath (Join-Path $skillRoot 'references/source-registry.md') -Raw

$descriptionMatch = [regex]::Match($skillText, '(?m)^description:\s*"(?<value>[^"]+)"\s*$')
if (-not $descriptionMatch.Success -or $descriptionMatch.Groups['value'].Value.Length -lt 40 -or
    $descriptionMatch.Groups['value'].Value.Length -gt 160) {
    $errors.Add('Frontmatter description must be quoted, concise and 40-160 characters.')
}
$shortMatch = [regex]::Match($yamlText, '(?m)^\s*short_description:\s*"(?<value>[^"]+)"\s*$')
if (-not $shortMatch.Success -or $shortMatch.Groups['value'].Value.Length -lt 25 -or
    $shortMatch.Groups['value'].Value.Length -gt 64) {
    $errors.Add('short_description must be quoted and 25-64 characters.')
}
if ($skillText.IndexOf('name: radiology-translation', [System.StringComparison]::Ordinal) -lt 0 -or
    $yamlText.IndexOf('$radiology-translation', [System.StringComparison]::Ordinal) -lt 0) {
    $errors.Add('Skill name/default prompt contract is missing.')
}
$escapedBacktick = ([string][char]92) + ([string][char]96)
if ($runtimeText.IndexOf($escapedBacktick, [System.StringComparison]::Ordinal) -ge 0) {
    $errors.Add('Runtime Markdown contains an escaped backtick.')
}

foreach ($forbidden in @(
    'top journals reward and reviewers demand',
    'Prospective beats retrospective',
    'The strongest evidence short of a trial',
    'Retrospective internal — weakest',
    'Prospective randomised (trial) — highest'
)) {
    if ($runtimeText.IndexOf($forbidden, [System.StringComparison]::OrdinalIgnoreCase) -ge 0) {
        $errors.Add("Over-absolute translation hierarchy remains: $forbidden")
    }
}

foreach ($phrase in @(
    'seven-axis', 'silent deployment', 'reader study', 'decision-curve', 'human factors',
    'implementation science', 'DICOM', 'IHE', 'site acceptance', 'PERFORMANCE_BLIND_INTERVAL',
    'change control', 'rollback', 'retirement', 'LIVE_VERIFICATION_REQUIRED',
    'conformance does not guarantee interoperability'
)) {
    if ($runtimeText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing translation contract phrase: $phrase")
    }
}

$positive = @($tests.positive_cases)
$boundary = @($tests.boundary_cases)
foreach ($mode in @($tests.required_modes)) {
    if ($mode -notin @($positive.mode)) { $errors.Add("Missing positive mode coverage: $mode") }
}
foreach ($owner in @(
    'radiology-writing', 'radiology-qualitative-mixed-methods', 'radiology-research-ops',
    'radiology-health-economics', 'radiology-reproducibility', 'radiology-data',
    'responsible-clinical-team', 'qualified-regulatory-and-institutional-authority',
    'radiology-innovation-transfer'
)) {
    if ($owner -notin @($boundary.expected_owner)) { $errors.Add("Missing boundary owner: $owner") }
}
foreach ($case in $positive) {
    if (@($case.required_checks).Count -lt 5) { $errors.Add("Positive case $($case.id) needs at least five checks.") }
}
foreach ($case in $boundary) {
    if ([string]::IsNullOrWhiteSpace($case.required_boundary)) { $errors.Add("Boundary case $($case.id) lacks a boundary.") }
}
if (@($tests.invariants).Count -lt 20) { $errors.Add('At least 20 scientific invariants are required.') }

$sourceRows = @($sourceText -split "`r?`n" | Where-Object { $_ -match '^\| .+ \| https://.+ \| .+ \| 20\d{2}-\d{2}-\d{2} \| .+ \|$' })
if ($sourceRows.Count -lt 15) { $errors.Add("Source registry needs at least 15 complete rows; found $($sourceRows.Count).") }

foreach ($file in $runtimeFiles | Where-Object { $_.Extension -eq '.md' }) {
    $text = Get-Content -LiteralPath $file.FullName -Raw
    foreach ($match in [regex]::Matches($text, '\[[^\]]+\]\((?<target>[^)]+)\)')) {
        $target = $match.Groups['target'].Value.Split('#')[0]
        if ($target -and $target -notmatch '^(https?://|mailto:)' -and
            -not (Test-Path -LiteralPath (Join-Path $file.DirectoryName $target))) {
            $errors.Add("Broken local Markdown link in $($file.Name): $target")
        }
    }
}

if ($errors.Count -gt 0) {
    Write-Host "FAIL: radiology-translation validation ($($errors.Count) issue(s))" -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-translation validation' -ForegroundColor Green
Write-Host "Positive cases: $($positive.Count); boundary cases: $($boundary.Count)"
Write-Host "Modes: $(@($tests.required_modes).Count); invariants: $(@($tests.invariants).Count); sources: $($sourceRows.Count)"
Write-Host 'Note: static validation does not run clinical studies, verify a live jurisdiction, integrate a site or authorize care.'
