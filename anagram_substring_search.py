'''
This problem is slightly different from standard pattern searching problem
A simple idea is to modify Rabin Karp Algorithm.

read https://www.geeksforgeeks.org/anagram-substring-search-search-permutations/

We can achieve O(n) time complexity under the assumption that alphabet size is fixed which is typically true as we have maximum 256 possible characters in ASCII.

'''

max_space = 256

def search(text,pattern):
    m = len(pattern)
    n = len(text)

    count_pattern = [0]*max_space
    count_text = [0]*max_space
    
    
    for i in range(m):
        count_pattern[ord(pattern[i])] += 1
        count_text[ord(text[i])] += 1


    for i in range(m,n):
        if compare(count_pattern,count_text):
            print "found at",i-m 
        
        count_text[ord(text[i])] += 1
        count_text[ord(text[i-m])] -= 1

    if compare(count_pattern,count_text):
        print "found at",n-m

def compare(count_pattern,count_text):
    for i in range(max_space):
        if count_pattern[i] != count_text[i]:
            return False 
    return True 

txt = "BACDGABCDA"
pat = "ABCD"       
search(txt, pat)