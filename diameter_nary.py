'''
      a
    / | \
   b  c  d
  / \    |
 e   f   g

Diameter is the number of nodes on the longest path between two leaf nodes.
'''
from collections import defaultdict

graph = {
    'a':['b','c','d'],
    'b':['a','e','f'],
    'c':['a'],
    'd':['a','g'],
    'e':['b'],
    'f':['b'],
    'g':['d']
}

def bfs_farthest_node(graph,source):
    visited = {}
    diameter = defaultdict(int)
    q = []
    q.append(source)
    visited[source] = True 
    while q:
        s = q.pop(0)
        for e in graph[s]:
            if e not in visited:
                visited[e] = True 
                diameter[e] = diameter[s]+1
                q.append(e)

    farthest_node = source
    farthest_dist = 0 
    for i in diameter.items():
        if i[1] > farthest_dist:
            farthest_node = i[0]
            farthest_dist = i[1]

    return farthest_node,farthest_dist

def diameter(graph):
    #run bfs to find farthest node from any node of tree
    first_farthest_node = bfs_farthest_node(graph,'a')[0]
    #run bfs from node find above and find the farthest from it
    return bfs_farthest_node(graph,first_farthest_node)[1]+1

print diameter(graph)
    

