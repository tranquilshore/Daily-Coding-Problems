a = [4,1,3,5,6]
a = [5,3,7,1,2,9]

def next_greater(a):
    stack = []
    stack.append(a[0])
    res = {}
    i = 1
    while i < len(a):
        while i<len(a) and a[i]<=stack[-1]:
            stack.append(a[i])
            i += 1
        while len(stack)>0 and a[i] >stack[-1]:
            res[stack.pop()] = a[i]
        stack.append(a[i])
        i += 1
    return res,stack 

print next_greater(a)
