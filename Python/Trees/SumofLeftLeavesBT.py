#T= O(n) where n is the number of nodes
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

def sum(root):
    ans=0
    if root:
        if child(root.left):
            ans+=root.left.data
        ans+=sum(root.left)
        ans+=sum(root.right)
        
    return ans
    
root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.right.left = Node(23)        
root.right.right = Node(52)
root.right.right.left = Node(50)
root.left.left = Node(5)
root.left.right = Node(12)
root.left.right.right = Node(12)

print (sum(root))
