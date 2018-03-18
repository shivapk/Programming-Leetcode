#Serialization is to store tree in a file so that it can be later restored. The structure of tree must be maintained. Deserialization is reading tree back from file.
#Time: O(n) #just tree traversal
#space: O(n) # ans array storing preorder results
from collections import defaultdict
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def serialize(self, root):
        ans = []
        self.encode(root,ans)
        return ' '.join(ans)
    
    def encode(self,root,ans):  #preorder traversal
        if root is None:
            ans.append('*')  #leaves childs
        else:
            ans.append(str(root.val))
            self.encode(root.left,ans)
            self.encode(root.right,ans)

    def deserialize(self, inp_string):
        arr = inp_string.split() #split based on space or use self.vals=iter(data.split()) and no need to pass vals in decode
        root=self.decode(arr)
        return root
    
    def decode(self,arr):
            val = arr.pop(0)  #or use val=next(self.vals)
            if val == '*':
                return None
            node = Node(int(val))
            node.left = self.decode(arr)
            node.right = self.decode(arr)
            return node
                                
root =  Node(15)
root.left = Node(10)
root.left.right=Node(12)
root.right = Node(20)
root.left.left = Node(8)
root.left.left.right=Node(6)
root.left.right = Node(12)
root.right.right = Node(25)
s=Solution()
print (s.deserialize(s.serialize(root)).val)
