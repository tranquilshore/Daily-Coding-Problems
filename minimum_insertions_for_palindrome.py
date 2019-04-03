'''
check string notes in notability for explanation.
Problem: minimum insertions required to convert a string to palinfromic string
'''
s = "geeks"
s = "abcba"
n = len(s)
dp = [[0 for i in range(n)] for i in range(n)]

def minimum_insertions(s,n):
    #this upper triangle traversal is same as for longest palindromic substring and subsequences as well
    for cur_len in range(2,n+1):
        for i in range(n-cur_len+1):
            j = i+cur_len-1

            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
    return dp[0][n-1]

print minimum_insertions(s,n)