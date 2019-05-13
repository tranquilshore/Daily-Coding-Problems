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
root.left.right = Node(6)

#preorder iterative traversal using a stack 
#don't use the recursive version as it uses recursion stack, which could lead to stack overflow solution
def print_all_path(root):
    current = root 
    s = []
    s.append(current)
    s.append(str(current.data))
    s.append(current.data)

    while s:
        pathsum = s.pop()
        path = s.pop()
        current = s.pop()

        if not current.left and not current.right:
            print "path: "+path, "pathsum: "+str(pathsum) 
        
        if current.right:
            rightstr = path + "->" + str(current.right.data)
            rightpathsum = pathsum + current.right.data 
            s.append(current.right)
            s.append(rightstr)
            s.append(rightpathsum)
        
        if current.left:
            leftstr = path + "->" + str(current.left.data)
            leftpathsum = pathsum + current.left.data 
            s.append(current.left)
            s.append(leftstr)
            s.append(leftpathsum)

print_all_path(root)




# def all_paths(root):
#     if root is None: return 
#     paths = []
#     q = []
#     q.append(root)
#     while q:
#         node = q.pop()
#         if not node.left and not node.right:
#             paths += []