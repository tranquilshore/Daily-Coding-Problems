'''
input:
dog
cat
apple
apricot
fish

output:
d
c
app
apr
f

solution:
make a trie store the frequency of character in the node as well, print the word till the frequency count of character is 1.
'''

class Node:
    def __init__(self,char=None):
        self.char = char 
        self.children = {}
        self.finished = False 
        self.count = 0 

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self,word):
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
            node.count += 1 
        node.finished = True 
    
    def unique_prefix(self,word):
        node = self.root 
        prefix = ''
        for char in word:
            node = node.children[char]
            prefix += char 
            if node.count == 1:
                return prefix 
        return prefix 

def shortest_unique_prefix(lst):
    trie = Trie()
    for word in lst:
        trie.insert(word)
    
    return [trie.unique_prefix(word) for word in lst]

lst = ['dog','cat','apple','apricot','fish']
lst = ['zebra','dog','duck','dove']
print shortest_unique_prefix(lst)
