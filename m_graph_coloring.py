'''
Given an undirected graph and a number m, determine if the graph can be colored with at most m colors such that no two adjacent vertices of the graph are colored with same color.
Watch this for recursive state space explanation https://www.youtube.com/watch?v=052VkKhIaQ4
'''

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0],
]

m = 3
vertices = len(graph)
colors = [0]*vertices

def is_safe(graph,colors,v,c):
    #iterate through adjacent vertices and check if vertex color is different from c 
    for i in range(vertices):
        if graph[v][i] and c == colors[i]:#so if color of current node ie. c is equal to any of its neighbours then return false
            return False 
    return True 

def graph_coloring(graph,colors,m,v):
    #if all vertices are assigned a colour 
    if v == vertices:
        return True
    
    #try different colors(1,2,3) for vertex v 
    for c in range(1,m+1):
        #check if assignment of color c to n is possible , c is going to be the color of current node
        if is_safe(graph,colors,v,c):
            #assign color c to v 
            colors[v] = c 

            #recursively assign colors to the rest of the vertices 
            if graph_coloring(graph,colors,m,v+1):
                return True 
            #if there is no solution, remove color(backtrack)
            colors[v] = 0

if graph_coloring(graph,colors,m,0):
    print colors 
else:
    print "Not possible"




    