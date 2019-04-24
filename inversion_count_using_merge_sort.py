'''
Inversion Count:
Two elements a[i] and a[j] forms an inversion if a[i] > a[j] and i < j. 
Inversion count of an array indicates, how far the array is from being sorted. if array is already sorted inversion count = 0, if array sorted
in reverse order the inversion count is maximum.

We can efficiently find it using merge sort in O(nlogn) which is better than simple O(n^2)
watch this to understand merge sort https://www.youtube.com/watch?v=TzeBrDU-JaY&t=788s
watch this to find inversion in merge sort https://www.youtube.com/watch?v=k9RQh21KrH8 
'''
inv_count = [0]
#time complexity of this method is O(n^2)
def naive_inversion_count(a):
    n = len(a)
    inv_count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] > a [j]:
                inv_count += 1
    return inv_count
#time complexity of this method is O(nlogn)
def inversion_count(a, temp, left, right):
    if right > left:
        mid = (right + left)/2
        #Inversion count will be sum of inversions in left-part, right-part and number of inversions in merging
        inversion_count(a, temp, left, mid)
        inversion_count(a, temp, mid+1, right)
        #merging two parts
        merge(a, temp,left, mid+1, right)

def merge(a, temp, left, mid, right):
    
    i = left #left subarray
    j = mid #right subarray
    k = left #resultant merged subarray
    
    while i <= mid -1 and j <= right:
        if a[i] <= a[j]:
            temp[k] = a[i]
            k += 1
            i += 1
        else:
            temp[k] = a[j]
            k += 1
            j += 1
            
            inv_count[0] += mid - 1
            
    while i <= mid-1:
        temp[k] = a[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = a [j]
        k += 1
        j += 1
    
    for i in range(left,right+1):
        a[i] = temp[i]
        

a = [1, 20, 6, 4, 5]
t = [None]*(len(a))

inversion_count(a, t, 0, len(a) - 1)
print a 
print inv_count[0]
