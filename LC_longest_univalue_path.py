'''
              1
             / \
            4   5
           / \   \
          4   4   5
answer will be 2 as 4-4-4 has two edges. The solution works same as maximum sum path in a binary tree problem, where we return only either left or right paths from a subtree and for answer 
consider the both left and right path.
'''
class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None 

root = Node(1)
root.left = Node(4)
root.left.left = Node(4)
root.left.left.left = Node(4)

root.left.right = Node(5) 
root.right = Node(5)
root.right.right = Node(5)

ans = [0]
def longest_univalue_path(root,ans):
    if root is None:
        return 0 
    left_len = longest_univalue_path(root.left,ans)
    right_len = longest_univalue_path(root.right,ans)
    left_arw = right_arw = 0 

    if root.left and root.left.val == root.val:
        left_arw = left_len + 1 
    if root.right and root.right.val == root.val:
        right_arw = right_len + 1 

    ans[0] = max(ans[0],left_arw+right_arw)
    return max(left_arw,right_arw)

longest_univalue_path(root,ans)
print ans[0]
