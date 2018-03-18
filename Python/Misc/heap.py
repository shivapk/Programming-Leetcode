def left(i):
  return (2*i+1)

def right(i):
  return (2*i+2)
  
def parent(i):
  return ((i-1)//2)

class minheap:
  def __init__(self):
    self.harr=[]
    
  def insert(self,val):
    self.harr.append(val)
    self.minheapify(len(self.harr)-1)
    
  def delete_val(self,i):
    temp=self.harr[i]
    self.harr[i]=self.harr[-1]
    del self.harr[-1]
    if (i>=(len(self.harr)//2)):
      return
    self.minheapify(i)
    
  def decrease_key(self,i,newval):
    self.harr[i]=newval
    self.minheapify(i)
    
  def extract_min(self):
    temp=self.harr[0]
    self.harr[0]=self.harr[-1]
    del self.harr[-1]
    self.minheapify(0)
    print (temp)
    
  def get_min(self):
    print (self.harr[0])
    
  def minheapify(self,i):
    l=left(i)
    r=right(i)
    p=parent(i)
    if (i>0 and self.harr[i]<self.harr[p]):
      self.harr[i],self.harr[p]=self.harr[p],self.harr[i]
      self.minheapify(p)
    elif (i<(len(self.harr)//2) and r<len(self.harr) and self.harr[i]>min(self.harr[l],self.harr[r])):
      if (l<len(self.harr) and self.harr[l]<=self.harr[r]):
        self.harr[p],self.harr[l]=self.harr[l],self.harr[p]
        self.minheapify(l)
      elif (r<len(self.harr) and self.harr[r]<self.harr[l]):
        self.harr[p],self.harr[r]=self.harr[r],self.harr[p]
        self.minheapify(r)
        
h=minheap()
h.insert(3)
h.insert(2)
h.delete_val(1)
h.insert(15)
h.insert(5)
h.insert(4)
h.insert(45)
h.extract_min()
h.get_min()
h.decrease_key(2, 1)
h.get_min();
    
        
  
    
        
        
        
    
    
    
    
    