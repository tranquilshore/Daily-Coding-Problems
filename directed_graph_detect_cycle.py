'''
color mechanism: white - unvisited, grey-processing, black-visited/processed
we visit a node u and color it grey, we visit neighbour of u that are white, if neighbour node is coloured grey then cycle exists
'''
graph={
    "A":["B"],
    "B":["D","C"],
    "C":["A"],
    "D":["E"],
    "E":[]
}

def cycle_exists(graph):
    visited = {u:"white" for u in graph}
    found_cycle = [False]
    for u in graph:
        if visited[u] == "white":
            dfs_visit(graph,u,visited,found_cycle)
        if found_cycle[0]:
            break 
    return found_cycle[0]

def dfs_visit(graph,u,visited,found_cycle):
    if found_cycle[0]: return 
    visited[u] = "grey"
    for v in graph[u]:
        if visited[v] == "grey":
            found_cycle[0] = True 
            return 
        if visited[v] == "white":
            dfs_visit(graph,v,visited,found_cycle)
        visited[v] = "black"

if cycle_exists(graph):
    print "cycle exists"
else:
    print "no cycles"