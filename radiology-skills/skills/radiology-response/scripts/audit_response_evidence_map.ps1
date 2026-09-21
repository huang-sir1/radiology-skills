#requires -Version 7.0

[CmdletBinding()]
param(
    [Parameter()]
    [string]$ResponseMapPath = (Join-Path (Split-Path -Parent $PSScriptRoot) 'references/transparent-peer-review-response-map-2024-2026.tsv'),

    [Parameter()]
    [string]$CanonicalCorpusPath = (Join-Path (Split-Path -Parent (Split-Path -Parent $PSScriptRoot)) 'radiology-radiogenomics/references/transparent-peer-review-corpus-2024-2026.tsv'),

    [Parameter()]
    [string]$PatternsPath = (Join-Path (Split-Path -Parent $PSScriptRoot) 'references/transparent-peer-review-response-patterns-2024-2026.md')
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$errors = [System.Collections.Generic.List[string]]::new()

$required = @(
    'record_id', 'doi', 'journal', 'publication_date', 'primary_stratum', 'post_publication_status', 'request_class',
    'concern_codes', 'concern_ontology_version', 'canonical_concern_families',
    'governing_criterion', 'decisive_concern', 'author_action', 'closure_evidence',
    'closure_status', 'author_response_strategy', 'review_locator', 'response_locator',
    'portable_skill_rule', 'review_file_url', 'review_file_sha256'
)
$requestClasses = @(
    'manuscript-grounded-defect', 'clarification-needed', 'optional-strengthening',
    'reviewer-preference', 'scope-contested-or-infeasible'
)
$closureStates = @(
    'experiment-or-analysis-added', 'analysis-or-evidence-added', 'text-or-claim-revised',
    'declined-with-explicit-boundary', 'evidence-based-pushback', 'partially-addressed',
    'reviewer-confirmed', 'author-response-documented'
)

foreach ($path in @($ResponseMapPath, $CanonicalCorpusPath)) {
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        throw "Required evidence map is missing: $path"
    }
}

$rows = @(Import-Csv -LiteralPath $ResponseMapPath -Delimiter "`t")
$canonical = @(Import-Csv -LiteralPath $CanonicalCorpusPath -Delimiter "`t")
if ($rows.Count -ne 100) { $errors.Add("Expected 100 response-map rows; found $($rows.Count).") }
if ($canonical.Count -ne 100) { $errors.Add("Expected 100 canonical rows; found $($canonical.Count).") }
if ($rows.Count -eq 0) { throw 'Response evidence map is empty.' }

$actualColumns = @($rows[0].PSObject.Properties.Name)
foreach ($column in $required) {
    if ($column -notin $actualColumns) { $errors.Add("Missing required column '$column'.") }
}

foreach ($row in $rows) {
    $id = [string]$row.record_id
    foreach ($column in $required) {
        if ($column -in $actualColumns -and [string]::IsNullOrWhiteSpace([string]$row.$column)) {
            $errors.Add("[$id] Empty field '$column'.")
        }
    }
    if ($id -notmatch '^TPR\d{3}$') { $errors.Add("[$id] Invalid record ID.") }
    if ([string]$row.doi -notmatch '^10\.\d{4,9}/\S+$') { $errors.Add("[$id] Invalid DOI.") }
    if ([string]$row.request_class -notin $requestClasses) { $errors.Add("[$id] Invalid request class '$($row.request_class)'.") }
    if ([string]$row.closure_status -notin $closureStates) { $errors.Add("[$id] Invalid closure state '$($row.closure_status)'.") }
    if ([string]$row.review_file_sha256 -notmatch '^[A-Fa-f0-9]{64}$') { $errors.Add("[$id] Invalid review-file SHA-256.") }
    if ([string]$row.review_file_url -notmatch '^https://') { $errors.Add("[$id] Review URL must use HTTPS.") }
    if ([string]$row.post_publication_status -notmatch '^(NO_NOTICE_SIGNAL_FOUND|CORRECTION|PUBLISHER_CORRECTION|EDITOR_NOTE|RETRACTION|EXPRESSION_OF_CONCERN) as screened \d{4}-\d{2}-\d{2}:') { $errors.Add("[$id] Invalid or undated post-publication screen status.") }
    if ([string]$row.review_locator -notmatch '(?i)(p\.?\s*\d+|page\s*\d+)') { $errors.Add("[$id] Review locator lacks a page.") }
    if ([string]$row.response_locator -notmatch '(?i)(p\.?\s*\d+|page\s*\d+)') { $errors.Add("[$id] Response locator lacks a page.") }
    if ([string]$row.author_response_strategy -notmatch '\|') { $errors.Add("[$id] Response strategy must expose at least two explicit moves.") }
    foreach ($narrativeField in @('decisive_concern', 'author_action', 'closure_evidence', 'portable_skill_rule')) {
        if ([string]$row.$narrativeField -notmatch '[.!?]["'']?$') {
            $errors.Add("[$id] $narrativeField appears truncated or is not a complete paraphrased sentence.")
        }
    }
    foreach ($responseField in @('author_action', 'closure_evidence')) {
        if ([string]$row.$responseField -match '(?i)\b(thanks? for|thank you|we are grateful|we appreciate(?: the reviewer)?)\b') {
            $errors.Add("[$id] $responseField contains courtesy boilerplate suggesting an un-paraphrased response excerpt.")
        }
    }
}

foreach ($field in @('record_id', 'doi')) {
    foreach ($duplicate in @($rows | Group-Object { ([string]$_.$field).Trim().ToLowerInvariant() } | Where-Object Count -gt 1)) {
        $errors.Add("Duplicate ${field}: '$($duplicate.Name)'.")
    }
}

