#requires -Version 7.0

[CmdletBinding()]
param(
    [string]$ProductRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path,
    [string]$PythonExecutable = $env:RADIOLOGY_SKILLS_PYTHON,
    [string]$QuickValidatePath = '',
    [string]$PluginValidatorPath = ''
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$env:PYTHONDONTWRITEBYTECODE = '1'
$root = [IO.Path]::GetFullPath($ProductRoot)
$allowlistPath = Join-Path $root 'release-allowlist.txt'
$ignorePath = Join-Path $root '.gitignore'
$errors = [System.Collections.Generic.List[string]]::new()
$expectedSkillCount = 40
$forbiddenDirectoryNames = @(
    '__pycache__', 'node_modules', 'research', 'tmp', '.git', '.venv', 'venv',
    '.artifact-audit', 'release-build', 'dist', 'runtime', 'runtimes'
)
$forbiddenFileExtensions = @(
    '.pyc', '.pyo', '.pyd', '.dll', '.exe', '.so', '.dylib', '.log', '.tmp'
)

if (-not (Test-Path -LiteralPath $allowlistPath -PathType Leaf)) {
    throw "Missing release allowlist: $allowlistPath"
}

$pluginManifestPath = Join-Path $root '.claude-plugin/plugin.json'
$marketplaceManifestPath = Join-Path $root '.claude-plugin/marketplace.json'
$codexPluginManifestPath = Join-Path $root '.codex-plugin/plugin.json'
$skillsPath = Join-Path $root 'skills'
$behaviorEvalPath = Join-Path $root 'behavior-evals'
foreach ($requiredPath in @(
    $pluginManifestPath, $marketplaceManifestPath, $codexPluginManifestPath, $skillsPath,
    $behaviorEvalPath
)) {
    if (-not (Test-Path -LiteralPath $requiredPath)) {
        $errors.Add("Missing required release path: $([IO.Path]::GetRelativePath($root, $requiredPath))")
    }
}

if ((Test-Path -LiteralPath $pluginManifestPath -PathType Leaf) -and
    (Test-Path -LiteralPath $marketplaceManifestPath -PathType Leaf) -and
    (Test-Path -LiteralPath $codexPluginManifestPath -PathType Leaf)) {
    try {
        $pluginManifest = Get-Content -LiteralPath $pluginManifestPath -Raw | ConvertFrom-Json
        $marketplaceManifest = Get-Content -LiteralPath $marketplaceManifestPath -Raw | ConvertFrom-Json
        $codexPluginManifest = Get-Content -LiteralPath $codexPluginManifestPath -Raw | ConvertFrom-Json
        $marketplacePlugins = @($marketplaceManifest.plugins)
        if ($marketplacePlugins.Count -ne 1) {
            $errors.Add("Marketplace manifest must contain exactly one plugin, found $($marketplacePlugins.Count)")
        }
        $marketplacePlugin = $marketplacePlugins | Select-Object -First 1
        foreach ($field in @('name', 'version', 'description')) {
            if ([string]::IsNullOrWhiteSpace([string]$pluginManifest.$field)) {
                $errors.Add("plugin.json is missing required field: $field")
            }
            if ([string]$pluginManifest.$field -ne [string]$marketplacePlugin.$field) {
                $errors.Add("Plugin/marketplace manifest mismatch: $field")
            }
            if ([string]$pluginManifest.$field -ne [string]$codexPluginManifest.$field) {
                $errors.Add("Claude/Codex plugin manifest mismatch: $field")
            }
        }
        if ([string]$codexPluginManifest.skills -ne './skills/') {
            $errors.Add('Codex plugin manifest must bind skills to ./skills/')
        }
        if ([string]$marketplaceManifest.name -ne [string]$pluginManifest.name) {
            $errors.Add('Marketplace top-level name must match the plugin name')
        }
        if ([string]$marketplacePlugin.source -ne './') {
            $errors.Add('Marketplace plugin source must be the local plugin root: ./')
        }
        if ([string]::IsNullOrWhiteSpace([string]$pluginManifest.author.name) -or
            [string]$marketplaceManifest.owner.name -ne [string]$pluginManifest.author.name -or
            [string]$codexPluginManifest.author.name -ne [string]$pluginManifest.author.name -or
            [string]$codexPluginManifest.interface.developerName -ne [string]$pluginManifest.author.name) {
            $errors.Add('Claude, marketplace and Codex author/owner identities must match')
        }
        if ([string]$codexPluginManifest.license -ne [string]$pluginManifest.license) {
            $errors.Add('Claude and Codex plugin license fields must match')
        }
    } catch {
        $errors.Add("Plugin manifest parse failure: $($_.Exception.Message)")
    }
}

if (Test-Path -LiteralPath $skillsPath -PathType Container) {
    $skillDirs = @(Get-ChildItem -LiteralPath $skillsPath -Directory -Force |
        Where-Object { $_.Name -like 'radiology-*' })
    if ($skillDirs.Count -ne $expectedSkillCount) {
        $errors.Add("Expected $expectedSkillCount radiology-* skills, found $($skillDirs.Count)")
    }
    foreach ($skillDir in $skillDirs) {
        foreach ($requiredRelative in @('SKILL.md', 'agents/openai.yaml')) {
            $requiredSkillFile = Join-Path $skillDir.FullName $requiredRelative
            if (-not (Test-Path -LiteralPath $requiredSkillFile -PathType Leaf)) {
                $errors.Add("Missing skill runtime file: $([IO.Path]::GetRelativePath($root, $requiredSkillFile))")
            }
        }
    }
}

$rawEntries = @(Get-Content -LiteralPath $allowlistPath | ForEach-Object { $_.Trim() } |
    Where-Object { $_ -and -not $_.StartsWith('#') })
$entries = [System.Collections.Generic.List[string]]::new()
$seenEntries = [System.Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
$rootPrefix = $root.TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar) +
    [IO.Path]::DirectorySeparatorChar
foreach ($rawEntry in $rawEntries) {
    $relative = $rawEntry.TrimEnd('/', '\')
    if ([string]::IsNullOrWhiteSpace($relative) -or [IO.Path]::IsPathRooted($relative)) {
        $errors.Add("Allowlist entry must be a non-rooted path below the product root: $rawEntry")
        continue
    }
    $segments = @($relative -split '[\\/]')
    if (@($segments | Where-Object { $_ -in @('', '.', '..') }).Count -gt 0) {
        $errors.Add("Allowlist entry contains an empty, dot or parent segment: $rawEntry")
        continue
    }
    try {
        $target = [IO.Path]::GetFullPath((Join-Path $root $relative))
    } catch {
        $errors.Add("Allowlist entry cannot be resolved safely: $rawEntry")
        continue
    }
    if (-not $target.StartsWith($rootPrefix, [StringComparison]::OrdinalIgnoreCase)) {
        $errors.Add("Allowlist entry escapes the product root: $rawEntry")
        continue
    }
    $canonical = [IO.Path]::GetRelativePath($root, $target).Replace('\', '/')
    $topLevel = @($canonical -split '/')[0]
    if ($forbiddenDirectoryNames -contains $topLevel) {
        $errors.Add("Forbidden development path is allowlisted: $rawEntry")
        continue
    }
    if (-not $seenEntries.Add($canonical)) {
        $errors.Add("Duplicate allowlist target after canonicalization: $rawEntry")
        continue
    }
    $entries.Add($canonical)
    if (-not (Test-Path -LiteralPath $target)) {
        $errors.Add("Allowlisted path is missing: $rawEntry")
    } elseif ((Get-Item -LiteralPath $target -Force).Attributes -band [IO.FileAttributes]::ReparsePoint) {
        $errors.Add("Allowlisted top-level path cannot be a reparse point: $rawEntry")
    }
}
$requiredAllowlistEntries = @(
    '.claude-plugin', '.codex-plugin', 'skills', 'behavior-evals', 'README.md', 'install.md',
    'LICENSE', '.gitignore', 'RELEASE.md', 'release-allowlist.txt', 'scripts'
)
foreach ($requiredEntry in $requiredAllowlistEntries) {
    if (-not $seenEntries.Contains($requiredEntry)) {
        $errors.Add("Required release surface is absent from the allowlist: $requiredEntry")
    }
}
foreach ($entry in $entries) {
    if ($requiredAllowlistEntries -notcontains $entry) {
        $errors.Add("Unapproved extra top-level release surface is allowlisted: $entry")
    }
}

if (-not (Test-Path -LiteralPath $ignorePath -PathType Leaf)) {
    $errors.Add('Missing .gitignore')
} else {
    $ignore = Get-Content -LiteralPath $ignorePath -Raw
    foreach ($pattern in @('/research/', '/tmp/', '**/__pycache__/', '*.py[cod]')) {
        if ($ignore.IndexOf($pattern, [StringComparison]::Ordinal) -lt 0) {
            $errors.Add(".gitignore is missing release exclusion: $pattern")
        }
    }
}

$releaseFiles = [System.Collections.Generic.List[IO.FileInfo]]::new()
foreach ($entry in $entries) {
    $target = Join-Path $root $entry.TrimEnd('/', '\')
    if (Test-Path -LiteralPath $target -PathType Leaf) {
        $file = Get-Item -LiteralPath $target
        if ($forbiddenFileExtensions -contains $file.Extension.ToLowerInvariant()) {
            $relativeArtifact = [IO.Path]::GetRelativePath($root, $file.FullName)
            $errors.Add("Forbidden generated or compiled artifact is allowlisted: $relativeArtifact")
        } else {
            $releaseFiles.Add($file)
        }
    } elseif (Test-Path -LiteralPath $target -PathType Container) {
        foreach ($hiddenPath in Get-ChildItem -LiteralPath $target -Recurse -Force |
            Where-Object {
                ($_.Attributes -band ([IO.FileAttributes]::Hidden -bor [IO.FileAttributes]::System)) -or
                $_.Name.StartsWith('.')
            }) {
            $relativeArtifact = [IO.Path]::GetRelativePath($root, $hiddenPath.FullName)
            $errors.Add("Hidden, system or dot-prefixed payload exists under an allowlisted path: $relativeArtifact")
        }
        foreach ($reparsePoint in Get-ChildItem -LiteralPath $target -Recurse -Force |
            Where-Object { $_.Attributes -band [IO.FileAttributes]::ReparsePoint }) {
            $relativeArtifact = [IO.Path]::GetRelativePath($root, $reparsePoint.FullName)
            $errors.Add("Reparse point exists under an allowlisted path: $relativeArtifact")
        }
        foreach ($forbiddenDir in Get-ChildItem -LiteralPath $target -Recurse -Directory -Force |
            Where-Object { $forbiddenDirectoryNames -contains $_.Name }) {
            $relativeArtifact = [IO.Path]::GetRelativePath($root, $forbiddenDir.FullName)
            $errors.Add("Forbidden development/cache directory exists under an allowlisted path: $relativeArtifact")
        }
        foreach ($file in Get-ChildItem -LiteralPath $target -Recurse -File -Force) {
            $relativeToEntry = [IO.Path]::GetRelativePath($target, $file.FullName)
            $segments = @($relativeToEntry -split '[\\/]')
            $directorySegments = if ($segments.Count -gt 1) {
                @($segments[0..($segments.Count - 2)])
            } else {
                @()
            }
            if (@($directorySegments | Where-Object { $forbiddenDirectoryNames -contains $_ }).Count) {
                continue
            }
            if ($forbiddenFileExtensions -contains $file.Extension.ToLowerInvariant()) {
                $relativeArtifact = [IO.Path]::GetRelativePath($root, $file.FullName)
                $errors.Add("Forbidden generated or compiled artifact exists under an allowlisted path: $relativeArtifact")
                continue
            }
            $releaseFiles.Add($file)
        }
    }
}

$uniqueReleaseFileCount = @($releaseFiles | ForEach-Object { $_.FullName } | Sort-Object -Unique).Count
if ($releaseFiles.Count -ne $uniqueReleaseFileCount) {
    $errors.Add('Allowlist entries produce duplicate release files')
}

function Resolve-ExecutablePath {
    param([string]$Candidate)
    if ([string]::IsNullOrWhiteSpace($Candidate)) {
        return $null
    }
    if (Test-Path -LiteralPath $Candidate -PathType Leaf) {
        return (Resolve-Path -LiteralPath $Candidate).Path
    }
    $command = Get-Command $Candidate -ErrorAction SilentlyContinue
    if ($null -ne $command -and -not [string]::IsNullOrWhiteSpace($command.Source)) {
        return $command.Source
    }
    return $null
}

function Invoke-ReleaseGate {
    param(
        [string]$Label,
        [string]$Executable,
        [string[]]$Arguments
    )
    Write-Host "Gate: $Label"
    & $Executable @Arguments
    if ($LASTEXITCODE -ne 0) {
        $errors.Add("Gate failed: $Label (exit $LASTEXITCODE)")
    }
}

function Test-FrozenGateInventory {
    param(
        [string]$Label,
        [IO.FileInfo[]]$DiscoveredFiles,
        [object[]]$ExpectedPaths
    )
    $discovered = @($DiscoveredFiles | Where-Object { $null -ne $_ } | ForEach-Object {
        [IO.Path]::GetRelativePath($root, $_.FullName).Replace('\', '/')
    })
    $expected = @($ExpectedPaths | ForEach-Object { [string]$_ })
    if ($expected.Count -eq 0) {
        $errors.Add("Frozen $Label inventory is empty")
        return
    }
    if ($expected.Count -ne @($expected | Sort-Object -Unique).Count) {
        $errors.Add("Frozen $Label inventory contains duplicate paths")
    }
    foreach ($path in $expected) {
        $segments = @($path -split '[\\/]')
        if ([IO.Path]::IsPathRooted($path) -or
            @($segments | Where-Object { $_ -in @('', '.', '..') }).Count -gt 0) {
            $errors.Add("Frozen $Label inventory contains an unsafe path: $path")
            continue
        }
        if ($discovered -notcontains $path) {
            $errors.Add("Frozen $Label inventory member is missing: $path")
        }
    }
    foreach ($path in $discovered) {
        if ($expected -notcontains $path) {
            $errors.Add("Discovered $Label is absent from frozen inventory: $path")
        }
    }
}

$testInventoryPath = Join-Path $root 'scripts/release-test-inventory.json'
$testInventory = $null
$expectedPythonTests = @()
$expectedPowerShellValidators = @()
if (-not (Test-Path -LiteralPath $testInventoryPath -PathType Leaf)) {
    $errors.Add('Missing frozen test inventory: scripts/release-test-inventory.json')
} else {
    try {
        $testInventory = Get-Content -LiteralPath $testInventoryPath -Raw | ConvertFrom-Json
        if ([string]$testInventory.schema_version -ne '1.0') {
            $errors.Add('Frozen test inventory schema_version must be 1.0')
        }
        $expectedPythonTests = @($testInventory.python_tests)
        $expectedPowerShellValidators = @($testInventory.powershell_validators)
    } catch {
        $errors.Add("Frozen test inventory parse failure: $($_.Exception.Message)")
    }
}

$pythonPath = Resolve-ExecutablePath $PythonExecutable
if ($null -eq $pythonPath) {
    $errors.Add(
        'Python 3 is required for release gates. Pass -PythonExecutable or set ' +
        'RADIOLOGY_SKILLS_PYTHON to a real interpreter path; Windows Store aliases are not accepted.'
    )
} else {
    & $pythonPath -c 'import sys, yaml, pypdf; from PIL import Image; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)'
    if ($LASTEXITCODE -ne 0) {
        $errors.Add(
            "Python release preflight failed: require Python 3.10+ with PyYAML, pypdf and Pillow: $pythonPath"
        )
    }
}

if ([string]::IsNullOrWhiteSpace($QuickValidatePath)) {
    $QuickValidatePath = Join-Path $env:USERPROFILE '.codex\skills\.system\skill-creator\scripts\quick_validate.py'
}
if ([string]::IsNullOrWhiteSpace($PluginValidatorPath)) {
    $PluginValidatorPath = Join-Path $env:USERPROFILE '.codex\skills\.system\plugin-creator\scripts\validate_plugin.py'
}

if ($null -ne $pythonPath) {
    $priorBytecodeSetting = $env:PYTHONDONTWRITEBYTECODE
    $env:PYTHONDONTWRITEBYTECODE = '1'
    try {
        foreach ($toolPath in @($QuickValidatePath, $PluginValidatorPath)) {
            if (-not (Test-Path -LiteralPath $toolPath -PathType Leaf)) {
                $errors.Add("Required Codex release validator is missing: $toolPath")
            }
        }
        if (Test-Path -LiteralPath $QuickValidatePath -PathType Leaf) {
            foreach ($skillDir in $skillDirs) {
                Invoke-ReleaseGate "skill quick_validate: $($skillDir.Name)" $pythonPath @(
                    $QuickValidatePath, $skillDir.FullName
                )
            }
        }
        if (Test-Path -LiteralPath $PluginValidatorPath -PathType Leaf) {
            Invoke-ReleaseGate 'Codex plugin/openai.yaml schema validation' $pythonPath @(
                $PluginValidatorPath, $root
            )
        }

        $assetValidator = Join-Path $root 'scripts/validate_release_assets.py'
        if (-not (Test-Path -LiteralPath $assetValidator -PathType Leaf)) {
            $errors.Add('Missing release JSON/YAML/link validator: scripts/validate_release_assets.py')
        } else {
            Invoke-ReleaseGate 'release JSON/YAML/frontmatter/local-link validation' $pythonPath @(
                $assetValidator, $root
            )
        }

        $pythonTests = @(
            Get-ChildItem -LiteralPath (Join-Path $root 'scripts') -Recurse -File -Force -Filter '*.py' -ErrorAction SilentlyContinue
            Get-ChildItem -LiteralPath $skillsPath -Recurse -File -Force -Filter '*.py'
            Get-ChildItem -LiteralPath $behaviorEvalPath -Recurse -File -Force -Filter '*.py' -ErrorAction SilentlyContinue
        ) | Where-Object { $_.Name -like 'test_*.py' -or $_.Name -like '*_test.py' } |
            Sort-Object FullName -Unique
        Test-FrozenGateInventory -Label 'Python test' -DiscoveredFiles ([IO.FileInfo[]]$pythonTests) `
            -ExpectedPaths ([object[]]$expectedPythonTests)
        foreach ($testFile in $pythonTests) {
            $relativeTest = [IO.Path]::GetRelativePath($root, $testFile.FullName)
            Invoke-ReleaseGate "Python regression: $relativeTest" $pythonPath @($testFile.FullName)
        }
    } finally {
        $env:PYTHONDONTWRITEBYTECODE = $priorBytecodeSetting
    }
}

$powerShellValidators = @(Get-ChildItem -LiteralPath $skillsPath -Recurse -File -Force -Filter 'validate_*.ps1') |
    Sort-Object FullName -Unique
Test-FrozenGateInventory -Label 'PowerShell validator' `
    -DiscoveredFiles ([IO.FileInfo[]]$powerShellValidators) `
    -ExpectedPaths ([object[]]$expectedPowerShellValidators)
foreach ($validator in $powerShellValidators) {
    $relativeValidator = [IO.Path]::GetRelativePath($root, $validator.FullName)
    Invoke-ReleaseGate "PowerShell contract: $relativeValidator" 'pwsh' @(
        '-NoProfile', '-File', $validator.FullName
    )
}

if ($errors.Count) {
    Write-Host "Release boundary: FAIL ($($errors.Count) issue(s))" -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" }
    exit 1
}

$bytes = ($releaseFiles | Measure-Object -Property Length -Sum).Sum
# Order by forward-slash relative path with OrdinalIgnoreCase to match build_release.py's
# casefold tree digest; culture-aware Sort-Object orders punctuation differently.
$treeRows = foreach ($file in $releaseFiles) {
    [PSCustomObject]@{
        Relative = [IO.Path]::GetRelativePath($root, $file.FullName).Replace('\', '/')
        File     = $file
    }
}
$orderedRows = [Linq.Enumerable]::OrderBy(
    [object[]]$treeRows,
    [Func[object, string]] { param($row) $row.Relative },
    [StringComparer]::OrdinalIgnoreCase
)
$treeLines = [System.Collections.Generic.List[string]]::new()
foreach ($row in $orderedRows) {
    $hash = (Get-FileHash -LiteralPath $row.File.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
    $treeLines.Add("$($row.Relative)`t$($row.File.Length)`t$hash`n")
}
$treeBytes = [Text.Encoding]::UTF8.GetBytes(($treeLines -join ''))
$treeHashBytes = [Security.Cryptography.SHA256]::HashData($treeBytes)
$treeHash = [Convert]::ToHexString($treeHashBytes).ToLowerInvariant()
Write-Host 'Release boundary: PASS' -ForegroundColor Green
Write-Host "Allowlist entries: $($entries.Count)"
Write-Host "Release files: $($releaseFiles.Count)"
Write-Host ('Release bytes: {0:N0}' -f $bytes)
Write-Host "Release tree SHA-256: $treeHash"
Write-Host 'Development research/tmp/.git paths are outside the release surface.'
Write-Host 'Skill quick_validate, Codex manifest/openai.yaml schema, JSON/YAML/link checks and discovered tests passed.'
