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
    'claim-evidence-and-narrative.md',
    'deck-quality-qa.md',
    'scientific-deck-routing.md',
    'visual-evidence-and-radiology-images.md'
)
$actualReferences = @(
    Get-ChildItem -LiteralPath (Join-Path $skillRoot 'references') -File -Filter '*.md' |
        Select-Object -ExpandProperty Name |
        Sort-Object
)
if (Compare-Object ($expectedReferences | Sort-Object) $actualReferences) {
    $errors.Add('The references directory must contain exactly the four registered progressive-disclosure references.')
}

$expectedTemplates = @('deck-brief.md', 'slide-map-and-source-ledger.md')
$actualTemplates = @(
    Get-ChildItem -LiteralPath (Join-Path $skillRoot 'templates') -File -Filter '*.md' |
        Select-Object -ExpandProperty Name |
        Sort-Object
)
if (Compare-Object ($expectedTemplates | Sort-Object) $actualTemplates) {
    $errors.Add('The templates directory must contain exactly the deck brief and slide/source ledger templates.')
}

$runtimeFiles = @(
    Join-Path $skillRoot 'SKILL.md'
    Join-Path $skillRoot 'agents/openai.yaml'
) + ($expectedReferences | ForEach-Object { Join-Path $skillRoot "references/$_" }) +
    ($expectedTemplates | ForEach-Object { Join-Path $skillRoot "templates/$_" })

$existingRuntimeFiles = @($runtimeFiles | Where-Object { Test-Path -LiteralPath $_ -PathType Leaf })
$runtimeText = ($existingRuntimeFiles | ForEach-Object { Get-Content -LiteralPath $_ -Raw }) -join [Environment]::NewLine
$skillText = Get-Content -LiteralPath (Join-Path $skillRoot 'SKILL.md') -Raw

