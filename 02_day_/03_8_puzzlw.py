def print_board(board):
    """
    Print the current state of the Tic-Tac-Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    """
    Check if there is a winner or the game is a draw.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check if the board is full (draw)
    for row in board:
        if " " in row:
            return None

    return "Draw"


def tic_tac_toe():
    """
    Main function to play the Tic-Tac-Toe game.
    """
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Get current player's move
        print(f"Player {players[current_player]}'s turn.")
        try:
            row, col = map(int, input("Enter row and column (0, 1, or 2) separated by a space: ").split())
            if board[row][col] != " ":
                print("That cell is already taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers (0, 1, or 2).")
            continue

        # Make the move
        board[row][col] = players[current_player]
        print_board(board)

        # Check for a winner
        result = check_winner(board)
        if result:
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"Player {result} wins!")
            break

        # Switch to the other player
        current_player = 1 - current_player


# Run the game
if __name__ == "__main__":
    tic_tac_toe()
