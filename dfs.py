graph = {
    "A":["B","C"],
    "B":["A","F"],
    "C":["A","D"],
    "D":["C","E"],
    "E":["D"],
    "F":["B"]
}

def dfs(graph):
    visited = {u:False for u in graph}
    for u in graph:
        if not visited[u]:
            dfs_visit(graph,u,visited)

def dfs_visit(graph,u,visited):
    visited[u] = True 
    print u,
    for v in graph[u]:
        if not visited[v]:
            dfs_visit(graph,v,visited)

dfs(graph)