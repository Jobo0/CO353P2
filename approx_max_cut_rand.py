import random
from collections import defaultdict
# Main Script - Fetch Inputs, do outputs from here. Run directly. 

def rand_cut(n):
    S = set()

    # 50/50 chance to include a vertex in the cut
    for vertex in range(1, n+1):
        if random.random() < 0.5:
            S.add(vertex)
    return S

def count_cut_edges(S, adjlist):
    # count edges that have one endpoint in S and one outside S
    count = 0
    for u in S:
        for v in adjlist[u]:
            if v not in S:
                count += 1

    return count

def rand_cut_trials(adjlist, trials,n):

    best_S = set()
    best_cut = 0

    for i in range(trials):
        S = rand_cut(n)
        cut_size = count_cut_edges(S, adjlist)
        if cut_size > best_cut:
            best_S = S
            best_cut = cut_size
    
    return best_S



def main():
    

    n, m = map(int, input().split())
    edgeAdjList = defaultdict(list)
    # defaults to empty list when key hasnt been added

    for i in range(m):
        u, v = map(int, input().split())
        edgeAdjList[u].append(v)
        edgeAdjList[v].append(u)

    cut = rand_cut_trials(edgeAdjList,15,n)
    print(len(cut))
    print(*cut)

if __name__ == "__main__":
    main()