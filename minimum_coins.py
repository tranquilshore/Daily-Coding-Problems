#recursive
import sys 

s = [1,2,3,4]
target = 15

def find_min_coins(s,n,target):
    if target == 0:
        return 0
    if target < 0:
        return sys.maxint

    coins = sys.maxint

    for i in range(n):
        res = find_min_coins(s,n,target-s[i])
        if res != sys.maxint:
            coins = min(coins,res+1)
    
    return coins 

print find_min_coins(s,len(s),target)

#dp bottom up

def find_min_coins_bottomup(s,target):
    n = len(s)
    m = target

    T = [[0 for i in range(m+1)] for i in range(n+1)]

    for i in range(m+1):
        T[0][i] = sys.maxint

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = min(T[i-1][j], T[i][j-s[i-1]] + 1)

    return T[n][m]

print find_min_coins_bottomup(s,target)