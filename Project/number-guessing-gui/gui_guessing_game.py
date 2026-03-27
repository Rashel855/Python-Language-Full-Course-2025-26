import tkinter as tk
import random


class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

        self.secret = random.randint(1, 100)
        self.attempts = 0
        self.best_score = None

        self.build_ui()

    # ---------- UI ----------
    def build_ui(self):
        title = tk.Label(
            self.root,
            text="🎯 Number Guessing Game",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=15)

        info = tk.Label(
            self.root,
            text="Guess a number between 1 and 100",
            font=("Arial", 11)
        )
        info.pack()

        self.entry = tk.Entry(
            self.root,
            font=("Arial", 16),
            justify="center"
        )
        self.entry.pack(pady=15, ipadx=10, ipady=5)
        self.entry.bind("<Return>", lambda event: self.check_guess())

        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12, "bold")
        )
        self.result_label.pack(pady=10)

        self.attempt_label = tk.Label(
            self.root,
            text="Attempts: 0",
            font=("Arial", 11)
        )
        self.attempt_label.pack()

        guess_btn = tk.Button(
            self.root,
            text="Guess",
            font=("Arial", 12),
            width=12,
            command=self.check_guess
        )
        guess_btn.pack(pady=8)

        reset_btn = tk.Button(
            self.root,
            text="New Game",
            font=("Arial", 11),
            width=12,
            command=self.new_game
        )
        reset_btn.pack(pady=5)

        self.best_label = tk.Label(
            self.root,
            text="Best Score: --",
            font=("Arial", 11)
        )
        self.best_label.pack(pady=10)

    # ---------- Game Logic ----------
    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="⚠ Enter a valid number", fg="red")
            return

        self.attempts += 1
        self.attempt_label.config(text=f"Attempts: {self.attempts}")

        if guess == self.secret:
            self.result_label.config(text="✅ Correct!", fg="green")

            if self.best_score is None or self.attempts < self.best_score:
                self.best_score = self.attempts
                self.best_label.config(text=f"Best Score: {self.best_score}")

        elif guess > self.secret:
            self.result_label.config(text="Too high!", fg="orange")
        else:
            self.result_label.config(text="Too low!", fg="orange")

        self.entry.delete(0, tk.END)

    def new_game(self):
        self.secret = random.randint(1, 100)
        self.attempts = 0
        self.attempt_label.config(text="Attempts: 0")
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)


# ---------- Run ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGame(root)
    root.mainloop()