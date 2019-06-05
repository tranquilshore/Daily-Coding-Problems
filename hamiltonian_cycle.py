'''
It is an NP-hard problem means there is no polynomial solution for this problem.

Hamiltonian Path in an undirected graph is a path that visits each vertex exactly once. A Hamiltonian cycle (or Hamiltonian circuit) is a Hamiltonian Path such that there is an edge (in graph) from the last vertex to the first vertex of the Hamiltonian Path. 

Following will be a backtracking solution:

Create an empty path array and add vertex 0 to it. 
Add other vertices, starting from the vertex 1. 
Before adding a vertex, check for whether 
1. it is adjacent to the previously added vertex and not already added.
2. If we find such a vertex, we add the vertex as part of the solution. If we do not find a vertex then we return false.

watch https://www.youtube.com/watch?v=dQr4wZCiJJ4 to understand
following code will only print single hamiltonian cycle
'''

graph = [[0, 1, 0, 1, 0], 
        [1, 0, 1, 1, 1],  
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],  
        [0, 1, 1, 1, 0]]

V = 5


def is_safe(v,pos,path):
    #if there an edge between added vertex and last vertex or not
    if graph[path[pos-1]][v] == 0:
        return False 
    for vertex in path:
        if vertex == v:
            return False 
    return True

def hamiltonian_cycle_util(path,pos):
    #if all vertices are included in the path
    if pos == V:
        #there must be an edge between last vertex and first vertex
        if graph[path[pos-1]][path[0]] == 1:
            return True 
        else:
            return False 
    
    #try different vertices as next candidate
    for v in range(1,V):
        if is_safe(v,pos,path):
            path[pos] = v 

            if hamiltonian_cycle_util(path,pos+1):
                return True 
            
            path[pos] = -1
    
    return False 

def hamiltonian_cycle(graph):
    path = [-1]*V 

    path[0] = 0 #just put first vertex in the path as hamiltonian cycle can start from any vertes if exists
    if hamiltonian_cycle_util(path,1) == False:
        print "solution doesn't exist"
        return False 
    
    path.append(path[0])#just to show the full cycle
    print path  
    return True 

hamiltonian_cycle(graph)
    