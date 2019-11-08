#iterative solution for swap pairs in linked list 

class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)

def swap(head):
    curr = head 
    if curr is None or curr.next is None:
        return curr 
    prev = head 
    curr = head.next 
    head = curr 
    while curr:
        nxt = curr.next 
        curr.next = prev
        if nxt is None:
            prev.next = nxt 
            curr = nxt 
        elif nxt.next is None:
            prev.next = nxt 
            curr = nxt.next 
        else:
            prev.next = nxt.next 
            curr = nxt.next 
            prev = nxt 
    return head 

def recursive(head):
    if head is None or head.next is None:
        return head 
    remaining = head.next.next 
    newhead = head.next 
    head.next.next = head 
    head.next = recursive(remaining)
    return newhead

def print_ll(head):
    curr = head 
    while curr:
        print curr.value,
        curr = curr.next 

#res = swap(head)
res = recursive(head)
print_ll(res)

