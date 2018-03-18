'''Time complexity : O(n). The whole tree is traversed once only. Here, n refers to the total number of nodes in the given binary tree.

Space complexity : O(h). res and avg array of size h are used. Here, h refers to the height(maximum number of levels) of the given binary tree. Further, the depth of the recursive tree could go upto h only.

logic-Let's visit every node of the tree once, keeping track of what depth we are on. We can do this with a simple DFS.

When we visit a node, avg[depth] will be a two element list, keeping track of the sum of the nodes we have seen at this depth, and the number of nodes we have seen at this depth. This is sufficient to be able to compute the average value at this depth.

At the end of our traversal, we can simply read off the answer.
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def avgoflevelsBT(self,root):
        avg=[]
        self.traversal(root,avg,0)
        i=0
        for s,count in avg:
            avg[i]=s/count
            i+=1
        return avg
    def traversal(self,root,avg,d):#DFS
        if root is None:
            return root
        if len(avg) <= d:
                avg.append([0, 0])
        avg[d][0] += root.val
        avg[d][1] += 1
        self.traversal(root.left,avg,d+1)
        self.traversal(root.right,avg,d+1)
                
root =  Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)
s=Solution()
print (s.avgoflevelsBT(root))

