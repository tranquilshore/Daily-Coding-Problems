from collections import namedtuple
import sys

def isvalid(grid,visit,row,col):
    return row>=0 and row<len(grid) and col>=0 and col<len(grid[0]) and grid[row][col] and not visit[row][col]

def bfs(grid,sx,sy,dx,dy):
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
            #code to find the path
            curr = node 
            while curr.x != -1:
                print curr.x,curr.y
                curr = path[curr.x][curr.y]

            #to just find min dist
            min_dist = dist
            break
        #check all 4 possible movements from the current cell
        for k in range(4):
            if isvalid(grid,visit,i+row[k],j+col[k]):
                visit[i+row[k]][j+col[k]] = True
                q.append(Node(i+row[k],j+col[k],dist+1))
                #matrix which will store the parent information
                path[i+row[k]][j+col[k]] = node 
    
    if min_dist != sys.maxint:
        print min_dist
    else:
        print "Destination can't be reached"
        

#1
grid = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]]

#2
'''
shortest distance between s and d 
{'0', '*', '0', 's'},
{'*', '0', '*', '*'},
{'0', '*', '*', '*'},
{'d', '*', '*', '*'}
'''
grid = [[0,1,0,1],
        [1,0,1,1],
        [0,1,1,1],
        [1,1,1,1]]

#3
#minimum moves required to move from 1 to 2
grid = [[ 0 , 3 , 2 ],
        [ 3 , 3 , 0 ],
        [ 1 , 3 , 0 ]];

r = len(grid)
c = len(grid[0])

class Node:
    def __init__(self,x,y):
        self.x = x 
        self.y = y

path = [[Node(-1,-1) for i in range(c)] for i in range(r)] 

Node = namedtuple('Node',['x','y','dist'])

row = [-1,0,0,1]
col = [0,-1,1,0]

#bfs(grid,0,0,3,4) #ans is 11
bfs(grid,0,3,3,0) #ans is 6



