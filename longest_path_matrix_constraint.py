'''
https://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/
Given a n*n matrix where all numbers are distinct, find the maximum length path (starting from any cell) such that all cells along the path are in increasing order with a difference of 1.

We can move in 4 directions from a given cell (i, j), i.e., we can move to (i+1, j) or (i, j+1) or (i-1, j) or (i, j-1) with the condition that the adjacent cells have a difference of 1.

eg.
Input:  mat[][] = {{1, 2, 9}
                   {5, 3, 8}
                   {4, 6, 7}}
Output: 4
The longest path is 6-7-8-9.


The idea is simple, we calculate longest path beginning with every cell. Once we have computed longest for all cells, we return maximum of all longest paths. One important observation in this approach is many overlapping subproblems. Therefore this problem can be optimally solved using Dynamic Programming.
'''

mat = [[1, 2, 9],  
    [5, 3, 8], 
    [4, 6, 7]]

n = len(mat) #assuming n*n matrix

def find_path_from_cell(i,j,mat,dp):
    # Base case  
    if (i<0 or i>=n or j<0 or j>=n): 
        return 0
  
    # If this subproblem is already solved  
    if (dp[i][j] != -1):  
        return dp[i][j]

    # Since all numbers are unique and in range from 1 to n*n,  
    # there is atmost one possible direction from any cell  
    if j<n-1 and mat[i][j] +1 == mat[i][j+1]: 
        dp[i][j] = 1 + find_path_from_cell(i,j+1,mat,dp) 
        return dp[i][j] 
  
    if j>0 and mat[i][j] +1 == mat[i][j-1]:  
        dp[i][j] = 1 + find_path_from_cell(i,j-1,mat,dp) 
        return dp[i][j] 
  
    if i>0 and mat[i][j] +1 == mat[i-1][j]: 
        dp[i][j] = 1 + find_path_from_cell(i-1,j,mat,dp) 
        return dp[i][j]  
  
    if i<n-1 and mat[i][j] +1 == mat[i+1][j]: 
        dp[i][j] = 1 + find_path_from_cell(i+1,j,mat,dp) 
        return dp[i][j] 
  
    # If none of the adjacent fours is one greater  
    dp[i][j] = 1
    return dp[i][j] 
    


def longest_overall(mat):
    result = 1
    dp = [[-1 for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                find_path_from_cell(i,j,mat,dp)
            result = max(result,dp[i][j])
    return result

print longest_overall(mat)


