[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$tests = Get-Content -LiteralPath (Join-Path $root 'tests/prisma-routing-cases.json') -Raw | ConvertFrom-Json
$text = @(
  Get-Content -LiteralPath (Join-Path $root 'SKILL.md') -Raw
  Get-Content -LiteralPath (Join-Path $root 'references/guideline-router.md') -Raw
  Get-Content -LiteralPath (Join-Path $root 'references/guideline-versions.md') -Raw
  Get-Content -LiteralPath (Join-Path $root 'references/prisma-general-scoping.md') -Raw
) -join "`n"
$errors = [System.Collections.Generic.List[string]]::new()
foreach ($phrase in @('PRISMA 2020','PRISMA-ScR','PRISMA-S','PRISMA-P','PRISMA-LSR','PRISMA-COSMIN','items 1-27','items 1-22','PRESENT','frozen evidence','flow diagram')) {
  if ($text.IndexOf($phrase, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) { $errors.Add("Missing phrase: $phrase") }
}
foreach ($route in @('prisma-2020','prisma-scr','prisma-s','prisma-p','prisma-lsr','prisma-cosmin-omi')) {
  if ($route -notin @($tests.positive_cases.route)) { $errors.Add("Missing positive route: $route") }
}
$ids = @($tests.positive_cases.id + $tests.boundary_cases.id)
if (($ids | Sort-Object -Unique).Count -ne $ids.Count) { $errors.Add('Case IDs must be unique.') }
if (@($tests.invariants).Count -lt 7) { $errors.Add('At least seven invariants are required.') }
if ($errors.Count) {
  Write-Host "FAIL: PRISMA reporting routes ($($errors.Count) issue(s))" -ForegroundColor Red
  $errors | ForEach-Object { Write-Host " - $_" }
  exit 1
}
Write-Host 'PASS: PRISMA general/scoping reporting routes' -ForegroundColor Green
Write-Host "Static contract cases: $(@($tests.positive_cases).Count)"
Write-Host "Boundary cases: $(@($tests.boundary_cases).Count)"
Write-Host "Invariants: $(@($tests.invariants).Count)"
Write-Host 'Note: static validation does not execute case prompts or prove model behavior.'
