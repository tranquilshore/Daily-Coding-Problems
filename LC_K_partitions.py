'''
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
nums = [1,1,3,2,2] , k = 3 
output = yes as ([1,2],[1,2],[3])
'''

'''
backtracking solution without any optimizations

just create partitions which only holds sum as only yes/no answer is required. partition size will be k 
try adding an element one by one and if can't then backtrack. 
can use this link to understand https://www.youtube.com/watch?v=O17fztIRR3I 


                                                                0,0,0 | 1
                                                             /
                                                        1,0,0 | 1 
                                            /                             \
                                        2,0,0 | 3                           1,1,0 | 3
                                   /                \                        /
                            2,3,0 | 2             2,0,3 | 2 (*)            1,1,3 | 2
                            /        \            /         \              /
                        2,3,2 | 2     (x)     2,2,3 | 2     (x)        3,1,3 | 2
                          (x)                   (x)                       /   
                                                                    3,3,3 | (end of array)
                                                                        (ans)

'''
nums = [1,1,3,2,2]
k = 3 

def can_k_partitions(nums,k):
    n = len(nums)
    
    #base cases
    if k > n or k == 0: #can't split array to more than it's length and can't make 0 splits
        return False 
    
    rem = sum(nums)%k 
    if rem:
        return False #if k can't completely divides the array sum then we can't split it fractionally

    target = sum(nums)/k #target sum for every k partitions
    partition_sums = [0]*k 

    def search(i):
        if i == n:
            return True 
        v = nums[i]

        for j,part in enumerate(partition_sums):
            if part+v <= target:
                partition_sums[j] += v #consider
                if search(i+1):
                    return True 
                partition_sums[j] -= v #backtrack 
        return False 
    
    return search(0)

print can_k_partitions(nums,k)
     

'''
optimizations:
1. sort the items and take items from end one by one, like maximum first and so on. So that we can fail early. Less subtrees would create.
2. can optimize at the (*) step above in the drawn recursion tree, as removing 3 from prev and putting in next makes the same situation. so whenever removing an element(while backtracking)
    leads to 0 sum partition, then just break break the recursion there.
'''


def can_k_partitions_optmzd(nums,k):
    n = len(nums)
    
    #base cases
    if k > n or k == 0: #can't split array to more than it's length and can't make 0 splits
        return False 
    
    rem = sum(nums)%k 
    if rem:
        return False #if k can't completely divides the array sum then we can't split it fractionally

    target = sum(nums)/k #target sum for every k partitions
    
    partition_sums = [0]*k 

    nums.sort() #optimize step 1

    #important base case
    if nums[-1] > target: #if an element like that exists then we can't put that element in any partition
        return False 

    def search():
        if not nums: #if array is empty
            return True 
        v = nums.pop()

        for j,part in enumerate(partition_sums):
            if part+v <= target:
                partition_sums[j] += v #consider
                if search():
                    return True 
                partition_sums[j] -= v #backtrack 
            
            if not part: #optimize step 2
                break 
        nums.append(v) #backtrack (important step because of step 1)
        return False 
    
    return search()

print can_k_partitions_optmzd(nums,k)