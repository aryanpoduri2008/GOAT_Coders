def solve_n_queens(n):
    board = [-1] * n  # Using a 1D array to store column positions
    solutions = []
    place_queens(board, 0, n, solutions)
    return solutions


def place_queens(board, row, n, solutions):
    if row == n:
        solutions.append(create_board(board, n))
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            place_queens(board, row + 1, n, solutions)
            board[row] = -1  # Backtrack


def is_safe(board, row, col):
    for r in range(row):
        c = board[r]
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def create_board(board, n):
    solved_board = []
    for r in range(n):
        solved_board.append("")
        for c in range(n):
            if board[r] == c:
                solved_board[r] += "Q"
            else:
                solved_board[r] += "."
    return solved_board
    # return ["".join("Q" if board[r] == c else "." for c in range(n)) for r in range(n)]


# Example usage
n = 8
solutions = solve_n_queens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()
