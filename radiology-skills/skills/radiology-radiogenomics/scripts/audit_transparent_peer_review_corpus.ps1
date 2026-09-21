#requires -Version 7.0

[CmdletBinding()]
param(
    [Parameter()]
    [string]$CorpusPath = (Join-Path (Split-Path -Parent $PSScriptRoot) 'references/transparent-peer-review-corpus-2024-2026.tsv'),

    [Parameter()]
    [string]$LessonsPath = (Join-Path (Split-Path -Parent $PSScriptRoot) 'references/transparent-peer-review-lessons-2024-2026.md'),

    [Parameter()]
    [string]$OntologyPath = (Join-Path (Split-Path -Parent $PSScriptRoot) 'references/transparent-peer-review-concern-ontology-v1.tsv'),

    [Parameter()]
    [switch]$VerifyRemote
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$errors = [System.Collections.Generic.List[string]]::new()
$windowStart = [datetime]'2024-08-22'
$windowEnd = [datetime]'2026-08-22'

$requiredColumns = @(
    'record_id', 'title', 'journal', 'publication_date', 'doi', 'venue_tier',
    'venue_selection_basis', 'journal_metric_note', 'primary_stratum', 'secondary_modalities',
    'study_content', 'article_url', 'review_file_url', 'review_material_type', 'review_rounds',
    'reviewer_count', 'review_file_sha256', 'review_pages', 'review_text_chars', 'extraction_method',
    'access_status', 'post_publication_status', 'concern_codes', 'concern_ontology_version',
    'canonical_concern_families', 'decisive_concern',
    'request_class', 'governing_criterion', 'author_action', 'minimum_repair',
    'stronger_optional_route', 'closure_evidence', 'closure_status', 'author_response_strategy',
    'manuscript_change', 'portable_skill_rule', 'review_locator', 'response_locator',
    'verification_note'
)

$allowedStrata = @(
    'imaging-ai', 'radiomics', 'digital-pathology', 'bulk-rna', 'single-cell',
    'spatial', 'multi-omics', 'perturbation', 'imaging-mechanism'
)
$allowedTiers = @('1-main-journal', '2-major-specialist', '3-high-impact-fallback')
$allowedRequestClasses = @(
    'manuscript-grounded-defect', 'clarification-needed', 'optional-strengthening',
    'reviewer-preference', 'scope-contested-or-infeasible'
)
$allowedClosureStates = @(
    'experiment-or-analysis-added', 'analysis-or-evidence-added', 'text-or-claim-revised',
    'declined-with-explicit-boundary', 'evidence-based-pushback', 'partially-addressed',
    'reviewer-confirmed', 'author-response-documented'
)
$allowedArticleHosts = @('nature.com', 'www.nature.com', 'cell.com', 'www.cell.com', 'sciencedirect.com', 'www.sciencedirect.com')
$allowedReviewHosts = @(
    'static-content.springer.com', 'media.springernature.com', 'cell.com', 'www.cell.com',
    'ars.els-cdn.com', 'linkinghub.elsevier.com'
)

function Add-AuditError {
    param([Parameter(Mandatory)][string]$Message)
    $errors.Add($Message)
}

function Get-UriHost {
    param([Parameter(Mandatory)][string]$Value)
    try {
        return ([uri]$Value).DnsSafeHost.ToLowerInvariant()
    }
    catch {
        return ''
    }
}

if (-not (Test-Path -LiteralPath $CorpusPath -PathType Leaf)) {
    throw "Transparent peer-review corpus is missing: $CorpusPath"
}

if (-not (Test-Path -LiteralPath $OntologyPath -PathType Leaf)) {
    throw "Concern ontology is missing: $OntologyPath"
}
$ontologyRows = @(Import-Csv -LiteralPath $OntologyPath -Delimiter "`t")
$ontologyVersions = @($ontologyRows.ontology_version | Sort-Object -Unique)
if ($ontologyVersions.Count -ne 1 -or [string]::IsNullOrWhiteSpace([string]$ontologyVersions[0])) {
    throw "Concern ontology must contain exactly one non-empty version; found '$($ontologyVersions -join ',')'."
}
$ontologyVersion = [string]$ontologyVersions[0]
$ontologyMap = @{}
foreach ($ontologyRow in $ontologyRows) {
    $rawCode = ([string]$ontologyRow.raw_concern_code).Trim().ToUpperInvariant()
    $family = ([string]$ontologyRow.canonical_concern_family).Trim().ToUpperInvariant()
    if ([string]::IsNullOrWhiteSpace($rawCode) -or [string]::IsNullOrWhiteSpace($family)) {
        throw 'Concern ontology contains an empty raw code or canonical family.'
    }
    if ($ontologyMap.ContainsKey($rawCode)) {
        throw "Concern ontology contains duplicate raw code '$rawCode'."
    }
    $ontologyMap[$rawCode] = $family
}
$familyCriterionPatterns = @{
    'CONTRIBUTION_CLAIM_CALIBRATION' = '(?i)\bcontribution\b.*\bclaim\b'
    'COHORT_LABEL_UNIT_LEAKAGE' = '(?i)\bindependent unit\b'
    'COMPARATOR_CONTROL_ABLATION' = '(?i)\bincremental value\b.*\bcompar'
    'STATISTICAL_INFERENCE_CONFOUNDING' = '(?i)\bestimand\b.*\buncertainty\b'
    'EXTERNAL_VALIDATION_ROBUSTNESS' = '(?i)\bgeneralization\b.*\bvalidation\b'
    'MEASUREMENT_QC_SPATIAL_TRUTH' = '(?i)\bmeasurement\b.*\breference standard\b'
    'MULTIOMICS_ALIGNMENT_ANNOTATION' = '(?i)\bcross-modal\b.*\bmatched units\b'
    'MECHANISM_FUNCTION_PERTURBATION' = '(?i)\bmechanistic language\b.*\bintervention\b'
    'INTERPRETABILITY_ALTERNATIVES' = '(?i)\battribution\b.*\balternative explanations\b'
    'REPRODUCIBILITY_OPENNESS' = '(?i)\breconstructable\b.*\bversioned\b'
    'CLINICAL_ETHICS_FEASIBILITY' = '(?i)\bclaimed use\b.*\bfeasibility\b'
}

$rows = @(Import-Csv -LiteralPath $CorpusPath -Delimiter "`t")
if ($rows.Count -ne 100) {
    Add-AuditError "Expected exactly 100 paper-level rows; found $($rows.Count)."
}
if ($rows.Count -eq 0) {
    throw 'Transparent peer-review corpus is empty.'
}

$actualColumns = @($rows[0].PSObject.Properties.Name)
foreach ($column in $requiredColumns) {
    if ($column -notin $actualColumns) {
        Add-AuditError "Missing required column '$column'."
    }
}

foreach ($row in $rows) {
    $id = [string]$row.record_id
    foreach ($column in $requiredColumns) {
        if ($column -in $actualColumns -and [string]::IsNullOrWhiteSpace([string]$row.$column)) {
            Add-AuditError "[$id] Empty required field '$column'."
        }
    }

    if ($id -notmatch '^TPR\d{3}$') {
        Add-AuditError "[$id] record_id must match TPR###."
    }
    if ([string]$row.doi -notmatch '^10\.\d{4,9}/\S+$') {
        Add-AuditError "[$id] Invalid DOI '$($row.doi)'."
    }

    $publicationDate = [datetime]::MinValue
    if (-not [datetime]::TryParseExact(
        [string]$row.publication_date,
        'yyyy-MM-dd',
        [Globalization.CultureInfo]::InvariantCulture,
        [Globalization.DateTimeStyles]::None,
        [ref]$publicationDate
    )) {
        Add-AuditError "[$id] publication_date is not yyyy-MM-dd."
    }
    elseif ($publicationDate -lt $windowStart -or $publicationDate -gt $windowEnd) {
        Add-AuditError "[$id] publication_date is outside 2024-08-22 through 2026-08-22."
    }

    if ([string]$row.venue_tier -notin $allowedTiers) {
        Add-AuditError "[$id] Unknown venue_tier '$($row.venue_tier)'."
    }
    if ([string]$row.journal -eq 'Cell Systems') {
        Add-AuditError "[$id] Cell Systems is ineligible under the frozen current-JIF>=10 rule."
    }
    elseif ([string]$row.journal -like 'Nature*' -and
        [string]$row.journal_metric_note -notmatch 'https://www\.nature\.com/nature-portfolio/about-journals/journal-metrics') {
        Add-AuditError "[$id] Nature Portfolio metric note lacks the official metrics source."
    }
    if ([string]$row.journal -eq 'Nature Communications' -and [string]$row.journal_metric_note -notmatch '(?i)2025 JIF 18\.1') {
        Add-AuditError "[$id] Nature Communications row lacks the current official 2025 JIF 18.1 evidence."
    }
    if ([string]$row.journal -eq 'Nature Methods' -and [string]$row.journal_metric_note -notmatch '(?i)2025 JIF 28\.3') {
        Add-AuditError "[$id] Nature Methods row lacks the current official 2025 JIF 28.3 evidence."
    }
    if ([string]$row.primary_stratum -notin $allowedStrata) {
        Add-AuditError "[$id] Unknown primary_stratum '$($row.primary_stratum)'."
    }
    if ([string]$row.request_class -notin $allowedRequestClasses) {
        Add-AuditError "[$id] Unknown request_class '$($row.request_class)'."
    }
    if ([string]$row.closure_status -notin $allowedClosureStates) {
        Add-AuditError "[$id] Unknown closure_status '$($row.closure_status)'."
    }
    if ([string]$row.access_status -ne 'VERIFIED_TEXT') {
        Add-AuditError "[$id] access_status must be VERIFIED_TEXT."
    }
    if ([string]$row.post_publication_status -notmatch '^(NO_NOTICE_SIGNAL_FOUND|CORRECTION|PUBLISHER_CORRECTION|EDITOR_NOTE|RETRACTION|EXPRESSION_OF_CONCERN) as screened \d{4}-\d{2}-\d{2}:') {
        Add-AuditError "[$id] post_publication_status must contain a dated, allowed one-time screen result."
    }

    if ([string]$row.review_file_sha256 -notmatch '^[A-Fa-f0-9]{64}$') {
        Add-AuditError "[$id] review_file_sha256 is not a 64-character digest."
    }
    $pages = 0
    if (-not [int]::TryParse([string]$row.review_pages, [ref]$pages) -or $pages -lt 2) {
        Add-AuditError "[$id] review_pages must be an integer >=2."
    }
    $chars = 0
    if (-not [int]::TryParse([string]$row.review_text_chars, [ref]$chars) -or $chars -lt 1000) {
        Add-AuditError "[$id] review_text_chars must be an integer >=1000."
    }
    $reviewRounds = 0
    if ((-not [int]::TryParse([string]$row.review_rounds, [ref]$reviewRounds) -or $reviewRounds -lt 1) -and
        [string]$row.review_rounds -notmatch '^NR[-:]') {
        Add-AuditError "[$id] review_rounds must be an integer >=1 or an explicit NR-reason."
    }
    $reviewerCount = 0
    if (-not [int]::TryParse([string]$row.reviewer_count, [ref]$reviewerCount) -or $reviewerCount -lt 1) {
        Add-AuditError "[$id] reviewer_count must be an integer >=1."
    }

    $articleHost = Get-UriHost -Value ([string]$row.article_url)
    $reviewHost = Get-UriHost -Value ([string]$row.review_file_url)
    if ($articleHost -notin $allowedArticleHosts) {
        Add-AuditError "[$id] Article URL is not on an allowed official publisher host: '$articleHost'."
    }
    if ($reviewHost -notin $allowedReviewHosts) {
        Add-AuditError "[$id] Review URL is not on an allowed official publisher/CDN host: '$reviewHost'."
    }
    if ([string]$row.article_url -notmatch '^https://') {
        Add-AuditError "[$id] article_url must use HTTPS."
    }
    if ([string]$row.review_file_url -notmatch '^https://') {
        Add-AuditError "[$id] review_file_url must use HTTPS."
    }

    if ([string]$row.review_locator -notmatch '(?i)(p\.?\s*\d+|page\s*\d+)') {
        Add-AuditError "[$id] review_locator lacks a page locator."
    }
    if ([string]$row.response_locator -notmatch '(?i)(p\.?\s*\d+|page\s*\d+)') {
        Add-AuditError "[$id] response_locator lacks a page locator."
    }
    foreach ($locatorField in @('review_locator', 'response_locator')) {
        foreach ($match in [regex]::Matches([string]$row.$locatorField, '(?i)(?:p\.?|page)\s*(\d+)')) {
            $locatorPage = [int]$match.Groups[1].Value
            if ($locatorPage -lt 1 -or $locatorPage -gt $pages) {
                Add-AuditError "[$id] $locatorField page $locatorPage is outside the 1-$pages review-file range."
            }
        }
    }
    if ([string]$row.concern_codes -notmatch '^[A-Z0-9_]+(?:;[A-Z0-9_]+)*$') {
        Add-AuditError "[$id] concern_codes must be semicolon-separated uppercase codes."
    }
    if ([string]$row.concern_ontology_version -cne $ontologyVersion) {
        Add-AuditError "[$id] concern_ontology_version must equal '$ontologyVersion'."
    }
    if ([string]$row.canonical_concern_families -notmatch '^[A-Z0-9_]+(?:;[A-Z0-9_]+)*$') {
        Add-AuditError "[$id] canonical_concern_families must be semicolon-separated uppercase codes."
    }
    $expectedFamilies = [System.Collections.Generic.List[string]]::new()
    foreach ($rawCode in @(([string]$row.concern_codes) -split ';')) {
        if (-not $ontologyMap.ContainsKey($rawCode)) {
            Add-AuditError "[$id] Raw concern code '$rawCode' is absent from ontology $ontologyVersion."
            continue
        }
        $family = [string]$ontologyMap[$rawCode]
        if (-not $expectedFamilies.Contains($family)) { $expectedFamilies.Add($family) }
    }
    $actualFamilies = @(([string]$row.canonical_concern_families) -split ';')
    if (($expectedFamilies -join ';') -cne ($actualFamilies -join ';')) {
        Add-AuditError "[$id] canonical_concern_families do not match the versioned ontology mapping."
    }
    if ($expectedFamilies.Count -gt 0) {
        $decisiveFamily = [string]$expectedFamilies[0]
        if (-not $familyCriterionPatterns.ContainsKey($decisiveFamily) -or
            [string]$row.governing_criterion -notmatch $familyCriterionPatterns[$decisiveFamily]) {
            Add-AuditError "[$id] governing_criterion is not aligned with decisive canonical family '$decisiveFamily'."
        }
    }
    foreach ($narrativeField in @('decisive_concern', 'author_action', 'minimum_repair', 'closure_evidence', 'portable_skill_rule')) {
        if ([string]$row.$narrativeField -notmatch '[.!?]["'']?$') {
            Add-AuditError "[$id] $narrativeField appears truncated or is not a complete paraphrased sentence."
        }
    }
    foreach ($responseField in @('author_action', 'closure_evidence')) {
        if ([string]$row.$responseField -match '(?i)\b(thanks? for|thank you|we are grateful|we appreciate(?: the reviewer)?)\b') {
            Add-AuditError "[$id] $responseField contains courtesy boilerplate suggesting an un-paraphrased response excerpt."
        }
    }

    if ($VerifyRemote) {
        try {
            $response = Invoke-WebRequest -Uri ([string]$row.review_file_url) -Method Get -Headers @{ Range = 'bytes=0-4' } -TimeoutSec 30 -MaximumRedirection 5
            $bytes = $response.Content
            if ($bytes -is [string]) {
                $prefix = $bytes.Substring(0, [Math]::Min(4, $bytes.Length))
                if ($prefix -notmatch '%PDF') {
                    Add-AuditError "[$id] Remote review file did not return a PDF prefix."
                }
            }
        }
        catch {
            Add-AuditError "[$id] Remote review-file verification failed: $($_.Exception.Message)"
        }
    }
}

foreach ($field in @('record_id', 'doi')) {
    foreach ($duplicate in @($rows | Group-Object { ([string]$_.$field).Trim().ToLowerInvariant() } | Where-Object Count -gt 1)) {
        Add-AuditError "Duplicate ${field}: '$($duplicate.Name)'."
    }
}

$strata = @($rows | Group-Object primary_stratum)
foreach ($stratum in $allowedStrata) {
    $matchingGroups = @($strata | Where-Object Name -eq $stratum)
    $count = if ($matchingGroups.Count -eq 0) { 0 } else { [int]$matchingGroups[0].Count }
    if ($count -eq 0) {
        Add-AuditError "Primary stratum '$stratum' is absent."
    }
    elseif ($count -gt 35) {
        Add-AuditError "Primary stratum '$stratum' exceeds the 35-paper cap ($count)."
    }
}

$natureCommunicationsCount = @($rows | Where-Object journal -eq 'Nature Communications').Count
if ($natureCommunicationsCount -gt 50) {
    Add-AuditError "Nature Communications exceeds the 50-paper cap ($natureCommunicationsCount)."
}
$tier12Count = @($rows | Where-Object venue_tier -in @('1-main-journal', '2-major-specialist')).Count
if ($tier12Count -lt 25) {
    Add-AuditError "Only $tier12Count papers are in venue tiers 1-2; at least 25 are required."
}
$cellSystemsCount = @($rows | Where-Object journal -eq 'Cell Systems').Count
if ($cellSystemsCount -ne 0) {
    Add-AuditError "Strict current-JIF corpus must contain zero Cell Systems records; found $cellSystemsCount."
}

$knownEditorNote = @($rows | Where-Object doi -eq '10.1038/s41588-025-02253-8')
if ($knownEditorNote.Count -ne 1 -or [string]$knownEditorNote[0].post_publication_status -notmatch '^EDITOR_NOTE ') {
    Add-AuditError 'Known Editor Note for DOI 10.1038/s41588-025-02253-8 is missing or misclassified.'
}

$strictReplacementContracts = @{
    'TPR095' = @{ doi = '10.1038/s41467-025-55847-5'; journal = 'Nature Communications'; sha256 = 'fb2d9fba337b02cf2399b9de584816481648891e67883daea0d7cb8cd7d1b4a1' }
    'TPR096' = @{ doi = '10.1038/s41467-025-56623-1'; journal = 'Nature Communications'; sha256 = '7ca5a951c5c1f40ca1dd8a18a954b8d928cd51b519eb54ad8a442ec55913f035' }
    'TPR097' = @{ doi = '10.1038/s41592-025-02624-3'; journal = 'Nature Methods'; sha256 = '360ea65af480a5d10cb56ee9f06297cef7088a8a5a871d6c1226804b6e92f9da' }
    'TPR098' = @{ doi = '10.1038/s41592-024-02415-2'; journal = 'Nature Methods'; sha256 = 'f9b42b7a7712c63bca86aaf0014eb3a2f3318893b4531cbfbb28794e8d6c9d9f' }
    'TPR099' = @{ doi = '10.1038/s41467-024-50904-x'; journal = 'Nature Communications'; sha256 = '59631387ceff2eb343d80068d37816aa23b93cdbe1ed7923fea6348bbb720ce6' }
    'TPR100' = @{ doi = '10.1038/s41467-025-61149-7'; journal = 'Nature Communications'; sha256 = '61070bebee8e1d49b3a161d4ed5bc5a890a86464bea7ea1b6350be2ba801a7ae' }
}
foreach ($recordId in $strictReplacementContracts.Keys) {
    $record = @($rows | Where-Object record_id -eq $recordId)
    $expected = $strictReplacementContracts[$recordId]
    if ($record.Count -ne 1 -or
        [string]$record[0].doi -cne [string]$expected.doi -or
        [string]$record[0].journal -cne [string]$expected.journal -or
        [string]$record[0].review_file_sha256 -cne [string]$expected.sha256) {
        Add-AuditError "Strict replacement regression for $recordId."
    }
}
$locatorContracts = @{
    'TPR021' = '(?i)pp\.4-5'
    'TPR097' = '(?i)pp\.21-22'
    'TPR099' = '(?i)pp\.6-20,60-64'
}
foreach ($recordId in $locatorContracts.Keys) {
    $record = @($rows | Where-Object record_id -eq $recordId)
    if ($record.Count -ne 1 -or [string]$record[0].response_locator -notmatch $locatorContracts[$recordId]) {
        Add-AuditError "Known response-locator regression for $recordId."
    }
}

# Keep the compact teaching reference synchronized with the canonical row-level evidence map.
# This catches a common failure mode: scientifically corrected source rows paired with stale prose counts.
if (-not (Test-Path -LiteralPath $LessonsPath -PathType Leaf)) {
    Add-AuditError "Transparent-review lessons file is missing: $LessonsPath"
}
else {
    $lessons = Get-Content -LiteralPath $LessonsPath -Raw
    $familyCounts = @{}
    foreach ($family in @($rows | ForEach-Object { ([string]$_.canonical_concern_families) -split ';' })) {
        if (-not $familyCounts.ContainsKey($family)) { $familyCounts[$family] = 0 }
        $familyCounts[$family]++
    }
    $ontologyFamilies = @($ontologyRows.canonical_concern_family | Sort-Object -Unique)
    foreach ($family in $ontologyFamilies) {
        $count = if ($familyCounts.ContainsKey($family)) { [int]$familyCounts[$family] } else { 0 }
        $pattern = ('(?m)^\|\s*{0}\s*\|\s*{1}\s*\|' -f [regex]::Escape([string]$family), $count)
        if ($lessons -notmatch $pattern) {
            Add-AuditError "Transparent-review lessons have a stale or missing canonical-family count for $family (expected $count)."
        }
    }
    if ($lessons -notmatch ([regex]::Escape("ontology v$ontologyVersion"))) {
        Add-AuditError "Transparent-review lessons do not declare the current concern ontology version '$ontologyVersion'."
    }

    $requestCounts = @{}
    foreach ($group in @($rows | Group-Object request_class)) { $requestCounts[$group.Name] = [int]$group.Count }
    foreach ($requestClass in $allowedRequestClasses) {
        if (-not $requestCounts.ContainsKey($requestClass)) { $requestCounts[$requestClass] = 0 }
    }
    $requestPattern = ('one decisive request class per paper:\s*{0}\s+manuscript-grounded defects,\s*{1}\s+clarification-needed items,\s*{2}\s+reviewer preferences,\s*{3}\s+optional strengthening requests and\s*{4}\s+scope-contested/infeasible request' -f
        $requestCounts['manuscript-grounded-defect'],
        $requestCounts['clarification-needed'],
        $requestCounts['reviewer-preference'],
        $requestCounts['optional-strengthening'],
        $requestCounts['scope-contested-or-infeasible'])
    if ($lessons -notmatch $requestPattern) {
        Add-AuditError 'Transparent-review lessons have stale request-class counts.'
    }

    $closureCounts = @{}
    foreach ($group in @($rows | Group-Object closure_status)) { $closureCounts[$group.Name] = [int]$group.Count }
    $closurePattern = ('The coded closure states are:\s*{0} experiment-or-analysis added,\s*{1} analysis-or-evidence added,\s*{2} text-or-claim revised,\s*{3} author-response documented,\s*{4} partially addressed,\s*{5} reviewer confirmed,\s*{6} evidence-based pushback\s*and {7} declined with an explicit boundary\.' -f
        $closureCounts['experiment-or-analysis-added'],
        $closureCounts['analysis-or-evidence-added'],
        $closureCounts['text-or-claim-revised'],
        $closureCounts['author-response-documented'],
        $closureCounts['partially-addressed'],
        $closureCounts['reviewer-confirmed'],
        $closureCounts['evidence-based-pushback'],
        $closureCounts['declined-with-explicit-boundary'])
    if ($lessons -notmatch $closurePattern) {
        Add-AuditError 'Transparent-review lessons have stale closure-state counts.'
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
    $strategyPattern = ('yields\s+{0}\s+accept-and-repair,\s*{1}\s+clarify/rewrite,\s*{2}\s+partially accept and\s*{3}\s+evidence-based contest/infeasibility' -f
        $strategyCounts.A, $strategyCounts.B, $strategyCounts.C, $strategyCounts.D)
    if ($lessons -notmatch $strategyPattern) {
        Add-AuditError 'Transparent-review lessons have stale dominant-response-architecture counts.'
    }
}

Write-Output "Transparent peer-review corpus rows: $($rows.Count)"
Write-Output "Venue tiers 1-2: $tier12Count; Nature Communications: $natureCommunicationsCount; current-JIF-ineligible Cell Systems: $cellSystemsCount"
Write-Output 'Post-publication screen:'
$rows | ForEach-Object { ([string]$_.post_publication_status -split ' ')[0] } |
    Group-Object | Sort-Object Name | ForEach-Object { Write-Output ("- {0}: {1}" -f $_.Name, $_.Count) }
Write-Output 'Primary strata:'
$strata | Sort-Object Name | ForEach-Object { Write-Output ("- {0}: {1}" -f $_.Name, $_.Count) }

if ($errors.Count -gt 0) {
    Write-Output 'Transparent peer-review corpus audit: FAIL'
    $errors | ForEach-Object { Write-Output "- $_" }
    exit 1
}

Write-Output 'Transparent peer-review corpus audit: PASS'
exit 0
