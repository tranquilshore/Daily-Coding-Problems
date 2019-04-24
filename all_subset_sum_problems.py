'''
Subset Sum Problem:
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
Return the subset as well. Done using DP. Watch this for proper explanation: https://www.youtube.com/watch?v=s6FhG--P7z0
'''

target = 7
a = [3,2,6,4]

target = 6
a = [3,8,1,2]

target = 24
a = [12, 1, 61, 5, 9, 2]

T = [[0 for i in range(target+1)] for i in range(len(a))]

def subset_sum_or_not(a,target,T):
    n = len(a)

    for i in range(n):
        T[i][0] = True
    
    for i in range(1,target+1):
        if a[0] == i:
            T[0][i] = True 
        else: 
            T[0][i] = False 
    
    for i in range(1,n):
        for j in range(1,target+1):
            if a[i] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = T[i-1][j] or T[i-1][j-a[i]]
    
    return T[n-1][target]

print subset_sum_or_not(a,target,T)

#traverse the array from bottom right to top left and follow the rules mentioned in the video mentioned above
def print_subset(T):
    r = len(T)-1
    c = len(T[0])-1
    while r >= 0 and c >= 0:
        if r == 0 and T[r][c] == True:
            print a[r],
        if T[r-1][c] == False:
            print a[r],
            c -= a[r]
            r -= 1
        else:
            r -= 1
    
print_subset(T)

'''
***********************************************************************************************************************************************
Top down dp solution to just find whether subset sum exists in the array or not.
It can be thought as a special case of 0-1 knapsack problem. For each item, there are two possibilities:

1. We include the current item in the subset and recurse for remaining items with remaining sum
2. We exclude the current item from subset and recurse for remaining items.
'''

lookup = {}
def subset_sum_or_not_topdown(a,n,target):
    #if target becomes 0 return true, subset found
    if target == 0:
        return True 

    if n < 0 or target < 0:
        return False 

    key = str(n) + "|" + str(target)

    if lookup.has_key(key) == False:
        include = subset_sum_or_not_topdown(a,n-1,target-a[n])#possibility 1
        exclude = subset_sum_or_not_topdown(a,n-1,target)#possiblity 2
        lookup[key] =  include or exclude

    return lookup[key]

print subset_sum_or_not_topdown(a,len(a)-1,target)

'''
*********************************************************************************************************************************************
Combinational Sum 1:
Given non negative integers and a target number, find all unique subsets where sum of those subsets equal to target.
To find all such subsets, we need to use backtracking:
Watch this to see how we need to create state space tree https://www.youtube.com/watch?v=j9_qWJClp64
'''
a = [10,1,2,7,6,1,5]
target = 8

#sort the input array before doing the dfs
def combinational_sum(a,target):
    n = len(a)
    res = []
    cand = []
    a.sort()

    def backtrack(start=0, partial=0):
        if partial == target:
            res.append(cand[:])
        else:
            for j in range(start,n):
                if partial+a[j] > target:
                    break 
                elif j>start and a[j]==a[j-1]:#takes care of duplicates 
                    continue 
                cand.append(a[j])
                backtrack(j+1,partial+a[j])
                cand.pop() #backtrack step 
    
    backtrack()
    return res 

print combinational_sum(a,target)

'''
****************************************************************************************************************************************************
Combinational Sum 2:
Same problem as above, but now the same numer may be chosen from array unlimited number of times.
Watch this to see the state space tree formation: https://www.youtube.com/watch?v=irFtGMLbf-s&t=745s 
'''
a = [4,2,6,8]
target = 8 
res = []
cand = []

a.sort() #sort the array before dfs

def combinational_sum_2(a,target,res,cand,i=0):
    if target < 0:
        return 
    if target == 0:
        res.append(cand[:])
        return 
    while i<len(a) and target-a[i] >= 0:
        cand.append(a[i])
        combinational_sum_2(a,target-a[i],res,cand,i) #keeping i same for choosing the element unlimited number of times
        i+=1
        cand.pop()


combinational_sum_2(a,target,res,cand)

print res 








