#Time Complexity of the above solution is O(n) as it does at most three traversals of binary tree.
'''
Given two nodes in a binary tree, check if they are cousins.
Two nodes are cousins if: 
1: they are not siblings (children of same parent).
2: they are on the same level.

'''

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


def iscousin(root,node1,node2):
    if node1 and node2:
        if level(root,node1,0)==level(root,node2,0) and issibling(root,node1,node2)==False:
            return True   
    return False
    
    
def issibling(root,node1,node2):
    if root is None:
        return False
    if (root.left==node1 and root.right==node2) or (root.left==node2 and root.right==node1):
        return True
    return (issibling(root.left,node1,node2) or issibling(root.right,node1,node2))
    
    
def level(root,node,h):
    if root is None:
        return 0
    if root == node:
        return h
    l=level(root.left,node,h+1)
    if l:
        return l
        
    return level(root.right,node,h+1)

    
    


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(15)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
 
node1 = root.left.right
node2 = root.right.right 

print (iscousin(root,node1,node2))

    
