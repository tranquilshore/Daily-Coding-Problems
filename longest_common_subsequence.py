'''
recursive thinking involve:
1. if a[i] == b[j] then add 1 to result and move both i and j recursively
    i.e. 1 + LCS(i+1,j+1)

2. else check either way:
    2.1 move in first string LCS(i+1,j)
    2.2 move in second string LCS(i,j+1)
    and return the maximum among them

Same solution can be used to find:

1. "minimum insertions required for palindrome":
    a. Find lcs between s and s.reverse
    b. then substract len(s) - lcs

2. "shortest common supersequence":
    a. find lcs btw two strings lcs(s1,s2)
    b. insert non-lcs characters of original strings to the lcs found above.
    that will be the shortest common supersequence.

3. "longest palindromic subsequence":
    a. find lcs between s and s.reverse
    that will be the longest palindromic subsequence.

'''

a = "bd"
b = "abcd"
n = len(a)
m = len(b)

#recursive
def lcs(i,j):
    if i >= n or j>=m:
        return 0 
    elif a[i] == b[j]:
        return 1+lcs(i+1,j+1)
    else:
        return max(lcs(i+1,j), lcs(i,j+1))

print lcs(0,0)

#dp bottom up
def lcs_bottomup(a,b):
    n = len(a)
    m = len(b)

    T = [[0 for i in range(m+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1] == b[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
    
    return T[n][m]

print lcs_bottomup(a,b)



