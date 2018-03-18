class Node(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
 
tvl=[]
def lorderrv(node):
    q=[]
    q.append((node,0))
    seen=-1
    while q:
        temp=q.pop()
        if temp[1]>seen:
            tvl.append(temp[0].val)
            seen=temp[1]
        if temp[0].left:
            q.append((temp[0].left,temp[1]+1))
        if temp[0].right:
            q.append((temp[0].right,temp[1]+1))
    return tvl
        
root=Node(10)
root.left=Node(8)
root.right=Node(13)
root.left.left=Node(4)
root.left.right=Node(9)
root.right.left=Node(11)
print(lorderrv(root))