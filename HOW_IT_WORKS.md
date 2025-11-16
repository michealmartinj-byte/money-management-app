# 💰 Money Manager - How It Works

## ❓ Does It Calculate Automatically?

**YES! The app calculates everything automatically.** Here's what happens:

### 1. **Automatic Bet Calculation**
When you click "📊 Next Bet", the app automatically:
- Calculates bet percentage based on previous results
- Multiplies your current balance by that percentage
- Shows you the exact amount to bet

**Example:**
```
Starting balance: $1000
Base percentage: 2%
Next bet = $1000 × 0.02 = $20 ✓ (shown automatically)
```

### 2. **Automatic Balance Updates**
When you click "✓ Record Win" or "✗ Record Loss":
- The app **automatically** updates your balance
- Recalculates the next bet percentage
- Updates the history table

**Example Flow:**
```
Session 1:
- Starting balance: $1000
- Next bet: $20 (2%)
- You record a LOSS → Balance becomes $980 (automatically updated)
- Next bet: $39.2 (4% of $980 - doubled percentage)

- You record a WIN → Balance becomes $1019.2 (automatically updated)
- Session ends
- Next session resets to 2%
```

### 3. **Automatic Column Descriptions**

| Column | Meaning | Calculated How |
|--------|---------|-----------------|
| **Step** | Trade number (1, 2, 3...) | Auto-incremented |
| **Bet $ Amount** | How much you bet in dollars | `Balance × Bet %` (auto) |
| **Bet %** | Percentage of balance bet | 2% (start), then 4%, 8%, 16%... on losses |
| **Win/Loss** | Trade result (you tell the app) | You click "Record Win" or "Record Loss" |
| **P&L ($)** | Profit or Loss amount | Auto-calculated: +Bet (win) or -Bet (loss) |
| **New Balance** | Your balance after this trade | Auto-calculated: Old Balance + P&L |

## 📊 Step-by-Step Example

**Scenario:** You start with $1000, base 2%, multiplier 2×

```
STEP 1
- App shows: "Next Bet = $20.00 (2%)" ✓ AUTO
- You place $20 bet in your broker
- You LOSE
- Click "✗ Record Loss"
- App shows:
  | Step | Bet $ Amount | Bet %  | Win/Loss | P&L  | New Balance |
  |------|--------------|--------|----------|------|-------------|
  | 1    | 20.00        | 2.00%  | Loss     | -20  | 980         |
- Your balance is NOW $980 ✓ AUTO

STEP 2
- App shows: "Next Bet = $39.20 (4%)" ✓ AUTO (doubled from 2%)
- You place $39.20 bet
- You LOSE again
- Click "✗ Record Loss"
- App shows:
  | Step | Bet $ Amount | Bet %  | Win/Loss | P&L   | New Balance |
  |------|--------------|--------|----------|-------|-------------|
  | 1    | 20.00        | 2.00%  | Loss     | -20   | 980         |
  | 2    | 39.20        | 4.00%  | Loss     | -39.2 | 940.80      |
- Your balance is NOW $940.80 ✓ AUTO

STEP 3
- App shows: "Next Bet = $75.26 (8%)" ✓ AUTO (doubled from 4%)
- You place $75.26 bet
- You WIN!
- Click "✓ Record Win"
- App shows:
  | Step | Bet $ Amount | Bet %  | Win/Loss | P&L   | New Balance |
  |------|--------------|--------|----------|-------|-------------|
  | 1    | 20.00        | 2.00%  | Loss     | -20   | 980         |
  | 2    | 39.20        | 4.00%  | Loss     | -39.2 | 940.80      |
  | 3    | 75.26        | 8.00%  | Win      | +75.26| 1016.06     |
- Your balance is NOW $1016.06 ✓ AUTO
- SESSION ENDS (stops after every win)
- Next session starts fresh at 2%
```

## 🎯 What You MUST Do Manually

1. **Place the actual trade** in your broker/exchange (the app doesn't do this)
2. **Click "Record Win" or "Record Loss"** after your trade completes
3. **Initialize balance** at the start (click "Initialize")
4. **Start a session** before first trade (click "▶ Start Session")

## ⚙️ Settings (You Can Change)

- **Base %:** Start percentage (default 2%) - change before starting session
- **Multiplier:** Loss scaling (default 2×) - doubles on each loss, change before starting session

## 📈 Example with Different Settings

**Custom Settings:**
- Base %: 5% (instead of 2%)
- Multiplier: 3× (instead of 2×)

```
Same as above, but:
- Step 1: 5% × $1000 = $50 bet
- Step 2 (if loss): 15% × $950 = $142.50 bet (5% × 3)
- Step 3 (if loss): 45% × $807.50 = $363.375 bet (15% × 3)
```

## 💡 Key Points

✅ **The app automatically:**
- Calculates next bet amount
- Updates balance
- Doubles bet % on each loss
- Resets to base % after a win
- Ends session after wins
- Shows all history

❌ **You must:**
- Place actual trades (in your broker)
- Tell the app if you won or lost
- Initialize account balance
- Start sessions
- Manage risk (the app doesn't stop risky bets)

---

**Summary:** The Money Manager handles ALL calculations automatically. You just need to:
1. Click "📊 Next Bet" to see how much to trade
2. Place that trade in your broker
3. Click "✓ Win" or "✗ Loss" to tell the app what happened
4. Repeat!

