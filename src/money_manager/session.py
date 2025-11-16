import json
import os
import uuid
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List, Optional, Dict


@dataclass
class Step:
    idx: int
    bet_percent: float
    bet_amount: float
    result: str  # 'win'|'loss'|'recorded'
    pnl: float
    balance_after: float
    timestamp: str


@dataclass
class Session:
    id: str
    start_balance: float
    active: bool
    steps: List[Step]
    created_at: str


class Account:
    def __init__(self, balance: float = 0.0, data_file: Optional[str] = None):
        self.balance = float(balance)
        self.data_file = data_file or os.path.join(os.getcwd(), "mm_account.json")
        self.sessions: List[Session] = []
        self.current_session: Optional[Session] = None

        # Try load existing
        if os.path.exists(self.data_file):
            try:
                self._load()
            except Exception:
                # ignore and start fresh
                pass

    def _load(self):
        with open(self.data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.balance = float(data.get("balance", self.balance))
        self.sessions = []
        for s in data.get("sessions", []):
            steps = [Step(**st) for st in s.get("steps", [])]
            sess = Session(id=s.get("id"), start_balance=s.get("start_balance"), active=s.get("active", False), steps=steps, created_at=s.get("created_at"))
            self.sessions.append(sess)
            if sess.active:
                self.current_session = sess

    def _save(self):
        data = {
            "balance": self.balance,
            "sessions": [
                {
                    "id": s.id,
                    "start_balance": s.start_balance,
                    "active": s.active,
                    "created_at": s.created_at,
                    "steps": [asdict(step) for step in s.steps],
                }
                for s in self.sessions
            ],
        }
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def init_account(self, balance: float):
        self.balance = float(balance)
        self.sessions = []
        self.current_session = None
        self._save()

    def start_session(self):
        if self.current_session is not None and self.current_session.active:
            raise RuntimeError("A session is already active")
        sess = Session(id=str(uuid.uuid4()), start_balance=self.balance, active=True, steps=[], created_at=datetime.utcnow().isoformat())
        self.sessions.append(sess)
        self.current_session = sess
        self._save()
        return sess

    def get_next_bet(self, base_percent: float = 0.02, multiplier: float = 2.0) -> Dict[str, float]:
        """Return next bet percentage and amount based on current session and account balance.

        - Start each session with `base_percent` of current balance.
        - On each loss, percentage *= multiplier.
        """
        if self.current_session is None or not self.current_session.active:
            # Not in a session: next session would start at base_percent
            pct = float(base_percent)
        else:
            # compute current pct based on previous steps
            if not self.current_session.steps:
                pct = float(base_percent)
            else:
                last = self.current_session.steps[-1]
                if last.result == "win":
                    pct = float(base_percent)
                else:
                    # last was a loss: double the last percentage
                    pct = float(last.bet_percent) * float(multiplier)

        bet_amount = round(self.balance * pct, 2)
        if bet_amount < 0.01:
            bet_amount = 0.01
        return {"bet_percent": pct, "bet_amount": bet_amount}

    def record_result(self, bet_percent: float, bet_amount: float, pnl: float, result: str):
        """Record a real outcome into current session and update balance.

        - `pnl` is positive for net profit, negative for net loss (already excluding stake if you prefer).
        - `result` should be 'win' or 'loss' or 'recorded'.
        """
        if self.current_session is None or not self.current_session.active:
            raise RuntimeError("No active session to record result")

        # Apply pnl (positive or negative)
        self.balance = round(self.balance + float(pnl), 2)

        step = Step(
            idx=len(self.current_session.steps) + 1,
            bet_percent=float(bet_percent),
            bet_amount=float(bet_amount),
            result=result,
            pnl=float(pnl),
            balance_after=self.balance,
            timestamp=datetime.utcnow().isoformat(),
        )
        self.current_session.steps.append(step)

        # If win, end session and reset
        if result == "win":
            self.current_session.active = False
            self.current_session = None

        # If balance <= 0, end session
        if self.balance <= 0:
            if self.current_session is not None:
                self.current_session.active = False
            self.current_session = None

        self._save()
        return step

    def force_end_session(self):
        if self.current_session:
            self.current_session.active = False
            self.current_session = None
            self._save()

    def status(self) -> Dict:
        s = None
        if self.current_session:
            s = {
                "id": self.current_session.id,
                "start_balance": self.current_session.start_balance,
                "steps": [asdict(st) for st in self.current_session.steps],
            }
        return {"balance": self.balance, "current_session": s}
