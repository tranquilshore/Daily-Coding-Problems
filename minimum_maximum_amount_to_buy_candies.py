'''
https://www.geeksforgeeks.org/find-minimum-maximum-amount-buy-n-candies/
In a candy store there are N different types of candies available and the prices of all the N different types of candies are provided. There is also an attractive offer by candy store. We can buy a single candy from the store and get at-most K other candies (all are different types) for free.

Find minimum amount of money we have to spend to buy all the N different candies.
Find maximum amount of money we have to spend to buy all the N different candies.
In both the cases we must utilize the offer and get maximum possible candies back. If k or more candies are available, we must take k candies for every candy purchase. If less than k candies are available, we must take all candies for a candy purchase.
eg.

Input :  price[] = {3, 2, 1, 4}
               k = 2
Output :  Min = 3, Max = 7

First Sort the price array.

For finding minimum amount :
  Start purchasing candies from starting 
  and reduce k free candies from last with
  every single purchase.

For finding maximum amount : 
   Start purchasing candies from the end 
   and reduce k free candies from starting 
   in every single purchase.
'''

a = [3,2,4,1]
n = len(a)
k = 2

a.sort()

def find_minimum(a,n,k):
    res = 0
    i = 0

    while n:
        #buy first candy
        res += a[i]
        #take k candy from back for free
        n = n-k
        i+=1
    return res 

def find_maximum(a,n,k):
    res = 0
    i = n-1 
    index = 0

    while i >= index:
        #buy candy from last
        res += a[i]
        #take first k candies free
        index += k 
        i -= 1
    
    return res 

print find_minimum(a,n,k), find_maximum(a,n,k)