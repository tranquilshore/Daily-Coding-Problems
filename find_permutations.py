a = ['1','2','3']

def permutations(a,l,r):
    if l == r:
        print a
    else:
        for i in range(l,r+1):
            a[l],a[i] = a[i],a[l]
            permutations(a,l+1,r)
            a[l],a[i] = a[i],a[l] #backtracking step

permutations(a,0,len(a)-1)