#length of longest increasing sub sequence
#j, i are pointers- logic- if arr[j]<arr[i] then dp[i]=max{dp[i],dp[j]+1}
#till every index i of array check from start of array with j
#Time=O(n^2)
#space=O(n)
def lis(arr):
    if len(arr)<=1:
        return len(arr)
    dp=[1]*(len(arr)) #tells length of largest incresing sequence at index i of array
    for i in range(len(arr)):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i]=max(dp[i],dp[j]+1)
                
    return max(dp)
        
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print (lis(arr))
