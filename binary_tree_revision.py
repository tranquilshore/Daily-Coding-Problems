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

def preorder_iterative(root):
    if root is None: return 
    s = []
    s.append(root)
    while s:
        current = s.pop()
        print current.data, 
        if current.right:
            s.append(current.right)
        if current.left:
            s.append(current.left)

#preorder_iterative(root)

def root_to_leaf_path(root):
    if root is None: return 
    s = []
    s.append(root) #for preorder
    s.append(str(root.data)) #for path 
    s.append(root.data)#for path sum 
    
    while s:
        pathsum = s.pop()
        path = s.pop()
        current = s.pop()

        if not current.left and not current.right:
            print path," -> ",pathsum
        
        if current.right:
            rightstr = path+"-"+str(current.right.data)
            rightpathsum = pathsum+current.right.data 
            s.append(current.right)
            s.append(rightstr)
            s.append(rightpathsum)
        
        if current.left:
            leftstr = path+"-"+str(current.left.data)
            leftpathsum = pathsum+current.left.data 
            s.append(current.left)
            s.append(leftstr)
            s.append(leftpathsum)

s = []
def root_to_leaf_path_recursive(root):
    if root is None: return 
    s.append(root.data)
    if not root.left and not root.right:
        print s 
    root_to_leaf_path_recursive(root.left)
    root_to_leaf_path_recursive(root.right)
    s.pop()

def nodes_distance_k_from_root(root,k):
    if root is None: return
    if k < 0: return 
    if k == 0: print root.data 
    nodes_distance_k_from_root(root.left,k-1)
    nodes_distance_k_from_root(root.right,k-1)

#root_to_leaf_path(root)
#root_to_leaf_path_recursive(root)
#nodes_distance_k_from_root(root,2)

#visit a node doing preorder traversal and see if root's data lies within the required range or not
import sys 
mini = -sys.maxint 
maxi = sys.maxint 

bst_root = Node(11)
bst_root.left = Node(3)
bst_root.right = Node(9)
bst_root.left.left = Node(1)
bst_root.left.right = Node(4)
bst_root.left.left.left = Node(0)

def bst_or_not(root,mini,maxi):
    if root is None: return True 
    if root.data < mini or root.data > maxi:# invalid condition for bst 
        return False 
    return bst_or_not(root.left,mini,root.data-1) and bst_or_not(root.right,root.data+1,maxi)

#print bst_or_not(bst_root,mini,maxi)

#height of a tree
def height(root):
    if root is None: return 0 
    lh = height(root.left)
    rh = height(root.right)
    return 1+max(lh,rh)

#print height(bst_root)

#diameter of binary tree: longest path between two leaf nodes of a binary tree
#which is nothing but maximum value of (leftheight+rightheight+1) at each node of a binary tree
#same height logic can be applied here 

ans = [0]
def diameter(root,ans):
    if root is None: return 0 
    lh = diameter(root.left,ans)
    rh = diameter(root.right,ans)
    ans[0] = max(ans[0],1+lh+rh)
    return 1+max(lh,rh)

#diameter(root,ans)
#print ans[0]

#height balanced or not: difference between the heights of left subtree and righ subtree is not more than 1 
def height_balanced_or_not(root):
    if root is None: return True 
    lh = height_balanced_or_not(root.left)
    if lh == -1: return -1 
    rh = height_balanced_or_not(root.right)
    if rh == -1: return -1 
    if abs(lh-rh) > 1: return -1 
    return 1+max(lh,rh)

#print height_balanced_or_not(root) # will return -1 if not height balanced else height of the tree

#count leaf nodes: can be done using preorder traversal 
def count_leaves(root):
    if root is None: return 0 
    if root.left is None and root.right is None:
        return 1 
    return count_leaves(root.left)+count_leaves(root.right)

#print count_leaves(root)

#if two trees identical or not: done doing preorder traversal 
def identical_or_not(root1,root2):
    if root1 is None and root2 is None:
        return True 
    if root1 is not None and root2 is not None:
        return root1.data == root2.data and identical_or_not(root1.left,root2.left) and identical_or_not(root1.right,root2.right)
    return False 

#print identical_or_not(root,bst_root)

