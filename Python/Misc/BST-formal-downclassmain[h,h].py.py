#https://gist.github.com/jakemmarsh/8273963
'''
The worst case time complexity of search and insert operations is O(h) where h is height of Binary Search Tree. 
In worst case, we may have to travel from root to the deepest leaf node. 
The height of a skewed tree may become n and the time complexity of search and insert operation may become O(n).

'''
class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def get(self):
        return self.data

    def set(self,data):
        self.data=data

    def getChildren(self):
        children=[]
        if self.left!=None:
            children.append(self.left.data)
        if self.right!=None:
            children.append(self.right.data)

        return children

    

class BST(object):
    def __init__(self):
        self.root=None

    def setRoot(self,value):
        self.root= Node(value)

    def insert(self,val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root,val)

    def insertNode(self,currentNode,val):
        if val<=currentNode.data:
            if currentNode.left:
                self.insertNode(currentNode.left,val)

            else:
                currentNode.left=Node(val)
                
        elif val>currentNode.data:
            if currentNode.right:
                self.insertNode(currentNode.right,val)

            else:
                currentNode.right=Node(val)
            

    def find(self,val):
        return self.findNode(self.root,val)

    def findNode(self,currentNode,val):
        if currentNode is None:
            return False
        elif val==currentNode.data:
            return True
        elif val<currentNode.data:
            return self.findNode(currentNode.left,val)
        else:
            return self.findNode(currentNode.right,val)

    def getChildren(self):
        if(self.root is None):
            return False
        else:
            r=self.root.getChildren()
            return r
        
        

b=BST()
b.insert(8)
b.insert(16)
b.insert(4)
b.insert(12)
print (b.getChildren())
            
        
        
        
        
        
        



