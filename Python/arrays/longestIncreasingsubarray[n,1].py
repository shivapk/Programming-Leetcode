#we have to simply find longest increasing subarray 
#logic-we can make one pass of the array and keep track of the current streak #of increasing elements, reset it when it does not increase.
#Time: O(n) as we are traversing array once
# Space: O(1)
def lcis(arr):
    if len(arr)==0:
        return 0
    temp_length=1 #for length of longest increase sub array at different instants of time.
    m=1 #max increasing subarray length
    
    for i in range(1,len(arr)): #start from 2nd element
        if arr[i]>arr[i-1]:
            temp_length+=1
        else:
            if m<temp_length:
                m=temp_length
      #again the length of the new increasing subarray is going to be calculated  
            temp_length=1
    #comparing the length of the last increasing subarray with max which is m    
    if m<temp_length:
        m=temp_length
    
    return m
            

arr = [3, 6, 4, 8, 12, 9, 11, 14, 7]
print (lcis(arr))

'''
#print that largest subarray
#We can print the subarray by keeping track of index with largest length.
#Time: O(n) as we are traversing array once
# Space: O(1)
def lcis(arr):
    if len(arr)==0:
        return 0
    temp_length=1 #for length of longest increase sub array at different instants of time.
    m=1 #max increasing subarray length
    start_index=0 ##########CHANGE-1###############  #to know from which index that max subarray is starting
    for i in range(1,len(arr)): #start from 2nd element
        if arr[i]>arr[i-1]:
            temp_length+=1
        else:
            if m<temp_length:
                m=temp_length  
                #index assign the starting index of longest increasing subarray.
                start_index=i-m         #########################CHANGE-2################
      #again the length of the new increasing subarray is going to be calculated  
            temp_length=1
  #comparing the length of the last increasing subarray with max which is m    
    if m<temp_length:
        m=temp_length
        start_index=n-m                    #####################CHANGE-3########################
    
    return arr[start_index:m+start_index]       ###################CHANGE-4####################
            

arr = [5, 6, 3, 5, 7, 8, 9, 1, 2]
print (lcis(arr))
'''
