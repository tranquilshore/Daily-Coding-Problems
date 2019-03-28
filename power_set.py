'''
Find power set of a set:
read - https://www.geeksforgeeks.org/recursive-program-to-generate-power-set/
Recursive solution: idea is equivalent to most of the other question with following two cases:
1. consider current character as part of current subset
2. do not consider current character as part of current subset.
'''

s = ['a','b','c']
ans = []
def power_set(s,index,ans):
    n = len(s)

    if index == n:
        print ans
        return 
    
    power_set(s,index+1,ans + [s[index]])
    power_set(s,index+1,ans)

power_set(s,0,ans)
