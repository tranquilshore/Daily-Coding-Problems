m = [[0,0,1],
    [0,0,1],
    [1,0,0]]

r = len(m)
c = len(m[0])

sol = [[0 for i in range(c)] for i in range(r)]

def check_conditions(m,x,y):
    return x>=0 and x<r and y>=0 and y<c and m[x][y] == 0

ans = [0]
def number_of_ways(m,sx,sy,dx,dy):
    if sx == dx and sy == dy:
        ans[0] += 1
        sol[sx][sy] = 1
        print sol  
        return 
    sol[sx][sy] = 1
    if check_conditions(m,sx,sy+1):
        number_of_ways(m,sx,sy+1,dx,dy)
    if check_conditions(m,sx+1,sy):
        number_of_ways(m,sx+1,sy,dx,dy)
    sol[sx][sy] = 0

number_of_ways(m,0,0,r-1,c-1)
print ans 
        