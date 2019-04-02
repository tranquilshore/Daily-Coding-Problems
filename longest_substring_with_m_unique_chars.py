'''
Given a string and a positive number m, find longest substring containing m distinct characters. if k is more than length of string 
return the whole string.

watch https://www.youtube.com/watch?v=8AQra0p_HmI&t=364s for explanation how sliding window technique works
read this https://www.techiedelight.com/find-longest-substring-containing-k-distinct-characters/ to understand the code 
'''

from collections import defaultdict

s = "arappa"
#s = "abcbdbdbbdcdabd"
n = len(s)
m = 2

d = defaultdict(int)


def lswmuc(s,n,m):
    start = end = 0 
    low = 0

    for high in range(n):
        d[s[high]] += 1

        #if window size is more than m, remove charcters from left 
        while len(d) > m:
            d[s[low]] -= 1
            #if frequency of leftmost char becomes 0 remove it from dictionary 
            if d[s[low]] == 0:
                del d[s[low]]
            low += 1 #shrink the window from left 

        #update the result
        if end - start < high - low:
            start = low 
            end = high 
    
    return s[start:end+1]

print lswmuc(s,n,m)
