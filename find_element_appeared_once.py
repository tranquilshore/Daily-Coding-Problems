#can be done using binary search O(logn)
a = [1,1,3,3,4,4,5,6,6]
n = len(a)

def search(a,low,high):
    if low>high:
        return None 
    if low == high:
        return a[low]
    
    mid = low +(high-low)/2

    # If mid is even and element next to mid is 
    # same as mid, then output element lies on 
    # right side, else on left side

    if mid%2 == 0:
        if a[mid] == a[mid+1]:
            return search(a,mid+2,high)
        else:
            return search(a,low,mid)
    else:
        if a[mid] == a[mid-1]:
            return search(a,mid+1,high)
        else:
            return search(a,low,mid)

print search(a,0,n-1)