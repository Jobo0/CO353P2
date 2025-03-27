from collections import defaultdict
# Main Script - Fetch Inputs, do outputs from here. Run directly. 

def greedy_max_cut(adj_list):
    # Greedily select node who will most increase cut size
    # Value indicates how much cut will increase by addition
    # Initialized as node degree
    node_values = {u: len(adj_list[u]) for u in adj_list}

    S = set()

    while True:
        # get node with highest value
        u = max(node_values, key=node_values.get)
        
        if node_values[u] <= 0: # adding to set won't increase cut
            break

        S.add(u)
        node_values[u] = 0 # adding u no longer increases cut size

        for v in adj_list[u]:
            node_values[v] -= 1
        
    return S

def main():
    

    n, m = map(int, input().split())
    edgeAdjList = defaultdict(list)
    # defaults to empty list when key hasnt been added

    for i in range(m):
        u, v = map(int, input().split())
        edgeAdjList[u].append(v)
        edgeAdjList[v].append(u)

    greedy_cut = greedy_max_cut(edgeAdjList)
    print(len(greedy_cut))
    print(*greedy_cut)

if __name__ == "__main__":
    main()