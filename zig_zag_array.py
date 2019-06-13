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