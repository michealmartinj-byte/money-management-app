Money Management App (Martingale Simulator)

This repository contains a simple money management simulator implementing a Martingale-style trading strategy.

Features:
- Martingale simulator with configurable parameters (starting balance, base bet, multiplier, win probability, payout multiplier, max bet, target profit).
- Simple CLI to run a simulation and print results.
- Example runner script and unit tests.

Usage (quick):

Run the example:

```pwsh
python -m src.cli --balance 1000 --base-bet 1 --multiplier 2 --win-prob 0.48 --payout 2 --target-profit 50 --max-rounds 1000
```

See `src/money_manager/martingale.py` for implementation details.

New CLI application for daily tracking (percentage martingale):

Initialize an account:

```pwsh
python -m src.app init 1000
```

Start a session:

```pwsh
python -m src.app start
```

Get next recommended bet (defaults: 2% base, double on loss):

```pwsh
python -m src.app next
```

Record a win (assumes 1:1 payout unless `--pnl` provided):

```pwsh
python -m src.app record --win
```

Record a loss:

```pwsh
python -m src.app record
```

Check status:

```pwsh
python -m src.app status
```

Account state is stored in `mm_account.json` in the current working directory.

Graphical user interface (Windows / cross-platform)

Run the Tkinter GUI:

```pwsh
python -m src.gui
```

What the GUI does:
- Initialize account balance and persist state to `mm_account.json`.
- Start and end sessions.
- Compute next bet as a percentage of current balance (default 2%), doubling the percent on each loss.
- Record wins/losses with automatic balance updates and session history.

Packaging to an executable (optional):
- Install `pyinstaller` and build a one-file exe:

```pwsh
python -m pip install pyinstaller
pyinstaller --onefile --name MoneyManager -w -F -p src src/gui.py

The generated executable will be in `dist\MoneyManager.exe`.

Create a Windows installer (Inno Setup)

1. Install Inno Setup from https://jrsoftware.org/ and make sure `iscc.exe` is on your PATH.
2. Build the installer using the provided PowerShell helper (run from project root):

```pwsh
cd money-management-app
\installer\build_installer.ps1
```

3. The resulting installer will be in `installer_output\MoneyManagerSetup.exe`.

Notes:
- The installer installs the exe to `C:\Program Files\MoneyManager` and places a default `mm_account.json` in your local appdata folder (`%LOCALAPPDATA%\MoneyManager`). Shortcuts created by the installer set the working directory to that data folder so the app reads/writes the saved account file there.
- If you want me to build the installer on your machine now, confirm and I will run the build script (requires Inno Setup installed).
```

The generated executable will be in `dist\MoneyManager.exe`.
