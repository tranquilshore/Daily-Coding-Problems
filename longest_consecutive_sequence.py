'''
Given an array of integers,find the length of the longest subsequence such that elements in the subsequence are consequtive integers.
eg. [10,4,200,1,2,3] - ans is 4 including [1,2,3,4]

Approach:
Put every element into the dictionary as keys and their indices as values.
Start from first element of the array and see if that element minus 1 is in the dictionary or not!(if it is in dictionary that means current 
element will be a part of sequence, can't consider the start of new sequence)
if element - 1 is not present in dictionary we can consider it to be a start of one of the sequence, then we keep adding 1 to every element
and keep checking if it is present in dictionary or not. if it is present we'll add that to output else move to next element of array.
'''

def largest_consecutive_sequence(a):
    d = {}
    ans = 0
    n = len(a)

    for i in range(n):
        d[a[i]] = i 
    
    for i in a:
        if d.has_key(i-1) == False:
            temp = i 
            while d.has_key(temp):
                temp += 1 
            if ans < temp-i:
                ans = temp-i 
    return ans 

a = [100,4,200,1,2,3]
print largest_consecutive_sequence(a)
    