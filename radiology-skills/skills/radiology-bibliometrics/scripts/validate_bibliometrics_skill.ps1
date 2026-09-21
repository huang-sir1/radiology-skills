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
if ($sourceRows.Count -lt 12 -or @($sourceRows | Where-Object { $_ -notmatch '\|\s*20\d{2}-\d{2}-\d{2}\s*\|\s*$' }).Count -gt 0) {
    $errors.Add('Every bibliometrics source row must carry its own ISO access date; central freshness policy enforces age.')
}
$escapedBacktick = ([string][char]92) + ([string][char]96)
if ($runtimeText.IndexOf($escapedBacktick, [System.StringComparison]::Ordinal) -ge 0) { $errors.Add('Runtime Markdown contains an escaped backtick.') }

foreach ($route in @('references/analysis-contract-and-methods.md','references/responsible-interpretation.md','references/source-registry.md','templates/corpus-passport.md','templates/bibliometric-analysis-and-claim-ledger.md')) {
    if ($skillText.IndexOf($route,[System.StringComparison]::OrdinalIgnoreCase) -lt 0) { $errors.Add("SKILL.md does not route to: $route") }
}
foreach ($phrase in @(
    'name: radiology-bibliometrics','$radiology-bibliometrics','corpus passport','database/index','exact query','retrieval date',
    'DOI','work-family','ORCID','ROR','full counting','fractional counting','field/classification','citation window',
    'threshold','normalization','clustering algorithm','resolution','seed','community stability','altmetrics','not merit',
    'STOP_CORPUS','STOP_IDENTITY','STOP_METRIC','STOP_NETWORK','STOP_INTERPRETATION','claim-source ledger',
    'Corpus passport ID','SHA-256 digest','Exact source locator','Scientific owner','Receiving owner','Next gate',
    'radiology-search','radiology-frontier','radiology-systematic-review','quality','clinical benefit','innovation'
)) {
    if ($runtimeText.IndexOf($phrase,[System.StringComparison]::OrdinalIgnoreCase) -lt 0) { $errors.Add("Missing bibliometrics contract phrase: $phrase") }
}
foreach ($url in @(
    'https://support.crossref.org/hc/en-us/articles/214320426-REST-API',
    'https://www.crossref.org/documentation/retrieve-metadata/',
    'https://help.openalex.org/',
    'https://info.orcid.org/documentation/collecting-and-sharing-orcid-ids/',
    'https://ror.readme.io/docs/ror-data-structure',
    'https://traditional.leidenranking.com/information/indicators',
    'https://doi.org/10.1038/520429a',
    'https://sfdora.org/dora_indicators_guidance/',
    'https://www.vosviewer.com/documentation/Manual_VOSviewer_1.6.20.pdf',
    'https://icite.od.nih.gov/'
)) {
    if ($runtimeText.IndexOf($url,[System.StringComparison]::OrdinalIgnoreCase) -lt 0) { $errors.Add("Missing authoritative source: $url") }
}

$descriptionMatch = [regex]::Match($skillText,'(?m)^description:\s*"([^"]+)"')
if (-not $descriptionMatch.Success -or $descriptionMatch.Groups[1].Value.Length -lt 40 -or $descriptionMatch.Groups[1].Value.Length -gt 160) { $errors.Add('Frontmatter description must be concise and 40-160 characters.') }
$shortMatch = [regex]::Match($yamlText,'(?m)^\s*short_description:\s*"([^"]+)"')
if (-not $shortMatch.Success -or $shortMatch.Groups[1].Value.Length -lt 25 -or $shortMatch.Groups[1].Value.Length -gt 64) { $errors.Add('short_description must be 25-64 characters.') }
if ($yamlText.IndexOf('$radiology-bibliometrics',[System.StringComparison]::Ordinal) -lt 0) { $errors.Add('default_prompt must explicitly invoke $radiology-bibliometrics.') }

$positiveCases = @($tests.positive_cases)
$boundaryCases = @($tests.boundary_cases)
$allIds = @($positiveCases.id + $boundaryCases.id)
if (($allIds | Sort-Object -Unique).Count -ne $allIds.Count) { $errors.Add('Routing case IDs must be unique.') }
foreach ($case in $positiveCases) {
    if ($case.mode -notin @($tests.required_modes)) { $errors.Add("Invalid mode in $($case.id): $($case.mode)") }
    if ([string]::IsNullOrWhiteSpace($case.prompt) -or @($case.required_checks).Count -lt 6) { $errors.Add("Case $($case.id) needs a prompt and at least six checks.") }
}
foreach ($mode in @($tests.required_modes)) { if ($mode -notin @($positiveCases.mode)) { $errors.Add("Missing positive mode: $mode") } }
foreach ($owner in @('radiology-search','radiology-frontier','radiology-systematic-review','radiology-citation','radiology-figure','NO_SKILL')) {
    if ($owner -notin @($boundaryCases.expected_owner)) { $errors.Add("Missing boundary owner: $owner") }
}
foreach ($case in $boundaryCases) {
    if ($case.expected_owner -like 'radiology-*' -and -not (Test-Path -LiteralPath (Join-Path $skillsRoot "$($case.expected_owner)/SKILL.md") -PathType Leaf)) { $errors.Add("Boundary case $($case.id) names unknown owner: $($case.expected_owner)") }
}
if (@($tests.invariants).Count -lt 20) { $errors.Add('At least twenty bibliometrics invariants are required.') }
if ($runtimeText -notmatch '\b20\d{2}-\d{2}-\d{2}\b' -or $runtimeText.IndexOf('LIVE_VERIFICATION_REQUIRED',[System.StringComparison]::Ordinal) -lt 0) { $errors.Add('Source registry access date or live-verification state is missing.') }

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology-bibliometrics validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}
Write-Host 'PASS: radiology-bibliometrics validation' -ForegroundColor Green
Write-Host "Positive cases: $($positiveCases.Count); boundary cases: $($boundaryCases.Count)"
Write-Host "Modes: $(@($tests.required_modes).Count); invariants: $(@($tests.invariants).Count)"
Write-Host 'Note: static validation does not retrieve a corpus, compute metrics or verify behavioral routing.'
