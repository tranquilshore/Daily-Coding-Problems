'''
LRU - Least Recently Used cache is a cache eviction policy which is useful when most recently accessed content is likely to be the most desired in the future.
So that we get less cache misses. As cache operations needs to be fast, we need O(1) time approach for it.

So, what we need to achieve in it is:
1. Fast lookup (using Dictionary/HashMap - O(1))
2. Fast Removals (using Doubly Linked List - O(1))

Will implement in two API:
1. Set(key,val) : will put the value to the front of the DLL and if the capacity is reached, will remove the last element of DLL
2. Get(key) : if present will put the element in front of the DLL else return -1.

'''

#doubly linked list node structure with key value pair
class Node:
    def __init__(self,k,v):
        self.key = k 
        self.value = v 
        self.next = None 
        self.prev = None 

class LRU_cache:
    #initialize the cache instance with its capacity
    def __init__(self,capacity):
        self.capacity = capacity
        self.dic = dict() #initializing the dictionary for fast lookups
        
        #initailizing dummy head and tail nodes and their pointers for DLL
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail 
        self.tail.prev = self.head 
    
    #to add any node in front of DLL(here it will always add from the tail side)
    def _add(self,node):
        p = self.tail.prev 
        p.next = node 
        self.tail.prev = node 
        node.next = self.tail 
        node.prev = p 
    
    #to remove a node from DLL for the cases when capacity is reached or when we need to put the accessed element in front, so we'll remove first and then add it to the front
    def _remove(self,node):
        p = node.prev  
        n = node.next 
        p.next = n 
        n.prev = p 

    #function which will return the asked content and add it to the front of DLL if it exists else return -1
    def get(self,key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n) #it will first remove the accessed element then
            self._add(n) # add it to the front of DLL to maintain the recent access order
            return n.value
        return -1 

    def set(self,key,value):
        n = Node(key,value)
        self._add(n) #adding node in front of DLL as it is recently accessed
        self.dic[key] = n #add that node to dictionary as well with key as key and value as pointer to node for fast lookups
        if len(self.dic) > self.capacity:
            #we are removing from the head side here 
            n = self.head.next 
            self._remove(n) #removing from DLL
            del self.dic[n.key] #removing from dictionary as well

cache = LRU_cache(3)

cache.set(1,1)
cache.set(2,2)
cache.set(3,3)
cache.set(5,5)
print cache.get(1) #will return -1
print cache.get(2)


    

