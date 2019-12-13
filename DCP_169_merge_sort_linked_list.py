class Node:
    def __init__(self,val):
        self.val = val 
        self.next = None 

head = Node(3)
head.next = Node(6)
head.next.next = Node(2)
head.next.next.next = Node(1)
head.next.next.next.next = Node(9)

def merge_sort(head):
    if head is None or head.next is None:
        return head 
    
    #get heads of two halfs to apply merge sort 
    middle = get_middle(head)
    head2 = middle.next 

    middle.next = None 

    left = merge_sort(head)
    right = merge_sort(head2)

    return merge(left,right)

def get_middle(head):
    if head is None:
        return None 
    slow = head 
    fast = head 
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next 
        fast = fast.next.next 
    return slow 

def merge(a,b):
    if a is None:
        return b 
    if b is None:
        return a 
    if a.val <= b.val:
        result = a 
        result.next = merge(a.next,b)
    else:
        result = b 
        result.next = merge(a,b.next)
    return result 

def print_ll(head):
    curr = head 
    while curr is not None:
        print curr.val,
        curr = curr.next 

ans = merge_sort(head)
print_ll(ans)

