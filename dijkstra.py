#visit the unvisited vertex with the smallest known distance from the start vertex - greedy approach
from heapq import heappush,heappop

graph = {
    "A":{"B":6,"D":1},
    "B":{"A":6,"D":2,"E":2,"C":5},
    "C":{"B":5,"E":5},
    "D":{"A":1,"B":2,"E":1},
    "E":{"D":1,"B":2,"C":5}
}

def dijkstra(graph,source):
    A = {u:None for u in graph}
    q = [(0,source)]
    while q:
        pathlen,v = heappop(q)
        if A[v] is None:
            A[v] = pathlen
            for w,edgelen in graph[v].items():
                if A[w] is None:
                    heappush(q,(pathlen+edgelen,w))
    return A 

print dijkstra(graph,"A")