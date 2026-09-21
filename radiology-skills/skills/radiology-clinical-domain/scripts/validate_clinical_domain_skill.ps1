[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$skillRoot = Split-Path -Parent $PSScriptRoot
$testsPath = Join-Path $skillRoot 'tests/routing-cases.json'
$tests = Get-Content -LiteralPath $testsPath -Raw | ConvertFrom-Json
$errors = [System.Collections.Generic.List[string]]::new()

foreach ($relativePath in $tests.required_files) {
    $target = Join-Path $skillRoot $relativePath
    if (-not (Test-Path -LiteralPath $target -PathType Leaf)) {
        $errors.Add("Missing required file: $relativePath")
    }
}

$runtimeFiles = @(
    Join-Path $skillRoot 'SKILL.md'
    Join-Path $skillRoot 'agents/openai.yaml'
    Join-Path $skillRoot 'references/clinical-domain-routing.md'
    Join-Path $skillRoot 'references/domain-playbooks.md'
    Join-Path $skillRoot 'references/acute-emergency-imaging-research.md'
    Join-Path $skillRoot 'references/musculoskeletal-imaging-research.md'
    Join-Path $skillRoot 'references/pediatric-imaging-research.md'
    Join-Path $skillRoot 'references/nuclear-medicine-theranostics-research.md'
    Join-Path $skillRoot 'templates/local-clinical-expert-profile.md'
    Join-Path $skillRoot 'templates/live-standard-receipt.md'
)
$runtimeText = ($runtimeFiles | ForEach-Object { Get-Content -LiteralPath $_ -Raw }) -join "`n"

$requiredPhrases = @(
    'name: radiology-clinical-domain',
    'plan',
    'audit',
    'mentor',
    'interpret',
    'writing-handoff',
    'PICO/estimand',
    'reference standard',
    'treatment and time-line',
    'mechanism',
    'validation ladder',
    'claim ceiling',
    'review red flags',
    'Learner prompts',
    'LIVE_VERIFICATION_REQUIRED',
    'AUTHOR_INPUT_NEEDED',
    'local clinical expert',
    'representativeness',
    'equity',
    'harm',
    'stakeholder',
    'radiology-translation',
    'subtype gate',
    'acute-emergency',
    'musculoskeletal',
    'pediatric',
    'nuclear-medicine-theranostics',
    'radiology-ethics: human-subjects',
    'consent/waiver',
    'privacy'
    'normative identifier'
    'retrieved artifact SHA-256'
    'section and page'
    'superseded relation'
)
foreach ($phrase in $requiredPhrases) {
    if ($runtimeText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing required contract phrase: $phrase")
    }
}

$sourceUrls = @(
    'https://www.acr.org/clinical-resources/clinical-tools-and-reference/reporting-and-data-systems/lung-rads',
    'https://www.iaslc.org/science-research/scientific-projects/iaslc-staging-project-lung-cancer-thymic-tumors-and',
    'https://ascopubs.org/doi/10.1200/JCO.23.01059',
    'https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Reporting-and-Data-Systems/LI-RADS',
    'https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Reporting-and-Data-Systems/BI-RADS',
    'https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Reporting-and-Data-Systems/PI-RADS',
    'https://www.jacc.org/doi/10.1016/j.jcmg.2022.07.002',
    'https://www.acr.org/clinical-resources/clinical-tools-and-reference/appropriateness-criteria',
    'https://skeletalrad.org/ssr-consensus-papers/',
    'https://www.fda.gov/radiation-emitting-products/medical-imaging/pediatric-x-ray-imaging',
    'https://eanm.org/publications/guidelines/overview/'
)
foreach ($url in $sourceUrls) {
    if ($runtimeText.IndexOf($url, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing authoritative source entry: $url")
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
    if ($case.domain -notin @($tests.required_domains)) {
        $errors.Add("Case $($case.id) has invalid domain: $($case.domain)")
    }
    if ([string]::IsNullOrWhiteSpace($case.prompt) -or @($case.required_checks).Count -lt 4) {
        $errors.Add("Case $($case.id) needs a prompt and at least four required checks.")
    }
}
foreach ($mode in @($tests.required_modes)) {
    if ($mode -notin @($positiveCases.mode)) {
        $errors.Add("Missing positive mode coverage: $mode")
    }
}
foreach ($domain in @($tests.required_domains)) {
    if ($domain -notin @($positiveCases.domain)) {
        $errors.Add("Missing positive domain coverage: $domain")
    }
}
if ($boundaryCases.Count -lt 4) {
    $errors.Add('At least four boundary cases are required.')
}
if (@($tests.invariants).Count -lt 12) {
    $errors.Add('At least twelve scientific invariants are required.')
}

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology-clinical-domain validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-clinical-domain validation' -ForegroundColor Green
Write-Host "Static contract cases: $($positiveCases.Count)"
Write-Host "Boundary cases: $($boundaryCases.Count)"
Write-Host "Modes covered: $(@($tests.required_modes).Count)"
Write-Host "Domains covered: $(@($tests.required_domains).Count)"
Write-Host "Scientific invariants: $(@($tests.invariants).Count)"
Write-Host "Authoritative source entries: $($sourceUrls.Count)"
Write-Host 'Note: static validation does not execute case prompts or prove model behavior.'
