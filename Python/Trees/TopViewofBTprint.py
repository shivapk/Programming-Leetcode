from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

dmap=defaultdict(list)
def topview(root,hdict):
    if root is None:
        return
    dmap[hdict].append(root.data)
    topview(root.left,hdict-1)
    topview(root.right,hdict+1)
    
           
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
topview(root,0)
for k in sorted(dmap.keys()):
    for i in dmap[k]:
        print (i,end=' ')
    print ('')
