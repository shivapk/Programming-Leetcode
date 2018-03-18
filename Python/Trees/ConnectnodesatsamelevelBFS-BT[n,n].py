'''

NT#If we do RECURSIVE version it WONT WORK for all trees..it just works for complete binary trees because of Preorder fashion
NT#When we are at node 4, we set the nextRight of its children which are 8 and 9 (the nextRight of 4 is already set as node 5). nextRight of 8 will simply be set as 9, but nextRight of 9 will be set as NULL which is incorrect.
NT#We can’t set the correct nextRight, because when we set nextRight of 9, we only have nextRight of node 4 and ancestors of node 4, we don’t have nextRight of nodes in right subtree of root. NEXTRIGHT MEANS NEXT
'''
'''
Level order traversal-No need of any assumptions like complete tree or not
we use with None markers which are needed to mark levels in tree.
Time=O(n) #simple tree traversal
Space=O(n) #queue
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.next=None
        
class Solution:
    def levelconnect(self,root):
        if root is None:
            return root
        q=[root]
        q.append(None)
        while q:
            curr=q.pop(0)
            if curr:
                curr.next=q[0] #next element in queue represents next node at current Level 
                
                #push left and right children of current
                if curr.left:
                    q.append(curr.left)     
                if curr.right:
                    q.append(curr.right)
                       
            elif len(q)!=0:#push None to mark nodes at this level are visited, this line not executed if curr is not null
                q.append(None)
                
    
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
s.levelconnect(root)
print (root.left.left.next.val)
print (root.left.right.next.val)
print (root.right.left.next.val)
print (root.right.right.next)
print (root.left.left.right.next.val)
