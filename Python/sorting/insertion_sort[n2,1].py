#Insertion sort
#Time==O(n2)
#space=O(1)
def insertionSort(a):
    for i in range(1,len(a)):
        for j in range(i,0,-1):
            if a[j]<a[j-1]:
                a[j],a[j-1]=a[j-1],a[j]
            else:
                break
                
    return a
    
    
l=[4,3,2,1]
print insertionSort(l)