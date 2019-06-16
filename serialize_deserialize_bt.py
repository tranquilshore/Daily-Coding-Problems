#serialize and deserialize
#serialization is to store tree in a file so that it can later be restored
#deserialization is reading a tree from a file

#just do a preorder traversal and put -1 for None pointers

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


preorder_recursive(root)
print
serialize(root)
print serialize_list
res = deserialize(serialize_list)
preorder_recursive(res)
