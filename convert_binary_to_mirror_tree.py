'''
The idea is to do queue based level order traversal. While doing traversal, swap left and right children of every node.
'''

class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def mirror_tree(root):
    if root is None:
        return 
    q = []
    q.append(root)
    while q:
        current = q.pop(0)
        current.left,current.right = current.right,current.left 
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)

def inorder(root):
    if root:
        inorder(root.left)
        print root.data, 
        inorder(root.right)

inorder(root)
print 
mirror_tree(root)
inorder(root)

