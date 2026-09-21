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
    'name: radiology-research-ops', '$radiology-research-ops', 'RACI', 'critical path',
    'site readiness', 'EVIDENCED_READY', 'AT_RISK', 'BLOCKED', 'FROZEN',
    'risk', 'issue', 'decision', 'change', 'deviation', 'incident',
    'OPS_STOP_AND_ESCALATE', 'recruitment', 'annotation', 'DICOM', 'scanner',
    'freeze', 'pause', 'TERMINATED', 'closeout', 'does not decide the scientific question',
    'post-award-funder-reporting', 'annual/interim/final', 'amendment',
    'POST_AWARD_REPORT_INCOMPLETE', 'POST_AWARD_REPORT_BLOCKED',
    'HUMAN_INSTITUTIONAL_FUNDER_ACTION_REQUIRED', 'original scientific owner'
)) {
    if ($runtimeText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing required operations contract phrase: $phrase")
    }
}

foreach ($route in @(
    'references/operations-control-model.md',
    'references/site-readiness-and-imaging-operations.md',
    'references/risk-change-freeze-and-closeout.md',
    'references/source-registry.md',
    'templates/research-operations-control-book.md',
    'templates/site-readiness-freeze-register.md'
)) {
    if ($skillText.IndexOf($route, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("SKILL.md does not route to: $route")
    }
}

if ($openaiText.IndexOf('$radiology-research-ops', [System.StringComparison]::Ordinal) -lt 0) {
    $errors.Add('agents/openai.yaml default_prompt must mention $radiology-research-ops.')
}
$shortMatch = [regex]::Match($openaiText, '(?m)^\s*short_description:\s*"([^"]+)"')
if (-not $shortMatch.Success -or $shortMatch.Groups[1].Value.Length -lt 25 -or $shortMatch.Groups[1].Value.Length -gt 64) {
    $errors.Add('openai short_description must be 25-64 characters.')
}

$sourceText = Get-Content -LiteralPath (Join-Path $skillRoot 'references/source-registry.md') -Raw
$sourceUrls = @(
    'https://www.fda.gov/regulatory-information/search-fda-guidance-documents/e6r3-good-clinical-practice-gcp',
    'https://www.ema.europa.eu/en/documents/scientific-guideline/ich-e6-r3-guideline-good-clinical-practice-gcp-step-5_en.pdf',
    'https://www.bmj.com/content/389/bmj-2024-081477',
    'https://www.nccih.nih.gov/grants/toolbox',
    'https://www.nidcr.nih.gov/research/conducting-nidcr-clinical-research/nidcr-accrual-retention-monitoring',
    'https://grants.nih.gov/grants/guide/notice-files/not98-084.html',
    'https://www.grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/dms/policy-overview',
    'https://www.nimh.nih.gov/funding/clinical-research/clinical-research-toolbox/nimh-clinical-research-toolbox'
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
foreach ($owner in @('radiology-design', 'radiology-grant', 'radiology-pipeline', 'radiology-translation', 'radiology-ethics', 'radiology-stats', 'NO_SKILL')) {
    if ($owner -notin @($boundaryCases.expected_owner)) { $errors.Add("Missing boundary owner coverage: $owner") }
}
foreach ($escalation in @('authorized-pi-sponsor-and-institution', 'authorized-finance-procurement-and-contracting-owner')) {
    if ($escalation -notin @($boundaryCases.required_escalation)) { $errors.Add("Missing escalation coverage: $escalation") }
}
if (@($tests.invariants).Count -lt 18) { $errors.Add('At least eighteen operations invariants are required.') }

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology-research-ops validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-research-ops validation' -ForegroundColor Green
Write-Host "Static contract cases: $($positiveCases.Count)"
Write-Host "Boundary cases: $($boundaryCases.Count)"
Write-Host "Modes covered: $(@($tests.required_modes).Count)"
Write-Host "Operations invariants: $(@($tests.invariants).Count)"
Write-Host "Authoritative source entries: $($sourceUrls.Count)"
Write-Host 'Note: static validation does not execute prompts, activate sites, authorize spending, or prove operational control.'
