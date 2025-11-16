# 📦 Installation Guide

## Windows

### Option 1: Pre-built Executable (Easiest)
1. Download `MoneyManager.exe` from the [Releases](https://github.com/michealmartinj-byte/money-management-app/releases) page
2. Double-click to run (no installation needed)
3. The app stores data in `%LOCALAPPDATA%\MoneyManager\`

### Option 2: From Source (Python)
```powershell
# Clone repository
git clone https://github.com/michealmartinj-byte/money-management-app.git
cd money-management-app

# Install Python 3.8+ first from https://www.python.org/downloads/

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m src.gui
```

---

## macOS

### Option 1: From Source (Required - no pre-built exe for macOS)

**Requirements:** Python 3.8+ and git

```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Clone repository
git clone https://github.com/michealmartinj-byte/money-management-app.git
cd money-management-app

# Install Python (if not already installed)
brew install python3

# Install dependencies
pip3 install -r requirements.txt

# Run the application
python3 -m src.gui
```

### Option 2: Create a Standalone macOS App (Optional)

```bash
# Install PyInstaller
pip3 install pyinstaller

# Build the app
pyinstaller --onefile --windowed --name MoneyManager -p src src/gui.py

# Run from dist/ folder
./dist/MoneyManager
```

---

## Linux (Ubuntu/Debian)

```bash
# Clone repository
git clone https://github.com/michealmartinj-byte/money-management-app.git
cd money-management-app

# Install Python 3.8+ (if needed)
sudo apt-get install python3 python3-pip python3-tk

# Install dependencies
pip3 install -r requirements.txt

# Run the application
python3 -m src.gui
```

---

## Command-Line Interface (All Platforms)

If you prefer the CLI instead:

```bash
# Initialize account with $1000
python -m src.app init 1000

# Start a trading session
python -m src.app start

# Get next recommended bet
python -m src.app next

# Record a win
python -m src.app record --win 20

# Check account status
python -m src.app status
```

---

## Data Storage

- **Windows:** `C:\Users\{YourUsername}\AppData\Local\MoneyManager\mm_account.json`
- **macOS:** `~/.local/share/MoneyManager/mm_account.json`
- **Linux:** `~/.local/share/MoneyManager/mm_account.json`

**Export to Excel:** Click "💾 Export to Excel" in the GUI to create `trading_history.xlsx`

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'tkinter'"
**Windows:** Should be included with Python. Reinstall Python and check "tcl/tk and IDLE"
**macOS/Linux:** Run `brew install python-tk@3.x` or `sudo apt-get install python3-tk`

### "openpyxl not found"
Run: `pip install openpyxl`

### Can't find the app on macOS
The built app might be blocked by Gatekeeper. Run in Terminal instead:
```bash
python3 -m src.gui
```

---

## Need Help?

- Check [HOW_IT_WORKS.md](HOW_IT_WORKS.md) for strategy explanation
- Review [README_GITHUB.md](README_GITHUB.md) for full documentation
- Open an issue on GitHub for bugs or feature requests
