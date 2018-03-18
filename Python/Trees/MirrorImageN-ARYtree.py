class Node:
    def __init__(self,data):
        self.data=data
        self.child=[]
    

def mirror(root):
    if root is None:
        return 
    if len(root.child)<2:
        return
    for i in range(len(root.child)):
        mirror(root.child[i])
     
    root.child.reverse()
    
        
def inorder(root,ans):
    if root:
        inorder(root.left,ans)
        ans.append(root.data)
        inorder(root.right,ans)
    return ans
        
def traversal(root):
    if root is None:
        return 
    queue=[]
    queue.append(root)
    while queue:
        l=len(queue)
        while (l>0):
            node=queue.pop(0)
            queue=queue+node.child
            print (node.data,end=' ')
            l-=1
  
        print ('')
            
            
        
root=Node(10)
root.child.append(Node(2))
root.child.append(Node(34))
root.child.append(Node(56))
root.child.append(Node(100))
root.child[2].child.append(Node(1))
root.child[3].child.append(Node(7))
root.child[3].child.append(Node(8))
root.child[3].child.append(Node(9))


traversal(root)
mirror(root)
print ('------------')
traversal(root)


    
    
