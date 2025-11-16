import random
from dataclasses import dataclass
from typing import List, Dict, Optional


@dataclass
class StepResult:
    round: int
    bet: float
    outcome: str
    balance: float


class MartingaleSimulator:
    """A simple Martingale-style simulator.

    Rules used here:
    - Start with `starting_balance` and a `base_bet`.
    - On each round place `current_bet` (initially base_bet).
    - Win probability is `win_prob`. On win, player receives `payout` times the stake (including stake).
    - On win: balance increases by bet*(payout-1) and `current_bet` resets to `base_bet`.
    - On loss: lose stake from balance, then `current_bet` *= multiplier.
    - Stop when target profit reached, bankrupt, max rounds reached, or a bet exceeds `max_bet`.
    """

    def __init__(
        self,
        starting_balance: float = 1000.0,
        base_bet: float = 1.0,
        multiplier: float = 2.0,
        win_prob: float = 0.5,
        payout: float = 2.0,
        target_profit: Optional[float] = None,
        max_bet: Optional[float] = None,
        max_rounds: int = 10000,
        seed: Optional[int] = None,
    ):
        self.starting_balance = float(starting_balance)
        self.base_bet = float(base_bet)
        self.multiplier = float(multiplier)
        self.win_prob = float(win_prob)
        self.payout = float(payout)
        self.target_profit = None if target_profit is None else float(target_profit)
        self.max_bet = None if max_bet is None else float(max_bet)
        self.max_rounds = int(max_rounds)
        self.seed = seed
        if seed is not None:
            random.seed(seed)

    def simulate(self) -> Dict:
        balance = float(self.starting_balance)
        current_bet = float(self.base_bet)
        rounds = 0
        history: List[StepResult] = []

        while rounds < self.max_rounds:
            rounds += 1

            # Check bet affordability and max_bet
            if current_bet > balance:
                history.append(StepResult(rounds, current_bet, "bankrupt", balance))
                break
            if self.max_bet is not None and current_bet > self.max_bet:
                history.append(StepResult(rounds, current_bet, "max_bet_exceeded", balance))
                break

            # Place the bet: subtract stake first
            balance -= current_bet

            # Determine outcome
            win = random.random() < self.win_prob
            if win:
                profit = current_bet * (self.payout - 1.0)
                balance += current_bet + profit  # receive stake + profit
                # Note: we subtracted the stake already; adding stake+profit yields net profit added
                outcome = "win"
                current_bet = float(self.base_bet)
            else:
                # lost stake already removed
                outcome = "loss"
                current_bet = current_bet * self.multiplier

            history.append(StepResult(rounds, float(current_bet if outcome == "win" else current_bet / (self.multiplier if outcome=="loss" else 1)), outcome, balance))

            # Check target profit
            if self.target_profit is not None:
                if balance - self.starting_balance >= self.target_profit:
                    break

            # If balance is zero or negative, stop
            if balance <= 0:
                break

        return {
            "starting_balance": self.starting_balance,
            "final_balance": balance,
            "rounds": rounds,
            "history": [r.__dict__ for r in history],
        }


def quick_simulation_example():
    sim = MartingaleSimulator(starting_balance=1000, base_bet=1, multiplier=2, win_prob=0.48, payout=2, target_profit=50, max_rounds=1000, seed=42)
    return sim.simulate()

if __name__ == "__main__":
    print(quick_simulation_example())
