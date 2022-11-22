class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        part_one = self.rob_house(nums[:len(nums)-1])
        part_two = self.rob_house(nums[1:])
        
        return max(part_one, part_two)
        
        
    
    def rob_house(self, arr):
        print(arr)
        if len(arr)==1:
            return arr[0]
        if len(arr) == 2:
            return max(arr[0], arr[1])
        
        arr[1] = max(arr[0], arr[1])
        
        for i in range(2, len(arr)):
            
            arr[i] = max(arr[i]+arr[i-2], arr[i-1])
            
            
        return arr[len(arr)-1]