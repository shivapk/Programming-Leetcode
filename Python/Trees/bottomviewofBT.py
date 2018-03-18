from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

dmap=defaultdict(list)
def bottomview(root,hdict,level):
    if root is None:
        return
    
    if dmap[hdict]:
        if dmap[hdict][1]<=level:
            dmap[hdict][0]=root.data
            dmap[hdict][1]=level
    else:
        dmap[hdict]=[root.data,level]
    bottomview(root.left,hdict-1,level+1)
    bottomview(root.right,hdict+1,level+1)
    
           
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

bottomview(root,0,0)
for k in sorted(dmap.keys()):
        print (dmap[k][0], end=' ')
