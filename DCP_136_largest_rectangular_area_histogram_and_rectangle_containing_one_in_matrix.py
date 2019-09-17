m = [
    [1,0,0,0],
    [1,0,1,1],
    [1,0,1,1],
    [0,1,0,0]
]
r = len(m)
c = len(m[0])

def max_rect_area_hist(arr):
    new_arr = [-1] + arr + [-1]
    stack = [0]
    ans = 0
    n = len(new_arr)

    for i in range(n):
        while new_arr[i] < new_arr[stack[-1]]:
            h = new_arr[stack.pop()]
            area = h*(i-stack[-1]-1)
            ans = max(area,ans)
        stack.append(i)
    return ans

def max_rect_with_ones(m,r,c):
    res = max_rect_area_hist(m[0])
    res_arr = [i+j for i,j in zip(m[1],m[0])]
    for i in range(2,r):
        res_arr = [i+j for i,j in zip(m[i],res_arr)]
        res = max(res,max_rect_area_hist(res_arr))

    return res 

print max_rect_with_ones(m,r,c)

