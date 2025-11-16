from money_manager.session import Account
import os


def test_session_flow(tmp_path):
    data_file = tmp_path / "acct.json"
    acct = Account(balance=1000, data_file=str(data_file))
    acct.init_account(1000)
    sess = acct.start_session()
    nxt = acct.get_next_bet()
    assert round(nxt["bet_amount"], 2) == round(1000 * 0.02, 2)
    # record a loss
    step1 = acct.record_result(bet_percent=nxt["bet_percent"], bet_amount=nxt["bet_amount"], pnl=-nxt["bet_amount"], result="loss")
    assert acct.balance == 1000 - nxt["bet_amount"]
    nxt2 = acct.get_next_bet()
    # next percent should be doubled
    assert round(nxt2["bet_percent"], 10) == round(nxt["bet_percent"] * 2, 10)
