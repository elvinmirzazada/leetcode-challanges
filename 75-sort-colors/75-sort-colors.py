class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, 1
        
        while p2 < len(nums):
            if nums[p1] > nums[p2]:
                
                nums[p1], nums[p2] = nums[p2], nums[p1]
                
            p2 += 1
            if p2 >= len(nums):
                p1 += 1
                p2 = p1 + 1
                    
           
        
        
                
        
        