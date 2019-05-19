'''
To find the cousins for a given node.
Two nodes are cousins if they are at same level but have different parents.
'''
class node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)

root.left.left.left = node(8)
root.left.left.right = node(9)

root.left.right.left = node(10)
root.left.right.right = node(11)

root.right.left = node(6)
root.right.right = node(7)

root.right.right.left = node(12)
root.right.right.right = node(13)

def cousins(root,val):
    if root is None: return 
    q = []
    q.append(root)
    while q:
        nodes_count = len(q)
        cousins = []
        found = False 
        while nodes_count>0:
            cur_node = q.pop(0)
            in_left = False
            if cur_node.left:
                q.append(cur_node.left)
                cousins.append(cur_node.left.data)
                if cur_node.left.data == val:
                    in_left = True
                    found = True 
                    cousins.pop()

            if cur_node.right:
                q.append(cur_node.right)
                cousins.append(cur_node.right.data)
                if in_left:
                    cousins.pop()
                if cur_node.right.data == val:
                    cousins.pop()
                    found = True
                    if cur_node.left:
                        cousins.pop()
        
            nodes_count -= 1 
        if found:
            print cousins

cousins(root,9)


