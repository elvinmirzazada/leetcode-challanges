class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dp = nums.copy()

        dp = sorted(dp)
        
        k = 0
        for i in range(0, len(dp), 2):
            nums[i], dp[k] = dp[k], nums[i]
            k += 1

        k = len(nums)-1
        for j in range(1, len(dp), 2):
            nums[j], dp[k] = dp[k], nums[j]
            k -= 1