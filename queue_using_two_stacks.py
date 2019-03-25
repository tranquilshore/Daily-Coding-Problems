'''
need to implement queue with following methods:
isEmpty()
size()
enqueue()
dequeue()
front()

using stacks methods:
isEmpty()
size()
push()
pop()
peek()
'''

class queue:
    def __init__(self):
        self.s1 = list()
        self.s2 = list()

    def isEmpty(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            return True 
        else:
            return False 
    
    def size(self):
        return len(self.s1) + len(self.s2)

    def enqueue(self,e):
        self.s1.append(e)

    def dequeue(self):
        if len(self.s2) == 0:
            while len(self.s1)!=0:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def front(self):
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())
        return self.s2[len(self.s1)-1]

q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print q.dequeue()
print q.front()

