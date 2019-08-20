#check https://www.youtube.com/watch?v=oDhu5uGq_ic
#time complexity of the following approach is O(n^2k) can be made O(nk)
k = 2
prices = [5,2,4,0,1]

def maximum_profit(k,prices):
    n = k+1
    m = len(prices)

    T = [[0 for i in range(m)] for i in range(n)]

    for i in range(1,n):
        for j in range(1,m):
            max_so_far = 0

            for k in range(j):
                curr_price = prices[j] - prices[k] + T[i-1][k]
                if curr_price>max_so_far:
                    max_so_far = curr_price

            T[i][j] = max(T[i][j-1], max_so_far)
    
    return T[n-1][m-1]

print maximum_profit(k,prices)