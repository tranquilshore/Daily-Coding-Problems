'''
idea is to do inorder traversal, while doing inorder pass level of current node also, keep track of maximum level seen so far and value of deepest
node seen so far.
O(n)
'''

class newNode:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = newNode(1)  
root.left = newNode(2)  
root.right = newNode(3)  
root.left.left = newNode(4)  
root.right.left = newNode(5)  
root.right.right = newNode(6)  
root.right.left.right = newNode(7)  
root.right.right.right = newNode(8)  
root.right.left.right.left = newNode(9)


res = [-1]
maxlevel = [-1]

def deepest_node(root,level,res,maxlevel):
    if root is not None:
        level += 1
        deepest_node(root.left,level,res,maxlevel)
        if level > maxlevel[0]:
            res[0] = root.data 
            maxlevel[0] = level 
        deepest_node(root.right,level,res,maxlevel)

deepest_node(root,0,res,maxlevel)
print res[0]