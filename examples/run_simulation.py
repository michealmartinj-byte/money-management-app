"""Example runner for the simulator."""
from money_manager.martingale import MartingaleSimulator


def run():
    sim = MartingaleSimulator(starting_balance=1000, base_bet=1, multiplier=2, win_prob=0.48, payout=2, target_profit=50, max_rounds=1000, seed=1)
    res = sim.simulate()
    print(f"Started: {res['starting_balance']}")
    print(f"Final: {res['final_balance']}")
    print(f"Rounds: {res['rounds']}")


if __name__ == "__main__":
    run()
