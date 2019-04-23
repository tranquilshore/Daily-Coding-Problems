'''
As inorder traversal of BST produces ascending ordered elements. During the traversal just keep the count during every node visit if it becomes
equal to k return the node's data. For kth Largest first traverse the right subtree and then left subtree.
'''

class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = Node(7)
root.left = Node(4)
root.right = Node(11)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.left = Node(9)
root.right.right = Node(15)

ans = [-1]
count = [0]
def kth_smallest(root,k,ans,count):
    if root is not None:
        kth_smallest(root.left,k,ans,count)
        count[0] += 1
        if count[0] == k:
            ans[0] = root.data 
        kth_smallest(root.right,k,ans,count)
    return ans[0] 

print kth_smallest(root,5,ans,count)

ans = [-1]
count = [0]
def kth_largest(root,k,ans,count):
    if root is not None:
        kth_largest(root.right,k,ans,count)
        count[0] += 1
        if count[0] == k:
            ans[0] = root.data 
        kth_largest(root.left,k,ans,count)
    return ans[0]

print kth_largest(root,2,ans,count)
