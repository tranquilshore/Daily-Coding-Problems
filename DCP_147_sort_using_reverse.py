import sys 
lst = [-12,8,17,7,9,11]

def min_index(lst,start,end):
    min_element = sys.maxint
    min_element_index = 0
    for i in range(start,end+1):
        if lst[i] < min_element:
            min_element = lst[i]
            min_element_index = i 
    return min_element_index 

def reverse(lst,start,end):
    while start < end:
        lst[start],lst[end] = lst[end],lst[start]
        start += 1
        end -= 1

def sort(lst):
    for i in range(len(lst)):
        min_ind = min_index(lst,i,len(lst)-1)
        reverse(lst,i,min_ind)

sort(lst)
print lst 



