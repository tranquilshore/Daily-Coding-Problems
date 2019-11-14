class Node:
    def __init__(self,value):
        self.val = value 
        self.next = None 

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

def recursive(head):
    if head is None or head.next is not None:
        return head 
    tmp = recursive(head.next)
    head.next.next = head 
    head.next = None 
    return tmp 

def print_ll(head):
    curr = head 
    while curr.next:
        print curr.val,
        curr = curr.next

res = recursive(head)
print_ll(res)
