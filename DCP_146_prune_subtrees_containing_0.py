class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 
    
root = Node(0)
root.left = Node(0)
root.right = Node(1)
root.left.left = Node(1)
root.left.right = Node(0)
root.left.left.left = Node(0)
root.left.left.right = Node(0)

def prune(root):
    if root is None:
        return root 
    root.left = prune(root.left)
    root.right = prune(root.right)
    if root.left is None and root.right is None and root.data == 0:
        return None 
    return root 

def print_tree(root):
    if root:
        print_tree(root.left)
        print root.data,
        print_tree(root.right)

res = prune(root)
print_tree(res)