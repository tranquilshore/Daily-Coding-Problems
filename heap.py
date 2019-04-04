'''
watch https://www.youtube.com/watch?v=2fA1FdxNqiE how heapify works

important points to remember:
leaf nodes start from n/2+1 index till n if array starts from index 1
maximum no. of nodes at height h is n/(2^(h+1))
'''
class heap:
    def __init__(self):
        self.array = []
    
    def append(self,x):
        self.array.append(x)
        return

    def print_heap(self):
        if len(self.array) == 0:
            print "No element to print"
        else:
            for i in range(len(self.array)):
                print self.array[i],

    #O(logn) operation
    def max_heapify(self,i):
        #l and r values has to be changed according to the array starting from 0
        l = 2*i+1 
        r = 2*i+2
        n = len(self.array)

        if l < n and self.array[l] > self.array[i]:
            largest = l
        else:
            largest = i 
        
        if r < n and self.array[r] > self.array[largest]:
            largest = r 
        
        if largest != i :
            self.array[i],self.array[largest] = self.array[largest],self.array[i]
            self.max_heapify(largest)

    #O(n) operation
    def build_max_heap(self):
        n = len(self.array)
        for i in range(n/2-1,-1,-1): #did n/2 -1 because in video array starts from 1, actually it starts from 0, so non leaf node will start from n/2-1
            self.max_heapify(i)

    #O(logn) operation
    def extract_max(self):
        n = len(self.array)
        if n < 1:
            return "heap underflow"
        max_ = self.array[0]
        self.array[0] = self.array[n-1]
        self.array.pop()
        self.max_heapify(0)
        return max_

    #O(nlogn) operation
    def heap_sort(self):
        self.build_max_heap()
        for i in range(len(self.array)):
            print self.extract_max(),

h = heap()
h.append(1)
h.append(2)
h.append(5)
h.append(9)
#h.build_max_heap()
#h.print_heap()

h.heap_sort()
