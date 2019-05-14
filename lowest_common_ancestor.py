'''
watch https://www.youtube.com/watch?v=13m9ZCB8gjw
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
root.left.right.left = Node(6)

n1 = 2
n2 = 6

def lca(root,n1,n2):
    if root is None: return None 
    if root.data == n1 or root.data == n2:
        return root 
    leftlca = lca(root.left,n1,n2)
    rightlca = lca(root.right,n1,n2)
    if leftlca and rightlca:
        return root 
    return leftlca if not rightlca else rightlca

ans = lca(root,n1,n2)
print ans.data 