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

def DFS(G,start,goal):
    stack=[]
    visited=set()
    prev={}

    stack.append(start)
    print(stack)
    prev['Biratnagar']=' '
    print(prev)

    while stack:
        poppedstate=stack.pop()
        visited.add(poppedstate)
        
        if poppedstate==goal:
            return True,prev
        
        else:
            for chimeki in G[poppedstate]:
                if chimeki  not in visited and chimeki  not in stack:
                    stack.append(chimeki)
                    prev[chimeki]=poppedstate
    return False, prev

def reconstruct_path(G, previous, goal):
    path = goal
    while previous[goal] != " ":
        path = previous[goal] + "->" + path
        goal = previous[goal]
    return path

start='Biratnagar'
goal='Damak'
flag,prev=DFS(G,start,goal)
if flag==1:
    print("path found")
    pprint.pprint(prev)
    print("----------------")
    path = reconstruct_path(G,prev, goal)
    print(path)
else:
    print("Goal not found")