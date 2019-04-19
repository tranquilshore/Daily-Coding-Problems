'''
Scan the array and compute Maximum, second maximum and third maximum element present in the array.
Scan the array and compute Minimum and second minimum element present in the array.
Return the maximum of product of Maximum, second maximum and third maximum and product of Minimum, second minimum and Maximum element
'''
import sys 
a = [10, 3, 5, 6, 20]
a = [-10, -3, -5, -6, -20]
a = [1, -4, 3, -6, 7, 0]

def max_triplet(a,n):
    maxA = maxB = maxC = -sys.maxint-1
    minA = minB = sys.maxint
    i = 0
    while i < n:
        if a[i]>maxA:
            maxC = maxB
            maxB = maxA
            maxA = a[i]
        elif a[i]>maxB:
            maxC = maxB
            maxB = a[i]
        elif a[i]>maxC:
            maxC = a[i]
        
        if a[i] < minA:
            minB = minA
            minA = a[i]
        elif a[i] < minB:
            minB = a[i]
        i += 1
    
    return max(minA*minB*maxA, maxA*maxB*maxC)

print max_triplet(a,len(a))