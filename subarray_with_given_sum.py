'''
Find subarray with the given sum.
eg.
a = [3,2,7,1,6]
k = 10

subarray with sum 10 is [2,7,1]
'''

#will return only one subarray, use continue insted of break, if want to find all subarrays
def subarray_with_given_sum(a,n,k):
    d = {}
    curr_sum = 0
    for i in range(n):
        curr_sum += a[i]

        if curr_sum == k:
            return a[0:i+1] 
        
        if d.has_key(curr_sum-k):
            return a[d[curr_sum-k]+1:i+1] 
        
        d[curr_sum] = i

    return "Not found"

a = [3,2,7,1,6]
k = 10

a = [1,2,3,4,5]
k = 9
n = len(a)

print subarray_with_given_sum(a,n,k)
    

    
