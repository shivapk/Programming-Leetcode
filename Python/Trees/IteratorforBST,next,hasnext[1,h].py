# Binary Search Tree Iterator, Calling next() will return the next smallest number in the BST.
#When next() be called, I pop one element and process its right child as new root.
#Time: O(1) for hasNext(), O(h) for next() [in average O(1) time, which means amortized over all the next() calls]
#Space: O(h) memory, where h is the height of the tree.-> q stores elements

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def __init__(self, root):
        self.q=[]  #elements in this queue are in descending order anytime ex.[10,7,6]
        self.fillwithleft(root)  #to make q filled up with all left side elements

     # return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.q != [] #if q is empty then return False

    # return an integer, the next smallest number
    def next(self):
        curr = self.q.pop() #pop minimum element every time[last element will be the minimum)
        self.fillwithleft(curr.right)  #to add next largest values than curr for 5 we add 7,6 so that 6 becomes the least next time.
        return curr.val

    def fillwithleft(self,root):
        while root:
            self.q.append(root)
            root=root.left


root=Node(10)
root.left=Node(5)
root.left.left=Node(4)
root.left.right=Node(7)
root.left.right.left=Node(6)
root.left.right.right=Node(9)
root.right=Node(14)
root.right.left=Node(12)
root.right.right=Node(16)
i= Solution(root)
elements=[]
while i.hasNext(): # if root is None hasNext() returns false so this loop will not run
    elements.append(i.next())
    
print (elements)
