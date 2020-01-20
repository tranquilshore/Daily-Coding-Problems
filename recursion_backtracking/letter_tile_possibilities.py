'''
Problem: You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.
Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Input: "AAABBC"
Output: 188

Gist: So the problem dropped down to finding unique permutaions of different size combinations of a given string.
'''

s = "AAABBC"


def combination(s, req_size, string_len):
    res = []

    def dfs(start, path, size):
        # 1 base case when we found the required size
        if size == req_size:
            res.append(path)
            return
        # 2 edge case when we reach the end of the string
        if start == string_len:
            return
        # 3 consider the character to be part
        dfs(start+1, path+s[start], size+1)
        # 4 do not consider the character
        dfs(start+1, path, size)

    dfs(0, "", 0)
    return res


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


def letter_tile_possibilities(s):
    ans = set()
    for i in range(1, len(s)+1):
        # get all different combinations of different size
        dfrnt_len_comb = combination(s, i, len(s))
        for elem in dfrnt_len_comb:
            # find the permutations of each combination
            all_permute = permutations(list(elem))
            # for uniqueness add them to set
            for permute in all_permute:
                ans.add("".join(permute))
    return len(ans)


print letter_tile_possibilities(s)
