'''
The worst case time complexity of search and insert operations is O(h) where h is height of Binary Search Tree. In worst case, we may have to travel from root to the deepest leaf node. The height of a skewed tree may become n and the time complexity of search and insert operation may become O(n).

Time= O(h)
Space=O(h)

'''

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
 
# A utility function to insert a new node with the given key
def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
                
def search(root,key):
     
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
 
    # Key is greater than root's key
    if root.val < key:
        return search(root.right,key)
   
    # Key is smaller than root's key
    return search(root.left,key)
 
# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
 
 
# Driver program to test the above functions
# Let us create the following BST
#      50
#    /    \
#   30     70
#   / \    / \
#  20 40  60 80
root = Node(50)
insert(root,Node(30))
insert(root,Node(20))
insert(root,Node(40))
insert(root,Node(70))
insert(root,Node(60))
insert(root,Node(80))
 
# Print inoder traversal of the BST
inorder(root)
print (search(root,10))
