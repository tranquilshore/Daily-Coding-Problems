'''
Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).
'''
s = ")("
def count_invalid_parentheses(s):
    opened = 0
    invalid = 0

    for c in s:
        if c == "(":
            opened += 1
        elif c == ")":
            if invalid > 0:
                opened -= 1
            else:
                invalid += 1
    invalid += opened
    return invalid

print count_invalid_parentheses(s)
