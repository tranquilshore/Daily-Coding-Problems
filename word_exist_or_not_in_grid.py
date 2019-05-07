grid = ["axmy",
        "bgdf",  
        "xeet",
        "raks"]
pat = "geeks"

r = len(grid)
c = len(grid[0])

def check_match(pat,grid):
    l = len(pat)

    #if total characters in matrix are less than pat
    if l > r*c:
        return False 

    for i in range(r):
        for j in range(c):
            #if first letter matches, then recurse and check
            if grid[i][j] == pat[0]:
                if find_match(pat,grid,i,j,0):
                    return True 
    return False 

def find_match(pat,grid,i,j,level):
    l = len(pat)
    #pattern matched
    if level == l:
        return True 
    #checking boudary conditions
    if i<0 or j<0 or i>=r or j>=c:
        return False 
    
    #if a grid matches with the letter while recursion
    if grid[i][j] == pat[level]:
        #marking cell as visited 
        temp = grid[i][j]
        grid[i].replace(grid[i][j],"#")

        #find subpattern in rest 4 directions
        res =   find_match(pat,grid,i-1,j,level+1) or find_match(pat,grid,i+1,j,level+1) or find_match(pat,grid,i,j-1,level+1) or find_match(pat,grid,i,j+1,level+1)

        #making cell unvisited again - backtracking
        grid[i].replace(grid[i][j],temp)
        return res 
    else:
        return False 


print check_match(pat,grid)

