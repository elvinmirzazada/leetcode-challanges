class Solution:
    def findMin(self, nums: List[int]) -> int:
        self.result = nums[0]
        self.c_binary_search(nums, 0, len(nums)-1)
        return self.result
        
    def c_binary_search(self, arr, i, j):
        if j >= i:
            if arr[i] < arr[j]:
                self.result = min(self.result, arr[i])
            else:
                mid = (i + j) // 2
                self.result = min(self.result, arr[mid]) 
                if arr[mid] >= arr[i]:                 
                    self.c_binary_search(arr, mid + 1 , j)
                else:
                    self.c_binary_search(arr, i, mid - 1)