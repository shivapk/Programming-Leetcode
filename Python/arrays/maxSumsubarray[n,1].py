#Maximum sum subarray 
#outputs size
#output of [1,2,3,-1] is 6
#time=O(n)
#space=O(1)
#Basically, keep adding each integer to the sequence until the sum drops below 0.
#If sum is negative, then should reset the sequence.
class Solution:
    def maxSubArray(self, nums):
        ans=nums[0]
        s=0 #sum
        for i in range(len(nums)):
            s+=nums[i]
            ans=max(s,ans) #to decide whether to add or not
            s=max(s,0)
            
        return ans
    
#nums=[-2,1,-3,4,-1,2,1,-5,4]
nums=[1,2,3,-1]
s=Solution()
print (s.maxSubArray(nums))
