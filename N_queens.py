'''
N Queens:
Problem of placing N chess queens on an N*N chess board so that no two queens attack each other. Print any one of the solution.
Read this: https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
watch the video in the link to understand the is_safe function.

we traverse columnwise. if all columns are exhausted we will have the answer.
else we try putting queen in all the rows of the column one by one, if it produces the valid answer we will move ahead else backtrack.
'''

N = 4
board = [ [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0] 
        ]
#why check only these directions, you can understand by watching the video on the above link
def is_safe(board,row,col):

    #check the row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False 

    #check upper diagonal on left side 
    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False 

    #check lower diagonal on left side
    for i,j in zip(range(row,N),range(col,-1,-1)):
        if board[i][j] == 1:
            return False 
    #if nothing False then return True 
    return True 

def solve_N_queen(board,col):
    #if col becomes equal or more than N, means all queens are placed then return True 
    if col >= N:
        print_board(board)
        return True 

    #res = False #for all possible solutions
    for i in range(N):
        if is_safe(board,i,col):
            board[i][col] = 1 #placing the queen on board

            #res = solve_N_queen(board,col+1) or res #make sure if any placement is possible to print all possible solutions
            if solve_N_queen(board,col+1):
                return True 
            
            board[i][col] = 0 #backtrack step 
    #return res #for all possible solutions
    return False 

def print_board(board):
    for i in range(N):
        for j in range(N):
            print board[i][j],
        print
    print 

if solve_N_queen(board,0) == False:
    print "Solution doesn't exist!"




    