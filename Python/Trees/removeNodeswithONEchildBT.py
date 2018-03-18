#Time complexity of the above solution is O(n) as it does a simple traversal of binary tree.
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def update(root):
    if root is None:
        return None
    root.left=update(root.left)
    root.right=update(root.right)
    if root.left is None and root.right:
        return root.right
    elif root.left and root.right is None:
        return root.left
    return root
        
        

    
    
def inorder(root,arr):
    if root is None:
        return
    inorder(root.left,arr)
    arr.append(root.data)
    inorder (root.right,arr)
    
    return arr

root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)
 
print (inorder(root,[]))
nroot=update(root)
print (inorder(nroot,[]))

    
    
