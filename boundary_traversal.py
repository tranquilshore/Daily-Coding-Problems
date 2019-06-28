class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.left.right = Node(6)

def print_leaves(root):
    if root:
        print_leaves(root.left)
        if root.left is None and root.right is None:
            print root.data,
        print_leaves(root.right)
    
def print_left(root):
    if root:
        if root.left:
            print root.data,
            print_left(root.left)
        elif root.right:
            print root.data,
            print_left(root.right)

def print_right(root):
    if root:
        if root.right:
            print_right(root.right)
            print root.data,
        elif root.left:
            print_right(root.left)
            print root.data, 

def boundary_traversal(root):
    if root:
        print root.data, 
        print_left(root.left)

        print_leaves(root.left)
        print_leaves(root.right)

        print_right(root.right)

boundary_traversal(root)