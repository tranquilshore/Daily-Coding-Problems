'''
Problem: Given a string s in a sorted order, find the combinations of substrings of given length n (n<=len(s)) in a lexicographical order.
Example:
Input: s = "abc", n = 2
Output: ["ab","ac","bc"]

Approach:
As we need to find all such combinations, can use recursion/dfs where we have two choices to make which is either consider the current character to be part
of combination or don't and handle the base case and edge case respectively.
                                                     
                                                    start  012
                                                      s   "abc"
                                                    size    3

                                                (start,path,size)
                                                    (0,"",0)
                                            /                           \
(line no. as indicated on code)   3                                     4
                               (1,a,1)                                (1,"",0)
                        /             \                               /
                    3                 4                              3
                (2,ab,2)           (2,a,1)                        (2,b,1)
                res=[ab]                                        
                                /       \                      /           \
                            3           4                     3             4
                        (3,ac,2)        (3,a,1)            (3,bc,2)         (3,b,1)
                    res=[ab,ac]         return         res=[ab,ac,bc]       return
'''


s = "abc"
req_size = 2
string_len = len(s)


def combination(s, req_size, string_len):
    res = []

    def dfs(start, path, size):
        # 1 base case when we found the required size
        if size == req_size:
            res.append(path)
            return
        # 2 edge case when we reach the end of the string
        if start == string_len:
            return
        # 3 consider the character to be part
        dfs(start+1, path+s[start], size+1)
        # 4 do not consider the character
        dfs(start+1, path, size)

    dfs(0, "", 0)
    return res


print combination(s, req_size, string_len)
