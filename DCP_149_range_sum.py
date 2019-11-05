a = [5,2,1,3,4,6,7,9,8,3]
a = [1,3,-2,8,-7]

'''
Segment tree is useful if there are more update queries and small sum range queries as both will take O(logn)
if sum range querry is more and update queries is less then we can simply use array type preprocessing(where we store sum from 0 to element's index) which can tell the sum range in O(1) but update in that case will be O(n)
'''

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

def update_seg_tree(root_seg,indx,diff):
    #if update querry range lies outside the node range then just return and don't do further in tree
    if indx < root_seg.start_ind or indx > root_seg.end_ind:
        return 
    #if it is within node range then update the node and go to both children recursively 
    root_seg.value += diff 
    #unless its a leaf node keep recursing
    if root_seg.left is not None and root_seg.right is not None:
        update_seg_tree(root_seg.left,indx,diff)
        update_seg_tree(root_seg.right,indx,diff)


#The function to update a value in input array and segment tree
def update(arr,indx,new_val,root_seg):
    n = len(arr)
    if indx < 0 or indx > n-1:
        print "Invalid Input!"
        return 
    #difference between the old value and new value 
    diff = new_val - a[indx]
    #update the value in array 
    a[indx] = new_val
    #update segment tree 
    update_seg_tree(root_seg,indx,diff)

def print_seg_tree(root_seg):
    if root_seg:
        print_seg_tree(root_seg.left)
        print root_seg.value,
        print_seg_tree(root_seg.right)

root_seg = make_segment_tree(a,0,len(a)-1)
print_seg_tree(root_seg)
print get_sum(root_seg,1,3)
update(a,3,11,root_seg)
print get_sum(root_seg,1,3)







     