[Setup]
AppName=MoneyManager
AppVersion=1.0
DefaultDirName={pf}\MoneyManager
DefaultGroupName=MoneyManager
Compression=lzma2
SolidCompression=yes
OutputDir=installer_output
OutputBaseFilename=MoneyManagerSetup

[Files]
; Main executable built by PyInstaller
Source: "{#GetCurrentDir}\\dist\\MoneyManager.exe"; DestDir: "{app}"; Flags: ignoreversion

; Include a default account file in the user's local appdata folder
Source: "{#GetCurrentDir}\\installer\\default_mm_account.json"; DestDir: "{localappdata}\\MoneyManager"; Flags: ignoreversion createallsubdirs

[Dirs]
Name: "{localappdata}\\MoneyManager"

[Icons]
Name: "{group}\\MoneyManager"; Filename: "{app}\\MoneyManager.exe"; WorkingDir: "{localappdata}\\MoneyManager"
Name: "{userdesktop}\\MoneyManager"; Filename: "{app}\\MoneyManager.exe"; WorkingDir: "{localappdata}\\MoneyManager"; Tasks: desktopicon

[Tasks]
Name: desktopicon; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked

[Run]
Filename: "{app}\\MoneyManager.exe"; Description: "{cm:LaunchProgram,MoneyManager}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{localappdata}\\MoneyManager"
