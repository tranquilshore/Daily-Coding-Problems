'''
given integer array, find the longest subsequence s.t. all the elements in the subsequence are sorted(ascending).
It also solves maximum sum increasing subsequence.
'''

a = [3,4,-1,0,6,2,3]
a = [2,5,8,1,3]

def LIS(a,n):
    T = [1 for i in range(n)]
    for i in range(1,n):
        for j in range(i):
            if a[j]<a[i]:
                T[i]=max(T[i],T[j]+1)
    return max(T)

print LIS(a,len(a))

###############################################################################################
#maximum sum increasing subsequence just add a[i] instead of 1 at step a and initialise T with original values
a = [3,10,2,1,20]
def MSIS(a,n):
    T = [0]*n 
    for i in range(n):
        T[i] = a[i]

    for i in range(1,n):
        for j in range(i):
            if a[j]<a[i]:
                T[i] = max(T[i],T[j]+a[i])#step a
    return max(T)

print MSIS(a,len(a))

######################################################################################################
'''
maximum length chain of pairs

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number. A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion. Find the longest chain which can be formed from a given set of pairs.
For example, if the given pairs are {{5, 24}, {39, 60}, {15, 28}, {27, 40}, {50, 90} }, then the longest chain that can be formed is of length 3, and the chain is {{5, 24}, {27, 40}, {50, 90}}

This problem is a variation of standard Longest Increasing Subsequence problem. Following is a simple two step process.
1) Sort given pairs in increasing order of first (or smaller) element.
2) Now run a modified LIS process where we compare the second element of already finalized LIS with the first element of new LIS being constructed.
'''

class Pair:
    def __init__(self,a,b):
        self.a = a 
        self.b = b 

a = [Pair(5,24),Pair(15, 25), Pair(27, 40), Pair(50, 60)]

def max_len_chain(a):
    n = len(a)

    T = [1 for i in range(n)]

    for i in range(1,n):
        for j in range(i):
            if a[i].a > a[j].b:
                T[i] = max(T[i],T[j]+1)
    return max(T)

print max_len_chain(a)
