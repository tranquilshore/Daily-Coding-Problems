'''
https://www.geeksforgeeks.org/find-triplet-sum-two-equals-third-element/
Given an array of integers you have to find three numbers such that sum of two elements equals the third element.
Examples:

Input : {5, 32, 1, 7, 10, 50, 19, 21, 2}
Output : 21, 2, 19

Approach:
1. Sort the array first.
2. Start fixing the greatest element of three from back and traverse the array to find other two numbers which sum upto the third element.

O(n^2)
'''

a = [5, 32, 1, 7, 10, 50, 19, 21, 2]

def triplets(a):
    n = len(a)
    a.sort()

    k = n-1 #index of last element to be fixed
    while k>=0:
        i = 0
        j = k-1
        while i<j:#same sorting logic of find a pair
            if a[k] == a[i]+a[j]:
                print "pairs are ",a[k],a[i],a[j]
                return 
            elif a[k]>a[i]+a[j]:
                i += 1
            else:
                j -= 1
        k -= 1

    print "no pair exist"
    return 

triplets(a)

'''
Find a triplet that sum to a given value

For example, if the given array is {12, 3, 4, 1, 6, 9} and given sum is 24, then there is a triplet (12, 3 and 9) present in array whose sum is 24.

O(n^2) approach

1) Sort the input array.
2) Fix the first element as A[i] where i is from 0 to array size-2. After fixing the first element of triplet, find the other two elements using method 1 of this post.
'''
a = [1, 4, 45, 6, 10, 8] 
target = 22

def triplet_sum(a,target):
    n = len(a)
    a.sort()

    for i in range(n-2):
        l = i+1
        r = n-1
        while l<r:
            if a[i]+a[l]+a[r] == target:
                print "triplet :",a[i],a[l],a[r]
                return True 
            elif a[i]+a[l]+a[r] < target:
                l += 1
            else:
                r -= 1
    return False

triplet_sum(a,target)