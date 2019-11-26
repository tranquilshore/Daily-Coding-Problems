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

    #1. code to get all suffixes or autocomplete a prefix
    def auto_complete(self,prefix):
        node = self.root 
        for char in prefix:
            if char not in node.children:
                return set()
            node = node.children[char]
        
        return list(self.all_suffixes(node,prefix))

    def all_suffixes(self,node,prefix):
        result = set()
        if node.finished:
            result.add(prefix)
        if not node.children:
            return result 
        return reduce(lambda a,b:a|b,[self.all_suffixes(node,prefix+char) for char,node in node.children.items()])|result # union of result set with what we get from recursive function

    #2. search if a word exist or not 
    def search(self,word):
        node = self.root 
        for char in word:
            if char not in node.children:
                return False 
            node = node.children[char]
        return node.finished 

    #3. longest common prefix 
    def longest_commmon_prefix(self):
        node = self.root 
        if len(node.children)>1 or len(node.children) == 0:
            return "No Common Prefix!"
        common_prefix = ""
        while len(node.children) == 1:
            for char in node.children:
                common_prefix += char 
                node = node.children[char]
        return common_prefix

    #4. shortest unique prefix 
    def shortest_unique_prefix(self,word):
        node = self.root 
        prefix = ""
        for char in word:
            node = node.children[char]
            prefix += char 
            if node.count == 1:
                return prefix 
        return prefix

    

trie = Trie()
words = ['geeksforgeeks','geeks','geek','geezer']
for w in words:
    trie.insert(w)

#Q1
print trie.auto_complete("geek")
#Q2
print trie.search("geezero")
#Q3
print trie.longest_commmon_prefix()
#Q4
for w in words:
    print trie.shortest_unique_prefix(w)
