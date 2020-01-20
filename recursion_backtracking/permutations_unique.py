'''
Problem: Given a collection of numbers that might contain duplicates, return all possible unique permutations.
Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

Approach: It is the same as of finding permutations. The only difference is to keep track of a character which has already seen.
'''

s = "112"


def permutations(nums):
    n = len(nums)
    ans = []

    def backtrack(f=0):
        # 1 base case
        if f == n:
            ans.append(nums[:])

        # added a set to take care of duplicates
        seen = set()
        for i in range(f, n):
            # if the character is seen for the first time
            if nums[i] not in seen:
                # 2 swap for the first time
                nums[f], nums[i] = nums[i], nums[f]
                # 3 recursive step with f incremented by 1
                backtrack(f+1)
                # 4 undo the step 2
                nums[f], nums[i] = nums[i], nums[f]
            seen.add(nums[i])

    backtrack()
    return ans


print permutations(list(s))
