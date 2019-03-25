a = [12,19,23,66,75,81,92,95,99]

def binary_search(a,low,high,key):
    if high < low:
        return -1
    mid = int((low+high)/2)
    if key == a[mid]:
        return mid 
    if key > a[mid]:
        return binary_search(a,mid+1,high,key)
    return binary_search(a,low,mid-1,key)

print binary_search(a,0,len(a)-1,100)
