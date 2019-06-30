'''
watch this to get the gist of it
https://www.youtube.com/watch?v=q6RicK1FCUs
'''
n = 3
#n - no. of discs | A,B,C - towers 
#movement goes like this: move discs from A to C using B 
def tower_of_hanoi(n,A,B,C):
    if n > 0:
        tower_of_hanoi(n-1,A,C,B) #move n-1 discs from A to B using C
        print "move disc from ",A," to ", C  
        tower_of_hanoi(n-1,B,A,C) #move n-1 discs from B to C using A 

print tower_of_hanoi(n,"A","B","C")
