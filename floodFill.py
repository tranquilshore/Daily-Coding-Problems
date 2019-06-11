def floodFill(screen,x,y,oldVal,newVal):
    if x>=R or x<0 or y>=C or y<0:
        return
    if screen[x][y] != oldVal:
        return
    screen[x][y] = newVal

    floodFill(screen,x+1,y,oldVal,newVal)
    floodFill(screen,x-1,y,oldVal,newVal)
    floodFill(screen,x,y+1,oldVal,newVal)
    floodFill(screen,x,y-1,oldVal,newVal)
    

screen = [[1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 0, 0],
     [1, 0, 0, 1, 1, 0, 1, 1],
     [1, 2, 2, 2, 2, 0, 1, 0],
     [1, 1, 1, 2, 2, 0, 1, 0],
     [1, 1, 1, 2, 2, 2, 2, 0],
     [1, 1, 1, 1, 1, 2, 1, 1],
     [1, 1, 1, 1, 1, 2, 2, 1]]

R = len(screen)
C = len(screen[0])

Sx = 4
Sy = 4
oldVal = screen[Sx][Sy] 
newVal = 3

floodFill(screen,Sx,Sy,oldVal,newVal)

for i in range(R):
    for j in range(C):
        print screen[i][j],
    print 
