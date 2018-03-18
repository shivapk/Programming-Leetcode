'''
iterative solution(Not BFS) assumption: it is a complete binary tree all nodes in last level are as left as possible
Since we are manipulating tree nodes on the same level, it's easy to come up with
a very standard BFS solution using queue. But because of next pointer, we actually
don't need a queue to store the order of tree nodes at each level, we just use a next
pointer like it's a link list at each level
Time=O(n) #simple tree traversal
Space=O(1) #this is our goal so restricted ourselfs to complete binary tree else use Level order traversal

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
        level_start=root
        while level_start:#to represent start of level
            curr=level_start
            while curr: #cur moves in the level
                if curr.left:
                   curr.left.next=curr.right
                if curr.right and curr.next:  # if more elements on the same level then right childs next is equal to its right nodes left child
                    curr.right.next=curr.next.left
                
                curr=curr.next
            
            level_start=level_start.left  #next level
            
    
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
''' This code works only for complete binary tree as our main motive is O(1) space
root.left.left.left=Node(8)
root.left.left.right=Node(9)
root.right.right.left=Node(10)
root.right.right.right=Node(11)
'''
s=Solution()
s.levelconnect(root)
print (root.left.left.next.val)
print (root.left.right.next.val)
print (root.right.left.next.val)
