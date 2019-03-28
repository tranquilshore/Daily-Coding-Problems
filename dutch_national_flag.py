'''
Need to sort an array containing only 0,1 and 2 numbers. It needs to be done in linear time.
Idea is simple: just need to use 3 variables to keep track of 0s,1s and 2s and do necessary swaps when required.
'''

a = [0,1,1,0,1,2,0,1,2,0,2,1]

def dutch_national_flag(a):
    n = len(a)
    low = mid = 0
    high = n-1

    while mid <= high:
        if a[mid] == 0:
            a[low],a[mid] = a[mid],a[low]
            low += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[high],a[mid] = a[mid],a[high]
            high -= 1

    return a 

print dutch_national_flag(a)