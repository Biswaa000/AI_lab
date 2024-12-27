
graph = {
    "Biratnagar": {"Itahari": 22, "Rangeli": 25},
    "Itahari": {"Biratnagar": 22, "Biratchowk": 30, "Dharan": 20},
    "Biratchowk": {"Itahari": 30, "Kanepokhari": 10},
    "Dharan": {"Itahari": 20},
    "Rangeli": {"Biratnagar": 25, "Kanepokhari": 25},
    "Kanepokhari": {"Rangeli": 25, "Biratchowk": 10, "Urlabari": 12},
    "Urlabari": {"Kanepokhari": 12, "Damak": 6},
    "Damak": {"Urlabari": 6}
}

def display_graph(graph):
    for city, connections in graph.items():
        print(f"{city}: {connections}")

display_graph(graph)
