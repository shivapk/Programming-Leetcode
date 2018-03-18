#CREATION OF LINKED LIST
class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
        
class Linked_list:
    def __init__(self):
        self.head=None
        
    def insert(self,val):
        temp=Node(val)
        if self.head==None:
            self.head=temp
            return True
        temp.next=self.head
        self.head=temp
        return True
    
    def print_list(self):
        temp=self.head
        while temp:
            print (temp.val,end=' ')
            temp=temp.next
            
    def search(self,x):
        temp=self.head
        while temp:
            if temp.val==x:
                return True
            temp=temp.next
        return False
    
    def delete(self,x):
        curr=self.head
        prev=None
        if curr.val==x:
                self.head=curr.next
                return True
        prev=curr
        curr=curr.next
        while curr:
            if curr.val==x:
                prev.next=curr.next
                return True
            prev=curr
            curr=curr.next
        return False
    
    def reverse(self):
        curr=self.head
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        self.head=prev
                  
ll=Linked_list()
ll.insert(5)
ll.insert(6)
ll.insert(7)
#ll.print_list()
print(ll.search(6))
print(ll.reverse())
ll.print_list()

