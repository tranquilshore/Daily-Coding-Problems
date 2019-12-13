'''
Problem Description:
https://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/ 

Idea: Use BFS, start from the given start word, traverse all words that adjacent(differ by one character) to it and keep doing so until we find the target word
or we have traversed all the words.
'''

start = "dog"
target = "cat"
d = ["dot","dop","dat","cat"]

class Qitem:
    def __init__(self,word,leng):
        self.word = word 
        self.leng = leng 

def is_adjacent(a,b):
    n = len(a)
    count = 0
    for i in range(n):
        if a[i]!=b[i]:
            count += 1
        if count > 1:
            break 
    return True if count == 1 else False

def shortest_chain(start,target,d):
    q = []
    item = Qitem(start,1)
    q.append(item)

    while len(q) > 0:
        curr = q.pop(0)
        
        for w in d:#going through all words of dictionary
            if is_adjacent(curr.word,w):
                item.word = w 
                item.leng = curr.leng + 1 
                q.append(item)

                d.remove(w)
                if w == target:
                    return item.leng
    return 0

print shortest_chain(start,target,d)
        

