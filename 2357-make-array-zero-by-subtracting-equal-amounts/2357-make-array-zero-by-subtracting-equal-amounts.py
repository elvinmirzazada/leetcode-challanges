class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        curr = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] > curr:
                curr = nums[i]
                result += 1    
        return result
        
        
        
# 0 1 3 5 5 


# 2 4 5 6 7