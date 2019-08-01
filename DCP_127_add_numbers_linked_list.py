class Node:
    def __init__(self,value):
        self.data = value 
        self.next = None 

#this is 9
num1 = Node(9)
#num1.next = Node(9) 

#this is 25
num2 = Node(5)
num2.next = Node(2)

carry = [0]
temp = [None]
prev = [None]
head = [None] 

def add(num1,num2,carry,prev,head):
    while num1 or num2:
        data1 = num1.data if num1 is not None else 0 
        data2 = num2.data if num2 is not None else 0 
        sum_ = data1+data2+carry[0] 
        carry[0] = 0 if sum_ < 10 else 1
        sum_ = sum_ if sum_ < 10 else sum_%10  

        temp[0] = Node(sum_) 

        if head[0] is None:
            head[0] = temp[0]
        else:
            prev[0].next = temp[0] 
        
        prev[0] = temp[0] 
        
        if num1:
            num1 = num1.next 
        if num2:
            num2 = num2.next 
    
    if carry[0]>0: 
        temp[0].next = Node(carry[0])

add(num1,num2,carry,prev,head)

def printll(head):
    current = head[0] 
    while current:
        print current.data, 
        current = current.next 

printll(head)







