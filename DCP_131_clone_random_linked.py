class Node:
    def __init__(self,value):
        self.data = value 
        self.next = None 
        self.random = None 

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

head.random = head.next.next 
head.next.random = head 
head.next.next.random = head.next 

def clone(head):
    #for keeping clone nodes in between actual nodes and assign next pointers
    current = head 
    while current:
        temp = current.next 
        current.next = Node(current.data)
        current.next.next = temp 
        current = temp 
    
    #for assigning random pointers to the clone nodes
    current = head 
    while current:
        current.next.random = current.random.next 
        if current.next:
            current = current.next.next 
        else:
            current = current.next 
    
    #segregating original and clone lists 
    original = head 
    clone = head.next 

    temp = clone 
    while original and clone:
        original.next = original.next.next if original.next else original.next 
        clone.next = clone.next.next if clone.next else clone.next 
        original = original.next 
        clone = clone.next 
    
    return temp

output = clone(head)

print output.random.data 
        
    
    