'''Time complexity : O(n). The whole tree is traversed once only. Here, n refers to the total number of nodes in the given binary tree.

Space complexity : O(m). The size of queue can grow upto atmost the maximum number of nodes at any level in the given binary tree. Here, m refers to the maximum mumber of nodes at any level in the input tree. ans length is just the number of levels(h), here m=O(n) if tree is complete

logic-simple level order traversal i.e BFS.
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def avgoflevelsBT(self,root):
        q=[root]#queue
        ans=[]#to store avg of nodes at a level
        while q:
            nodes=len(q) #number of nodes at a particular level
            s=0 #sum
            for i in range(nodes):
                temp=q.pop(0)
                s+=temp.val
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            ans.append(s/nodes)
            
        return ans
        
root =  Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)
s=Solution()
print (s.avgoflevelsBT(root))

        
