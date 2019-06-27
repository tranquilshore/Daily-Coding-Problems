class Trie:
    def __init__(self):
        self.children = {}
        self.flag = False

    def add(self,char):
        self.children[char] = Trie()

    def insert(self,word):
        node = self
        for char in word:
            if char not in node.children:
                node.add(char)
            node = node.children[char] #if char is present get to next level of trie
        node.flag = True
    
    def contains(self,word): #searching functionality
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.flag
    
    def all_suffixes(self,prefix):
        results = set()
        if self.flag:
            results.add(prefix)
        if not self.children:
            return results
        return reduce(lambda a,b:a|b,[node.all_suffixes(prefix+char) for (char,node) in self.children.items()])|results
    
    def auto_complete(self,prefix):
        node = self
        for char in prefix:
            if char not in node.children:
                return set()
            node = node.children[char]
        return list(node.all_suffixes(prefix))

    def common_prefix(self):
        node = self
        if len(node.children) > 1 or len(node.children) == 0:
            return "No Common Prefix"
        cmn_prefix = list()
        while len(node.children) == 1:
            for char in node.children:
                cmn_prefix.append(char)
                node = node.children[char]
        return cmn_prefix
        
        

trie = Trie()
words = ["geeksforgeeks", "geeks", "geek", "geezer"]
for word in words:
    trie.insert(word)
print trie.auto_complete("geek")
print trie.common_prefix()
    

    
