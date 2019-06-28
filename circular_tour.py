'''
https://leetcode.com/problems/gas-station/discuss/319512/O(n)-complexity-solution.
Suppose there is a circle. There are n petrol pumps on that circle. You are given two sets of data.
1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.

Calculate the first point from where a truck will be able to complete the circle (The truck will stop at each petrol pump and it has infinite capacity). Expected time complexity is O(n). Assume for 1 litre petrol, the truck can go 1 unit of distance.

For example, let there be 4 petrol pumps with amount of petrol and distance to next petrol pump value pairs as {4, 6}, {6, 5}, {7, 3} and {4, 5}. The first point from where truck can make a circular tour is 2nd petrol pump. Output should be start = 1 (index of 2nd petrol pump).

couple of points:

1. we first check if a solution exists by summing all gas values and all cost values and checking if sum(gas)>sum(cost). If this condition is satisfied, we are guaranteed a unique solution by the problem.
2. find the starting poiint.
'''
petrol = [4,6,7,4]
distance = [6,5,3,5]

n = len(petrol)

def circular_tour(petrol,distance,n):
    if sum(petrol) < sum(distance):
        return -1 

    balance = 0
    pos = 0
    for i in range(n):
        balance += petrol[i] - distance[i]
        if balance<0:
            pos = i+1 
            balance = 0
    
    return pos 

print circular_tour(petrol,distance,n)




