#Time complexity is O(n) i'm doing just a simple tree traversal in level order
#space complexity=O(1) still O(n) because of queue
'''We can solve the problem in O(1) extra space using following fact : If both nodes are at same level and if we traverse up using parent pointers of both nodes, the first common node in the path to root is lca.
The idea is to find depths of given nodes and move up the deeper node pointer by the difference between depths. Once both nodes reach same level, traverse them up and return the first common node.
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def lca(self, root, x, y):
        que=[]#level order traversal
        prt={}#parent
        prt[root]=None
        que.append(root)
        while x not in prt or y not in prt: # (valid if x,y are Node type)
                temp=que.pop()
                if temp.left:
                    que.append(temp.left)
                    prt[temp.left]=temp
                if temp.right:
                    que.append(temp.right)
                    prt[temp.right]=temp
                    
                if len(que)==0: #end case
                    break

        if x in prt and y in prt:
            dx = self.depth(x,prt)
            dy = self.depth(y,prt)
            if dx<dy:#If y is deeper
                loop=dy-dx
                while loop!=0: #Move y up until it reaches the same level as x
                    y=prt[y]
                    loop-=1
                    
            elif dx>dy:
                loop=dx-dy
                while loop!=0: #Move y up until it reaches the same level as x
                    x=prt[x]
                    loop-=1
            #Now x and y are at same levels  
            while x!=None and y!=None:
                if x==y:
                    return x.val
                x=prt[x]
                y=prt[y]    
        else:
            return None
        
        
        
    def depth(self,root,prt):
        d=-1
        while (root!=None):
            root=prt[root]
            d+=1
        return d
        
root=Node(3)
root.left=Node(5)
root.left.left=Node(6)
root.left.right=Node(2)
x=root.left.right.left=Node(7)
root.left.right.right=Node(4)
root.right=Node(1)
root.right.left=Node(0)
y=root.right.right=Node(8)
s=Solution()
print (s.lca(root,x,y))
