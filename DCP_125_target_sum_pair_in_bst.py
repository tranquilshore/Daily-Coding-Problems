class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(11)
root.right.right = Node(15)

target = 29

def pair_with_sum(root):
    if root is None:
        return 
    s1 = []
    current1 = root 
    done1 = False 
    
    s2 = []
    current2 = root
    done2 = False 

    while True:
        while not done1:
            if current1:
                s1.append(current1)
                current1 = current1.left 
            else:
                if len(s1)>0:
                    current1 = s1.pop()
                    left = current1.data   
                    current1 = current1.right 
                    done1 = True 
                else:
                    done1 = True
        
        while not done2:
            if current2:
                s2.append(current2)
                current2 = current2.right
            else:
                if len(s2)>0:
                    current2 = s2.pop()
                    right = current2.data   
                    current2 = current2.left  
                    done2 = True 
                else:
                    done2 = True

        if left + right == target:
            return left,right   
        elif left+right < target:
            done1 = False 
        else:
            done2 = False 

        if left > right:
            return False 
    

print pair_with_sum(root)
