m = [
    ['b','b','c','b'],
    ['b','c','c','b'],
    ['c','c','c','b'],
    ['b','c','b','b']
]

in_sym = 'g'
sx = 1
sy = 2

r = len(m)
c = len(m[0])

def check_boundaries(x,y):
    return x<r and x>=0 and y<c and y>=0

def flood_fill(m,sx,sy,in_sym):
    temp = m[sx][sy] 
    m[sx][sy] = in_sym
    if check_boundaries(sx+1,sy) and m[sx+1][sy] == temp:
        flood_fill(m,sx+1,sy,in_sym)
    if check_boundaries(sx-1,sy) and m[sx-1][sy] == temp:
        flood_fill(m,sx-1,sy,in_sym)
    if check_boundaries(sx,sy+1) and m[sx][sy+1] == temp:
        flood_fill(m,sx,sy+1,in_sym)
    if check_boundaries(sx,sy-1) and m[sx][sy-1] == temp:
        flood_fill(m,sx,sy-1,in_sym)

flood_fill(m,sx,sy,in_sym)
print m 
    
    




