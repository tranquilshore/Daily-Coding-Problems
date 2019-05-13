'''
idea is to find the pivot from where the array has been rotated after that just use binary search on both the sides as those sides are sorted.
Hence time complexity will remain O(logn)
'''

a = [6,7,8,1,2,3,4,5]
a = [4,5,1,2,3]
a = [4,5,6,7,8,9,1,2,3]

def pivoted_binary_search(a,key):
    pivot = find_pivot(a,0,len(a)-1)

    if pivot == -1:
        return binary_search(a,0,len(a)-1,key)

    if a[pivot] == key:
        return pivot
    if a[0] < key:
        return binary_search(a,0,pivot-1,key)
    return binary_search(a,pivot+1,len(a)-1,key)

def find_pivot(a,low,high):
    if high<low:
        return -1
    mid = int((low+high)/2)

    if mid < high and a[mid] > a[mid+1]:
        return mid 
    if mid > low and a[mid] < a[mid-1]:
        return mid-1
    if a[low] > a[mid]:
        return find_pivot(a,low,mid-1)
    return find_pivot(a,mid+1,high)

def binary_search(a,low,high,key):
    if high < low:
        return -1
    mid = int((low+high)/2)
    if key == a[mid]:
        return mid 
    if key > a[mid]:
        return binary_search(a,mid+1,high,key)
    return binary_search(a,low,mid-1,key)

print pivoted_binary_search(a,2)