#if tree is symmetric or not/ mirrot image of itself or not 
#recursive is same as identical just need to pass root1.left,root2.right in recursion step as for mirrot left becomes right and right becomes left
#iterative solution is - every level of tree should be pallindromic 

sym_root = Node(1)
sym_root.left = Node(2)
sym_root.right = Node(2)

sym_root.left.left = Node(3)
sym_root.left.right = Node(4)

sym_root.right.left =Node(4)
#sym_root.right.right = Node(3)


def symmetric(root1,root2):
    if root1 is None and root2 is None:
        return True 
    if root1 is not None and root2 is not None:
        return root1.data == root2.data and symmetric(root1.left,root2.right) and symmetric(root1.right,root2.left)
    return False 

#print symmetric(sym_root,sym_root)

def inorder_iterative(root):
    if root is None: return 
    s = []
    current = root 
    done = 1
    while done:
        if current is not None:
            s.append(current)
            current = current.left 
        else:
            if len(s)>0:
                current = s.pop()
                print current.data, 
                current = current.right 
            else:
                done = 0

#inorder_iterative(root)

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

# binary_to_dll(root,headref)
# printdll(headref)

#serialize and deserialize
#serialization is to store tree in a file so that it can later be restored
#deserialization is reading a tree from a file

#just do a preorder traversal and put -1 for None pointers

def preorder_recursive(root):
    if root is not None:
        print root.data,
        preorder_recursive(root.left)
        preorder_recursive(root.right)

serialize_list = []
def serialize(root):
    if root is None:
        serialize_list.append(-1)
        return 
    serialize_list.append(root.data)
    serialize(root.left)
    serialize(root.right)


def deserialize(serialize_list):
    if len(serialize_list) == 0:
        return None 
    tmp = serialize_list.pop(0) 
    if tmp == -1:
        return None 
    else:
        d_root = Node(tmp)
    d_root.left = deserialize(serialize_list) 
    d_root.right = deserialize(serialize_list)
    return d_root


# preorder_recursive(root)
# print
# serialize(root)
# print serialize_list
# res = deserialize(serialize_list)
# preorder_recursive(res)


#lowest common ancestor

#important points to remember: prereqisite that both nodes should be present in the tree
#1. if any of the two values matches root then return root as LCA else recurse in subtrees
#2. if both left and right subtree return something then that root is lca
#3. if only one of them return something then that will be the lca 

def lca(root,n1,n2):
    if root is None: return 
    if root.data == n1 or root.data == n2:#1
        return root.data 
    leftlca = lca(root.left,n1,n2)
    rightlca = lca(root.right,n1,n2)
    if leftlca and rightlca:#2
        return root.data
    return leftlca if leftlca is not None else rightlca#3

#print lca(root,6,5)

#maximum path sum in binary tree
#lets see how can we add a subtree to a part of maximum path

#1.just take a root from it 
#2.take either root and left or root and right part of that subtree
#3.just the whole subtree then that subtree is the answer as it can not be part of the other subtree(path can't trace back)

#important point to remember is return root and left or root and right part of subtree at the end to find other max path

res = [0]
def max_path_sum(root,res):
    if root is None: return 0 
    l = max_path_sum(root.left,res)
    r = max_path_sum(root.right,res)
    maxlr = max(l,r)
    maxsingle = max(maxlr+root.data,root.data)
    maxall = max(maxsingle,l+r+root.data)
    res[0] = max(res[0],maxall)
    return maxsingle

#max_path_sum(root,res)
#print res[0]

#lowest common ancestor in bst
def lca_bst(root,n1,n2):
    if root is None:
        return 
    if root.data > n1 and root.data > n2:#If both n1 and n2 are smaller than root, then LCA is in left
        lca_bst(root.left,n1,n2)
    if root.data < n1 and root.data < n2:#If both n1 and n2 are greater than root, then LCA is in right
        lca_bst(root.right,n1,n2)
    return root #else the first root which lies between n1 and n2 is the answer

#connect nodes at same level
def connect_node(p):
    if p is None: return 
    p.nextRight = None 
    while p is not None:
        q = p 
        while q is not None:
            if q.left:
                if q.right:
                    q.left.nextRight = q.right 
                else:
                    q.left.nextRight = getNextRight(q)
            if q.right:
                q.right.nextRight = getNextRight(q)
            q = q.nextRight
        if p.left:
            p = p.left 
        elif p.right:
            p = p.right 
        else:
            p = getNextRight(p)

