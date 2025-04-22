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

def DFS(G, Start, goal):
    stack = []
    prev = {}
    visited = set()

    stack.append(Start)
    prev[Start] = ' ' 

    while stack:
        poppedState = stack.pop()
        visited.add(poppedState)

        if poppedState == goal:
            return True, prev
        for chimeki in G[poppedState]:
            if chimeki not in stack and chimeki not in visited:
                stack.append(chimeki)
                prev[chimeki] = poppedState

    return False, prev

def reconstruct_path(G, previous, goal):
    path = goal
    while previous[goal] != " ":
        path = previous[goal] + "->" + path
        goal = previous[goal]
    return path

start = "Biratnagar"
goal = "Damak"

value, previous = DFS(G, start, goal)

if value:
    print("Goal found")
    pprint.pprint(previous)
    print("----------------")
    path = reconstruct_path(G, previous, goal)
    print(path)
else:
    print("Goal not found")
