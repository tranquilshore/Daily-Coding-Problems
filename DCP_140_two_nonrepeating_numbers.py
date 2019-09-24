arr = [2, 4, 6, 8, 10, 2, 6, 10]

'''
prerequisite:
1. check this to understand how to find rightmost set bit in a binary number https://www.techiedelight.com/bit-hacks-part-3-playing-rightmost-set-bit-number/
2. this to understand how algorithm works https://algorithms.tutorialhorizon.com/find-two-non-repeating-numbers-in-an-array-in-on-time-and-o1-space/
'''

def two_nonrepeating(arr):
    n = len(arr)
    xor = arr[0]

    for i in range(1,n):
        xor ^= arr[i] #will get rid of all duplicates only some new value containing the bits of x and y

    binary_with_only_rightmost_set_bit = xor^(xor&(xor-1)) #this bit will either be of x or y as xor of same should be 0 not 1
    
    a = 0
    b = 0 
    for i in range(n):
        x = arr[i]
        if x & binary_with_only_rightmost_set_bit != 0:
            a ^= x 
        else:
            b ^= x 
    return a,b 

print two_nonrepeating(arr)



