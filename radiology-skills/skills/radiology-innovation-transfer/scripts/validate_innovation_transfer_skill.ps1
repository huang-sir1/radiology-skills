[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$skillRoot = Split-Path -Parent $PSScriptRoot
$skillsRoot = Split-Path -Parent $skillRoot
$tests = Get-Content -LiteralPath (Join-Path $skillRoot 'tests/routing-cases.json') -Raw | ConvertFrom-Json
$errors = [System.Collections.Generic.List[string]]::new()

foreach ($relativePath in @($tests.required_files)) {
    if (-not (Test-Path -LiteralPath (Join-Path $skillRoot $relativePath) -PathType Leaf)) { $errors.Add("Missing required file: $relativePath") }
}
$runtimeFiles = Get-ChildItem -LiteralPath $skillRoot -Recurse -File |
    Where-Object { $_.Extension -in @('.md','.yaml','.json') -and $_.FullName -notmatch '\\scripts\\' }
$runtimeText = ($runtimeFiles | ForEach-Object { Get-Content -LiteralPath $_.FullName -Raw }) -join [Environment]::NewLine
$skillText = Get-Content -LiteralPath (Join-Path $skillRoot 'SKILL.md') -Raw
$yamlText = Get-Content -LiteralPath (Join-Path $skillRoot 'agents/openai.yaml') -Raw
$sourceText = Get-Content -LiteralPath (Join-Path $skillRoot 'references/source-registry.md') -Raw
$sourceRows = @($sourceText -split "`r?`n" | Where-Object { $_.StartsWith('| [') })
if ($sourceRows.Count -lt 14 -or @($sourceRows | Where-Object { $_ -notmatch '\|\s*20\d{2}-\d{2}-\d{2}\s*\|\s*$' }).Count -gt 0) {
    $errors.Add('Every innovation-transfer source row must carry its own ISO access date; central freshness policy enforces age.')
}
$escapedBacktick = ([string][char]92) + ([string][char]96)
if ($runtimeText.IndexOf($escapedBacktick, [System.StringComparison]::Ordinal) -ge 0) { $errors.Add('Runtime Markdown contains an escaped backtick.') }

foreach ($route in @('references/transfer-modes-and-evidence-gates.md','references/patent-readiness-and-diligence.md','references/source-registry.md','templates/innovation-disclosure-passport.md','templates/diligence-evidence-map.md','templates/nonconfidential-summary.md')) {
    if ($skillText.IndexOf($route,[System.StringComparison]::OrdinalIgnoreCase) -lt 0) { $errors.Add("SKILL.md does not route to: $route") }
}
foreach ($phrase in @(
    'name: radiology-innovation-transfer','$radiology-innovation-transfer','disclosure-triage','patent-landscape',
    'readiness-assessment','value-proposition','rights-and-partnership','nonconfidential-summary','diligence-handoff',
    'claim-source ledger','STOP_PUBLIC_DISCLOSURE','STOP_CONFIDENTIAL_CHANNEL','STOP_RIGHTS','STOP_LEGAL_OPINION',
    'STOP_REGULATED_CLAIM','LIVE_VERIFICATION_REQUIRED','patentability','freedom-to-operate','FTO','TRL','MRL',
    'clinical validity','clinical utility','market interest','adoption','TTO','regulatory/quality','DICOM','PACS','PHI',
    'radiology-translation','radiology-dissemination','not a patentability'
)) {
    if ($runtimeText.IndexOf($phrase,[System.StringComparison]::OrdinalIgnoreCase) -lt 0) { $errors.Add("Missing innovation-transfer contract phrase: $phrase") }
}
foreach ($url in @(
    'https://www.wipo.int/publications/en/details.jsp?id=3938',
    'https://www.wipo.int/en/web/patent-analytics',
    'https://patentscope.wipo.int/search/en/search.jsf',
    'https://www.uspto.gov/patents/basics/apply',
    'https://ppubs.uspto.gov/pubwebapp/static/pages/landing.html',
    'https://www.wipo.int/en/web/patents/faq_patents',
    'https://www.wipo.int/en/web/trade-secrets/',
    'https://www.nasa.gov/directorates/somd/space-communications-navigation-program/technology-readiness-levels/',
    'https://www.cto.mil/sea/pg/',
    'https://www.dodmantech.mil/JDMTP/Subpanels-Technical-Working-Groups-TWG/Manufacturing-Readiness-Level-Working-Group/',
    'https://autm.net/surveys-and-tools/tech-transfer-practices-manual/volume-3',
    'https://www.fda.gov/medical-devices/regulatory-accelerator/medical-device-software-guidance-navigator',
    'https://www.imdrf.org/documents/software-medical-device-samd-clinical-evaluation'
)) {
    if ($runtimeText.IndexOf($url,[System.StringComparison]::OrdinalIgnoreCase) -lt 0) { $errors.Add("Missing authoritative source: $url") }
}

$descriptionMatch = [regex]::Match($skillText,'(?m)^description:\s*"([^"]+)"')
if (-not $descriptionMatch.Success -or $descriptionMatch.Groups[1].Value.Length -lt 40 -or $descriptionMatch.Groups[1].Value.Length -gt 160) { $errors.Add('Frontmatter description must be concise and 40-160 characters.') }
$shortMatch = [regex]::Match($yamlText,'(?m)^\s*short_description:\s*"([^"]+)"')
if (-not $shortMatch.Success -or $shortMatch.Groups[1].Value.Length -lt 25 -or $shortMatch.Groups[1].Value.Length -gt 64) { $errors.Add('short_description must be 25-64 characters.') }
if ($yamlText.IndexOf('$radiology-innovation-transfer',[System.StringComparison]::Ordinal) -lt 0) { $errors.Add('default_prompt must explicitly invoke $radiology-innovation-transfer.') }

$positiveCases = @($tests.positive_cases)
$boundaryCases = @($tests.boundary_cases)
$allIds = @($positiveCases.id + $boundaryCases.id)
if (($allIds | Sort-Object -Unique).Count -ne $allIds.Count) { $errors.Add('Routing case IDs must be unique.') }
foreach ($case in $positiveCases) {
    if ($case.mode -notin @($tests.required_modes)) { $errors.Add("Invalid mode in $($case.id): $($case.mode)") }
    if ([string]::IsNullOrWhiteSpace($case.prompt) -or @($case.required_checks).Count -lt 6) { $errors.Add("Case $($case.id) needs a prompt and at least six checks.") }
}
foreach ($mode in @($tests.required_modes)) { if ($mode -notin @($positiveCases.mode)) { $errors.Add("Missing positive mode: $mode") } }
foreach ($owner in @('radiology-translation','radiology-acquisition-qc','radiology-data','radiology-ethics','radiology-grant','radiology-writing','radiology-dissemination','NO_SKILL')) {
    if ($owner -notin @($boundaryCases.expected_owner)) { $errors.Add("Missing boundary owner: $owner") }
}
foreach ($case in $boundaryCases) {
    if ($case.expected_owner -like 'radiology-*' -and -not (Test-Path -LiteralPath (Join-Path $skillsRoot "$($case.expected_owner)/SKILL.md") -PathType Leaf)) { $errors.Add("Boundary case $($case.id) names unknown owner: $($case.expected_owner)") }
}
foreach ($escalation in @('institutional-TTO-and-qualified-patent-counsel','qualified-jurisdictional-IP-counsel')) {
    if ($escalation -notin @($boundaryCases.required_escalation)) { $errors.Add("Missing required escalation: $escalation") }
}
if (@($tests.invariants).Count -lt 20) { $errors.Add('At least twenty innovation-transfer invariants are required.') }
if ($runtimeText -notmatch '\b20\d{2}-\d{2}-\d{2}\b') { $errors.Add('Source registry accessed date is missing.') }
if ($sourceText.IndexOf('Current deskbook artifact/version is unresolved',[System.StringComparison]::OrdinalIgnoreCase) -lt 0) { $errors.Add('MRL source registry must preserve unresolved current-deskbook status.') }

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology-innovation-transfer validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}
Write-Host 'PASS: radiology-innovation-transfer validation' -ForegroundColor Green
Write-Host "Positive cases: $($positiveCases.Count); boundary cases: $($boundaryCases.Count)"
Write-Host "Modes: $(@($tests.required_modes).Count); invariants: $(@($tests.invariants).Count)"
Write-Host 'Note: static validation does not search patents, determine legal status, disclose material or perform qualified diligence.'
