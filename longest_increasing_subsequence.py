'''
given integer array, find the longest subsequence s.t. all the elements in the subsequence are sorted(ascending).
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
