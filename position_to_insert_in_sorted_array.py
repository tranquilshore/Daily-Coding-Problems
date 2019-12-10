
'''
This is what bisect library does in python.
It finds the position of a number to be added in a sorted list in logn time.
To insert it at that position will always take linear-n time.
'''


a = [2,3,7,7,9,11,13,19,29,31,59]

#finds the position of an element to be added in a sorted list in logn time.
#but it finds the left most position in a case when the item to be added already existed in a given sorted list.
def left_position(a,x,lo=0,hi=None):
    if lo<0:
        raise ValueError('lo must not be negative')
    if hi is None:
        hi = len(a)
    
    while lo<hi:
        mid = (lo+hi)//2 
        if a[mid]<x:
            lo = mid + 1 
        else:
            hi = mid #this is the main part, which is different in both functions as when a[mid] == x then this function changes hi but right_position function changes lo
    return lo 

#finds the position of an element to be added in a sorted list in logn time.
#but it finds the right most position in a case when the item to be added already existed in a given sorted list.
def right_position(a,x,lo=0,hi=None):
    if lo<0:
        raise ValueError('lo must not be negative')
    if hi is None:
        hi = len(a)
    
    while lo<hi:
        mid = (lo+hi)//2 
        if a[mid]>x:
            hi = mid 
        else:
            lo = mid + 1  
    return lo 

print left_position(a,7)
print right_position(a,7)