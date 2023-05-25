class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append([src, dest, weight])

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def kruskal(self):
        self.graph = sorted(self.graph, key=lambda x: x[2])  # Sort edges by weight
        parent = [i for i in range(self.V)]  # Initialize parent array for union-find
        mst = []

        for edge in self.graph:
            src, dest, weight = edge
            parent_src = self.find_parent(parent, src)
            parent_dest = self.find_parent(parent, dest)

            if parent_src != parent_dest:  # Check if including the edge creates a cycle
                mst.append(edge)
                parent[parent_src] = parent_dest  # Perform union operation

        return mst
g = Graph(6)
g.add_edge(0, 1, 2)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 7)
g.add_edge(2, 4, 3)
g.add_edge(3, 4, 2)
g.add_edge(3, 5, 1)
g.add_edge(4, 5, 5)

mst = g.kruskal()
for edge in mst:
    print(f"Source: {edge[0]}, Destination: {edge[1]}, Weight: {edge[2]}")
