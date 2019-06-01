'''
given a rod of length n and list of prices of rod of length i, find the optimal way
to cut the rod into smaller rods to maximize the profit.
eg.
length = [1,2,3,4]
prices = [2,5,7,8]

profit will be 12, by (2,3) or (1,2,2) as we can consider the same element again, it gives the feel
of coin change problem where we find the total number of ways.
'''
import sys 
prices = [2,5,7,8]
#prices = [1,5,8,9,10,17,17,20]
#prices = [3,5,8,9,10,17,17,20]

#recursive
#one by one partition the rod of length n into two parts of length i and n-i, recur for length n-i and finally return the maximum of all.
#rodcut(n) = max(prices[i-1] + rodcut(n-i))

def rodcut(prices,n):
    if n <= 0:
        return 0 
    maxval = -sys.maxint
    for i in range(1,n+1):
        cost =  prices[i-1] + rodcut(prices,n-i)
        if cost > maxval:
            maxval = cost
    return maxval
print rodcut(prices,len(prices))

#dp bottom up watch https://www.youtube.com/watch?v=IRwVmTmN6go to understand dp

def rodcut_bottomup(prices,length):
    m = length 
    n = len(prices)

    T = [[0 for i in range(m+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if i > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j], prices[i-1]+T[i][j-i])
    return T[n][m]

print rodcut_bottomup(prices,5)
