param(
    [string]$PythonExe = ""
)

$ErrorActionPreference = "Stop"
$scriptPath = Join-Path $PSScriptRoot "validate_submission_skill.py"
if (-not $PythonExe) {
    $bundled = ""
    if (-not [string]::IsNullOrEmpty($env:USERPROFILE)) {
        $bundled = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
    }
    if ($bundled -and (Test-Path -LiteralPath $bundled)) {
        $PythonExe = $bundled
    } else {
        $command = Get-Command python -ErrorAction SilentlyContinue
        if ($command) {
            $PythonExe = $command.Source
        } else {
            throw "Python was not found. Pass -PythonExe with an explicit interpreter path."
        }
    }
}
& $PythonExe $scriptPath
if ($LASTEXITCODE -ne 0) {
    throw "radiology-submission validation failed with exit code $LASTEXITCODE"
}
