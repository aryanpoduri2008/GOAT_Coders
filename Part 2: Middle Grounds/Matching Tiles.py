import random


def generate_board(size=4):
    num_pairs = (size * size) // 2
    tiles = list(range(1, num_pairs + 1)) * 2
    random.shuffle(tiles)

    # Create a 2D board
    board = []
    tiles_idx = 0
    for i in range(size):
        board.append([])
        for j in range(size):
            board.append(tiles[tiles_idx])
            tiles_idx += 1
    return board


def print_board(board, revealed):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if revealed[i][j]:
                print(f"{board[i][j]:2}", end=" ")
            else:
                print(" *", end=" ")  # Hidden tiles
        print()


def is_complete(revealed):
    return all(all(row) for row in revealed)


def matching_tiles_game():
    print("Welcome to the Matching Tiles Game!")
    size = 4  # Default size (4x4)
    board = generate_board(size)
    revealed = [[False] * size for _ in range(size)]

    moves = 0
    while not is_complete(revealed):
        print_board(board, revealed)

        # Get first tile
        try:
            row1 = int(input("Enter the row of the first tile (0 - 3): "))
            col1 = int(input("Enter the column of the first tile (0 - 3): "))
            if revealed[row1][col1]:
                print("Tile already matched! Choose a different tile.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter numbers between 0 and 3.")
            continue

        # Reveal first tile temporarily
        revealed[row1][col1] = True
        print_board(board, revealed)

        # Get second tile
        try:
            row2 = int(input("Enter the row of the second tile (0 - 3): "))
            col2 = int(input("Enter the column of the second tile (0 - 3): "))
            if (row1, col1) == (row2, col2) or revealed[row2][col2]:
                print("Invalid choice! Can't pick the same or already matched tile.")
                revealed[row1][col1] = False
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter numbers between 0 and 3.")
            revealed[row1][col1] = False
            continue

        # Reveal second tile temporarily
        revealed[row2][col2] = True
        print_board(board, revealed)
        moves += 1

        # Check if tiles match
        if board[row1][col1] == board[row2][col2]:
            print("Match found!")
        else:
            print("No match. Try again.")
            revealed[row1][col1] = False
            revealed[row2][col2] = False

    print(f"Congratulations! You matched all tiles in {moves} moves!")


matching_tiles_game()
