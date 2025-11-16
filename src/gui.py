"""Tkinter GUI for the Money Management App (percentage-based Martingale).

Run with:
  python -m src.gui

This GUI uses the existing `Account` class for persistence (`mm_account.json`).
"""
import tkinter as tk
from tkinter import ttk, messagebox
from decimal import Decimal
from money_manager.session import Account


class MoneyApp(tk.Tk):
    def __init__(self, data_file=None):
        super().__init__()
        self.title("Money Manager - Percentage Martingale")
        self.geometry("700x480")

        self.account = Account(data_file=data_file)

        # Controls
        frm = ttk.Frame(self)
        frm.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)

        # Balance display and init
        bal_row = ttk.Frame(frm)
        bal_row.pack(fill=tk.X, pady=4)
        ttk.Label(bal_row, text="Balance:").pack(side=tk.LEFT)
        self.balance_var = tk.StringVar(value=str(self.account.balance))
        self.balance_lbl = ttk.Label(bal_row, textvariable=self.balance_var, font=(None, 12, "bold"))
        self.balance_lbl.pack(side=tk.LEFT, padx=6)

        ttk.Label(bal_row, text="Init balance:").pack(side=tk.LEFT, padx=(20, 4))
        self.init_entry = ttk.Entry(bal_row, width=12)
        self.init_entry.pack(side=tk.LEFT)
        ttk.Button(bal_row, text="Init", command=self.on_init).pack(side=tk.LEFT, padx=6)

        # Session controls
        sess_row = ttk.Frame(frm)
        sess_row.pack(fill=tk.X, pady=4)
        ttk.Button(sess_row, text="Start Session", command=self.on_start_session).pack(side=tk.LEFT)
        ttk.Button(sess_row, text="End Session", command=self.on_end_session).pack(side=tk.LEFT, padx=6)

        # Bet controls
        bet_row = ttk.Frame(frm)
        bet_row.pack(fill=tk.X, pady=4)
        ttk.Label(bet_row, text="Base %:").pack(side=tk.LEFT)
        self.base_percent_var = tk.DoubleVar(value=0.02)
        ttk.Entry(bet_row, textvariable=self.base_percent_var, width=8).pack(side=tk.LEFT)
        ttk.Label(bet_row, text="Multiplier:").pack(side=tk.LEFT, padx=(10, 0))
        self.mult_var = tk.DoubleVar(value=2.0)
        ttk.Entry(bet_row, textvariable=self.mult_var, width=8).pack(side=tk.LEFT)

        ttk.Button(bet_row, text="Next Bet", command=self.on_next_bet).pack(side=tk.LEFT, padx=8)
        self.next_bet_var = tk.StringVar(value="-")
        ttk.Label(bet_row, textvariable=self.next_bet_var).pack(side=tk.LEFT)

        ttk.Button(bet_row, text="Record Win", command=self.on_record_win).pack(side=tk.RIGHT)
        ttk.Button(bet_row, text="Record Loss", command=self.on_record_loss).pack(side=tk.RIGHT, padx=6)

        # Session history
        hist_frame = ttk.LabelFrame(frm, text="Current Session Steps")
        hist_frame.pack(fill=tk.BOTH, expand=True, pady=8)

        columns = ("idx", "bet", "pct", "result", "pnl", "balance")
        self.tree = ttk.Treeview(hist_frame, columns=columns, show="headings")
        for c in columns:
            self.tree.heading(c, text=c)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Footer
        footer = ttk.Frame(frm)
        footer.pack(fill=tk.X, pady=6)
        ttk.Button(footer, text="Refresh", command=self.refresh).pack(side=tk.LEFT)
        ttk.Button(footer, text="Quit", command=self.quit).pack(side=tk.RIGHT)

        self.refresh()

    def on_init(self):
        try:
            val = float(self.init_entry.get())
        except Exception:
            messagebox.showerror("Invalid", "Please enter a valid number for initial balance.")
            return
        self.account.init_account(val)
        self.refresh()

    def on_start_session(self):
        try:
            sess = self.account.start_session()
            messagebox.showinfo("Session", f"Started session {sess.id} at {sess.start_balance}")
        except Exception as e:
            messagebox.showwarning("Start", str(e))
        self.refresh()

    def on_end_session(self):
        self.account.force_end_session()
        messagebox.showinfo("Session", "Session ended (if any)")
        self.refresh()

    def on_next_bet(self):
        info = self.account.get_next_bet(base_percent=self.base_percent_var.get(), multiplier=self.mult_var.get())
        self.next_bet_var.set(f"{info['bet_amount']} ({info['bet_percent']*100:.2f}% )")

    def _record(self, win: bool):
        # Ensure session exists
        if self.account.current_session is None:
            try:
                self.account.start_session()
            except Exception:
                pass

        info = self.account.get_next_bet(base_percent=self.base_percent_var.get(), multiplier=self.mult_var.get())
        bet_percent = info["bet_percent"]
        bet_amount = info["bet_amount"]

        if win:
            pnl = float(bet_amount)
        else:
            pnl = -float(bet_amount)

        try:
            step = self.account.record_result(bet_percent=bet_percent, bet_amount=bet_amount, pnl=pnl, result=("win" if win else "loss"))
            messagebox.showinfo("Recorded", f"Step {step.idx} recorded: {step.result} pnl={step.pnl} bal={step.balance_after}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

        self.refresh()

    def on_record_win(self):
        self._record(True)

    def on_record_loss(self):
        self._record(False)

    def refresh(self):
        # update balance
        self.balance_var.set(str(self.account.balance))

        # update session tree
        for i in self.tree.get_children():
            self.tree.delete(i)

        sess = self.account.current_session
        if sess:
            for st in sess.steps:
                self.tree.insert("", tk.END, values=(st.idx, f"{st.bet_amount}", f"{st.bet_percent*100:.2f}%", st.result, st.pnl, st.balance_after))


def main():
    app = MoneyApp()
    app.mainloop()


if __name__ == "__main__":
    main()
