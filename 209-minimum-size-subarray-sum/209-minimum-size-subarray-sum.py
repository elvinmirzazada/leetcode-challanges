class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        curr_sum = 0
        start = 0
        
        idx = 0
        while idx < len(nums):
            
            
            if curr_sum >= target:
                min_len = min(min_len, idx-start+1)
                curr_sum -= nums[start]
                start += 1
            else:
                curr_sum += nums[idx]
            
            if curr_sum < target:
                idx += 1
                
        return min_len if min_len < float('inf') else 0
        