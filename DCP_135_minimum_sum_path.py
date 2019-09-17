import sys
import copy 
class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = Node(10)
root.left = Node(5)
root.right = Node(5)
root.left.right = Node(2)
root.right.right = Node(1)
root.right.right.left = Node(-1)

def minimum_sum_path_root_to_leaf(root,min_val):
    if root is None: return 
    s.append(root.data)
    if root.left is None and root.right is None:
        if sum(s) < min_val[0]:
            min_val[0] = sum(s)
            global ans 
            ans = copy.copy(s)

    minimum_sum_path_root_to_leaf(root.left,min_val)
    minimum_sum_path_root_to_leaf(root.right,min_val)
    s.pop()

ans = []
s = []
min_val = [sys.maxint]

minimum_sum_path_root_to_leaf(root,min_val)
print ans,min_val
