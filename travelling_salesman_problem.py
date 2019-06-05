'''
TSP is nothing but minimum weighted hamiltonian cycle of a graph.
It is an NP Hard problem
Backtracking solution
'''

V = 4
graph= [[ 0, 10, 15, 20 ], 
        [ 10, 0, 35, 25 ], 
        [ 15, 35, 0, 30 ], 
        [ 20, 25, 30, 0 ]]

#to keep track of visited nodes
v = [False for i in range(V)]

#mark first node as visited
v[0] = True 
ans = []
def tsp(graph,v,currpos,V,count,cost):
    #last node is reached and there is an edge between that node and starting node
    if count == V and graph[currpos][0]:
        ans.append(cost+graph[currpos][0])
        return 
    
    for i in range(1,V):
        #if not visited and there is an edge between i and currpos
        if v[i] == False and graph[currpos][i]:
            v[i] = True 
            tsp(graph,v,i,V,count+1,cost+graph[currpos][i])
            v[i] = False 

tsp(graph,v,0,V,1,0)
print min(ans)
