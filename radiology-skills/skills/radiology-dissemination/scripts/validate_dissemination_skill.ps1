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

$runtimeFiles = Get-ChildItem -LiteralPath $skillRoot -Recurse -File |
    Where-Object { $_.Extension -in @('.md', '.yaml', '.json') -and $_.FullName -notmatch '\\scripts\\' }
$runtimeText = ($runtimeFiles | ForEach-Object { Get-Content -LiteralPath $_.FullName -Raw }) -join [Environment]::NewLine
$skillText = Get-Content -LiteralPath (Join-Path $skillRoot 'SKILL.md') -Raw
$yamlText = Get-Content -LiteralPath (Join-Path $skillRoot 'agents/openai.yaml') -Raw
$sourceText = Get-Content -LiteralPath (Join-Path $skillRoot 'references/source-registry.md') -Raw
$sourceRows = @($sourceText -split "`r?`n" | Where-Object { $_.StartsWith('| [') })
if ($sourceRows.Count -lt 12 -or @($sourceRows | Where-Object { $_ -notmatch '\|\s*20\d{2}-\d{2}-\d{2}\s*\|\s*$' }).Count -gt 0) {
    $errors.Add('Every dissemination source row must carry its own ISO access date; central freshness policy enforces age.')
}
$escapedBacktick = ([string][char]92) + ([string][char]96)
if ($runtimeText.IndexOf($escapedBacktick, [System.StringComparison]::Ordinal) -ge 0) { $errors.Add('Runtime Markdown contains an escaped backtick.') }

foreach ($route in @(
    'references/modes-and-audience-actions.md',
    'references/rights-privacy-accessibility.md',
    'references/source-registry.md',
    'templates/dissemination-brief.md',
    'templates/claim-source-ledger.md'
)) {
    if ($skillText.IndexOf($route, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("SKILL.md does not route to: $route")
    }
}

foreach ($phrase in @(
    'name: radiology-dissemination', '$radiology-dissemination', 'Audience action',
    'claim-source ledger', 'PLAN_ONLY', 'DRAFT_TEXT', 'CREATE_ARTIFACT', 'AUDIT',
    'conference-poster', 'conference-abstract', 'plain-language-summary',
    'patient-public-explanation', 'clinical-evidence-brief', 'policy-brief', 'press-social',
    'LIVE_RULE_UNVERIFIED', 'LIVE_VERIFICATION_REQUIRED', 'STOP_PHI', 'STOP_RIGHTS',
    'STOP_EMBARGO', 'STOP_AUTHORITY', 'PowerPoint crop', 'black box', 'alt text',
    'radiology-paper2ppt', 'radiology-figure', 'radiology-writing', 'not medical advice'
)) {
    if ($runtimeText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing dissemination contract phrase: $phrase")
    }
}

foreach ($url in @(
    'https://www.rsna.org/annual-meeting/abstract-submission',
    'https://www.nih.gov/institutes-nih/nih-office-director/office-communications-public-liaison/clear-communication/plain-language-nih',
    'https://osp.od.nih.gov/policies/return-of-research-results/',
    'https://training.cochrane.org/handbook/current/chapter-iii',
    'https://www.who.int/initiatives/evidence-informed-policy-network/the-evipnet-approach',
    'https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/journals-and-the-media.html',
    'https://www.w3.org/TR/2024/REC-WCAG22-20241212/',
    'https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html',
    'https://www.rsna.org/-/media/Files/RSNA/Practice-Tools/RemovingPHI.pdf'
)) {
    if ($runtimeText.IndexOf($url, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing authoritative source: $url")
    }
}

$descriptionMatch = [regex]::Match($skillText, '(?m)^description:\s*"([^"]+)"')
if (-not $descriptionMatch.Success -or $descriptionMatch.Groups[1].Value.Length -lt 40 -or $descriptionMatch.Groups[1].Value.Length -gt 160) {
    $errors.Add('Frontmatter description must be concise and 40-160 characters.')
}
$shortMatch = [regex]::Match($yamlText, '(?m)^\s*short_description:\s*"([^"]+)"')
if (-not $shortMatch.Success -or $shortMatch.Groups[1].Value.Length -lt 25 -or $shortMatch.Groups[1].Value.Length -gt 64) {
    $errors.Add('short_description must be 25-64 characters.')
}
if ($yamlText.IndexOf('$radiology-dissemination', [System.StringComparison]::Ordinal) -lt 0) {
    $errors.Add('default_prompt must explicitly invoke $radiology-dissemination.')
}

$positiveCases = @($tests.positive_cases)
$boundaryCases = @($tests.boundary_cases)
$allIds = @($positiveCases.id + $boundaryCases.id)
if (($allIds | Sort-Object -Unique).Count -ne $allIds.Count) { $errors.Add('Routing case IDs must be unique.') }
foreach ($case in $positiveCases) {
    if ($case.mode -notin @($tests.required_modes)) { $errors.Add("Invalid mode in $($case.id): $($case.mode)") }
    if ($case.artifact_scope -notin @($tests.required_artifact_scopes)) { $errors.Add("Invalid artifact scope in $($case.id).") }
    if ([string]::IsNullOrWhiteSpace($case.prompt) -or @($case.required_checks).Count -lt 6) {
        $errors.Add("Case $($case.id) needs a prompt and at least six checks.")
    }
}
foreach ($mode in @($tests.required_modes)) {
    if ($mode -notin @($positiveCases.mode)) { $errors.Add("Missing positive mode: $mode") }
}
foreach ($scope in @($tests.required_artifact_scopes)) {
    if ($scope -notin @($positiveCases.artifact_scope)) { $errors.Add("Missing artifact scope: $scope") }
}
foreach ($owner in @('radiology-paper2ppt','radiology-figure','radiology-writing','radiology-table','radiology-systematic-review','NO_SKILL')) {
    if ($owner -notin @($boundaryCases.expected_owner)) { $errors.Add("Missing boundary owner: $owner") }
}
foreach ($case in $boundaryCases) {
    if ($case.expected_owner -like 'radiology-*' -and -not (Test-Path -LiteralPath (Join-Path $skillsRoot "$($case.expected_owner)/SKILL.md") -PathType Leaf)) {
        $errors.Add("Boundary case $($case.id) names unknown owner: $($case.expected_owner)")
    }
}
if (@($tests.invariants).Count -lt 20) { $errors.Add('At least twenty dissemination invariants are required.') }
if ($runtimeText -notmatch '\b20\d{2}-\d{2}-\d{2}\b') { $errors.Add('Source registry accessed date is missing.') }

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology-dissemination validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-dissemination validation' -ForegroundColor Green
Write-Host "Positive cases: $($positiveCases.Count); boundary cases: $($boundaryCases.Count)"
Write-Host "Modes: $(@($tests.required_modes).Count); invariants: $(@($tests.invariants).Count)"
Write-Host 'Note: static validation does not create, submit, publish or inspect a real dissemination artifact.'
