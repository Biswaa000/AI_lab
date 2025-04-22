from queue import PriorityQueue

class Puzzle:
    def __init__(self, board, g_score, parent=None):
        self.board = board
        self.g_score = g_score  # Cost to reach the current state
        self.parent = parent    # Parent state for path reconstruction

    def __lt__(self, other):
        return (self.g_score + self.h_score()) < (other.g_score + other.h_score())

    def h_score(self):
        """
        Heuristic function (Manhattan Distance) to estimate cost to goal.
        """
        goal = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        dist = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:  # Skip the blank tile
                    x, y = divmod(self.board[i][j] - 1, 3)  # Goal position
                    dist += abs(i - x) + abs(j - y)
        return dist

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
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:  # Check boundaries
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                neighbors.append(Puzzle(new_board, self.g_score + 1, self))
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


def a_star(initial_board):
    """
    Solve the 8 Puzzle using A* Search Algorithm.
    """
    initial_state = Puzzle(initial_board, 0)
    pq = PriorityQueue()
    pq.put(initial_state)
    visited = set()

    while not pq.empty():
        current = pq.get()

        # Convert the board into a tuple (immutable) for visited tracking
        board_tuple = tuple(tuple(row) for row in current.board)
        if board_tuple in visited:
            continue
        visited.add(board_tuple)

        # Check if goal state is reached
        if current.is_goal():
            return current

        # Explore neighbors
        for neighbor in current.get_neighbors():
            neighbor_tuple = tuple(tuple(row) for row in neighbor.board)
            if neighbor_tuple not in visited:
                pq.put(neighbor)

    return None


def reconstruct_path(goal_state):
    """
    Reconstruct the path from the initial state to the goal state.
    """
    path = []
    current = goal_state
    while current is not None:
        path.append(current)
        current = current.parent
    return path[::-1]


# Example usage
if __name__ == "__main__":
    initial_board = [
        [2, 8, 3],
        [1, 6, 4],
        [7, 0, 5]
    ]

    print("Initial Board:")
    print(Puzzle(initial_board, 0))

    goal_state = a_star(initial_board)
    if goal_state:
        print("\nGoal Found! Solution Path:")
        solution_path = reconstruct_path(goal_state)
        for step, state in enumerate(solution_path):
            print(f"\nStep {step}:")
            print(state)
        print(f"\nTotal Steps: {len(solution_path) - 1}")
    else:
        print("\nNo solution found!")
