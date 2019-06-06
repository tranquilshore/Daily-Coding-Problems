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

'''
Largest subarray with 0 sum
'''

a = [15,-2,2,-8,1,7,10,23]

def largest_subarray_zero_sum(a):
    n = len(a)
    d = {}

    curr_sum = 0
    max_len = 0 

    for i in range(n):
        curr_sum += a[i]

        if a[i] == 0 and max_len == 0:#if an element with value 0 is present
            max_len = 1
        
        if curr_sum == 0: #if that subarray starts from the starting index
            max_len = i+1 

        if curr_sum in d:
            max_len = max(max_len,i-d[curr_sum])
        else:
            d[curr_sum] = i 
    return max_len

print largest_subarray_zero_sum(a)
        

    

    
