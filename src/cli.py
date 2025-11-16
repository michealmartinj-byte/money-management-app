"""Simple CLI for running the Martingale simulator."""
import argparse
import json
from money_manager.martingale import MartingaleSimulator


def parse_args():
    p = argparse.ArgumentParser(description="Martingale simulator CLI")
    p.add_argument("--balance", type=float, default=1000.0, help="Starting balance")
    p.add_argument("--base-bet", type=float, default=1.0, help="Base bet size")
    p.add_argument("--multiplier", type=float, default=2.0, help="Martingale multiplier")
    p.add_argument("--win-prob", type=float, default=0.5, help="Win probability per round")
    p.add_argument("--payout", type=float, default=2.0, help="Payout multiplier on win (including stake)")
    p.add_argument("--target-profit", type=float, default=None, help="Target profit to stop the simulation")
    p.add_argument("--max-bet", type=float, default=None, help="Maximum bet allowed")
    p.add_argument("--max-rounds", type=int, default=10000, help="Maximum simulation rounds")
    p.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility")
    return p.parse_args()


def main():
    args = parse_args()
    sim = MartingaleSimulator(
        starting_balance=args.balance,
        base_bet=args.base_bet,
        multiplier=args.multiplier,
        win_prob=args.win_prob,
        payout=args.payout,
        target_profit=args.target_profit,
        max_bet=args.max_bet,
        max_rounds=args.max_rounds,
        seed=args.seed,
    )
    result = sim.simulate()
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
