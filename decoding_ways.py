'''
https://www.youtube.com/watch?v=qli-JCrSwuk&t=886s to understand
'''
inpt = "1234"
n = len(inpt)

def decode_ways(inpt,n):
    if n == 0:
        return 1
    s = len(inpt)-n 
    if inpt[s] == 0:
        return 0 
    
    result = decode_ways(inpt,n-1)
    if n >= 2 and int(inpt[s:s+2]) <= 26:
        result += decode_ways(inpt,n-2)
    return result 

print decode_ways(inpt,n)

dp = [None]*(n+1)
def decode_ways_dp(inpt,n,dp):
    if n == 0:
        return 1
    s = len(inpt)-n 
    if inpt[s] == 0:
        return 0 
    
    #change 1
    if dp[n] != None:
        return dp[n]
    
    result = decode_ways_dp(inpt,n-1,dp)
    if n >= 2 and int(inpt[s:s+2]) <= 26:
        result += decode_ways_dp(inpt,n-2,dp)
    #change 2
    dp[n] = result
    return result

print decode_ways_dp(inpt,n,dp)