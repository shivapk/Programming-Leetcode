#merge sort for linked list


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LL:
    def __init__(self):
        self.head=None
        
    def insert(self,data):
        if self.head:
            temp=Node(data)
            temp.next=self.head
            self.head=temp
        else:
            self.head=Node(data)
    
def plist(node):
        temp=node
        while temp:
            print ((temp.data),end=' ')
            temp=temp.next
            
def getmid(head):
        mid=end=head
        while end.next and end.next.next:
            end=end.next.next
            mid=mid.next
        return mid
            
            
def msort(llist):
    
    if llist and llist.next: #llist is of type Node
        mid=getmid(llist)
        temp=mid.next
        mid.next=None
        llist1=msort(llist)
        llist2=msort(temp)
        return merge(llist1,llist2)
    else:
        return llist
    
def merge(l1,l2):   #l1,l2 are of type Node
    ans=None
    if l1==None:
        return l2
    if l2==None:
        return l1
        
    if l1.data<=l2.data:
        ans=l1
        ans.next=merge(l1.next,l2)
    else:
        ans=l2
        ans.next=merge(l1,l2.next)
    return ans


l=LL()
l.insert(9)
l.insert(5)
l.insert(4)
l.insert(-11)
retl=msort(l.head)
if retl:
    plist(retl)
else:
    print ('Empty List')
