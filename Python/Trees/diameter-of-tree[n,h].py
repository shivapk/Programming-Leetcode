#Time=O(n) travesing every node once.
#space=O(h)
#diameter of a tree is given by ans[0]
'''
The diameter of a tree T is the largest of the following quantities:
* the diameter of T’s left subtree
* the diameter of T’s right subtree
* the longest path between leaves that goes through the root of T (this can be computed from the heights of the subtrees of T)
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def traversal(root,ans):#calculating height and update ans if found longest
    if root is None:
        return 0
    left=traversal(root.left,ans)
    right=traversal(root.right,ans)
    ans[0]=max(ans[0],left+right) #ans[0] is the diameter
    return 1+max(left,right)   #height
        
root=Node(5)
root.left=Node(6)
root.right=Node(8)
root.left.left=Node(4)
root.left.right=Node(1)
root.right.left=Node(2)
root.right.right=Node(3)
ans=[0]#intial diameter be 0
traversal(root,ans)
print (ans[0])
