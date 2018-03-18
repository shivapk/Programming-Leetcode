#https://www.youtube.com/watch?v=YlgPi75hIBc
'''
The worst case time complexity of search and insert operations is O(h) where h is height of Binary Search Tree. In worst case, we may have to travel from root to the deepest leaf node. The height of a skewed tree may become n and the time complexity of search and insert operation may become O(n).

Time= O(h)
Space=O(h)

'''
class Node(object):
    def __init__(self,val):
        self.value=val
        self.leftChild=None
        self.rightChild=None

    def insert(self,data):
        if self.value==data:   #we assume no duplicates
            return False
        elif self.value>data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild=Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild=Node(data)
                return True

    def find(self,data):
        if self.value==data:
            return True
        elif self.value>data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False

        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print (self.value)
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print (self.value)
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            
            if self.rightChild:
                self.rightChild.postorder()
            print (self.value)

                

class Tree(object):
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root=Node(data)
            return True

    def find(self,data):
        if self.root:
            return self.root.find(data)

        else:
            return False

    def preorder(self):
        print ('PredOrder')
        self.root.preorder()
        

    def inorder(self):
        print ('InOrder')
        self.root.inorder()
        

    def postorder(self):
        print ('PostOrder')
        self.root.postorder()


bst=Tree()
bst.insert(10)
bst.insert(5)
bst.insert(9)
bst.insert(100)
bst.insert(32)
bst.insert(1)
bst.insert(4)
bst.insert(8)
bst.preorder()
bst.inorder()
bst.postorder()
    
        
            
        
        
        
        
        
        



