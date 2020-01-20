'''
Problem: Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Approach: This problem is exactly same as "brace_expansion" problem solved previously. Look at that problem to see how its recursive
tree would be built.
'''

num = "23"

def phone_letter_combinations(num):
    num_list = list(num)

    phone_dic = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
    }

    lst = []
    for num in num_list:
        lst.append(phone_dic[num])
    
    curr = []
    ans = []

    def backtrack(pos,curr,lst,ans):
        if pos == len(lst):
            ans.append(''.join(curr))
            return 
        for choice in lst[pos]:
            curr.append(choice)
            backtrack(pos+1,curr,lst,ans)
            curr.pop()

    backtrack(0,curr,lst,ans)
    # to handle the edge case where [""] should be printed as []
    return ans if len(ans[0]) > 0 else []

print phone_letter_combinations(num)