class Node():
    def __init__(self,key,value,next=None):
        self.key=key
        self.value=value
        self.next=next
    
class HashMap():
     def __init__(self,size):
         self.size=size
         self.array=[None]*(self.size)
         
     def find_hash(self,key):
         sum=0
         for char in key:
             sum+=ord(char)
         return (sum%(self.size))
      
     def insert(self,key,value):
         hash=self.find_hash(key)
         #key_value=[key,value]
         if (self.array[hash]==None):
             self.array[hash]=Node(key,value)  
             return True
         else:
             temp=self.array[hash]
             while temp.next!=None:
                 if temp.key==key:
                     temp.value=value
                     return True
                 else:
                    temp=self.array[hash].next
             if temp.key==key:
                 temp.value=value
                 return True
             temp.next=Node(key,value)
             return True 
     def find(self,key):
         hash=self.find_hash(key)
         if self.array[hash] is not None:
             temp=self.array[hash]
             while temp:
                  if temp.key==key:
                      return (temp.value)
                  temp=temp.next
         return False
      
     def delete(self,key):
         hash=self.find_hash(key)
         if self.array[hash] is not None:
             temp=self.array[hash]
             prev=None
             while temp:
                 if temp.key==key:
                     if prev:
                        prev.next=temp.next
                     else:
                        self.array[hash]=temp.next
                     return True
                 temp=temp.next
         
         return False
         
     def print(self):
         for i in range(len(self.array)):
                 temp=self.array[i]
                 while temp:
                     print (temp.key, temp.value)
                     temp=temp.next
             
             
    
    
    
h=HashMap(8)
h.insert('alpha', '1234')
h.insert('beta', '5678')
h.insert('gamma', '910112')
h.insert('delta', '131415')
h.print()
h.delete('beta')
h.delete('alpha')
h.print()
