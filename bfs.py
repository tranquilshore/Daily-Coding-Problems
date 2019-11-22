'''
a - b - e
|   |
c   d - f
'''

graph = {
    'a':['b','c'],
    'b':['a','d','e'],
    'c':['a'],
    'd':['b','f'],
    'e':['b'],
    'f':['d']
}

def bfs(graph,source):
    visited = {}
    queue = []
    queue.append(source)
    visited[source] = True 
    while queue:
        s = queue.pop(0)
        print s, 
        for e in graph[s]:
            if e not in visited:
                queue.append(e)
                visited[e] = True 

bfs(graph,"a")