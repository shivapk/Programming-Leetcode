#Maximum subarray 
#outputs size
#output of [1,2,3,-1] is 6
#time=O(n)
#space=O(n)
class Solution:
    def maxSubArray(self, nums):
        if len(nums)==1:
            return nums[0]
        #using dynamic programming array to represent maximum sum of elements till i th index of input array
        dp=[0]*len(nums)
        dp[0]=num[0]
        # to find maximum of dp array
        maximum=dp[0] 
        for i in range(1,len(nums)):
            dp[i]=nums[i]+(dp[i-1] if dp[i-1]>0 else 0)
            maximum=max(maximum,dp[i])
    
        return maximum
    
#nums=[-2,1,-3,4,-1,2,1,-5,4]
nums=[1,2,3,-1]
s=Solution()
print (s.maxSubArray(nums))
