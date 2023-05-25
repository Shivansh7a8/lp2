# Graph class to represent the undirected graph
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self, start):
        visited = set()  # set to keep track of visited vertices
        self._dfs_recursive(start, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')  # Process the current vertex
        
        # Visit all adjacent vertices
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)
# Create a graph
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)

# Perform DFS starting from vertex 0
print("Depth-First Traversal (starting from vertex 0):")
graph.dfs(0)