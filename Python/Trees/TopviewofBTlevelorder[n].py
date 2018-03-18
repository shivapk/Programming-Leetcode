from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def topview(root):
    hdist=0
    level=0
    if root is None:
        return
    queue=[]
    queue.append([root,hdist])
    dmap=defaultdict(int)
    while queue:
        current=queue.pop(0)
        if dmap[current[1]]==0:
            dmap[current[1]]=current[0].data
        if current[0].left:
            queue.append([current[0].left,current[1]-1])
        if current[0].right:
            queue.append([current[0].right,current[1]+1])
    return dmap
           
root=Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
dmap=topview(root)
for v in sorted(dmap.keys()):
    print (dmap[v], end=' ')

