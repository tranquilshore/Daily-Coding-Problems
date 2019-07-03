'''
use recursion
idea is to consider every input digit one by one, replace the character with every character in the 
mobile keypad and recur for the next digit. When all the digits are processed, print the result.
'''

keypad = [
    [],
    [],
    ['A','B','C'],
    ['D','E','F'],
    ['G','H','I'],
    ['J','K','L'],
    ['M','N','O'],
    ['P','Q','R','S'],
    ['T','U','V'],
    ['W','X','Y','Z']
]

inpt = [2,3]
n = len(inpt)

def find_combinations(keypad,inpt,res,index):
    #if every digit is processed print result
    if index == -1:
        print res," ",
        return 
    #get the current digit
    digit = inpt[index]
    
    #get the length of character set for that digit
    charsize = len(keypad[digit])

    #one by one replace the digit with each character in corresponding list and recur for next digit
    for i in range(charsize):
        find_combinations(keypad,inpt,keypad[digit][i]+res,index-1)


#find_combinations(keypad,inpt,"",n-1)

def find_combinations_iterative(keypad,inpt,n):
    res_list = []
    for c in keypad[inpt[0]]:
        res_list.append(c)
    for i in range(1,n):
        tmp = []
        for c in keypad[inpt[i]]:
            for ch in res_list:
                tmp.append(ch+c)
        res_list = tmp 
    return res_list

print find_combinations_iterative(keypad,inpt,n)

