a = [2,8,9,4,5,6]
a = [2,4,1,3,5]
a = [5,3,7,2,8]
l = 0
h = len(a)-1 

inv_count = [0]

def merge(a,l,m,h):
    n1 = m-l+1 
    n2 = h-m

    L = [a[l+i] for i in range(n1)]
    R = [a[m+1+j] for j in range(n2)]

    i = j = 0
    k = l 

    while i < n1 and j<n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
            inv_count[0] += m-i+1 #inversion count step do just mid - i(index where L[i]>R[j])
        k += 1
    while i<n1:
        a[k] = L[i]
        i += 1
        k += 1
    while j<n2:
        a[k] = R[j]
        j += 1
        k += 1

def merge_sort(a,l,h):
    if l<h:
        m = l + (h-l)/2
        merge_sort(a,l,m)
        merge_sort(a,m+1,h)
        merge(a,l,m,h)
 
merge_sort(a,l,h)
print a 
print inv_count[0]