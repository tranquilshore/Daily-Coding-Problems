'''
Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.
'''

mapping = {
    '1':['a','b','c'],
    '2':['d','e','f'],
    '3':['g','h','i'],
    '4':['j','k','l'],
    '5':['m','n','o'],
    '6':['p','q','r','s'],
    '7':['t','u','v'],
    '8':['w','x','y','z']
}

digits = '222'

def get_permutations(digits,mapping):
    digit = digits[0]

    if len(digits) == 1:
        return mapping[digit]

    result = []
    for char in mapping[digit]:
        for perm in get_permutations(digits[1:],mapping):
            result.append(char+perm)
    return result

print get_permutations(digits,mapping)