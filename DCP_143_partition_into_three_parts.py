a = [9,12,3,5,14,10,10]

def keep_left(a,x):
    l = 0
    m = 1
    h = len(a)-1
    while m < h:
        if a[m] == x:
            m += 1
        elif a[m] < x:
            a[l],a[m] = a[m],a[l]
            l += 1
            m += 1
        else:
            a[m],a[h] = a[h],a[m]
            h -= 1
    return a 

print keep_left(a,10)

        
        