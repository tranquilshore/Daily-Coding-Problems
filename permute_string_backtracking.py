#https://courses.cs.washington.edu/courses/cse143/12su/lectures/07-16/12-recursive-backtracking.pdf

s = "tea"

def permute(s,res):
    if len(s) == 0:
        print res 
    else:
        for i in range(len(s)):
            res.append(s[i]) #choose
            permute(s[:i]+s[i+1:], res) #explore
            res.pop() #unchoose

permute(s,[])
