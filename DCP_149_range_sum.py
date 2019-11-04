a = [5,2,1,3,4,6,7,9,8,3]

#number of nodes on segment tree will be 2*n-1, but to index left and right subtree with 2*n and 2*n+1,
#start making segment tree from first index hence take segment tree(represented as array) size as 2*n

#node structure of a segment tree
class Node:
    def __init__(self,value,start_ind,end_ind,left,right):
        self.value = value 
        self.start_ind = start_ind
        self.end_ind = end_ind
        self.left = left 
        self.right = right 
    
    def interval(self):
        return (self.start_ind, self.end_ind)

#segment tree construction - it takes O(n) time for construction
def make_segment_tree(lst,start_ind,end_ind):
    if start_ind == end_ind:
        val = lst[0]
        return Node(val,start_ind,end_ind,None,None)
    mid = len(lst)/2 
    left = make_segment_tree(lst[:mid],start_ind,start_ind+mid-1)
    right = make_segment_tree(lst[mid:],start_ind+mid,end_ind)
    root_val = left.value + right.value
    return Node(root_val,start_ind,end_ind,left,right)

#it takes O(logn) time for querrying the sum of a given range
def get_sum(root_seg,start,end):
    #if node range is inside the querry range then just return the nodes value
    if start <= root_seg.start_ind and end >= root_seg.end_ind:
        return root_seg.value 
    #if node range and querry range are disjoint then return 0
    if end < root_seg.start_ind or start > root_seg.end_ind:
        return 0 
    #else in any case of intersections go to both children recursively
    return get_sum(root_seg.left,start,end) + get_sum(root_seg.right,start,end)

root_seg = make_segment_tree(a,0,len(a)-1)
print get_sum(root_seg,2,8)





     