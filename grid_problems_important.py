'''
Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 5 islands.
{{1, 1, 0, 0, 0},
{0, 1, 0, 0, 1},
{1, 0, 0, 1, 1},
{0, 0, 0, 0, 0},
{1, 0, 1, 0, 1}}

Idea is simple to do just bfs and count the segregated areas.
Note that the given solution is simply works as BFS for disconnected graph.
'''

M = [[1, 1, 0, 0, 0],
[0, 1, 0, 0, 1],
[1, 0, 0, 1, 1],
[0, 0, 0, 0, 0],
[1, 0, 1, 0, 1]]

row = [-1,-1,-1,0,0,1,1,1]
col = [-1,0,1,-1,1,-1,0,1]

r = len(M)
c = len(M[0])

visited = [[0 for i in range(c)] for i in range(r)]

def is_safe(M,visited,i,j):
    return i >= 0 and i <r and j >= 0 and j < c and M[i][j] and not visited[i][j]

def bfs(M,visited,si,sj):
    q = [(si,sj)]
    visited[si][sj] = True 

    while q:
        curr = q.pop(0)
        i = curr[0]
        j = curr[1]

        for k in range(8):
            if is_safe(M,visited,i+row[k],j+col[k]):
                visited[i+row[k]][j+col[k]] = True 
                q.append((i+row[k],j+col[k]))

def count_islands(M):
    res = 0
    for i in range(r):
        for j in range(c):
            if M[i][j] and not visited[i][j]:
                bfs(M,visited,i,j)
                res += 1
    return res 

print count_islands(M)

'''
find if path exists or not
1 - source
2 - destination
3 - blank space
0 - wall
'''

M = [[0,3,2],
     [3,3,0],
     [1,3,0]]

r = len(M)
c = len(M[0])

row = [-1,0,0,1]
col = [0,-1,1,0]


for i in range(r):
    for j in range(c):
        if M[i][j] == 1:
            sx = i
            sy = j 
        if M[i][j] == 2:
            dx = i 
            dy = j
        if M[i][j] > 0:
            M[i][j] = 1

def is_safe_path(M,visited,i,j):
    if i>=0 and i<r and j>=0 and j<c and not visited[i][j] and M[i][j]:
        return True 
    else:
        return False 

def bfs_path(M,sx,sy,dx,dy):
    visited = [[0 for i in range(c)] for i in range(r)]
    q = [(sx,sy)]
    visited[sx][sy] = True 
    path_flag = False
    while q:
        curr = q.pop(0)
        i = curr[0]
        j = curr[1]

        if i == dx and j == dy:
            path_flag = True 
        
        for k in range(4):
            if is_safe_path(M,visited,i+row[k],j+col[k]):
                visited[i+row[k]][j+col[k]] = True 
                q.append((i+row[k], j+col[k]))

    return path_flag

print bfs_path(M,sx,sy,dx,dy)

'''
Minimum cost path (using dijkstra)

Given a square grid of size N, each cell of which contains integer cost which represents a cost to traverse through that cell, we need to find a path from top left cell to bottom right cell by which total cost incurred is minimum.

It is not possible to solve this problem using dynamic programming similar to previous problem because here current state depends not only on right and bottom cells but also on left and upper cells. We solve this problem using dijkstra algorithm. Each cell of grid represents a vertex and neighbor cells adjacent vertices. We do not make an explicit graph from these cells instead we will use matrix as it is in our dijkstra algorithm.

'''
from heapq import heappush, heappop
import sys 
grid = [
    [31,100,65,12,18],
    [10,13,47,157,6],
    [100,113,174,11,33],
    [88,124,41,20,140],
    [99,32,111,41,20]
]

r = len(grid)
c = len(grid[0])

def shortest(grid,r,c):
    dis = [[sys.maxint for i in range(c)] for i in range(r)]
    visited = [[0 for i in range(c)] for i in range(r)]
    row = [-1,0,1,0]
    col = [0,1,0,-1]

    queue = [(grid[0][0],0,0)]
    dis[0][0] = grid[0][0]

    while queue:
        curr = heappop(queue)
        x = curr[1]
        y = curr[2]
        visited[x][y] = True 
        for k in range(4):
            newx = x + row[k]
            newy = y + col[k]
            
            if newx>=0 and newx<r and newy>=0 and newy<c and visited[newx][newy] == False and dis[x][y] + grid[newx][newy] < dis[newx][newy]:
                dis[newx][newy] = grid[newx][newy] + dis[x][y]
                heappush(queue,(dis[newx][newy],newx,newy))
    
    return dis[r-1][c-1]

print shortest(grid,r,c)

