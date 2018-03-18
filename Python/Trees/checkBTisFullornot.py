#Time complexity of the above code is O(n) where n is number of nodes in given binary tree.
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
def child(node):
    if node:
        if node.left==None and node.right==None:
            return True
    return False

def binary(root):
    if root is None:
        return True

    elif root.left and root.right:
              return (binary(root.left) and binary(root.right))
    elif root.left or root.right:
        return False
    
    return True

root = Node(10);
root.left = Node(20);
root.right = Node(30);
 
root.left.right = Node(40);
root.left.left = Node(50);
root.right.left = Node(60);
root.right.right = Node(70);
 
root.left.left.left = Node(80);
root.left.left.right = Node(90);
root.left.right.left = Node(80);
root.left.right.right = Node(90);
root.right.left.left = Node(80);
root.right.left.right = Node(90);
root.right.right.left = Node(80);
root.right.right.right = Node(90);


print (binary(root))

    
    

    
