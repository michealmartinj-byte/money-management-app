"""CLI app for daily money tracking with percentage-based Martingale progression."""
import argparse
from pathlib import Path
from money_manager.session import Account


def get_data_file():
    # place account file next to project root
    return str(Path.cwd() / "mm_account.json")


def cmd_init(args):
    acct = Account(data_file=get_data_file())
    acct.init_account(args.balance)
    print(f"Initialized account with balance: {acct.balance}")


def cmd_status(args):
    acct = Account(data_file=get_data_file())
    s = acct.status()
    print(f"Balance: {s['balance']}")
    if s["current_session"]:
        print(f"Active session id: {s['current_session']['id']}")
        print("Steps:")
        for st in s["current_session"]["steps"]:
            print(f"  {st['idx']}: bet {st['bet_amount']} ({st['bet_percent']*100:.2f}%) -> {st['result']} pnl={st['pnl']} bal={st['balance_after']}")
    else:
        print("No active session")


def cmd_start(args):
    acct = Account(data_file=get_data_file())
    sess = acct.start_session()
    print(f"Started session {sess.id} at balance {sess.start_balance}")


def cmd_next(args):
    acct = Account(data_file=get_data_file())
    info = acct.get_next_bet(base_percent=args.base_percent, multiplier=args.multiplier)
    print(f"Next bet: {info['bet_amount']} ({info['bet_percent']*100:.2f}% of balance {acct.balance})")


def cmd_record(args):
    acct = Account(data_file=get_data_file())
    # Determine next bet if not provided
    if args.bet_percent is None or args.bet_amount is None:
        info = acct.get_next_bet(base_percent=args.base_percent, multiplier=args.multiplier)
        bet_percent = info["bet_percent"]
        bet_amount = info["bet_amount"]
    else:
        bet_percent = args.bet_percent
        bet_amount = args.bet_amount

    # If user provided pnl use that, otherwise infer from win/loss assuming even payout
    if args.pnl is not None:
        pnl = args.pnl
    else:
        # assume win -> profit = bet_amount (1:1), loss -> profit = -bet_amount
        if args.win:
            pnl = float(bet_amount)
        else:
            pnl = -float(bet_amount)

    result = "win" if args.win else "loss"
    step = acct.record_result(bet_percent=bet_percent, bet_amount=bet_amount, pnl=pnl, result=result)
    print(f"Recorded step {step.idx}: {result} pnl={step.pnl} balance={step.balance_after}")


def build_parser():
    p = argparse.ArgumentParser(description="Money management app (percentage martingale)")
    sub = p.add_subparsers(dest="cmd")

    init = sub.add_parser("init")
    init.add_argument("balance", type=float, help="Initial balance (e.g., 1000)")
    init.set_defaults(func=cmd_init)

    status = sub.add_parser("status")
    status.set_defaults(func=cmd_status)

    start = sub.add_parser("start")
    start.set_defaults(func=cmd_start)

    nxt = sub.add_parser("next")
    nxt.add_argument("--base-percent", type=float, default=0.02)
    nxt.add_argument("--multiplier", type=float, default=2.0)
    nxt.set_defaults(func=cmd_next)

    record = sub.add_parser("record")
    record.add_argument("--win", action="store_true", help="Mark this bet as a win (default payout 1:1 unless --pnl provided)")
    record.add_argument("--pnl", type=float, default=None, help="Specify exact PnL for this bet (positive for win, negative for loss)")
    record.add_argument("--bet-percent", type=float, default=None, help="Bet percent used (overrides computation)")
    record.add_argument("--bet-amount", type=float, default=None, help="Bet amount used (overrides computation)")
    record.add_argument("--base-percent", type=float, default=0.02)
    record.add_argument("--multiplier", type=float, default=2.0)
    record.set_defaults(func=cmd_record)

    return p


def main():
    p = build_parser()
    args = p.parse_args()
    if not hasattr(args, "func"):
        p.print_help()
        return
    args.func(args)


if __name__ == "__main__":
    main()
