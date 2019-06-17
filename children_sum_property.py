class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None

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