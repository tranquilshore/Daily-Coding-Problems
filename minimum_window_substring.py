'''
watch https://www.youtube.com/watch?v=qzYhjk-nDGU&t=267s for problem and solution's explanation
'''

import collections

s = "figehaeci"
t = "aei"

def minimum_substring_window(s,t):
    need = collections.Counter(t)
    l,r,i,j,missing = 0,0,0,0,len(t)

    while r < len(s):
        if need[s[r]] > 0 : missing -= 1
        need[s[r]] -= 1
        r += 1
        
        while missing == 0:
            if j == 0 or r-l < j-i:
                i,j = l,r 
            need[s[l]] += 1 
            if need[s[l]] > 0 : missing += 1
            l += 1
    return s[i:j]

print minimum_substring_window(s,t)