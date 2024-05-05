

def DFS(graph: dict[str, list[str]], current: str, visited: list[str]):
    print(current)
    visited.append(current)
    queue = [item for item in graph[current] if item not in visited]
    while len(queue) > 0:
        _next = queue.pop(0)
        visited = DFS(graph, _next, visited)
        queue = [item for item in queue if item not in visited]
    return visited


def BFS(graph, start, end) -> int:  # BFS
    queue = [*graph[start]]
    visited = [start]
    path_length = 1
    while len(queue) > 0:
        current = queue.pop(0)
        visited.append(current)
        if current == end:
            return path_length
        _next = [item for item in graph[current] if item not in visited]
        queue = [*queue, *_next]
        path_length += 1

    return -1


def main_alt():
    graph = {
        "Sam": ["Soo Jin"],
        "Soo Jin": ["Sam",  "Tony"],
        "Tony": ["Sasuke"],
        "Sasuke": ["Naruto"],
        "Naruto": ["Sasuke", "Dokoro-chan"],
        "Dokoro-chan": ["Sasuke"]
    }

    x = BFS(graph, "Sam", "Dokoro-chan")
    print(x)
    x = BFS(graph, "Dokoro-chan", "Sam")
    print(x)
    print('-------')
    DFS(graph, "Dokoro-chan", [])


if __name__ == "__main__":
    main_alt()
