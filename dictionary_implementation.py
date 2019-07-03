'''
Dictionary/Hashmap is all about mapping keys to a fixed size keyspace using uniform hash functions.
Actual implementation has dynamic hash size, which is O(1) amortized.
Below is a basic implementaion of Dictionary in Python.
'''
class dictionary:
    dictionary_size = 10
    table = [None]*dictionary_size
    
    def hash(self,key):
        return key%10
    
    def insert(self,key,value):
        hashed_key = self.hash(key)
        if self.table[hashed_key] == None:
            self.table[hashed_key] = value 
        else:#this this is to handle collisions
            if type(self.table[hashed_key]) == list:
                self.table[hashed_key].append(value)
            else:
                self.table[hashed_key] = [self.table[hashed_key], value]
    
    def lookup(self,key):
        hashed_key = self.hash(key)
        if self.table[hashed_key] == None:
            return "Key Not Found!"
        else:
            return self.table[hashed_key]
    
    def delete(self,key):
        hashed_key = self.hash(key)
        if self.table[hashed_key] != None:
            self.table[hashed_key] = None 
            print "Successfully deleted"
        else:
            print "Key Not Found!"

d = dictionary()
d.insert(23,"sahil")
d.insert(5,"dobby")
d.insert(6,"tranquil")
d.insert(13,"honey")
print d.lookup(23)
print d.lookup(6)
print d.lookup(99)
d.delete(5)
print d.lookup(5)


        
