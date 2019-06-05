'''
How to find the largest number with given digit sum s and number of digits d?

Examples:

Input  : s = 9, d = 2
Output : 90

Input  : s = 20, d = 3
Output : 992

Greedy approach to solve the problem. The idea is to one by one fill all digits from leftmost to rightmost (or from most significant digit to least significant).
'''

s = 20
d = 3

def find_largest(s,d):
    if s == 0:
        if d == 1:
            print "0"
        else:
            print "Not possible"
        return 
    
    if s > 9*d:
        print "Not possible"
        return 
    
    res = [0]*d 
    for i in range(d):
        #fill 9 first to make the number largest
        if s >= 9:
            res[i] = 9
            s -= 9
        else:#if remaining sum becomes less than 9 then just fill it
            res[i] = s 
            s = 0 
    return res 

print find_largest(s,d)

