'''
Given n appointments, find all conflicting appointments.

use Interval Tree to solve this problem in O(nLogn) time

1) Create an Interval Tree, initially with the first appointment.
2) Do following for all other appointments starting from the second one.
   a) Check if the current appointment conflicts with any of the existing 
     appointments in Interval Tree.  If conflicts, then print the current
     appointment.  This step can be done O(Logn) time.
   b) Insert the current appointment in Interval Tree. This step also can
      be done O(Logn) time.

Every node of Interval Tree stores following information.
a) i: An interval which is represented as a pair [low, high]
b) max: Maximum high value in subtree rooted with this node.

The low value of an interval is used as key to maintain order in BST. The insert and delete operations are same as insert and delete in self-balancing BST used.
'''


class Node:
    def __init__(self,low,high):
        self.low = low
        self.high = high 
        self.max_ = high
        self.left = None 
        self.right = None


def insert(root,low,high):
    if root is None:
        return Node(low,high)
    
    #if root's low value is smaller,then new interval goes to left subtree
    if low < root.low:
        root.left = insert(root.left,low,high)
    else:
        root.right = insert(root.right,low,high)
    
    root.max_ = max(root.max_,high)
    return root 

def inorder(root):
    if root is not None:
        inorder(root.left)
        print "<",root.low,",",root.high,">",
        inorder(root.right)

def overlap_search(root,low,high):
    if root is None:
        return None 
    
    if root.low <= high and low <= root.high:
        return root.low,root.high 
    
    #if root's max is greater than given interval's low, then it can present in left subtree else right
    if root.left is not None and root.left.max_ >= low :
        return overlap_search(root.left,low,high)
    
    return overlap_search(root.right,low,high)

def conflicting_intervals(intervals):
    n = len(intervals)

    #create an empty interval tree and add first appointment
    root = None 
    root = insert(root,intervals[0][0],intervals[0][1])

    #process rest of the intervals
    for i in range(1,n):
        res = overlap_search(root,intervals[i][0],intervals[i][1])
        if res:
            print intervals[i][0],intervals[i][1]," conflicts with ", res[0],res[1]
        root = insert(root,intervals[i][0], intervals[i][1])


intervals = [(15, 20), (10, 30), (17, 19), (5, 20), (12, 15), (30, 40)]

# n = len(intervals) 
# root = None 
# for i in range(n):
#     root = insert(root,intervals[i][0], intervals[i][1])

#inorder(root)

#print overlap_search(root,11,18)
conflicting_intervals(intervals)


