# scripts/install_desktop_shortcut.ps1
#
# Creates a Desktop shortcut to launch bypass-pet via the repo's venv,
# using pythonw.exe so no console window flashes on launch.
#
# Run manually:
#   powershell -ExecutionPolicy Bypass -File scripts\install_desktop_shortcut.ps1

$ErrorActionPreference = "Stop"

$repoRoot   = (Resolve-Path "$PSScriptRoot\..").Path
$pythonw    = Join-Path $repoRoot ".venv\Scripts\pythonw.exe"

if (-not (Test-Path $pythonw)) {
    Write-Host "ERROR: $pythonw not found." -ForegroundColor Red
    Write-Host "Run 'python -m venv .venv; .\.venv\Scripts\pip install -e .' from the repo root first." -ForegroundColor Yellow
    exit 1
}

$desktop  = [Environment]::GetFolderPath('Desktop')
$lnkPath  = Join-Path $desktop "Bypass Pet.lnk"

$wsh  = New-Object -ComObject WScript.Shell
$lnk  = $wsh.CreateShortcut($lnkPath)
$lnk.TargetPath       = $pythonw
$lnk.Arguments        = "-m bypass_pet"
$lnk.WorkingDirectory = $repoRoot
$lnk.IconLocation     = "$pythonw,0"
$lnk.Description      = "Toggle Claude Code Desktop bypass mode (Fight Club Jack/Tyler pet)"
$lnk.WindowStyle      = 7   # minimized; pet creates its own top-level window anyway
$lnk.Save()

Write-Host ""
Write-Host "  [OK] Created shortcut:"
Write-Host "       $lnkPath" -ForegroundColor Green
Write-Host ""
Write-Host "  Double-click 'Bypass Pet' on your Desktop to launch the pet."
Write-Host "  Right-click the pet -> Quit to close it."
Write-Host ""
