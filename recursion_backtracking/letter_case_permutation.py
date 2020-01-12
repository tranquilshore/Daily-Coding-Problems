'''
Problem: Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string. 
Return a list of all possible strings we could create.

eg.
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]


Recursive approach:
Recursion Tree: going from left to right of given string we have two options to do when a character is an alphabet.
i.e. make it lowercase or uppercase. 

                    a1b2                i=0, char[i] is a letter, so we can either make it uppercase or lowercase
               /           \
           A1b2            a1b2         i=1, char[i] is a number, just increment i
            |                |
           A1b2             a1b2        i=2, char[i] is a letter, make it uppercase or lowercase
        /       \          /     \
      A1B2     A1b2      a1B2    a1b2   i==len(S), add it to result

'''

s = "a1b2"

def letter_case_permutation(s):
    size = len(s)
    res = []

    def backtrack(s,word,i):
        if i == len(s):
            res.append(word)
            return 

        if s[i].isalpha():
            backtrack(s,word+s[i].lower(),i+1)
            backtrack(s,word+s[i].upper(),i+1)
        else:
            backtrack(s,word+s[i],i+1)

    backtrack(s,"",0)
    return res

print letter_case_permutation(s)
