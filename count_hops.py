'''
Given a distance dist, count total number of ways to cover the distance with 1, 2 and 3 steps.
'''
dist = 4

#recursive
def count_hops(dist):
    if dist == 0:
        return 1
    if dist < 0:
        return 0 
    return count_hops(dist-1)+count_hops(dist-2)+count_hops(dist-3)

print count_hops(dist)

#dp
def count_hops_dp(dist):
    count = [0]*(dist+1)

    #there are one way to cover 0 and 1 distances
    count[0] = 1
    count[1] = 1
    #there are two ways to cover distance 2
    count[2] = 2

    for i in range(3,dist+1):
        count[i] = count[i-1]+count[i-2]+count[i-3]
    
    return count[dist]

print count_hops_dp(dist)