class Node:
    def __init__(self,value):
        self.data = value 
        self.next = None 
    
head = Node(8)
head.next = Node(2)
head.next.next = Node(7)
head.next.next.next = Node(11)
head.next.next.next.next = Node(5)

def printll(head):
    tmp = head 
    while tmp:
        print tmp.data,
        tmp = tmp.next 

def middle(head):
    if head is None: return None 
    if head.next is None or head.next.next is None:
        return head 
    slow = fast = head 
    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next 
    return slow 

#print middle(head).data

#reverse a linked list - iterative solution
def reverse(head):
    current = head 
    prev = nxt = None 
    while current:
        nxt = current.next
        current.next = prev 
        prev = current
        current = nxt 
    return prev 

#printll(reverse(head))

#reverse a linked list - recursive solution
result = [None]
def reverse_recursive(current,prev):
    if current.next is None:
        result[0] = current
        current.next = prev 
        return
    nxt = current.next 
    current.next = prev 
    reverse_recursive(nxt,current)

# reverse_recursive(head,None)
# printll(result[0])


#reverse in groups: read notes to understand it 
def reverse_in_groups(head,k):
    current = head 
    nxt = prev = None 
    count = 0 
    while count < k and current:
        nxt = current.next 
        current.next = prev 
        prev = current
        current = nxt 
        count += 1 
    if nxt:
        head.next = reverse_in_groups(nxt,k)
    return prev 

#printll(reverse_in_groups(head,2))

#rotate linked list till k nodes 
def rotate(head,k):
    if k == 0 or head is None: return
    current = head 
    count = 1 
    while count<k and current:
        current = current.next 
        count += 1 
    if current is None: return #when k is greater than the nodes present 
    
    kthnode = current 
    while current.next:
        current = current.next 
    
    current.next = head 
    head = kthnode.next 
    kthnode.next = None 
    return head 

#printll(rotate(head,3))


'''
1 - 2 - 3 - 4 - 5
            |   |
            7 - 6
'''

loophead = Node(1)
loophead.next = Node(2)
loophead.next.next = Node(3)
loophead.next.next.next = Node(4)
loophead.next.next.next.next = Node(5)
loophead.next.next.next.next.next = Node(6)
loophead.next.next.next.next.next.next = Node(7)
loophead.next.next.next.next.next.next.next = loophead.next.next.next

#works for these edge cases as well
edge_loop = Node(7)
edge_loop.next = Node(8)
edge_loop.next.next = edge_loop

def detect_and_remove(loophead):
    slow = loophead
    fast = loophead.next  
    while fast and fast.next:
        if slow == fast:
            #print "look exists"
            break  
        slow = slow.next 
        fast = fast.next.next
    
    if slow == fast:
        slow = loophead
        while slow != fast.next:
            slow = slow.next 
            fast = fast.next 
        fast.next = None 
    return loophead

#printll(detect_and_remove(edge_loop))

#nth node from end of linked list 
def nthnode(head,n):
    slow = fast = head 
    count = 0 
    while fast and count < n:
        fast = fast.next 
        count += 1 
    while fast:
        slow = slow.next 
        fast = fast.next 
    return slow.data     

#print nthnode(head,4)

'''
merge sort in linked list:
merge sort is prefered for sorting in linked lists because of slow random access performance of linked list for algorithms
like quick sort makes them perform poorly, but not in merge sort.
'''

#finding middle code
def middle1(head):
    if head is None: return None 
    if head.next is None or head.next.next is None:
        return head 
    slow = fast = head 
    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next 
    return slow 

#merging sorted linked list code
def sortedmerge(a,b):
    result = None
    if a is None: return b 
    if b is None: return a 
    if a.data <= b.data:
        result = a 
        result.next = sortedmerge(a.next,b)
    else:
        result = b 
        result.next = sortedmerge(a,b.next)
    return result

def mergesort_linkedlist(head):
    if head is None or head.next is None:
        return head 
    
    middle_ = middle1(head)
    nextofmiddle = middle_.next 

    middle_.next = None 
    left = mergesort_linkedlist(head)
    right = mergesort_linkedlist(nextofmiddle)

    return sortedmerge(left,right)

#printll(mergesort_linkedlist(head))

#flatten a linked list 
class flattennode:
    def __init__(self,value):
        self.data = value 
        self.right = None 
        self.down = None 

headf = flattennode(2)
headf.right = flattennode(1)
headf.down = flattennode(4)
headf.down.down = flattennode(6)
headf.right.down = flattennode(11)
headf.right.down.down = flattennode(19)

def flatten(head):
    if head is None or head.right is None:
        return head 
    return flatmerge(head,flatten(head.right))

def flatmerge(a,b):
    result = None 
    if a is None: return b 
    if b is None: return a 
    if a.data <= b.data:
        result = a 
        result.down = flatmerge(a.down,b)
    if a.data > b.data:
        result = b 
        result.down = flatmerge(a,b.down)
    return result 
    
def printflatten(node):
    tmp = node 
    while tmp:
        print tmp.data, 
        tmp = tmp.down

printflatten(flatten(headf))





