'''
#Recursive solution
level order traversal
Time=O(n) #simple tree traversal
Space=O(h) #stack where h is the height
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def levelorder(self,root):
        if root == None:
            return root
        return self.traversal(root, 0,[])
        #return ret
        
    def traversal(self,root,depth,ans):
        if root is None:
            return root
        if(len(ans) == depth):  #end of level so append []
            ans.append([])
            
        ans[depth].append(root.val)
        
        self.traversal(root.left, depth+1,ans)
        self.traversal(root.right, depth+1,ans)
        return ans
    
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
root.left.left.left=Node(8)
root.left.left.right=Node(9)
root.right.right.left=Node(10)
root.right.right.right=Node(11)
s=Solution()
print (s.levelorder(root))
