from queue import PriorityQueue
import pprint

G = {
    "Biratnagar": {"Itahari": 22, "Rangeli": 25},
    "Itahari": {"Biratnagar": 22, "Biratchowk": 11, "Dharan": 20},
    "Biratchowk": {"Itahari": 11, "Kanepokhari": 10, "Biratnagar": 30},
    "Dharan": {"Itahari": 20},
    "Rangeli": {"Biratnagar": 25, "Kanepokhari": 25, "Urlabari": 40},
    "Kanepokhari": {"Rangeli": 25, "Biratchowk": 10, "Urlabari": 12},
    "Urlabari": {"Kanepokhari": 12, "Damak": 6, "Rangeli": 40},
    "Damak": {"Urlabari": 6}
}

h = {
    "Biratnagar": 46,
    "Itahari": 39,
    "Dharan": 41,
    "Rangeli": 28,
    "Biratchowk": 29,
    "Kanepokhari": 17,
    "Urlabari": 6,
    "Damak": 0
}

def aStar(G, h, start, goal):
    PQ = PriorityQueue()
    prev =dict()
    visited = set()

    # Enqueue the starting state into the priority queue
    PQ.put((0 + h[start], (start, 0)))
    prev[start] = " "

    while not PQ.empty():
        outStateFScore, outStateInfo = PQ.get()
        outState, outStateGScore = outStateInfo

        # Add the current state to the visited set
        if outState in visited:
            continue
        visited.add(outState)

        # Check if we reached the goal
        if outState == goal:
            return True, prev, outStateGScore

        # Explore neighbors
        for chimeki in G[outState]:
            if chimeki not in visited:
                chimekiGScore = outStateGScore + G[outState][chimeki]
                PQ.put((chimekiGScore + h[chimeki], (chimeki, chimekiGScore)))
                prev[chimeki] = outState

    return False, prev

def reconstruct_path(G, previous, goal):
    path = goal
    while previous[goal] != " ":
        path = previous[goal] + "->" + path
        goal = previous[goal]
    return path

start = "Biratnagar"
goal = "Damak"

value, previous, cost = aStar(G, h, start, goal)

if value:
    print("Goal found")
    pprint.pprint(previous)
    print("----------------")
    path = reconstruct_path(G, previous, goal)
    print("Path:", path)
    print("Total cost:", cost)
else:
    print("Goal not found")
