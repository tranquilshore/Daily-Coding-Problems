'''
for easiest explanation watch https://www.youtube.com/watch?v=76-CYD0jn7s
'''

import sys 
a = [100,80,120,130,70,60,100,125]

def maximum_profit(a):
    n = len(a)
    profit = 0
    min_price = sys.maxint

    for i in range(n):
        min_price = min(a[i], min_price)
        profit = max(profit,a[i]-min_price)
    
    return profit

print maximum_profit(a)


         