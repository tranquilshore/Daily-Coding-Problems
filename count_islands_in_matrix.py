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
