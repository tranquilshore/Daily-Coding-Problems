a = [3,9,1,2]

def optimal_strategy_game_bottomup(a):
    n = len(a)
    T = [[(0,0) for i in range(n)] for i in range(n)]

    for i in range(n):
        T[i][i] = (a[i],0)

    for i in range(n):
        for j in range(i+1,n):
            if a[i] + T[i+1][j][1] >= a[j] + T[i][j-1][1]:
                T[i][j] = (a[i] + T[i+1][j][1] , T[i+1][j][0] )
            else:
                T[i][j] = (a[j] + T[i][j-1][1], T[i][j-1][0])
    return T[0][n-1][0]

print optimal_strategy_game_bottomup(a)
