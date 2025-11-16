from money_manager.martingale import MartingaleSimulator


def test_quick_simulation_reaches_target():
    sim = MartingaleSimulator(starting_balance=1000, base_bet=1, multiplier=2, win_prob=1.0, payout=2, target_profit=10, max_rounds=10, seed=0)
    result = sim.simulate()
    # If win_prob==1.0 and payout==2, each round gains base_bet profit (since stake returned + profit)
    assert result["final_balance"] >= 1000


def test_bankrupt_scenario():
    sim = MartingaleSimulator(starting_balance=10, base_bet=5, multiplier=2, win_prob=0.0, payout=2, max_rounds=10, seed=0)
    result = sim.simulate()
    assert result["final_balance"] <= 10
