class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = Node(24)
root.left = Node(5)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(3)
root.right.left = Node(3)
root.right.right = Node(4)

def is_sum_tree(root):
    if root is None or (root.left is None and root.right is None):
        return True 
    if is_sum_tree(root.left) and is_sum_tree(root.right):
        if root.left is None:
            ls = 0
        elif root.left.left is None and root.left.right is None:
            ls = root.left.data  
        else:
            ls = 2*root.left.data  
        
        if root.right is None:
            rs = 0 
        elif root.right.left is None and root.right.right is None:
            rs = root.right.data  
        else:
            rs = 2*root.right.data 
        
        return root.data == ls+rs 
    return False 

print is_sum_tree(root)