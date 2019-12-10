'''
To rotate a matrix by 90 clockwise:
eg:
1,2,3    7,4,1
4,5,6 -> 8,5,2
7,8,9    9,6,3

steps:
1. take transpose
2. reverse the rows

To rotate a matrix by 90 anticlockwise:
eg:
1,2,3    3,6,9
4,5,6 -> 2,5,8
7,8,9    1,4,7

steps:
1. take transpose
2. reverse the columns
'''

m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

r = len(m)
c = len(m[0])

def transpose(m,r,c):
    for i in range(0,r):
        for j in range(i,c):
            temp = m[i][j]
            m[i][j] = m[j][i]
            m[j][i] = temp 

def reverse_rows(m,r,c):
    for i in range(0,r):
        m[i].reverse()

transpose(m,r,c)
reverse_rows(m,r,c)

print m 

