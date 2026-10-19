# Kruskal's Algorithm to find Minimum Spanning Tree

# Disjoint Set Union (DSU) / Union-Find
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    # Find parent with path compression
    def findParent(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    # Union by rank
    def unionSets(self, u, v):
        rootU = self.findParent(u)
        rootV = self.findParent(v)

        # If both have the same parent, a cycle would form
        if rootU == rootV:
            return False

        # Union by rank
        if self.rank[rootU] < self.rank[rootV]:
            self.parent[rootU] = rootV

        elif self.rank[rootU] > self.rank[rootV]:
            self.parent[rootV] = rootU

        else:
            self.parent[rootV] = rootU
            self.rank[rootU] += 1

        return True


def kruskalsMST(V, edges):
    # Step 1: Sort edges by weight
    edges.sort(key=lambda edge: edge[2])

    dsu = DisjointSet(V)
    mst = []
    mstWeight = 0

    # Step 2: Select edges that do not form cycles
    for edge in edges:
        src, dest, weight = edge

        if dsu.unionSets(src, dest):
            mst.append(edge)
            mstWeight += weight

        # MST contains V - 1 edges
        if len(mst) == V - 1:
            break

    # Print the resulting MST
    print("Edges in the Minimum Spanning Tree:")

    for edge in mst:
        print(edge[0], "--", edge[1], "==", edge[2])

    print("Total Weight of Minimum Spanning Tree:", mstWeight)
     


def main():
    V = 6

    # Edges: (source, destination, weight)
    edges = [
        (0, 1, 4),
        (0, 2, 4),
        (1, 2, 2),
        (2, 3, 3),
        (2, 5, 2),
        (2, 4, 4),
        (3, 4, 3),
        (5, 4, 3)
    ]

    kruskalsMST(V, edges)


if __name__ == "__main__":
    main()
print(92460118292)
