'''
Longest Common Subsequence
'''

s1 = "afctbm"
s2 = "fatmkb"

def longest_common_subsequence(s1,s2):
    n = len(s1)
    m = len(s2)

    T = [[0 for i in range(m+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]: #add i-1 != j-1 to get longest repeated subsequence
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max(T[i][j-1],T[i-1][j])
    
    return T[n][m]

print longest_common_subsequence(s1,s2) 

'''
Longest Palindromic Subsequence
'''

s = "RQPTPR"

def lognest_palindromic_subsequence(s):
    n = len(s)
    T = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):#single letter is already a palindrome
        T[i][i] = 1 

    for curr_len in range(1,n):
        i = 0
        for j in range(curr_len,n):
            if s[i] == s[j]:
                T[i][j] = 2 + T[i+1][j-1]
            else:
                T[i][j] = max(T[i+1][j],T[i][j-1])
            i += 1

    return T[0][n-1]

print lognest_palindromic_subsequence(s)

'''
Longest Palindromic substring
'''
s = "banana"

def longest_palindromic_substring(s):
    n = len(s) 
    T = [[False for i in range(n)] for i in range(n)]

    res = 1 
    for i in range(n):
        T[i][i] = True 

    for curr_len in range(1,n):
        i = 0 
        for j in range(curr_len,n):
            if s[i] == s[j] and T[i+1][j-1]:
                res = max(res,curr_len)
                T[i][j] = True 
            else:
                T[i][j] = False 
            i += 1 
    return res+1

print longest_palindromic_substring(s)

'''
Minimum insertion for palindrome
'''
s = "geeks"

def min_insert_for_palindrome(s):
    n = len(s)
    T = [[0 for i in range(n)] for i in range(n)]

    for curr_len in range(1,n):
        i = 0 
        for j in range(curr_len,n):
            if s[i] == s[j]:
                T[i][j] = T[i+1][j-1]
            else:
                T[i][j] = 1 + min(T[i+1][j],T[i][j-1])
            i += 1 

    return T[0][n-1]

print min_insert_for_palindrome(s)

'''
Minimum deletion to make palindrome!
Idea: just find longest palindromic subsequence and subtract the its length from the total length.

Find if string is K-Palindrome or not!
Idea: This also can be solved like above, at the end just check that minimum deletion length is less than k or not.
'''

'''
Permutations of a string
'''
s = "abc"
s = list(s)
l = 0
r = len(s)-1
def permutations(s,l,r):
    if l == r:
        print s 
    else:
        for i in range(l,r+1):
            s[l],s[i] = s[i],s[l]
            permutations(s,l+1,r)
            s[l],s[i] = s[i],s[l] 

print permutations(s,l,r)

'''
Longest Non-Repeating Substring
'''

s = "sahail"
def longest_non_repeating(s):
    n = len(s)
    res = 0
    start = 0
    d = {}
    for i,c in enumerate(s):
        if c in d:
            res = max(res,i-start)
            start = max(start,d[c]+1)
        d[c] = i 
    return max(res,n-start)

print longest_non_repeating(s)

'''
Word Break Problem
'''

s = "ilikesamsung"
d = ["i","like","sam","sung"]

def word_break(s,d):
    if len(s) == 0:
        return True 
    for i in range(1,len(s)+1):
        prefix = s[:i]
        if prefix in d and word_break(s[i:],d):
            return True 
    return False 

print word_break(s,d)

lookup = {}
def word_break_dp_toptobottom(s,d):
    n = len(s)
    if n == 0:#that if we reach the end of the string
        return True 
    
    if lookup.has_key(n) is False:
        lookup[n] = False #marking subproblem as seen(0 assuming initially string can't be segmented)
        for i in range(1,n+1):
            prefix = s[:i]
            if prefix in d and word_break_dp_toptobottom(s[i:],d):
                lookup[n] = True 
                return lookup[n]
    return lookup[n]  
        
print word_break_dp_toptobottom(s,d)

def word_break_dp_bottom_up(s,d):
    n = len(s)
    T = [[False for i in range(n)] for i in range(n)]

    for i in range(n):
        if s[i] in d:
            T[i][i] = True 
    
    for curr_len in range(1,n):
        i = 0 
        for j in range(curr_len,n):
            curr_str = s[i:j+1]
            
            if curr_str in d:
                T[i][j] = True 
                continue 

            for k in range(i+1,j+1):
                if T[i][k-1] and T[k][j]:
                    T[i][j] = True 
                    break 
            i += 1
    
    return T[0][n-1]

print word_break_dp_bottom_up(s,d)

    



