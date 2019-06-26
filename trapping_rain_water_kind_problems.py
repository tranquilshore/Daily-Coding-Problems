'''
water contributed by a single building on an index is calculated as:

minimum (max height building on left side , max height building on right side) - own height on that index 
so to do this in linear time, we need two array to keep left max and right max
'''

a = [3,0,0,2,0,4]
n = len(a)

def water_capacity(a,n):
    leftmax = [0]*n
    rightmax = [0]*n 
    water = 0 

    leftmax[0] = a[0]
    for i in range(1,n):
        leftmax[i] = max(a[i],leftmax[i-1]) #here its a[i] and not a[i-1] later questions has that

    rightmax[n-1] = a[n-1]
    for i in range(n-2,-1,-1):
        rightmax[i] = max(a[i],rightmax[i+1])
    
    for i in range(n):
        water += min(leftmax[i],rightmax[i]) - a[i]

    return water 

#print water_capacity(a,n)

'''
Find the element before which all the elements are smaller than it, and after which all are greater

find left max array and right min array and find if a[i] sits in between
'''
import sys 

a = [5,1,4,3,6,8,10,7,9]
n = len(a)

def find_partition(a,n):
    leftmax = [0]*n 
    rightmin = [0]*n 

    leftmax[0] = -sys.maxint
    for i in range(1,n):
        leftmax[i] = max(a[i-1],leftmax[i-1]) #difference is its a[i-1]
    
    rightmin[n-1] = sys.maxint 
    for i in range(n-2,-1,-1):
        rightmin[i] = min(a[i+1],rightmin[i+1])
    
    for i in range(n):
        if a[i] > leftmax[i] and a[i]<rightmin[i]:
            return i 
    return False 

#print find_partition(a,n)

'''
Given an array arr[], find the maximum j - i such that arr[j] > arr[i]
https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/

Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
Output: 6  (j = 7, i = 1)

idea:

unlike above problem where we keep leftmax and right min
here we need to keep leftmin and rightmax and at the end use merge procedure to find the max j - i 
'''

a = [9,2,3,4,5,6,7,8,18,0]
n = len(a)

def max_index_diff(a,n):
    leftmin = [0]*n 
    rightmax = [0]*n 

    leftmin[0] = a[0]
    for i in range(1,n):
        leftmin[i] = min(a[i],leftmin[i-1])
    
    rightmax[n-1] = a[n-1]
    for i in range(n-2,-1,-1):
        rightmax[i] = max(a[i],rightmax[i+1])
    
    maxdiff = -1
    i = j = 0
    #merge sort type procedure to find max j-i
    while i<n and j <n:
        if leftmin[i] < rightmax[j]:
            maxdiff = max(maxdiff,j-i)
            j += 1
        else:
            i += 1

    return maxdiff

print max_index_diff(a,n)
