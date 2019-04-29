'''
Given a number n, find the smallest number that has same set of digits as n and is greater than n. If n is the greatest possible number with its set of digits, then print not possible.
eg.

Input:  n = "218765"
Output: "251678"

Input:  n = "1234"
Output: "1243"

Input: n = "4321"
Output: "Not Possible"

Idea:
watch https://www.youtube.com/watch?v=t_TMt_BFGiQ or https://www.geeksforgeeks.org/find-next-greater-number-set-digits/ 
'''

number = [2,1,8,7,6,5]
number = [4,3,2,1]
number = [1,2,3,4]
number = [5,3,4,9,7,6]
n = len(number)

def next_higher_number(number,n):

    # Start from the right most digit and find the first digit that is smaller than the digit next to it
    for i in range(n-1,0,-1):
        if number[i] > number[i-1]:
            break 
    # If no such digit found,then all numbers are in descending order, no greater number is possible
     
    if i-1 == 0:
        print "Next higher number is not possible"
        return 
    
    # Find the smallest digit on the right side of (i-1)th digit that is greater than number[i-1]
    x = number[i-1]
    smallest = i 
    for j in range(i+1,n):
        if number[j] > x and number[j] < number[smallest]:
            smallest = j 
    
    # Swapping the above found smallest digit with (i-1)th
    number[smallest], number[i-1] = number[i-1], number[smallest]

    #to get the prefix
    temp = number[:i]
    # Sort the digits after i-1 in ascending order
    number = sorted(number[i:])

    return temp+number 

print next_higher_number(number, n)

'''
The above implementation can be optimized in following ways.
1) We can use binary search in step II instead of linear search.
2) In step IV, instead of doing simple sort, we can apply some clever technique to do it in linear time. Hint: We know that all digits are linearly sorted in reverse order except one digit which was swapped.
'''


