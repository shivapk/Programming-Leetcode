'''
This is a typical tree traversal question. We start from root and 
check if the node has one child, if yes then print the only child of that node. 
If node has both children, then recur for both the children.

Time =O(n) # tree traversal
space=O(h)
'''

class Node(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
 
tvl=[]
a=0
def nosibling(node):
    if node:
    #If this is an internal node , recur for left
    # and right subtrees
       if node.left and node.right:
               nosibling(node.left)
               nosibling(node.right)    
       else:
    # If right child is NULL and left is not, print
    # left child and recur for left child
          if node.left:
               tvl.append(node.left.val)
               nosibling(node.left)
     # If left child is NULL, and right is not, print
    # right child and recur for right child
          elif node.right:
               tvl.append(node.right.val)
               nosibling(node.right)
            
          else:
               return None
             
    return tvl
        
root=Node(10)
root.left=Node(8)
root.right=Node(13)
root.right.left=Node(11)
root.left.left=Node(4)
root.left.right=Node(9)
root.left.left.right=Node(6)
print(nosibling(root))

