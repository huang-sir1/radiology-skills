[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$skillRoot = Split-Path -Parent $PSScriptRoot
$skillsRoot = Split-Path -Parent $skillRoot
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
        Where-Object { $_.Extension -in @('.md', '.yaml', '.json') -and $_.FullName -notmatch '\\scripts\\' }
)
$runtimeText = ($runtimeFiles | ForEach-Object { Get-Content -LiteralPath $_.FullName -Raw }) -join [Environment]::NewLine
$skillText = Get-Content -LiteralPath (Join-Path $skillRoot 'SKILL.md') -Raw

$requiredPhrases = @(
    'name: radiology-grant',
    '$radiology-grant',
    'grant call passport',
    'CALL_VERSION_UNRESOLVED',
    'ADMIN_PASS',
    'ADMIN_CONDITIONAL',
    'ADMIN_FAIL',
    'ADMIN_NOT_ASSESSABLE',
    'administrative',
    'scientific merit',
    'criterion finding',
    'triage/targeted',
    'full audit',
    'mock panel',
    'revision/resubmission',
    'funder-package-finalization',
    'FUNDER_PACKAGE_INCOMPLETE',
    'FUNDER_PACKAGE_BLOCKED',
    'HUMAN_INSTITUTIONAL_SUBMISSION_REQUIRED',
    'NOT_CALIBRATED',
    'radiology gate',
    'acquisition/reconstruction',
    'reference standard',
    'leakage',
    'claim ceiling',
    'milestone',
    'fallback',
    'budget',
    'VERIFIED_CURRENT',
    'USER_ATTESTED',
    'HYPOTHESIS',
    'PLANNED',
    'STOP_AND_REFRAME',
    'AI_ASSISTED_ADVISORY',
    'CONFLICTING',
    'NOT_ESTABLISHED',
    'DRAFT_NONCONTROLLING',
    'H27',
    'H28',
    'H29',
    'multimodal intersection',
    'model-lineage',
    'aim-level sample-size',
    'external-independence',
    'mechanism evidence ladder',
    'TRIPOD+AI',
    'PROBAST+AI',
    'METRICS',
    'IBSI',
    'Factor 1',
    'Factor 2',
    'Factor 3',
    'scientific value',
    'innovation',
    'social impact',
    'feasibility',
    'radiology-paper2ppt'
)
foreach ($phrase in $requiredPhrases) {
    if ($runtimeText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing required contract phrase: $phrase")
    }
}

