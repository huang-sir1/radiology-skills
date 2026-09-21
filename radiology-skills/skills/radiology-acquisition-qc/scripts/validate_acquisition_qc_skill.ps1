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

$expectedReferences = @(
    'ct-acquisition-reconstruction.md',
    'mr-acquisition-reconstruction.md',
    'pet-spect-acquisition-quantification.md',
    'ultrasound-ceus-elastography.md',
    'projection-radiography-mammo-dbt.md',
    'phantom-test-retest-protocol-shift.md',
    'mr-spectroscopy.md',
    'functional-mri.md',
    'diffusion-tensor-tractography.md'
)
$actualReferences = @(
    Get-ChildItem -LiteralPath (Join-Path $skillRoot 'references') -File -Filter '*.md' |
        Select-Object -ExpandProperty Name |
        Sort-Object
)
if (Compare-Object ($expectedReferences | Sort-Object) $actualReferences) {
    $errors.Add('The references directory must contain exactly the nine registered playbooks.')
}

$runtimeFiles = @(
    Join-Path $skillRoot 'SKILL.md'
    Join-Path $skillRoot 'agents/openai.yaml'
    Join-Path $skillRoot 'templates/imaging-measurement-passport.md'
) + ($expectedReferences | ForEach-Object { Join-Path $skillRoot "references/$_" })

$existingRuntimeFiles = @($runtimeFiles | Where-Object { Test-Path -LiteralPath $_ -PathType Leaf })
$runtimeText = ($existingRuntimeFiles | ForEach-Object { Get-Content -LiteralPath $_ -Raw }) -join [Environment]::NewLine

$requiredPhrases = @(
    'name: radiology-acquisition-qc',
    '$radiology-acquisition-qc',
    'CT',
    'MRI',
    'PET',
    'SPECT',
    'ultrasound',
    'CEUS',
    'elastography',
    'projection radiography',
    'mammography',
    'DBT',
    'phantom',
    'test-retest',
    'protocol shift',
    'MRS',
    'MRSI',
    'fMRI',
    'BOLD',
    'DTI',
    'tractography',
    'LOCAL_EXTENSION_REQUIRED',
    'series selection',
    'reconstruction',
    'quantitative',
    'represented',
    'wholly unseen',
    'adaptation',
    'PASS',
    'CONDITIONAL',
    'STOP',
    'AUTHOR_INPUT_NEEDED',
    'eligible',
    'acquired',
    'exported',
    'accepted',
    'nondiagnostic',
    'excluded',
    'claim ceiling',
    'radiology-clinical-domain',
    'radiology-data',
    'radiology-annotation',
    'radiology-radiomics',
    'radiology-deep-learning',
    'radiology-method-evaluation',
    'radiology-stats',
    'radiology-translation',
    'radiology-radiogenomics'
)
foreach ($phrase in $requiredPhrases) {
    if ($runtimeText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing required contract phrase: $phrase")
    }
}

foreach ($reference in $expectedReferences) {
    $link = "references/$reference"
    $skillText = Get-Content -LiteralPath (Join-Path $skillRoot 'SKILL.md') -Raw
    if ($skillText.IndexOf($link, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("SKILL.md does not route to: $link")
    }
}

$sourceUrls = @(
    'https://www.dicomstandard.org/current/',
    'https://qibawiki.rsna.org/index.php/Profiles',
    'https://doi.org/10.1148/QIBA/20231219',
    'https://doi.org/10.1148/QIBA/20221215',
    'https://doi.org/10.1148/QIBA/20230615',
    'https://doi.org/10.1148/QIBA/20240115',
    'https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Practice-Parameters-and-Technical-Standards',
    'https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1394_web.pdf'
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
    if ($case.modality -notin @($tests.required_modalities)) {
        $errors.Add("Case $($case.id) has invalid modality: $($case.modality)")
    }
    if ([string]::IsNullOrWhiteSpace($case.prompt) -or @($case.required_checks).Count -lt 5) {
        $errors.Add("Case $($case.id) needs a prompt and at least five required checks.")
    }
}
foreach ($mode in @($tests.required_modes)) {
    if ($mode -notin @($positiveCases.mode)) {
        $errors.Add("Missing positive mode coverage: $mode")
    }
}
foreach ($modality in @($tests.required_modalities)) {
    if ($modality -notin @($positiveCases.modality)) {
        $errors.Add("Missing positive modality coverage: $modality")
    }
}

$requiredBoundaryOwners = @(
    'radiology-data',
    'radiology-clinical-domain',
    'radiology-annotation',
    'radiology-radiomics',
    'radiology-deep-learning',
    'radiology-method-evaluation',
    'radiology-translation',
    'radiology-radiogenomics',
    'responsible-clinical-team',
    'LOCAL_EXTENSION_REQUIRED'
)
foreach ($owner in $requiredBoundaryOwners) {
    if ($owner -notin @($boundaryCases.expected_owner)) {
        $errors.Add("Missing boundary owner coverage: $owner")
    }
}
if (@($tests.invariants).Count -lt 14) {
    $errors.Add('At least fourteen scientific invariants are required.')
}

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology-acquisition-qc validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology-acquisition-qc validation' -ForegroundColor Green
Write-Host "Static contract cases: $($positiveCases.Count)"
Write-Host "Boundary cases: $($boundaryCases.Count)"
Write-Host "Modes covered: $(@($tests.required_modes).Count)"
Write-Host "Modalities covered: $(@($tests.required_modalities).Count)"
Write-Host "Scientific invariants: $(@($tests.invariants).Count)"
Write-Host "Authoritative source entries: $($sourceUrls.Count)"
Write-Host 'Note: static validation does not execute case prompts or prove model behavior.'
