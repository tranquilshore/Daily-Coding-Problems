'''
https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/

one solution is to use a custom comparator in sorting.
ie. 
Given two numbers X and Y, how should myCompare() decide which number to put first we compare two numbers XY (Y appended at the end of X) and YX (X appended at the end of Y). If XY is larger, then X should come before Y in output, else Y should come before. For example, let X and Y be 542 and 60. To compare X and Y, we compare 54260 and 60542. Since 60542 is greater than 54260, we put Y first.
'''
a = [54, 546, 548, 60]

def comparator(a,b):
    ab = str(a)+str(b)
    ba = str(b)+str(a)
    return cmp(int(ba),int(ab))

result = sorted(a,cmp=comparator)
print result

'''
https://www.geeksforgeeks.org/arrange-given-numbers-form-biggest-number-set-2/
It follows an algorithm
1. Find number of digits in the largest number. Let number of digits be n.
    like n = 3 in above example 546
2. Create extended version of all numbers. In extended version, we have n+1 digits formed by concatenating the number of with itself and truncating extra digits.
    extended version 546546... consider only till n+1 ie. 5465
3. Sort original numbers according to their extended values. Concatenate array to get answer
'''
def largestNumber(a): 
    extval, ans = [], "" 
    l = len(str(max(a))) + 1
      
    for i in a: 
        temp = str(i)*l 
        extval.append((temp[:l:],i))

    extval.sort(reverse = True)
    for i in extval: 
        ans += str(i[1])
          
    return ans 

print largestNumber(a)