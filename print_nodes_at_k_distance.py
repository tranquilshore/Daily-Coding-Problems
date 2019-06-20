'''
logic is to add path in the array and print all nodes from that at k distance, k will decrement and while printing nodes at k just don't print the next node in the array
'''

class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 
    
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.left.right.right.left = Node(16)

target = root.left.right 

path = []
def print_path_till_node(root,target,path):
    if root is None: return False 
    path.append(root)
    if root == target:
        return True 
    #check whether required node lies in left or right subtree
    if print_path_till_node(root.left,target,path) or print_path_till_node(root.right,target,path):
        return True 
    #reaches here then it doesn't lies in either of these so remove it from the path and return False 
    path.pop()
    return False 


# print_path_till_node(root,target,path)
# print path

def print_nodes_at_k_distance_from_root(root,exclude,k):
    if root is None: return 
    if k == 0:
        print root.data, 
        return 
    if root.left != exclude:
        print_nodes_at_k_distance_from_root(root.left,exclude,k-1)
    if root.right != exclude:
        print_nodes_at_k_distance_from_root(root.right,exclude,k-1)

#print_nodes_at_k_distance(root,root.left.right,2)

def print_nodes_at_k_distance(root,target,k):
    print_path_till_node(root,target,path)
    n = len(path)
    path.append(None)

    for i in range(n-1,-1,-1):
        if k >= 0:
            print_nodes_at_k_distance_from_root(path[i],path[i+1],k)
            k -= 1

print_nodes_at_k_distance(root,target,2)



    