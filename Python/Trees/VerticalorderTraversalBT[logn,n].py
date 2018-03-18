#If we use level order traversal, we can make sure that if a node like 12 comes below in same vertical line, it is printed after a node like 9 which comes above in vertical line.
#Time: O(n*logn) #sorted operation is costlier rest is just tree traversal
#space: O(n) #size of queue can grow max in last level which is of O(n)
#I followed this approach beacuse using preorder traversal, nodes in a vertical line may not be prined in same order as they appear in tree.
from collections import defaultdict
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def verticalline(self,root):
        if root is None:
            return root
        level=defaultdict(list)
        q=[(root,0)]
        for n,i in q:  #n is node, i is vertical level 0 for root,-1 for left, +1 for right
            level[i].append(n.val)
            if n.left:
                q.append([n.left,i-1])
            if n.right:
                q.append([n.right,i+1])
        return [level[i] for i in sorted(level)]
                
                
root =  Node(15)
root.left = Node(10)
root.left.right=Node(12)
root.right = Node(20)
root.left.left = Node(8)
root.left.left.right=Node(6)
root.left.right = Node(12)
root.right.right = Node(25)


s=Solution()
print (s.verticalline(root))
