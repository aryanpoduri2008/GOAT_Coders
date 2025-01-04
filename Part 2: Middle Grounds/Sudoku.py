import random


def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 23)
        for j, value in enumerate(row):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(f"{value if value != 0 else '.'} ", end="")
        print()


def is_valid_move(board, row, col, num):
    # Check the row
    if num in board[row]:
        return False
    # Check the column
    if num in [board[i][col] for i in range(9)]:
        return False
    # Check the 3x3 box
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for i in range(box_row_start, box_row_start + 3):
        for j in range(box_col_start, box_col_start + 3):
            if board[i][j] == num:
                return False
    return True


def is_complete(board):
    return all(0 not in row for row in board)


def generate_puzzle():
    board = [[0] * 9 for _ in range(9)]
    for _ in range(15):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while not is_valid_move(board, row, col, num) or board[row][col] != 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
        board[row][col] = num
    return board


def sudoku():
    board = generate_puzzle()
    print("Welcome to Sudoku! Fill the grid with numbers (1-9).")
    print_board(board)

    while not is_complete(board):
        try:
            row = int(input("Enter row (0 - 8): "))
            col = int(input("Enter column (0 - 8): "))
            num = int(input("Enter number (1 - 9): "))

            if row < 0 or row >= 9 or col < 0 or col >= 9 or num < 1 or num > 9:
                print("Invalid input! Enter row/column in 0 - 8 and number in 1 - 9.")
                continue

            if board[row][col] != 0:
                print("Cell is already filled! Try another.")
            elif is_valid_move(board, row, col, num):
                board[row][col] = num
                print("Move accepted!")
            else:
                print("Invalid move! Try again.")
            print_board(board)

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    print("Congratulations, you've completed the Sudoku!")


sudoku()
