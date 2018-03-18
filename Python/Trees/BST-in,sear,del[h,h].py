'''
The worst case time complexity of search and insert operations is O(h) where h is height of Binary Search Tree. In worst case, we may have to travel from root to the deepest leaf node. The height of a skewed tree may become n and the time complexity of search and insert operation may become O(n).

Time= O(h)
Space=O(h)

'''
class Node():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def insert(root,value):
    if root is None:
        root=Node(value)
        return root
    elif root.val>value:
            root.left=insert(root.left,value)

    elif root.val<value:
            root.right=insert(root.right,value)
        
    return root

def search(root,value):
    if root is None:
        return False
    if root.val==value:
        return True
    
    elif root.val<value:
        search(root.left,value)
    else:
        search(root.right,value)
        
    return False
        
def delete(root, value):
 
    # Base Case
    if root is None:
        return root 
 
    # If the value to be deleted is smaller than root's value
    # then it lies in left subtree
    if value < root.val:
        root.left = delete(root.left, value)
 
    # If the value to be delete is greater than the root's value
    # then it lies in right subtree
    elif value > root.val:
        root.right = delete(root.right, value)
 
    # If value is same as root's value, then this is the node
    # to be deleted
    else:   
        # Node with only one child or no child
        if root.left is None :
            temp = root.right 
            root = None
            return temp 
             
        elif root.right is None :
            temp = root.left 
            root = None
            return temp
 
        # If root has two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = inorderSucc(root.right)
 
        # Copy the inorder successor's content to this node
        root.val = temp.val
 
        # Delete the inorder successor which is in the right subtree
        root.right = delete(root.right , temp.val)
 
    return root 
 
# to check whether insert, delete operations are correct            
def inorder(root):
    if root is None:
        return root
    inorder(root.left)
    print (root.val,end=' ')
    inorder(root.right)
    
def inorderSucc(current):
    while current.left:
        current=current.left
    return current
    
r=Node(4)
r=insert(r,2)
r=insert(r,3)
r=insert(r,40)
r=insert(r,54)
r=insert(r,15)
r=insert(r,20)
r=delete(r,15)
#print (search(r,4))
inorder(r)

                    
        
