import sys 
class Node:
    def __init__(self,value):
        self.data = value 
        self.left = None 
        self.right = None 

root = Node(4)
root.left = Node(2)
root.right = Node(-5)
root.left.left = Node(-1)
root.left.right = Node(3)
root.right.left = Node(-2)
root.right.right = Node(6)


def minimum_sum_level(root):
    if root is None: return 
    level = 0
    q = []
    q.append(root)
    minimum_sum = sys.maxint
    minimum_sum_lvl = 0
    while q:
        nodescount = len(q)
        level_sum = 0
        while nodescount > 0:
            node = q.pop(0)
            #print node.data,
            level_sum += node.data

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            nodescount -= 1
        #print "level: ",level 
        print "level: ",level, "level sum: ", level_sum

        if level_sum < minimum_sum:
            minimum_sum_lvl = level 
            minimum_sum = level_sum
        level += 1
        #print 
    return minimum_sum_lvl

print minimum_sum_level(root)