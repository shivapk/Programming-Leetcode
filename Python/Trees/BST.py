class Node():
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

   
def insert(root,value):
    if root is None:
         temp=Node(value)
         root=temp
         return True
    else:
        if root.value>value:
            if root.left:
                insert(root.left,value)

            else:
                root.left=Node(value)
                
        else:
            if root.right:
                insert(root.right,value)

            else:
                root.right=Node(value)
    return True

def search(root,value):
    if root is None:
        return False
    elif (root.value)==value:
        return True
        
    elif root.value>value:
            root.left.search(value)
    else:
        root.right.search(value)

    return True

def inordersuccessor(current):   #minimum value node
    while current.left:
        current=current.left
    return current

def delete(root,value):
    #root is None
    if root is None:
        return False
    #data is in the root node
    elif (root.value)==value:
        #both its childs are empty
        if root.left is None and root.right is None:
            self.root=None
            return True
        #only left child exists
        elif root.left and root.right is None:
            root=root.left
            return True
        #only right child exists
        elif root.right and root.left is None:
            root=root.right
            return True
        #both left and right childs exists
        else:
            temp=inordersuccessor(self,self.root.right)
            root.value=temp.value
            root.right.delete(value)
    #data is in the left of the root
        
    elif root.value>value:
            root.left.delete(value)
    #data is in the right of the root
    else:
        root.right.delete(value)
        
    return True

# to check whether insert, delete operations are correct
def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.value)
        inorder(root.right)
        
    
r=Node(4)
insert(r,2)
insert(r,3)
insert(r,40)
insert(r,54)
insert(r,15)
insert(r,20)
inorder(r)


                    
        
