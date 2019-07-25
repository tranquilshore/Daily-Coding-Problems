M = [
    [0,3,1,1],
    [2,0,0,4],
    [1,5,3,1]
]
r = len(M)
c = len(M[0])

def max_num_coins(M,r,c):
    T = [[0 for i in range(c)] for j in range(r)]

    T[0][0] = M[0][0]
    for i in range(1,r):
        T[i][0] = M[i][0] + T[i-1][0]
    
    for i in range(1,c):
        T[0][i] = M[0][i] + T[0][i-1]
    
    for i in range(1,r):
        for j in range(1,c):
            T[i][j] = max(T[i-1][j],T[i-1][j-1],T[i][j-1]) + M[i][j]

    return T[r-1][c-1]

print max_num_coins(M,r,c)