class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        return self.rec_find(nums)
        
    def rec_find(self, arr):
        if len(arr) == 1:
            return arr[0]
        
        new_arr = []
        for i in range(len(arr)-1):
            new_arr.append((arr[i] + arr[i+1]) % 10)
        
        return self.rec_find(new_arr)