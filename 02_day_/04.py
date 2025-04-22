class Puzzle:
    def __init__(self, board, parent=None, move=""):
        self.board = board
        self.parent = parent  # Parent state for path reconstruction
        self.move = move  # The move that led to this state

    def is_goal(self):
        """
        Check if the current board matches the goal state.
        """
        return self.board == [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]

    def get_neighbors(self):
        """
        Generate all valid neighboring states.
        """
        neighbors = []
        x, y = self.find_blank()
        moves = {
            "Up": (x - 1, y),
            "Down": (x + 1, y),
            "Left": (x, y - 1),
            "Right": (x, y + 1),
        }
        for move, (nx, ny) in moves.items():
            if 0 <= nx < 3 and 0 <= ny < 3:  # Check boundaries
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                neighbors.append(Puzzle(new_board, self, move))
        return neighbors

    def find_blank(self):
        """
        Locate the blank tile (0) in the board.
        """
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def __str__(self):
        """
        Represent the board as a string for easy visualization.
        """
        return "\n".join([" ".join(map(str, row)) for row in self.board])


def dfs(initial_board):
    """
    Solve the 8 Puzzle using Depth-First Search.
    """
    initial_state = Puzzle(initial_board)
    stack = [initial_state]
    visited = set()

    while stack:
        current = stack.pop()

        # Convert the board into a tuple (immutable) for visited tracking
        board_tuple = tuple(tuple(row) for row in current.board)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)

        # Check if goal state is reached
        if current.is_goal():
            return current

        # Add neighbors to the stack
        for neighbor in current.get_neighbors():
            neighbor_tuple = tuple(tuple(row) for row in neighbor.board)
            if neighbor_tuple not in visited:
                stack.append(neighbor)

    return None


def reconstruct_path(goal_state):
    """
    Reconstruct the path from the initial state to the goal state.
    """
    path = []
    current = goal_state
    while current.parent is not None:
        path.append((current.move, current.board))
        current = current.parent
    path.reverse()
    return path


# Example usage
if __name__ == "__main__":
    initial_board = [
        [2, 8, 3],
        [1, 6, 4],
        [7, 0, 5]
    ]

    print("Initial Board:")
    print(Puzzle(initial_board))

    goal_state = dfs(initial_board)
    if goal_state:
        print("\nGoal Found! Solution Path:")
        solution_path = reconstruct_path(goal_state)
        for step, (move, board) in enumerate(solution_path, 1):
            print(f"\nStep {step}: Move {move}")
            print(Puzzle(board))
        print("\nFinal Goal State:")
        print(goal_state)
    else:
        print("\nNo solution found!")
