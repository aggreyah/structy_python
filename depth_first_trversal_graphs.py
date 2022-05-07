def depth_first_print(a_graph, start):
    if graph is None or not a_graph:
        return []
    stack = [start]
    while stack:
        current = stack.pop(0)
        print(current)
        for item in a_graph[current]:
            stack.append(item)


def depth_first_print_recursive(a_graph, current):
    print(current)
    for neighbor in a_graph[current]:
        depth_first_print_recursive(a_graph, neighbor)


if __name__ == "__main__":
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": []
    }
    depth_first_print_recursive(graph, "a")
