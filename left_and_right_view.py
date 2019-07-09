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
root.right.right.left = Node(6)

#whenever in preorder traversal manner, if level of a node changes for the first time, it will be a candidate for the left view
maxlevel = [0]
def leftview(root,level,maxlevel):
    if root is None:
        return 
    if maxlevel[0] < level:
        print root.data, 
        maxlevel[0] = level 
    leftview(root.left,level+1,maxlevel)
    leftview(root.right,level+1,maxlevel)

leftview(root,1,maxlevel)
print
#use the above logic to print righ view, just by first traversing right subtree and then left subtree
maxlevel = [0]
def rightview(root,level,maxlevel):
    if root is None:
        return 
    if maxlevel[0] < level:
        print root.data, 
        maxlevel[0] = level 
    rightview(root.right,level+1,maxlevel)
    rightview(root.left,level+1,maxlevel)

rightview(root,1,maxlevel)