'''
level order traversal
Time=O(n) #simple tree traversal
Space=O(n) #queue
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
         
        q=[root]
        #ans=[]
        while q: 
            ln=len(q) #nodes at current level
            temp=[]
            while ln>0:  # for all nodes at current level insert their childs in to q     
                curr = q.pop(0)
                temp.append(curr.val)  #replace with print (curr.val,end=' ') to just print  
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                ln-=1
            
            print (temp)   #replce with print ('') to just print
            #ans.append(temp)
        #return ans use this if you want a list of lists
        
    
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
s.levelorder(root)

