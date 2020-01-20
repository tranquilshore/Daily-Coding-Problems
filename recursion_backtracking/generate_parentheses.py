'''
Problem: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


Brute Force:
Naive solution would be to generate all 2^{2n} sequences of '(' and ')' characters. Then, we will check if each one is valid.
Time Complexity for the above approach: O(2^{2n}n) For each of 2^{2n} sequences, we need to create and validate the sequence, which takes O(n) work.

Recursive/Backtracking approach:
Instead of adding '(' or ')' every time as in Approach 1, let's only add them when we know it will remain a valid sequence. We can do this by keeping track of the number of opening and closing brackets we have placed so far.
Recursion Tree would look like for num=3:
                                                                          s l r
                                                                        ('',0,0)
                                                                        l<3
                                                                        /
                                                                    ('(',1,0) 2
                                    l<3                                                                    r<l
                                /                                                                           \
                            ('((',2,0) 2                                                                ('()',1,1) 3
                        l<3                 r<l                                                             l<3
                        /                     \                                                             /
                    ('(((',3,0) 2           ('(()',2,1) 3                                           ('()(',2,1) 2
                        r<l                  l<3          r<l                                   l<3             r<l
                    /                     /                 \                                   /                \
            ('((()',3,1) 3          ('(()(',3,1) 2          ('(())',2,2) 3             ('()((',3,1) 3           ('()()',2,2) 2
                r<l                     r<l                     l<3                       r<l                       l<3                  
                /                     /                       \                             /                       \
        ('((())',3,2) 3          ('(()()',3,2) 3         ('(())(',3,2) 2            ('()(()',3,2) 3             ('()()(',3,2) 2
            r<l                     r<l                       r<l                       r<l                         r<l
            /                   /                             \                         /                             \
('((()))',3,3) 3            ('(()())',3,3) 3           ('(())()',3,3) 3         ('()(())',3,3) 3                   ('()()()',3,3) 3
ans=['((()))']             ans=['((()))',              ans=['((()))',           ans=['((()))',                     ans=['((()))',
                                '(()())']                  '(()())',                '(()())',                           '(()())',
                                                           '(())()']                '(())()',                           '(())()',
                                                                                    '()(())']                           '()(())',
                                                                                                                        '()()()']


'''
num = 3

def generate_parentheses(num):
    ans = []

    def backtrack(s="",left=0,right=0):
        #1 base case when it acheived required string length
        if len(s) == 2*num:
            ans.append(s)
            return 
        #2 start placing left bracket if it would not exceed N
        if left < num:
            backtrack(s+'(',left+1,right)
        #3 start placing right bracket if it would not exceed left
        if right < left:
            backtrack(s+')',left,right+1)
    
    backtrack()
    return ans 

print generate_parentheses(num)
