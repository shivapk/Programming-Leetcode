class Node(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
 
tvl=[]
def lorder(node):
    q=[]
    q.append(node)
    while q:
        temp=q.pop(0)
        tvl.append(temp.val)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    return tvl
        
root=Node(10)
root.left=Node(8)
root.right=Node(13)
root.left.left=Node(4)
root.left.right=Node(9)
print(lorder(root))