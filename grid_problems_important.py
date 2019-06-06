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

'''
Minimum cost path with right and bottom moves allowed

The path to reach (m, n) must be through one of the 3 cells: (m-1, n-1) or (m-1, n) or (m, n-1). So minimum cost to reach (m, n) can be written as 'minimum of the 3 cells plus cost[m][n]'.

minCost(m, n) = min (minCost(m-1, n-1), minCost(m-1, n), minCost(m, n-1)) + cost[m][n]

Here is the dp solution
'''
cost = [[1, 2, 3], 
        [4, 8, 2], 
        [1, 5, 3]]
r = len(cost)
c = len(cost[0])

def min_cost_path(cost,r,c):
    T = [[0 for i in range(c)] for i in range(c)]
    T[0][0] = cost[0][0]

    for i in range(r):
        T[i][0] = T[i-1][0] + cost[i][0]
    
    for i in range(c):
        T[0][i] = T[0][i-1] + cost[0][i]

    for i in range(1,r):
        for j in range(1,c):
            T[i][j] = min(T[i-1][j-1],T[i-1][j],T[i][j-1]) + cost[i][j]
    
    return T[r-1][c-1]

print min_cost_path(cost,r,c)

'''
Given a matrix of dimension m*n where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
0: Empty cell

1: Cells have fresh oranges

2: Cells have rotten oranges 

So we have to determine what is the minimum time required so that all the oranges become rotten. A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right). If it is impossible to rot every orange then simply return -1.
'''

M = [
    [2,1,0,2,1],
    [1,0,1,2,1],
    [1,0,0,2,1]
]
r = len(M)
c = len(M[0])

def check_all(M):
    for i in range(r):
        for j in range(c):
            if M[i][j] == 1:
                return True 
    return False 

def is_valid(i,j):
    return i>=0 and i<r and j>=0 and j<c 

def rotten_time(M,r,c):
    q = []
    ans = 0 #will hold the time
    #store all the rotten oranges in the queue
    for i in range(r):
        for j in range(c):
            if M[i][j] == 2:
                q.append((i,j))
    
    #separating these rotten oranges from the oranges which will rotten due to the oranges in the first time frame 
    q.append((-1,-1))

    while q:
        rotten_flag = False 
        while q[0][0] != -1 and q[0][1] != -1:
            
            x = q[0][0]
            y = q[0][1]

            #check down adjacent if it can be rotten
            if is_valid(x+1,y) and M[x+1][y] == 1:
                #if this is the first orange to get rotten, increase count and set the rotten flag
                if rotten_flag is False:
                    ans += 1
                    rotten_flag = True 
                #make the orange rotten
                M[x+1][y] = 2

                #push the adjacent orange to queue 
                x += 1
                q.append((x,y))
                x -= 1 #move back to current cell 
            
            #check for up adjacent
            if is_valid(x-1,y) and M[x-1][y] == 1:
                #if this is the first orange to get rotten, increase count and set the rotten flag
                if rotten_flag is False:
                    ans += 1
                    rotten_flag = True 
                #make the orange rotten
                M[x-1][y] = 2

                #push the adjacent orange to queue 
                x -= 1
                q.append((x,y))
                x += 1 #move back to current cell

            #check for left adjacent
            if is_valid(x,y-1) and M[x][y-1] == 1:
                #if this is the first orange to get rotten, increase count and set the rotten flag
                if rotten_flag is False:
                    ans += 1
                    rotten_flag = True 
                #make the orange rotten
                M[x][y-1] = 2

                #push the adjacent orange to queue 
                y -= 1
                q.append((x,y))
                y += 1 #move back to current cell

            #check for right adjacent
            if is_valid(x,y+1) and M[x][y+1] == 1:
                #if this is the first orange to get rotten, increase count and set the rotten flag
                if rotten_flag is False:
                    ans += 1
                    rotten_flag = True 
                #make the orange rotten
                M[x][y+1] = 2

                #push the adjacent orange to queue 
                y += 1
                q.append((x,y))
                y -= 1 #move back to current cell
            
            q.pop(0)

        #pop the delimeter
        q.pop(0)

        #if rotten oranges then separate them usign delimeter for the next time frame to process
        if q:
            q.append((-1,-1))
    
    if check_all(M):
        return -1
    else:
        return ans 

print rotten_time(M,r,c)

'''
Minimum cells required to reach destination with jumps equal to cell values
https://www.geeksforgeeks.org/minimum-cells-required-reach-destination-jumps-equal-cell-values/
https://www.geeksforgeeks.org/minimum-steps-required-to-reach-the-end-of-a-matrix-set-2/ 
'''
from collections import namedtuple
import sys

grid = [
    [2,3,2,1,4],
    [3,2,5,8,2],
    [1,1,2,2,1]
]

# grid = [
#     [2,4,2],
#     [5,3,8],
#     [1,1,1]
# ]

grid = [
    [2,1,2],
    [1,1,1],
    [1,1,1]
]
class iNode:
    def __init__(self,x,y):
        self.x = x 
        self.y = y

Node = namedtuple('Node',['x','y','dist'])

row = [0,1]
col = [1,0]
n = len(grid)

r = len(grid)
c = len(grid[0])

path = [[iNode(-1,-1) for i in range(c)] for i in range(r)]

def isvalid(grid,visit,row,col):
    return row>=0 and row<len(grid) and col>=0 and col<len(grid[0]) and not visit[row][col]

def bfs_(grid,sx,sy,dx,dy):
    visit = [[0]*len(grid[0]) for i in range(len(grid))]
    q = []
    visit[sx][sy] = True #mark source as visited
    q.append(Node(sx,sy,0)) #append source to queue
    min_dist = sys.maxint

    while len(q)>0:
        node = q.pop(0)
        
        i = node.x
        j = node.y
        dist = node.dist

        #if destination is found update min_dist and stop
        if i == dx and j == dy:

            #code to find path
            curr = node 
            while curr.x != -1:
                print curr.x,curr.y #will print the path
                curr = path[curr.x][curr.y]


            min_dist = dist
            break

        curr_cell_val = grid[i][j]

        #check all 4 possible movements from the current cell
        for k in range(2):
            if isvalid(grid,visit,i+row[k]*curr_cell_val,j+col[k]*curr_cell_val):
                visit[i+row[k]*curr_cell_val][j+col[k]*curr_cell_val] = True
                q.append(Node(i+row[k]*curr_cell_val,j+col[k]*curr_cell_val,dist+1))

                #matrix which will store parent information
                path[i+row[k]*curr_cell_val][j+col[k]*curr_cell_val] = node 
    
    if min_dist != sys.maxint:
        print min_dist
    else:
        print "Destination can't be reached"

bfs_(grid,0,0,r-1,c-1)







