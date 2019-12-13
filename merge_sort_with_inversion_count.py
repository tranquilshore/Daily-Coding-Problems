'''

                                                          [2,4,1,6,8,5,3,7]

                                                    /                          \

                                        [2,4,1,6]m                           [8,5,3,7]
                                            L                                    R
                                     /             \                    /                  \
                                
                               [2,4]m              [1,6]            [8,5]m                [3,7]
                                 L                  R                  L                    R
                            /       \            /      \           /      \           /          \

                          [2]m       [4]         [1]m     [6]      [8]m     [5]     [3]m          [7]
                           L          R           L        R         L       R       L             R
m: middle index at every recursion step

whenever at merging step if L[i]>R[i] we need to add m-i+1 to answer to find the overall inversion count in O(nlogn) time.


                                                            6+2+1=9(ans)
                                                          [1,2,3,4,5,6,7,8]

                                                    /                          \
                                         0+2 = 2                              1+2+1=4
                                        [1,2,4,6]m                           [3,5,7,8]
                                            L                                    R
                                     /             \                    /                  \
                                 0                   0                1                     0
                               [2,4]m              [1,6]            [5,8]m                [3,7]
                                 L                  R                  L                    R
                            /       \            /      \           /      \           /          \

                          [2]m       [4]         [1]m     [6]      [8]m     [5]     [3]m          [7]
                           L          R           L        R         L       R       L             R

'''


a = [2,8,9,4,5,6]
a = [2,4,1,3,5]
a = [5,3,7,2,8]
a = [2,4,1,6,8,5,3,7]
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