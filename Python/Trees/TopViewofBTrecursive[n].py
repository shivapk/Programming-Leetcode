#Time Complexity of the above implementation is O(n) where n is number of nodes in given binary tree. The assumption here is that add() and contains() methods of HashSet work in O(1) time.
from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

distance=defaultdict(int)
def topview(root,hdist,clevel):
    if root is None:
        return
    if distance[hdist]:
        if (distance[hdist][1]>clevel):
            distance[hdist]=[root.data,clevel]
    else:
        distance[hdist]=[root.data,clevel]
        
    topview(root.left,hdist-1,clevel+1)
    topview(root.right,hdist+1,clevel+1)
    
    
           
root=Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
topview(root,0,0)
for v in distance.values():
    print (v[0], end=' ')

