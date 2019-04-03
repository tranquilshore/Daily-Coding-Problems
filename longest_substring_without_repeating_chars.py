'''
traverse the string from left to right and keep putting into dictionary untill you find a char which already existed in dictionary.
if char existed update the result as max(res,i-start) and start variable as max(start,d[c]+1). At very end result the max(res,len(s)-start)
'''

s = "acbdcafa"

def lswrc(s):
    start = end = res = 0
    d = {}
    for i,c in enumerate(s):
        if c in d:
            res = max(res,i-start)
            start = max(start,d[c]+1)
        d[c] = i 
    return max(res,len(s)-start)

print lswrc(s)
