#Time complexity is O(n)
from collections import defaultdict
hdist=defaultdict(list)
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.hright=None


def connect(root):
    if root is None:
        return 
    queue=[]
    queue.append((root,0))
    while queue:
        temp=queue.pop(0)
        if queue and temp[1]==queue[0][1]:
            temp[0].hright=queue[0][0]
        if temp[0].left:
            queue.append((temp[0].left,temp[1]+1))
        if temp[0].right:
            queue.append((temp[0].right,temp[1]+1))
    return root
        

root = Node(1);
root.left =Node(2);
root.right = Node(3);
root.left.left = Node(4);
root.left.right = Node(5);
root.right.left = Node(6);
root.right.right = Node(7);
root.right.left.left = Node(8);
root.right.left.left.left = Node(9);


#print (inorder(root,[]))
root=connect(root)
print (root.data,'->', root.hright.data if root.hright!=None else root.hright)
print (root.left.data,'->', root.left.hright.data if root.left.hright else None)
print (root.right.data,'->', root.right.hright.data if root.right.hright else None)
print (root.left.left.data,'->', root.left.left.hright.data if root.left.left.hright else None)
print (root.left.right.data,'->', root.left.right.hright.data if root.left.right.hright else None)
print (root.right.left.data,'->', root.right.left.hright.data if root.right.left.hright else None)
print (root.right.right.data,'->', root.right.right.hright.data if root.right.right.hright else None)
print (root.right.left.left.data,'->', root.right.left.left.hright.data if root.right.left.left.hright else None)
print (root.right.left.left.left.data,'->', root.right.left.left.left.hright.data if root.right.left.left.left.hright else None)

    
