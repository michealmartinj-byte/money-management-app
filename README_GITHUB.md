# 💰 Money Manager - Martingale Trading App

A beautiful, modern GUI application for tracking daily money management using a percentage-based Martingale trading strategy. Start with 2% of your balance, double the bet on losses, and reset to 2% on wins.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![GUI](https://img.shields.io/badge/GUI-Tkinter-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-red?style=flat-square)

## 🎯 Features

- **Beautiful Dark-themed GUI** — Modern design with intuitive controls
- **Percentage-based Martingale** — Automatically calculates bet sizes (2% base, 4% on loss 1, 8% on loss 2, etc.)
- **Session Management** — Start/end trading sessions, track history
- **Persistent Storage** — Account data saved in `%LOCALAPPDATA%\MoneyManager\`
- **Real-time Balance Tracking** — Color-coded balance display (green=profit, red=loss)
- **CLI Tool** — Command-line interface for automation
- **Simulator** — Pure martingale logic for backtesting
- **Cross-platform** — Runs on Windows, macOS, Linux

## 📦 Installation

### Option 1: Pre-built Executable (Windows)

1. Download the latest release from [Releases](releases)
2. Double-click `MoneyManager.exe` or use the Desktop shortcut
3. Initialize your account balance and start trading

### Option 2: From Source (Python)

**Requirements:** Python 3.8+

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/money-manager-martingale.git
cd money-manager-martingale

# Install dependencies
pip install -r requirements.txt

# Run the GUI
python -m src.gui_new
```

## 🚀 Quick Start

### Initialize Account
1. Open MoneyManager GUI (or run `python -m src.gui_new`)
2. Enter initial balance (e.g., 1000) in the "Init Balance" field
3. Click "Initialize"

### Start Trading
1. Click "▶ Start Session"
2. Click "📊 Next Bet" to see recommended bet amount
3. Place your trade in your broker/exchange
4. Click "✓ Record Win" or "✗ Record Loss"
5. View your session history in the table below

### CLI Usage

```bash
# Initialize account
python -m src.app init 1000

# Start a trading session
python -m src.app start

# Get next recommended bet
python -m src.app next

# Record a win
python -m src.app record --win

# Check account status
python -m src.app status
```

## 📊 How Martingale Strategy Works

Starting balance: **$1000**

| Round | Result | Bet % | Bet $ | P&L | Balance |
|-------|--------|-------|-------|-----|---------|
| 1     | Loss   | 2%    | $20   | -$20 | $980   |
| 2     | Loss   | 4%    | $39.2 | -$39.2 | $940.8 |
| 3     | Win    | 8%    | $75.3 | +$75.3 | $1016.1 |
| 4     | Win    | 2%    | $20   | +$20 | $1036.1 |

**Key Rules:**
- Start new session at 2% of current balance
- Each loss → multiply bet % by 2
- Each win → reset bet % to 2% (ends current session)
- App stops session after a win; next session starts fresh at 2%

## 🛠 Project Structure

```
money-manager-martingale/
├── src/
│   ├── gui.py                 # Original GUI
│   ├── gui_new.py            # Beautiful redesigned GUI ✨
│   ├── app.py                # CLI application
│   ├── cli.py                # Simulator CLI
│   └── money_manager/
│       ├── martingale.py      # Martingale simulator logic
│       └── session.py         # Session & account manager
├── examples/
│   └── run_simulation.py      # Example usage
├── tests/
│   ├── test_martingale.py    # Unit tests
│   └── test_session.py       # Session tests
├── installer/
│   ├── MoneyManager.iss      # Inno Setup installer script
│   ├── build_installer.ps1   # Build helper
│   └── default_mm_account.json
├── dist/
│   └── MoneyManager.exe      # Built Windows executable
├── README.md                 # This file
├── GITHUB_SETUP.md          # GitHub push instructions
├── requirements.txt         # Python dependencies
└── .gitignore              # Git ignore rules
```

## 🧪 Testing

Run the test suite:

```bash
python -m pytest tests/ -v
```

## ⚙️ Configuration

### Default Parameters
- **Base bet:** 2% of current balance
- **Multiplier:** 2× (doubles on each loss)
- **Win payout:** 1:1 (you keep the bet + profit)

Customize in the GUI:
- Change "Base %" field to adjust starting percentage
- Change "Multiplier" field to adjust loss scaling

## 📝 Examples

### Example 1: Simulate a series of trades
```bash
python -m src.cli --balance 1000 --base-bet 1 --multiplier 2 --win-prob 0.5 --payout 2 --target-profit 100
```

### Example 2: CLI daily tracking
```bash
# Day 1
python -m src.app init 5000        # Start with $5000
python -m src.app start             # Begin session
python -m src.app record --win       # First trade: win
python -m src.app status            # Check balance

# Day 2
python -m src.app start
python -m src.app record            # Loss (--win not specified defaults to loss)
python -m src.app next              # See next bet size
python -m src.app record --win      # Win to end session
```

## ⚠️ Disclaimer

**This app is for educational purposes only.** The Martingale strategy has risks:
- Requires unlimited capital (to survive long losing streaks)
- Broker/exchange may have bet limits
- Transaction fees/slippage can erode profits
- Use only money you can afford to lose

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by trading risk management strategies
- Built with Python and Tkinter
- Modern UI design principles

## 📧 Support

For issues, feature requests, or questions:
- Open an issue on GitHub
- Check existing issues and documentation first

---

**Happy trading! 📈** Remember: always trade responsibly and within your risk tolerance.

