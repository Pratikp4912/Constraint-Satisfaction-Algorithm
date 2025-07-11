import tkinter as tk
from itertools import permutations
import re

def solve():
    expr = entry.get().replace(" ", "")
    words = re.findall(r'[A-Z]+', expr.upper())
    unique_letters = sorted(set(''.join(words)))
    if len(unique_letters) > 10:
        result.set("Too many letters (max 10)!")
        return

    for perm in permutations(range(10), len(unique_letters)):
        table = dict(zip(unique_letters, perm))
        if any(table[w[0]] == 0 for w in words):  # no leading zero
            continue
        equation = expr
        for k, v in table.items():
            equation = equation.replace(k, str(v))
        if eval(equation):
            result.set(equation)
            return
    result.set("No solution found.")

root = tk.Tk()
root.title("Cryptarithmetic Solver")

tk.Label(root, text="Enter Equation (e.g., SEND + MORE == MONEY):").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack()

tk.Button(root, text="Solve", command=solve).pack(pady=10)
result = tk.StringVar()
tk.Label(root, textvariable=result, font=('Arial', 14), fg='green').pack()

root.mainloop()