foreach ($reference in $expectedReferences) {
    if ($skillText.IndexOf("references/$reference", [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("SKILL.md does not route to reference: $reference")
    }
}
foreach ($template in $expectedTemplates) {
    if ($skillText.IndexOf("templates/$template", [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("SKILL.md does not route to template: $template")
    }
}

$requiredPhrases = @(
    'name: radiology-paper2ppt',
    '$radiology-paper2ppt',
    'radiology-grant',
    'radiology-figure',
    'radiology-table',
    'content-planning',
    'artifact scope',
    'Artifact fidelity class',
    'Evidence fidelity class',
    'NATIVE_EDITABLE',
    'MIXED_EDITABLE_AND_SOURCE_CROPS',
    'RENDERED_REFERENCE_ONLY',
    'EVIDENCE_CRITICAL',
    'EVIDENCE_SUPPORTING',
    'EXPLORATORY_STORYBOARD',
    'Upstream Claim ID',
    'accurate source crop',
    'GENERATED ILLUSTRATION',
    'MISSING',
    'UNVERIFIED',
    'parity/round-trip',
    'EDITABLE_PPTX_PARITY_NOT_RUN',
    'audience outcome',
    'communication job',
    'message title',
    'claim ceiling',
    'SOURCE_OBSERVED',
    'ANALYSIS_DERIVED',
    'INTERPRETATION',
    'RECOMMENDATION',
    'PROPOSED',
    'PowerPoint crop is not permanent removal',
    'black bars are not de-identification',
    'sanitization',
    'diagnostic display',
    'Accessibility Checker',
    'alt text',
    'reading order',
    'unique descriptive titles',
    'render every final slide',
    'full size',
    'overlap',
    'font',
    'speaker notes',
    '[Sources]',
    'timed rehearsal',
    'REHEARSAL_NOT_RUN',
    'PASS',
    'CONDITIONAL',
    'STOP',
    'NOT_RUN'
)
foreach ($phrase in $requiredPhrases) {
    if ($runtimeText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Missing required presentation contract phrase: $phrase")
    }
}

$sourceUrls = @(
    'https://www.ijee.ie/articles/Vol29-6/23_ijee2791ns.pdf',
    'https://doi.org/10.1371/journal.pcbi.1009554',
    'https://doi.org/10.1371/journal.pcbi.0030077',
    'https://ods.od.nih.gov/News/Scientifically_Speaking_How_to_Prepare_an_Effective_Talk.aspx',
    'https://www.grants.nih.gov/policy-and-compliance/policy-topics/peer-review/simplifying-review/framework',
    'https://www.rsna.org/annual-meeting/attendee-resources/faculty-and-presenter-resources',
    'https://doi.org/10.1371/journal.pbio.1002128',
    'https://dicom.nema.org/medical/dicom/current/output/chtml/part14/chapter_7.html',
    'https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html',
    'https://www.rsna.org/-/media/Files/RSNA/Practice-Tools/RemovingPHI.pdf',
    'https://support.microsoft.com/en-us/accessibility/powerpoint/make-your-powerpoint-presentations-accessible-to-people-with-disabilities',
    'https://wiki.creativecommons.org/wiki/Best_practices_for_attribution'
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
    if ($case.deck_type -notin @($tests.required_deck_types)) {
        $errors.Add("Case $($case.id) has invalid deck type: $($case.deck_type)")
    }
    if ($case.artifact_scope -notin @($tests.required_artifact_scopes)) {
        $errors.Add("Case $($case.id) has invalid artifact scope: $($case.artifact_scope)")
    }
    if ($case.evidence_state -notin @($tests.required_evidence_states)) {
        $errors.Add("Case $($case.id) has invalid evidence state: $($case.evidence_state)")
    }
    if ([string]::IsNullOrWhiteSpace($case.prompt) -or @($case.required_checks).Count -lt 6) {
        $errors.Add("Case $($case.id) needs a prompt and at least six required checks.")
    }
}
foreach ($deckType in @($tests.required_deck_types)) {
    if ($deckType -notin @($positiveCases.deck_type)) {
        $errors.Add("Missing positive deck-type coverage: $deckType")
    }
}
foreach ($scope in @($tests.required_artifact_scopes)) {
    if ($scope -notin @($positiveCases.artifact_scope)) {
        $errors.Add("Missing positive artifact-scope coverage: $scope")
    }
}

$requiredArtifactFidelity = @(
    'NATIVE_EDITABLE',
    'MIXED_EDITABLE_AND_SOURCE_CROPS',
    'RENDERED_REFERENCE_ONLY'
)
if (Compare-Object $requiredArtifactFidelity @($tests.required_artifact_fidelity_classes)) {
    $errors.Add('Artifact fidelity classes must match the registered three-class contract.')
}
$requiredEvidenceFidelity = @('EVIDENCE_CRITICAL', 'EVIDENCE_SUPPORTING', 'EXPLORATORY_STORYBOARD')
if (Compare-Object $requiredEvidenceFidelity @($tests.required_evidence_fidelity_classes)) {
    $errors.Add('Evidence fidelity classes must match the registered three-class contract.')
}

$deckBriefText = Get-Content -LiteralPath (Join-Path $skillRoot 'templates/deck-brief.md') -Raw
foreach ($phrase in @('Artifact fidelity class', 'Evidence fidelity class', 'visible placeholders')) {
    if ($deckBriefText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Deck brief is missing fidelity contract phrase: $phrase")
    }
}

$slideMapText = Get-Content -LiteralPath (Join-Path $skillRoot 'templates/slide-map-and-source-ledger.md') -Raw
foreach ($phrase in @('Upstream Claim ID', 'Evidence-carrier fidelity', 'MISSING', 'UNVERIFIED', 'Editable PPTX parity/round-trip')) {
    if ($slideMapText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Slide-map template is missing evidence-fidelity phrase: $phrase")
    }
}
foreach ($state in @($tests.required_evidence_states)) {
    if ($state -notin @($positiveCases.evidence_state)) {
        $errors.Add("Missing positive evidence-state coverage: $state")
    }
}

$requiredBoundaryOwners = @(
    'radiology-grant',
    'radiology-figure',
    'radiology-table',
    'radiology-writing',
    'radiology-prereview',
    'radiology-submission',
    'radiology-clinical-domain',
    'radiology-acquisition-qc'
)
foreach ($owner in $requiredBoundaryOwners) {
    if ($owner -notin @($boundaryCases.expected_owner)) {
        $errors.Add("Missing boundary-owner coverage: $owner")
    }
}

if (@($tests.invariants).Count -lt 20) {
    $errors.Add('At least twenty scientific-presentation invariants are required.')
}

if ($errors.Count -gt 0) {
    Write-Host 'FAIL: radiology scientific presentation validation' -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: radiology scientific presentation validation' -ForegroundColor Green
Write-Host "Positive routing cases: $($positiveCases.Count)"
Write-Host "Boundary cases: $($boundaryCases.Count)"
Write-Host "Deck types covered: $(@($tests.required_deck_types).Count)"
Write-Host "Artifact scopes covered: $(@($tests.required_artifact_scopes).Count)"
Write-Host "Artifact fidelity classes: $(@($tests.required_artifact_fidelity_classes).Count)"
Write-Host "Evidence fidelity classes: $(@($tests.required_evidence_fidelity_classes).Count)"
Write-Host "Evidence states covered: $(@($tests.required_evidence_states).Count)"
Write-Host "Scientific invariants: $(@($tests.invariants).Count)"
Write-Host "Authoritative source entries: $($sourceUrls.Count)"
Write-Host 'Note: static validation does not execute prompts, inspect a real deck, or prove presentation behavior.'
