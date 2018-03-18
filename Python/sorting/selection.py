#Selection sort
#time=O(n^2)
#space=O(1)
def selectionsort(l):
  for j in range(len(l)-1):
    min=l[j]
    
    
    for i in range(j+1,len(l)):
       
        
        if min>l[i]:
            min=l[i]
            a=i
    l[l.index(min)],l[j]=l[j],l[l.index(min)]
  return l
    
            
          
a=[9,8,7,6,5,4,3,2,1] 
 
print (selectionsort(a))
    