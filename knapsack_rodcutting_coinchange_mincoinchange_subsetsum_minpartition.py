#01 knapsack

#recursive
import sys 
values = [20,5,10,40,15,25]
weights = [1,2,3,8,7,4]

capacity = 10
n = len(values)

def knapsack(values,weights,n,capacity):
    if capacity < 0:
        return -sys.maxint

    if n < 0 or capacity == 0:
        return 0

    #include current item and recur for remaining items with decreased capacity
    include = values[n] + knapsack(values,weights,n-1,capacity-weights[n])
    #exclude current item and recur for remaining items
    exclude = knapsack(values,weights,n-1,capacity)
    return max(include,exclude)

print knapsack(values,weights,n-1,capacity)

#dp top down
lookup = {}
def knapsack_topdown(values,weights,n,capacity):
    if capacity < 0:
        return -sys.maxint 

    if n < 0 or capacity == 0:
        return 0 
    
    key = str(n) + "|" +str(capacity)
    if lookup.has_key(key) == False:
        incl = values[n] + knapsack_topdown(values,weights,n-1,capacity-weights[n])
        excl = knapsack_topdown(values,weights,n-1,capacity)
        lookup[key] = max(incl,excl)
    return lookup[key]
print knapsack_topdown(values,weights,n-1,capacity)

#dp bottom up
def knapsack_bottomup(values,weights,capacity):
    n = len(values)
    m = capacity

    T = [[0 for i in range(m+1)] for i in range(n+1)]
    #keep first row and column 0 because no profit can be made without any capacity and without any element

    for i in range(1,n+1):
        for j in range(1,m+1):
            if weights[i-1]>j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j],values[i-1]+T[i-1][j-weights[i-1]])
    return T[n][m]

print knapsack_bottomup(values,weights,capacity)
###############################################################################################################################################
#rod cutting is same as knapsack 
#important - only difference is that infinite rod cuts can be taken into consideration

length = [1,2,3,4,5,6,7,8]
profit = [1,5,8,9,10,17,17,20]
target = 8
n = len(profit)-1
import sys 
def rod_cut_profit(length,profit,n,target):
    if target==0:
        return 0
    if target < 0 or n<0:
        return -sys.maxint
    incl = profit[n] + rod_cut_profit(length,profit,n,target-length[n]) #only change is we recurse with same n (as infinite cuts are allowed)
    excl = rod_cut_profit(length,profit,n-1,target)
    return max(incl,excl)

print rod_cut_profit(length,profit,n,target)

#dp solution will be the same as of knapsack above with just a minute change that we will look at the same row


###############################################################################################################################################

#coin change (Total number of ways)

#recursive
s = [1,3,5,7]
target = 8
n = len(s)
def coin_change_ways(s,n,target):

    if target == 0:
        return 1
    if n < 0 or target < 0:
        return 0

    #include current coin and recur with remaining change(N-s[n]) with same number of coins
    incl = coin_change_ways(s,n,target-s[n])
    #exclude current coin and recur with remaining coins
    excl = coin_change_ways(s,n-1,target)

    return incl+excl

print coin_change_ways(s,n-1,target)

#dp top down
lookup = {}
def coin_change_ways_topdown(s,n,target):
    if target == 0:
        return 1
    if n < 0 or target < 0:
        return 0 
    key = str(n)+"|"+str(target)

    if lookup.has_key(key) == False:
        incl = coin_change_ways_topdown(s,n,target-s[n])
        excl = coin_change_ways_topdown(s,n-1,target)
        lookup[key] = incl+excl
    return lookup[key]

print coin_change_ways_topdown(s,n-1,target)

#dp bottom up
def coin_change_ways_bottomup(s,target):
    n = len(s)
    m = target 

    T = [[0 for i in range(m+1)] for i in range(n+1)]

    #first column has just 1 way to make target 0 which is just to have nothing
    for i in range(n+1):
        T[i][0] = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1]>j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = T[i-1][j] + T[i][j-s[i-1]]
    return T[n][m]

print coin_change_ways_bottomup(s,target)

####################################################################################################################################
#coin change (minimum number of coins)

s = [1,2,3,4]
target = 15

n = len(s)-1

def minimum_coins(s,n,target):
    if target == 0:
        return 0
    if n<0 or target<0:
        return sys.maxint
    
    incl = 1+minimum_coins(s,n,target-s[n]) #as we including a coin add 1
    excl = minimum_coins(s,n-1,target)
    return min(incl,excl)

print minimum_coins(s,n,target)

def find_min_coins_bottomup(s,target):
    n = len(s)
    m = target

    T = [[0 for i in range(m+1)] for i in range(n+1)]

    for i in range(m+1):
        T[0][i] = sys.maxint

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1] > j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = min(T[i-1][j], T[i][j-s[i-1]] + 1)

    return T[n][m]

print find_min_coins_bottomup(s,target)

####################################################################################################################################

#subset sum problem

#recursive
s = [2,4,2,1]
target = 5 

def subsetsum(s,n,target):
    if target == 0:
        return True 
    if n<0 or target < 0:
        return False 
    incl = subsetsum(s,n-1,target-s[n])
    excl = subsetsum(s,n-1,target)
    return incl or excl

print subsetsum(s,n-1,target)

#dp top down 
lookup = {}

def subsetsum_topdown(s,n,target):
    if target == 0:
        return True 
    if n < 0 or target < 0:
        return False 
    
    key = str(n)+"|"+str(target)
    if lookup.has_key(key) == False:
        incl = subsetsum(s,n-1,target-s[n])
        excl = subsetsum(s,n-1,target)
        lookup[key] = incl or excl
    return lookup[key]

print subsetsum_topdown(s,n-1,target)

#dp bottom up 
def subsetsum_bottomup(s,target):
    n = len(s)
    m = target 

    T = [[False for i in range(m+1)] for i in range(n+1)]

    #if target is 0 then we can get that by excluding every element everytime so it will always be true
    for i in range(n+1):
        T[i][0] = True
    
    for i in range(n+1):
        for j in range(m+1):
            if s[i-1]>j:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = T[i-1][j] or T[i-1][j-s[i-1]]
    return T[n][m]

print subsetsum_bottomup(s,target)

####################################################################################################################################

#minimum sum partition
#idea is same to include an element in one set and exclude it from it and add it to another set

s = [10,20,15,5,25]
#s = [36,7,46,40]
n = len(s)


#recursive
def minimum_sum_partition(s,n,s1,s2):#s1 and s2 are sum of two subsets
    if n < 0: #if list becomes empty
        return abs(s1-s2)
    
    #include current item in the subset 1 and recur for remaining items
    incl = minimum_sum_partition(s,n-1,s1+s[n],s2)
    #exclude the current item from subset 1 and recur for remaining items
    excl = minimum_sum_partition(s,n-1,s1,s2+s[n])
    return min(incl,excl)

print minimum_sum_partition(s,n-1,0,0)

#dp top down
lookup = {}
def minimum_sum_partition_topdown(s,n,s1,s2):
    if n < 0:
        return abs(s1-s2)
    key = str(n)+"|"+str(s1)
    if lookup.has_key(key) == False:
        incl = minimum_sum_partition_topdown(s,n-1,s1+s[n],s2)
        excl = minimum_sum_partition_topdown(s,n-1,s1,s2+s[n])
        lookup[key] = min(incl,excl)
    return lookup[key]

print minimum_sum_partition_topdown(s,n-1,0,0)






