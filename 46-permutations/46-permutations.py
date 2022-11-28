class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = {i: False for i in range(len(nums))}
        
        
        
        
        def backtracking(nums, permutation):

            if len(permutation) == len(nums):
                result.append(permutation.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    permutation.append(nums[i])
                    backtracking(nums, permutation)
                    permutation.pop()
                    used[i] = False
                    
                    
                    
        backtracking(nums, [])
        return result