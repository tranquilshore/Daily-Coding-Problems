from collections import defaultdict
import sys 
s = "dog cat hello cat dog dog world cat hello"

w1 = "hello"
w2 = "world"

def smallest_distance(s,w1,w2):
    s_arr = s.split(" ")
    n = len(s_arr)
    min_dist = n+1

    if w1 == w2:
        return 0
    
    for i in range(n):
        if s_arr[i] == w1 or s_arr[i] == w2:
            prev = i 
            break 
    
    while i < n:
        if s_arr[i] == w1 or s_arr[i] == w2:
            if s_arr[prev] != s_arr[i] and i - prev < min_dist:
                min_dist = i-prev-1
                prev = i 
            else:
                prev = i 
        i += 1 
    return min_dist

print smallest_distance(s,w1,w2)


        
        
            