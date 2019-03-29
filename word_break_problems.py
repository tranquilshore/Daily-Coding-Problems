'''
Given an input string and dictionary of words. find out if input string can be segmented into a space separated sequence of dictionary words.
eg. dictionary - { i, like, sam, sung, samsung, mobile, ice, cream, icecream, man, go, mango}
    input string - "ilike"
    output - True

Recursive idea: consider each prefix and search it in dictionary. If prefix is present in dictionary we recurse for rest of the string(suffix).
if recursive call for suffix returns true, we return true, otherwise we try next prefix. 
if tried all prefixes and none of them resulted in solution, return false 
'''

string = "iloveicecreamandmango"
dic = ["mobile","samsung","sam","sung","man","mango", "icecream","and","go","i","love","ice","cream"]

def dictionary_contains(word):
    if word in dic:
        return True 
    return False 

def word_break(dic,string):
    if len(string) == 0: #returns true if reach end of the string
        return True 
    
    for i in range(1,len(string)+1):#take prefix and check and recurse for the rest of the string 
        prefix = string[:i]
        if dictionary_contains(prefix) and word_break(dic,string[i:]):
            return True 
    return False 

print word_break(dic,string)

#as above problem have both optimal substructure and overlapping subproblems feature, we will use dp top down approach
from collections import defaultdict
lookup = defaultdict(bool)
def word_break_dp(dic,string,lookup):
    n = len(string)
    if n == 0:
        return True 

    if lookup.has_key(n) == False: #seen for the first time 
        for i in range(1,n+1):
            prefix = string[:i]
            if dictionary_contains(prefix) and word_break_dp(dic,string[i:],lookup):
                lookup[n] = True 
                return lookup[n]
    return lookup[n]

print word_break_dp(dic,string,lookup)

'''
Word break Problem:
Print all the ways in which the string can be segmented.
Backtracking
'''

def word_bread_all_segments(dic,string,res):
    n = len(string)
    if n == 0:
        print res 
        return

    for i in range(1,n+1):
        prefix = string[:i]
        if dictionary_contains(prefix):
            word_bread_all_segments(dic,string[i:],res+" "+prefix)

word_bread_all_segments(dic,string,"")




