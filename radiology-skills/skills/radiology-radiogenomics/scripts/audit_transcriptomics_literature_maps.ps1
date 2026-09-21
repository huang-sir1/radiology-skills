param(
    [switch]$VerifyPubMed
)

$ErrorActionPreference = 'Stop'
$referenceRoot = Join-Path (Split-Path -Parent $PSScriptRoot) 'references'
$windowStart = [datetime]'2024-08-21'
$windowEnd = [datetime]'2026-08-21'
$requiredColumns = @(
    'id', 'modality', 'theme', 'title', 'publication_date', 'journal', 'doi', 'pmid',
    'evidence_type', 'concrete_content', 'decision_changed', 'constraints', 'skill_action',
    'writing_requirement', 'jif_value', 'jif_year', 'jif_source'
)
$mapSpecs = @(
    @{ File = 'bulk-rna-literature-map-2024-2026.tsv'; Expected = 33; Guide = 'bulk-rna-research-guidance.md'; Prefix = 'BK' },
    @{ File = 'single-cell-literature-map-2024-2026.tsv'; Expected = 34; Guide = 'single-cell-research-guidance.md'; Prefix = 'SC' },
    @{ File = 'spatial-transcriptomics-literature-map-2024-2026.tsv'; Expected = 33; Guide = 'spatial-transcriptomics-research-guidance.md'; Prefix = 'ST' }
)

$auditErrors = [System.Collections.Generic.List[string]]::new()
$allRows = [System.Collections.Generic.List[object]]::new()

