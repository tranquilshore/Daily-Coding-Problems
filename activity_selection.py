'''
You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

Example 2 : Consider the following 6 activities 
sorted by by finish time.
     start[]  =  {1, 3, 0, 5, 8, 5};
     finish[] =  {2, 4, 6, 7, 9, 9};
A person can perform at most four activities. The 
maximum set of activities that can be executed 
is {0, 1, 3, 4} [ These are indexes in start[] and 
finish[] ]

idea is to sort the elements based upon their finishing time now compare finish of first element with start of next element,
if it is less, then add that to answer
'''

start  =  [1, 3, 0, 5, 8, 5];
finish =  [2, 4, 6, 7, 9, 9];

def activity_selection(start,finish):
    n = len(start)

    i = 0
    count = 1 #first activity is always selected - important step
    for j in range(1,n):
        if start[j] >= finish[i]:
            count += 1
            i = j 
    return count 

print activity_selection(start,finish)
