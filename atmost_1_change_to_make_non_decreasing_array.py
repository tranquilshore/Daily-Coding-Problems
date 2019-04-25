'''
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

At first glance, it looks like an easy and straightforward problem, but believe me it's greedy problem. In the problem, you are allowed to make atmost "one" modification to make a non-decreasing array.
read this to understand approach http://nirajsdatabase.blogspot.com/2017/08/given-array-with-n-integers-your-task.html 
'''

a = [10,5,9]
n = len(a)

def check(a,n):
    count = 0
    for i in range(n-1):
        if count <= 1:
            if a[i] > a[i+1]:
                if i>0:
                    if a[i-1] <= a[i+1]: #if number is lesser or equal then modify
                        a[i] = a[i-1]
                    else:
                        a[i+1] = a[i] #modify next less element to current element, use [2,5,12,4,15] as eg to understand this use case
                count += 1
    return count <= 1

print check(a,n)
print a 
