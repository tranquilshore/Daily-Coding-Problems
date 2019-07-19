'''
idea is to find max sum everytime we find including and excluding sum
incl: tells what is the maximum sum you can do till a certain point including that number
excl: tell what is the maximum sum you can do excluding that number.
'''

import sys 
a = [5, 5, 10, 100, 10, 5]
a = [1,2,3]
a = [1,20,3]
a = [1,2]
a = [1]
a = []

def max_sum_no_adjacent(a):
    n = len(a) 
    
    incl = excl = 0 
    for i in range(n):
        temp = incl 
        incl = max(incl,excl+a[i])
        excl = temp 
    return max(excl,incl)

print max_sum_no_adjacent(a)
          
      