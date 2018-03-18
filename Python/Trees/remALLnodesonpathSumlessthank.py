#Time complexity of the above solution is O(n) where n is number of nodes in given Binary Tree.
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def update(root,k):
    return update1(root,k,1)

def update1(root,k,l):
    if root is None:
        return 
    root.left=update1(root.left,k,l+1)   
    root.right=update1(root.right,k,l+1)
    if root.left is None and root.right is None and l<k:
        return None
    return root

    
    
def inorder(root,arr):
    if root is None:
        return
    inorder(root.left,arr)
    arr.append(root.data)
    inorder (root.right,arr)
    
    return arr

root=Node(1)        
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
root.right.right = Node(6)
root.right.right.left = Node(8)
print (inorder(root,[]))
nroot=update(root,4)
print (inorder(nroot,[]))


    
    
