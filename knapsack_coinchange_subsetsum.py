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

