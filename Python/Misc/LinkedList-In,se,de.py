#https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/

class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

        
        
class LL(object):
    def __init__(self,head=None):
        self.head=head

    def insert(self,data):
        if self.head:
            n=Node(data,self.head)
            self.head=n
            
        else:
            self.head=Node(data)

    def search(self,data):
        current=self.head
        while current:
            if current.data==data:
                print ('Found')
            current=current.next
        
    def size(self):
        current=self.head
        count=0
        while current:
            count+=1
            current=current.next
        print (count)
            
           

    def remove(self,data):
        current=self.head
        previous=None
        if current:
            if current.data==data:
                self.head=self.head.next

            else:
                previous=self.head
                current=self.head.next
                while current:
                    if current.data==data:
                        previous.next=current.next
                        current=None
                        return
                    else:
                        previous=current
                        current=current.next
                print ('Not Found')
            

    def print_all(self):
        current=self.head
        
        while current:
            print (current.data)
            current=current.next

        

    
            
           

a=LL()
a.insert(4)
a.insert(5)
a.insert(6)
a.insert(6)
a.size()
a.print_all()

