'''
To do it in linear time, every node will return 4 types of information for which we create a user defined data type:
1. min value of left subtree. 
2. max value of right subtree.
3. root is bst or not.
4. size of bst
'''
import sys 

class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = Node(7)
root.left = Node(5)
root.right = Node(16)
root.left.left = Node(2)
root.left.right = Node(9)
root.right.left = Node(17)
root.right.right = Node(19)

class minmax:
    def __init__(self,mini=sys.maxint, maxi=-sys.maxint, isbst=True, size=0):
        self.mini = mini 
        self.maxi = maxi 
        self.isbst = isbst
        self.size = size 

def largest_bst(root):
    if root is None:
        return minmax()
    #do a postorder traversal
    leftminmax = largest_bst(root.left)
    rightminmax = largest_bst(root.right)

    m = minmax()
    if not leftminmax.isbst or not rightminmax.isbst or leftminmax.maxi>root.data or rightminmax.mini<root.data:
        m.isbst = False
        m.size = max(leftminmax.size, rightminmax.size)
        return m 
    
    #if reached here means the subtree with this node as root is bst 
    m.isbst = True 
    m.size = leftminmax.size + rightminmax.size + 1
    m.mini = leftminmax.mini if root.left is not None else root.data #easily understood
    m.maxi = rightminmax.maxi if root.right is not None else root.data 
    return m 

ans = largest_bst(root)
print ans.size 