'''
length of longest increasing sub sequence
Note that we are dealing with end elements only.
open geeks for geeks parallelly 
http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
The loop runs for N elements. In the worst case, we may end up querying ceil value using binary search for many A[i].
Therefore, T(n) = O(N log N).
space=O(N) for storing ans array
'''
def lis(a):
    if len(a)==0:
        return 0
    ans=[]  #stores end values of sequences [3,4,7,9,11,14] but not sequence
    ans.append(a[0])
    for i in range(1,len(a)):
        print (a[i])
        if a[i]<ans[0]: #new smallest value
            ans[0]=a[i]
            print (ans)
        elif a[i]>ans[-1]: #A[i] wants to extend largest subsequence
                ans.append(a[i])
                print (ans)
                
        else:
            #A[i] wants to be current end candidate of an existing subsequence. 
            #It will replace ceil value in ans
            curr=binarysearch(ans,a[i])
            ans[curr]=a[i]
            print (ans)
    return len(ans)
            
def binarysearch(ans,val):
    end=len(ans)-1
    start=-1
    while end-start > 1:
        mid = start + (end - start)//2
        if ans[mid]>=val:
            end = mid
        else:
            start = mid
    return end

arr = [3, 6, 4, 8, 12, 9, 11, 14, 7]
print (lis(arr))
