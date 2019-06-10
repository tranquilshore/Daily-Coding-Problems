#https://algorithmsandme.com/find-kth-smallest-element-in-two-sorted-arrays/
import math
import sys 

a = [1,3,11]
b = [1,5,7,8,9]
k = 5

def find_kth_smallest(a,b,k):
    lena = len(a)
    lenb = len(b)

    if lena+lenb < k:
        return -1

    imin = 0
    imax = min(lena,k-1) #given in the link above,

    i = 0
    j = 0
    while imin <= imax:
        i = int(math.ceil((imin+imax)/2.0)) 
        j = k-i-1

        maxleftx = a[i-1] if i-1>=0 else -sys.maxint
        minrightx = a[i] if i<lena else sys.maxint
        maxlefty = b[j-1] if j-1>=0 else -sys.maxint
        minlefty = b[j] if j<lenb else sys.maxint 

        if maxlefty > minrightx:
            imin = i + 1 #i is too small, increase it
        elif i>0  and maxleftx>minlefty:
            imax = i-1#i is too big must decrease it 
        else:
            return min(minrightx,minlefty)
    return -1

print find_kth_smallest(a,b,k)

#mean for different size arrays
def median(a,b):
    if len(b)<len(a):
        return median(b,a)
    x = len(a)
    y = len(b)

    low = 0
    high = x

    while low <= high:
        partitionx = (low+high)/2
        partitiony = (x+y+1)/2 - partitionx 


        maxleftx = -sys.maxint if partitionx == 0 else a[partitionx-1]
        minrightx = sys.maxint if partitionx == x else a[partitionx]
        maxlefty = -sys.maxint if partitiony == 0 else b[partitiony-1]
        minrighty = sys.maxint if partitiony == y else b[partitiony]

        if maxleftx <= minrighty and maxlefty <= minrightx:
            if (x+y)%2 == 0:
                return (max(maxleftx,maxlefty) + min(minrightx,minrighty))/2.0
            else:
                return max(maxleftx,maxlefty)
        elif maxleftx > minrighty:
            high = partitionx - 1
        else:
            low = partitionx + 1
        
    return -1



print median(a,b)
        



