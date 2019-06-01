a = "sahilthakur"
b = "trilthmur"

def longest_common_substring(a,b):
    n = len(a)
    m = len(b)

    T = [[0 for i in range(m+1)] for i in range(n+1)]
    res = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1] == b[j-1]:
                T[i][j] = T[i-1][j-1] + 1
                res = max(res,T[i][j])
            else:
                T[i][j] = 0
    return res 

print longest_common_substring(a,b)