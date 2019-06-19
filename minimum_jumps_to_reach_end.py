#stairs and ladder concept for linear solution
def minjumps_linear(a):
    if len(a) <= 1:
        return 0
    ladder = a[0] #track of ladder
    stairs = a[0] #track of stairs
    jumps = 1
    for level in range(1,len(a)):
        if level == len(a) - 1:
            return jumps
        if level + a[level] > ladder:
            ladder = level + a[level]
        stairs -= 1
        if stairs == 0:
            jumps += 1
            stairs = ladder - level
    return jumps
#a = [2,3,1,1,2,4,2,0,1,1]
#a = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
a = [3,2,4,1,2,5,6,1]
print minjumps_linear(a)    