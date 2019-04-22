m = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
]

r = len(m)
c = len(m[0])

def spiral(m,r,c):
    k = l = 0
    
    while k<r and l<c:
        #print first row from remaining rows
        for i in range(l,c):
            print m[k][i],
        k += 1

        #print last column from remaining columns
        for i in range(k,r):
            print m[i][c-1],
        c -= 1

        if k < r:
            for i in range(c-1,l-1,-1):
                print m[r-1][i],
            r -= 1

        if l < c:
            for i in range(r-1,k-1,-1):
                print m[i][l],
            l += 1

spiral(m,r,c)





