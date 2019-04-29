'''
We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].

Idea : just do the topological sort for the above graph.
'''

graph = {'CSC100': [],
         'CSC200': ['CSC100'],
         'CSC300': ['CSC100', 'CSC200']}


def topological_sort(graph):
    L = []
    color = {u: 'white' for u in graph}
    found_cycle = [False]

    for u in graph:
        if color[u] == 'white':
            dfs_visit(graph,u,found_cycle,color,L)
        if found_cycle[0]:
            break 
    if found_cycle[0]:
        L = []
    L.reverse()
    return L 

def dfs_visit(graph,u,found_cycle,color,L):
    if found_cycle[0]:
        return 
    color[u] = 'grey'
    for v in graph[u]:
        if color[v] == 'grey':
            found_cycle[0] = True 
            return 
        if color[v] == 'white':
            dfs_visit(graph,v,found_cycle,color,L)
    color[u] = 'black'
    L.append(u)

ans = topological_sort(graph)
if len(ans) == 0:
    print "can't finish all cources!"
else:
    print ans #print the answer in reverse order as the requirement is opposite of the topological sort result.

