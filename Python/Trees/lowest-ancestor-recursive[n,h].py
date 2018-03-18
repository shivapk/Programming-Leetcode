#Time complexity is O(n) i'm doing just a simple tree traversal in bottom up fashion.
#space complexity=O(h) where is height of the tree

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def lca(self, root, x, y):
        flag=[False,False]#if only x or y exists case
        ans=self.lcamain(root,x,y,flag)
        if flag[0] and flag[1]:
            return ans.val
        elif flag[0] and self.searchforother(root,y):
            return ans.val
        elif flag[1] and self.searchforother(root,x):
            return ans.val
        return None
        
    def lcamain(self,root,x,y,flag):  #x,y are assumed values if they are Node type then also no problem
        if root is None:
            return root
        if root.val==x:
            flag[0]=True
            return root
        if root.val==y:
            flag[1]=True
            return root
        left=self.lcamain(root.left,x,y,flag)  #goes down till it find..if both are present down then searchfortoher
        right=self.lcamain(root.right,x,y,flag)
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        
    def searchforother(self,root,v): #needed because 5,6 are input then 6 is not checked above
        if root is None:
            return False
        if root.val==v or self.searchforother(root.left,v) or self.searchforother(root.right,v):
            return True
        return False
            
root=Node(3)
root.left=Node(5)
root.left.left=Node(6)
root.left.right=Node(2)
root.left.right.left=Node(7)
root.left.right.right=Node(4)
root.right=Node(1)
root.right.left=Node(0)
root.right.right=Node(8)
s=Solution()
print (s.lca(root,6,5))

