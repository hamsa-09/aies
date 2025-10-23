import numpy as np
import matplotlib.pyplot as plt

def solve(n, col=0, board=None, res=None):
    if board is None:
        board = np.zeros((n, n), int)
        res = []
    if col == n:
        res.append(board.copy())
        return res
    for r in range(n):
        if (board[r][:col] == 0).all() and \
           all(board[r-i][col-i] == 0 for i in range(1, min(r, col) + 1)) and \
           all(board[r+i][col-i] == 0 for i in range(1, min(n-1-r, col) + 1)):  # <-- fixed here
            board[r][col] = 1
            solve(n, col + 1, board, res)
            board[r][col] = 0
    return res

def show(sol, n, i):
    plt.imshow(np.add.outer(range(n), range(n)) % 2, cmap="gray")
    for r in range(n):
        for c in range(n):
            if sol[r][c]:
                plt.text(c, r, "♛", ha="center", va="center", fontsize=28, color="red")
    plt.title(f"Solution {i+1} (n={n})"); plt.axis("off"); plt.show()

try:
    n = int(input("Enter n (1–9): "))
    if not 1 <= n <= 9:
        raise ValueError
except ValueError:
    print("Please enter an integer between 1 and 9.")
    raise SystemExit

S = solve(n)
print(f"{len(S)} solutions found")
for i, s in enumerate(S): show(s, n, i)
