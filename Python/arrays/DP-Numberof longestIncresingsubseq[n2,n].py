#for lon incr subseq- j, i are pointers- logic- if arr[j]<arr[i] then ans[i]=max{ans[i],ans[j]+1}
'''
old- ans[i] represents the length of the longest subsequence in a[:i+1] && ended with index i.

new- ans2[i] represents the number of the subsequences which are satisfied the conditions mentioned in above.

I also update the final result, stored in count in the loop.

maxval represents the length of the longest increasing subsequence.

count represents the number of the increasing subsequence with length equals to maxval.

'''
'''biggest difference here compared with longest incre subseq is that we also need to find the number of the longest subsequence. A basic idea is to use another array to memorize the number'''
#Time=O(n^2)
#space=O(n)
def lis(a):
    if len(a)<=1:
        return len(a)
    ans=[1]*(len(a))
    ans2=[1]*(len(a))
    maxval=count=1
    for i in range(1,len(a)):
        for j in range(i):
            if a[i]>a[j]:
                if ans[j]+1>ans[i]:
                    ans[i]=ans[j]+1
                    ans2[i]=ans2[j]
                elif ans[j]+1==ans[i]:
                    ans2[i]+=ans2[j]
        if ans[i]>maxval:
            maxval=ans[i]
            count=ans2[i]
        elif ans[i]==maxval:
            count+=ans2[i]
                    
    return count
 
        
arr = [10, 22, 9, 33, 21, 50, 41, 60]
#arr=[1,3,5,4,7]
print (lis(arr))
