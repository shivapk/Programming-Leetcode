list=[1,2,4,6,8,9,11,14]


def search(list,k):
    n=len(list)
    if n==0:
        return False
    elif list[n//2]==k:
        return True
    elif list[n//2]>k:
        return search(list[:n//2],k)
    elif list[n//2]<k:
        return search(list[(n//2) +1:],k)
    return False
    
    
print (search(list,11))
          