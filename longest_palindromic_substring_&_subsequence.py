'''
Longest Palindromic Substring:
watch https://www.youtube.com/watch?v=obBdxeCx_Qs or see notability notes for polynomial solution
manacher's algorithm gives the linear solution for this problem.
'''

s = "banana"
s = "strtmtrk"

#polynomial solution O(n^2)
def longest_palindromic_substring(s):
    n = len(s)
    T = [[0 for i in range(n)] for i in range(n)]
    maxlen = 1
    start = 0

    #a single character is always a palindrome
    for i in range(n):
        T[i][i] = True 
    
    #for substrings of length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            T[i][i+1] = True 
            start = i 
            maxlen = 2

    #for substrings of length 3 or more, here i and j finds the first and last index of current length of substring
    for cur_len in range(3,n+1):
        for i in range(n-cur_len+1):
            j = i+cur_len-1

            if s[i] == s[j] and T[i+1][j-1]:
                T[i][j] = True 
                start = i 
                maxlen = cur_len

    return s[start:maxlen+2]

print longest_palindromic_substring(s)

s = "agbdba"

'''
Longest Palindromic Subsequence:
watch https://www.youtube.com/watch?v=_nCsPn7_OgI for explanation.

Both problems will fill the matrix in upper triangle fashion. Follows same traversing pattern.
'''

def longest_palindromic_subsequence(s):
    n = len(s)
    T = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        T[i][i] = 1

    for cur_len in range(2,n+1):
        for i in range(n-cur_len+1):
            j = i+cur_len-1

            if s[i] == s[j]:
                T[i][j] = 2 + T[i+1][j-1]
            else:
                T[i][j] = max(T[i+1][j], T[i][j-1])
    
    return T[0][n-1]

print longest_palindromic_subsequence(s)

'''
Given a string, find out if the string is K-Palindrome or not. A K-palindrome string transforms into a palindrome on removing at most k characters from it.

eg String - abcdecba, k = 1 ans - yes

If the difference between longest palindromic 
subsequence and the original string is less 
than equal to k, then the string is k-palindrome

'''

    