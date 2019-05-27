'''
print diameter(longest left to leaf path) path.
'''

class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = Node(1); 
root.left = Node(2); 
root.right = Node(3); 
root.left.left = Node(4); 
root.left.right = Node(5); 
root.left.right.left = Node(6); 
root.left.right.right = Node(7); 
root.left.left.right = Node(8); 
root.left.left.right.left = Node(9);
 
#           1 
#         /   \      
#        2     3 
#      /   \    
#     4     5 
#      \   / \  
#       8 6   7 
#      / 
#     9 


#code to print the all root to leaf paths of a binary tree
# def print_route(root,stack):
#     if root is None:
#         return 
#     stack.append(root.data)
#     if root.left is None and root.right is None:
#         print '->'.join([str(i) for i in stack])
    
#     print_route(root.left,stack)
#     print_route(root.right,stack)
#     stack.pop()


def print_route_updated(root,stack,space,length):
    if root is None:
        return 
    stack.append(root.data)
    if root.left is None and root.right is None:
        if len(stack) > length[0]:
            space[0] = ' -> '.join([str(i) for i in stack])
            length[0] = len(stack)
        
    print_route_updated(root.left,stack,space,length)
    print_route_updated(root.right,stack,space,length)
    stack.pop()

ans = [0]
k = [None]
def diameter(root,ans):
    if root is None: return 0
    lh = diameter(root.left,ans)
    rh = diameter(root.right,ans)
    if 1+lh+rh>ans[0]:
        ans[0] = 1+lh+rh
        k[0] = root  
    return 1+max(lh,rh)

diameter(root,ans)
#print ans[0],k[0].data

#print_route_updated(k[0],stack)
space = [""]
stack = []
length = [0]
print_route_updated(k[0].left,stack,space,length)
print space[0],
print "->",k[0].data,"->",
space = [""]
stack = []
length = [0]
print_route_updated(k[0].right,stack,space,length)
print space[0] 
#print k[0].data  
#print_route_updated(k[0].right,stack)
