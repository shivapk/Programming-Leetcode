def MergeSort(A):
    r=(len(A))//2
    #print (r)
    if r<1:
        return A
    L=MergeSort(A[0:r])
    R=MergeSort(A[r:])
    
    return Merge(L,R)

def Merge(L,R):
    l=[]  # should be of the size n
    i=j=k=0
    while (i<len(L) and j<len(R)):
        if L[i]<=R[j]:
            l.append(L[i])
            i=i+1
        else:
            
            l.append(R[j])
            j=j+1
        k=k+1
    while (i<len(L)):
        l.append(L[i])
        i=i+1
        k=k+1
    while (j<len(R)):
        l.append(R[j])
        j=j+1
        k=k+1
        
    return l


print (MergeSort([6,5,4,3,2,1]))
    


    


    




    





