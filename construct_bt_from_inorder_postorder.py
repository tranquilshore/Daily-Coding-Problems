In = [4,8,2,5,1,6,3,7]
Post = [8,4,5,2,6,7,3,1]

instart = 0 
inend = len(In)-1

pindex = [0]
pindex[0] = len(Post)-1 #which is equal to inend

class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

def build_tree(In, Post, instart, inend, pindex):
    if instart > inend: return None
    
    root = Node(Post[pindex[0]])
    pindex[0] -= 1

    if instart == inend: return root 
    index = In.index(root.data)

    #first recurse from right and then left, as we are use post order to always find root
    root.right = build_tree(In,Post,index+1,inend,pindex)
    root.left = build_tree(In,Post,instart,index-1,pindex)
    return root 

def inorder(root):
    if root:
        inorder(root.left)
        print root.data, 
        inorder(root.right)

res = build_tree(In,Post,instart,inend,pindex)
inorder(res)