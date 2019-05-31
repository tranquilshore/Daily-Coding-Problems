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
