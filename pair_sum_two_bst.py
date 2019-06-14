class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root1 = Node(5)
root1.left = Node(3)
root1.right = Node(9)
root1.right.left = Node(6)
root1.right.right = Node(11)

root2 = Node(7)
root2.left = Node(2)
root2.right = Node(10)

target = 20

def pair_sum(root1,root2):
    if root1 is None or root2 is None:
        return 
    s1 = []
    s2 = []
    current1 = root1 
    current2 = root2 
    done1 = 1 
    done2 = 1 

    len_t1 = 5
    len_t2 = 3

    t1 = 0
    t2 = 0

    while True:
        while done1:
            if current1 is not None:
                s1.append(current1)
                current1 = current1.left 
            else:
                if len(s1)>0:
                    current1 = s1.pop()
                    val1 = current1.data 
                    t1 += 1
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
                    t2 += 1
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
        if t1 == len_t1 or t2 == len_t2:
            return "Not existed"

print pair_sum(root1,root2)

