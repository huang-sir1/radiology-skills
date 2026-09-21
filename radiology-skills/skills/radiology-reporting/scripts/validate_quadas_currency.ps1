[CmdletBinding()]
param(
    [string]$SuiteRoot
)

$ErrorActionPreference = 'Stop'
$reportingRoot = Split-Path -Parent $PSScriptRoot
if ([string]::IsNullOrWhiteSpace($SuiteRoot)) {
    $SuiteRoot = (Resolve-Path -LiteralPath (Join-Path $reportingRoot '..\..')).Path
} else {
    $SuiteRoot = (Resolve-Path -LiteralPath $SuiteRoot).Path
}

$errors = [System.Collections.Generic.List[string]]::new()
$paths = [ordered]@{
    skill = Join-Path $reportingRoot 'SKILL.md'
    versions = Join-Path $reportingRoot 'references/guideline-versions.md'
    router = Join-Path $reportingRoot 'references/guideline-router.md'
    dta = Join-Path $reportingRoot 'references/stard-prisma-quadas.md'
    reportingReadme = Join-Path $reportingRoot 'README.md'
    citationScope = Join-Path $SuiteRoot 'skills/radiology-citation/references/radiology-journal-scope.md'
    designBlueprint = Join-Path $SuiteRoot 'skills/radiology-design/references/study-blueprints.md'
}

$text = @{}
foreach ($entry in $paths.GetEnumerator()) {
    if (-not (Test-Path -LiteralPath $entry.Value -PathType Leaf)) {
        $errors.Add("Missing QUADAS contract file: $($entry.Value)")
        continue
    }
    $text[$entry.Key] = Get-Content -LiteralPath $entry.Value -Raw
}

$required = [ordered]@{
    versions = @(
        '**QUADAS-3** | **1.2 (2026)**',
        '10.7326/ANNALS-25-02104',
        '10.7326/ANNALS-25-04943',
        'https://www.bristol.ac.uk/population-health-sciences/projects/quadas/',
        'https://www.bristol.ac.uk/population-health-sciences/projects/quadas/quadas-3/',
        'https://www.bristol.ac.uk/population-health-sciences/projects/quadas/quadas-3/resources/',
        'https://www.bristol.ac.uk/population-health-sciences/projects/quadas/quadas-c/',
        '**QUADAS-C**',
        '10.7326/M21-2234',
        '**QUADAS-2 (legacy)**'
    )
    dta = @(
        'QUADAS-3 v1.2',
        'selected accuracy-estimate level',
        'state the systematic-review synthesis question',
        'define the ideal test accuracy trial',
        'identify the accuracy estimates to assess',
        'Participants',
        'Index Test',
        'Target Condition',
        'Analysis',
        'QUADAS-C cannot be used alone',
        'does not assess indirect comparisons',
        'does not assess applicability'
    )
    router = @(
        'PRISMA-DTA + QUADAS-3 v1.2 per selected accuracy estimate',
        'QUADAS-C alongside QUADAS-3',
        'does not assess indirect between-study comparisons'
    )
    skill = @(
        'QUADAS-3 v1.2',
        'QUADAS-C alongside QUADAS-3',
        'per selected accuracy estimate'
    )
    reportingReadme = @('QUADAS-3 v1.2 / QUADAS-C')
    citationScope = @('QUADAS-3', 'QUADAS-C')
    designBlueprint = @('QUADAS-3 v1.2', 'QUADAS-C alongside QUADAS-3')
}

foreach ($entry in $required.GetEnumerator()) {
    if (-not $text.ContainsKey($entry.Key)) { continue }
    foreach ($phrase in $entry.Value) {
        if ($text[$entry.Key].IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
            $errors.Add("$($entry.Key) missing current QUADAS contract phrase: $phrase")
        }
    }
}

$surfaceFiles = @(
    $rootReadme = Join-Path $SuiteRoot 'README.md'
    if (Test-Path -LiteralPath $rootReadme -PathType Leaf) { Get-Item -LiteralPath $rootReadme -Force }
    Get-ChildItem -LiteralPath (Join-Path $SuiteRoot 'skills') -Recurse -Force -File -Filter '*.md'
)

$legacyPattern = '(?i)legacy|supersed(?:e|ed|es)|historical|previous|old version|legacy only|旧版|历史|已取代'
$quadas2Hits = 0
foreach ($file in $surfaceFiles) {
    $lineNumber = 0
    foreach ($line in Get-Content -LiteralPath $file.FullName) {
        $lineNumber++
        if ($line -notmatch '(?i)QUADAS[ -]?2') { continue }
        $quadas2Hits++
        if ($line -notmatch $legacyPattern) {
            $relative = [System.IO.Path]::GetRelativePath($SuiteRoot, $file.FullName)
            $errors.Add("Unlabelled QUADAS-2 product text at ${relative}:$lineNumber")
        }
    }
}

$combined = ($text.Values -join "`n")
foreach ($pattern in @(
    '(?i)PRISMA-DTA\s*\+\s*QUADAS[ -]?2',
    '(?i)QUADAS[ -]?2\s*/\s*QUADAS-C',
    '(?i)QUADAS[ -]?2\s+if\s+part\s+of\s+a\s+review',
    '(?i)per-study\s+QUADAS[ -]?2'
)) {
    if ($combined -match $pattern) {
        $errors.Add("Forbidden obsolete primary-route wording matched: $pattern")
    }
}

$rootReadmeText = if (Test-Path -LiteralPath (Join-Path $SuiteRoot 'README.md')) {
    Get-Content -LiteralPath (Join-Path $SuiteRoot 'README.md') -Raw
} else { '' }
if ($rootReadmeText.IndexOf('QUADAS-3', [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
    $errors.Add('Root README does not expose QUADAS-3 as the current product route.')
}

if ($errors.Count -gt 0) {
    Write-Host "FAIL: QUADAS currency contract ($($errors.Count) issue(s))" -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: QUADAS currency contract' -ForegroundColor Green
Write-Host 'Current primary tool: QUADAS-3 v1.2'
Write-Host 'Comparative companion: QUADAS-C alongside QUADAS-3'
Write-Host "Legacy-labelled QUADAS-2 lines: $quadas2Hits"
Write-Host "Release-facing Markdown files scanned: $($surfaceFiles.Count)"
Write-Host 'Note: this validator checks frozen product text and official-source identifiers; live source currency must still be re-verified at use.'
