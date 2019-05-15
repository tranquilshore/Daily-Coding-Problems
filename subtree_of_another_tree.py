'''
eg. 1
Tree1
          x 
        /    \
      a       b
       \
        c


Tree2
              z
            /   \
          x      e
        /    \     \
      a       b      k
       \
        c

tree 1 is a subtree of tree2

eg.2
Tree1
          x 
        /    \
      a       b
     /        
    c         


Tree2
          x 
        /    \
      a       b
     /         \
    c            d

tree 1 is not a subtree of tree2 
For the second example we also need to store some info if we encounter None nodes, which will help to solve such cases.

'''

class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root1 = Node('x')
root1.left = Node('a')
root1.right = Node('b')
root1.left.left = Node('c')


root2 = Node('x')
root2.left = Node('a')
root2.right = Node('b')
root2.left.left = Node('c')
root2.right.right = Node('d')

#primitive
def preorder_traversal(root):
    stack = []
    stack.append(root)
    res = ''
    while stack:
        node = stack.pop()
        #print node.data,
        res += node.data
            
        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)  

    return res 

#another way to do preorder
def pre_order_traversal(root):
    stack = []
    res = ''
    node = root
    while stack or node:
        while node:
            stack.append(node)
            res += node.data 
            node = node.left 
            if not node:
                res += "$"
        node = stack.pop()
        node = node.right 
        if not node:
            res += "$"
    return res 



print pre_order_traversal(root1) #xac$$$b$$
print pre_order_traversal(root2) #xac$$$b$d$$

'''
now if root1's preorder traversal is a subtring of root2 preorder traversal then it is the subtree of the other tree else it is not.
To do substring search we can do that using KMP or rabin karp in 0(n) time.
So, overall time complexity will remain linear.
'''

#print pre_order_traversal(root2)

