class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = Node(10)
root.left = Node(-2)
root.right = Node(6)
root.left.left = Node(8)
root.left.right = Node(-4)
root.right.left = Node(7)
root.right.right = Node(5)

def convert_to_sum_tree(root):
    if root is None: return 0 
    oldval = root.data 
    root.data = convert_to_sum_tree(root.left) + convert_to_sum_tree(root.right)
    return root.data + oldval 

def inorder(root):
    if root:
        inorder(root.left)
        print root.data, 
        inorder(root.right)

convert_to_sum_tree(root) 
inorder(root)