'''
Problem: Given a list of pairs of equivalent words synonyms and a sentence text, Return all possible synonymous sentences sorted lexicographically.
Example 1:

Input:
synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
text = "I am happy today but was sad yesterday"
Output:
["I am cheerful today but was sad yesterday",
​​​​​​​"I am cheerful today but was sorrow yesterday",
"I am happy today but was sad yesterday",
"I am happy today but was sorrow yesterday",
"I am joy today but was sad yesterday",
"I am joy today but was sorrow yesterday"]

Recursive/DFS/Backtrack approach: This problem is similar to letter_case_permutation problem. Except that if we find a synonym then we need to recurse one more time
if a word replaced with synonym has another synonym. The given synonym input leads to an edge like input of a graph. Here we didn't keep visited information, so it
will create duplicates for which we have chosen set to be the final result for no duplicates. As final answer needs to be sorted lexicographically, so we sorted result.
The recursion tree would look like:

                                                                                                            0, 1,  2  ,  3  , 4 , 5 , 6 ,    7
                                                                                                           [I,am,happy,today,but,was,sad,yesterday]
                                                                                                        /(skipped nodes without synonyms)
                                                                                   i
                                                                            0, 1,  2  ,  3  , 4 , 5 , 6 ,    7
                                                                           [I,am,happy,today,but,was,sad,yesterday] 
                                                                            curr = [I,am]
                                                                        /                                                           \
                                                            i                                                                            i
                                               0, 1,  2  ,  3  , 4 , 5 , 6 ,    7                                           0, 1,  2  ,  3  , 4 , 5 , 6 ,    7
                                              [I,am,happy,today,but,was,sad,yesterday]                                     [I,am,happy,today,but,was,sad,yesterday]
                                                curr = [I,am,happy]                                                         curr=[I,am,joy]
                                                      /(skipped nodes without synonyms)                                     *(as joy also has a synonym, it will create 
                                                               i                                                             another branch to replace joy as well when
                                     0, 1,  2  ,  3  , 4 , 5 , 6 ,    7                                                      it will come back to this call stack)
                                    [I,am,happy,today,but,was,sad,yesterday]                                                                    /                           \
                                    curr=[I,am,happy,today,but,was]                                                                     ..........                    .............
                                /(skipped to answer)                    \
                                                    i                   
                0, 1,  2  ,  3  , 4 , 5 , 6 ,    7                      0, 1,  2  ,  3  , 4 , 5 , 6 ,    7
               [I,am,happy,today,but,was,sad,yesterday]                [I,am,happy,today,but,was,sad,yesterday]
               curr=[I,am,happy,today,but,was,sad,yesterday]            curr=[I,am,happy,today,but,was,sorrow,yesterday]
               ans = [[I,am,happy,today,but,was,sad,yesterday]]         ans=[[I,am,happy,today,but,was,sad,yesterday],
                                                                            [I,am,happy,today,but,was,sorrow,yesterday]]
'''


text = "I am happy today but was sad yesterday"
synonyms = [["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]]


def synonyms_sentences(text, synonyms):
    # getting the list of words from given text
    text_list = text.split(" ")

    # converting synonyms to dictionary - key value pairs
    synonyms_dic = {}
    for synonym in synonyms:
        synonyms_dic[synonym[0]] = synonym[1]
        synonyms_dic[synonym[1]] = synonym[0]

    res = set()
    curr = []

    def backtrack(text_list, curr, i):
        if i == len(text_list):
            res.add(" ".join(curr))
            return
        if text_list[i] in synonyms_dic:
            backtrack(text_list, curr + [text_list[i]], i+1)
            backtrack(text_list, curr + [synonyms_dic[text_list[i]]], i+1)
            if synonyms_dic[text_list[i]] in synonyms_dic:
                backtrack(text_list, curr +
                          [synonyms_dic[synonyms_dic[text_list[i]]]], i+1)
        else:
            backtrack(text_list, curr + [text_list[i]], i+1)

    backtrack(text_list, curr, 0)
    return sorted(res)


print synonyms_sentences(text, synonyms)
