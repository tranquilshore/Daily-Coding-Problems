'''
https://www.youtube.com/watch?v=fZ3p2Iw-O2I
'''

n = 14
k = 2

def winner(n,k):
    if n == 1:
        return 0 
    return (winner(n-1,k)+k)%n 

print winner(n,k)