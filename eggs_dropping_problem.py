'''
watch https://www.youtube.com/watch?v=3hcaVyX00_4&t=331s to understand

There are two possible cases:
given n eggs and k floors, suppose we are at xth floor then those two possibilities will be
1. if egg breaks at xth floor, then we have 1 less egg to work with and we have to check in the floor down xth floor
    i.e. mineggsdrop(n-1,x-1)
2. if egg doesn't break at xth floor, we have same no. of eggs to work with, with no. of floors in xth to k to work with.
    i.e. mineggsdrop(n,k-x)

at each floor we find the max work, we would do ie. 1 + max(mineggsdrop(n-1,x-1), mineggsdrop(n,k-x)), 1 because it doesn't matter eggs breaks or not we are making an attempt
as requirement is to find the minimum attempts, we will find the minimum of above value among k floors. That will be the final answer
'''
import sys 
n = 2 #no of eggs
k = 36 #no of floors

#recursive
def mineggsdrop(n,k):
    if k == 1 or k == 0:#base case when we just have 1 or 0 floor doesn't matter how many eggs we have, result will be just k
        return k 
    if n == 1:#if just have 1 egg, then we have to make k attempts
        return k 
    
    res = sys.maxint
    for x in range(1,k+1):
        res = min(res, 1+max(mineggsdrop(n-1,x-1), mineggsdrop(n,k-x)))
    
    return res  

#print mineggsdrop(n,k)

#dp 
def mineggsdrop_bottomup(n,k):
    T = [[0 for i in range(k+1)] for i in range(n+1)]

    for i in range(1,k+1):#base case when we have just 1 egg
        T[1][i] = i 
    
    for i in range(1,n+1):#base case when we just have 1 floor, for 0 floor its already set when we initialized the 2d array
        T[i][1] = 1 

    for i in range(2,n+1):
        for j in range(2,k+1):
            if i > j:
                T[i][j] = T[i-1][j]
            else:
                res = sys.maxint
                for x in range(1,j+1):
                    res = min(res,1+max(T[i-1][x-1], T[i][j-x]))
                    T[i][j] = res 
        
    return T[n][k]

print mineggsdrop_bottomup(n,k)

