'''
Knight's Tour:
Given a chess board, print all sequences of moves of a knight on a chessboard such that knight visits every square only once.
read this https://www.techiedelight.com/print-possible-knights-tours-chessboard/ for understanding the problem well.
'''

#order in which knight will move in anti circular fashion and will be optimum
row = [2,1,-1,-2,-2,-1,1,2,2]
col = [1,2,2,1,-1,-2,-2,-1,1]

N = 5 #size of the chess board
pos = 1 #starting position for the knight to start the tour

visited = [[0 for i in range(N)] for i in range(N)]

#function which will make sure we move with the boundaries of the chess board
def is_valid(x,y):
    if x<0 or y<0 or x>=N or y>=N:
        return False 
    return True 

def knight_tour(visited,x,y,pos):
    visited[x][y] = pos #mark current squar as visited

    if pos >= N*N: #condition for all squares visited, print the solution
        for i in range(N):
            for j in range(N):
                print visited[i][j], " ",
            print 
        print
        #visited[x][y] = 0 #backtracking after printing the one possible moves of knight, don't use it if only one possible solution is required
        return

    for k in range(8):
        newx = x+row[k]
        newy = y+col[k]

        if is_valid(newx,newy) and visited[newx][newy] == 0:
            knight_tour(visited,newx,newy,pos+1)

    visited[x][y] = 0 #backtrack from the current square and remove it from current path

knight_tour(visited,0,0,pos)

'''
Chess Knight Problem:
given a chess board, find the shortest distance taken by a knight to reach given destination from given source.
using bfs to find the shortest distance.
'''

from collections import namedtuple

N=8
Node = namedtuple('Node',['x','y','dist'])
grid = [[0 for i in range(N)] for i in range(N)]

def bfs(grid,sx,sy,dx,dy):
    r = len(grid)
    c = len(grid[0])

    visit = [[0 for i in range(c)] for i in range(r)]

    q = []
    visit[sx][sy] = True #marked source as visited
    q.append(Node(sx,sy,0))

    while len(q) > 0:
        node = q.pop(0)

        i = node.x 
        j = node.y 
        dist = node.dist 

        if i == dx and j == dy:
            return dist
        
        for k in range(8):
            newx = i + row[k]
            newy = j + col[k]

            if is_valid(newx,newy) and visit[newx][newy] == 0:
                visit[newx][newy] = True 
                q.append(Node(newx,newy,dist+1))

    return -1

print bfs(grid,0,7,7,0)


    


    




