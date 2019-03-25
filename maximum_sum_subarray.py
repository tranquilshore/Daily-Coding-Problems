'''
kadane's algorithm: works in O(n) time
prerequisite - array should have atleast 1 positive element, if array has all negative elements we can write extra simple condition to find that.

idea:
to maximum sum subarray ending at i+1, we can add maximum subarray ending at i
maximum sum subarray ending at i could be positive or negative

if positive:
    add that value to the current value 
if negative:
    better off by not considering that subarray

i.e. why
if sum+a[i] < 0: sum = 0
if sum+a[i] > 0: sum += a[i]

as sum will reset everytime is becomes negative we will track the answer in another variable ans.

'''
a = [-2, -3, 4, -1, -2, 1, 5, -3]

def maximum_sum_subarray(a):
    n = len(a)
    ans = sum_ = 0

    for i in range(n):
        if sum_+a[i] > 0:
            sum_ += a[i]
        else:
            sum_ = 0
        
        if ans < sum_: # which is nothing but ans = max(ans,sum_)
            ans = sum_ 
    
    return ans

def maximum_sum_subarray_range(a):
    n = len(a)
    ans = sum_ = 0

    start = end = s = 0

    for i in range(n):
        if sum_+a[i] > 0:
            sum_ += a[i]
        else:
            sum_ = 0
            s = i+1 
        
        if ans < sum_:
            ans = sum_ 
            start = s 
            end = i 
    
    return ans, start, end 

print maximum_sum_subarray(a)
print maximum_sum_subarray_range(a)
        


