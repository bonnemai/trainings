def solveNQueens(n):
    board = [-1] * n
    solutions = []

    def is_valid(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row=0):
        if row == n:
            # build board representation
            sol = []
            for r in range(n):
                line = "." * board[r] + "Q" + "." * (n - board[r] - 1)
                sol.append(line)
            solutions.append(sol)
            return

        for col in range(n):
            if is_valid(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # backtrack

    backtrack()
    return solutions

print(len(solveNQueens(8)))  # 92 solutions
print(solveNQueens(8))  # 92 solutions