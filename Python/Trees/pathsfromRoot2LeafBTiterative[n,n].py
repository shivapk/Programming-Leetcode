#Given a binary tree, get all root-to-leaf paths
#Time=O(n) #simple level order tree traversal
#space=O(n) #queue size can increse maximum at the leaf level =O(n)
#iterative BFS solution
from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Solution:
    def getallpaths(self,root):
        if root is None:
            return []
        paths=[]
        q=deque()
        q.append((root,'')) #insert tuple with node and current path
        while q:
            node,curr=q.popleft()    #current node and current path
            if node.left==None and node.right==None:
                paths.append(curr+str(node.val))
                
            if node.left:
                q.append((node.left,curr+str(node.val)+'->'))
                         
            if node.right:
                q.append((node.right,curr+str(node.val)+'->'))
                         
        return paths
    
root=Node(5)
root.left=Node(6)
root.right=Node(8)
root.left.left=Node(4)
root.left.right=Node(1)
root.right.left=Node(2)
root.right.right=Node(3)
s=Solution()
print (s.getallpaths(root))
