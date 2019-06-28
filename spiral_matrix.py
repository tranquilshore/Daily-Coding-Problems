m = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [12,14,15,16]
]

r = len(m)
c = len(m[0])

#just need to take 4 pointers for row and col's start and end and keep changing them after every for loop
def print_spiral(m,r,c):
    row_start = 0
    row_end = r-1
    col_start = 0
    col_end = c-1

    while row_start < row_end and col_start < col_end:
        for i in range(col_start,col_end+1):
            print m[row_start][i],
        row_start += 1

        for i in range(row_start,row_end+1):
            print m[i][col_end],
        col_end -= 1

        for i in range(col_end,col_start-1,-1):
            print m[row_end][i],
        row_end -= 1 

        for i in range(row_end,row_start-1,-1):
            print m[i][col_start],
        col_start += 1

print_spiral(m,r,c) 


    
