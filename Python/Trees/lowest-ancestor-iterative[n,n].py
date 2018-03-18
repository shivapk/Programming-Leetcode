#Time complexity is O(n) i'm doin just a simple tree traversal in level order
#space complexity=O(n) for storing parent, O(h) for ancestors
#After we found both x and y, we create a set of x's ancestors. Then we travel through y's ancestors, the first one appears in x's is our answer.

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def lca(self, root, x, y):
        que=[]#level order traversal
        prt={}#parent
        que.append(root)
        prt[root]=None
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
        ancestors=[]
        if x in prt and y in prt:
            while x:
                ancestors.append(x)
                x=prt[x]
            while y not in ancestors:
                y=prt[y]
            return y.val 
        else:
            return None
                   
root=Node(3)
root.left=Node(5)
x=root.left.left=Node(6)
root.left.right=Node(2)
root.left.right.left=Node(7)
y=root.left.right.right=Node(4)
root.right=Node(1)
root.right.left=Node(0)
root.right.right=Node(8)
s=Solution()

print (s.lca(root,x,y))

