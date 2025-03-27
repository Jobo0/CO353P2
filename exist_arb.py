from collections import defaultdict
import heapq
# Main Script - Fetch Inputs, do outputs from here. Run directly. 

class Graph:
    def __init__(self, vertices, edge_count):
        self.vertices = vertices
        self.edges = defaultdict(list)
        self.edge_count = edge_count
    
    def add_edge(self, u, v):
        self.edges[u].append(v)
    
    def dfs(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.edges[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(v)
    
    def transpose(self):
        # reversed edges - for Kosaraju SCC find
        transposed_graph = Graph(self.vertices, self.edge_count)
        for node in self.edges:
            for neighbor in self.edges[node]:
                transposed_graph.add_edge(neighbor, node)
        return transposed_graph
    
    def dfs_util(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for neighbor in self.edges[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited, component)
    
    def find_sccs(self):
        # Kosaraju implementation for SCC's O(m + n)
        stack = []
        visited = [False] * self.vertices

        for i in range(self.vertices):
            if not visited[i]:
                self.dfs(i, visited, stack)
        
        transposed_graph = self.transpose()

        visited = [False] * self.vertices
        sccs = []

        while stack:
            node = stack.pop()
            if not visited[node]:
                component = []
                transposed_graph.dfs_util(node, visited, component)
                sccs.append(component)
        
        return sccs
    
    def arb_exist(self):
        if not (self.vertices > self.edge_count - 1): 
            return False # graph cannot be connected

        sccs = self.find_sccs() # O(n + m) = O(m)
        scc_index = {node: i for i, scc in enumerate(sccs) for node in scc}
        in_degree = [0] * len(sccs)

        for u in self.edges:
            for v in self.edges[u]:
                if scc_index[u] != scc_index[v]:
                    in_degree[scc_index[v]] += 1
        
        return in_degree.count(0) == 1 # only 1 scc has in-degree 0


def main():
    # Use Kosaraju algorithm for SCC, determine if only one SCC has in-degree 0
    # implies from arbitrary node in this SCC, all nodes are reachable (arborescence existence)

    n, m = map(int, input().split())
    g = Graph(n, m)

    for i in range(m):
        u, v = map(int, input().split())
        g.add_edge(u, v)


    ans = "yes" if g.arb_exist() else "no"
    print(ans)

if __name__ == "__main__":
    main()