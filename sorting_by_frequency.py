from collections import defaultdict

d = defaultdict(int)

a = [2, 5, 2, 8, 5, 6, 8, 8]

def frequency_sort(a):
    n = len(a) 
    for i in a: #O(n) operation
        d[i] += 1

    tmp_arr = []
    for key,value in d.items():
        tmp_arr.append((key,value))
    
    res = sorted(tmp_arr,key= lambda item:item[1],reverse=True) #O(mlogm) m are distinct items
    return res 

print frequency_sort(a)

'''
If two key has same frequency then create a dictionary of key and index and from there find which come first.
After this time complexity will be:
O(n) + O(mlogm)
'''