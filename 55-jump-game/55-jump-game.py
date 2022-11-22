class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_el = 0
        i = 0
        while i <= max_el:
            max_el = max(max_el, i+nums[i])
            if max_el >= n -1:
                return True
            i+=1
        return False
            
#         dp = [-1] * len(nums)
        
#         dp[len(dp)-1] = 1
        
#         for i  in range(len(nums)-2, -1, -1):
#             further_jump = min(i+nums[i], len(nums)-1)
#             for j in range(i+1, further_jump+1):
#                 if dp[j] == 1:
#                     dp[i] = 1
#                     break

# -----------------------------
#             if dp[i] == 1:
#                 continue
#             if i > 0 and dp[i-1] == -1:
#                 continue
#             if nums[i] > 0 and dp[i] > -1:   
#                 for j in range(nums[i]+1):

#                     if j+i < len(nums):

#                         dp[i+j] = 1
        # print(dp)        
        return dp[0] == 1