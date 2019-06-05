def getmindiff(a,n,k):
    if n <= 1:
        return 0
    a.sort()
    maxe = a[n-1]
    mine = a[0]

    if k >= maxe - mine:
        return maxe-mine
    
    a[0] += k
    a[n-1] -= k

    new_max = max(a[0],a[n-1])
    new_min = min(a[0],a[n-1])

    for j in range(1,n-1):
        #if current is less than newmin add k else if more than new max subtract k
        if a[j] < new_min:
            a[j] += k
        elif a[j] > new_max:
            a[j] -= k
        #if a[j] is in between newmax and min then if a[j] is closer to new_max, then subtract k else add k
        elif a[j] - new_min > new_max - a[j]:
            a[j] -= k
        else:
            a[j] += k
        
        new_max = max(a[j], new_max)
        new_min = min(a[j], new_min)
    
    return new_max-new_min

a = [1, 10, 14, 14, 14, 15]
n = len(a)
k = 6
print getmindiff(a,n,k)

        

        