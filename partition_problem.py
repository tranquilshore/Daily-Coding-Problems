'''
partition problem is same as subset sum problem solved below.
to see if we can partition a set into two subsets with equal sum or not we just need to check if the whole sum of set is even and then 
find the subset with sum as (whole sum)/2. if we can do that then we can partition the set
'''
a = [15, 5, 20, 10, 35, 15, 10]
target = 55

def subset_sum(a,n,target):
    if target == 0:
        return True 

    if n < 0 or target < 0:
        return False 

    incl = subset_sum(a,n-1,target-a[n])
    excl = subset_sum(a,n-1,target)

    return incl or excl 

print subset_sum(a,len(a)-1,target)

lookup = {}
def subset_sum_dp(a,n,target):
    if target == 0:
        return True 

    if n < 0 or target < 0:
        return False 

    key = str(n)+"|"+str(target)
    if lookup.has_key(key) == False:
        incl = subset_sum_dp(a,n-1,target-a[n])
        excl = subset_sum_dp(a,n-1,target)
        lookup[key] = incl or excl
    return lookup[key]

print subset_sum_dp(a,len(a)-1,target)