#Time=O(n2)
#space=O(logn)

def quicksort(A,start,end):
    if start<end:
        #print (a)
        pivot=partition(A,start,end)
        quicksort(A,start,pivot-1)
        quicksort(A,pivot+1,end)
    else:
        return -1
    
def partition(A,start,end):
    pi=A[end]
    j=start-1
    for i in range(start,end):    #high is len(A)-1
        if A[i]<=pi:
            j=j+1
            A[j],A[i]=A[i],A[j]
            
    #print (pi, A[end])
    A[j+1],A[end]= A[end],A[j+1]
    return j+1


a=[9,6,5,0,8,2,4,7]
quicksort(a,0,7)
print (a)
#print (partition([9,6,5,0,8,2,4,7]))
#print (partition([9,19,13,5,12,8,7,4,21,2,6,11]))

            
        
    


    


    




    





