#only for BST as inorder traversal gives sorted ascennding order 
#Time=O(n) - The entire tree is traversed only once in the worst case. Here, n refers to the number of nodes in the given tree.
#Space=O(logn)- each list sizes(inorder,revinorder) can grow till O(log n)

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def Bstreqsum(self,root,k):
        v1=v2=0
        inorder=[]
        revinorder=[]
        temp1=root
        temp2=root
    #flag1, val1 and curr1 are used for normal inorder traversal using inorder
    #flag2, val2 and curr2 are used for reverse inorder traversal using revinorder
        flag1=flag2=False
        while True:
            
            while flag1==False:#Find next node in normal Inorder traversal.
                if temp1!=None:
                    inorder.append(temp1)
                    temp1=temp1.left
                else:
                    if len(inorder)==0:
                        flag1=True
                    else:
                        temp1=inorder.pop()
                        v1=temp1.val
                        temp1=temp1.right
                        flag1=True
        #Find next node in REVERSE Inorder traversal. The only difference between above and below loop is, in below loop right subtree is traversed before left subtree
            while flag2==False:
                if temp2!=None:
                    revinorder.append(temp2)
                    temp2=temp2.right
                else:
                    if len(revinorder)==0:
                        flag2=True
                    else:
                        temp2=revinorder.pop()
                        v2=temp2.val
                        temp2=temp2.left
                        flag2=True
                        
        #If we find a pair, then print the pair and return. The first condition makes sure that two same values are not added
                            
            if v1!=v2 and v1+v2==k:
                return True
     # If sum of current values is smaller, then move to next node in normal inorder traversal
            elif v1+v2 < k:
                flag1 = False
        #If sum of current values is greater, then move to next node in reverse inorder traversal
            elif v1+v2>k:
                flag2 = False
        #If any of the inorder traversals is over, then there is no pair so return false
            if v1>=v2:
                return False    
root =  Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)
s=Solution()
print (s.Bstreqsum(root,45))
