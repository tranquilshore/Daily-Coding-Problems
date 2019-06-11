#using doubly linked list, head of ddl will always store the first non repeated character of the stream
class Node:
    def __init__(self,value):
        self.data = value 
        self.next = None 
        self.prev = None 

class DDL:
    head = tail = None 
    def append(self,value):
        tmp = Node(value)
        if self.head is None:
            self.head = self.tail = tmp 
            return 
        self.tail.next = tmp
        tmp.prev = self.tail 
        self.tail = tmp

    def print_DDL(self):
        tmp = self.head 
        while tmp is not None:
            print tmp.data,
            tmp = tmp.next 
    
    def delete(self,address):
        if self.head is None or address is None:
            return 
        if self.head == address:
            self.head = address.next 
        if address.next is not None:
            address.next.prev = address.prev 
        if address.prev is not None:
            address.prev.next = address.next

    def first_non_repeating_in_stream(self,stream):
        address_store = [None]*256
        repeated = [False]*256

        for i in stream:
            #if already repeated don't go inside
            if repeated[ord(i)] == False:
                #if seen for the first time add it to address store and ddl
                if address_store[ord(i)] == None:
                    self.append(i)
                    address_store[ord(i)] = self.tail 
                else:#if already in address store remove it from ddl and address store and mark it as repeated
                    self.delete(address_store[ord(i)])
                    address_store[ord(i)] = None 
                    repeated[ord(i)] = True 
            if self.head is not None:
                print self.head.data 

# ddl = DDL()
# ddl.append(4)
# ddl.append(5)
# ddl.append(9)

# ddl.print_DDL()

# ddl.delete(ddl.head.next)

# ddl.print_DDL()

ddl = DDL()
ddl.first_non_repeating_in_stream("abacdbf")


