import sys 

a = [6,2,1,9,3,11,9,4]

'''
making a segment tree takes O(n) and quering for minimum value in a range will take O(logn)
'''

class Node:
    def __init__(self,value,start_ind,end_ind,left,right):
        self.value = value 
        self.start_ind = start_ind
        self.end_ind = end_ind 
        self.left = left 
        self.right = right 

def make_segment_tree(lst,start_ind,end_ind):
    if start_ind == end_ind:
        val = lst[0]
        return Node(val,start_ind,end_ind,None,None)
    mid = len(lst)/2 
    left = make_segment_tree(lst[:mid],start_ind,start_ind+mid-1)
    right = make_segment_tree(lst[mid:],start_ind+mid,end_ind)
    root_val = min(left.value,right.value)
    return Node(root_val,start_ind,end_ind,left,right)

def get_min(root_seg,start,end):
    if start <= root_seg.start_ind and end >= root_seg.end_ind:
        return root_seg.value 
    if end < root_seg.start_ind or start > root_seg.end_ind:
        return sys.maxint 
    return min(get_min(root_seg.left,start,end), get_min(root_seg.right,start,end))

root_seg = make_segment_tree(a,0,len(a)-1)
print get_min(root_seg,3,7)