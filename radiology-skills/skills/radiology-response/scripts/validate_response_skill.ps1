#requires -Version 7.0

[CmdletBinding()]
param(
    [Parameter()]
    [string]$SkillRoot = (Split-Path -Parent $PSScriptRoot)
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$failures = [System.Collections.Generic.List[string]]::new()
$root = [IO.Path]::GetFullPath($SkillRoot)

function Add-Failure([string]$Message) { $failures.Add($Message) }

$requiredFiles = @(
    'SKILL.md', 'README.md', 'agents/openai.yaml',
    'references/action-mapping.md', 'references/revision-letter-writing-chain.md',
    'references/imaging-reviewer-playbook.md',
    'references/mechanism-reviewer-playbook.md', 'references/imaging-mechanism-reviewer-playbook.md',
    'references/transparent-peer-review-response-patterns-2024-2026.md',
    'references/transparent-peer-review-response-map-2024-2026.tsv',
    'references/response-audit-gate.md', 'references/reject-decision-tree.md',
    'references/radiogenomics-state-crosswalk.md',
    'references/prereview-response-state-crosswalk.md',
    'templates/point-by-point-response-matrix.md',
    'templates/final-response-and-verification-package.md',
    'templates/local-reviewer-experience-registry.md',
    'templates/response-package-receipt.template.json',
    'scripts/validate_response_package_receipt.py',
    'scripts/test_response_package_receipt.py',
    'tests/response-contract-cases.json'
)
foreach ($relative in $requiredFiles) {
    if (-not (Test-Path -LiteralPath (Join-Path $root $relative) -PathType Leaf)) {
        Add-Failure "Missing required file: $relative"
    }
}

$skillText = Get-Content -Raw -LiteralPath (Join-Path $root 'SKILL.md')
$actionText = Get-Content -Raw -LiteralPath (Join-Path $root 'references/action-mapping.md')
$auditText = Get-Content -Raw -LiteralPath (Join-Path $root 'references/response-audit-gate.md')
$corpusPatternText = Get-Content -Raw -LiteralPath (Join-Path $root 'references/transparent-peer-review-response-patterns-2024-2026.md')
$writingChainText = Get-Content -Raw -LiteralPath (Join-Path $root 'references/revision-letter-writing-chain.md')
$finalTemplateText = Get-Content -Raw -LiteralPath (Join-Path $root 'templates/final-response-and-verification-package.md')
$crosswalkText = Get-Content -Raw -LiteralPath (Join-Path $root 'references/prereview-response-state-crosswalk.md')
$receiptTemplateText = Get-Content -Raw -LiteralPath (Join-Path $root 'templates/response-package-receipt.template.json')
$receiptValidatorText = Get-Content -Raw -LiteralPath (Join-Path $root 'scripts/validate_response_package_receipt.py')
$semanticContracts = @(
    @{ Text = $skillText; Phrase = 'Evidence before rhetoric'; File = 'SKILL.md' },
    @{ Text = $skillText; Phrase = 'Frozen yardstick'; File = 'SKILL.md' },
    @{ Text = $skillText; Phrase = 'comment -> position/rationale -> action and method -> result/evidence'; File = 'SKILL.md' },
    @{ Text = $skillText; Phrase = 'appeal instructions'; File = 'SKILL.md' },
    @{ Text = $skillText; Phrase = 'round-aware ID'; File = 'SKILL.md' },
    @{ Text = $skillText; Phrase = 'validate_response_package_receipt.py'; File = 'SKILL.md' },
    @{ Text = $skillText; Phrase = 'evidence-synthesis'; File = 'SKILL.md' },
    @{ Text = $actionText; Phrase = 'scope-contested/infeasible'; File = 'references/action-mapping.md' },
    @{ Text = $actionText; Phrase = 'ACKNOWLEDGE_ONLY'; File = 'references/action-mapping.md' },
    @{ Text = $actionText; Phrase = 'Editorial obligation'; File = 'references/action-mapping.md' },
    @{ Text = $auditText; Phrase = 'Two-pass evidence-before-persuasion audit'; File = 'references/response-audit-gate.md' },
    @{ Text = $auditText; Phrase = 'Claim strength did not increase'; File = 'references/response-audit-gate.md' },
    @{ Text = $auditText; Phrase = 'unresolved_placeholder_count = 0'; File = 'references/response-audit-gate.md' },
    @{ Text = $auditText; Phrase = 'scientific_validity_certificate'; File = 'references/response-audit-gate.md' },
    @{ Text = $corpusPatternText; Phrase = 'one decisive request class per paper'; File = 'references/transparent-peer-review-response-patterns-2024-2026.md' },
    @{ Text = $corpusPatternText; Phrase = 'result-before-location'; File = 'references/transparent-peer-review-response-patterns-2024-2026.md' },
    @{ Text = $corpusPatternText; Phrase = 'transparent review is not a clean-paper certificate'; File = 'references/transparent-peer-review-response-patterns-2024-2026.md' },
    @{ Text = $writingChainText; Phrase = 'Accept and repair'; File = 'references/revision-letter-writing-chain.md' },
    @{ Text = $writingChainText; Phrase = 'Evidence-based disagreement'; File = 'references/revision-letter-writing-chain.md' },
    @{ Text = $writingChainText; Phrase = 'Cannot perform the requested experiment or analysis'; File = 'references/revision-letter-writing-chain.md' },
    @{ Text = $writingChainText; Phrase = 'Negative or null result'; File = 'references/revision-letter-writing-chain.md' },
    @{ Text = $writingChainText; Phrase = 'Working draft versus submission-ready letter'; File = 'references/revision-letter-writing-chain.md' }
    @{ Text = $crosswalkText; Phrase = 'SCIENTIFIC_PREREVIEW_PASS'; File = 'references/prereview-response-state-crosswalk.md' }
    @{ Text = $crosswalkText; Phrase = 'SCIENTIFIC_PREREVIEW_CONDITIONAL'; File = 'references/prereview-response-state-crosswalk.md' }
    @{ Text = $crosswalkText; Phrase = 'SCIENTIFIC_PREREVIEW_FAIL'; File = 'references/prereview-response-state-crosswalk.md' }
    @{ Text = $crosswalkText; Phrase = 'source_review_state'; File = 'references/prereview-response-state-crosswalk.md' }
    @{ Text = $receiptTemplateText; Phrase = 'affected_claim_ids'; File = 'templates/response-package-receipt.template.json' }
    @{ Text = $receiptTemplateText; Phrase = 'source_review_state'; File = 'templates/response-package-receipt.template.json' }
    @{ Text = $receiptTemplateText; Phrase = 'project_state_digest'; File = 'templates/response-package-receipt.template.json' }
    @{ Text = $receiptTemplateText; Phrase = 'modality_role_digest'; File = 'templates/response-package-receipt.template.json' }
    @{ Text = $receiptTemplateText; Phrase = 'response_package_digest'; File = 'templates/response-package-receipt.template.json' }
    @{ Text = $receiptValidatorText; Phrase = 'canonical_digest'; File = 'scripts/validate_response_package_receipt.py' }
    @{ Text = $receiptValidatorText; Phrase = 'source_artifact_id is not registered in artifacts'; File = 'scripts/validate_response_package_receipt.py' }
    @{ Text = $receiptValidatorText; Phrase = '--source-prereview-receipt'; File = 'scripts/validate_response_package_receipt.py' }
    @{ Text = $receiptValidatorText; Phrase = '--post-prereview-receipt'; File = 'scripts/validate_response_package_receipt.py' }
    @{ Text = $receiptValidatorText; Phrase = 'absent from both bound prereview receipts'; File = 'scripts/validate_response_package_receipt.py' }
    @{ Text = $receiptValidatorText; Phrase = 'must not require a radiogenomics scientific_handoff_digest'; File = 'scripts/validate_response_package_receipt.py' }
    @{ Text = $receiptValidatorText; Phrase = 'evidence-synthesis response artifacts missing frozen roles'; File = 'scripts/validate_response_package_receipt.py' }
    @{ Text = $finalTemplateText; Phrase = 'INTERNAL—DO NOT SUBMIT'; File = 'templates/final-response-and-verification-package.md' }
    @{ Text = $finalTemplateText; Phrase = 'READY_FOR_SUBMISSION_ASSEMBLY'; File = 'templates/final-response-and-verification-package.md' }
    @{ Text = $finalTemplateText; Phrase = 'Author approval receipt'; File = 'templates/final-response-and-verification-package.md' }
    @{ Text = $finalTemplateText; Phrase = 'Source document/version/digest + locator / quote status'; File = 'templates/final-response-and-verification-package.md' }
    @{ Text = $finalTemplateText; Phrase = 'Action code'; File = 'templates/final-response-and-verification-package.md' }
    @{ Text = $finalTemplateText; Phrase = 'N/A—NO_NEW_WORK'; File = 'templates/final-response-and-verification-package.md' }
    @{ Text = $finalTemplateText; Phrase = 'N/A—NO_MANUSCRIPT_CHANGE_JUSTIFIED'; File = 'templates/final-response-and-verification-package.md' }
    @{ Text = $finalTemplateText; Phrase = 'Parent ID / prior IDs'; File = 'templates/final-response-and-verification-package.md' }
    @{ Text = $finalTemplateText; Phrase = 'Verification method/verifier'; File = 'templates/final-response-and-verification-package.md' }
    @{ Text = $finalTemplateText; Phrase = 'Author decision + authority source/approver/date'; File = 'templates/final-response-and-verification-package.md' }
    @{ Text = $finalTemplateText; Phrase = 'No unresolved EDITOR_CLARIFICATION_REQUESTED item remains'; File = 'templates/final-response-and-verification-package.md' }
    @{ Text = $finalTemplateText; Phrase = 'Quantitative analysis: estimand, independent unit, comparator, estimate, uncertainty and location'; File = 'templates/final-response-and-verification-package.md' }
    @{ Text = $finalTemplateText; Phrase = 'Experiment: biological unit, control, intervention, readout, replication, actual result and location'; File = 'templates/final-response-and-verification-package.md' }
    @{ Text = $finalTemplateText; Phrase = 'affected_claim_ids'; File = 'templates/final-response-and-verification-package.md' }
    @{ Text = $finalTemplateText; Phrase = 'source_review_state'; File = 'templates/final-response-and-verification-package.md' }
    @{ Text = $finalTemplateText; Phrase = 'response_package_digest'; File = 'templates/final-response-and-verification-package.md' }
    @{ Text = $finalTemplateText; Phrase = 'risk-of-bias-applicability'; File = 'templates/final-response-and-verification-package.md' }
)
foreach ($contract in $semanticContracts) {
    if ($contract.Text.IndexOf($contract.Phrase, [StringComparison]::OrdinalIgnoreCase) -lt 0) {
        Add-Failure "$($contract.File) is missing semantic contract '$($contract.Phrase)'."
    }
}

try {
    $receiptTemplate = $receiptTemplateText | ConvertFrom-Json -Depth 50
    foreach ($field in @(
        'project_state_digest', 'modality_role_digest', 'analysis_lock_digest',
        'claim_registry_digest', 'scientific_handoff_digest',
        'source_scientific_prereview_state', 'post_revision_scientific_prereview_state',
        'source_scientific_prereview_receipt_digest',
        'post_revision_scientific_prereview_receipt_digest',
        'source_review_items', 'artifacts', 'response_package_digest'
    )) {
        if ($receiptTemplate.PSObject.Properties.Name -notcontains $field) {
            Add-Failure "response-package receipt is missing top-level field '$field'."
        }
    }
    $sourceItems = @($receiptTemplate.source_review_items)
    if ($sourceItems.Count -eq 0) {
        Add-Failure 'response-package receipt needs a source_review_items template row.'
    }
    else {
        foreach ($field in @(
            'finding_id', 'affected_claim_ids', 'criterion', 'source_review_state',
            'source_artifact_id', 'source_artifact_sha256', 'evidence_locator',
            'response_item_id', 'response_closure_state'
        )) {
            if ($sourceItems[0].PSObject.Properties.Name -notcontains $field) {
                Add-Failure "response-package source item is missing field '$field'."
            }
        }
    }
}
catch {
    Add-Failure "response-package-receipt.template.json is invalid: $($_.Exception.Message)"
}

if ($actionText -match [regex]::Escape('N/A—NO_CHANGE_JUSTIFIED')) {
    Add-Failure 'references/action-mapping.md contains the retired no-change alias N/A—NO_CHANGE_JUSTIFIED.'
}

$auditLines = @(Get-Content -LiteralPath (Join-Path $root 'references/response-audit-gate.md'))
$ledgerHeaderIndex = [Array]::FindIndex(
    [string[]]$auditLines,
    [Predicate[string]]{ param($line) $line.StartsWith('| Canonical issue ID |') }
)
if ($ledgerHeaderIndex -lt 0) {
    Add-Failure 'references/response-audit-gate.md is missing the response-ledger table.'
}
else {
    $expectedColumns = ($auditLines[$ledgerHeaderIndex].Trim('|').Split('|')).Count
    foreach ($offset in 1..3) {
        $rowIndex = $ledgerHeaderIndex + $offset
        if ($rowIndex -ge $auditLines.Count) {
            Add-Failure 'references/response-audit-gate.md has a truncated response-ledger table.'
            break
        }
        $actualColumns = ($auditLines[$rowIndex].Trim('|').Split('|')).Count
        if ($actualColumns -ne $expectedColumns) {
            Add-Failure "references/response-audit-gate.md response-ledger row $($offset + 1) has $actualColumns columns; expected $expectedColumns."
        }
    }
}

$casePath = Join-Path $root 'tests/response-contract-cases.json'
if (Test-Path -LiteralPath $casePath) {
    try { $caseDoc = Get-Content -Raw -LiteralPath $casePath | ConvertFrom-Json -Depth 50 }
    catch { Add-Failure "response-contract-cases.json is invalid: $($_.Exception.Message)"; $caseDoc = $null }
    if ($null -ne $caseDoc) {
        $cases = @($caseDoc.cases)
        if ($cases.Count -ne 26) { Add-Failure "Expected 26 response contract cases; found $($cases.Count)." }
        $requiredCaseIds = @(
            'post-review-appeal-policy-dependent', 'desk-reject-appeal-brief',
            'final-placeholder-blocker', 'round-two-reopens-comment', 'praise-only-comment',
            'stale-artifact-manifest', 'quoted-revision-text-mismatch',
            'reviewer-confirmation-without-artifact', 'negative-null-result-propagation',
            'duplicate-comment-cross-reference', 'answer-from-existing-record',
            'no-change-justified-final', 'review-study-family-overlap-revision',
            'ambiguous-editor-instruction'
        )
        foreach ($requiredCaseId in $requiredCaseIds) {
            if ($cases.id -notcontains $requiredCaseId) {
                Add-Failure "Missing required response regression case '$requiredCaseId'."
            }
        }
        $allowedRequestClasses = @(
            'manuscript-grounded-defect', 'clarification-needed', 'optional-strengthening',
            'reviewer-preference', 'scope-contested-or-infeasible',
            'non-actionable-summary-or-praise', 'N/A—AUDIT_CONTROL'
        )
        $allowedScopes = @(
            'all', 'imaging-only', 'mechanism-only', 'imaging-mechanism', 'evidence-synthesis'
        )
        foreach ($duplicate in @($cases | Group-Object id | Where-Object Count -gt 1)) {
            Add-Failure "Duplicate response case id: $($duplicate.Name)"
        }
        foreach ($case in $cases) {
            foreach ($field in @('id', 'scope', 'scenario', 'expected_request_class')) {
                if ([string]::IsNullOrWhiteSpace([string]$case.$field)) {
                    Add-Failure "Case '$($case.id)' has empty field '$field'."
                }
            }
            if ([string]$case.expected_request_class -notin $allowedRequestClasses) {
                Add-Failure "Case '$($case.id)' has unknown request class '$($case.expected_request_class)'."
            }
            if ([string]$case.scope -notin $allowedScopes) {
                Add-Failure "Case '$($case.id)' has unknown scope '$($case.scope)'."
            }
            if (@($case.expected_action_codes).Count -eq 0 -or @($case.required_outputs).Count -eq 0 -or @($case.forbidden_claims).Count -eq 0) {
                Add-Failure "Case '$($case.id)' must define action, required-output and forbidden-claim contracts."
            }
            foreach ($code in @($case.expected_action_codes)) {
                if ($actionText.IndexOf("``$code``", [StringComparison]::OrdinalIgnoreCase) -lt 0) {
                    Add-Failure "Case '$($case.id)' uses undeclared action code '$code'."
                }
            }
            foreach ($relative in @($case.references)) {
                if (-not (Test-Path -LiteralPath (Join-Path $root $relative) -PathType Leaf)) {
                    Add-Failure "Case '$($case.id)' references missing file '$relative'."
                }
            }
        }
        Write-Output "Response contract cases: $($cases.Count)"
    }
}

foreach ($markdown in Get-ChildItem -LiteralPath $root -Recurse -File -Filter '*.md') {
    $text = Get-Content -Raw -LiteralPath $markdown.FullName
    foreach ($match in [regex]::Matches($text, '\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)')) {
        $target = $match.Groups[1].Value
        if ($target -match '^[a-z]+://' -or $target -match '^mailto:') { continue }
        $resolved = [IO.Path]::GetFullPath((Join-Path $markdown.DirectoryName $target))
        if (-not (Test-Path -LiteralPath $resolved)) {
            Add-Failure "Broken Markdown link in $($markdown.Name): $target"
        }
    }
}

$evidenceAudit = Join-Path $root 'scripts/audit_response_evidence_map.ps1'
if (-not (Test-Path -LiteralPath $evidenceAudit -PathType Leaf)) {
    Add-Failure 'Missing response evidence-map audit script.'
}
else {
    $powerShellHost = (Get-Process -Id $PID).Path
    & $powerShellHost -NoLogo -NoProfile -File $evidenceAudit
    if ($LASTEXITCODE -ne 0) {
        Add-Failure "Response evidence-map audit exited with code $LASTEXITCODE."
    }
}

if ($failures.Count -gt 0) {
    Write-Output "Radiology response skill validation: FAIL ($($failures.Count))"
    $failures | ForEach-Object { Write-Output "- $_" }
    exit 1
}

Write-Output 'Radiology response skill validation: PASS'
exit 0
