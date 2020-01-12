'''
Problem: Given a set of distinct integers, nums, return all possible subsets (the power set).
For example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Backtracking Approach:  let us loop over the length of combination, rather than the candidate numbers, and generate all combinations for a given length with the help of backtracking technique.

nums = [1,2,3]
output = []

                                                  k=0
                                               (0,curr=[])
                                               output = [ [] ]

                                                  k=1
                                               (0,curr=[])
                                        /           |                  \
                            (1,curr=[1])          (2,curr=[2])          (3,curr=[3])
                            output=[[],[1]]      output=[[],[1],[2]]    output=[[],[1],[2],[3]]

                                                  k=2
                                               (0,curr=[])
                                        /                             \
                        (1,curr=[1])                                (2,curr=[2])
                        /           \                                   \
        (2,curr=[1,2])          (3,curr=[1,3])                          (3,curr=[2,3])
    output=[[],[1],[2],[3],     output=[[],[1],[2],[3],                 output=[[],[1],[2],[3],
            [1,2]]                      [1,2],[1,3]]                            [1,2],[1,3],[2,3]]

                                                  k=3
                                               (0,curr=[])
                                               /
                                            (1,curr=[1])
                                            /
                                        (2,curr=[1,2])
                                        /
                                    (3,curr=[1,2,3])
                                    output=[[],[1],[2],[3],
                                            [1,2],[1,3],[2,3],[1,2,3]]
                                                           

'''

def subsets(nums):
    def backtrack(first = 0, curr = []):
        # if the combination is done
        if len(curr) == k:  
            output.append(curr[:])
            return 
        for i in range(first, n):
            # add nums[i] into the current combination
            curr.append(nums[i])
            # use next integers to complete the combination
            backtrack(i + 1, curr)
            # backtrack
            curr.pop()
    
    output = []
    n = len(nums)
    for k in range(n + 1):
        backtrack()
    return output

nums = [1,2,3]
print subsets(nums)