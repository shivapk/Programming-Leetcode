#Complexity of the identicalTree() will be according to the tree with lesser number of nodes. Let number of nodes in two trees be m and n then complexity of sameTree() is O(m) where m < n
'''
Given two trees, find if they are identical. 
Two trees are said to be identical if they are structurally same and have same data in all nodes.
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    

def eqTrees(root1,root2):
    if root1 is None and root2 is None:
        return True
    
    if root1 is not None and root2 is not None:

        return root1.data==root2.data and eqTrees(root1.left,root2.left) and eqTrees(root1.right,root2.right)
        
    return False
        

root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
 
root2.left = Node(2)
root2.right = Node(3)

 
print (eqTrees(root1, root2))
