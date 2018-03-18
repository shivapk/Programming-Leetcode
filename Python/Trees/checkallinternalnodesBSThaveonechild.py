

def check(arr):
    max=min=arr[-1]
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>max:
            max=arr[i]
        elif arr[i]<min:
            min=arr[i]
        else:
            return False
                
    return True
        

arr=[9, 8, 5, 7, 6]
print (check(arr))
