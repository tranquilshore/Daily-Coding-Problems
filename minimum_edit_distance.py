'''
Levenshtein Distance Problem:
minimum number of single character edits(ie. insertion,deletion or substitution) required to change 
one word into another. Each of these operations has unit cost.
watch https://www.youtube.com/watch?v=We3YDTzNXEk&t=239s for explanation.
watch https://www.geeksforgeeks.org/edit-distance-dp-5/ as well.
'''
#recursive
def editDistance(str1, str2, m , n):  
    if m==0: 
         return n 
    if n==0: 
        return m 
  
    # If last characters of two strings are same, nothing 
    # much to do. Ignore last characters and get count for 
    # remaining strings. 
    if str1[m-1]==str2[n-1]: 
        return editDistance(str1,str2,m-1,n-1) 
  
    # If last characters are not same, consider all three 
    # operations on last character of first string, recursively 
    # compute minimum cost for all three operations and take 
    # minimum of three values. 
    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert 
                   editDistance(str1, str2, m-1, n),    # Remove 
                   editDistance(str1, str2, m-1, n-1)    # Replace 
                   ) 


#dp
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

'''
minimum operations required to convert string A to string B. The only operation allowed is to move any character
from the first string to the front.

1. first confirm if both strings have same set of characters.
2. then simultaneously traverse both strings from end, if both character match move to next character. if it doesn't match 
    then keep counting the mismatch characters and keep moveing in first string till a match is found. Repeat the above untill we
    exhaust the strings.

https://www.techiedelight.com/find-minimum-operations-required-transform-string-into-another/
'''

