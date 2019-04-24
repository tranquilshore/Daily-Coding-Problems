'''
Construct a BT given inorder and postorder or inorder and preorder.
'''
In = [4,8,2,5,1,6,3,7]
post = [8,4,5,2,6,7,3,1]

class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 



def _search(a,start,end,data):
    for i in range(start,end+1):
        if a[i] == data:
            return i

def build_tree(In, post, instart, inend, pindex):
    if instart > inend:
        return None 
    
    root = Node(post[pindex[0]])
    pindex[0] -= 1 #we have to add 1 if preorder is given

    if instart == inend:
        return root
    
    iindex = _search(In,instart,inend,root.data)

    root.right = build_tree(In,post,iindex+1,inend,pindex)
    root.left = build_tree(In,post,instart,iindex-1,pindex)
    return root 

def inorder_print(root):
    if root is not None:
        inorder_print(root.left)
        print root.data,
        inorder_print(root.right)


instart = 0
inend = len(In)-1
pindex = [len(In)-1] #for preorder pindex will be first element of preorder array ie. 0

root = build_tree(In,post,instart,inend,pindex)
inorder_print(root)
