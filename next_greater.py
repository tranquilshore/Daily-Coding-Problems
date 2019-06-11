nums = [98,23,54,12,20,7,27]

d = {}
stack = []
ans = []

for x in nums:
    while len(stack) and x > stack[-1]:
        d[stack.pop()] = x
    stack.append(x)

for x in nums:
    ans.append(d.get(x,-1))

print ans