foreach ($spec in $mapSpecs) {
    $mapPath = Join-Path $referenceRoot $spec.File
    if (-not (Test-Path -LiteralPath $mapPath -PathType Leaf)) {
        $auditErrors.Add("Missing map: $($spec.File)")
        continue
    }

    $rows = @(Import-Csv -LiteralPath $mapPath -Delimiter "`t")
    if ($rows.Count -ne $spec.Expected) {
        $auditErrors.Add("$($spec.File): expected $($spec.Expected) rows, found $($rows.Count)")
    }
    if ($rows.Count -eq 0) {
        continue
    }

    $actualColumns = @($rows[0].PSObject.Properties.Name)
    foreach ($column in $requiredColumns) {
        if ($column -notin $actualColumns) {
            $auditErrors.Add("$($spec.File): missing column '$column'")
        }
    }

    foreach ($row in $rows) {
        foreach ($column in $requiredColumns) {
            if ($column -in $actualColumns -and [string]::IsNullOrWhiteSpace([string]$row.$column)) {
                $auditErrors.Add("$($spec.File) [$($row.id)]: empty '$column'")
            }
        }

        $publicationDate = [datetime]::MinValue
        if (-not [datetime]::TryParseExact(
            [string]$row.publication_date,
            'yyyy-MM-dd',
            [Globalization.CultureInfo]::InvariantCulture,
            [Globalization.DateTimeStyles]::None,
            [ref]$publicationDate
        )) {
            $auditErrors.Add("$($spec.File) [$($row.id)]: invalid publication_date")
        }
        elseif ($publicationDate -lt $windowStart -or $publicationDate -gt $windowEnd) {
            $auditErrors.Add("$($spec.File) [$($row.id)]: publication date outside the accepted window")
        }

        $jifValue = 0.0
        if (-not [double]::TryParse(
            [string]$row.jif_value,
            [Globalization.NumberStyles]::Float,
            [Globalization.CultureInfo]::InvariantCulture,
            [ref]$jifValue
        )) {
            $auditErrors.Add("$($spec.File) [$($row.id)]: invalid jif_value")
        }
        elseif ($jifValue -lt 10.0) {
            $auditErrors.Add("$($spec.File) [$($row.id)]: jif_value below 10")
        }

        if ([string]$row.pmid -notmatch '^\d+$') {
            $auditErrors.Add("$($spec.File) [$($row.id)]: PMID is not numeric")
        }
        if ([string]$row.doi -notmatch '^10\.[0-9]{4,9}/\S+$') {
            $auditErrors.Add("$($spec.File) [$($row.id)]: DOI format is invalid")
        }
        if ([string]$row.jif_source -notmatch '^https://') {
            $auditErrors.Add("$($spec.File) [$($row.id)]: jif_source must be an HTTPS URL")
        }

        $allRows.Add($row)
    }

    $guidePath = Join-Path $referenceRoot $spec.Guide
    if (-not (Test-Path -LiteralPath $guidePath -PathType Leaf)) {
        $auditErrors.Add("Missing guide: $($spec.Guide)")
    }
    else {
        $guideText = Get-Content -LiteralPath $guidePath -Raw
        $guideIds = [System.Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
        $idPattern = "\b$($spec.Prefix)\d{2}R?\b"
        foreach ($match in [regex]::Matches($guideText, $idPattern)) {
            [void]$guideIds.Add($match.Value)
        }

        $rangePattern = "\b$($spec.Prefix)(\d{2})\s*[–-]\s*$($spec.Prefix)(\d{2})\b"
        foreach ($match in [regex]::Matches($guideText, $rangePattern)) {
            $rangeStart = [int]$match.Groups[1].Value
            $rangeEnd = [int]$match.Groups[2].Value
            if ($rangeEnd -ge $rangeStart) {
                foreach ($number in $rangeStart..$rangeEnd) {
                    [void]$guideIds.Add(("{0}{1:D2}" -f $spec.Prefix, $number))
                }
            }
        }

        foreach ($row in $rows) {
            if (-not $guideIds.Contains([string]$row.id)) {
                $auditErrors.Add("$($spec.Guide): evidence row $($row.id) is not used by the playbook")
            }
        }
        foreach ($guideId in $guideIds) {
            if ($guideId -notin @($rows.id)) {
                $auditErrors.Add("$($spec.Guide): cited evidence ID $guideId is absent from its map")
            }
        }
    }

    Write-Output ("{0}: {1}/{2} rows" -f $spec.File, $rows.Count, $spec.Expected)
}

if ($allRows.Count -ne 100) {
    $auditErrors.Add("Combined corpus: expected 100 rows, found $($allRows.Count)")
}

foreach ($field in @('id', 'doi', 'pmid')) {
    $duplicates = @(
        $allRows |
            Group-Object { ([string]$_.$field).Trim().ToLowerInvariant() } |
            Where-Object { $_.Count -gt 1 }
    )
    foreach ($duplicate in $duplicates) {
        $auditErrors.Add("Duplicate ${field}: $($duplicate.Name)")
    }
}

if ($VerifyPubMed -and $allRows.Count -gt 0) {
    $pmids = @($allRows | ForEach-Object { [string]$_.pmid } | Sort-Object -Unique)
    $body = @{ db = 'pubmed'; id = ($pmids -join ','); retmode = 'json' }
    $response = Invoke-RestMethod -Method Post -Uri 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi' -Body $body
    $resolved = @($response.result.uids)
    foreach ($row in $allRows) {
        $pmid = [string]$row.pmid
        if ($pmid -notin $resolved) {
            $auditErrors.Add("PubMed did not resolve PMID $pmid")
            continue
        }

        $summary = $response.result.PSObject.Properties[$pmid].Value
        $pubMedDois = @(
            $summary.articleids |
                Where-Object { $_.idtype -eq 'doi' } |
                ForEach-Object { ([string]$_.value).Trim().ToLowerInvariant() }
        )
        $expectedDoi = ([string]$row.doi).Trim().ToLowerInvariant()
        if ($expectedDoi -notin $pubMedDois) {
            $auditErrors.Add("PMID $pmid does not resolve to DOI $expectedDoi")
        }
    }
    Write-Output ("PubMed resolved: {0}/{1}" -f $resolved.Count, $pmids.Count)
}

if ($auditErrors.Count -gt 0) {
    Write-Output 'Transcriptomics literature-map audit: FAIL'
    $auditErrors | ForEach-Object { Write-Output "- $_" }
    exit 1
}

Write-Output 'Transcriptomics literature-map audit: PASS'
Write-Output ("Combined unique corpus: {0}" -f $allRows.Count)
