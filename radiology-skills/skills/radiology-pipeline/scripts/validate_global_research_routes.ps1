[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$pipelineRoot = Split-Path -Parent $PSScriptRoot
$skillsRoot = Split-Path -Parent $pipelineRoot
$casesPath = Join-Path $pipelineRoot 'tests/global-research-routing-cases.json'
$routingPath = Join-Path $pipelineRoot 'references/research-intent-routing.md'
$cyclePath = Join-Path $pipelineRoot 'references/research-decision-cycle.md'
$packetPath = Join-Path $pipelineRoot 'assets/research-decision-packet.template.md'
$passportPath = Join-Path $pipelineRoot 'references/project-passport-and-registries.md'
$tutorPath = Join-Path $pipelineRoot 'references/tutor-state-machine.md'
$simulationPath = Join-Path $pipelineRoot 'references/simulation-and-teaching-data.md'
$improvementPath = Join-Path $pipelineRoot 'references/evidence-based-skill-improvement-loop.md'
$lifecycleMapPath = Join-Path $pipelineRoot 'references/research-lifecycle-capability-map.md'
$pipelineSkillPath = Join-Path $pipelineRoot 'SKILL.md'

$errors = [System.Collections.Generic.List[string]]::new()
$cases = Get-Content -LiteralPath $casesPath -Raw | ConvertFrom-Json
$routingText = Get-Content -LiteralPath $routingPath -Raw
$cycleText = Get-Content -LiteralPath $cyclePath -Raw
$packetText = Get-Content -LiteralPath $packetPath -Raw
$passportText = Get-Content -LiteralPath $passportPath -Raw
$tutorText = Get-Content -LiteralPath $tutorPath -Raw
$simulationText = Get-Content -LiteralPath $simulationPath -Raw
$improvementText = Get-Content -LiteralPath $improvementPath -Raw
$lifecycleMapText = Get-Content -LiteralPath $lifecycleMapPath -Raw
$pipelineSkillText = Get-Content -LiteralPath $pipelineSkillPath -Raw

$skillNames = @(
    Get-ChildItem -LiteralPath $skillsRoot -Directory |
        Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') } |
        ForEach-Object { $_.Name }
)

$positive = @($cases.positive_cases)
$boundary = @($cases.boundary_cases)
$clarification = @($cases.clarification_cases)
$tutor = @($cases.tutor_cases)
$ids = @($positive.id + $boundary.id + $clarification.id + $tutor.id)
if (($ids | Sort-Object -Unique).Count -ne $ids.Count) {
    $errors.Add('Global routing case IDs must be unique.')
}

if ($cases.schema_version -lt 2) {
    $errors.Add('Global routing cases must use schema_version >= 2 with clarification_cases.')
}

foreach ($case in $positive) {
    if ($case.expected_owner -notin $skillNames) {
        $errors.Add("Unknown positive-case owner $($case.expected_owner) in $($case.id)")
    }
    if ([string]::IsNullOrWhiteSpace($case.prompt) -or [string]::IsNullOrWhiteSpace($case.phase)) {
        $errors.Add("Positive case $($case.id) needs phase and prompt.")
    }
    if ($case.phase -notin @($cases.required_lifecycle_phases)) {
        $errors.Add("Positive case $($case.id) uses an unregistered lifecycle phase: $($case.phase)")
    }
}
foreach ($case in $boundary) {
    foreach ($owner in @($case.owner_a, $case.owner_b)) {
        if ($owner -notin $skillNames) {
            $errors.Add("Unknown boundary owner $owner in $($case.id)")
        }
    }
    if ($case.owner_a -eq $case.owner_b) {
        $errors.Add("Boundary case $($case.id) must distinguish two owners.")
    }
}
$boundaryOwners = @($boundary | ForEach-Object { $_.owner_a; $_.owner_b } | Sort-Object -Unique)
foreach ($skillName in $skillNames) {
    if ($skillName -notin $boundaryOwners) {
        $errors.Add("Skill lacks a global owner-disambiguation boundary case: $skillName")
    }
}
$requiredClarificationPrompts = @(
    '会议摘要',
    '做个 meta-analysis',
    '做外部验证',
    '帮我看看论文',
    '做 PPI/公平性'
)
foreach ($requiredPrompt in $requiredClarificationPrompts) {
    if ($requiredPrompt -notin @($clarification.prompt)) {
        $errors.Add("Missing required bare-prompt clarification case: $requiredPrompt")
    }
}
foreach ($case in $clarification) {
    if ([string]::IsNullOrWhiteSpace($case.id) -or [string]::IsNullOrWhiteSpace($case.prompt)) {
        $errors.Add('Every clarification case needs a non-empty id and prompt.')
    }
    if ($case.expected_action -cne 'CLARIFY') {
        $errors.Add("Clarification case $($case.id) must declare expected_action=CLARIFY.")
    }
    if ($case.silent_primary_owner_forbidden -isnot [bool] -or -not $case.silent_primary_owner_forbidden) {
        $errors.Add("Clarification case $($case.id) must forbid silent primary-owner selection.")
    }
    if ($null -ne $case.PSObject.Properties['expected_owner'] -or $null -ne $case.PSObject.Properties['primary_owner']) {
        $errors.Add("Clarification case $($case.id) must not preselect expected_owner or primary_owner.")
    }
    $options = @($case.disambiguation_options)
    if ($options.Count -lt 2) {
        $errors.Add("Clarification case $($case.id) needs at least two disambiguation_options.")
        continue
    }
    $optionIds = @($options.option_id)
    $optionOwners = @($options.owner)
    if (($optionIds | Sort-Object -Unique).Count -ne $optionIds.Count) {
        $errors.Add("Clarification case $($case.id) option_id values must be unique.")
    }
    if (($optionOwners | Sort-Object -Unique).Count -lt 2) {
        $errors.Add("Clarification case $($case.id) must distinguish at least two owners.")
    }
    foreach ($option in $options) {
        if ([string]::IsNullOrWhiteSpace($option.option_id) -or [string]::IsNullOrWhiteSpace($option.meaning)) {
            $errors.Add("Clarification case $($case.id) has an option without option_id or meaning.")
        }
        if ($option.owner -notin $skillNames) {
            $errors.Add("Unknown clarification owner $($option.owner) in $($case.id)")
        }
    }
}
foreach ($case in $tutor) {
    if ($case.expected_owner -notin $skillNames) {
        $errors.Add("Unknown tutor-case owner $($case.expected_owner) in $($case.id)")
    }
    if ($case.interaction_style -notin @('direct-expert', 'guided-learning')) {
        $errors.Add("Tutor case $($case.id) has invalid interaction_style.")
    }
    if ($case.artifact_mode -notin @('read-only', 'authorized-write')) {
        $errors.Add("Tutor case $($case.id) has invalid artifact_mode.")
    }
    if ($case.simulation_authorized -isnot [bool]) {
        $errors.Add("Tutor case $($case.id) must declare boolean simulation_authorized.")
    }
    if ([string]::IsNullOrWhiteSpace($case.prompt)) {
        $errors.Add("Tutor case $($case.id) needs a prompt.")
    }
}

$descriptionRows = @(
    Get-ChildItem -LiteralPath $skillsRoot -Directory |
        Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') } |
        ForEach-Object {
            $skillPath = Join-Path $_.FullName 'SKILL.md'
            $skillText = Get-Content -LiteralPath $skillPath -Raw
            $match = [regex]::Match($skillText, '(?m)^description:\s*["''](?<value>.*)["'']\s*$')
            if (-not $match.Success) {
                $errors.Add("Skill has no one-line quoted description: $($_.Name)")
                return
            }
            [pscustomobject]@{
                Name = $_.Name
                Length = $match.Groups['value'].Value.Length
                BudgetLength = $match.Groups['value'].Value.Length + 2
            }
        }
)
$descriptionTotal = ($descriptionRows | Measure-Object -Property BudgetLength -Sum).Sum
if ($descriptionTotal -gt 5000) {
    $errors.Add("Discovery description budget exceeds 5000 characters: $descriptionTotal")
}
foreach ($row in $descriptionRows) {
    if ($row.Length -gt 220) {
        $errors.Add("Discovery description exceeds 220 characters: $($row.Name)=$($row.Length)")
    }
}

$owners = @($positive.expected_owner)
foreach ($skill in $skillNames) {
    if ($skill -notin $owners) {
        $errors.Add("Skill lacks a positive global-intent route: $skill")
    }
    if ($routingText.IndexOf("``$skill``", [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Skill is absent from the human routing contract: $skill")
    }
}
if (($owners | Sort-Object -Unique).Count -ne $skillNames.Count) {
    $errors.Add('Positive route ownership must cover every skill at least once in this registry.')
}

foreach ($phase in @($cases.required_lifecycle_phases)) {
    if ($phase -notin @($positive.phase)) {
        $errors.Add("Missing lifecycle phase coverage: $phase")
    }
}

$routingPhrases = @(
    'exactly one **primary owner**', 'current scientific decision', 'Handoff minimum',
    'parameter provenance', 'metric fit', 'whole-manuscript', 'submission files', 'estimand',
    'research-integrity', 'research-ops', 'consensus-guideline', 'qualitative-mixed-methods',
    'health-economics', 'reproducibility', 'dissemination', 'bibliometrics', 'innovation-transfer',
    'post-publication', 'PPI/stakeholder/equity decision ledger', 'production proofs/queries',
    'living-review surveillance', 'cross-artifact staleness map',
    'HUMAN_INSTITUTIONAL_SUBMISSION_REQUIRED', 'post-award conditions'
)
foreach ($phrase in $routingPhrases) {
    if ($routingText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Routing contract missing phrase: $phrase")
    }
}

$tutorPhrases = @(
    'direct-expert', 'guided-learning', 'T1-baseline', 'T4-teach-back', 'T5-transfer',
    'mastery_status', 'read-only by default', 'does not authorize',
    'explicitly authorizes', 'unresolved learner questions'
)
$tutorSurface = $tutorText + "`n" + $simulationText + "`n" + $pipelineSkillText + "`n" + $routingText
foreach ($phrase in $tutorPhrases) {
    if ($tutorSurface.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Tutor contract missing phrase: $phrase")
    }
}

foreach ($state in 0..9) {
    if ($cycleText.IndexOf("D$state ", [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Research decision cycle missing state D$state")
    }
}
$cyclePhrases = @(
    'Assumption register', 'Experiment/analysis plan', 'protected-test access',
    'Negative, null and failure evidence', 'Learner-facing guidance', 'knowledge reuse'
)
foreach ($phrase in $cyclePhrases) {
    if (($cycleText + "`n" + $packetText).IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Decision-cycle artifact missing phrase: $phrase")
    }
}

$evidenceSynthesisPhrases = @(
    'study_scope=evidence-synthesis', 'Evidence-synthesis decision plan',
    'study-family ledger', 'effect-row ledger', 'primary_evidence_state=synthesized'
)
foreach ($phrase in $evidenceSynthesisPhrases) {
    if (($cycleText + "`n" + $packetText + "`n" + $passportText).IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Evidence-synthesis decision contract missing phrase: $phrase")
    }
}

$passportHandoffPhrases = @(
    'Receiving owner:',
    'Claim boundary / prohibited upgrade:'
)
foreach ($phrase in $passportHandoffPhrases) {
    if ($passportText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Project-passport compact handoff missing phrase: $phrase")
    }
}

if ($pipelineSkillText.IndexOf('references/evidence-based-skill-improvement-loop.md', [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
    $errors.Add('Pipeline SKILL.md does not route to the evidence-based improvement loop.')
}
$improvementPhrases = @(
    'ROUTING_ERROR', 'EXECUTION_LAPSE', 'TEMPLATE_FRICTION', 'HANDOFF_GAP',
    'SOURCE_DRIFT', 'RUNTIME_LIMITATION', 'NO_DEFECT',
    'at least two distinct run IDs', 'P0/P1 invariant break',
    'persistent_change_authorized=true', 'smallest proposed change', 'regression to add', 'rollback'
)
foreach ($phrase in $improvementPhrases) {
    if ($improvementText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Evidence-based improvement contract missing phrase: $phrase")
    }
}

$requiredPostPublicationCaseIds = @(
    'postpublication-integrity-correction',
    'postpublication-current-citation',
    'postpublication-production-deposit',
    'postpublication-data-request',
    'living-review-update',
    'postpublication-derivative-correction',
    'deployed-system-retirement',
    'postpublication-project-staleness'
)
foreach ($caseId in $requiredPostPublicationCaseIds) {
    if ($caseId -notin @($positive.id)) {
        $errors.Add("Missing post-publication positive route: $caseId")
    }
}
$requiredFundingLifecycleCaseIds = @(
    'funder-package-finalization',
    'post-award-funder-reporting'
)
foreach ($caseId in $requiredFundingLifecycleCaseIds) {
    if ($caseId -notin @($positive.id)) {
        $errors.Add("Missing funder lifecycle positive route: $caseId")
    }
}
$requiredBoundaryCaseIds = @(
    'ppi-design-versus-qualitative-study',
    'ppi-design-versus-ethics',
    'equity-inference-versus-engagement',
    'postpublication-correction-versus-current-citation',
    'postpublication-production-versus-data-request',
    'living-review-versus-bibliometric-snapshot',
    'public-derivative-versus-deployed-system-retirement',
    'funder-package-versus-post-award-reporting'
)
foreach ($caseId in $requiredBoundaryCaseIds) {
    if ($caseId -notin @($boundary.id)) {
        $errors.Add("Missing PPI/equity or post-publication boundary route: $caseId")
    }
}

if ($pipelineSkillText.IndexOf('references/research-lifecycle-capability-map.md', [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
    $errors.Add('Pipeline SKILL.md does not progressively route to the authoritative lifecycle capability map.')
}
$lifecycleMapPhrases = @(
    'authoritative topology',
    'Main lifecycle',
    'Cross-lifecycle assurance planes',
    'Non-linear branches',
    'D0-D9 to Stage 0-11 crosswalk',
    'Branch 5F Funding',
    'Branch 5P Scientific communication',
    'Branch 5T Translation/deployment',
    'Branch 5D Dissemination',
    'Branch 5B Bibliometrics',
    'Branch 5I Innovation/transfer',
    'Stage 11 Published-output lifecycle',
    'PPI, stakeholder participation and equity'
)
foreach ($phrase in $lifecycleMapPhrases) {
    if ($lifecycleMapText.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $errors.Add("Lifecycle capability map missing phrase: $phrase")
    }
}

if ($errors.Count -gt 0) {
    Write-Host "FAIL: global research routing validation ($($errors.Count) issue(s))" -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

Write-Host 'PASS: global research routing validation' -ForegroundColor Green
Write-Host "Skills covered by positive routes: $($skillNames.Count)"
Write-Host "Boundary/disambiguation cases: $($boundary.Count)"
Write-Host "Clarification-before-routing cases: $($clarification.Count)"
Write-Host "Tutor interaction/permission cases: $($tutor.Count)"
Write-Host "Discovery descriptions: $descriptionTotal chars across $($descriptionRows.Count) skills"
Write-Host "Lifecycle phases covered: $(@($cases.required_lifecycle_phases).Count)"
Write-Host 'Research decision states: D0-D9'
