class stacks:
    def __init__(self):
        self.size = 10 
        self.list = [None]*self.size 
        self.s0 = 0 #grows up
        self.s1 = len(self.list)/2 #grows up
        self.s2 = len(self.list)-1 #grows down 

    def push(self,data,stack):
        if stack == 0:
            self.list[self.s0] = data 
            self.s0 += 1
        elif stack == 1:
            self.list[self.s1] = data   
            self.s1 += 1
        else:
            self.list[self.s2] = data   
            self.s2 -= 1

        if self.is_resize_needed():
            self.resize(self.size*2)

    def is_resize_needed(self):
        return self.s0 == len(self.list)/2 or self.s1 > self.s2 
    
    def resize(self,size):
        prev_list = self.list 
        prev_s0 = self.s0 
        prev_s1 = self.s1 
        prev_s2 = self.s2 

        self.size = size 
        self.list = [None]*self.size  
        self.s0 = 0 #grows up
        self.s1 = len(self.list)/2 #grows up
        self.s2 = len(self.list)-1 #grows down

        for i in range(prev_s0):
            self.push(prev_list[i],0)

        for i in range(len(prev_list)/2,prev_s1):
            self.push(prev_list[i],1)

        for i in reversed(range(prev_s2+1, len(prev_list))):
            self.push(prev_list[i],2)
        
    def pop(self,stack):
        if stack == 0:
            self.s0 -= 1
            return self.list[self.s0]
        elif stack == 1:
            self.s1 -= 1
            return self.list[self.s1]
        else:
            self.s2 -= 1
            return self.list[self.s2]



        



     
