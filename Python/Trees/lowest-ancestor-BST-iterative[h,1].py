#Time =O(h) where h is the height
#space=O(1) space optimization compared to recursive

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def bstLca(self, root,x,y):
        while root:
            if root.val>x and root.val>y:
                root=root.left
            elif root.val<x and root.val<y:
                root=root.right
            else:
                return root
                
root=Node(10)
root.left=Node(5)
root.left.left=Node(4)
root.left.right=Node(7)
root.left.right.left=Node(6)
root.left.right.right=Node(9)
root.right=Node(14)
root.right.left=Node(12)
root.right.right=Node(16)
s=Solution()
print (s.bstLca(root,9,12))

