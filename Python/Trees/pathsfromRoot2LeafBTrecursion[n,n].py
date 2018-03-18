#Given a binary tree, get all root-to-leaf paths
#Time=O(n) #simple tree traversal
#space=O(n) #paths array
#recursive traversal type solution
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
        curr=''
        self.traversal(root,curr,paths)#curr to store current processing path
        return paths
    
    def traversal(self,root,curr,paths): #curr to store current processing path
        #no need of root is None then return None
        if root.left==None and root.right==None:  #reached leaf of the tree so append the path
            paths.append(curr+str(root.val))
            #if you want to print, replace above with print (curr+str(root.val))
            
        if root.left:
            self.traversal(root.left,curr+str(root.val)+'->',paths)
            
        if root.right:
            self.traversal(root.right,curr+str(root.val)+'->',paths)
            
            
    
root=Node(5)
root.left=Node(6)
root.right=Node(8)
root.left.left=Node(4)
root.left.right=Node(1)
root.right.left=Node(2)
root.right.right=Node(3)
s=Solution()
print (s.getallpaths(root))
