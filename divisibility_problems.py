'''
Count pairs in array whose sum is divisible by K
https://www.hackerrank.com/challenges/divisible-sum-pairs/forum to understand logic
'''

a = [3,4,9,27]
k = 6

mods = [0]*k 

for i in a:
    mods[i%k] += 1 

count = 0 

count += (mods[0]*(mods[0]-1))/2

for i in range(1,k/2+1):
    if i != k-i:
        count += mods[i]*mods[k-i]

if k%2 == 0:
    count += (mods[k/2]*(mods[k/2]-1))/2 

print count 
        