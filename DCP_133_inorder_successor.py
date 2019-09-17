class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

given_node =root.left.right.right
given_node = root.left.right

#keep traversing left child to find the minimum element in bst
def min_node_bst(root):
    current = root 
    while current.left:
        current = current.left
    return current.data 

#using search like technique to find the next greater element
def inorder_successor(root,given_node):
    if given_node.right:
        return min_node_bst(given_node.right)
    while root:
        if given_node.data < root.data:
            succ = root
            root = root.left 
        elif given_node.data > root.data:
            root = root.right 
        else:
            break 
    return succ.data   

print inorder_successor(root,given_node)
    
