'''
invert a binary tree

     4
   /   \
  2     7     
 / \   / \
1   3 6   9

to 


     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = Node(4)
root.left = Node(2)
root.right = Node(7)

root.left.left = Node(1)
root.left.right = Node(3)

root.right.left = Node(6)
root.right.right = Node(9)

#using dfs
def invert(root):
    if root is None:
        return None 
    temp = invert(root.right)
    root.right = invert(root.left)
    root.left = temp 
    return root

#using bfs or level order traversal
def invert_iterative(root):
    if root is None:
        return None 
    q = [root]
    while q:
        curr = q.pop(0)
        curr.left,curr.right = curr.right,curr.left
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    return root 

def print_inorder(root):
    if root is not None:
        print_inorder(root.left)
        print root.data,
        print_inorder(root.right)

temp = invert_iterative(root)
print_inorder(temp)