$canonicalById = @{}
foreach ($row in $canonical) { $canonicalById[[string]$row.record_id] = $row }
foreach ($row in $rows) {
    $id = [string]$row.record_id
    if (-not $canonicalById.ContainsKey($id)) {
        $errors.Add("[$id] Missing from canonical corpus.")
        continue
    }
    $source = $canonicalById[$id]
    foreach ($field in $required | Where-Object { $_ -ne 'record_id' }) {
        if ([string]$row.$field -cne [string]$source.$field) {
            $errors.Add("[$id] Field '$field' is not synchronized with the canonical corpus.")
        }
    }
}

$tpr097 = @($rows | Where-Object record_id -eq 'TPR097')
if ($tpr097.Count -ne 1 -or [string]$tpr097[0].response_locator -notmatch '(?i)pp\.21-22') {
    $errors.Add('[TPR097] Response locator must retain the registered-report simulation action pages pp.21-22.')
}

# The compact response-writing lessons contain exact corpus-derived counts. Verify them against the
# synchronized map so a later row-level scientific correction cannot leave stale teaching claims.
if (-not (Test-Path -LiteralPath $PatternsPath -PathType Leaf)) {
    $errors.Add("Transparent-review response-patterns file is missing: $PatternsPath")
}
else {
    $patterns = Get-Content -LiteralPath $PatternsPath -Raw
    $closureCounts = @{}
    foreach ($group in @($rows | Group-Object closure_status)) { $closureCounts[$group.Name] = [int]$group.Count }
    $closurePattern = ('The coded closure states are\s*{0} experiment-or-analysis added,\s*{1} analysis-or-evidence added,\s*{2} text-or-claim revised,\s*{3} author-response documented,\s*{4} partially addressed,\s*{5} reviewer confirmed,\s*{6} evidence-based pushback\s*and {7} declined with an explicit boundary\.' -f
        $closureCounts['experiment-or-analysis-added'],
        $closureCounts['analysis-or-evidence-added'],
        $closureCounts['text-or-claim-revised'],
        $closureCounts['author-response-documented'],
        $closureCounts['partially-addressed'],
        $closureCounts['reviewer-confirmed'],
        $closureCounts['evidence-based-pushback'],
        $closureCounts['declined-with-explicit-boundary'])
    if ($patterns -notmatch $closurePattern) {
        $errors.Add('Transparent-review response patterns have stale closure-state counts.')
    }

    $strategyCounts = @{ A = 0; B = 0; C = 0; D = 0 }
    foreach ($row in $rows) {
        $strategy = if ([string]$row.closure_status -in @('declined-with-explicit-boundary', 'evidence-based-pushback') -or [string]$row.request_class -eq 'scope-contested-or-infeasible') {
            'D'
        }
        elseif ([string]$row.closure_status -eq 'partially-addressed' -or [string]$row.author_response_strategy -match '^accept-or-partially-accept') {
            'C'
        }
        elseif ([string]$row.closure_status -eq 'text-or-claim-revised' -or [string]$row.author_response_strategy -match '^clarify-rationale') {
            'B'
        }
        else { 'A' }
        $strategyCounts[$strategy]++
    }
    $strategyPattern = ('yields\s+{0}\s+accept-and-repair,\s*{1}\s+clarify/rewrite,\s*{2}\s+partially accept and\s*{3}\s+evidence-based contest/infeasibility routes\.' -f
        $strategyCounts.A, $strategyCounts.B, $strategyCounts.C, $strategyCounts.D)
    if ($patterns -notmatch $strategyPattern) {
        $errors.Add('Transparent-review response patterns have stale dominant-response-architecture counts.')
    }

    $requestCounts = @{}
    foreach ($group in @($rows | Group-Object request_class)) { $requestCounts[$group.Name] = [int]$group.Count }
    foreach ($requestClass in $requestClasses) {
        if (-not $requestCounts.ContainsKey($requestClass)) { $requestCounts[$requestClass] = 0 }
    }
    $requestPatterns = [ordered]@{
        'manuscript-grounded-defect' = ('{0}\s+manuscript-grounded\s+defects' -f $requestCounts['manuscript-grounded-defect'])
        'clarification-needed' = ('{0}\s+clarification-needed\s+items' -f $requestCounts['clarification-needed'])
        'reviewer-preference' = ('{0}\s+reviewer\s+preferences' -f $requestCounts['reviewer-preference'])
        'optional-strengthening' = ('{0}\s+optional\s+strengthening\s+requests' -f $requestCounts['optional-strengthening'])
        'scope-contested-or-infeasible' = ('{0}\s+scope-contested/infeasible\s+request' -f $requestCounts['scope-contested-or-infeasible'])
    }
    foreach ($requestClass in $requestPatterns.Keys) {
        if ($patterns -notmatch $requestPatterns[$requestClass]) {
            $errors.Add("Transparent-review response patterns lack the current request-class count for '$requestClass' ($($requestCounts[$requestClass])).")
        }
    }
}

Write-Output "Response evidence map rows: $($rows.Count)"
Write-Output 'Request classes:'
$rows | Group-Object request_class | Sort-Object Name | ForEach-Object { Write-Output ("- {0}: {1}" -f $_.Name, $_.Count) }
Write-Output 'Closure states:'
$rows | Group-Object closure_status | Sort-Object Name | ForEach-Object { Write-Output ("- {0}: {1}" -f $_.Name, $_.Count) }

if ($errors.Count -gt 0) {
    Write-Output "Response evidence-map audit: FAIL ($($errors.Count))"
    $errors | ForEach-Object { Write-Output "- $_" }
    exit 1
}

Write-Output 'Response evidence-map audit: PASS'
exit 0
