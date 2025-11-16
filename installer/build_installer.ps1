<#
Build the Inno Setup installer using `iscc.exe` (Inno Setup Compiler).

Requires: Inno Setup installed and `iscc.exe` available on PATH.
Run from PowerShell in the project root:

  .\installer\build_installer.ps1

If Inno Setup is not installed, download it from https://jrsoftware.org/
#>
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$projectRoot = Split-Path -Parent $scriptDir
Push-Location $projectRoot

$iss = Join-Path $scriptDir 'MoneyManager.iss'
if (-not (Test-Path $iss)) {
    Write-Error "Cannot find $iss"
    Pop-Location
    exit 1
}

$iscc = Get-Command iscc -ErrorAction SilentlyContinue
if (-not $iscc) {
    Write-Error "Inno Setup Compiler (iscc.exe) not found on PATH. Install Inno Setup: https://jrsoftware.org/"
    Pop-Location
    exit 1
}

Write-Output "Building installer from $iss"
& iscc $iss

if ($LASTEXITCODE -eq 0) {
    Write-Output "Installer built in: $projectRoot\installer_output\"
} else {
    Write-Error "Installer build failed (iscc exit code $LASTEXITCODE)"
}

Pop-Location
