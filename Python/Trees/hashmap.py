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
         key_value=[key,value]
         if (self.array[hash]==None):
             self.array[hash]=[key_value]  
             return True
         else:
             for pair in self.array[hash]:
                 if pair[0]==key:
                     pair[1]==value
                     return True
             self.array[hash].append(key_value)
             return True 
     def find(self,key):
         hash=self.find_hash(key)
         if self.array[hash] is not None:
             for pair in self.array[hash]:
                  if pair[0]==key:
                      return pair[1]
         return False
      
     def delete(self,key):
         hash=self.find_hash(key)
         if self.array[hash] is not None:
             for index in range(0,len(self.array[hash])):
                 if self.array[hash][index][0]==key:
                     del self.array[hash][index]
                     return True
         return False
         
     def print(self):
         for item in self.array:
             if item is not None:
                 print (item)
             
             
    
    
    
h=HashMap(8)
h.insert('alpha', '1234')
h.insert('beta', '5678')
h.insert('gamma', '910112')
h.insert('delta', '131415')
h.print()
h.delete('beta')
h.delete('alpha')
h.print()
