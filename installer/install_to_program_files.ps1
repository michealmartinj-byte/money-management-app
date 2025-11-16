# Elevated installer script: moves built exe to Program Files and creates shortcuts
try {
    $project = Split-Path -Parent $MyInvocation.MyCommand.Definition | Split-Path -Parent
} catch {
    $project = Get-Location
}

$src = Join-Path $project 'dist\MoneyManager.exe'
if (-not (Test-Path $src)) {
    Write-Error "Source executable not found: $src"
    exit 1
}

$destDir = 'C:\Program Files\MoneyManager'
if (-not (Test-Path $destDir)) {
    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
}

$destExe = Join-Path $destDir 'MoneyManager.exe'
Copy-Item -Path $src -Destination $destExe -Force

# Copy account file to local appdata so working dir can be there
$dataDir = Join-Path $env:LOCALAPPDATA 'MoneyManager'
if (-not (Test-Path $dataDir)) { New-Item -ItemType Directory -Path $dataDir -Force | Out-Null }
$acctSrc = Join-Path $project 'mm_account.json'
if (Test-Path $acctSrc) {
    Copy-Item -Path $acctSrc -Destination (Join-Path $dataDir 'mm_account.json') -Force
}

# Create Start Menu folder and shortcut
$ws = New-Object -ComObject WScript.Shell
$startMenuDir = Join-Path $env:APPDATA 'Microsoft\Windows\Start Menu\Programs\MoneyManager'
if (-not (Test-Path $startMenuDir)) { New-Item -ItemType Directory -Path $startMenuDir -Force | Out-Null }
$lnk = Join-Path $startMenuDir 'MoneyManager.lnk'
$s = $ws.CreateShortcut($lnk)
$s.TargetPath = $destExe
$s.WorkingDirectory = $dataDir
$s.Save()

# Create Desktop shortcut for the current user
$desktop = [Environment]::GetFolderPath('Desktop')
$lnk2 = Join-Path $desktop 'MoneyManager.lnk'
$s2 = $ws.CreateShortcut($lnk2)
$s2.TargetPath = $destExe
$s2.WorkingDirectory = $dataDir
$s2.Save()

Write-Output "Installed exe to: $destExe"
Write-Output "Start Menu shortcut: $lnk"
Write-Output "Desktop shortcut: $lnk2"
