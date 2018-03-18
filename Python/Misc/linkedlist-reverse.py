class Node():
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
        
class list():
    def __init__(self):
        self.head=None
        self.size=0
    def insert(self,value):
         temp=Node(value,self.head)
         self.head=temp
         self.size+=1
         
    def delete(self,value):
         this_node=self.head
         prev_node=None
         while this_node:
             if (this_node.value==value):
                  if prev_node:
                     prev_node.next=this_node.next
                  else:
                     self.head=this_node.next
                  self.size-=1
                  return True
             else:
                prev_node=this_node
                this_node=this_node.next
                
         return False
         
    def find(self,value):
        this_node=self.head
        while this_node:
            if (this_node.value==value):
                return True
            else:
                this_node=this_node.next
        return False
     
    def print(self):
         this_node=self.head
         while this_node:
             print(this_node.value, end='->')
             this_node=this_node.next
         print ('None')
         return 
         
    def reverse(self):
        this_node=self.head
        prev_node=None
        while this_node:
             up_next=this_node.next
             this_node.next=prev_node
             prev_node=this_node
             this_node=up_next
        self.head=prev_node
            
                
l=list()
l.insert(2)
l.insert(6)
l.insert(8)
l.insert(12)
l.reverse()
l.print()

                
        
                     
         
        
    
