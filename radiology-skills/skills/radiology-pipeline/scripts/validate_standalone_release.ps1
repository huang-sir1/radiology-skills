#requires -Version 7.0

[CmdletBinding()]
param(
    [Parameter()]
    [string]$ProductRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$productRootFull = [IO.Path]::GetFullPath($ProductRoot)
$skillsRoot = Join-Path $productRootFull 'skills'
if (-not (Test-Path -LiteralPath $skillsRoot -PathType Container)) {
    throw "Skills root is missing: $skillsRoot"
}

$failures = [System.Collections.Generic.List[string]]::new()
$skillDirectories = @(Get-ChildItem -LiteralPath $skillsRoot -Directory |
    Where-Object { $_.Name -like 'radiology-*' })

foreach ($directory in $skillDirectories) {
    $entrypoint = Join-Path $directory.FullName 'SKILL.md'
    if (-not (Test-Path -LiteralPath $entrypoint -PathType Leaf)) {
        $failures.Add("Missing SKILL.md: $($directory.FullName)")
    }
}

$developmentOnlyRelativePaths = @(
    'skills\radiology-radiogenomics\references\architecture-provenance.md',
    'skills\radiology-pipeline\scripts\validate_standalone_release.ps1'
)
$externalPeerIds = @(
    'academic-research-suite',
    'nature-writing',
    'nature-polishing',
    'nature-statistics'
)
$textExtensions = @('.md', '.json', '.yaml', '.yml', '.ps1', '.py')

$runtimeFiles = @(Get-ChildItem -LiteralPath $skillsRoot -Recurse -File | Where-Object {
    $textExtensions -contains $_.Extension.ToLowerInvariant()
})

foreach ($file in $runtimeFiles) {
    $relativePath = [IO.Path]::GetRelativePath($productRootFull, $file.FullName)
    if ($developmentOnlyRelativePaths -contains $relativePath) {
        continue
    }

    $content = Get-Content -Raw -LiteralPath $file.FullName
    foreach ($peerId in $externalPeerIds) {
        if ($content.IndexOf($peerId, [StringComparison]::OrdinalIgnoreCase) -ge 0) {
            $failures.Add("External peer skill ID '$peerId' appears in runtime artifact: $relativePath")
        }
    }
}

$standaloneContentContracts = [ordered]@{
    'skills\radiology-writing\SKILL.md' = @(
        'If no packet exists',
        'do not block traceable sections',
        'bounded local scientific-state map'
    )
    'skills\radiology-polishing\SKILL.md' = @(
        'standalone mechanism studies',
        'VENUE_STYLE_UNVERIFIED'
    )
    'skills\radiology-radiogenomics\SKILL.md' = @(
        'independently publishable',
        'full workflow must remain usable'
    )
}

foreach ($relativePath in $standaloneContentContracts.Keys) {
    $fullPath = Join-Path $productRootFull $relativePath
    if (-not (Test-Path -LiteralPath $fullPath -PathType Leaf)) {
        $failures.Add("Standalone content contract is missing: $relativePath")
        continue
    }
    $content = Get-Content -Raw -LiteralPath $fullPath
    foreach ($requiredPhrase in $standaloneContentContracts[$relativePath]) {
        if ($content.IndexOf($requiredPhrase, [StringComparison]::OrdinalIgnoreCase) -lt 0) {
            $failures.Add("Standalone content contract '$relativePath' is missing '$requiredPhrase'")
        }
    }
}

if ($failures.Count -gt 0) {
    Write-Host "Standalone release validation: FAIL ($($failures.Count) issue(s))"
    foreach ($failure in $failures) {
        Write-Host " - $failure"
    }
    exit 1
}

Write-Host "Standalone release validation: PASS"
Write-Host "Radiology skill directories: $($skillDirectories.Count)"
Write-Host "Runtime artifacts scanned: $($runtimeFiles.Count)"
Write-Host 'External Academic/Nature peer skills are development references only.'
