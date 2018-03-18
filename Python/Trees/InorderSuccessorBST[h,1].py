# In Binary Search Tree, Inorder Successor of an input node is the node with the smallest key greater than the key of input node.Inorder Successor is NULL for the last node in Inoorder traversal.
#Time: O(h) where h is height of tree.
#space: O(1)
from collections import defaultdict
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def inorder_succ(self, root,target):
        ans=None
        while root!=None:
            if target.val<root.val:
                ans=root
                root=root.left
            else:
                root=root.right
        return ans.val if ans else None
    def inorder_pred(self,root,target):
        ans=None
        while root!=None:
            if target.val>root.val:
                ans=root
                root=root.right
            else:
                root=root.left
        return ans.val if ans else None
    
root =  Node(10)
root.left = Node(6)
root.left.right=Node(8)
root.right = Node(14)
root.left.left = Node(4)
root.right.right = Node(16)
root.right.left = Node(12)
target = root.left
s=Solution()
print (s.inorder_pred(root,target))
