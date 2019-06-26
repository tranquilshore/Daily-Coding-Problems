a = [1,7,3,4,9,6,11]

def zig_zag(a):
    n = len(a)
    flag = True 

    for i in range(n-1):
        if flag:
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
        else:
            if a[i] < a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
        flag = not flag 
    return a
print zig_zag(a)

'''
another type of rearrangement
https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form-set-2-o1-extra-space/

'''

#idea is that after final rearrangement first hald values of original arrays are at even indexes and second half values of original arrays at odd indexes
#so idea is to find the nextindex for first and second halfs using the formula below and 
a = [3,6,8,11]
n = len(a)

def rearrange(a,n):
    current_index = 0 
    current_val = a[0]
    count = 0 
    while count < n:
        if current_index < n/2:
            next_index = 2*current_index + 1
        else:
            next_index = 2*(n-1-current_index)
        
        next_val = a[next_index]
        a[next_index] = current_val 
        current_val = next_val 
        current_index = next_index 
        count += 1

rearrange(a,n)
print a 