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
    'name: radiology-consensus-guideline', '$radiology-consensus-guideline',
    'clinical-practice-guideline', 'appropriateness-criteria', 'practice-parameter',
    'technical-standard', 'expert-consensus-statement', 'patient/public', 'COI',
    'EVIDENCE_READY', 'EVIDENCE_STALE', 'GRADE', 'EtD', 'Delphi', 'RAND/UCLA',
    'nominal group', 'consensus percentage', 'STABLE_DISAGREEMENT',
    'GUIDANCE_STOP_AND_REFRAME', 'systematic review', 'retirement',
    'underlying systematic review', 'cannot adopt, endorse'
)) {
    if ($runtimeText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing required consensus/guideline phrase: $phrase")
    }
}

foreach ($route in @(
    'references/evidence-to-recommendation.md',
    'references/formal-consensus-methods.md',
    'references/radiology-guidance-lifecycle.md',
    'references/source-registry.md',
    'templates/consensus-guideline-protocol.md',
    'templates/recommendation-etd-ledger.md'
)) {
    if ($skillText.IndexOf($route, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("SKILL.md does not route to: $route")
    }
}

if ($openaiText.IndexOf('$radiology-consensus-guideline', [System.StringComparison]::Ordinal) -lt 0) {
    $errors.Add('agents/openai.yaml default_prompt must mention $radiology-consensus-guideline.')
}
$shortMatch = [regex]::Match($openaiText, '(?m)^\s*short_description:\s*"([^"]+)"')
if (-not $shortMatch.Success -or $shortMatch.Groups[1].Value.Length -lt 25 -or $shortMatch.Groups[1].Value.Length -gt 64) {
    $errors.Add('openai short_description must be 25-64 characters.')
}

$sourceText = Get-Content -LiteralPath (Join-Path $skillRoot 'references/source-registry.md') -Raw
$sourceUrls = @(
    'https://www.who.int/publications/i/item/9789241548960',
    'https://www.bmj.com/content/353/bmj.i2089',
    'https://www.nice.org.uk/process/pmg20',
    'https://www.rand.org/pubs/monograph_reports/MR1269.html',
    'https://doi.org/10.1177/0269216317690685',
    'https://doi.org/10.1371/journal.pmed.1004326',
    'https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Practice-Parameters-and-Technical-Standards',
    'https://cs.acr.org/-/media/ACR/Files/Appropriateness-Criteria/Rating-Round-Information.pdf'
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
foreach ($owner in @('radiology-systematic-review', 'radiology-clinical-domain', 'radiology-stats', 'radiology-reporting', 'radiology-health-economics', 'NO_SKILL')) {
    if ($owner -notin @($boundaryCases.expected_owner)) { $errors.Add("Missing boundary owner coverage: $owner") }
}
foreach ($escalation in @('authorized-society-guideline-governance', 'responsible-clinical-team')) {
    if ($escalation -notin @($boundaryCases.required_escalation)) { $errors.Add("Missing escalation coverage: $escalation") }
}
if (@($tests.invariants).Count -lt 18) { $errors.Add('At least eighteen consensus/guideline invariants are required.') }

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology-consensus-guideline validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-consensus-guideline validation' -ForegroundColor Green
Write-Host "Static contract cases: $($positiveCases.Count)"
Write-Host "Boundary cases: $($boundaryCases.Count)"
Write-Host "Modes covered: $(@($tests.required_modes).Count)"
Write-Host "Consensus/guideline invariants: $(@($tests.invariants).Count)"
Write-Host "Authoritative source entries: $($sourceUrls.Count)"
Write-Host 'Note: static validation does not execute prompts, confer endorsement, or prove consensus/guideline behavior.'
