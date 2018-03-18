class Node(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
 
tvl=[]
def inorder(node):
    if node:
        tvl.append(node.val)
        print (inorder(node.left))
        print (inorder(node.right))

    return tvl
        
root=Node(10)
root.left=Node(8)
root.right=Node(13)
root.left.left=Node(4)
root.left.right=Node(9)
print(inorder(root))