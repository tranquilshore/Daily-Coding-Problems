class Node:
    def __init__(self,value):
        self.data = value 
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

def reverse(head):
    if head is None: return
    current = head 
    prev = nxt = None 
    while current:
        nxt = current.next 
        current.next = prev 
        prev = current
        current = nxt 
        head = prev
    return head 

node = reverse(head)

while node:
    print node.data, 
    node = node.next 
