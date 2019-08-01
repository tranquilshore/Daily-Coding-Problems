'''
reversing it by swaping will take n*k swaps which will be its time complexity
by below reverse logic, it will take linear time O(3n)=O(n) to rotate an array
'''

a = [1,2,3,4,5,6]
n = len(a)
k = 2 

def reverse(a,l,r):
    while l<r:
        a[l],a[r] = a[r],a[l]
        l += 1
        r -= 1 

reverse(a,0,k-1)
reverse(a,k,n-1)
reverse(a,0,n-1)
print a 

    