import sys 

maxval = sys.maxint 
minval = -sys.maxint-1

class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = Node(10)
root.left = Node(0)
root.right = Node(25)
root.left.left = Node(-1)
root.left.right = Node(21)
root.right.left = Node(16)
root.right.right = Node(32)

def is_bst(root,minval,maxval):
    if root is None:
        return True 
    if root.data < minval or root.data > maxval:
        return False 
    return is_bst(root.left,minval,root.data-1) and is_bst(root.right,root.data+1,maxval)

print is_bst(root,minval,maxval)