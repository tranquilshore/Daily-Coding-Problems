'''
pair sum in same tree
done using iterative inorder traversal simultaneously from both the ends of bst.
space taken will be O(logn) if it will be a self balancing bst.
'''

class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = Node(5)
root.left = Node(3)
root.right = Node(9)
root.right.left = Node(6)
root.right.right = Node(11)

target = 16

def pair_sum(root):
    if root is None: return 
    s1 = []
    s2 = []
    done1 = 1
    done2 = 1
    current1 = root
    current2 = root  

    while True:
        while done1:
            if current1 is not None:
                s1.append(current1)
                current1 = current1.left 
            else:
                if len(s1)>0:
                    current1 = s1.pop()
                    val1 = current1.data
                    current1 = current1.right
                    done1 = 0
                else:
                    done1 = 0

        while done2:
            if current2 is not None:
                s2.append(current2)
                current2 = current2.right 
            else:
                if len(s2)>0:
                    current2 = s2.pop()
                    val2 = current2.data 
                    current2 = current2.left 
                    done2 = 0
                else:
                    done2 = 0 

        if val1 + val2 == target:
            print val1,val2
            return True 
        elif val1 + val2 < target:
            done1 = True 
        elif val1 + val2 > target:
            done2 = True 
        #we didn't find any such pairs
        if val1 >= val2:
            return False 


inorder_iterative(root)

