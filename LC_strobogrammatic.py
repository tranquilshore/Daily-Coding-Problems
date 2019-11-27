'''
Read this https://leetcode.com/problems/strobogrammatic-number-ii/discuss/418620/Awesome-algorithm-with-easy-and-detailed-explanation!-Beats-96-runtime-100-memory 
for perfect explanation.
'''
def find_strobogrammatic(n):
    layer_pairs = [('0','0'),('1','1'),('6','9'),('8','8'),('9','6')]
    
    if n%2 == 0:
        inner_numbers = ['']
    else:
        inner_numbers = ['0','1','8']
    
    layers = n/2 

    for l in range(layers):
        new_inner_numbers = []
        for inner_number in inner_numbers:
            for lp in layer_pairs:
                if l == layers-1 and lp[0] == '0':
                    continue 
                new_inner_number = lp[0] + inner_number + lp[1]
                new_inner_numbers.append(new_inner_number)
        inner_numbers = new_inner_numbers 
    
    return inner_numbers

print find_strobogrammatic(3)
