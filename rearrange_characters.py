from collections import Counter 

s = "aaaabc"

def reorganize(s):
    if len(s) == 1:
        return s

    #creates the frequency table
    cnt = Counter(s)
    res = ""
    while True:
        #when it's all zero in the frequency table
        if sum(cnt.values()) == 0:
            break

        top,second = cnt.most_common(2)#instead of most common use extract max of heap to get logn time complexity
        #when there is only one character left
        if top[1] == 1 and not second[1]:
            res += top[0]
            break 
        
        #when most frequent is the only one left with count more than 1 then its impossible to reorganize
        elif top[1]>1 and not second[1]:
            return ""
        else:
            res += top[0]
            res += second[0]
            cnt[top[0]] -= 1 
            cnt[second[0]] -= 1
    return res 

print reorganize(s)

'''
Now the time complexity is O(n^2) but if we use max heap to get top 2 most common
elements then it will be O(nlogn)
'''
        
        

        
    


print reorganize(s)
