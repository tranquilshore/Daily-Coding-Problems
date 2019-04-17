'''
topological sorting: works only for DAGs, if there is a cycle in graph, topological sorting can't be done
idea is to modify the dfs, in dfs we start from vertex and print it immediately and then recursively calls DFS for its adjacent vertices.
in topological sorting we don't print the vertex immediately, we first call topological sort recursively for all its adjacent vertices and 
then push it on stack.

we can do the colour coding traversing which checks for cycles as well and return the reverse of the list with all black colour nodes.
'''

graph={
    "A":["B","C"],
    "B":["D","C"],
    "C":[],
    "D":["E"],
    "E":[]
}

def topological_sort(graph):
    visited = {u:"white" for u in graph}
    L = []
    found_cycle = [False]

    for u in graph:
        if visited[u] == "white":
            dfs_visit(graph,u,visited,L,found_cycle)
        if found_cycle[0]:
            break 
    if found_cycle[0]:
        L = []
    L.reverse()
    return L 

def dfs_visit(graph,u,visited,L,found_cycle):
    if found_cycle[0]: return 
    visited[u] = "grey"
    for v in graph[u]:
        if visited[v] == "grey":
            found_cycle[0] = True 
            return 
        if visited[v] == "white":
            dfs_visit(graph,v,visited,L,found_cycle)
    visited[u] = "black"
    L.append(u)

print topological_sort(graph)
