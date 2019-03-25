'''
idea is to reduce the number of multiplications to be done inorder to find pow(x,y)
for even y:
    x^y = (x^2)^(y/2)
for odd y:
    x^y = x*((x^2)^(y-1)/2)

it will make time complexity of power function to be O(log y)
'''

def power(x,y):
    base = float(x) 
    exponent = y 
    if y == 0:
        return 1
    if y < 0:
        base = 1/base  
        exponent = -y 
    coeff = 1
    while exponent > 1:
        if exponent % 2 == 0:
            base *= base 
            exponent = exponent // 2
        else:
            coeff *= base 
            base *= base 
            exponent = (exponent-1)//2
    return coeff * base 

print power(4,7)