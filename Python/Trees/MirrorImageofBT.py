#Time=O(n)
#any tree traversal is O(n) since T(n)=T(k)+T(n-k-1)+c, analyse for Skewed tree and equal number of nodes on left and half
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    

def mirror(root):
    if root is None:
        return root
    tempr=mirror(root.right)
    templ=mirror(root.left)
    root.left=tempr
    root.right=templ
    return root
    
        
def inorder(root,ans):
    if root:
        inorder(root.left,ans)
        ans.append(root.data)
        inorder(root.right,ans)
    return ans
        
        

root = Node(1)

root.left = Node(2)

root.right = Node(3)
root.left.left=Node(4)
root.right.left=Node(5)


print (inorder(root,[]))
mirror(root)
print (inorder(root,[]))
