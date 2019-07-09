class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = Node(50)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(30)


def increment(root,diff):
    if root.left:
        root.left.data += diff 
        increment(root.left,diff)#recursively call to fix the descendants
    elif root.right:
        root.right.data += diff 
        increment(root.right,diff)

def convert_children_sum(root):
    left_data = 0 
    right_data = 0
    diff = 0

    if root is None or root.left is None and root.right is None:
        return 
    else:
        convert_children_sum(root.left)
        convert_children_sum(root.right)
    
    if root.left:
        left_data = root.left.data 
    if root.right:
        right_data = root.right.data     
    
    diff = left_data + right_data - root.data    
    if diff > 0:
        root.data += diff 
    if diff < 0:
        increment(root,-diff)

def inorder(root):
    if root:
        inorder(root.left)
        print root.data, 
        inorder(root.right)

convert_children_sum(root)
inorder(root)