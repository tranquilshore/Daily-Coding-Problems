'''
https://www.geeksforgeeks.org/find-a-tour-that-visits-all-stations/
Suppose there is a circle. There are n petrol pumps on that circle. You are given two sets of data.
1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.

Calculate the first point from where a truck will be able to complete the circle (The truck will stop at each petrol pump and it has infinite capacity). Expected time complexity is O(n). Assume for 1 litre petrol, the truck can go 1 unit of distance.

For example, let there be 4 petrol pumps with amount of petrol and distance to next petrol pump value pairs as {4, 6}, {6, 5}, {7, 3} and {4, 5}. The first point from where truck can make a circular tour is 2nd petrol pump. Output should be start = 1 (index of 2nd petrol pump).
'''

class petrol_pump:
    def __init__(self,petrol,distance):
        self.petrol = petrol
        self.distance = distance

def start_of_tour(a):
    n = len(a)

    #consider first as start and second as the end
    start = 0 
    end = 1

    curr_petrol = a[start].petrol - a[start].distance
    #while all pumps are not visited 
    while start != end:
        while start != end and curr_petrol < 0:
            curr_petrol -= a[start].petrol - a[start].distance
            start = (start+1)%n 
            #zero is considered as start again, so no possible solution
            if start == 0:
                return -1 
        curr_petrol += a[end].petrol - a[end].distance
        end = (end+1)%n 
    return start 

a = [petrol_pump(6,4), petrol_pump(3,6),petrol_pump(7,3)]
a = [petrol_pump(4,6), petrol_pump(6,5), petrol_pump(7,3), petrol_pump(4,5)]
print start_of_tour(a)



