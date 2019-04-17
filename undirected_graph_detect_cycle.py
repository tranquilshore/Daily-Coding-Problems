'''
idea is whenever we visit a vertex v which has a neighbour u which is already visited but is not the parent of v, then we say the cycle exists
'''
graph = {
    "A":["B","C"],
    "B":["A","F","C"],
    "C":["A","D","B"],
    "D":["C","E"],
    "E":["D"],
    "F":["B"]
}

def cycle_exists(graph):
    visited = {u:False for u in graph}
    found_cycle = [False]

    for u in graph:
        if not visited[u]:
            dfs_visit(graph,u,visited,u,found_cycle)#parameters: graph,current node, visited, parent node(for source, source is its parent),found_cycle
        if found_cycle[0]:
            break 
    return found_cycle[0]

def dfs_visit(graph,current,visited,parent,found_cycle):
    if found_cycle[0]: return
    visited[current] = True 
    for v in graph[current]:
        if visited[v] and v!=parent: # condition explained above to find cycle in undirected graph
            found_cycle[0] = True 
            return 
        if not visited[v]:
            dfs_visit(graph,v,visited,current,found_cycle)

cycle = cycle_exists(graph)
if cycle:
    print "cycle exists"
else:
    print "no cycles"
