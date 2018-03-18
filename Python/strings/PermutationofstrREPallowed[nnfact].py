#Time=O(n*n!) Note that there are n! permutations and it requires O(n) time for each permutation.
#Space=O(n) as the depth of the tree will be n
#duplicates allowed
#if you dont want duplicates instead of array use set or check in the array before adding
def solution(arr,l,r,ans):
    if l==r:
        #if ''.join(arr) not in ans: this is to check duplicates
            ans.add((''.join(arr))) 
    else:
        for i in range(l,r+1):
            arr[i],arr[l]=arr[l],arr[i]
            solution(arr,l+1,r,ans)
            arr[i],arr[l]=arr[l],arr[i]
    return ans
                        
#S=''
S='aa'
ans=set()
#ans=[]
print (solution(list(S),0,len(S)-1,ans))
