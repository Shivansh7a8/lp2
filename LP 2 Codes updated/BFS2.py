from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex)  # Or perform any other operation on the vertex

        for neighbor in graph[vertex]:
            neighbor = int(neighbor)  # Convert the neighbor to an integer
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3:[1], 4:[1], 5:[2]}
bfs(graph, 0)
