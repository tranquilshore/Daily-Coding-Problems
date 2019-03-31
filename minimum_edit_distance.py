'''
Levenshtein Distance Problem:
minimum number of single character edits(ie. insertion,deletion or substitution) required to change 
one word into another. Each of these operations has unit cost.
watch https://www.youtube.com/watch?v=We3YDTzNXEk&t=239s for explanation.
watch https://www.geeksforgeeks.org/edit-distance-dp-5/ as well.
'''

def levenshtein_distance(s1,s2,m,n):
    #added extra row and col for null string
    dp = [[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i 
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])

    return dp[m][n]

s1 = "sunday"
s2 = "saturday"
print levenshtein_distance(s1,s2,len(s1),len(s2))