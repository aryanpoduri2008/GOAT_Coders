def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
            all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe(n=3):
    board = [[" " for _ in range(n)] for _ in range(n)]
    players = ["X", "O"]
    print("Welcome to Tic Tac Toe!")
    print("Player 1 is X, Player 2 is O")
    print_board(board)

    turn = 0
    while True:
        current_player = players[turn % 2]
        print(f"\nPlayer {turn % 2 + 1}'s turn ({current_player}):")
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input! Please enter numbers between 0 and 2.")
            continue

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current_player
            print_board(board)
            if is_winner(board, current_player):
                print(f"\nPlayer {turn % 2 + 1} ({current_player}) wins!")
                break
            if is_full(board):
                print("\nThe game is a draw!")
                break
            turn += 1
        else:
            print("Invalid move! Try again.")


tic_tac_toe()
