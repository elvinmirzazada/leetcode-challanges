class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 1
        
#         dp = [1] * len(nums)
        
#         for i in range(1, len(nums)):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], 1 + dp[j])
                
#         return max(dp)

        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        
        return len(sub)