#Time Complexity: O(n) where n is the number of nodes in given BST.
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def update(root,min,max):
    if root is None:
        return
    root.left=update(root.left,min,max)
    root.right=update(root.right,min,max)
    if root.data<min:
        return root.right
    elif root.data>max:
        return root.left
    return root
    
def inorder(root,arr):
    if root is None:
        return
    inorder(root.left,arr)
    arr.append(root.data)
    inorder (root.right,arr)
    
    return arr

        
           
root=Node(6)
root.left = Node(-13)
root.right = Node(14)
root.left.right = Node(-8)
root.right.left=Node(13)
root.right.left.left=Node(7)
root.right.right=Node(15)
print (inorder(root,[]))
nroot=update(root,-10,1)
print (inorder(nroot,[]))
