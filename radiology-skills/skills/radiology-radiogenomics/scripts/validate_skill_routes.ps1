#requires -Version 7.0

[CmdletBinding()]
param(
    [Parameter()]
    [string]$SkillRoot = (Split-Path -Parent $PSScriptRoot),

    [Parameter()]
    [string]$ManifestPath,

    [Parameter()]
    [string]$CasesPath,

    [Parameter()]
    [switch]$VerifyLiterature
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:Failures = [System.Collections.Generic.List[string]]::new()
$script:Warnings = [System.Collections.Generic.List[string]]::new()
$script:SkillRootFull = [IO.Path]::GetFullPath($SkillRoot).TrimEnd(
    [IO.Path]::DirectorySeparatorChar,
    [IO.Path]::AltDirectorySeparatorChar
)

if ([string]::IsNullOrWhiteSpace($ManifestPath)) {
    $ManifestPath = Join-Path $script:SkillRootFull 'manifest.yaml'
}
if ([string]::IsNullOrWhiteSpace($CasesPath)) {
    $CasesPath = Join-Path $script:SkillRootFull 'tests/routing-cases.json'
}

function Add-Failure {
    param([Parameter(Mandatory)][string]$Message)
    $script:Failures.Add($Message)
}

function Add-ValidationWarning {
    param([Parameter(Mandatory)][string]$Message)
    $script:Warnings.Add($Message)
}

function Read-JsonDocument {
    param(
        [Parameter(Mandatory)][string]$Path,
        [Parameter(Mandatory)][string]$Label
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        Add-Failure "$Label is missing: $Path"
        return $null
    }

    try {
        return Get-Content -Raw -LiteralPath $Path | ConvertFrom-Json -Depth 100
    }
    catch {
        Add-Failure "$Label is not valid JSON-subset YAML/JSON: $Path :: $($_.Exception.Message)"
        return $null
    }
}

function Test-IsSequence {
    param([AllowNull()]$Value)
    return $null -ne $Value -and
        $Value -isnot [string] -and
        $Value -is [System.Collections.IEnumerable]
}

function Get-ScalarValues {
    param([AllowNull()]$Value)

    if ($null -eq $Value) {
        return @()
    }
    if ($Value -is [string]) {
        return @($Value)
    }
    if (Test-IsSequence $Value) {
        $items = [System.Collections.Generic.List[string]]::new()
        foreach ($item in $Value) {
            if ($null -ne $item) {
                $items.Add([string]$item)
            }
        }
        return @($items)
    }
    return @([string]$Value)
}

function Get-CheckedStringArray {
    param(
        [Parameter(Mandatory)][string]$Owner,
        [AllowNull()]$Value,
        [switch]$Required
    )

    if ($null -eq $Value) {
        if ($Required) {
            Add-Failure "$Owner must be present and must be an array of strings."
        }
        return @()
    }
    if ($Value -is [string] -or -not (Test-IsSequence $Value)) {
        Add-Failure "$Owner must be an array, even when it has one value."
        return @(Get-ScalarValues $Value)
    }

    $result = [System.Collections.Generic.List[string]]::new()
    foreach ($item in $Value) {
        if ($item -isnot [string] -or [string]::IsNullOrWhiteSpace([string]$item)) {
            Add-Failure "$Owner contains a value that is not a non-empty string."
            continue
        }
        $result.Add(([string]$item).Trim())
    }
    return @($result)
}

function Test-AxisAssignment {
    param(
        [Parameter(Mandatory)][string]$AxisName,
        [Parameter(Mandatory)]$AxisDefinition,
        [AllowNull()]$Value,
        [Parameter(Mandatory)][string]$Context,
        [switch]$EnforceShape
    )

    $valuesProperty = $AxisDefinition.PSObject.Properties['values']
    if ($null -eq $valuesProperty) {
        Add-Failure "Axis '$AxisName' is missing a values array."
        return
    }
    $allowedValues = @(Get-ScalarValues $valuesProperty.Value)
    if ($allowedValues.Count -eq 0) {
        Add-Failure "Axis '$AxisName' has no allowed values."
        return
    }

    $multiProperty = $AxisDefinition.PSObject.Properties['multi']
    $isMulti = $null -ne $multiProperty -and [bool]$multiProperty.Value
    $allowScalarProperty = $AxisDefinition.PSObject.Properties['allow_scalar']
    $allowScalar = $null -ne $allowScalarProperty -and [bool]$allowScalarProperty.Value
    if ($EnforceShape) {
        if ($isMulti -and -not $allowScalar -and $null -ne $Value -and -not (Test-IsSequence $Value)) {
            Add-Failure "$Context axis '$AxisName' must be an array."
        }
        if (-not $isMulti -and (Test-IsSequence $Value)) {
            Add-Failure "$Context axis '$AxisName' must be a scalar."
        }
    }

    foreach ($assignedValue in @(Get-ScalarValues $Value)) {
        if ([string]::IsNullOrWhiteSpace($assignedValue)) {
            Add-Failure "$Context axis '$AxisName' contains an empty value."
            continue
        }
        $known = @($allowedValues | Where-Object {
                [string]::Equals($_, $assignedValue, [StringComparison]::OrdinalIgnoreCase)
            }).Count -gt 0
        if (-not $known) {
            Add-Failure "$Context axis '$AxisName' uses undeclared value '$assignedValue'."
        }
    }
}

function ConvertTo-CanonicalSkillPath {
    param(
        [Parameter(Mandatory)][string]$RelativePath,
        [Parameter(Mandatory)][string]$Context,
        [switch]$CheckExists
    )

    $candidate = $RelativePath.Trim()
    if ([string]::IsNullOrWhiteSpace($candidate)) {
        Add-Failure "$Context contains an empty path."
        return $null
    }
    if ([IO.Path]::IsPathRooted($candidate) -or $candidate -match '^[A-Za-z][A-Za-z0-9+.-]*:') {
        Add-Failure "$Context must use a relative skill path, found '$candidate'."
        return $null
    }

    try {
        $fullPath = [IO.Path]::GetFullPath((Join-Path $script:SkillRootFull $candidate))
    }
    catch {
        Add-Failure "$Context has an invalid path '$candidate': $($_.Exception.Message)"
        return $null
    }

    $rootPrefix = $script:SkillRootFull + [IO.Path]::DirectorySeparatorChar
    $insideRoot = $fullPath.StartsWith($rootPrefix, [StringComparison]::OrdinalIgnoreCase)
    if (-not $insideRoot) {
        Add-Failure "$Context escapes the skill root: '$candidate'."
        return $null
    }
    if ($CheckExists -and -not (Test-Path -LiteralPath $fullPath -PathType Leaf)) {
        Add-Failure "$Context points to a missing file: '$candidate'."
    }

    return ([IO.Path]::GetRelativePath($script:SkillRootFull, $fullPath) -replace '\\', '/')
}

function Get-StringLeaves {
    param([AllowNull()]$Value)

    if ($null -eq $Value) {
        return
    }
    if ($Value -is [string]) {
        Write-Output $Value
        return
    }
    if (Test-IsSequence $Value) {
        foreach ($item in $Value) {
            Get-StringLeaves $item
        }
        return
    }

    $properties = @($Value.PSObject.Properties)
    foreach ($property in $properties) {
        Get-StringLeaves $property.Value
    }
}

function Test-ConditionValue {
    param(
        [AllowNull()]$Actual,
        [AllowNull()]$Expected
    )

    $actualValues = @(Get-ScalarValues $Actual)
    $expectedValues = @(Get-ScalarValues $Expected)
    if ($actualValues.Count -eq 0 -or $expectedValues.Count -eq 0) {
        return $false
    }
    if ($expectedValues -contains '*') {
        return $true
    }

    foreach ($actualValue in $actualValues) {
        foreach ($expectedValue in $expectedValues) {
            if ([string]::Equals(
                    $actualValue.Trim(),
                    $expectedValue.Trim(),
                    [StringComparison]::OrdinalIgnoreCase
                )) {
                return $true
            }
        }
    }
    return $false
}

function Test-RuleMatches {
    param(
        [Parameter(Mandatory)]$Rule,
        [Parameter(Mandatory)]$Axes
    )

    $conditions = @($Rule.when.PSObject.Properties)
    foreach ($condition in $conditions) {
        $actualProperty = $Axes.PSObject.Properties[$condition.Name]
        if ($null -eq $actualProperty) {
            return $false
        }
        if (-not (Test-ConditionValue -Actual $actualProperty.Value -Expected $condition.Value)) {
            return $false
        }
    }
    return $true
}

function Get-AxisCompatibilityIssues {
    param([Parameter(Mandatory)]$Axes)

    $issues = [System.Collections.Generic.List[string]]::new()
    $taskValues = @(Get-ScalarValues $Axes.PSObject.Properties['task'].Value)
    $task = if ($taskValues.Count -gt 0) { $taskValues[0] } else { '' }
    $scopeValues = @(Get-ScalarValues $Axes.PSObject.Properties['study_scope'].Value)
    $scope = if ($scopeValues.Count -gt 0) { $scopeValues[0] } else { '' }
    $writingProperty = $Axes.PSObject.Properties['writing_job']
    $writingJobs = @(if ($null -ne $writingProperty) { Get-ScalarValues $writingProperty.Value })
    $sectionProperty = $Axes.PSObject.Properties['manuscript_section']
    $sections = @(if ($null -ne $sectionProperty) { Get-ScalarValues $sectionProperty.Value })
    $submissionProperty = $Axes.PSObject.Properties['submission_phase']
    $submissionPhases = @(if ($null -ne $submissionProperty) { Get-ScalarValues $submissionProperty.Value })

    if ($task -eq 'writing-revision') {
        if ($writingJobs.Count -eq 0 -or $writingJobs -contains 'not-applicable') {
            $issues.Add('writing-revision requires a concrete writing_job.')
        }
        if ($sections.Count -eq 0 -or $sections -contains 'not-applicable') {
            $issues.Add('writing-revision requires at least one concrete manuscript_section.')
        }
    }
    elseif (@($writingJobs | Where-Object { $_ -ne 'not-applicable' }).Count -gt 0) {
        $issues.Add("task '$task' cannot carry an active writing_job.")
    }

    if ($task -eq 'submission-rebuttal') {
        if ($submissionPhases.Count -ne 1 -or $submissionPhases[0] -notin @('initial', 'post-decision')) {
            $issues.Add('deprecated submission-rebuttal alias requires exactly one phase: initial or post-decision.')
        }
    }
    elseif ($task -eq 'initial-submission-package') {
        if ($submissionPhases.Count -ne 1 -or $submissionPhases[0] -ne 'initial') {
            $issues.Add('initial-submission-package requires submission_phase=initial.')
        }
    }
    elseif ($task -eq 'post-decision-adjudication') {
        if ($submissionPhases.Count -ne 1 -or $submissionPhases[0] -ne 'post-decision') {
            $issues.Add('post-decision-adjudication requires submission_phase=post-decision.')
        }
    }
    elseif (@($submissionPhases | Where-Object { $_ -ne 'not-applicable' }).Count -gt 0) {
        $issues.Add("task '$task' cannot carry an active submission_phase.")
    }

    $activeProperty = $Axes.PSObject.Properties['active_modalities']
    $active = @(if ($null -ne $activeProperty) { Get-ScalarValues $activeProperty.Value })
    $molecularModalities = @('bulk-rna', 'single-cell', 'spatial', 'pathology', 'multi-omics', 'other-omics', 'perturbation')
    if ($scope -eq 'imaging-only') {
        $forbidden = @($active | Where-Object { $_ -in ($molecularModalities + @('deep-fusion')) })
        if ($forbidden.Count -gt 0) {
            $issues.Add("imaging-only contains an active biological or cross-modal fusion object: $($forbidden -join ', ').")
        }
    }
    elseif ($scope -eq 'mechanism-only') {
        $forbidden = @($active | Where-Object { $_ -in @('radiomics', 'deep-fusion') })
        if ($forbidden.Count -gt 0) {
            $issues.Add("mechanism-only contains active imaging/fusion modality: $($forbidden -join ', ').")
        }
    }
    elseif ($scope -eq 'imaging-mechanism') {
        $roleModalities = [System.Collections.Generic.List[string]]::new()
        foreach ($roleAxis in @('active_modalities', 'external_reference_modalities', 'generated_or_predicted_modalities', 'proposed_validation_modalities')) {
            $roleProperty = $Axes.PSObject.Properties[$roleAxis]
            if ($null -ne $roleProperty) {
                foreach ($item in @(Get-ScalarValues $roleProperty.Value)) {
                    $roleModalities.Add($item)
                }
            }
        }
        $hasImaging = @($active | Where-Object { $_ -in @('radiomics', 'deep-fusion') }).Count -gt 0
        $hasBiology = @($roleModalities | Where-Object { $_ -in ($molecularModalities + @('deep-fusion')) }).Count -gt 0
        if (-not $hasImaging) {
            $issues.Add('imaging-mechanism requires an active imaging object.')
        }
        if (-not $hasBiology) {
            $issues.Add('imaging-mechanism requires an active, external, generated, or proposed biological object.')
        }
    }

    return @($issues)
}

function Get-RoutedPaths {
    param(
        [Parameter(Mandatory)]$Manifest,
        [Parameter(Mandatory)]$Axes
    )

    $selected = [System.Collections.Generic.HashSet[string]]::new(
        [StringComparer]::OrdinalIgnoreCase
    )
    $always = [System.Collections.Generic.HashSet[string]]::new(
        [StringComparer]::OrdinalIgnoreCase
    )
    $excluded = [System.Collections.Generic.HashSet[string]]::new(
        [StringComparer]::OrdinalIgnoreCase
    )
    $matchedRuleIds = [System.Collections.Generic.List[string]]::new()

    foreach ($path in @(Get-ScalarValues $Manifest.always_load)) {
        $canonical = ConvertTo-CanonicalSkillPath -RelativePath $path -Context 'manifest.always_load'
        if ($null -ne $canonical) {
            [void]$always.Add($canonical)
            [void]$selected.Add($canonical)
        }
    }

    foreach ($rule in @($Manifest.rules)) {
        if (-not (Test-RuleMatches -Rule $rule -Axes $Axes)) {
            continue
        }

        $ruleId = [string]$rule.id
        $matchedRuleIds.Add($ruleId)
        foreach ($path in @(Get-ScalarValues $rule.load)) {
            $canonical = ConvertTo-CanonicalSkillPath -RelativePath $path -Context "rule '$ruleId' load"
            if ($null -ne $canonical) {
                [void]$selected.Add($canonical)
            }
        }

        if ($null -ne $rule.PSObject.Properties['exclude']) {
            foreach ($path in @(Get-ScalarValues $rule.exclude)) {
                $canonical = ConvertTo-CanonicalSkillPath -RelativePath $path -Context "rule '$ruleId' exclude"
                if ($null -ne $canonical) {
                    [void]$excluded.Add($canonical)
                }
            }
        }
    }

    foreach ($path in $excluded) {
        if ($always.Contains($path)) {
            Add-Failure "A matched rule attempted to exclude always_load path '$path'."
            continue
        }
        [void]$selected.Remove($path)
    }

    return [pscustomobject]@{
        Paths = @($selected | Sort-Object)
        MatchedRules = @($matchedRuleIds)
        Excluded = @($excluded | Sort-Object)
    }
}

function Get-FrontmatterValue {
    param(
        [Parameter(Mandatory)][string[]]$Lines,
        [Parameter(Mandatory)][string]$Key
    )

    for ($index = 0; $index -lt $Lines.Count; $index++) {
        $match = [regex]::Match($Lines[$index], '^' + [regex]::Escape($Key) + ':\s*(?<value>.*)$')
        if (-not $match.Success) {
            continue
        }

        $raw = $match.Groups['value'].Value.Trim()
        if ($raw -in @('>', '>-', '|', '|-')) {
            $parts = [System.Collections.Generic.List[string]]::new()
            for ($next = $index + 1; $next -lt $Lines.Count; $next++) {
                if ($Lines[$next] -match '^\S') {
                    break
                }
                $trimmed = $Lines[$next].Trim()
                if (-not [string]::IsNullOrWhiteSpace($trimmed)) {
                    $parts.Add($trimmed)
                }
            }
            return ($parts -join ' ')
        }

        if ($raw.Length -ge 2) {
            $first = $raw.Substring(0, 1)
            $last = $raw.Substring($raw.Length - 1, 1)
            if (($first -eq '"' -and $last -eq '"') -or ($first -eq "'" -and $last -eq "'")) {
                return $raw.Substring(1, $raw.Length - 2)
            }
        }
        return $raw
    }
    return $null
}

function Get-QuotedYamlValue {
    param(
        [Parameter(Mandatory)][string]$Text,
        [Parameter(Mandatory)][string]$Key,
        [Parameter(Mandatory)][string]$Context
    )

    $pattern = '(?m)^\s{2}' + [regex]::Escape($Key) + ':\s*(?<value>.+?)\s*$'
    $match = [regex]::Match($Text, $pattern)
    if (-not $match.Success) {
        Add-Failure "$Context is missing interface.$Key."
        return $null
    }

    $raw = $match.Groups['value'].Value.Trim()
    if ($raw.Length -lt 2) {
        Add-Failure "$Context interface.$Key must be a quoted, non-empty string."
        return $null
    }
    $first = $raw.Substring(0, 1)
    $last = $raw.Substring($raw.Length - 1, 1)
    if (($first -ne '"' -or $last -ne '"') -and ($first -ne "'" -or $last -ne "'")) {
        Add-Failure "$Context interface.$Key must be quoted."
        return $null
    }
    return $raw.Substring(1, $raw.Length - 2)
}

function Test-SkillMetadata {
    $skillPath = Join-Path $script:SkillRootFull 'SKILL.md'
    if (-not (Test-Path -LiteralPath $skillPath -PathType Leaf)) {
        Add-Failure "SKILL.md is missing: $skillPath"
        return
    }

    $skillText = Get-Content -Raw -LiteralPath $skillPath
    $frontmatterMatch = [regex]::Match(
        $skillText,
        '\A---\r?\n(?<frontmatter>.*?)\r?\n---(?:\r?\n|\z)',
        [Text.RegularExpressions.RegexOptions]::Singleline
    )
    if (-not $frontmatterMatch.Success) {
        Add-Failure 'SKILL.md must begin with a closed YAML frontmatter block.'
        return
    }

    $frontmatterLines = @($frontmatterMatch.Groups['frontmatter'].Value -split '\r?\n')
    $name = Get-FrontmatterValue -Lines $frontmatterLines -Key 'name'
    $description = Get-FrontmatterValue -Lines $frontmatterLines -Key 'description'
    $expectedName = Split-Path -Leaf $script:SkillRootFull

    if ([string]::IsNullOrWhiteSpace($name)) {
        Add-Failure 'SKILL.md frontmatter is missing name.'
    }
    else {
        if ($name -notmatch '^[a-z0-9-]+$' -or $name.Length -gt 64) {
            Add-Failure "SKILL.md name '$name' must use lowercase letters, digits, and hyphens and be at most 64 characters."
        }
        if ($name -cne $expectedName) {
            Add-Failure "SKILL.md name '$name' does not match folder '$expectedName'."
        }
    }
    if ([string]::IsNullOrWhiteSpace($description)) {
        Add-Failure 'SKILL.md frontmatter is missing a non-empty description.'
    }
    elseif ($description.Length -gt 1024) {
        Add-Failure "SKILL.md description is $($description.Length) characters; maximum is 1024."
    }

    $bodyStart = $frontmatterMatch.Index + $frontmatterMatch.Length
    if ([string]::IsNullOrWhiteSpace($skillText.Substring($bodyStart))) {
        Add-Failure 'SKILL.md has no instruction body after frontmatter.'
    }

    $agentPath = Join-Path $script:SkillRootFull 'agents/openai.yaml'
    if (-not (Test-Path -LiteralPath $agentPath -PathType Leaf)) {
        Add-Failure "agents/openai.yaml is missing: $agentPath"
        return
    }

    $agentText = Get-Content -Raw -LiteralPath $agentPath
    if ($agentText -notmatch '(?m)^interface:\s*$') {
        Add-Failure 'agents/openai.yaml is missing the interface block.'
    }
    $displayName = Get-QuotedYamlValue -Text $agentText -Key 'display_name' -Context 'agents/openai.yaml'
    $shortDescription = Get-QuotedYamlValue -Text $agentText -Key 'short_description' -Context 'agents/openai.yaml'
    $defaultPrompt = Get-QuotedYamlValue -Text $agentText -Key 'default_prompt' -Context 'agents/openai.yaml'

    if ([string]::IsNullOrWhiteSpace($displayName)) {
        Add-Failure 'agents/openai.yaml interface.display_name is empty.'
    }
    if ($null -ne $shortDescription -and ($shortDescription.Length -lt 25 -or $shortDescription.Length -gt 64)) {
        Add-Failure "agents/openai.yaml short_description must be 25-64 characters; found $($shortDescription.Length)."
    }
    if ($null -ne $defaultPrompt -and $null -ne $name) {
        $invocation = '$' + $name
        if ($defaultPrompt.IndexOf($invocation, [StringComparison]::Ordinal) -lt 0) {
            Add-Failure "agents/openai.yaml default_prompt must explicitly mention '$invocation'."
        }
    }

    foreach ($iconKey in @('icon_small', 'icon_large')) {
        $iconMatch = [regex]::Match(
            $agentText,
            '(?m)^\s{2}' + [regex]::Escape($iconKey) + ':\s*(?<value>.+?)\s*$'
        )
        if (-not $iconMatch.Success) {
            continue
        }
        $rawIcon = $iconMatch.Groups['value'].Value.Trim().Trim('"', "'")
        $canonicalIcon = ConvertTo-CanonicalSkillPath -RelativePath $rawIcon -Context "agents/openai.yaml interface.$iconKey" -CheckExists
        if ($null -eq $canonicalIcon) {
            continue
        }
    }
}

function Test-MarkdownLinks {
    $markdownFiles = @(Get-ChildItem -LiteralPath $script:SkillRootFull -Recurse -File -Filter '*.md')
    $linkPattern = [regex]::new(
        '!?\[[^\]]*\]\((?<target><[^>]+>|[^\s\)]+)',
        [Text.RegularExpressions.RegexOptions]::IgnoreCase
    )
    $checkedLinks = 0

    foreach ($markdownFile in $markdownFiles) {
        $text = Get-Content -Raw -LiteralPath $markdownFile.FullName
        foreach ($match in $linkPattern.Matches($text)) {
            $target = $match.Groups['target'].Value.Trim().Trim('<', '>')
            if ([string]::IsNullOrWhiteSpace($target) -or $target.StartsWith('#')) {
                continue
            }
            if ($target.StartsWith('//') -or $target -match '^[A-Za-z][A-Za-z0-9+.-]*:') {
                continue
            }

            $cutPositions = @(
                @($target.IndexOf('#'), $target.IndexOf('?')) | Where-Object { $_ -ge 0 }
            )
            if ($cutPositions.Count -gt 0) {
                $target = $target.Substring(0, ($cutPositions | Measure-Object -Minimum).Minimum)
            }
            if ([string]::IsNullOrWhiteSpace($target)) {
                continue
            }

            try {
                $target = [Uri]::UnescapeDataString($target)
                if ([IO.Path]::IsPathRooted($target)) {
                    Add-Failure "Markdown link in '$($markdownFile.FullName)' is not portable: '$target'."
                    continue
                }
                $resolved = [IO.Path]::GetFullPath((Join-Path $markdownFile.DirectoryName $target))
            }
            catch {
                Add-Failure "Markdown link in '$($markdownFile.FullName)' is invalid: '$target'."
                continue
            }

            $rootPrefix = $script:SkillRootFull + [IO.Path]::DirectorySeparatorChar
            if (-not $resolved.StartsWith($rootPrefix, [StringComparison]::OrdinalIgnoreCase)) {
                Add-Failure "Markdown link escapes the skill root in '$($markdownFile.FullName)': '$target'."
                continue
            }
            if (-not (Test-Path -LiteralPath $resolved)) {
                Add-Failure "Broken Markdown link in '$($markdownFile.FullName)': '$target'."
                continue
            }
            $checkedLinks++
        }
    }

    Write-Host "[CHECK] Markdown internal links resolved: $checkedLinks"
}

function Test-UnfinishedMarkers {
    $markerPattern = '(?i)(?<![A-Za-z])(?:T' + 'ODO|T' + 'BD|FIX' + 'ME)(?![A-Za-z])'
    $textExtensions = [System.Collections.Generic.HashSet[string]]::new(
        [StringComparer]::OrdinalIgnoreCase
    )
    foreach ($extension in @('.md', '.yaml', '.yml', '.json', '.ps1', '.py', '.txt')) {
        [void]$textExtensions.Add($extension)
    }

    foreach ($file in Get-ChildItem -LiteralPath $script:SkillRootFull -Recurse -File) {
        if (-not $textExtensions.Contains($file.Extension)) {
            continue
        }
        $text = Get-Content -Raw -LiteralPath $file.FullName
        $match = [regex]::Match($text, $markerPattern)
        if (-not $match.Success) {
            continue
        }
        $line = 1 + ([regex]::Matches($text.Substring(0, $match.Index), '\n')).Count
        Add-Failure "Unfinished scaffold marker found in '$($file.FullName)' at line $line."
    }
}

if (-not (Test-Path -LiteralPath $script:SkillRootFull -PathType Container)) {
    Add-Failure "Skill root is missing: $script:SkillRootFull"
}

$manifest = Read-JsonDocument -Path $ManifestPath -Label 'manifest.yaml'
$caseDocument = Read-JsonDocument -Path $CasesPath -Label 'routing-cases.json'

$manifestRuleIds = [System.Collections.Generic.HashSet[string]]::new(
    [StringComparer]::OrdinalIgnoreCase
)
$ruleCoverage = @{}
$manifestTemplatePaths = [System.Collections.Generic.HashSet[string]]::new(
    [StringComparer]::OrdinalIgnoreCase
)
$manifestAxes = $null

if ($null -ne $manifest) {
    $axesProperty = $manifest.PSObject.Properties['axes']
    if ($null -eq $axesProperty -or $null -eq $axesProperty.Value) {
        Add-Failure 'manifest.axes is missing.'
    }
    else {
        $manifestAxes = $axesProperty.Value
        $axisDefinitions = @($manifestAxes.PSObject.Properties)
        if ($axisDefinitions.Count -eq 0) {
            Add-Failure 'manifest.axes must contain at least one declared axis.'
        }
        foreach ($axisDefinitionProperty in $axisDefinitions) {
            $defaultProperty = $axisDefinitionProperty.Value.PSObject.Properties['default']
            if ($null -ne $defaultProperty) {
                Test-AxisAssignment -AxisName $axisDefinitionProperty.Name -AxisDefinition $axisDefinitionProperty.Value -Value $defaultProperty.Value -Context 'manifest default' -EnforceShape
            }
            else {
                Test-AxisAssignment -AxisName $axisDefinitionProperty.Name -AxisDefinition $axisDefinitionProperty.Value -Value $null -Context 'manifest axis'
            }
        }
    }

    $alwaysLoadProperty = $manifest.PSObject.Properties['always_load']
    $alwaysLoad = @(if ($null -eq $alwaysLoadProperty) {
        @(Get-CheckedStringArray -Owner 'manifest.always_load' -Value $null -Required)
    }
    else {
        @(Get-CheckedStringArray -Owner 'manifest.always_load' -Value $alwaysLoadProperty.Value -Required)
    })
    if ($alwaysLoad.Count -eq 0) {
        Add-Failure 'manifest.always_load must contain at least one shared-core path.'
    }
    foreach ($path in $alwaysLoad) {
        [void](ConvertTo-CanonicalSkillPath -RelativePath $path -Context 'manifest.always_load' -CheckExists)
    }
    if ($alwaysLoad.Count -ne 1 -or $alwaysLoad[0] -ne 'static/core/stance-and-boundaries.md') {
        Add-Failure 'manifest.always_load must contain only static/core/stance-and-boundaries.md.'
    }

    $expectedProvisionalDefaults = [ordered]@{
        interaction_mode = 'unknown'
        tutor_style = 'provisional'
        study_scope = 'unknown'
        task = 'unknown'
        project_stage = 'unknown'
        claim_target = 'provisional'
        input_evidence = 'unknown'
        audience = 'unknown'
    }
    foreach ($axisName in $expectedProvisionalDefaults.Keys) {
        $axisProperty = $manifestAxes.PSObject.Properties[$axisName]
        if ($null -eq $axisProperty) {
            Add-Failure "Manifest is missing provisional axis '$axisName'."
            continue
        }
        $defaultProperty = $axisProperty.Value.PSObject.Properties['default']
        if ($null -eq $defaultProperty -or [string]$defaultProperty.Value -ne $expectedProvisionalDefaults[$axisName]) {
            Add-Failure "Axis '$axisName' must default to '$($expectedProvisionalDefaults[$axisName])'."
        }
    }

    $rulesProperty = $manifest.PSObject.Properties['rules']
    $rules = if ($null -eq $rulesProperty) {
        Add-Failure 'manifest.rules is missing.'
        @()
    }
    elseif ($rulesProperty.Value -is [string] -or -not (Test-IsSequence $rulesProperty.Value)) {
        Add-Failure 'manifest.rules must be an array.'
        @($rulesProperty.Value)
    }
    else {
        @($rulesProperty.Value)
    }
    if ($rules.Count -eq 0) {
        Add-Failure 'manifest.rules must contain at least one route rule.'
    }

    for ($ruleIndex = 0; $ruleIndex -lt $rules.Count; $ruleIndex++) {
        $rule = $rules[$ruleIndex]
        $idProperty = $rule.PSObject.Properties['id']
        $ruleId = if ($null -ne $idProperty) { ([string]$idProperty.Value).Trim() } else { '' }
        if ([string]::IsNullOrWhiteSpace($ruleId)) {
            Add-Failure "manifest.rules[$ruleIndex] is missing a non-empty id."
            $ruleId = "index-$ruleIndex"
        }
        elseif (-not $manifestRuleIds.Add($ruleId)) {
            Add-Failure "Duplicate manifest rule id '$ruleId'."
        }
        else {
            $ruleCoverage[$ruleId] = 0
        }

        $whenProperty = $rule.PSObject.Properties['when']
        if ($null -eq $whenProperty -or $null -eq $whenProperty.Value) {
            Add-Failure "Rule '$ruleId' is missing a when object."
        }
        else {
            $conditions = @($whenProperty.Value.PSObject.Properties)
            if ($conditions.Count -eq 0) {
                Add-Failure "Rule '$ruleId' has an empty when object."
            }
            foreach ($condition in $conditions) {
                $conditionValues = @(Get-ScalarValues $condition.Value)
                if ($conditionValues.Count -eq 0 -or @($conditionValues | Where-Object { [string]::IsNullOrWhiteSpace($_) }).Count -gt 0) {
                    Add-Failure "Rule '$ruleId' condition '$($condition.Name)' must contain non-empty string values."
                }
                if ($condition.Value -isnot [string] -and -not (Test-IsSequence $condition.Value)) {
                    Add-Failure "Rule '$ruleId' condition '$($condition.Name)' must be a string or string array."
                }
                if ($null -eq $manifestAxes) {
                    continue
                }
                $axisDefinition = $manifestAxes.PSObject.Properties[$condition.Name]
                if ($null -eq $axisDefinition) {
                    Add-Failure "Rule '$ruleId' uses undeclared axis '$($condition.Name)'."
                }
                else {
                    Test-AxisAssignment -AxisName $condition.Name -AxisDefinition $axisDefinition.Value -Value $condition.Value -Context "rule '$ruleId'"
                }
            }
        }

        $loadProperty = $rule.PSObject.Properties['load']
        $loadPaths = if ($null -eq $loadProperty) {
            @(Get-CheckedStringArray -Owner "rule '$ruleId'.load" -Value $null -Required)
        }
        else {
            @(Get-CheckedStringArray -Owner "rule '$ruleId'.load" -Value $loadProperty.Value -Required)
        }
        foreach ($path in $loadPaths) {
            [void](ConvertTo-CanonicalSkillPath -RelativePath $path -Context "rule '$ruleId'.load" -CheckExists)
        }

        $excludeProperty = $rule.PSObject.Properties['exclude']
        if ($null -ne $excludeProperty) {
            $excludePaths = @(Get-CheckedStringArray -Owner "rule '$ruleId'.exclude" -Value $excludeProperty.Value)
            foreach ($path in $excludePaths) {
                [void](ConvertTo-CanonicalSkillPath -RelativePath $path -Context "rule '$ruleId'.exclude" -CheckExists)
            }
        }
    }

    $conditionalCoreRules = [ordered]@{
        'unresolved-request-alignment' = 'static/core/research-request-passport.md'
        'request-passport-planning' = 'static/core/research-request-passport.md'
        'integrity-gates-review' = 'static/core/failure-modes-and-integrity-gates.md'
        'claim-ledger-task' = 'static/core/terminology-and-claim-ledgers.md'
        'mentor-core' = 'static/core/reader-and-mentor-workflow.md'
        'task-output-contract' = 'static/core/output-presets-and-revision-loop.md'
    }
    foreach ($ruleId in $conditionalCoreRules.Keys) {
        $matchingRules = @($rules | Where-Object { [string]$_.id -eq $ruleId })
        if ($matchingRules.Count -ne 1) {
            Add-Failure "Conditional core rule '$ruleId' must appear exactly once."
            continue
        }
        $loadPaths = @(Get-ScalarValues $matchingRules[0].load)
        if ($conditionalCoreRules[$ruleId] -notin $loadPaths) {
            Add-Failure "Conditional core rule '$ruleId' must load '$($conditionalCoreRules[$ruleId])'."
        }
    }

    $templatesProperty = $manifest.PSObject.Properties['templates']
    if ($null -eq $templatesProperty) {
        Add-Failure 'manifest.templates is missing; declare the reusable template paths.'
    }
    else {
        $templateLeaves = @(Get-StringLeaves $templatesProperty.Value)
        if ($templateLeaves.Count -eq 0) {
            Add-Failure 'manifest.templates contains no template paths.'
        }
        foreach ($path in $templateLeaves) {
            $canonical = ConvertTo-CanonicalSkillPath -RelativePath $path -Context 'manifest.templates' -CheckExists
            if ($null -ne $canonical) {
                [void]$manifestTemplatePaths.Add($canonical)
            }
        }
    }

    $onDemandProperty = $manifest.PSObject.Properties['on_demand']
    if ($null -eq $onDemandProperty) {
        Add-Failure 'manifest.on_demand is missing.'
    }
    elseif ($onDemandProperty.Value -is [string] -or -not (Test-IsSequence $onDemandProperty.Value)) {
        Add-Failure 'manifest.on_demand must be an array.'
    }
    else {
        $onDemandEntries = @($onDemandProperty.Value)
        for ($onDemandIndex = 0; $onDemandIndex -lt $onDemandEntries.Count; $onDemandIndex++) {
            $entry = $onDemandEntries[$onDemandIndex]
            $conditionProperty = $entry.PSObject.Properties['condition']
            $pathProperty = $entry.PSObject.Properties['path']
            if ($null -eq $conditionProperty -or [string]::IsNullOrWhiteSpace([string]$conditionProperty.Value)) {
                Add-Failure "manifest.on_demand[$onDemandIndex] is missing a non-empty condition."
            }
            if ($null -eq $pathProperty -or [string]::IsNullOrWhiteSpace([string]$pathProperty.Value)) {
                Add-Failure "manifest.on_demand[$onDemandIndex] is missing a non-empty path."
            }
            else {
                [void](ConvertTo-CanonicalSkillPath -RelativePath ([string]$pathProperty.Value) -Context "manifest.on_demand[$onDemandIndex].path" -CheckExists)
            }
        }
    }
}

$requiredTemplates = @()
$routingCases = @()
if ($null -ne $caseDocument) {
    $requiredTemplatesProperty = $caseDocument.PSObject.Properties['required_templates']
    $requiredTemplates = if ($null -eq $requiredTemplatesProperty) {
        @(Get-CheckedStringArray -Owner 'routing-cases.required_templates' -Value $null -Required)
    }
    else {
        @(Get-CheckedStringArray -Owner 'routing-cases.required_templates' -Value $requiredTemplatesProperty.Value -Required)
    }
    foreach ($path in $requiredTemplates) {
        $canonical = ConvertTo-CanonicalSkillPath -RelativePath $path -Context 'routing-cases.required_templates' -CheckExists
        if ($null -ne $canonical -and $null -ne $manifest -and -not $manifestTemplatePaths.Contains($canonical)) {
            Add-Failure "Required template '$canonical' is not declared under manifest.templates."
        }
    }

    $templateEntryContracts = [ordered]@{
        'templates/research-request-passport.md' = 'SKILL.md'
        'templates/claim-evidence-mechanism-ledger.md' = 'static/core/terminology-and-claim-ledgers.md'
        'templates/mechanism-bridge-canvas.md' = 'references/radiomics-mechanism-bridge.md'
        'templates/reviewer-audit.md' = 'references/constructive-manuscript-review-chain.md'
        'templates/constructive-review-and-repair-matrix.md' = 'references/constructive-manuscript-review-chain.md'
        'templates/mentor-decision-memo.md' = 'static/core/output-presets-and-revision-loop.md'
        'templates/revision-trace-matrix.md' = 'static/core/output-presets-and-revision-loop.md'
        'templates/claim-to-section-writing-map.md' = 'references/scientific-writing-chain.md'
    }
    foreach ($requiredTemplatePath in $requiredTemplates) {
        if (-not $templateEntryContracts.Contains($requiredTemplatePath)) {
            Add-Failure "Required template '$requiredTemplatePath' has no declared task-entry surface."
            continue
        }
        $entrySurface = [string]$templateEntryContracts[$requiredTemplatePath]
        $entryFullPath = Join-Path $script:SkillRootFull $entrySurface
        if (-not (Test-Path -LiteralPath $entryFullPath -PathType Leaf)) {
            Add-Failure "Template entry surface '$entrySurface' is missing for '$requiredTemplatePath'."
            continue
        }
        $entryText = Get-Content -Raw -LiteralPath $entryFullPath
        $templateFileName = Split-Path -Leaf $requiredTemplatePath
        if ($entryText.IndexOf($templateFileName, [StringComparison]::OrdinalIgnoreCase) -lt 0) {
            Add-Failure "Template '$requiredTemplatePath' is not explicitly reachable from '$entrySurface'."
        }
    }
    Write-Host "[CHECK] Task-to-template entry contracts: $($templateEntryContracts.Count) templates"

    $casesProperty = $caseDocument.PSObject.Properties['cases']
    if ($null -eq $casesProperty) {
        Add-Failure 'routing-cases.json is missing cases.'
    }
    elseif ($casesProperty.Value -is [string] -or -not (Test-IsSequence $casesProperty.Value)) {
        Add-Failure 'routing-cases.json cases must be an array.'
        $routingCases = @($casesProperty.Value)
    }
    else {
        $routingCases = @($casesProperty.Value)
    }
    if ($routingCases.Count -lt 10) {
        Add-Failure "routing-cases.json must define at least 10 cases; found $($routingCases.Count)."
    }
}

$caseIds = [System.Collections.Generic.HashSet[string]]::new(
    [StringComparer]::OrdinalIgnoreCase
)
foreach ($case in $routingCases) {
    $caseFailureCountBefore = $script:Failures.Count
    $idProperty = $case.PSObject.Properties['id']
    $caseId = if ($null -ne $idProperty) { ([string]$idProperty.Value).Trim() } else { '' }
    if ([string]::IsNullOrWhiteSpace($caseId)) {
        Add-Failure 'A routing case is missing a non-empty id.'
        $caseId = '<unnamed-case>'
    }
    elseif (-not $caseIds.Add($caseId)) {
        Add-Failure "Duplicate routing case id '$caseId'."
    }

    $axesProperty = $case.PSObject.Properties['axes']
    if ($null -eq $axesProperty -or $null -eq $axesProperty.Value -or @($axesProperty.Value.PSObject.Properties).Count -eq 0) {
        Add-Failure "Case '$caseId' must define a non-empty axes object."
        continue
    }
    if ($null -ne $manifestAxes) {
        foreach ($assignment in @($axesProperty.Value.PSObject.Properties)) {
            $axisDefinition = $manifestAxes.PSObject.Properties[$assignment.Name]
            if ($null -eq $axisDefinition) {
                Add-Failure "Case '$caseId' uses undeclared axis '$($assignment.Name)'."
                continue
            }
            Test-AxisAssignment -AxisName $assignment.Name -AxisDefinition $axisDefinition.Value -Value $assignment.Value -Context "case '$caseId'" -EnforceShape
        }
    }
    foreach ($compatibilityIssue in @(Get-AxisCompatibilityIssues -Axes $axesProperty.Value)) {
        Add-Failure "Case '$caseId' has incompatible axes: $compatibilityIssue"
    }

    $mustLoadProperty = $case.PSObject.Properties['must_load']
    $mustNotLoadProperty = $case.PSObject.Properties['must_not_load']
    $mustLoad = if ($null -eq $mustLoadProperty) {
        @(Get-CheckedStringArray -Owner "case '$caseId'.must_load" -Value $null -Required)
    }
    else {
        @(Get-CheckedStringArray -Owner "case '$caseId'.must_load" -Value $mustLoadProperty.Value -Required)
    }
    $mustNotLoad = if ($null -eq $mustNotLoadProperty) {
        @(Get-CheckedStringArray -Owner "case '$caseId'.must_not_load" -Value $null -Required)
    }
    else {
        @(Get-CheckedStringArray -Owner "case '$caseId'.must_not_load" -Value $mustNotLoadProperty.Value -Required)
    }

    $canonicalMustLoad = [System.Collections.Generic.HashSet[string]]::new(
        [StringComparer]::OrdinalIgnoreCase
    )
    $canonicalMustNotLoad = [System.Collections.Generic.HashSet[string]]::new(
        [StringComparer]::OrdinalIgnoreCase
    )
    foreach ($path in $mustLoad) {
        $canonical = ConvertTo-CanonicalSkillPath -RelativePath $path -Context "case '$caseId'.must_load" -CheckExists
        if ($null -ne $canonical) {
            [void]$canonicalMustLoad.Add($canonical)
        }
    }
    foreach ($path in $mustNotLoad) {
        $canonical = ConvertTo-CanonicalSkillPath -RelativePath $path -Context "case '$caseId'.must_not_load" -CheckExists
        if ($null -ne $canonical) {
            [void]$canonicalMustNotLoad.Add($canonical)
        }
    }
    foreach ($path in $canonicalMustLoad) {
        if ($canonicalMustNotLoad.Contains($path)) {
            Add-Failure "Case '$caseId' lists '$path' in both must_load and must_not_load."
        }
    }

    if ($null -eq $manifest) {
        continue
    }
    $route = Get-RoutedPaths -Manifest $manifest -Axes $axesProperty.Value
    $routeSet = [System.Collections.Generic.HashSet[string]]::new(
        [StringComparer]::OrdinalIgnoreCase
    )
    foreach ($path in $route.Paths) {
        [void]$routeSet.Add($path)
    }

    if ($route.MatchedRules.Count -eq 0) {
        Add-Failure "Case '$caseId' matched no manifest rule."
    }
    foreach ($ruleId in $route.MatchedRules) {
        if ($ruleCoverage.ContainsKey($ruleId)) {
            $ruleCoverage[$ruleId] = [int]$ruleCoverage[$ruleId] + 1
        }
    }
    foreach ($path in $canonicalMustLoad) {
        if (-not $routeSet.Contains($path)) {
            Add-Failure "Case '$caseId' did not load required path '$path'. Matched rules: $($route.MatchedRules -join ', ')."
        }
    }
    foreach ($path in $canonicalMustNotLoad) {
        if ($routeSet.Contains($path)) {
            Add-Failure "Case '$caseId' loaded forbidden path '$path'. Matched rules: $($route.MatchedRules -join ', ')."
        }
    }

    if ($script:Failures.Count -eq $caseFailureCountBefore) {
        Write-Host "[ROUTE PASS] $caseId :: rules=$($route.MatchedRules -join ',') :: files=$($route.Paths.Count)"
    }
    else {
        Write-Host "[ROUTE FAIL] $caseId :: rules=$($route.MatchedRules -join ',') :: files=$($route.Paths.Count)"
    }
}

if ($null -ne $manifest) {
    $matrixScopes = @(
        [pscustomobject]@{
            Scope = 'imaging-only'
            Modalities = @('radiomics')
            ActivePlaybooks = @('references/radiomics-pipeline.md')
            ReviewAdapter = 'references/imaging-reviewer-playbook.md'
            MentorAdapter = 'references/imaging-only-mentoring.md'
            RequiresBridge = $false
        },
        [pscustomobject]@{
            Scope = 'mechanism-only'
            Modalities = @('bulk-rna')
            ActivePlaybooks = @('references/bulk-rna-research-guidance.md')
            ReviewAdapter = 'references/mechanism-reviewer-playbook.md'
            MentorAdapter = 'references/standalone-mechanism-mentoring.md'
            RequiresBridge = $false
        },
        [pscustomobject]@{
            Scope = 'imaging-mechanism'
            Modalities = @('radiomics', 'bulk-rna')
            ActivePlaybooks = @('references/radiomics-pipeline.md', 'references/bulk-rna-research-guidance.md')
            ReviewAdapter = 'references/reviewer-playbook.md'
            MentorAdapter = 'references/research-mentoring-and-idea-development.md'
            RequiresBridge = $true
        }
    )
    $reviewAdapters = @(
        'references/imaging-reviewer-playbook.md',
        'references/mechanism-reviewer-playbook.md',
        'references/reviewer-playbook.md'
    )
    $mentorAdapters = @(
        'references/imaging-only-mentoring.md',
        'references/research-mentoring-and-idea-development.md',
        'references/standalone-mechanism-mentoring.md'
    )
    $submissionPaths = @(
        'references/imaging-submission-package.md',
        'references/mechanism-submission-package.md',
        'references/radiogenomics-submission-package.md'
    )
    $canonicalActivePlaybooks = @(
        'references/radiomics-pipeline.md',
        'references/bulk-rna-research-guidance.md'
    )
    $matrixCells = 0
    $submissionIsolationCells = 0

    foreach ($task in @('writing-revision', 'manuscript-review')) {
        foreach ($mode in @('reviewer', 'mentor', 'combined')) {
            foreach ($scopeSpec in $matrixScopes) {
                $axes = [pscustomobject][ordered]@{
                    interaction_mode = $mode
                    study_scope = $scopeSpec.Scope
                    active_modalities = $scopeSpec.Modalities
                    task = $task
                    writing_job = if ($task -eq 'writing-revision') { 'section-draft' } else { 'not-applicable' }
                    manuscript_section = if ($task -eq 'writing-revision') { 'results' } else { 'full-manuscript' }
                    submission_phase = 'not-applicable'
                    claim_target = 'association'
                    project_stage = 'manuscript'
                    input_evidence = 'manuscript-prose-or-figure'
                }
                $route = Get-RoutedPaths -Manifest $manifest -Axes $axes
                $routeSet = [System.Collections.Generic.HashSet[string]]::new(
                    [StringComparer]::OrdinalIgnoreCase
                )
                foreach ($path in $route.Paths) {
                    [void]$routeSet.Add($path)
                }

                $cell = "$task/$mode/$($scopeSpec.Scope)"
                foreach ($compatibilityIssue in @(Get-AxisCompatibilityIssues -Axes $axes)) {
                    Add-Failure "Task matrix '$cell' has incompatible axes: $compatibilityIssue"
                }
                $expectedChain = if ($task -eq 'writing-revision') {
                    'references/scientific-writing-chain.md'
                }
                else {
                    'references/constructive-manuscript-review-chain.md'
                }
                $forbiddenChain = if ($task -eq 'writing-revision') {
                    'references/constructive-manuscript-review-chain.md'
                }
                else {
                    'references/scientific-writing-chain.md'
                }
                if (-not $routeSet.Contains($expectedChain)) {
                    Add-Failure "Task matrix '$cell' did not load '$expectedChain'."
                }
                if ($routeSet.Contains($forbiddenChain)) {
                    Add-Failure "Task matrix '$cell' incorrectly loaded '$forbiddenChain'."
                }
                $expectedRuleId = if ($task -eq 'writing-revision') {
                    'scientific-writing-chain'
                }
                else {
                    'constructive-manuscript-review-chain'
                }
                $forbiddenRuleId = if ($task -eq 'writing-revision') {
                    'constructive-manuscript-review-chain'
                }
                else {
                    'scientific-writing-chain'
                }
                if ($route.MatchedRules -notcontains $expectedRuleId) {
                    Add-Failure "Task matrix '$cell' did not match task rule '$expectedRuleId'."
                }
                if ($route.MatchedRules -contains $forbiddenRuleId) {
                    Add-Failure "Task matrix '$cell' matched forbidden task rule '$forbiddenRuleId'."
                }

                $hasPitfalls = $routeSet.Contains('references/pitfalls.md')
                if ($task -eq 'manuscript-review' -and -not $hasPitfalls) {
                    Add-Failure "Task matrix '$cell' did not load the manuscript-review pitfalls adapter."
                }
                if ($task -eq 'writing-revision' -and $hasPitfalls) {
                    Add-Failure "Task matrix '$cell' loaded manuscript-review pitfalls during writing."
                }

                $loadedActivePlaybooks = @($canonicalActivePlaybooks | Where-Object { $routeSet.Contains($_) })
                $expectedActivePlaybooks = @($scopeSpec.ActivePlaybooks)
                if ($loadedActivePlaybooks.Count -ne $expectedActivePlaybooks.Count -or
                    @($expectedActivePlaybooks | Where-Object { $_ -notin $loadedActivePlaybooks }).Count -gt 0) {
                    Add-Failure "Task matrix '$cell' active playbooks mismatch. Expected: $($expectedActivePlaybooks -join ', '); loaded: $($loadedActivePlaybooks -join ', ')."
                }

                $loadedReviewAdapters = @($reviewAdapters | Where-Object { $routeSet.Contains($_) })
                if ($task -eq 'writing-revision' -and $loadedReviewAdapters.Count -ne 0) {
                    Add-Failure "Task matrix '$cell' loaded reviewer adapter(s): $($loadedReviewAdapters -join ', ')."
                }
                if ($task -eq 'manuscript-review') {
                    if ($loadedReviewAdapters.Count -ne 1 -or $loadedReviewAdapters[0] -ne $scopeSpec.ReviewAdapter) {
                        Add-Failure "Task matrix '$cell' must load exactly '$($scopeSpec.ReviewAdapter)'; loaded: $($loadedReviewAdapters -join ', ')."
                    }
                }

                $loadedMentorAdapters = @($mentorAdapters | Where-Object { $routeSet.Contains($_) })
                if ($mode -eq 'reviewer' -and $loadedMentorAdapters.Count -ne 0) {
                    Add-Failure "Task matrix '$cell' loaded mentor adapter(s) in reviewer mode: $($loadedMentorAdapters -join ', ')."
                }
                if ($mode -ne 'reviewer' -and ($loadedMentorAdapters.Count -ne 1 -or $loadedMentorAdapters[0] -ne $scopeSpec.MentorAdapter)) {
                    Add-Failure "Task matrix '$cell' must load exactly mentor adapter '$($scopeSpec.MentorAdapter)'; loaded: $($loadedMentorAdapters -join ', ')."
                }

                $loadedSubmissions = @($submissionPaths | Where-Object { $routeSet.Contains($_) })
                if ($loadedSubmissions.Count -ne 0) {
                    Add-Failure "Task matrix '$cell' loaded submission material: $($loadedSubmissions -join ', ')."
                }

                if ($scopeSpec.RequiresBridge) {
                    foreach ($requiredBridgePath in @('references/radiomics-mechanism-bridge.md', 'references/sample-to-image-mapping.md')) {
                        if (-not $routeSet.Contains($requiredBridgePath)) {
                            Add-Failure "Task matrix '$cell' did not load required bridge path '$requiredBridgePath'."
                        }
                    }
                }
                else {
                    foreach ($forbiddenBridgePath in @('references/radiomics-mechanism-bridge.md', 'references/sample-to-image-mapping.md')) {
                        if ($routeSet.Contains($forbiddenBridgePath)) {
                            Add-Failure "Task matrix '$cell' loaded cross-scale bridge path '$forbiddenBridgePath' outside imaging-mechanism scope."
                        }
                    }
                }

                $submissionStageAxes = $axes.PSObject.Copy()
                $submissionStageAxes.project_stage = 'submission'
                $submissionStageRoute = Get-RoutedPaths -Manifest $manifest -Axes $submissionStageAxes
                $submissionStageSet = [System.Collections.Generic.HashSet[string]]::new(
                    [StringComparer]::OrdinalIgnoreCase
                )
                foreach ($path in $submissionStageRoute.Paths) {
                    [void]$submissionStageSet.Add($path)
                }
                $leakedSubmission = @($submissionPaths | Where-Object { $submissionStageSet.Contains($_) })
                if ($leakedSubmission.Count -gt 0) {
                    Add-Failure "Submission-stage isolation '$cell' leaked package(s): $($leakedSubmission -join ', ')."
                }
                $submissionIsolationCells++
                $matrixCells++
            }
        }
    }
    Write-Host "[CHECK] Writing/review orthogonality matrix: $matrixCells cells"
    Write-Host "[CHECK] Submission-stage task isolation: $submissionIsolationCells cells"

    $submissionScopeSpecs = @(
        [pscustomobject]@{
            Scope = 'imaging-only'; Modalities = @('radiomics')
            Package = 'references/imaging-submission-package.md'
            Reviewer = 'references/imaging-reviewer-playbook.md'
        },
        [pscustomobject]@{
            Scope = 'mechanism-only'; Modalities = @('bulk-rna')
            Package = 'references/mechanism-submission-package.md'
            Reviewer = 'references/mechanism-reviewer-playbook.md'
        },
        [pscustomobject]@{
            Scope = 'imaging-mechanism'; Modalities = @('radiomics', 'bulk-rna')
            Package = 'references/radiogenomics-submission-package.md'
            Reviewer = 'references/reviewer-playbook.md'
        }
    )
    $submissionTaskCells = 0
    foreach ($phase in @('initial', 'post-decision')) {
        foreach ($stage in @('manuscript', 'submission')) {
            foreach ($scopeSpec in $submissionScopeSpecs) {
                $submissionAxes = [pscustomobject][ordered]@{
                    interaction_mode = 'reviewer'
                    study_scope = $scopeSpec.Scope
                    active_modalities = $scopeSpec.Modalities
                    external_reference_modalities = @()
                    generated_or_predicted_modalities = @()
                    proposed_validation_modalities = @()
                    task = 'submission-rebuttal'
                    writing_job = 'not-applicable'
                    manuscript_section = 'not-applicable'
                    submission_phase = $phase
                    claim_target = 'association'
                    project_stage = $stage
                    input_evidence = 'manuscript-prose-or-figure'
                }
                $submissionCell = "$phase/$stage/$($scopeSpec.Scope)"
                foreach ($compatibilityIssue in @(Get-AxisCompatibilityIssues -Axes $submissionAxes)) {
                    Add-Failure "Submission reachability '$submissionCell' has incompatible axes: $compatibilityIssue"
                }
                $submissionRoute = Get-RoutedPaths -Manifest $manifest -Axes $submissionAxes
                $submissionRouteSet = [System.Collections.Generic.HashSet[string]]::new(
                    [StringComparer]::OrdinalIgnoreCase
                )
                foreach ($path in $submissionRoute.Paths) {
                    [void]$submissionRouteSet.Add($path)
                }
                $expectedRule = if ($phase -eq 'initial') {
                    "initial-submission-$($scopeSpec.Scope)"
                }
                else {
                    "submission-rebuttal-$($scopeSpec.Scope)"
                }
                if ($submissionRoute.MatchedRules -notcontains $expectedRule) {
                    Add-Failure "Submission reachability '$submissionCell' did not match '$expectedRule'."
                }
                $loadedPackages = @($submissionPaths | Where-Object { $submissionRouteSet.Contains($_) })
                if ($loadedPackages.Count -ne 1 -or $loadedPackages[0] -ne $scopeSpec.Package) {
                    Add-Failure "Submission reachability '$submissionCell' package mismatch. Expected '$($scopeSpec.Package)'; loaded '$($loadedPackages -join ', ')'."
                }
                $loadedReviewers = @($reviewAdapters | Where-Object { $submissionRouteSet.Contains($_) })
                if ($phase -eq 'initial' -and $loadedReviewers.Count -ne 0) {
                    Add-Failure "Initial-submission reachability '$submissionCell' loaded reviewer adapter(s): $($loadedReviewers -join ', ')."
                }
                if ($phase -eq 'post-decision' -and
                    ($loadedReviewers.Count -ne 1 -or $loadedReviewers[0] -ne $scopeSpec.Reviewer)) {
                    Add-Failure "Post-decision reachability '$submissionCell' reviewer mismatch. Expected '$($scopeSpec.Reviewer)'; loaded '$($loadedReviewers -join ', ')'."
                }
                $submissionTaskCells++
            }
        }
    }
    Write-Host "[CHECK] Submission task reachability: $submissionTaskCells cells"

    $invalidAxisCases = [ordered]@{
        'writing-without-job-or-section' = [pscustomobject]@{
            interaction_mode = 'reviewer'; study_scope = 'imaging-only'; active_modalities = @('radiomics')
            task = 'writing-revision'; writing_job = 'not-applicable'; manuscript_section = 'not-applicable'
            submission_phase = 'not-applicable'
        }
        'non-writing-with-active-writing-job' = [pscustomobject]@{
            interaction_mode = 'reviewer'; study_scope = 'imaging-only'; active_modalities = @('radiomics')
            task = 'manuscript-review'; writing_job = 'section-draft'; manuscript_section = 'results'
            submission_phase = 'not-applicable'
        }
        'imaging-only-with-bulk-rna' = [pscustomobject]@{
            interaction_mode = 'reviewer'; study_scope = 'imaging-only'; active_modalities = @('radiomics', 'bulk-rna')
            task = 'analysis-interpretation'; writing_job = 'not-applicable'; submission_phase = 'not-applicable'
        }
        'mechanism-only-with-radiomics' = [pscustomobject]@{
            interaction_mode = 'reviewer'; study_scope = 'mechanism-only'; active_modalities = @('radiomics', 'bulk-rna')
            task = 'analysis-interpretation'; writing_job = 'not-applicable'; submission_phase = 'not-applicable'
        }
        'imaging-mechanism-without-biology' = [pscustomobject]@{
            interaction_mode = 'reviewer'; study_scope = 'imaging-mechanism'; active_modalities = @('radiomics')
            task = 'analysis-interpretation'; writing_job = 'not-applicable'; submission_phase = 'not-applicable'
        }
        'imaging-only-with-deep-fusion' = [pscustomobject]@{
            interaction_mode = 'reviewer'; study_scope = 'imaging-only'; active_modalities = @('deep-fusion')
            task = 'analysis-interpretation'; writing_job = 'not-applicable'; submission_phase = 'not-applicable'
        }
    }
    foreach ($invalidCaseId in $invalidAxisCases.Keys) {
        $detectedIssues = @(Get-AxisCompatibilityIssues -Axes $invalidAxisCases[$invalidCaseId])
        if ($detectedIssues.Count -eq 0) {
            Add-Failure "Adversarial axis case '$invalidCaseId' was not rejected."
        }
    }
    Write-Host "[CHECK] Adversarial incompatible-axis contracts: $($invalidAxisCases.Count) cases"

    $writingReferencePath = Join-Path $script:SkillRootFull 'references/scientific-writing-chain.md'
    $writingTemplatePath = Join-Path $script:SkillRootFull 'templates/claim-to-section-writing-map.md'
    $writingSurfaceText = (Get-Content -Raw -LiteralPath $writingReferencePath) + "`n" +
        (Get-Content -Raw -LiteralPath $writingTemplatePath)
    $writingJobValues = @(Get-ScalarValues $manifest.axes.writing_job.values | Where-Object { $_ -ne 'not-applicable' })
    foreach ($writingJobValue in $writingJobValues) {
        $needle = ([string][char]96) + $writingJobValue + ([string][char]96)
        if ($writingSurfaceText.IndexOf($needle, [StringComparison]::OrdinalIgnoreCase) -lt 0) {
            Add-Failure "Writing job '$writingJobValue' has no explicit writing-chain contract."
        }
    }
    $sectionValues = @(Get-ScalarValues $manifest.axes.manuscript_section.values | Where-Object { $_ -ne 'not-applicable' })
    foreach ($sectionValue in $sectionValues) {
        if ($writingSurfaceText.IndexOf($sectionValue, [StringComparison]::OrdinalIgnoreCase) -lt 0) {
            Add-Failure "Manuscript section '$sectionValue' has no explicit writing/template surface."
        }
    }
    Write-Host "[CHECK] Writing axis value contracts: $($writingJobValues.Count) jobs, $($sectionValues.Count) sections"

    $contentContracts = [ordered]@{
        'references/scientific-writing-chain.md' = @(
            'W-RETURN-TO-LEDGER',
            'W-LEDGER-READY',
            'W-HANDOFF-READY',
            'W-POLISH-READY',
            'Interaction-mode overlay',
            'Preset D scientific map plus Preset A',
            'Preset D architecture plus Preset B',
            'Preset E order followed by the affected part of Preset D',
            'primary evidence state',
            'Modality subtype',
            'Claim-link status',
            'No skill owns scientific facts',
            'directly without a packet',
            'shortest sufficient evidence chain',
            'Cross-artifact consistency',
            'A structural scaffold with placeholders is allowed'
        )
        'references/constructive-manuscript-review-chain.md' = @(
            'minimum feasible remedy',
            'optional stronger route',
            'cost/trade-off',
            'closure evidence',
            'Literature and theory',
            'confidence/scope limit'
        )
        'templates/claim-to-section-writing-map.md' = @(
            'Evidence pointer',
            'Target section',
            'Paragraph job',
            'missing—absence marker only',
            'Writer-editable fields',
            'Internal module-composition receipt'
        )
        'templates/constructive-review-and-repair-matrix.md' = @(
            'Genuine strengths',
            'Class',
            'Typed evidence anchor',
            'Governing criterion',
            'Minimum feasible remedy',
            'Frozen criteria for re-review',
            'Original confidence/scope limit'
        )
        'references/reviewer-playbook.md' = @(
            'Class',
            'Governing criterion',
            'Minimum feasible remedy'
        )
        'references/imaging-reviewer-playbook.md' = @(
            'class',
            'governing criterion',
            'minimum feasible remedy'
        )
        'references/mechanism-reviewer-playbook.md' = @(
            'class',
            'governing criterion',
            'minimum feasible remedy'
        )
        'references/transparent-peer-review-lessons-2024-2026.md' = @(
            'publication is not evidence',
            'generic “selection bias” disclaimer',
            'Formal journal requirement',
            'versioned canonical concern families',
            'ontology v1.0.0',
            'raw codes remain',
            'Reviewer-first chain',
            'Scope adapters',
            'Request triage',
            'Writing chain derived from reviewer scrutiny',
            'Revision and response-letter closure',
            'comment -> request class -> author decision'
        )
        'references/transparent-peer-review-concern-ontology-v1.tsv' = @(
            "ontology_version`traw_concern_code`tcanonical_concern_family",
            'CONTRIBUTION_CLAIM_CALIBRATION',
            'MECHANISM_FUNCTION_PERTURBATION',
            'REPRODUCIBILITY_OPENNESS'
        )
        'static/core/reader-and-mentor-workflow.md' = @(
            'direct-expert',
            'guided-learning',
            'T1-baseline',
            'T4-teach-back',
            'T5-transfer',
            'mastery_status',
            'does not authorize simulated data/results or file edits'
        )
        'references/analysis-plan-sap.md' = @(
            'treatment-contextual prognosis',
            'average-treatment-effect',
            'effect-modification',
            'does not by itself establish heterogeneity of benefit',
            'significance in one',
            'not an interaction test'
        )
        'references/radiomics-pipeline.md' = @(
            'wholly unseen',
            'standard ComBat/neuroCombat',
            'frozen transform for that new level',
            'adaptation rather than untouched validation'
        )
    }
    foreach ($contractPath in $contentContracts.Keys) {
        $fullContractPath = Join-Path $script:SkillRootFull $contractPath
        if (-not (Test-Path -LiteralPath $fullContractPath -PathType Leaf)) {
            Add-Failure "Content contract file is missing: '$contractPath'."
            continue
        }
        $contractText = Get-Content -Raw -LiteralPath $fullContractPath
        foreach ($requiredPhrase in $contentContracts[$contractPath]) {
            if ($contractText.IndexOf($requiredPhrase, [StringComparison]::OrdinalIgnoreCase) -lt 0) {
                Add-Failure "Content contract '$contractPath' is missing required phrase '$requiredPhrase'."
            }
        }
    }
    Write-Host "[CHECK] Writing/review semantic content contracts: $($contentContracts.Count) files"
}

foreach ($ruleId in $ruleCoverage.Keys | Sort-Object) {
    if ([int]$ruleCoverage[$ruleId] -eq 0) {
        Add-Failure "Manifest rule '$ruleId' is not exercised by routing-cases.json."
    }
}

Test-SkillMetadata
Test-MarkdownLinks
Test-UnfinishedMarkers

if ($VerifyLiterature) {
    $powerShellHost = (Get-Process -Id $PID).Path
    $literatureAudit = Join-Path $script:SkillRootFull 'scripts/audit_transcriptomics_literature_maps.ps1'
    if (-not (Test-Path -LiteralPath $literatureAudit -PathType Leaf)) {
        Add-Failure "Literature audit script is missing: $literatureAudit"
    }
    else {
        Write-Host '[CHECK] Running deterministic 100-paper literature-map audit.'
        & $powerShellHost -NoLogo -NoProfile -File $literatureAudit
        if ($LASTEXITCODE -ne 0) {
            Add-Failure "Literature-map audit exited with code $LASTEXITCODE."
        }
    }

    $transparentReviewAudit = Join-Path $script:SkillRootFull 'scripts/audit_transparent_peer_review_corpus.ps1'
    if (-not (Test-Path -LiteralPath $transparentReviewAudit -PathType Leaf)) {
        Add-Failure "Transparent-review audit script is missing: $transparentReviewAudit"
    }
    else {
        Write-Host '[CHECK] Running deterministic 100-paper transparent-review corpus audit.'
        & $powerShellHost -NoLogo -NoProfile -File $transparentReviewAudit
        if ($LASTEXITCODE -ne 0) {
            Add-Failure "Transparent-review corpus audit exited with code $LASTEXITCODE."
        }
    }
}

foreach ($warning in $script:Warnings) {
    Write-Host "[WARN] $warning" -ForegroundColor Yellow
}

if ($script:Failures.Count -gt 0) {
    Write-Host "Skill route validation: FAIL ($($script:Failures.Count) issue(s))" -ForegroundColor Red
    foreach ($failure in $script:Failures) {
        Write-Host "- $failure" -ForegroundColor Red
    }
    exit 1
}

Write-Host "Skill route validation: PASS ($($routingCases.Count) routing cases, $($manifestRuleIds.Count) rules, $($requiredTemplates.Count) templates)." -ForegroundColor Green
exit 0
