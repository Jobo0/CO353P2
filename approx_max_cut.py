from collections import defaultdict
import heapq
# Main Script - Fetch Inputs, do outputs from here. Run directly. 

def main():
    

    n, m = map(int, input().split())
    edgeAdjList = defaultdict(list)
    # defaults to empty list when key hasnt been added

    for i in range(m):
        u, v = map(int, input().split())
        edgeAdjList[u].append(v)


    print("placeholder")

if __name__ == "__main__":
    main()