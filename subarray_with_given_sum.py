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

'''
find pair/pairs with given sum
O(n)
'''

a = [8,7,2,5,3,1]
target = 10 

def pair_sum(a,target):
    n = len(a)
    d = {}

    for i in range(n):
        if d.has_key(target-a[i]):
            print "at index ",d[target-a[i]]," and ", i 
        d[a[i]] = i 

print pair_sum(a,target)

'''
Four sum problem
unsorted array is given check if it contains four elements with given sum

Idea: take all the pairs and solve it like find pairs problem like above
O(n^2) solution
'''
from collections import defaultdict

a = [2,7,4,0,9,5,1,3]
target = 20 

def four_sum(a,target):
    n = len(a)
    d = defaultdict(list)

    for i in range(n):
        for j in range(i+1,n):
            if d.has_key(target - (a[i]+a[j])):
                tmp = d[target - (a[i]+a[j])]
                #to make sure there is no repeated element
                if tmp[0] != i and tmp[0] != j and tmp[1] != i and tmp[1] != j:
                    print tmp[0],tmp[1],"|",i,j 
                    return True 

            d[a[i]+a[j]] = (i,j)
four_sum(a,target)

'''
swapping pairs make sum equal

Find a pair in two array swapping which makes the sum of both the arrays same.
Idea- 
We are looking for two values, a and b, such that: 
sumA - a + b = sumB - b + a
    2a - 2b  = sumA - sumB
      a - b  = (sumA - sumB) / 2

      that means a = (sumA-sumB)/2 + b
we need to find above a in array A

O(n+m) complexity
'''

a=[4, 1, 2, 1, 1, 2]
b=[3, 6, 3, 3]

# a = [5, 7, 4, 6]
# b = [1, 2, 3, 8]

def swap_pairs(a,b):
    sum1 = sum(a)
    sum2 = sum(b)
    d = defaultdict(int)
    diff = (sum1-sum2)/2

    for i in a:
        d[i] += 1 

    for i in b:
        if d.has_key(diff+i):
            print diff+i,"|",i 
            return True 
    
    return False 

swap_pairs(a,b)
        

    

    
