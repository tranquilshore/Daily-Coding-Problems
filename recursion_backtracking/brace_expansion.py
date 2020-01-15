'''
Problem:
A string S represents a list of words.
Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  If there is more than one option, then curly braces delimit the options.  For example, "{a,b,c}" represents options ["a", "b", "c"].
For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].
Return all words that can be formed in this manner, in lexicographical order.

Example 1:

Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]

Backtracking Approach:
Create a list of lists by first parsing the input. eg. [[a,b],[c],[d,e]] then recurse over all the list elements till you reach
the end of the list. 

                                          pos      0    1    2
                                          lst   [[a,b],[c],[d,e]]
                                          curr = []
                                          ans = []

                                                (pos=0,curr,lst,ans)
                                                curr = [a]                              
                                    /                                                    \ (curr=[b])
                        (pos=1,curr,lst,ans)                                        (pos=1,curr,lst,ans)                                
                            curr= [a,c]                                                 curr=[b,c]
                        /                                                                   |
            (pos=2,curr,lst,ans)                                                   (pos=2,curr,lst,ans)
            curr = [a,c,d]                                                              curr=[b,c,d]
            /               \                                                   /                       \(curr will be [b,c,e])
                        (curr will be [a,c,e])                   (pos=3,curr,lst,ans)                  (pos=3,curr,lst,ans)
(pos=3,curr,lst,ans)      (pos=3,curr,lst,ans)                     ans=[acd,ace,bcd]                    ans=[acd,ace,bcd,bce]
ans=[acd]                   ans=[acd,ace]

'''

s = "{a,b}c{d,e}f"

def brace_expansion(s):
    curr = []
    lst = []
    strt_brace = False
    s = list(s)

    # code to parse the input
    for c in s:
        if c == '{':
            curr = []
            strt_brace = True 
        elif c == '}':
            strt_brace = False 
            lst.append(list(curr))
            curr = []
        elif strt_brace and c != ',':
            curr.append(c)
        elif not strt_brace:
            lst.append([c])
    
    def backtrack(pos,curr,lst,ans):
        if pos == len(lst):
            ans.append(''.join(curr))
            return 
        for choice in lst[pos]:
            curr.append(choice)
            backtrack(pos+1,curr,lst,ans)
            curr.pop()

    ans = []
    backtrack(0,[],lst,ans)
    ans.sort()
    return ans 

print brace_expansion(s)

