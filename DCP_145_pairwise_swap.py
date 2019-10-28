class Node:
    def __init__(self,value):
        self.data = value 
        self.next = None 

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

def pairwise_swap(head):
    if head is None or head.next is None:
        return head 
    prev = head 
    curr = head.next 
    head = curr
    while True:
        nxt = curr.next 
        curr.next = prev 
        if nxt is None or nxt.next is None:
            prev.next = nxt 
            return head 
        prev.next = nxt.next 
        prev = nxt 
        curr = prev.next 

def print_ll(head):
    curr = head 
    while curr:
        print curr.data, 
        curr = curr.next

res = pairwise_swap(head)
print_ll(res)
