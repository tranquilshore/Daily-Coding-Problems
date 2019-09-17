#this will use as much space as there are non zero elements
class CompactArray:
    def __init__(self,arr,n):#take sparse array and length of sparse array as constructor arguments
        self._dict = {}
        self.n = n 
        for i,e in enumerate(arr):
            if e != 0:
                self._dict[i] = e 
        
    def check_bounds(self,i):#check bounds of the sparse array
        if i<0 or i>=self.n:
            raise IndexError("Out of bounds!")
    
    def set(self,i,val):
        self.check_bounds(i)#first check if its a valid index
        if val != 0: #store only if value is different from 0
            self._dict[i] = val 
            return 
        elif i in self._dict:#if trying to store 0 remove that index from the compact array
            del self._dict[i]
    
    def get(self,i):
        self.check_bounds(i)
        return self._dict.get(i,0) #returns value if key i exists else returns 0
    

