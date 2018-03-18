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
h.insert('Bob', '567-8888')
h.insert('Ming', '293-6753')
h.insert('Ming', '333-8233')
#h.insert('Ankit', '293-8625')
h.insert('Aditya', '852-6551')
#h.insert('Alicia', '632-4123')
#h.insert('Mike', '567-2188')
#h.insert('Aditya', '777-8888')
#h.print()
h.delete('Bob')
h.delete('Ming')
h.delete('Aditya')
h.print()
#print('Ming: ' + h.find('Ming'))