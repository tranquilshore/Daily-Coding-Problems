a = [3,4,9,6,1]

#using the help of position_to_insert_in_sorted_array problem
def left_position(a,x,lo=0,hi=None):
    if lo < 0:
        raise ValueError('lo can not be negative!')
    if hi == None:
        hi = len(a)
    while lo<hi:
        mid = (lo+hi)//2 
        if a[mid]<x:
            lo = mid + 1
        else:
            hi = mid 
    return lo 

#take n*logn time better than n^2
def count_smaller_array(a):
    s = []
    ans = []
    for i in reversed(a):
        pos = left_position(s,i)#find the position of elem from reversed of list in s, takes logn time
        ans.append(pos)#that pos will be the ans at that index
        s.insert(pos,i)#insert at sorted place, takes n time
    return ans 

print list(reversed(count_smaller_array(a)))