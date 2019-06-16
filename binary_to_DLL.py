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
root.left.left.left = Node(6)

headref = [None] 
def binary_to_dll(root,headref):
    if root is None: return 
    binary_to_dll(root.right,headref)
    root.right = headref[0]
    if headref[0] is not None:
        headref[0].left = root
    headref[0] = root 
    binary_to_dll(root.left,headref)

def printdll(headref):
    temp = headref[0]
    while temp:
        print temp.data, 
        temp = temp.right 

binary_to_dll(root,headref)
printdll(headref)