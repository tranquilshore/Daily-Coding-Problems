'''
Problem: 
In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

    Every time you are located in a cell you will collect all the gold in that cell.
    From your position you can walk one step to the left, right, up or down.
    You can't visit the same cell more than once.
    Never visit a cell with 0 gold.
    You can start and stop collecting gold from any position in the grid that has some gold.

Example:
Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.

DFS approach: We will recurse at every position of the grid and find maximum gold from all those positions.
Lets take a case when source is (0,1). We'll try to understand by looking at visited grid, which maintains the visited cells state of the grid.

                                                                0 0 0 
                                                                0 0 0 
                                                                0 0 0
                                                            /
                                                        0 1 0 
                                                        0 0 0 
                                                        0 0 0
                                                    res= [6]
                                                /
                                    0 1 0 
                                    0 1 0 
                                    0 0 0
                                res= [6,8]  
                    (backtracked when all children are done)
                        /           \                       \
                    0 1 0               0 1 0               0 1 0 
                    0 1 0               0 1 1               1 1 0 
                    0 1 0               0 0 0               0 0 0 
                res= [6,8,9]          res= [6,8,7]          res= [6,8,5]
        (no more to explore)        (no more to explore)    (no more to explore)
                backtrack              backtrack            backtrack

All the above nodes represents a path which is stored in res, keep track of maximum from all of them

'''

grid = [
    [0, 6, 0],
    [5, 8, 7],
    [0, 9, 0]
]


# checks for out of boundary, already visited and can't visit conditions
def check_conditions(grid, row, col, visited, x, y):
    return x >= 0 and x < row and y >= 0 and y < col and visited[x][y] != 1 and grid[x][y] != 0


def universal_max_path(grid):
    row = len(grid)
    col = len(grid[0])
    unv_max_gold = [0]

    def find_max_path(sx, sy, visited, res, max_val):

        if check_conditions(grid, row, col, visited, sx, sy):

            # add the element to result
            res.append(grid[sx][sy])
            visited[sx][sy] = 1

            # recurse at every neighbour
            find_max_path(sx+1, sy, visited, res, max_val)
            find_max_path(sx-1, sy, visited, res, max_val)
            find_max_path(sx, sy+1, visited, res, max_val)
            find_max_path(sx, sy-1, visited, res, max_val)

            # condition for max gold
            if max_val[0] < sum(res):
                max_val[0] = sum(res)
            # backtrack steps
            visited[sx][sy] = 0
            res.pop()

    # this will check max path from every position in the matrix
    for i in range(row):
        for j in range(col):
            visited = [[0 for l in range(col)] for m in range(row)]
            max_val = [0]
            find_max_path(i, j, visited, [], max_val)
            unv_max_gold[0] = max(unv_max_gold[0], max_val[0])

    return unv_max_gold[0]


print universal_max_path(grid)