$requiredRoutes = @(
    'references/call-and-compliance-gate.md',
    'references/nsfc-2024-2026-change-map.md',
    'references/nsfc-application-content-playbook.md',
    'references/nsfc-radiology-code-and-call-router.md',
    'references/imaging-methodology-router.md',
    'references/source-registry.md',
    'references/review-modes-and-criteria.md',
    'references/grant-architecture.md',
    'references/radiology-feasibility-audit.md',
    'references/evidence-contract-and-stopping-rules.md',
    'templates/grant-call-passport.md',
    'templates/grant-review-report.md',
    'templates/aim-milestone-risk-register.md'
)
foreach ($route in $requiredRoutes) {
    if ($skillText.IndexOf($route, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("SKILL.md does not route to: $route")
    }
}

$sourceUrls = @(
    'https://www.nsfc.gov.cn/p1/2931/3971/3972/qy2026.html',
    'https://www.nsfc.gov.cn/p1/2931/3971/3974/sqgd2.html',
    'https://www.nsfc.gov.cn/u/cms/www/202601/161125020ts3.pdf',
    'https://www.nsfc.gov.cn/p1/2931/3971/3973/2026ndgjzrkxjjggjc.html',
    'https://www.nsfc.gov.cn/p1/3381/2824/99667.html',
    'https://www.nsfc.gov.cn/p1/3381/2821/99242.html',
    'https://www.nsfc.gov.cn/p1/2961/2962/3643/tj.html',
    'https://www.nsfc.gov.cn/p1/2931/3971/4002/99886.html',
    'https://www.nsfc.gov.cn/p1/2858/3220/3250/75693.html',
    'https://www.nsfc.gov.cn/p1/2858/3220/3250/96593.html',
    'https://www.nsfc.gov.cn/p1/2871/2873/69510.html',
    'https://grants.nih.gov/grants/guide/notice-files/NOT-OD-24-010.html',
    'https://grants.nih.gov/grants/how-to-apply-application-guide/format-and-write/write-your-application.htm',
    'https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-155.html',
    'https://grants.nih.gov/grants/guide/pa-files/PA-25-301.html',
    'https://grants.nih.gov/new-to-nih/information-for/foreign-grants',
    'https://grants.nih.gov/policy-and-compliance/policy-topics/clinical-trials/definition',
    'https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-067.html',
    'https://grants.nih.gov/funding/activity-codes/PF5',
    'https://erc.europa.eu/apply-grant/synergy-grant',
    'https://erc.europa.eu/news-events/news/changes-2026-and-2027-work-programmes',
    'https://wellcome.org/research-funding/guidance/prepare-to-apply/eligibility-information-grant-applicants',
    'https://doi.org/10.1148/ryai.240300',
    'https://doi.org/10.1038/s41591-025-03953-8',
    'https://doi.org/10.1136/bmj-2023-078378',
    'https://doi.org/10.1136/bmj-2024-082505',
    'https://doi.org/10.1136/bmj-2024-081554',
    'https://doi.org/10.1038/s41591-024-03470-0',
    'https://pubmed.ncbi.nlm.nih.gov/38228979/',
    'https://doi.org/10.1148/radiol.231319',
    'https://doi.org/10.1038/s41571-025-01067-1',
    'https://doi.org/10.1038/s41591-022-01772-9',
    'https://doi.org/10.1148/radiol.2015142202',
    'https://www.dicomstandard.org/current/',
    'https://qibawiki.rsna.org/index.php/Profiles'
)
foreach ($url in $sourceUrls) {
    if ($runtimeText.IndexOf($url, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing authoritative source entry: $url")
    }
}

if ($runtimeText.IndexOf('三 main body blocks', [System.StringComparison]::OrdinalIgnoreCase) -ge 0) {
    $errors.Add('Mixed-language placeholder detected in the NSFC architecture snapshot.')
}
$architectureText = Get-Content -LiteralPath (Join-Path $skillRoot 'references/grant-architecture.md') -Raw
foreach ($boundary in @('OFFICIAL_CYCLE_SNAPSHOT', 'verify', 'live electronic form', 'legacy heading')) {
    if ($architectureText.IndexOf($boundary, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("NSFC cycle snapshot lacks boundary phrase: $boundary")
    }
}

$changeMapText = Get-Content -LiteralPath (Join-Path $skillRoot 'references/nsfc-2024-2026-change-map.md') -Raw
foreach ($boundary in @(
    'application year',
    'science division/office',
    'special call/clinical track',
    'one month after project-plan approval',
    'in-service postgraduate eligibility',
    'Do not rewrite this as',
    'general 2027 annual guide'
)) {
    if ($changeMapText.IndexOf($boundary, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("NSFC three-year map lacks boundary phrase: $boundary")
    }
}

$internationalText = Get-Content -LiteralPath (Join-Path $skillRoot 'references/international-grants.md') -Raw
foreach ($boundary in @(
    '**PA-25-301** is **Clinical Trial Not Allowed**',
    '**PA-26-002** is **Clinical Trial Optional**',
    'study eligibility',
    '`NOT_ALLOWED`',
    '`REQUIRED`',
    '`OPTIONAL`',
    '25 May 2026',
    'Earlier due dates and existing award terms'
)) {
    if ($internationalText.IndexOf($boundary, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("International grant reference lacks trial-scope boundary: $boundary")
    }
}
$passportText = Get-Content -LiteralPath (Join-Path $skillRoot 'templates/grant-call-passport.md') -Raw
foreach ($boundary in @(
    'Study/aim-level clinical-trial classification',
    'NOT_ALLOWED / REQUIRED / OPTIONAL / UNRESOLVED',
    'Foreign-organization eligibility is not study eligibility',
    'Unknown classification cannot become `ADMIN_PASS`'
)) {
    if ($passportText.IndexOf($boundary, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Grant call passport lacks trial-scope field/boundary: $boundary")
    }
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
    if ([string]::IsNullOrWhiteSpace($case.prompt) -or @($case.required_checks).Count -lt 6) {
        $errors.Add("Case $($case.id) needs a prompt and at least six required checks.")
    }
}
foreach ($case in $boundaryCases) {
    if ($case.expected_owner -like 'radiology-*') {
        $ownerSkill = Join-Path $skillsRoot "$($case.expected_owner)/SKILL.md"
        if (-not (Test-Path -LiteralPath $ownerSkill -PathType Leaf)) {
            $errors.Add("Boundary case $($case.id) names an unknown skill owner: $($case.expected_owner)")
        }
    }
}
foreach ($mode in @($tests.required_modes)) {
    if ($mode -notin @($positiveCases.mode)) {
        $errors.Add("Missing positive mode coverage: $mode")
    }
}

$requiredBoundaryOwners = @(
    'radiology-prereview',
    'radiology-paper2ppt',
    'radiology-frontier',
    'radiology-design',
    'radiology-research-ops',
    'NO_SKILL'
)
foreach ($owner in $requiredBoundaryOwners) {
    if ($owner -notin @($boundaryCases.expected_owner)) {
        $errors.Add("Missing boundary owner coverage: $owner")
    }
}
$requiredEscalations = @(
    'institutional-research-office-and-funder',
    'responsible-clinical-team'
)
foreach ($escalation in $requiredEscalations) {
    if ($escalation -notin @($boundaryCases.required_escalation)) {
        $errors.Add("Missing external escalation coverage: $escalation")
    }
}
if (@($tests.invariants).Count -lt 18) {
    $errors.Add('At least eighteen grant-review invariants are required.')
}

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology-grant validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-grant validation' -ForegroundColor Green
Write-Host "Static contract cases: $($positiveCases.Count)"
Write-Host "Boundary cases: $($boundaryCases.Count)"
Write-Host "Modes covered: $(@($tests.required_modes).Count)"
Write-Host "Grant-review invariants: $(@($tests.invariants).Count)"
Write-Host "Authoritative source entries: $($sourceUrls.Count)"
Write-Host 'Note: static validation does not execute prompts, calibrate panel scores, or prove grant-review behavior.'
