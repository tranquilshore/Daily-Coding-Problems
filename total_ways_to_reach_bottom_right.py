r = 5
c = 5

m = [[0 for i in range(r)] for i in range(c)]

for i in range(r):
    m[0][i] = 1

for i in range(c):
    m[i][0] = 1

for i in range(1,r):
    for j in range(1,c):
        m[i][j] = m[i-1][j] + m[i][j-1]

print m[r-1][c-1]