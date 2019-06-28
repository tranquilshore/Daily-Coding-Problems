'''
majority element's count will be more than n/2
Given elements are in sorted order
'''

a = [3,4,5,5,6,6,6,6,6,6]
x = 6 

def find_index(a,x,flag):
    low = 0 
    high = len(a) - 1 
    result = -1
    while low <= high:
        mid = (low+high)/2
        result = mid  
        if a[mid] == x:
            if flag:
                high = mid-1 
            else:
                low = mid+1 
        elif x < a[mid]:
            high = mid - 1 
        else:
            low = mid + 1 
    return result

firstindex = find_index(a,x,True)
lastindex = find_index(a,x,False) 
print lastindex-firstindex