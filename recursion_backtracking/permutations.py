'''
Problem: Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Backtracking Approach: Start traversing the list from left to right, take each element of list and swap it with itself and every other element of list on its right.
Take one pointer lets call it first, which will get swaped with itself and with other pointer called i which will traverse from first to end of the list. After one element
is swaped, it will recurse for the  rest of the elements. When one solution is found, to find other solutions, it should undo the swap and again swap for other different 
pointers (backtracking step).
Lets look at its recursive tree:
                                                             
                                                             (f=0) 
                                                             f
                                                             i
                                                             0,1,2  (swap f with i)
                                                            [1,2,3]
                                     /                                      \
                                (f=1) 3                                     (f=0) 3(represents step no. in code)
                                  f                                         f                               \
           (swap f with i)        i                                           i                        ...................
                                0,1,2                                       0,1,2                       (keep following like this to get all permutations)
                               [1,2,3]                                     [2,1,3]
                        /               \                                /          \
                    (f=2) 3            (f=1) 3                      (f=1) 3         (f=1) 3
                        f                 f                           f               f
                        i                   i                         i                 i
                    0,1,2               0,1,2                       0,1,2           0,1,2
                   [1,2,3]             [1,3,2]                     [2,1,3]         [2,3,1]
                /                        /                          /                  /
            (f==3) 3                   (f=2) 3                  (f=2) 3             (f=2) 3
        output=[[1,2,3]]                    f                       f                   f
                                            i                       i                   i
                                        0,1,2                   0,1,2               0,1,2
                                       [1,3,2]                 [2,1,3]             [2,3,1]
                                       /                        /                       \
                                    (f=3) 3                   (f=3) 3                   (f=3) 3
                                output=[[1,2,3]             output=[[1,2,3],            output=[[1,2,3],
                                        [1,3,2]]                    [1,3,2],                    [1,3,2],
                                                                    [2,1,3]]                    [2,1,3],
                                                                                                [2,3,1]]
                                
Time complexity is close to O(n!)
'''
nums = [1, 2, 3]


def permutations(nums):
    n = len(nums)
    ans = []

    def backtrack(f=0):
        # 1 base case
        if f == n:
            ans.append(nums[:])

        for i in range(f, n):
            # 2 swap for the first time
            nums[f], nums[i] = nums[i], nums[f]
            # 3 recursive step with f incremented by 1
            backtrack(f+1)
            # 4 undo the step 2
            nums[f], nums[i] = nums[i], nums[f]

    backtrack()
    return ans


print permutations(nums)
