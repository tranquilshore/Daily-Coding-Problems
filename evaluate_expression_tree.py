'''
Evaluation of expression tree.
'''
class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

def evaluate_expression_tree(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None :
        return int(root.data)
    
    left_sum = evaluate_expression_tree(root.left)
    right_sum = evaluate_expression_tree(root.right)

    if root.data == "+":
        return left_sum+right_sum
    if root.data == "-":
        return left_sum-right_sum
    if root.data == "*":
        return left_sum*right_sum
    if root.data == "/":
        return left_sum/right_sum

root = Node('+') 
root.left = Node('*') 
root.left.left = Node('5') 
root.left.right = Node('4') 
root.right = Node('-') 
root.right.left = Node('100') 
root.right.right = Node('20') 
print evaluate_expression_tree(root)