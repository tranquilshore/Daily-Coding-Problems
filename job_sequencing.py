'''
watch https://www.youtube.com/watch?v=zPtI8q9gvX8 to understand the problem and solution

Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline. It is also given that every job takes single unit of time, so the minimum possible deadline for any job is 1. How to maximize total profit if only one job can be scheduled at a time.
'''

a = [['a', 2, 100],
    ['b', 1, 19], 
    ['c', 2, 27], 
    ['d', 1, 25], 
    ['e', 3, 15]]

def job_sequencing(a,t):
    n = len(a)

    a = sorted(a,key=lambda item:item[2],reverse=True)

    result = [False]*t
    job = [0]*t

    for i in range(n):
        for j in range(min(t-1, a[i][1]-1),-1,-1):
            if result[j] is False:
                result[j] = True 
                job[j] = a[i][0]
                break 

    return job  

print job_sequencing(a,3)

#time complexity is O(n^2) can be optimized using disjoint sets


