'''
Need to implement get_max method using the stack in constant time.
idea: keep track of max element whenever you push into stack using another stack. 
'''
class stackWithMax:
    def __init__(self):
        self.main_stack = []
        self.track_stack = []

    def push(self,x):
        self.main_stack.append(x)

        if len(self.main_stack) == 1:
            self.track_stack.append(x)
            return 
        
        if x > self.track_stack[-1]:
            self.track_stack.append(x)
        else:
            self.track_stack.append(self.track_stack[-1])

    def pop(self):
        self.main_stack.pop()
        self.track_stack.pop()

    def get_max(self):
        return self.track_stack[-1]

s = stackWithMax()
s.push(10)
s.push(5)
s.push(7)
print s.get_max()