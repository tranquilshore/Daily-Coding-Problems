'''
https://www.geeksforgeeks.org/minimum-number-operation-required-convert-number-x-y/
and https://www.geeksforgeeks.org/convert-number-m-n-using-minimum-number-given-operations/

This solution works for both

Given a initial number x and two operations which are given below:
1. Multiply number by 2.
2. Subtract 1 from the number.

The task is to find out minimum number of operation required to convert number x into y using only above two operations. We can apply these operations any number of times.
Constraints:
1 <= x, y <= 10000

The idea is to use BFS for this. We run a BFS and create nodes by multiplying with 2 and subtracting by 1, thus we can obtain all possible numbers reachable from starting number.
Important Points :
1) When we subtract 1 from a number and if it becomes < 0 i.e. Negative then there is no reason to create next node from it (As per input constraints, numbers x and y are positive).
2) Also, if we have already created a number then there is no reason to create it again. i.e. we maintain a visited array.

'''

class Node:
    def __init__(self,value,level):
        self.value = value 
        self.level = level 
    
def min_operations(x,y):
    visit = []
    q = []
    q.append(Node(x,0))

    while q:
        tmp = q.pop(0)

        if tmp.value == y :
            return tmp.level 
        
        visit.append(tmp.value)
        
        if tmp.value*2 not in visit:
            q.append(Node(tmp.value*2,tmp.level+1))
        
        if tmp.value-1 >= 0 and tmp.value-1 not in visit:
            q.append(Node(tmp.value-1, tmp.level+1))
    
    return -1
print min_operations(15,20)





