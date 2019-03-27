'''
Sudoku Solver:
Given a partially filled 9X9 grid, the goal is to assign digits from 1 to 9 to the empty cells, so that every row, column and subgrid of size 3X3
contains exactly one instance of the digits from 1 to 9
'''

grid=[[3,0,6,5,0,8,4,0,0], 
    [5,2,0,0,0,0,0,0,0], 
    [0,8,7,0,0,0,0,3,1], 
    [0,0,3,0,1,0,0,8,0], 
    [9,0,0,8,6,3,0,0,5], 
    [0,5,0,0,9,0,6,0,0], 
    [1,3,0,0,0,0,2,5,0], 
    [0,0,0,0,0,0,0,7,4], 
    [0,0,5,2,0,6,3,0,0]]

def find_empty_location(grid,l):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                l[0] = row 
                l[1] = col 
                return True 
    return False

def used_in_row(grid,row,num):
    for i in range(9):
        if grid[row][i] == num:
            return True 
    return False 

def used_in_col(grid,col,num):
    for i in range(9):
        if grid[i][col] == num:
            return True 
    return False 

def used_in_box(grid,row,col,num):
    for i in range(3):
        for j in range(3):
            if grid[i+row][j+col] == num:
                return True 
    return False 

def check_location_is_safe(grid,row,col,num):
    return not used_in_row(grid,row,num) and not used_in_col(grid,col,num) and not used_in_box(grid,row-row%3,col-col%3,num)

def sudoku_solver(grid):
    l = [0,0]

    if not find_empty_location(grid,l):
        return True 
    
    row = l[0]
    col = l[1]

    for num in range(1,10):
        if check_location_is_safe(grid,row,col,num):
            grid[row][col] = num 

            if sudoku_solver(grid):
                return True 
            
            grid[row][col] = 0 #backtrack step
    
    return False 

def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print grid[i][j],
        print 

if sudoku_solver(grid):
    print_grid(grid)
else:
    print "No solution exists!"

