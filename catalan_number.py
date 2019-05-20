'''
Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.
1) Count the number of expressions containing n pairs of parentheses which are correctly matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
2) Count the number of possible Binary Search Trees with n keys 
3) Number of different Unlabeled Binary Trees can be there with n nodes.
4) Number of ways to insert n pairs of parentheses in a word of n+1 letters.

watch https://www.youtube.com/watch?v=YDf982Lb84o 
'''

def catalan(n):
    catalan = [0 for i in range(n+1)]

    catalan[0] = 1
    catalan[1] = 1

    for i in range(2,n+1):
        for j in range(i):
            catalan[i] += catalan[j]*catalan[i-j-1]
    
    return catalan[n]

print catalan(5)