def getNextRight(p):
    temp = p.nextRight
    while temp:
        if temp.left:
            return temp.left 
        if temp.right:
            return temp.right 
        temp = temp.nextRight
    return None 

#level of a node
def level_of_node(root,key,level):
    if root is None:
        return -1 
    if root.data == key:
        return level 
    l = level_of_node(root.left,key,level+1)
    if l != -1:
        return l 
    return level_of_node(root.right,key,level+1)

#print level_of_node(root,6,0)

#distance between two nodes of binary tree
def distance_btw_nodes(root,n1,n2):
    if root is not None:
        lca = lca(root,n1,n2)
        d1 = level_of_node(lca,n1,0)
        d2 = level_of_node(lca,n2,0)
        return d1+d2 

#largest bst in a binary tree

#in postorder traversal manner
#from every node return 4 types of information for which we create user defined data type
#1. minimum value at left subtree
#2. maximum value of right subtree
#3. root is bst or not
#4. size of bst 
import sys 
class minimax:
    def __init__(self,mini=sys.maxint,maxi=-sys.maxint,isbst=True,size=0):
        self.mini = mini 
        self.maxi = maxi 
        self.isbst = isbst 
        self.size = size 

def largest_bst(root):
    if root is None:
        return minimax()
    leftminimax = largest_bst(root.left)
    rightminimax = largest_bst(root.right)
    m = minimax()

    if not leftminimax.isbst or not rightminimax.isbst or leftminimax.maxi>root.data or rightminimax.mini <root.data:
        m.isbst = False 
        m.size = max(leftminimax.size, rightminimax.size)
        return m 
    #reaches here means root is bst
    m.isbst = True 
    m.size = leftminimax.size + rightminimax.size + 1
    m.mini = leftminimax.mini if root.left is not None else root.data 
    m.maxi = rightminimax.maxi if root.right is not None else root.data
    return m 

#print largest_bst(bst_root).size 

#level order traversal 
def level_order_traversal(root):
    if root is None: return 
    q = []
    q.append(root)
    while True:
        nodecount = len(q)
        if nodecount == 0: break 
        while nodecount > 0:
            current = q.pop(0)
            print current.data,
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            nodecount -= 1
        print 

#level_order_traversal(root)

#spiral order traversal 
def spiral_order_traversal(root):
    if root is None: return 
    q1 = []
    q2 = []

    q1.append(root)
    while q1 or q2:
        while q1:
            current = q1.pop(0)
            print current.data,
            if current.right:
                q2.append(current.right)
            if current.left:
                q2.append(current.left)
        while q2:
            current = q2.pop(0)
            print current.data,
            if current.left:
                q1.append(current.left)
            if current.right:
                q1.append(current.right)

#spiral_order_traversal(root)

#vertical order/ top view and bottom view 
def vertical_order(root):
    if root is None: return 
    q = []
    m = {}
    q.append((root,0))
    while q:
        n = q[0][0]
        val = q[0][1]
        q.pop(0)

        #for vertical traversal
        if m.has_key(val):
            m[val].append(n.data)
        else:
            m[val] = n.data
        
        # #for top view 
        # if m.has_key(val) == False:
        #     m[val] = n.data 
        #     print n.data

        # m[val] = n.data #for bottom view  

        if n.left:
            q.append((n.left,val-1))
        if n.right:
            q.append((n.right,val+1))

child_sum_node = Node(10)
child_sum_node.left = Node(8)
child_sum_node.right = Node(2)
child_sum_node.left.left = Node(3)
child_sum_node.left.right = Node(5)
child_sum_node.right.right = Node(2)

def children_sum_property(root):
    left_data = 0 
    right_data = 0 

    if root == None or (root.left == None and root.right == None):
        return 1 
    else:
        if root.left:
            left_data = root.left.data 
        if root.right:
            right_data = root.right.data
        if root.data == left_data+right_data and children_sum_property(root.left) and children_sum_property(root.right):
            return 1 
        else:
            return 0 
if children_sum_property(child_sum_node):
    print "holds the property"
else:
    print "doesn't"
 
        
        

