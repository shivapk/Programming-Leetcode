'''
#recursive
Validate BST:
BST is defined as follows:conditions for a tree to be BST:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Generally we do a In-Order Traversal of the given tree and store the result in a temp array.
Check if the temp array is sorted in ascending order, if it is, then the tree is BST.

But Optimization:

We can avoid the use of Array. While doing In-Order traversal, we keep track of previously visited node. If the value of the currently visited node is less than the previous value, then tree is not BST. 

Time:O(n)#normal inorder traversal.everynode visited once so O(n)
Space:O(h) because of stack, where h is the height

'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def validateBST(self,root):
        return self.checkBST(root,None,None)
    
    def checkBST(self,root,min,max):
        if root is None:
            return True #empty tree is a BST
        #Traverse tree in inorder style and keep track of previous node
        if(min != None and root.val <= min):
            return False
        if(max != None and root.val >= max):
            return False

        return self.checkBST(root.left, min, root.val) and self.checkBST(root.right, root.val, max) #both left and right subtree has to be BST
      
            
        
root =  Node(10)
root.left = Node(6)
root.left.right=Node(8)
root.right = Node(14)
root.left.left = Node(4)
root.right.right = Node(16)
root.right.left = Node(12)
s=Solution()
print (s.validateBST(root))

