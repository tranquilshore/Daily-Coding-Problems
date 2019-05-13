'''
level order traversal of a binary tree
'''

class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(6)
root.right.left = Node(4)
root.right.right = Node(5)

def level_order_traversal(root):
    if root is None: return 
    q = []
    q.append(root)
    while q:
        nodecount = len(q)
        while nodecount>0:
            curr = q.pop(0)
            print curr.data,
            
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            nodecount -= 1
        print 

level_order_traversal(root)