#Time=O(n) - The entire tree is traversed only once in the worst case. Here, n refers to the number of nodes in the given tree.
#Space=O(n)- The size of the set can grow upto n in the worst case.

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def Bstreqsum(self,root,k):
        h=set()
        return self.traversal(root,h,k)
        
    def traversal(self,root,h,k):
        if root is None:
            return False
        elif k-root.val in h:
            return True
        h.add(root.val)
        if self.traversal(root.left,h,k):
            return True
        if self.traversal(root.right,h,k):
            return True
        return False
    
root =  Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)
s=Solution()
print (s.Bstreqsum(root,25))
