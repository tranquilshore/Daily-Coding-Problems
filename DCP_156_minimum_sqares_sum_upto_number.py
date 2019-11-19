n = 27

def min_sqares(n):
    if n <= 3:
        return n 
    
    res = n
    for x in range(1,n+1):
        temp = x*x 
        if temp > n:
            break 
        else:
            res = min(res,1+min_sqares(n-temp))
    return res 

dp = {}
def min_sqares_dp(n):
    if n <= 3:
        return n 
    
    if n in dp:
        return dp[n]
    
    res = n 
    for x in range(1,n+1):
        temp = x*x 
        if temp > n:
            break 
        else:
            res = min(res,1+min_sqares(n-temp))
            dp[n] = res 
    return dp[n]



print min_sqares_dp(n)