'''
Given arrival and departure times of all trains, find the minimum number of platforms required so that no train waits.
approach:
idea is to consider all events in sorted order, don't create the single sorted list of all events, rather individually sorts arrays and then use
merge process of merge sort to process them together as a single sorted array.
'''

arr = [2,2.1,3,3.2,3.5,5]
dep = [2.3,3.4,3.2,4.3,4,5.2]
n = len(arr)

def minimum_platforms(arr,dep,n):
    arr.sort()
    dep.sort()

    platform_needed = result = i = 1
    j = 0

    while i<n and j<n:
        if arr[i] < dep[j]:
            platform_needed += 1
            i += 1
            if platform_needed > result:
                result = platform_needed
        else:
            platform_needed -= 1
            j += 1
    
    return result 

print minimum_platforms(arr,dep,n)
