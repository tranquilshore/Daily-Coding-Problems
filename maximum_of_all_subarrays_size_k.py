'''
Given an array and integer k, find the maximum for each and every contiguous subarray of size k.
Idea is to create a deque of capacity k, stores only useful elements. An element is useful if it is 
greater than all other elements on left side of it in current window.

Imp: we will enter indexes of the elements into deque.

keep appending if no element in deque or if appending value is less than the rightmost value,
keep poping the existing elements if appending element is greater than the existing elements.

these above two rules will make sure than we have the maximum element in deque at the leftmost spot.
keep moving and extracting the largest from the window and take care of removing the element from deque if its not present in that window.

At the end we will have the result. Time taken will be linear O(n) as every element get added and removed 
from the deque only twice which is O(2n) ie O(n).

'''

from collections import deque

a = [12,1,78,90,57,89,56]
k = 3
def get_max(a,n,k):
    dq = deque()

    for i in range(k):
        while dq and a[i] >= a[dq[-1]]:
            dq.pop()
        dq.append(i)
    
    for i in range(k,n):
        print a[dq[0]],

        while dq and dq[0] <= i-k:#take care of element not in window
            dq.popleft()

        while dq and a[i] >= a[dq[-1]]:
            dq.pop()
        
        dq.append(i)
    print a[dq[0]]

get_max(a,len(a),k)