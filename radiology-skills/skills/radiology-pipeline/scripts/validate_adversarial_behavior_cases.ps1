[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$pipelineRoot = Split-Path -Parent $PSScriptRoot
$skillsRoot = Split-Path -Parent $pipelineRoot
$tests = Get-Content -LiteralPath (Join-Path $pipelineRoot 'tests/adversarial-behavior-cases.json') -Raw | ConvertFrom-Json
$contract = Get-Content -LiteralPath (Join-Path $pipelineRoot 'references/adversarial-research-behavior-contract.md') -Raw
$errors = [System.Collections.Generic.List[string]]::new()
$skillNames = @(Get-ChildItem -LiteralPath $skillsRoot -Directory | Where-Object {
  Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md')
} | ForEach-Object Name)
$cases = @($tests.cases)
$ids = @($cases.id)
if (($ids | Sort-Object -Unique).Count -ne $ids.Count) { $errors.Add('Behavior case IDs must be unique.') }
foreach ($case in $cases) {
  if ($case.primary_owner -notin $skillNames) { $errors.Add("Unknown owner in $($case.id): $($case.primary_owner)") }
  if (@($case.required_behaviors).Count -lt 3) { $errors.Add("Case $($case.id) needs at least three required behaviors") }
  if (@($case.forbidden_behaviors).Count -lt 2) { $errors.Add("Case $($case.id) needs at least two forbidden behaviors") }
  if ([string]::IsNullOrWhiteSpace($case.closure_evidence)) { $errors.Add("Case $($case.id) lacks closure evidence") }
}
foreach ($family in @($tests.required_families)) {
  if ($family -notin @($cases.family)) { $errors.Add("Missing behavior family: $family") }
}
foreach ($phrase in @('fluent answer fails','minimum defensible repair','measured, derived, estimated','not an automated proof','qualified reviewer')) {
  if ($contract.IndexOf($phrase, [StringComparison]::OrdinalIgnoreCase) -lt 0) { $errors.Add("Behavior contract missing: $phrase") }
}
if ($errors.Count) {
  Write-Host "FAIL: adversarial behavior registry ($($errors.Count) issue(s))" -ForegroundColor Red
  $errors | ForEach-Object { Write-Host " - $_" }
  exit 1
}
Write-Host 'PASS: adversarial behavior registry' -ForegroundColor Green
Write-Host "Cases: $($cases.Count)"
Write-Host "Behavior families: $(@($tests.required_families).Count)"
Write-Host 'Note: structural registry validation is not a model-behavior evaluation.'
