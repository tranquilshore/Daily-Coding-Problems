'''
Given a 2D grid of characters and a word, find all occurrences of given word in grid. A word can be matched in all 8 directions at any point. Word is said be found in a direction if all characters match in this direction (not in zig-zag form).

mat[ROW][COL]= { {'B', 'N', 'E', 'Y', 'S'},
     	         {'H', 'E', 'D', 'E', 'S'},
	             {'S', 'G', 'N', 'D', 'E'}};
Word = "DES"
Output:
D(1, 2) E(1, 1) S(2, 0) 
D(1, 2) E(1, 3) S(0, 4) 
D(1, 2) E(1, 3) S(1, 4)
D(2, 3) E(1, 3) S(0, 4)
D(2, 3) E(1, 3) S(1, 4)
D(2, 3) E(2, 4) S(1, 4)

Idea:
The problem can be easily solved by applying DFS() on each occurrence of first character of the word in the matrix.
unlike standard DFS(), where we recursively call for all adjacent vertices, here we can recursive call for 8 neighbours only.
'''

def is_valid(i,j,visited):
    return i>=0 and i<r and j>=0 and j<c and not visited[i][j]

def dfs(grid,i,j,visited,word,path,index,n):
    #return if current character doesn't match with next character in word or we exceed the word len limit
    if index>=n or grid[i][j] != word[index]:
        return 
    
    visited[i][j] = True 
    #append current character and position to path
    path += word[index]+"("+str(i)+","+str(j)+")"

    #if current character matches last character of word
    if index==n-1:
        print path 
        return 
    
    #recurse for all connected neighbours
    for k in range(8):
        if is_valid(i+row[k],j+col[k],visited):
            dfs(grid,i+row[k],j+col[k],visited,word,path,index+1,n)
    visited[i][j] = False 

def find_words(grid,word,n):
    for i in range(r):
        for j in range(c):
            if grid[i][j] == word[0]:
                #check and print path if exists
                dfs(grid,i,j,visited,word,"",0,n) #(grid,i,j,previousRow,previousCol,word,stringPath,indexOfCharInWord,lenOfWord)

grid = [
    ['G','I','Z'],
    ['U','E','K'],
    ['Q','S','E']
]; 

r = len(grid)
c = len(grid[0])

row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]

visited = [[0 for i in range(c)] for i in range(r)]

word = "GEEKS"
n = len(word)

find_words(grid,word,n)










