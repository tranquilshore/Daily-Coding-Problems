'''
   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h
and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, the longest path would be c -> a -> d -> f, with a length of 17.

Solution:
The gist is similar to what i explained in the max path sum in binary tree video. Path with maximum sum will either go through two children passing through root
or just one children.
'''

class Node:
    def __init__(self,idf):
        self.idf = idf 
        self.max_path = 0
        self.children = []

#this will return the max path using the gist mentioned above from each node and children combination and return it. Final return will hold the answer.
def get_max_pathlen(root):
    if not root.children:
        return 0 
    
    path_lens = []
    child_max_pathlens = []

    for child,dist in root.children:
        path_lens.append(child.max_path + dist)
        child_max_pathlens.append(get_max_pathlen(child))
    
    child_max_pathlens = max(child_max_pathlens)
    
    return max(sum(sorted(path_lens)[-2:]), child_max_pathlens)

#this will find the math path at each node
def update_max_paths(root):
    if not root.children:
        root.max_path = 0 
        return 
    root_paths = []
    
    for child,dist in root.children:
        update_max_paths(child)
        root_paths.append(child.max_path + dist)
    
    root.max_path = max(root_paths)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.children = [(b,3),(c,5),(d,8)]
d.children = [(e,2),(f,4)]
e.children = [(g,1),(h,1)]

update_max_paths(a)
print get_max_pathlen(a)



