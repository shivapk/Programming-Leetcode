class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
def isleaf(node):
    if node:
        if node.left==None and node.right==None:
            return True
    return False

def count(root):
    if root is None:
        return 0
    
    return 1+count(root.left)+count(root.right)
    
def binary(node,i,count):
    if node is None:
        return True
    elif i>=count:
        return False
    #print (i,count)
    return (binary(node.left,2*i+1,count) and binary(node.right,2*i+2,count))
root = Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
#root.left.left.left=Node(6)
print (binary(root,0,count(root)))